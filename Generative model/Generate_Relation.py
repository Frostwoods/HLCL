# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-27 00:11:48
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 02:33:05
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
from scipy.stats import randint
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

    def __init__(self):
        self.sample_indepent=Sample_Multinomial()
        
        self.matfn1 = '/home/weiliu/workspace/python/matlab/mat4py.mat'  
    def __call__(self, xi, Stroke_Set, num):
    	Relation_Dict={'relationid':None,'relationpara':None}
        self.num=num
        self.Stroke_Set=Stroke_Set
        #1:Indenpent 2:Start 3:End 4 :along
    	if xi == 1:
    		para=self.Gen_Indepentrelation(num)
    	elif xi == 2:
    		para=self.Gen_Startrelation()
    	elif xi == 3:
    		para=self.Gen_Endrelation()
	    elif xi == 4:
	    	para=self.Gen_Alongrelation()
    	else:
    		print "wrong relation "
    	Relation_Dict['relationid']=xi;
    	Relation_Dict['relationpara']=para;
        return Relation_Dict
    def Gen_Indepentrelation(self,num):
    	#需要重写
         self.independentmat_p_mat=sio.loadmat(self.matfn1)
         self.independentmat_p_array= np.reshape(self.independentmat_p_mat,self.independentmat_p_mat.size)
         sample=self.sample_indepent(self.independentmat_p_array.size,self.independentmat_p_array)
         r=self.independentmat_p_mat.shape[0]

    	return [sample[0]//r,sample[0]%r]
        

    def Gen_Startrelation(self):
    	# uniform 
    	return [randint.rvs(1, self.num)]

    def Gen_Endrelation(self):
    	# uniform
    	return [randint.rvs(1, self.num)]

    def Gen_Alongrelation(self):
    	# uniform s subS typelevel coor
        !!! 起始位置 tho
        mu=randint.rvs(self.num)
        nu=randint.rvs(self.Stroke_Set[mu]['substorekesnum_int'])
        
        tho=randint.rvs(1,6)
        #Stroke_Set(mu)['sbustrokes_list'](nu)['control_x_array'](tho)

    	return [mu,nu,tho]
 