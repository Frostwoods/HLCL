# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: test_search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:19:17
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-12-19 15:56:52
"""
Descripition:



Change Activity:



"""
from ddt import ddt,data,unpack
import unittest 
import search_substrokes as targetCode
import numpy as np
import pandas as pd

@ddt
class Mytest(unittest.TestCase):

    def setUP(self):
        csv_data=pd.read_csv('afakestroke.csv')
        self.faketraj=np.array([[x,y] for (x,y) in zip(csv_data.x,csv_data.y)])
        self.fakepropose=np.array(csv_data.p)


    @data ((np.array([1,1]),np.array([3,3]),0),\
        (np.array([0,3]),np.array([0,-3]),np.pi),\
        (np.array([0,3]),np.array([2,2]),np.pi/4.0))
    @unpack
    def test_cal_angles_two_vectors(self,v1,v2,angle):
    	
        self.assertEqual(targetCode.cal_angles_two_vectors(v1,v2),angle)
       # self.assertEqual(np.array([1,2,4]).tolist(),np.array(range(1,4)).tolist())


    @data((np.array([[1,1],[1,2],[2,2],[3,3],[3,2],[4,1],[5,0]]),\
        np.array([np.pi/2,np.pi/4,np.pi*3/4,np.pi/4,0]))\
    	,(np.array([[-1,-1],[2,2],[3,3]]),np.array([0])))
    @unpack
    def test_cal_directionOfnodeInatrajectory(self,trajectory,angle_list):
    
        self.assertEquals(targetCode.cal_directionOfnodeInatrajectory(trajectory).tolist(), angle_list.tolist()) 		
    

    @data ((np.array([np.pi*8/16,np.pi*6/16,0]),np.array([0.63766275,0.359796761,0.002540489])),\
        (np.array([0,0,0,0]),np.array([0.25,0.25,0.25,0.25])))
    @unpack
    def test_prob_node_byangle(self,anglearray,parray):
        #print targetCode.prob_node_byangle(anglearray)
        self.assertTrue(np.all(np.isclose(targetCode.prob_node_byangle(anglearray),parray)))
        
    @data ((4,1),(8,2),(12,3))
    @unpack
    def testSampleSplitbyp(self,testlen,limit):
        #3个断点1
        #1之间大于5
        #随机性检验  
        unNormP=np.random.rand(testlen)
        NormP=unNormP/unNormP.sum()
        #print NormP.sum()
        #NormP=np.array([0.5,0.4,0.05,0.05])
        SubProp=targetCode.sampleSplitbyp(NormP,limit=limit)
        #print SubProp
        splitIndex=np.where(SubProp)[0]
        self.assertEqual(splitIndex.size,3)
        dis=[splitIndex[i+1]-splitIndex[i] for i in range(2)]
       # print dis
        self.assertTrue(np.all(dis>=limit))    
    #@data input tlen boolean 
    #       output  m*tlen boolean m,splitsnum in tlen
    
    #input 1*n a propose
    #output m*n every possibleplace
    @data(([1,0,1,0,0,1,0,1],([[1,0,0,0,0,1,0,1],[1,0,1,0,0,0,0,1]])),\
            (([1,0,0,1,0,0,1,0,1,0,0,0,1]),([[1,0,0,0,0,0,1,0,1,0,0,0,1],\
                [1,0,0,1,0,0,0,0,1,0,0,0,1],[1,0,0,1,0,0,1,0,0,0,0,0,1]])
            ))
    @unpack
    def testProposeMerges(self,propose,mergedpropose):
        self.assertTrue(np.all(targetCode.proposeMerges(propose)==mergedpropose))
       # [print(p) for p in targetCode.proposeMerges(propose)]
    
    @data((2,10000),(3,10000))
    @unpack
    def testsampleShiftForWiggles(self,sigma,nsap):
        shiftlist=[targetCode.sampleShiftForWiggles(sigma) for i in range(nsap)]
    
        shiftelement=list(set(shiftlist))
        shiftelement.sort()

        shiftcount=[shiftlist.count(i) for i in shiftelement]

        shiftp=np.array(shiftcount)*1.0
        shiftp=shiftp/shiftp.sum()
        maxpid=np.where(shiftp==np.max(shiftp))[0]
        print shiftelement
        print maxpid,shiftelement[maxpid[0]]
        maxshift=np.max(shiftelement)
        minshift=np.min(shiftelement)
        
        self.assertTrue(maxshift<=3*sigma)
        self.assertTrue(minshift>=-3*sigma)
        self.assertEquals(abs(shiftelement[maxpid[0]]),1)

    @data (((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),3),((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),2))
    @unpack
    def testProposeWiggle(self,propose,Sigma):
        
        wiggleProposes=targetCode.poposeWiggles(propose,Sigma)
        #self.assertTrue(wigglePropose.shape[0]<=asamp)
        [self.assertEqual(np.where((wigp==propose)==False)[0].size,2) for wigp in wiggleProposes ]

    @data (((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),3),((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),2))
    @unpack
    def testProposeRepalce(self,traj,propose):    
        #[self.assertTrue(i>3) for i in range(8)]
        replaceProposes=targetCode.poposeReplaces(traj,propose)
        [self.assertEqual(np.where((wigp==propose)==False)[0].size,2) for wigp in replaceProposes ]  
    # propose,traj,propose
    @data((np.array([[1,1],[1,2],[2,2],[3,3],[3,2],[4,1],[5,0]]),\
        np.array([np.pi/2,np.pi/4,np.pi*3/4,np.pi/4,0]))\
        ,(np.array([[-1,-1],[2,2],[3,3]]),np.array([0])))
    @unpack

    @data(1,2)
    def testMakeParse(self,traj,propose):
        self.setUP()
        S,Idx=targetCode.makeParse(self.faketraj,self.fakepropose)
        print S,Idx


if __name__ =='__main__' :
    pandasDataAnalysisSuit = unittest.TestLoader().loadTestsFromTestCase(Mytest)
    unittest.TextTestRunner(verbosity = 2).run(pandasDataAnalysisSuit) 
