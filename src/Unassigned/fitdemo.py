# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: fitdemo.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-11 18:41:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2019-06-11 19:01:52
"""
Descripition:



Change Activity:



"""
from PIL import Image
K = 5
verbose = true
include_mcmc = false
fast_mode = true
filename = 'F:/Code/Matlab/BPL-master/bottomup/testimg/zhe.png'
img = Image.open(filename).convert('L')
G== fitMotorprograms(img,K,verbose,include_mcmc,fast_mode);