# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: generator_demo.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-12-21 21:32:13
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 20:03:23
"""
Descripition:



Change Activity:

undone  img_save


"""

import sys
sys.path.append('F:\Code\Matlab\HLCL')

from Generative model.Generate_Type import *
from Generative model.Generate_Token import *
import pickle
from Multinomial.Sample_Multinomial import Sample_Multinomial
from Gaussian.sample_multigaussian import sample_multigaussian
from scipy.stats import Gamma
from scipy.stats import randint
from Gaussian.sample_gaussian import sample_gaussian

from scipy.interpolate import BSpline
def img_save(img,id,defualtname='test'):


'======================15======================'
def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)        
def main():
	sampletime=100

	#load parameters  use pickle
	'''
	typeparafn='F:'
	tokenparafn='F'
	f=open('typeparafn.json',"r")
	f2=open('tokenparafn.json','r')
	typepara_dict=[json.loads(line) for line in f]
	tokenpara_dict=[json.loads(line) for line in f2]
	f.close()
	f2.close()
	'''
	typepara_dict=load_obj('typeparafn')
	tokenpara_dict=load_obj('tokenparafn')

	sap_multinomial=Sample_Multinomial()
	
	#type level
	sap_strokesnum=Sample_Kappa(typepara_dict['kappa'],Sample_Multinomial)
	sap_substrokenum=Sample_SubstrokesNum(typepara_dict['subnum'],Sample_Multinomial)
	sap_fstid=Sample_FirstSubstrokesid(typepara_dict['fst_id'],Sample_Multinomial)
	sap_subid=Sample_Substrokesid(typepara_dict['subid'],Sample_Multinomial)

	sap_substrokeid=Generate_Substrokes_ID(sap_fstid,sap_subid)	
	sap_crlpoints=Sample_Controlpoints(typepara_dict['ctlp'],sample_multigaussian)
	sap_scale=Sample_Scale(typepara_dict['scl'],Gamma.rvs)

	sap_relationid=Sample_Relationid(randint.rvs) 

	gen_stroke=Generate_Stroke(sap_substrokeid,sap_crlpoints,sap_scale)			
	gen_relation=Generate_Relation(typepara_dict['rlt'],Sample_Multinomial)
	
	gen_typechar=Generate_Type(sap_strokesnum,sap_substrokenum,
								gen_stroke,sap_relationid,gen_relation)	
	#tokenlevel

	gen_startloc=Generate_Startlocation(tokenpara_dict['strloc'],sample_multigaussian)
	
	adv_rl=addvar_relation(tokenpara_dict['nspara']['rlt'],sample_gaussian)
	adv_ctp=addvar_controlpoint(tokenpara_dict['nspara']['ctp'],sample_multigaussian)
	adv_scl=addvar_scale(tokenpara_dict['nspara']['scl'],sample_gaussian)

	gen_trj=Generate_Trajectory()

	noi_img=Generate_binaryimages_img(sap_tsf,sampguas,??)

	gen_img=Generate_Token(gen_startloc,adv_rl,adv_ctp,
				adv_scl,gen_trj,noi_img)

	#creat picture
	type_list=[gen_typechar() for i in range[sampletime]]

	img_list=[gen_img(t) for t in type_list]
	
	[img_save(img_list[i],i) for i in range(sampletime)]

	#visualazation
	
if __name__ =='__main__' :
	main()


