# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:18:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2019-06-21 21:12:49
"""
Descripition:



Change Activity:



"""
import numpy as np
from scipy.stats import norm
import copy
import cv2
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

def proposeWiggles(propose,sigma_wiggle=3):
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
    return splitedproposes
def proposeASplit(traj,propose):
    splitpropose=copy.deepcopy(propose)
    S,Idx=makeParse(traj,propose)
    bid=np.random.choice(range(len(S)))
    subtrj=S[bid]
    sptid=sampleSplitInSubtraj(subtrj)
    splitpropose[Idx[bid][sptid]]=True
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
        S,Idx=makeParse(traj,replaceproposes[n])
        subtrj=S[n]
        sptid=sampleSplitInSubtraj(subtrj)
        replaceproposes[n][Idx[n][sptid]]=True
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
class darwAStrokebytrj(object):
    """docstring for darwa"""
    def __init__(self, imgsize=[128,128,3],isvis=True):
        self.isvis=isvis
        self.imgsize = imgsize
        self.black=[0,0,0]
    def __call__(self,trj,img=None,move2centre=True):
        if img is None:img = np.ones((self.imgsize[0], self.imgsize[1], 3), np.uint8) * 255
        
        if move2centre:
            movedtrj=trj+np.trunc(([self.imgsize[0]/2,self.imgsize[1]/2]-trj.mean(axis=0)))
        else:
            movedtrj=trj
        for [x,y] in movedtrj:
            img[int(x)][int(y)]=self.black
        if  self.isvis:
            cv2.imshow("aStroke",img)
            cv2.waitKey(0)
        return img
class darwParseOfAStroke(object):
    def __init__(self,isvis=True):
        self.isvis=isvis
        self.colorlist=[[255,0,0],[0,255,0],[0,0,255],\
                     [0,255,255],[255,0,255],[255,255,0]]

    def __call__(self,img,S):

        pass
def darwastroke(img,astrokepoint_list,color = (123, 123, 123),line_width=1):
    """docstring for Darwastroke"""

    for point in astrokepoint_list:
        pts = np.array(point, dtype=np.int32)
        pts = pts.reshape((-1, 1, 2))       
        cv2.polylines(img, [pts], False, color,thickness=line_width, lineType=8)
    return img

    
class searchSubstrokes(object):
    """docstring for searchSubstrokes"""
    def __init__(self,proposeSplits,proposeWiggles=proposeWiggles ):
        
     
        self.Splitsnsap=5
        self.curscore= None
        self.hist_hyp=set()
        self.Score=score_all_propose
        self.proposeSplits=proposeSplits
        self.proposeWiggles=proposeWiggles

    def __call__(self,traj):


        propose=self.setdefaultpropose(traj.shape[0])

        while True:
            prop_hyp=[]
            prop_split=self.proposeSplits(traj,propose,self.Splitsnsap)
            prop_merge=self.proposeMerges(propose)
            prop_wiggle=self.proposeWiggles(propose)
            prop_replace=self.proposeReplaces(traj,propose)
            prop_hyp.append(prop_split,prop_merge,prop_wiggle,prop_replace)           
            #undone
            prob_hyp=self.rmv_hyp(prop_hyp)           
            #undone
            II=self.Score(prop_hyp)
            
            windx=np.argmax(II)
            if II[windx]>self.curr_score+1
                self.hyp=prop_hyp[windx]
                [self.hist_hyp.update(x) for x in prob_hyp]
                #undone direction opti
            else 
                break
                
        return self.hyp
        
    def setdefaultpropose(self,n):
        #传进来 
        initpropose=np.zeros((n,))
        initpropose[0]=1
        initpropose[-1]=1
        return initpropose==1
class score_all_propose(object):
    def __init__(self,singlescore):

    def __call__(self,proposes):
        score_list=[]
        for prop in proposes:
            score_list.append(self.score)

class Score_stroke_propose(object):
    """docstring for Scoresubs"""
    def __init__(self, arg):        
        self.arg = arg
    def __call__(self,traj,hyp):

def score_stroke(stats):
    score=0
    score+=CPD.scoreStroke()
    score+=CPD.scoreInvscaleType
    score+=CPD.socre_invascale_token
    score+=CPD.score_shape_marginalize
    return score

class cls_trj_as_subid(object):
    def __init__(self,mean,sd,bspFit):
        self.fitBspline=bspFit
        self.mean=mean
        self.sd=sd
        self.prmnum=len(self.mean)
        self.mltnormpdf=multivariate_normal.pdf
    def __call__(self,trj):
        ctrpoint=self.fit_bspline(self.sval,trj).T
        scorelist=[self.mltnormpdf(ctrpoint,self.mean(i),self.sd(i)) for i in range(self.prmnum)]        
        return np.argmax(scorelist)
        



if __name__ =='__main__' :
    Graph=creat_toy_graph()
    #print Graph.nodes[1]['Location']
    penwalker=Penwalker(Graph)
    a,b=penwalker()
    searchSubstrokes(proposeSplits)
    B=（A,)
    print 'final result_Parseset:'
    print a
    print 'final result_Strokeset:'
    print b
