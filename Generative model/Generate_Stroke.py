# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Stroke.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:25:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 01:59:22
"""
Descripition:
	Sample stroke

	Input:
		serial number :i [int]
		number of substrokes : ni [int]
		

	Output:
		Si: [ni_list of dict]



Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')

from sample.Sample_Controlpoints import *
from sample.Sample_Scale import *
from sample.Sample_FirstSubstrokesid import *
from sample.Sample_Substrokesid import *


class Generate_Stroke(object):
    """docstring for Generate_Sr"""
    def __init__(self, arg):
        self.Generate_Substrokes_ID=Generate_Substrokes_ID()
        self.Sample_Controlpoints=Sample_Controlpoints()
        self.Sample_Scale=Sample_Scale()

    def __call__(self, id, substrokes_num):
        SubstrokesID=[]
        substrokes_control_x=[]
        substrokes_Scale_y=[]
        substrokes_dictlist[]

        SubstrokesID += self.Generate_Substrokes_ID()
        for i in range(1, substrokes_num):
            SubstrokesID += self.Generate_Substrokes_ID(SubstrokesID[i - 1])
        
        for i in range(substrokes_num):
            substrokes_control_x += self.Sample_Controlpoints(SubstrokesID[i])
            substrokes_Scale_y += self.Sample_Scale(SubstrokesID[i])
            substrokes_dictlist +=[{'substrokesid_int': SubstrokesID(i),'control_x_array':substrokes_control_x(i),'scale_y':substrokes_Scale_y(i)}]
        
        return {'substorekesnum_int':substrokes_num,'sbustrokes_list':substrokes_dictlist} 

class Generate_Substrokes_ID(object):
    """docstring for Generate_Substrokes_ID"""

    def __init__(self):
        self.Sample_FirstSubstrokesid=Sample_FirstSubstrokesid()
        self.Sample_Substrokesid=Sample_Substrokesid()

    def __call__(self, formerid=None):
        if formerid is None:
            current_id = Sample_FirstSubstrokesid()
        else:
            current_id = Sample_Substrokesid(formerid)
        return current_id




        