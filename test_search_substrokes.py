# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: test_search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:19:17
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-22 11:45:06
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
    
    @data
    @unpack
    def test_prob_node(self):

    def test_propose_splits(self):    
        #alomost equal  去看高概率的是否多出现 

if __name__ =='__main__' :
    pandasDataAnalysisSuit = unittest.TestLoader().loadTestsFromTestCase(Mytest)
    unittest.TextTestRunner(verbosity = 2).run(pandasDataAnalysisSuit) 
