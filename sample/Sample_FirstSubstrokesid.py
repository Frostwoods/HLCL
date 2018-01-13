# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_FirstSubstrokesid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 09:52:46
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-06 22:03:38
"""
Descripition:



Change Activity:
Undone para read


"""

class Sample_FirstSubstrokesid(object):
    """docstring for sampel_"""

    def __init__(self, samplepara, Samplemode):
        
        self.Sample = SampleMode
        self.NUM= samplepara['num']
        self.P =samplepara['p']        
    def __call__(self):

        return self.Sample(self.NUM, self.P)
