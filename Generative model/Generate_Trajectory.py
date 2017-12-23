# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Trajectory.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 10:53:38
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 09:54:39
"""
Descripition:
	Input :a starting location L,token-level control points x,token-level scale y
y

	Output T: a sequence of points in the image plane that represents
the path of the pen.


Change Activity:



"""
from scipy.interpolate import BSpline

class Generate_Trajectory(object):
	"""docstring for Gen"""
	#see matlab edtion
	def __init__(self, sval):
		super(Gen, self).__init__()
		self.sval = sval
		self.twodim_bspline=twodim_bspline()
	def __call__(self,start_location,var_control_x_array,var_scale_y):
		#transform?
		
		dim=len(var_control_x_array)
		rawTrajecory_array=twodim_bspline(var_control_x_array)		

		return var_scale_y*rawTrajecory_array-rawTrajecory_array[0]+start_location

	def bspline_eval(self,var_control_x_array,var_scale_y)
		#uniform cubic b-spline
		BSpline
		BSpline(var_control_x_array,[1],3)
		