# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: sample_gaussian.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-14 19:22:49
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-15 15:38:28
"""
Descripition:



Change Activity:

Done

"""
from scipy.stats import  norm
class sample_gausssian():

    def __init__(self ):
 		pass
    def __call__(self, Mean, Cov,sampletimes=1):
        # Return a Sample            

        return norm.rvs ( Mean, Cov,sampletimes)

    

if __name__ =='__main__' :
	A=sample_gausssian()

	print(A(0,1,8))