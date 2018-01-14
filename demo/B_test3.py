# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: B_test3.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-11 22:23:19
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 20:12:42
"""
Descripition:



Change Activity:



"""
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

def calculateAstroketrajectory( ctplist, scalelist,startlocation):
	
	point_list=[]		
	for ctpnscl in zip(ctplist,scalelist) :
		absulutectp = ctpnscl[1] * ctpnscl[0]  + startlocation
		point_list.append(bspline(absulutectp))
		startlocation=absulutectp[-1]
	return point_list

		
def darwastroke(img,astrokepoint_list,color = (123, 123, 123),line_width=1):
	"""docstring for Darwastroke"""

	for point in astrokepoint_list:
		pts = np.array(point, dtype=np.int32)
		pts = pts.reshape((-1, 1, 2))		
		cv2.polylines(img, [pts], False, color,thickness=line_width, lineType=8)
	return img

if __name__ == '__main__':

    ctp1 = np.array([[0, 0], [4, -2], [2, -5], [0, -8], [4, -9]])
    ctp2 = np.array([[0, 0], [1, 2], [3, 0], [2, -3], [0, -5]])
    ctp3 = np.array([[0, 0], [0, -1], [0, -2], [0, -3], [0, -4]])
    ctp4 = np.array([[0, 0], [1, 2], [2, 0], [3, -2], [4, 0]])
    substrokesctplist = [ctp1, ctp2, ctp3, ctp4]

    charsubnumlist=[2,3,4]
    charidlist=[[1,0],[0, 3, 1],[3,0,1,0]]
    charsclist=[[2,2],[5,5,5],[3,4,2,5]]
    charstartlocationlist=[np.array([20, 60]),np.array([30, 80]),np.array([50, 80])]
    
    charctplist=[[substrokesctplist[i] for i in subidlist] for subidlist in charidlist]

    img_width = 105
    img_length = 105
    r_img = np.ones((img_width, img_length, 3), np.uint8) * 255

    strokesctplist=[calculateAstroketrajectory(para[0],para[1],para[2]) for para in zip(charctplist,charsclist,charstartlocationlist)]
    r_img=reduce(darwastroke,strokesctplist,r_img)

    cv2.imshow("Art", r_img)
    cv2.waitKey(0)

