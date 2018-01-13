# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Controlpoints.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 10:27:15
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-06 22:10:27
"""
Descripition:

	input subid[int]
	output ctp[5*2 list]

Change Activity:


load_fun unfinished


"""

class Sample_Controlpoints():
	def __init__(self,samplepara,samplemode):
		self.sample=samplemode()
		self.mean_list=samplepara['mean']
		sefl.cov_list=samplepara['cov']
		 
	def __call__(self,SubstrokesID):

		return self.sample(self.mean_list[SubstrokesID],self.cov_list[SubstrokesID])

