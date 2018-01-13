# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: addvar_relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:25:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-11 22:01:34
"""
Descripition:



Change Activity:



"""

class addvar_relation(object):
	"""docstring for addvar_controlpoint"""
	def __init__(self, nosiepara,nosiemodle):


		self.sample=nosiemodle()
		self.para = nosiepara
		

	def __call__(self,tao):
		return self.sample(tao,self.para)

