# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_SubstrokesNum.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:14
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 22:03:15
"""
Descripition:
	Input kappa: [int]
	Output n: [int]


Change Activity:
Undone para read


"""

class Sample_SubstrokesNum(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode ):           
        self.Sample = SampleMode
        
        #self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 

    def __call__(self,Stroke_order,PM):
    	self.read_parameter(Stroke_order)  
        return self.Sample(self.NUM, self.P)

    