# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: test_search_substrokes.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-13 13:19:17
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-13 13:31:50
"""
Descripition:



Change Activity:



"""
from ddt import ddt,data,file_ate,unpack
import unittest 
import search_substrokes as targetCode

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

    @data(((1,1),(3,3),0),((0,3),(2,0),np.pi/2.0))
    @unpack
    def test_Multinomial(self,v1,v2,p):
    	self.assertEqual(target.cal_angles_two_vectors(v1,v2),p)

