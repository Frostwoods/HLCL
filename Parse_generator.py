# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Parse_generator.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-10-31 19:03:03
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-13 15:08:49
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
    for i in nodelist:
        #print i,nodelocationlist[i-1]
        ToyG.nodes[i]['Location']=nodelocationlist[i-1]
    for (x,y) in edgelist:
        ToyG.edges[x,y]['isunused']=True

    #print len(ToyG.edges),ToyG.edges[1,2],ToyG.edges[2,1]

    return ToyG


class Penwalker():
    """docstring for """

    def __init__(self, graph):
        
        self.orginal_graph=graph
        
        #hyper para
        self.testmode=True
        if self.testmode:print 'Testmode open'
        self.parse_terminal_num = 10
        self.stroke_terminal_num = 10
        self.cost_node_constant=0.4
        self.cost_pickup_constant=2
        #Output
        self.parses_set = set()
        self.strokes_set = set()
        #Other
        self.current_action_dict={}


    def __call__(self):

        while len(self.parses_set) <= self.parse_terminal_num and len(self.strokes_set) < self.stroke_terminal_num:
            
            self.graph=copy.deepcopy(self.orginal_graph)
            self.current_stroke=[]
            self.current_parse=[]
            self.current_node=None
            self.last_node=None
            self.last_edgevector=None


            self.current_node=self.uniform_choice_node(list(self.graph.nodes))[0]
            self.current_stroke.append(self.current_node)
            step=1
            if self.testmode:print '[STEP]:',step,'current_node:',self.current_node
            while self.count_all_unused_edges():
                #generate a parse
                if self.last_node is not None:                    
                    #self.current_action_dict['retrace']=np.pi/2
                    self.current_action_dict['pickup']=np.pi/4
                    if self.count_unused_edges(self.last_node)==0:
                        self.current_action_dict['retrace']=np.pi/2
                self.cost_calculate()
                action=self.select_action_by_cost()
                self.action_perform(action)
                if self.testmode:print 'cur_stroke',self.current_stroke,'cur_parse',self.current_parse
                step=step+1
                if self.testmode:print '[STEP]:',step,'current_node:',self.current_node
                self.current_action_dict={}

            if self.testmode:print  'RESULT-A-Parse:',self.current_parse
            curpar=tuple(tuple(p) for p in self.current_parse)

            self.parses_set.add(curpar)
            self.current_parse=[]
        return self.parses_set,self.strokes_set

    def cost_calculate(self):
        
        for i in self.graph.neighbors(self.current_node):
            #print i,self.graph.nodes[i]
            if self.graph.edges[i,self.current_node]['isunused']:
                edgevector=np.array(self.graph.nodes[i]['Location'])\
                           -np.array(self.graph.nodes[self.current_node]['Location'])
                if self.last_edgevector is None:
                    lastedgevector=edgevector
                else:
                    lastedgevector=self.last_edgevector
                self.current_action_dict[i]=abs(np.angle(complex(edgevector[0],edgevector[1])\
                                            /complex(lastedgevector[0],lastedgevector[1])))
                #if self.testmode:print self.current_action_dict

    def select_action_by_cost(self):
        if self.testmode:print 'action_cost_list(angle):',self.current_action_dict
        actionlist,actioncost=zip(*self.current_action_dict.items())
        actionprob_unnorm=np.array([self.cost2prob(i) for i in actioncost])
        #if self.testmode:print actionlist,actionprob_unnorm.sum()
        action=np.random.choice(actionlist,1,p=actionprob_unnorm/actionprob_unnorm.sum())[0]
        #if self.testmode:print action,type(action),type(self.current_node)
        return action
    def cost2prob(self,angle):

        return np.e**(-self.cost_node_constant*angle)

    def uniform_choice_node(self,nodelist):        
        return np.random.choice(nodelist,1)


    def action_perform(self, action):
    	if action == 'pickup':
            
            newnode=self.pickup_new_node()
            if self.testmode:print 'Action:pickup',newnode
            newnode=newnode.astype(np.int32)
            self.strokes_set.add(tuple(self.current_stroke))
            self.current_parse.append(self.current_stroke)
            self.current_stroke=[]
            self.last_node=None
            self.current_node=newnode
            self.current_stroke.append(newnode)
        elif action == 'retrace':
            if self.testmode:print 'Action:retrace',action
            newnode=self.last_node
            self.current_stroke.append(newnode)
            self.last_edgevector=np.array(self.graph.nodes[newnode]['Location'])\
                       -np.array(self.graph.nodes[self.current_node]['Location'])
            self.last_node=self.current_node
            self.current_node=newnode

        else:
            if self.testmode:print 'Action:move',action

            newnode=action.astype(np.int32)
            self.graph.edges[newnode,self.current_node]['isunused']=False
            if self.testmode:print 'edgestate',self.graph.edges[newnode,self.current_node]['isunused']
            #if self.testmode:print type(newnode),type(self.current_node)
            self.current_stroke.append(newnode)
            self.last_edgevector=np.array(self.graph.nodes[newnode]['Location'])\
                       -np.array(self.graph.nodes[self.current_node]['Location'])
            self.last_node=self.current_node
            self.current_node=newnode
        self.current_action_dict={}
 


if __name__ =='__main__' :
    Graph=creat_toy_graph()
    #print Graph.nodes[1]['Location']
    penwalker=Penwalker(Graph)
    a,b=penwalker()
    print 'final result_Parseset:'
    print a
    print 'final result_Strokeset:'
    print b
