# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_SubstrokesNum.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:14
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-20 14:31:00
"""
Descripition:



Change Activity:
2017-11-20 14:00:07 :80%


"""

class Sample_SubstrokesNum(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):


        self.read_parameter(Stroke_order)        
        self.Sample = SampleMode()

    def __call__(self,Stroke_order):

        return self.Sample(self.NUM, self.P)

    def read_parameter(self,Stroke_order):
        self.NUM, self.P = someloadingfunciton(Stroke_order)
