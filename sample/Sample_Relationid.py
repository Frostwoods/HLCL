# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Relationid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:44:32
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 01:45:04
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
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Multinomial.Sample_Multinomial import Sample_Multinomial

class Sample_Relationid(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode=Sample_Multinomial):
    	self.NUM=4       
        self.Sample = SampleMode()
		self.matfn = 'path'
        self.P = sio.loadmat(matfn)
    def __call__(self):

        return self.Sample(self.NUM,self.P)+1

