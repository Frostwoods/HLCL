# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: test_search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:19:17
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-12-07 19:51:58
"""
Descripition:



Change Activity:



"""
from ddt import ddt,data,unpack
import unittest 
import search_substrokes as targetCode
import numpy as np


@ddt
class Mytest(unittest.TestCase):

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
        [self.assertTrue(i<5) for i in range(8)]
    @data ((4,1),(8,2),(12,3))
    @unpack
    def testSampleSplits(self,testlen,limit):
        #3个断点1
        #1之间大于5
        #随机性检验  
        unNormP=np.random.rand(testlen)
        NormP=unNormP/unNormP.sum()
        print NormP.sum()
        #NormP=np.array([0.5,0.4,0.05,0.05])
        SubProp=targetCode.sampleSplits(NormP,limit=limit)
        print SubProp
        splitIndex=np.where(SubProp)[0]
        self.assertEqual(splitIndex.size,3)
        dis=[splitIndex[i+1]-splitIndex[i] for i in range(2)]
        print dis
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
        [print(p) for p in targetCode.proposeMerges(propose)]
    @data ([1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1])
    @unpack
    def testProposeWiggle(self,propose):
        wigglePropose=targetCode.poposeWiggles(propose,asamp)
        self.assertTrue(wigglePropose.shape[0]<=asamp)
        [self.assertEqual(np.where((wigp==propose)==False)[0].size,2) for wigp in wigglePropose ]

    @data ([1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1])
    @unpack
    def testProposeRepalce(self,propose):    
        [self.assertTrue(i>3) for i in range(8)]
        
if __name__ =='__main__' :
    pandasDataAnalysisSuit = unittest.TestLoader().loadTestsFromTestCase(Mytest)
    unittest.TextTestRunner(verbosity = 2).run(pandasDataAnalysisSuit) 
