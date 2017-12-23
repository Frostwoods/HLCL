# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_FirstSubstrokesid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 09:52:46
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 00:59:56
"""
Descripition:



Change Activity:
Undone para read


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Multinomial.Sample_Multinomial import Sample_Multinomial

class Sample_FirstSubstrokesid(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):
        self.Sample = SampleMode()
        self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
        self.read_parameter()    
    def __call__(self):

        return self.Sample(self.NUM, self.P)

    def read_parameter(self):
        self.NUM, self.P = someloadingfunciton()
        return sio.loadmat(self.matfn) 