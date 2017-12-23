# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Token.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:46:53
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 07:14:03
"""
Descripition:
	 Draw Characher Image Given a character type φ

	 Input:
		character type φ [dict]

	 Output:
	 	a character image I [n*n array]


Change Activity:
	 10.22 add pseudo code(undone) by Yang Zhao 没看懂 需计算机图形学补课 


"""
import sys
sys.path.append('F:\Code\Matlab\HLCL')
from Generative model.Generate_Startlocation import *
from Generative model.Generate_Trajectory import *
from Generative model.Generate_binaryimages_img import *

from sample.addvar_relation import *
from sample.addvar_controlpoint import *
from sample.addvar_scale import *
from sample.Sample_Transformationnumber import *
from sample.Sample_Gaufliter import *
from sample.Sample_Radomflips import *

class Generate_Token(object):
	"""docstring for Gen"""
	def __init__(self, arg):
		self.Generate_Startlocation=Generate_Startlocation()		
		self.addvar_relation=addvar_relation()
		self.addvar_controlpoint=addvar_controlpoint()
		self.addvar_scale=addvar_scale()
		self.Generate_Trajectory=Generate_Trajectory()
		self.Sample_Transformationnumber=Sample_Transformationnumber()		
	
	def __call__(self,Type_phi):
		self.Kappa_int=Type_phi['storekesnum']
		self.m_relationset_list=Type_phi['relations']
		self.trajectory_list=[]
		self.start_location=[]

		for i in xrange(self.Kappa):
			#1:Indenpent 2:Start 3:End 4 :along
			if self.m_relationset_list[i]['relationid']==4:
				self.m_relationset_list[i]['relationpar']=addvar_relation(self.m_relationset_list[i]['relationpar'][2],std)
			
			self.start_location+=[Generate_Startlocation(self.m_relationset_list[i],self.trajectory_list)]
			
			var_control_x_array=[addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x']) for j in range(Type_phi['strokes'][i]['substorekesnum_int'])]
			var_scale_y=[addvar_scale(Type_phi['strokes'][i]['scale_y']) for j in range(Type_phi['strokes'][i]['substorekesnum_int'])]
			
			self.Trajectory[i]=Generate_Trajectory(self.start_location,self.var_control_x_array,self.var_scale_y)

			#for  j in xrange(Type_phi['strokes'][i]['substorekesnum_int']):
			#	var_control_x_array[j]=addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x'])
			#	var_scale_y[j]=addvar_scale(Type_phi['strokes'][i]['scale_y'])			
		A=Sample_Transformationnumber()
		Eposilon=Sample_Gaufliter()
		Sigma=Sample_Radomflips()
		
		I=Generate_binaryimages_img(self.Trajectory,A,Eposilon,Sigma)

		return I

	
 












































































































































































































		
