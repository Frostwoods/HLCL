# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Controlpoints.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 10:27:15
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 01:59:24
"""
Descripition:

	input subid[int]
	output ctp[5*2 list]

Change Activity:


load_fun unfinished


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Gaussian.sample_multigaussian import sample_multigaussian

class Sample_Controlpoints():
	def __init__(self,samplemode=sample_multigaussian):
		self.sample=samplemode()
		self.matfn = '/home/wei'
		self.mean_list,sefl.cov_list=self.load_fun()
		 
	def __call__(self,SubstrokesID):

		return self.sample(self.mean_list[SubstrokesID],self.cov_list[SubstrokesID])

	def load_fun(self,)

		return sio.loadmat(self.matfn) 