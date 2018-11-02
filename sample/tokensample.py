# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: tokensample.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-03-11 15:26:49
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 17:47:47
"""
Descripition:



Change Activity:



"""

class addvar_controlpoint(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiepara,nosiemodle):
		self.sample=nosiemodle()
		self.para = nosiepara


	def __call__(self,mean):
		return self.sample(mean,self.para)

class addvar_relation(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiepara,nosiemodle):


		self.sample=nosiemodle()
		self.para = nosiepara
		

	def __call__(self,tao):
		return self.sample(tao,self.para)

class addvar_scale(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self,  nosiepara,nosiemodle):

		self.sample=nosiemodle()
		self.para = nosiepara

	def __call__(self,scale):
		return self.sample(scale,self.para)



