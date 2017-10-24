# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Gernerate_Type.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 14:35:37
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-23 19:08:53
"""
Descripition:
	part of Generative model for character
	type level
	Generate a new character type

	Input:
		unkown

	Output:
		Character type
		φ = {κ, S, R}
		κ: number of strokes
		S: strokes {S1, ……, Sκ}
		R: relations between strokes {R1, ……, Rκ}

Usage:


Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao


"""

κ = Sample_from_distribution('k')

for x in xrange(1,k):

	n(x) = Sample_from_distribution('n(x)|k')

	S(x) = Generate_Stroke(x, n(x))

	ξ(x) = Sample_from_distribution('ξ')

	R(x) = Sample_from_distribution('Ri|ξ, S1, ……, Sx')
φ = {k, R, S}


return φ
