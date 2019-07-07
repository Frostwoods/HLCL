# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: quicktest_subsearch.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-12-19 16:25:05
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2018-12-26 20:16:48
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
        self.fakepropose=np.array(list(csv_data.p))
  
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
    
    @data (((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),3),((1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1),2))
    @unpack
    def testProposeWiggle(self,propose,Sigma):
        
        wiggleProposes=targetCode.poposeWiggles(propose,Sigma)
        #self.assertTrue(wigglePropose.shape[0]<=asamp)
       # print wiggleProposes
        #[self.assertEqual(np.where((wigp==propose)==False)[0].size,2) for wigp in wiggleProposes ]

    @data(4)    
    def testProposeRepalce(self,index):    
        #[self.assertTrue(i>3) for i in range(8)]
        self.setUP()
        replaceProposes=targetCode.proposeReplaces(self.faketraj,self.fakepropose)
        #[self.assertEqual(np.where((wigp==propose)==False)[0].size,2) for wigp in replaceProposes ]  
    	print np.where(self.fakepropose)
    	print np.where(replaceProposes)
    	#print replaceProposes
    @data(4)
    def testProposeSplits(self,nasamp):
    	self.setUP()
    	splitproposes=targetCode.proposeSplits(self.faketraj,self.fakepropose,nasamp)
    	#print splitproposes
  

    def testMakeParse(self):
        self.setUP()
        S,Idx=targetCode.makeParse(self.faketraj,self.fakepropose)
        #pprint S,Idx

    def testVisulization(self):
        self.setUP()
        strdraw=targetCode.darwAStrokebytrj()
        strdraw(self.faketraj)

if __name__ =='__main__' :
    pandasDataAnalysisSuit = unittest.TestLoader().loadTestsFromTestCase(Mytest)
    unittest.TextTestRunner(verbosity = 2).run(pandasDataAnalysisSuit) 
