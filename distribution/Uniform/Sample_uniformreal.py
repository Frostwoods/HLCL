# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_uniformreal.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-15 15:48:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-15 15:51:22
"""
Descripition:



Change Activity:

done


"""

from scipy.stats import  uniform
class sample_uniformreal():
    """Multinomial distribution for kappa"""

    def __init__(self ):
        '''NUM 取值域大小 P 各值对应概率 '''
		
        	#self.NUM = NUM
        pass
    def __call__(self, loc,scale,sampletimes=1):
        # Return a Sample 

        return uniform.rvs(loc,scale,sampletimes)
if __name__ =='__main__' :
    A=sample_uniformreal()

    print(A(2,3,8))