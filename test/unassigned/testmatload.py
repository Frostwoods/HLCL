# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: testmatload.py
# @Author: Yang Zhao psy
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-11 21:04:40
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-11 21:11:37
"""
Descripition:



Change Activity:



"""
import scipy.io as sio

data = sio.loadmat('F:/Code/Matlab/HLCL/classes/lutendpoint.mat')
data2=sio.loadmat('F:/Code/Matlab/HLCL/HLCLdefault.mat')
print data['lut'][0]
print data2