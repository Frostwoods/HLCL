# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Gaufliter.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:17:58
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:42:10
"""
Descripition:



Change Activity:

done

"""
import sys

sys.path.append('F:\Code\Matlab\HLCL\distribution')
from Uniform.sample_uniformreal	 import sample_uniformreal


class Sample_Gaufliter():
	def __init__(self,samplemode=sample_uniformreal):
		self.sample=samplemode()
		self.loc=0.5
		self.scale=16

	def __call__(self):
		return self.sample(self.loc,self.scale)