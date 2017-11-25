# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Relationid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:32
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-03 10:58:01
"""
Descripition:
	Sample Strokes Relations id 

	Input:SampleMode{
		Sample_Mutinomial 
	}

	Output Relationid{
		1:'Independent'
		2:'Start'
		3:'End'
		4:'Along'
	}

Change Activity:
	para loading unfinished Nov.3


"""
class Sample_Relationid(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode=Sample_Multinomial):
    	self.NUM=4
        self.read_parameter()
        self.Sample = SampleMode(self.NUM, self.P)

    def __call__(self):

        return self.Sample()

    def read_parameter(self):

         self.P = someloadingfunciton()
