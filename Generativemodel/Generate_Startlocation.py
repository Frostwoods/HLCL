# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Startlocation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 13:04:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-07 22:11:19
"""
Descripition:
	Inuput Relation ,Trajectory 
	Out put current start locaiton
	
	function g
	N(g(...),sigma)


Change Activity:
	cal_mean along undone


"""

class Generate_Startlocation(object):
	"""docstring for Generate_Startlocation"""
	def __init__(self,sapara, samplemode):
		#super(Generate_Startlocation, self).__init__()
		self.sample = samplemode()
		sel.cov=sapara
	def __call__(self,Relation,Trajectory):

		return sample(cal_meanlocation(Relation,Trajectory),self.cov)

	def cal_meanlocation(self,Relation,Trajectory):
		#1:Indenpent 2:Start 3:End 4 :along
		if Relation['relationid']==0:
			mean=Relation['para']
		elif Relation['relationid']==1:
			mean=Trajectory[Relation['para']][0]
		elif Relation['relationid']==2:	
			mean=Trajectory[Relation['para']][-1]
		elif Relation['relationid']==3:
			#'spline-eval' undone
			mean=[0,0]
		return mean
