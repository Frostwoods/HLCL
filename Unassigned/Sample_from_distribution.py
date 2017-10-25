# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Sample_from_distribution.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:21:58
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-10-25 20:12:42
"""
Descripition:
    Sample from a given distribution

    Input: 
         distribution type:{
                




            }   
         parameter 什么数据格式能兼容？
    

    Output：
         a sample
Usage:



Change Activity:
10.25 mutinomial finished, add markov , gassuian , gamma
    

Comment:
    hard work ahh
    定义一个分布的类：自由的增加分布种类
    输入数据类型：整合的参数输入方式

    目前需要包含的分布
        多项式分布 √
        高斯分布
        马尔科夫过程
        伽马分布 

"""
import numpy as np
from scipy.stats import multinomial, dirichlet, gamma, multivariate_normal


class kappa_Multinomial():
    """Multinomial distribution for kappa"""

    def __init__(self):
        self.valuelist = None
        self.valuenumber = None
        self.probabilities = None
        self.temporary_sample = None

    def learn_distribution(self):
        # learn probabilities
        pass

    def set_max_numbers(self, maxnumber=None):
        if maxnumber is None:
            self.valuenumber = np.random.randint(1, 10)
        else:
            self.valuenumber = maxnumber
        print self.valuenumber

    def set_random_probabilities(self, defaultupper=10):
        prior = np.random.randint(1, defaultupper, self.valuenumber)
        self.probabilities = dirichlet.rvs(prior)[0]
        print self.probabilities

    def sample_from_multinomial(self, sampletimes=1):
        if self.valuenumber is None:
            self.set_random_numbers()
            self.set_random_probabilities()

        sample = np.zeros(sampletimes)
        for x in xrange(0, sampletimes):
            One_sample = multinomial.rvs(1, self.probabilities)
            sample[x] = np.where(One_sample == 1)[0] + 1
        self.temporary_sample = sample


class SubStrokes_Multinomial():
    """docstring for ClassName"""
    # 父类继承 多项式分布

    def __init__(self):
        pass


class Markov_Martrix(object):
    """first-order Markov Processe"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

class Gaussian():
    """控制点取样"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

class Gamma():
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        

class Relasions():
    """relation id  multinomial"""
    #then sample parameter given relation

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        




def main():
    # test funcion
    test = kappa_Multinomial()
    test.sample_from_multinomial(5)
    print test.temporary_sample


if __name__ == "__main__":
    main()
