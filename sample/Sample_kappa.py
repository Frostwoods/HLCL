# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_kappa.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:42:41
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-20 14:30:01
"""
Descripition:



Change Activity:



"""


class Sample_kappa(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):

        self.read_parameter()
        self.Sample = SampleMode()

    def __call__(self):

        return self.Sample(self.NUM, self.P)

    def read_parameter(self):
        self.NUM, self.P = someloadingfunciton()
