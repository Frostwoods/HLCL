# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Radomflips.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:18:25
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 07:14:07
"""
Descripition:



Change Activity:

done

"""
import sys
sys.path.append('F:\Code\Matlab\HLCL\distribution')
from Uniform.sample_uniformreal	 import sample_uniformreal


class Sample_Radomfilps():
	def __init__(self,samplemode=sample_uniformreal):
		self.sample=samplemode()
		self.loc=0.0001
		self.scale=0.4999

	def __call__(self):
		return self.sample(self.loc,self.scale)

