# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_controlpoint.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:38
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:34:43
"""
Descripition:



Change Activity:



"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Gaussian.sample_multigaussian import sample_multigaussian

class addvar_controlpoint(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiemodle=sample_multigaussian):


		self.sample=samplemode()
		self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 		
		self.cov =[]		
		self.cov=self.load(self.matfn)

	def __call__(self,mean):
		return self.sample(mean,self.cov)

	def load(self,matfn):
		return sio.loadmat(self.matfn)