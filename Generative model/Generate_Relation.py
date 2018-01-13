# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-27 00:11:48
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-11 22:01:33
"""
Descripition:

    Output dict
	Four relation types


		Independent; ???
			Ji;  multinomial on 2D
			Li

		Start;
			mu pre strokes uniform

		End;
			mu uniform

		Along
			mu uiniform
			nu  presubstrokes uniform
			tau ?? type-level spline coordinate


Change Activity:



"""

import scipy.io as sio   
import numpy as np
from __future__ import division #截断除法 3//4=0
import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
import scipy.io as sio 
from Multinomial.Sample_Multinomial import Sample_Multinomial


randint.rvs(1, 3, loc=0, size=1, random_state=None)

class Generate_Relation():
    """relation id  multinomial"""
    # then sample parameter given relation
l
    def __init__(self,sampaepara,sapmlemode_ind):

        self.sample_indepent=sapmlemode_ind()
        self.independentmat_p_mat=sampalepara['ind']['mat']

    def __call__(self, xi, Stroke_Set, num):
    	Relation_Dict={}
        
        #1:Indenpent 2:Start 3:End 4 :along
        fun_dict{'along':genInet,}
    	para_para
        if xi == 0:
    		para=self.Gen_Indepentrelation(num)
    	elif xi == 1:
    		para=self.Gen_Startrelation(num)
    	elif xi == 2:
    		para=self.Gen_Endrelation(num)
	    elif xi == 3:
	    	para=self.Gen_Alongrelation(Stroke_Set)
    	else:
    		print "wrong relation "
    	Relation_Dict['relationid']=xi;
    	Relation_Dict['relationpara']=para;
        return Relation_Dict
    def Gen_Indepentrelation(self,num):
    	#需要重写
        
         sample=self.sample_indepent(size(sief.independentmat_p_mat),sief.independentmat_p_mat.flatten())
         r=self.independentmat_p_mat.shape[0]

    	return [sample[0]//r,sample[0]%r]
        

    def Gen_Startrelation(self):
    	# uniform 
    	return [randint.rvs(0, num)]

    def Gen_Endrelation(self):
    	# uniform
    	return [randint.rvs(0, num)]

    def Gen_Alongrelation(self):
    	# uniform s subS typelevel coor
       
        mu=randint.rvs(self.num)
        nu=randint.rvs(self.Stroke_Set[mu]['substorekesnum_int'])
        
        tho=randint.rvs(0,5)
        #Stroke_Set(mu)['sbustrokes_list'](nu)['control_x_array'](tho)

    	return [mu,nu,tho]
 