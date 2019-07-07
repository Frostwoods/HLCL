# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: testGraph.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-01 13:51:24
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-16 20:04:15
"""
Descripition:



Change Activity:



"""
import networkx as nx
import numpy as np
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (1, 3)])


G.node[1]['L'] = [1, 2]
# print G.edge, G.node, G.number_of_edges
# print G.edge[3], list(G.edge), [G.edge[i] for i in range(1, len(G.edge) + 1)]


def creat_toy_graph():
    # edgelist = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
    #              (6, 7), (7, 8), (8, 9), (4, 8), (4, 9)]
    nodelist=zip(range(-9,0),range(0,9))
    nodelocationlist=[(1,4),(1.5,3.5),(1,3),(2,3),(3,3),(3,4),(2.5,4.2),(2,3.5),(2,1.5)]
    ToyG = nx.Graph()
    ToyG.add_nodes_from(nodelist)
    edgelist = [((1,4), (1.5,3.5))]
    ToyG.add_edges_from(edgelist,test='hello')
    print ToyG.nodes,ToyG.edges[((1,4), (1.5,3.5))],'edges'#,ToyG.edges[edgelist]['test']

    # for i in nodelist:
    # 	ToyG.nodes[i]['Location']=nodelocationlist[i]
    for (x,y) in edgelist:
        ToyG.edges[x,y]['isused']=False
    a=ToyG.nodes
    #print ToyG.nodes
    # print len(ToyG.edges),ToyG.edges[1,2],ToyG.edges[2,1]
    #print ToyG.nodes
    test= [n for n in ToyG.neighbors(-1)]
    vector=np.array(ToyG.nodes[2]['Location'])-np.array(ToyG.nodes[1]['Location'])
    print np.angle(complex(vector[0],vector[1]),deg=True)

    print np.angle(complex(1,1)/complex(-1,1),deg=True)
    return ToyG
if __name__ =='__main__' :
    G=creat_toy_graph()
    print G.nodes[1]
