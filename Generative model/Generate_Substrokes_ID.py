# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Substrokes_ID.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-23 10:59:24
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-06 22:27:21
"""
Descripition:



Change Activity:



"""
class Generate_Substrokes_ID(object):
    """docstring for Generate_Substrokes_ID"""

    def __init__(self,Sample_FirstSubstrokesid,Sample_Substrokesid):
        self.Sample_FirstSubstrokesid=Sample_FirstSubstrokesid
        self.Sample_Substrokesid=Sample_Substrokesid

    def __call__(self, formerid):
        if formerid==None :
            current_id = Sample_FirstSubstrokesid()
        else:
            current_id = Sample_Substrokesid(formerid)
        return current_id