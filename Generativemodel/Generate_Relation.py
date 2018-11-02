# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-27 00:11:48
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-08 11:08:45
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
from __future__ import division #截断除法 3//4=0

import numpy as np
from random import randint

#randint.rvs(1, 3, loc=0, size=1, random_state=None)

class Generate_Relation():
    """relation id  multinomial"""
    # then sample parameter given relation

    def __init__(self,sampaepara,sapmlemode_ind):

        self.sample_indepent=sapmlemode_ind
        self.independentmat_p_mat=sampaepara['ind']['mat']

    def __call__(self, xi, Stroke_Set, num):
        Relation_Dict={}
        
        #1:Indenpent 2:Start 3:End 4 :along
       # fun_dict{'along':genInet,}
        #para_para
        if xi == 0:
            para=self.Gen_Indepentrelation(num)
        elif xi == 1:
            para=self.Gen_Startrelation(num)
        elif xi == 2:
            para=self.Gen_Endrelation(num)
        elif xi == 3:
            para=self.Gen_Alongrelation(num,Stroke_Set)
        else:
            print "wrong relation "
        Relation_Dict['relationid']=xi;
        Relation_Dict['relationpara']=para;
        return Relation_Dict
    def Gen_Indepentrelation(self,num):
        #需要重写
        
        sample=self.sample_indepent(len(self.independentmat_p_mat)^2,reduce(lambda x,y:x+y,self.independentmat_p_mat))
        r=len(self.independentmat_p_mat)
        print [sample[0]//r,sample[0]%r]
        return [sample[0]//r,sample[0]%r]

    def Gen_Startrelation(self,num):
        # uniform 
        return [randint(0, num)]

    def Gen_Endrelation(self,num):
        # uniform
        return [randint(0, num)]

    def Gen_Alongrelation(self,num,Stroke_Set):
        # uniform s subS typelevel coor
       
        mu=randint(0,num)
        nu=randint(0,Stroke_Set[mu]['substorekesnum_int'])
        
        tho=randint(0,5)
        #Stroke_Set(mu)['sbustrokes_list'](nu)['control_x_array'](tho)

        return [mu,nu,tho]
 