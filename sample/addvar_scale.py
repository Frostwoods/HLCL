# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_scale.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:52
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:37:01
"""
Descripition:



Change Activity:



"""
import scipy.io as sio
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
from Gaussian.sample_gaussian import sample_gaussian

class addvar_scale(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiemodle=sample_gaussian):


		self.sample=samplemode()
		self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
		
		self.cov =[1]
		
		#self.cov=self.load(self.matfn)
	def __call__(self,scale):
		return self.sample(scale,self.cov)


	def load(self,matfn):
		return sio.loadmat(matfn)