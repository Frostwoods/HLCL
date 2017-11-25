# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Multinomial.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-03 09:47:49
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-21 18:54:31
"""
Descripition:
	Sample in Multinomial distribution
	init

	call
    
    related function
        Sample_kappa
        Sample_FirstSubstrokesid
        Sample_SubstrokesNum
        Sample_Substrokesid


Change Activity:



"""
class Sample_Multinomial():
    """Multinomial distribution for kappa"""

    def __init__(self):
        '''NUM 取值域大小 P 各值对应概率 '''
        pass
            #self.NUM = NUM

    def __call__(self, NUM=none,P=none,sampletimes=1):
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
'''
class Sample_Multinomial():
    """Multinomial distribution for kappa"""

    def __init__(self, NUM=none, P=none):
        #NUM 取值域大小 P 各值对应概率 
		self.NUM = NUM
        if P is None:
        	if NUM is None:
        		self.gen_NUM()
        	self.gen_P()
        else:
        	self.P = P
        	#self.NUM = NUM

    def __call__(self, sampletimes=1):
        # Return a Sample 
        sample = np.zeros(sampletimes)
        for x in xrange(0, sampletimes):
            One_sample = multinomial.rvs(1, self.probabilities)
            sample[x] = np.where(One_sample == 1)[0] + 1        
        return sample

    def gen_NUM(self, maxnumber=10):
    	#random generate the size of distribution 
        self.NUM = np.random.randint(1, maxnumber)

    def gen_P(self):
        #sample P in dirichlet distribution 
        prior =np.random.randint(1, 10, self.NUM)
        # fix prior =（120，22，23，……，）
        self.P = dirichlet.rvs(prior)[0]

'''