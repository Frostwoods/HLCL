# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Framework_CharacterToken.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-19 21:06:51
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-15 13:26:12
"""
Descripition:



Change Activity:



"""
Typelevel
Type_phi
charactertype_dict={'storekesnum':Int,'relations':relations_list,'strokes':strokes_list}

relations_list=[relation_dict,…，] 
relation_dict={'relationid'：None，'relationpara':None}

strokes_list=[stroke_dict_1，……，stroke_dict_k]
stroke_dict={'substorekesnum_int':,'sbustrokes_list':}
substrokes_dict={'substrokesid_int': SubstrokesID,'control_x_array':substrokes_control_x,'scale_y':substrokes_Scale_y,}            
       # return Storke_Integrate()


Tokenlevel

charactertoken_dict={'stratlocation':None,'control_x_array_m':None,'scale_y_m':None，
					'stroke_trajectory':None,'relation_m':None,	'image_transformation_A':None，	
					'gaussian_filter_blurring':sigma,'bernoulli_flips':epsilon	
					}\

