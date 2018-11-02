# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Trajectory.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 10:53:38
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 18:19:40
"""
Descripition:
	Input :a starting location L,token-level control points x,token-level scale y
y

	Output T: a sequence of points in the image plane that represents
the path of the pen.


Change Activity:



"""
from scipy.interpolate import BSpline
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt
import cv2


def bspline(cv, n=50, degree=3, periodic=False):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
                  False - Curve is open
    """

    # If periodic, extend the point array by count+degree+1
    cv = np.asarray(cv)
    count = len(cv)

    if periodic:
        factor, fraction = divmod(count + degree + 1, count)
        cv = np.concatenate((cv,) * factor + (cv[:fraction],))
        count = len(cv)
        degree = np.clip(degree, 1, degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree, 1, count - 1)

    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0 - degree, count + degree + degree - 1, dtype='int')
    else:
        kv = np.array([0] * degree + range(count - degree + 1) +
                      [count - degree] * degree, dtype='int')

    # Calculate query range
    u = np.linspace(periodic, (count - degree), n)

    # Calculate result
    arange = np.arange(len(u))
    points = np.zeros((len(u), cv.shape[1]))
    for i in xrange(cv.shape[1]):
        points[arange, i] = si.splev(u, (kv, cv[:, i], degree))

    return points

def calculateAstroketrajectory( startlocation,ctplist, scalelist):
	
	point_list=[]		
	for ctpnscl in zip(ctplist,scalelist) :
		absulutectp = ctpnscl[1] * ctpnscl[0]  + startlocation
		point_list.append(bspline(absulutectp))
		startlocation=absulutectp[-1]
	return point_list

		

class Generate_Trajectory(object):
	"""docstring for Gen"""
	#see matlab edtion
	def __init__(self, sval,):
		super(Gen, self).__init__()
		self.sval = sval
		self.twodim_bspline=twodim_bspline()
	def __call__(self,start_location,var_control_x_array,var_scale_y):
		#transform?
		
		dim=len(var_control_x_array)
		rawTrajecory_array=twodim_bspline(var_control_x_array)		

		return var_scale_y*rawTrajecory_array-rawTrajecory_array[0]+start_location

	def bspline_eval(self,var_control_x_array,var_scale_y):
		#uniform cubic b-spline
		
		return BSpline(var_control_x_array,[1],3)


	