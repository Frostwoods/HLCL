# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: typesample.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-14 21:50:17
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-10 20:28:48
"""
Descripition:



Change Activity:



"""
from scipy.stats import randint


class Sample_Kappa(object):
    """docstring for sampel_"""

    def __init__(self, samplepara, samplemode):
        self.sample = samplemode
        self.NUM = samplepara['num']
        self.P = samplepara['p']

    def __call__(self):
        return int(self.sample(self.NUM, self.P)[0]+1)


class Sample_FirstSubstrokesid(object):
    """docstring for sampel_"""

    def __init__(self, samplepara, Samplemode):
        self.Sample = Samplemode
        self.NUM = samplepara['num']
        self.P = samplepara['p']

    def __call__(self):
        return self.Sample(self.NUM, self.P)


class Sample_Substrokesid(object):
    """docstring for sampel_"""

    def __init__(self, samplepara, Samplemode):
        self.markov_mat = samplepara['markovmat']
        self.num = samplepara['num']
        self.Sample = Samplemode

    def __call__(self, former_subStroke_id):
        # self.read_parameter(Former_SubStroke_id)

        return self.Sample(self.num, self.markov_mat[former_subStroke_id])


class Sample_Controlpoints():
    def __init__(self, samplepara, samplemode):
        self.sample = samplemode()
        self.mean_list = samplepara['mean']
        self.cov_list = samplepara['cov']

    def __call__(self, SubstrokesID):
       
        return self.sample(self.mean_list[SubstrokesID], self.cov_list[SubstrokesID])


class Sample_Relationid(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode):
        self.num = 4
        self.Sample = SampleMode

    def __call__(self, i):
        return randint.rvs(0, self.num)


class Sample_Scale(object):
    """docstring for S"""

    def __init__(self, samplepara, samplemode):

        self.sample = samplemode
        self.alpha_list = samplepara['alpha']
        self.beta_list = samplepara['beta']

    def __call__(self, SubstrokesID):
        return self.sample(self.alpha_list[SubstrokesID], scale=1 / self.beta_list[SubstrokesID])


class Sample_SubstrokesNum(object):
    """docstring for sampel_"""

    def __init__(self, para, SampleMode):
        self.Sample = SampleMode
        self.para = para
        #self.matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat'

    def __call__(self, Stroke_order):
        if Stroke_order > 2:
            Stroke_order = 2
        return int(self.Sample(self.para[Stroke_order]['num'], self.para[Stroke_order]['p'])[0]+1)
