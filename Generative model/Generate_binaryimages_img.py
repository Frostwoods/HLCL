# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_binaryimages_img.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:18:59
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 07:14:04
"""
Descripition:



Change Activity:



"""
class  Generate_binaryimages_img(object):
 	"""docstring for ClassName"""
 	def __init__(self, arg):
 		self.filter=[]
 		self.imgsize=[105,105]
 	def __call__(self,Trajectory,A,Eposilon,Sigma):
 		global_rescaling(Trajectory,A)	
 		global_translation(Trajectory,A)
 		img=ink_model(Trajectory)


 		convolving_img_twice(img,self.filter)
 		Gaussian_filter(img,Eposilon)
 		Bernoulli_filter(img,Sigma)
		return	img

