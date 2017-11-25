# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Sample_from_distribution.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:21:58
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-06 08:03:05
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
        狄拉克分布（冲击分布） 

"""
import numpy as np
from scipy.stats import multinomial, dirichlet, gamma, multivariate_normal
import const

class Multinomial():
    """Multinomial distribution for kappa"""

    def __init__(self, p = None):
        #self.valuenumber = None
        #self.const.VALUENUMBER=
        self.probabilities = None
        if p is None:
            self.set_max_numbers()
            self.set_random_probabilities()
        else:
            self.probabilities = p
            self.const.VALUENUMBER = len(p)

        self.temporary_sample = None
    def __call__(self,arg):
        #Sample
        # Commander rule
        pass


    def set_max_numbers(self, maxnumber=None):
        if maxnumber is None:
            self.const.VALUENUMBER = np.random.randint(1, 10)
        else:
            self.const.VALUENUMBER = maxnumber


    def set_random_probabilities(self):
        # set get 成对出现
        # 输入 输出
        prior = np.random.randint(1, 10, self.valuenumber)
        #fix prior =（120，22，23，……，）

        self.probabilities = dirichlet.rvs(prior)[0]


    def learn_distribution(self,data = None):
        # learn probabilities

        pass

    def sample_from_multinomial(self, sampletimes=1):
        if self.valuenumber is None:
            self.set_random_numbers()
            self.set_random_probabilities()

        sample = np.zeros(sampletimes)

        for x in xrange(0, sampletimes):
            One_sample = multinomial.rvs(1, self.probabilities)
            sample[x] = np.where(One_sample == 1)[0] + 1

        self.temporary_sample = sample




class Markov_Martrix():
    """first-order Markov Processe"""
    #multivariate_normal


    def __init__(self):
        pass

    def Set_parameter():
        pass

    def Learn_parameter():
        pass

    def sample():
        pass

        
class Multi_Gaussian():
    """控制点取样"""
    #inverse wishart
    def __init__(self, arg):
        pass
    def Set_parameter():
        pass

    def Learn_parameter():
        pass
    def sample():
        pass

class Gamma():
    """docstring for ClassName"""
    def __init__(self):
        pass
    def Set_parameter():
        pass

    def Learn_parameter():
        pass
    def sample():
        pass
        self.arg = arg
        

        
class Dirac(object):
    """docstring for ClassName"""
    #狄拉克δ函数_ 
    def __init__(self, arg):
        pass




        





def main():
    # test funcion
    test = Sample_Multinomial()
    test.sample_from_multinomial(5)
    print test.temporary_sample


if __name__ == "__main__":
    main()
