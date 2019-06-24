# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: generateParse.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-10-31 19:03:03
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-17 10:26:43
"""
Descripition:
	HLCL SM 3.3
	Generate random parses as candidates
	Input:a graph from Image2graph.py
	Output:
		candidate parses
			Prase=[stroke_c] #a list of stroke_m
			
			storke_c=[node] #a list of node from the given graph
			
	there must be some funtion by which
		stroke_c can be transformed to
			 	trajectory_c [[xi,yi]]
Env:
    python 2.7 ,numpy,copy,networkx 2.2

Unit test:
	a toy graph created by function creat_toy_graph
        
    just run this file

Change Activity:



"""
import networkx as nx 
import numpy as np
import copy
def creat_toy_graph():
    edgelist = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                 (6, 7), (7, 8), (4, 8), (4, 9)]
    nodelist=range(1,10)
    nodelocationlist=[(1,4),(1.5,3.5),(1,3),(2,3),(3,3),(3,4),(2.5,4.2),(2,3.5),(2,1.5)]
    ToyG = nx.Graph()
    ToyG.add_nodes_from(nodelist)
    ToyG.add_edges_from(edgelist)
    for (i,node) in enumerate(nodelist):
        print i,node,ToyG.nodes[1]
        ToyG.nodes[node]['Location']=nodelocationlist[i]
    for (x,y) in edgelist:
        ToyG.edges[x,y]['isunused']=True

    #print len(ToyG.edges),ToyG.edges[1,2],ToyG.edges[2,1]

    return ToyG


class PenWalker():
    """docstring for """

    def __init__(self, graph):
        
        self.orginalgraph=graph
        for edge in self.orginalgraph.edges:
            self.orginalgraph.edges[edge]['isunused']=True
        #hyper para
        print 'nodes',self.orginalgraph.nodes
        self.testmode=True
        if self.testmode:print 'Testmode open'
        self.parseterminalnum = 10
        self.stroketerminalnum = 10
        self.costnodeconstant=0.4
        self.costpickupconstant=2
        #Output
        self.parsesset = set()
        self.strokesset = set()
        #Other
        self.currentactiondict={}
    def countAllUnusedEdges(self):
        for (x,y) in self.graph.edges:
            if self.graph.edges[x,y]['isunused']:
                return True
        return False
    def countUnusedEdges(self,node):
        count=0
        for neighbor in self.graph.neighbors(node):
            if self.graph.edges[neighbor,node]['isunused']:
                count=count+1
        return count
    def __call__(self):

        while len(self.parsesset) <= self.parseterminalnum and len(self.strokesset) < self.stroketerminalnum:
            
            self.graph=copy.deepcopy(self.orginalgraph)
            self.currentstroke=[]
            self.currentparse=[]
            self.currentnode=None
            self.last_node=None
            self.last_edgevector=None


            self.currentnode=self.sampleNodeFromUniform(list(self.graph.nodes))
            self.currentstroke.append(self.currentnode)
            step=1
            if self.testmode:print '[STEP]:',step,'currentnode:',self.currentnode
            while self.countAllUnusedEdges():
                #generate a parse
                if self.last_node is not None:                    
                    #self.currentactiondict['retrace']=np.pi/2
                    self.currentactiondict['pickup']=np.pi/4
                    if self.countUnusedEdges(self.last_node)==0:
                        self.currentactiondict['retrace']=np.pi/2
                self.calculateCost()
                action=self.sampleActionByCost()
                self.doAction(action) 
                step=step+1
                if self.testmode:print 'cur_stroke',self.currentstroke,'cur_parse',self.currentparse
                if self.testmode:print '[STEP]:',step,'currentnode:',self.currentnode
                self.currentactiondict={}

            if self.testmode:print  'RESULT-A-Parse:',self.currentparse
            curpar=tuple(tuple(p) for p in self.currentparse)

            self.parsesset.add(curpar)
            self.currentparse=[]
        return self.parsesset,self.strokesset

    def calculateCost(self):
        
        for i in self.graph.neighbors(self.currentnode):

            
            if self.graph.edges[i,self.currentnode]['isunused']:
                #Toy angle 
                edgevector=np.array(self.graph.nodes[i]['Location'])\
                           -np.array(self.graph.nodes[self.currentnode]['Location'])
                if self.last_edgevector is None:
                    lastedgevector=edgevector
                else:
                    lastedgevector=self.last_edgevector
                self.currentactiondict[i]=abs(np.angle(complex(edgevector[0],edgevector[1])\
                                            /complex(lastedgevector[0],lastedgevector[1])))
                #if self.testmode:print self.currentactiondict
        print 'actionlist',self.currentactiondict,self.currentactiondict.items()
        actionlist=self.currentactiondict.keys()
        actioncost=self.currentactiondict.values()
        # actionlist,actioncost=self.currentactiondict.items()
        print actionlist,actioncost
    def sampleActionByCost(self):
        if self.testmode:print 'action_cost_list(angle):',self.currentactiondict
        # actionlist,actioncost=self.currentactiondict.items()

        actionlist=list(self.currentactiondict.keys())
        actioncost=list(self.currentactiondict.values())
        actionprob_unnorm=np.array([self.cost2prob(i) for i in actioncost])
        #if self.testmode:print actionlist,actionprob_unnorm.sum()
        action=actionlist[np.random.choice(range(len(actionlist)),1,p=actionprob_unnorm/actionprob_unnorm.sum())[0]]
        #if self.testmode:print action,type(action),type(self.currentnode)
        return action
    def cost2prob(self,angle):

        return np.e**(-self.costnodeconstant*angle)

    def sampleNodeFromUniform(self,nodelist): 
        return nodelist[np.random.randint(len(nodelist))]

    def pickup_new_node(self):
        nodelist=[]
        newedgescount=[]
        for node in self.graph.nodes:
            if node != self.currentnode:
                count=self.countUnusedEdges(node)
                if count>0:
                    nodelist.append(node)
                    newedgescount.append(count)
        prob=np.power(np.array(newedgescount)*1.,-(self.costpickupconstant))
        print prob,np.power
        prob=prob/prob.sum()  
        newnode=nodelist[np.random.choice(range(len(nodelist)),1,p=prob)[0]]
        print 'picknodelist',nodelist ,newedgescount,prob
        return newnode
    def doAction(self, action):
    	if action == 'pickup':
            
            newnode=self.pickup_new_node()
            if self.testmode:print 'Action:pickup',newnode
            #newnode=newnode.astype(np.int32)
            self.strokesset.add(tuple(self.currentstroke))
            self.currentparse.append(self.currentstroke)
            self.currentstroke=[]
            self.last_node=None
            self.currentnode=newnode
            self.currentstroke.append(newnode)
        elif action == 'retrace':
            if self.testmode:print 'Action:retrace',action
            newnode=self.last_node
            self.currentstroke.append(newnode)
            self.last_edgevector=np.array(self.graph.nodes[newnode]['Location'])\
                       -np.array(self.graph.nodes[self.currentnode]['Location'])
            self.last_node=self.currentnode
            self.currentnode=newnode

        else:
            if self.testmode:print 'Action:move',action

            newnode=action
            self.graph.edges[newnode,self.currentnode]['isunused']=False
            if self.testmode:print 'edgestate',self.graph.edges[newnode,self.currentnode]['isunused']
            #if self.testmode:print type(newnode),type(self.currentnode)
            self.currentstroke.append(newnode)
            self.last_edgevector=np.array(self.graph.nodes[newnode]['Location'])\
                       -np.array(self.graph.nodes[self.currentnode]['Location'])
            self.last_node=self.currentnode
            self.currentnode=newnode
        self.currentactiondict={}
 


if __name__ =='__main__' :
    Graph=creat_toy_graph()
    #print Graph.nodes[1]['Location']
    penwalker=PenWalker(Graph)
    a,b=penwalker()
    print 'final result_Parseset:'
    print a
    print 'final result_Strokeset:'
    print b
