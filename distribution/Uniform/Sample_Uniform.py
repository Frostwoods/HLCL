# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Uniform.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-21 19:09:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-21 20:02:43
"""
Descripition:



Change Activity:



"""
from scipy.stats import randint
class Sample_Uniform():
    """Multinomial distribution for kappa"""

    def __init__(self):
        '''NUM 取值域大小 P 各值对应概率 '''
        pass
            #self.NUM = NUM

    def __call__(self, NUM=none,sampletimes=1):
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
            One_sample = multinomial.rvs(1, self.probabilities)
            sample[x] = np.where(One_sample == 1)[0] + 1        
        return sample

    def gen_NUM(self, maxnumber=10):
        '''random generate the size of distribution '''
        self.NUM = np.random.randint(1, maxnumber)

    def gen_P(self):
        '''sample P in dirichlet distribution '''
        prior =np.random.randint(1, 10, self.NUM)
        # fix prior =（120，22，23，……，）
        self.P = dirichlet.rvs(prior)[0] 