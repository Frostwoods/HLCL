# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: typegenerator_test.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-21 21:32:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 18:20:52
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
from Generativemodel.Generate_Startlocation import *
from Generativemodel.Generate_Trajectory import *
from Generativemodel.Generate_Token import *
#from Generativemodel import *
from sample.typesample import *
from sample.tokensample import *
from distribution.distribution import *
import pickle


from scipy.stats import randint,gamma


#from scipy.interpolate import BSpline
#def img_save(img,id,defualtname='test'):


def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)     
def main():
	sampletime=3

	path='F:/Code/Matlab/HLCL/demo/faketypepara.pkl'
	path2='F:/Code/Matlab/HLCL/demo/faketokenpara.pkl'
	typepara_dict=load_obj(path)
	tokenpara_dict=load_obj(path2)
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

	gen_startloc=Generate_Startlocation(tokenpara_dict['strloc'],sample_multigaussian)
	
	adv_rl=addvar_relation(tokenpara_dict['nspara']['rlt'],sample_gaussian)
	adv_ctp=addvar_controlpoint(tokenpara_dict['nspara']['ctp'],sample_multigaussian)
	adv_scl=addvar_scale(tokenpara_dict['nspara']['scl'],sample_gaussian)

	gen_trj=calculateAstroketrajectory

	#noi_img=Generate_binaryimages_img(sap_tsf,sampguas,??)
	noi_img=[]
	gen_token=Generate_Token(gen_startloc,adv_rl,adv_ctp,
				adv_scl,gen_trj,noi_img)


	#creat picture
	type_list=[gen_typechar() for i in range(sampletime)]
	print gen_typechar(),'1234'
	print type_list[0],'-------',type_list[1]
	print gen_token(type_list[0])
	#visualazation
	
if __name__ =='__main__' :
	main()


