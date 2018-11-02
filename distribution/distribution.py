# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: distribution.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-14 21:41:19
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 18:18:25
"""
Descripition:



Change Activity:



"""
from scipy.stats import  multivariate_normal,norm,multinomial,dirichlet
import numpy as np

class sample_multigaussian():
    """Multinomial distribution for kappa"""

    def __init__(self ):
        '''NUM 取值域大小 P 各值对应概率 '''
		
        	#self.NUM = NUM

    def __call__(self, mean, cov,sampletimes=1):
        # Return a Sample 

        return multivariate_normal.rvs(mean,cov,sampletimes)

class sample_gaussian():

    def __init__(self ):
 		pass
    def __call__(self, Mean, Cov,sampletimes=1):
        # Return a Sample            

        return norm.rvs ( Mean, Cov,sampletimes)

class Sample_Multinomial():
    """Multinomial distribution for kappa"""

    def __init__(self):
        '''NUM 取值域大小 P 各值对应概率 '''
        pass
            #self.NUM = NUM

    def __call__(self, NUM=None,P=None,sampletimes=1):
        self.NUM = NUM
        if P is None:
            if NUM is None:
                self.gen_NUM()
            self.gen_P()
        else:
            self.P = P
        # Return a Sample 
        sample = np.zeros(sampletimes)
        for x in xrange(0, sampletimes):
            One_sample = multinomial.rvs(1 , self.P)
            sample[x] = np.where(One_sample == 1)[0]   
        return sample

    def gen_NUM(self, maxnumber=10):

        '''random generate the size of distribution '''
        self.NUM = np.random.randint(1, maxnumber)

    def gen_P(self):
        '''sample P in dirichlet distribution '''
        prior =np.random.randint(0, 10, self.NUM)
        # fix prior =（120，22，23，……，）
        self.P = dirichlet.rvs(prior)[0]


if __name__ =='__main__' :
    A=sample_multigausssian()

    print(A([0,1],[[1,0],[0,1]],8))