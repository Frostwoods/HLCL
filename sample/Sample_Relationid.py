# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Relationid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:32
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-07 21:44:19
"""
Descripition:
	Sample Strokes Relations id 

	Input:

	Output Relationid [int]

	{
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

    def __init__(self, SampleMode):
    	self.num=4       
        self.Sample = SampleMode

        
    def __call__(self,i):

        return randint.rvs(0, self.num)

