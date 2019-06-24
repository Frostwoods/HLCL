# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: generateRandomParses.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-10-30 14:57:12
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2019-06-11 19:17:52
"""
Descripition:
	HLCL SM 3.3


Change Activity:



"""
def generateRandomParses(I,lib,ninit,verbose=False):
	G=extract_skeleton(I,verbose)
	RW=randomWalker(G)
	PP = processParses(I,lib,verbose)
	[bestMP,score_sorted] = parsesToMPs(I,PP,ninit,lib,verbose)
	return bestMP