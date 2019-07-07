# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: test_likelyhood.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-12 19:31:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-12 21:11:10
"""
Descripition:



Change Activity:



"""
from ddt import ddt,data,file_ate,unpack
import unittest 
import likelyhood as target

def add(a,b):
    c = a+b
    return c

@ddt
class Mytest(unittest.TestCase):
	"""docstring for Mytest"""
	@data((1,1,2), (1,2,3))
    @unpack
    def test_addnum(self,a, b, expected_value):
        self.assertEqual(add(a,b),expected_value)

    @data()
    @unpack
    def test_Multinomial(self,var,p_list,p):
    	self.assertEqual(target.Multinoial_likelyhood(var,p_l),p)

    

