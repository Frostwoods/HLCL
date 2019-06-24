# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: B_test2.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-11 22:23:19
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-12 22:15:02
"""
Descripition:



Change Activity:



"""
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt


def bspline(cv, n=100, degree=3, periodic=False):
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
        factor, fraction = divmod(count+degree+1, count)
        cv = np.concatenate((cv,) * factor + (cv[:fraction],))
        count = len(cv)
        degree = np.clip(degree,1,degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree,1,count-1)


    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0-degree,count+degree+degree-1,dtype='int')
    else:
        kv = np.array([0]*degree + range(count-degree+1) + [count-degree]*degree,dtype='int')

    # Calculate query range
    u = np.linspace(periodic,(count-degree),n)


    # Calculate result
    arange = np.arange(len(u))
    points = np.zeros((len(u),cv.shape[1]))
    for i in xrange(cv.shape[1]):
        points[arange,i] = si.splev(u, (kv,cv[:,i],degree))

    return points


if __name__ =='__main__' :
	ctp1 = np.array([[0, 0], [4, -2], [2, -5], [0, -8], [4, -9]])
	ctp2 = np.array([[0, 0], [1, 2], [3, 0], [2, -3], [0, -5]])
	ctp3 = np.array([[0, 0], [0, -1], [0, -2], [0, -3], [0, -4]])
	ctp4 = np.array([[0, 0], [1, 2], [2, 0], [3, -2], [4, 0]])
	substrokesctplist=[ctp1,ctp2,ctp3,ctp4]
	
	scalelist=[1,1,0.7]
	substrokesnum=3
	subidlist=[0,3,1]
	fig = plt.figure(figsize=(105,105),dpi=500)
	#plt.axis('off')
	frame = plt.gca()
# y 轴不可见
	frame.axes.get_yaxis().set_visible(False)
# x 轴不可见
	frame.axes.get_xaxis().set_visible(False)

	ax = fig.add_subplot(111)
	startlocation=np.array([3,10])
	for i in range (substrokesnum):
		absulutectp= scalelist[i]*(substrokesctplist[subidlist[i]])+startlocation
		point = bspline(absulutectp)
		x = point[:,0]
		y = point[:,1]
		startlocation=absulutectp[4]
		plt.plot(x,y,label='153')
		#plt.legend(),linewidth=50

		print point
	plt.show()


class Darwastroke(object):
		"""docstring for Darwastroke"""
		def __init__(self, substrokesctplist):
			self.ctplist = substrokesctplist
		def __call__(self,substrokesnum,subidlist,scalelist):

			for i in range (substrokesnum):
				absulutectp= scalelist[i]*(substrokesctplist[subidlist[i]])+startlocation
				point = bspline(absulutectp)
				x = point[:,0]
				y = point[:,1]
				startlocation=absulutectp[4]
				plt.plot(x,y,label='153')
				plt.legend()
			plt.show()





	#plt.xlim([min(x) - 1.0, max(x) + 1.0])
	#plt.ylim([min(y) - 1.0, max(y) + 1.0])
	


