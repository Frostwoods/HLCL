# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_scale.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:52
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-07 22:30:04
"""
Descripition:



Change Activity:



"""

class addvar_scale(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self,  nosiepara,nosiemodle):

		self.sample=nosiemodle()
		self.para = nosiepara

	def __call__(self,scale):
		return self.sample(scale,self.para)
