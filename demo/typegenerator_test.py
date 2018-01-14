# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: typegenerator_test.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-21 21:32:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 23:29:54
"""
Descripition:



Change Activity:

undone  img_save


"""

import sys
sys.path.append('F:\Code\Matlab\HLCL')
sys.path.append('F:\Code\Matlab\HLCL\distribution')
from Generativemodel.Generate_Substrokes_ID import *
from Generativemodel.Generate_Stroke import *
from Generativemodel.Generate_Relation import *
from Generativemodel.Gernerate_Type import *
#from Generativemodel import *
from sample.typesample import *
from distribution.distribution import *
import pickle


from scipy.stats import randint,gamma


#from scipy.interpolate import BSpline
#def img_save(img,id,defualtname='test'):


def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)     
def main():
	sampletime=100

	path='F:/Code/Matlab/HLCL/demo/faketypepara.pkl'

	typepara_dict=load_obj(path)
	#tokenpara_dict=load_obj('tokenparafn')
	#print typepara_dict
	sap_multinomial=Sample_Multinomial()
	
	#type level

	sap_strokesnum=Sample_Kappa(typepara_dict['kappa'],sap_multinomial)
	sap_substrokenum=Sample_SubstrokesNum(typepara_dict['subnum'],sap_multinomial)
	sap_fstid=Sample_FirstSubstrokesid(typepara_dict['fst_id'],sap_multinomial)
	sap_subid=Sample_Substrokesid(typepara_dict['subid'],sap_multinomial)

	sap_substrokeid=Generate_Substrokes_ID(sap_fstid,sap_subid)	
	sap_crlpoints=Sample_Controlpoints(typepara_dict['ctlp'],sample_multigaussian)
	sap_scale=Sample_Scale(typepara_dict['scl'],gamma.rvs)

	sap_relationid=Sample_Relationid(randint.rvs) 

	gen_stroke=Generate_Stroke(sap_substrokeid,sap_crlpoints,sap_scale)			
	gen_relation=Generate_Relation(typepara_dict['rlt'],sap_multinomial)
	
	gen_typechar=Generate_Type(sap_strokesnum,sap_substrokenum,
								gen_stroke,sap_relationid,gen_relation)	
	#tokenlevel


	print gen_typechar()
	#creat picture
	type_list=[gen_typechar() for i in range(sampletime)]
	print type_list
	#visualazation
	
if __name__ =='__main__' :
	main()


