# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:18:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-23 13:27:53
"""
Descripition:



Change Activity:



"""
import numpy as np
'''
class toy_stroke():
    pass
class toy_primatives():
    pass
'''
'''
class search_substrokes():

# input: a storke a list of node with edges trajector between them
# [n*2] 3个点
# output:
    def __init__(self, primatives):        
        self.primatives = primatives
        pass
    def __call__(self):
        pass
'''
def sampleSplits(p_array,limit=5):
    subPropose=np.zeros(p_array.size)
    newP=p_array
    newP[:limit]=0
    newP[-limit:]=0
    split=np.random.choice(range(p_array.size),1,p=newP/newP.sum())[0]
    subPropose[0],subPropose[-1],subPropose[split]=1,1,1
    return subPropose==1

def prob_node_byangle(anglearray,baseline=0.001):
#1	input:  output
    p_array=np.square(anglearray)+baseline
    return p_array/p_array.sum()
    
def cal_directionOfnodeInatrajectory(trajectory,jumpnum=1):
    #inuput n*2array 

    v1_list=[trajectory[i]-trajectory[i-jumpnum] for i in range(jumpnum,trajectory.shape[0]-jumpnum)]
    v2_list=[trajectory[i+jumpnum]-trajectory[i] for i in range(jumpnum,trajectory.shape[0]-jumpnum)]
    return np.array([cal_angles_two_vectors(v1,v2) for (v1,v2) in zip(v1_list,v2_list)])

def cal_angles_two_vectors(v1,v2):

#2   
    return abs(np.angle(complex(v1[0],v1[1])\
             /complex(v2[0],v2[1])))
'''
def propose_merges():

    pass
def propose_wiggles():
    pass
def propose_replace():
    pass

def fit_bspline(trajectory):

    return ctrpoint

def score_substroke_propose():
	pass
'''



if __name__ =='__main__' :
    Graph=creat_toy_graph()
    #print Graph.nodes[1]['Location']
    penwalker=Penwalker(Graph)
    a,b=penwalker()
    print 'final result_Parseset:'
    print a
    print 'final result_Strokeset:'
    print b
