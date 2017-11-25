# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: constsaver.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 16:42:29
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-27 20:14:03
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
import copy
const.HAHA = 3
const.VALUENUMBER=10 #kappa 的值
class test(object):
	"""docstring for test"""
	def __init__(self, arg):
		#super(test, self).__init__()
		const.ARG = arg
		self.ARG=copy.deepcopy(const.ARG)


def main():
	k=test(3)
	print k.ARG
	k.ARG=4
	print k.ARG


if __name__ =="__main__":
	main()