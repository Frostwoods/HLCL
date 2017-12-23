# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_SubstrokesNum.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:14
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 01:05:24
"""
Descripition:
	Input kappa: [int]
	Output n: [int]


Change Activity:
Undone para read


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Multinomial.Sample_Multinomial import Sample_Multinomial

class Sample_SubstrokesNum(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):           
        self.Sample = SampleMode()
        self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
    def __call__(self,Stroke_order):
    	self.read_parameter(Stroke_order)  
        return self.Sample(self.NUM, self.P)

    def read_parameter(self,Stroke_order):
        
        self.NUM, self.P = sio.loadmat(self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat'  Stroke_order)
