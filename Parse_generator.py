# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Parse_generator.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-10-31 19:03:03
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-02 16:46:17
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

Unit test:
	a toy graph  a list of dictionary node
        
        node {'id':i,'Location':[x,y],'edgelist':[id of other nodes],['']}
    node['id']

Change Activity:



"""
import networkx as nx 
import numpy as np

def creat_toy_graph():
    edgelist = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
                 (6, 7), (7, 8), (8, 9), (4, 8), (4, 9)]
    nodelist=range(1,10)
    nodelocationlist=[(1,4),(1.5,3.5),(1,3),(2,3),(3,3),(3,4),(2.5,4.2),(2,3.5),(2,1.5)]
    ToyG = nx.Graph()
    ToyG.add_nodes_from(nodelist)
    ToyG.add_edges_from(edgelist)
    for i in nodelist:
        print i,nodelocationlist[i-1]
        ToyG.nodes[i]['Location']=nodelocationlist[i-1]
    for (x,y) in edgelist:
        ToyG.edges[x,y]['isunused']=Ture

    print len(ToyG.edges),ToyG.edges[1,2],ToyG.edges[2,1]

    return ToyG


class Penwalker():
    """docstring for """

    def __init__(self, graph):
        
        self.orginal_graph=graph
        
        #hyper para
        self.parse_terminal_num = 150
        self.stroke_terminal_num = 100
        self.cost_node_constant=0.4
        self.cost_pickup_constant=2
        #Output
        self.parses_set = set()
        self.strokes_set = set()
        #Other
        self.current_action_dict={}
        self.current_node=None
        self.last_node=None
        self.last_edgevector=None

    def __call__(self, arg):

        while len(self.parses_set) <= self.parse_terminal_num and len(self.strokes_set) < self.stroke_terminal_num:
            
            self.graph=self.orginal_graph
            self.current_storke=[]
            self.current_parse=[]
            
            self.current_node=self.uniform_choice_node()

            while len(self.unused_edges)>0:
                #generate a parse
                if self.current_node is not None:                    
                    self.current_action_dict['retrace']=np.pi/2
                    self.current_action_dict['pickup']=np.pi/4


         	    self.cost_calculate()
                action=self.select_action_by_cost()
                self.action_perform()


         	self.current_storke.append(self.current_parse)
        return self.parses_set,self.strokes_set

    def cost_calculate(self):
         for i in self.graph.neighbors(self.current_node):
            print i,self.graph.nodes[i]
            if self.graph.edges[i,self.current_node]['isunused']:
                edgevector=np.array(self.graph.nodes[i]['Location'])\
                           -np.array(self.graph.nodes[self.current_node]['Location'])
                if self.lastedgevector is None:
                    lastedgevector=edgevector
                else:
                    lastedgevector=self.lastedgevector
                self.current_action_dict[i]=abs(np.angle(complex(edgevector[0],edgevector[1])\
                                            /complex(lastedgevector[0],lastedgevector[1])))

    def select_action_by_cost(self):
        actionlist,actioncost=zip(*self.current_action_dict.items())
        actionprob_unnorm=np.array([self.cost2prob(i) for i in actioncost])
        action=np.random.choice(actionlist,1,actionprob_unnorm/actionprob_unnorm.sum)
        return action
    def cost2prob(self,angle):

        return np.e**(-self.cost_node_constant*angle)

    def uniform_choice_node(self):        
        return np.random.choice(self.graph.nodes,1)

    def action_perform(self, action):
    	if action == 'pickup':
            self.pickup_new_node()
            self.strokes_set.append(self.current_stroke)
            self.current_parse.append(self.current_storke)
            self.current_storke=[]
        elif action == 'retrace':
            pass
        else:
            self.current_storke.append[action]
            self.last_edgevector=np.array(self.graph.nodes[action]['Location'])\
                       -np.array(self.graph.nodes[self.current_node]['Location'])
            self.last_node=self.curren_node
            self.current_node=action

    def pickup_new_node(self):
        newnodelist,unused_edgesnumber=count_unused_edges
        pickprob_unnorm=np.array([self.pickup_prob(i),for i in  unused_edgesnumber])
        pickupprob=pickupprob/pickprob.sum
        return  np.random.choice(newnodelist,1,pickupprob)

    def pickup_prob(self,n):
        return 1/(n**self.cost_pickup_constant)

    def count_unused_edges(self):
        pass




if __name__ =='__main__' :
    Graph=creat_toy_graph()
    print Graph.nodes[1]['Location']
    penwalker=Penwalker(Graph)
    penwalker.current_node=4
    penwalker.lastedgevector=[0,1]
    penwalker.cost_calculate()
    print penwalker.current_action_dict