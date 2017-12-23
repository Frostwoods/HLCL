# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:32:58
"""
Descripition:



Change Activity:



"""
import scipy.io as sio
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
from Gaussian.sample_gaussian import sample_gaussian

class addvar_relation(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiemodle=sample_gaussian):


		self.sample=samplemode()
		self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
		
		#self.cov =[]
		
		self.cov=self.load(self.matfn)
	def __call__(self,tao):
		return self.sample(tao,self.cov)


	def load(self,matfn):
		return sio.loadmat(self.matfn)