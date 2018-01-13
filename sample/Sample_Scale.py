# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Scale.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-22 01:16:11
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-06 22:27:30
"""
Descripition:
	Input subid [int]
	Output scale [int]


Change Activity:



"""


class Sample_Scale(object):
	"""docstring for S"""
	def __init__(self, samplepara,samplemode):
		
		self.sample = samplemode
		self.alpha_list=samplepara['alpha']
		self.beta_list=samplepara['beta']
	def __call__(self,SubstrokesID):
		return self.sample(self.alpha_list[SubstrokesID], scale=1/self.beta_list[SubstrokesID])
