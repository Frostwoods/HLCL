# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: constsaver.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 16:42:29
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-22 17:13:56
"""
Descripition:
	const saver for project HLCL
	rule:
		Const name must be all uppercase
		Const value cannot be modified

Usage:
	
	add const in this file

		const.CONST = 2333


	when use const in another file:

		#add this on the head
		import const
		import constsaver

		#then call const you need
		Output=Do_Sth(Input, default=const.CONST)

Change Activity:
	None


"""
import const

const.HAHA = 3

