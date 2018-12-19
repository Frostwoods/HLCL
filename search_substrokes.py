# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:18:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-12-19 16:10:23
"""
Descripition:



Change Activity:



"""
import numpy as np
from scipy.stats import norm
import copy
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
def sampleSplitbyp(p_array,limit=5):
    subPropose=np.zeros(p_array.size)
    newP=p_array
    newP[:limit]=0
    newP[-limit:]=0
    split=np.random.choice(range(p_array.size),1,p=newP/newP.sum())[0]
    #subPropose[0],subPropose[-1],subPropose[split]=1,1,1
    #return subPropose==1
    return split
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

    return abs(np.angle(complex(v1[0],v1[1])\
             /complex(v2[0],v2[1])))


def proposeMerges(propose):

    splitIndex=np.where(propose)[0]
    spt=splitIndex[1:-1]
    meragedproposes=np.tile(propose,(spt.size,1))
    for n in range(spt.size):
        meragedproposes[n][spt[n]]=False
    return meragedproposes 

def poposeWiggles(propose,sigma_wiggle=3):
    #input 1*n np.array(boolen)
    #output nsap*n 
    #！！rejection undone
    splitIndex=np.where(propose)[0]
    spt=splitIndex[1:-1]
    wigglepropose=np.tile(propose,(spt.size,1))
    for n in range(spt.size):      
        wigglepropose[n][spt[n]]=False
        shift=sampleShiftForWiggles(sigma_wiggle)
        wigglepropose[n][spt[n]+shift]=True

    return wigglepropose

def sampleShiftForWiggles(sigma_wiggle=3):
    sd=int(sigma_wiggle)
    x=np.append(np.arange(-3*sd,0),np.arange(1,3*sd+1))
    py=norm.pdf(x,0,sd)
    py=py/py.sum()
    indx=np.random.choice(range(py.size),1,p=py)[0]
    
    return x[indx]

def proposeSplits(traj,propose,nsamp):
    splitedproposes=[proposeASplit(traj,propose) for i in range(nsamp)]
    return list(set(splitedproposes))
def proposeASplit(traj,propose):
    splitpropose=copy.deepcopy(propose)
    S,Idx=make_parse(traj,propose)
    bid=np.randomchoice(range(len(S)))
    subtrj=S(bid)
    sptid=sampleSplitInSubtraj(subtrj)
    splitpropose[Idx[bid][sptid]]=true
    return splitpropose

def sampleSplitInSubtraj(subtrj):
    anglearray=cal_directionOfnodeInatrajectory(subtrj,jumpnum=3)
    p_array=prob_node_byangle(anglearray,baseline=0.001)
    split=sampleSplitbyp(p_array,limit=5)
    return split
def proposeReplaces(traj,propose):
    #delete a existed node and resample one by proposesplit
    #sample a split to replace
    splitIndex=np.where(propose)[0]
    spt=splitIndex[1:-1]
    replaceproposes=np.tile(propose,(spt.size,1))
    
    for n in range(spt.size):      
        replaceproposes[n][spt[n]]=False
        S,Idx=make_parse(traj,replaceproposes[n])
        subtraj=S[n]
        sptid=sampleSplitInSubtraj(subtrj)
        replaceproposes[Idx[n][sptid]]=true
    #  rpl=np.random.choice(range(len(spt)))
    #replacepropose[spt[rpl]]=false
    #wigglepropose=np.tile(propose,(spt.size,1))
    #S,Idx=make_parse(traj,propose)
    #subtraj=S[rpl]
    #sptid=sampleSplitInSubtraj(subtrj)
    #replacepropose[Idx[bid][sptid]]=true
    return replaceproposes

def makeParse(traj,hyp):
    spt=np.where(hyp)[0]
    nsub=spt.size-1
    S=[traj[spt[i]:spt[i+1]] for i in range(nsub)]
    Idx=[range(spt[i],spt[i+1]) for i in range(nsub)]
    return S,Idx
    '''
def propose_wiggles():
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
