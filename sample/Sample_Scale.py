# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Scale.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-22 01:16:11
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:35:59
"""
Descripition:
	Input subid [int]
	Output scale [int]


Change Activity:



"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from scipy.stats import Gamma

class Sample_Scale(object):
	"""docstring for S"""
	def __init__(self, samplemode=Gamma.rvs):
		
		self.sample = samplemode
		self.matfn = '/home/wei'
		self.alpha_list,self.beta_list=sio.loadmat(self.matfn)

	def __call__(self,SubstrokesID):
		return self.sample(self.alpha_list[SubstrokesID], scale=1/self.beta_list[SubstrokesID])
