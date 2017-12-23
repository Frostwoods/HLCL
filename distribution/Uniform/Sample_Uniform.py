# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Uniform.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-21 19:09:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-21 21:27:06
"""
Descripition:



Change Activity:



"""
from scipy.stats import randint
import numpy as np
class Sample_Uniform():

    def __init__(self):
        '''NUM 取值域大小 P 各值对应概率 '''
        pass
            #self.NUM = NUM

    def __call__(self, NUM=None,sampletimes=1):
        self.NUM = NUM
 
        if NUM is None:
            self.gen_NUM()
  
        # Return a Sample 
        sample = np.zeros(sampletimes)
        for x in xrange(0, sampletimes):           
            sample[x] = np.random.randint(self.NUM )    
        return sample

    def gen_NUM(self, maxnumber=10):
        '''random generate the size of distribution '''
        self.NUM = np.random.randint(1, maxnumber)

