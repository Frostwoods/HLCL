# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Stroke.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:25:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-22 19:41:35
"""
Descripition:
	Sample stroke 

	Input:
		serial number :i
		number of substrokes : ni
		unkown,

	Output:
		Si = {Si1, ……, Sini}



Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao
	

"""
zi(1) = Sample_from_distribution（'zi'）

for j in xrange(2, ni):
	zi(j) = Sample_from_distribution('zij|zi(j-1)')

for k in xrange(1, ni):
	xi(k) = Sample_from_distribution（'xik|zik'）
	yi(k) = Sample_from_distribution（'yik|zik'）
	si(k) = {xi(k), yi(k), zi(k)}

si = {si(1), ……, si(ni)}



