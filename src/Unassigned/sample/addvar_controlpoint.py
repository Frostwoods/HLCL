# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_controlpoint.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:38
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-07 22:29:11
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

