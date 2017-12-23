# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Transformationnumber.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:17:39
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:39:48
"""
Descripition:



Change Activity:



"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Gaussian.sample_multigaussian import sample_multigaussian


class Sample_Transformationnumber(object):
	"""docstring for Sampel"""
	def __init__(self, samplemode=sample_multigaussian):

		self.sample=samplemode()
		self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat' 
		self.mean = [1,1,0,0]
		self.cov =[]
		self.cov=self.load(self.matfn)
	def __call__(self):
		return self.sample(self.mean,self.cov)


	def load(self,matfn):
		return sio.loadmat(matfn)


