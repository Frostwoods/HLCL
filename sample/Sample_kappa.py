# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_kappa.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-01 10:42:41
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-11 22:01:34
"""
Descripition:
	
	Output kappa: [int] 


Change Activity:
Undone pararead


io as sio 
"""

class Sample_Kappa(object):
    """docstring for sampel_"""

    def __init__(self,samplepara, samplemode ):

      
        self.sample = samplemode()
        self.NUM= samplepara['num']
        self.P =samplepara['p']
    def __call__(self):

        return self.sample(self.NUM, self.P)
