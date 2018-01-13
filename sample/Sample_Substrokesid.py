# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Substrokesid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 09:53:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-06 21:59:39
"""
Descripition:



Change Activity:
Undone para reading


"""

class Sample_Substrokesid(object):
    """docstring for sampel_"""

    def __init__(self, samplepara, Samplemode):

        self.markov_mat=samplepara['markovmat']
        self.num=samplepara['num']
        self.Sample = SampleMode()

    def __call__(self,former_subStroke_id):
    	#self.read_parameter(Former_SubStroke_id)
        
        return self.Sample(self.num, self.markov_mat[former_subStroke_id,:])

