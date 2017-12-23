# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: sample_multigaussian.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-14 19:22:49
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-16 13:53:41
"""
Descripition:



Change Activity:
done

"""
from scipy.stats import  multivariate_normal
class sample_multigaussian():
    """Multinomial distribution for kappa"""

    def __init__(self ):
        '''NUM 取值域大小 P 各值对应概率 '''
		
        	#self.NUM = NUM

    def __call__(self, mean, cov,sampletimes=1):
        # Return a Sample 

        return multivariate_normal.rvs(mean,cov,sampletimes)
if __name__ =='__main__' :
    A=sample_multigausssian()

    print(A([0,1],[[1,0],[0,1]],8))