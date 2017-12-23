# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_kappa.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:42:41
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-21 23:54:47
"""
Descripition:
	
	Output kappa: [int] 


Change Activity:
Undone pararead


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Multinomial.Sample_Multinomial import Sample_Multinomial
class Sample_kappa(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):

      
        self.Sample = SampleMode()
        self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
        self.NUM, self.P = self.read_parameter()
    def __call__(self):

        return self.Sample(self.NUM, self.P)

    def read_parameter(self):
        #someloadingfunciton()
         return sio.loadmat(self.matfn) 