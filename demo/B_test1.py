# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: B_test1.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-11 22:01:26
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-11 22:17:00
"""
Descripition:



Change Activity:



"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si

points = np.array([[1, 10], [7, 8], [5, 5], [3, 2], [9, 1]])
x = points[:,0]
y = points[:,1]

t = range(len(x))
knots = [2]
ipl_t = np.linspace(0, 11 , 100)

x_tup = si.splrep(t, x, k=3, t=knots)
y_tup = si.splrep(t, y, k=3, t=knots)
print len(x_tup)
x_i = si.splev(ipl_t, x_tup)
print len(x_i)
y_i = si.splev(ipl_t, y_tup)

print 'knots:', x_tup,'down'

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, y, label='original')
#plt.plot(x_tup, y_tup, label='splinepoint')
plt.plot(x_i, y_i, label='spline')
plt.xlim([min(x) - 1.0, max(x) + 1.0])
plt.ylim([min(y) - 1.0, max(y) + 1.0])
plt.legend()
plt.show()