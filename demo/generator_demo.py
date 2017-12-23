# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: generator_demo.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-21 21:32:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 01:32:50
"""
Descripition:



Change Activity:

undone  img_save


"""

import sys
sys.path.append('F:\Code\Matlab\HLCL')

from Generative model.Generate_Type import *
from Generative model.Generate_Token import *

def img_save(img,id,defualtname='test'):



def main():
	sampletime=100
	GenAType_cls=Generate_Type()
	renderimg_cls=Generate_Token()
	type_list=[GenAType_cls() for i in range[sampletime]]
	img_list=[renderimg_cls(type_list[i]) for i in range[sampletime]]
	[img_save(img_list[i],i) for i in range(sampletime)]

	
if __name__ =='__main__' :
	main()
