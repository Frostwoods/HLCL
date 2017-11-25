# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Generate_Relation.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-27 00:11:48
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-21 20:23:34
"""
Descripition:
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
randint.rvs(1, 3, loc=0, size=1, random_state=None)

class Generate_Relation():
    """relation id  multinomial"""
    # then sample parameter given relation

    def __init__(self):
        pass

    def __call__(self, xi, Stroke_Set, num):
    	Relation_Dict={'relationid':None,'relationpara':None}
        self.num=num
        self.Stroke_Set=Stroke_Set
    	if xi == 1:
    		para=self.Gen_Indepentrelation()
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
    def Gen_Indepentrelation(self):
    	

    	return

    def Gen_Startrelation(self):
    	# uniform 


    	return randint.rvs(1, self.num)

    def Gen_Endrelation(self):
    	# uniform
    	return randint.rvs(1, self.num)

    def Gen_Alongrelation(self):
    	# uniform s subS typelevel coor
        mu=randint.rvs(1, self.num)
        nu=randint.rvs(1,self.Stroke_Set(mu)['substorekesnum_int']+1)
        tho=randint.rvs(1,6)
        #Stroke_Set(mu)['sbustrokes_list'](nu)['control_x_array'](tho)

    	return (mu,nu,tho)
