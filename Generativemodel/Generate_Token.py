# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Token.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:46:53
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 21:22:49
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

class Generate_Token(object):
	"""docstring for Gen"""
	def __init__(self, gen_startloc,adv_rl,adv_ctp,adv_scl,gen_trj,noi_img):
		self.Generate_Startlocation=gen_startloc		
		self.addvar_relation=addvar_relation
		self.addvar_controlpoint=addvar_controlpoint
		self.addvar_scale=addvar_scale
		self.Generate_Trajectory=Generate_Trajectory
		slef.Generate_binaryimages_img=noi_img

	def __call__(self,Type_phi):
		kappa=Type_phi['storekesnum']
		m_relationset_list=Type_phi['relations']
		trajectory_list=[]
		start_loc=[]



		for i in xrange(kappa):
			#1:Indenpent 2:Start 3:End 4 :along
			if m_relationset_list[i]['relationid']==4:
				m_relationset_list[i]['relationpar']=addvar_relation(m_relationset_list[i]['relationpar'][2],std)
			sub_num=Type_phi['strokes'][i]['substorekesnum_int']
			start_loc.append=[Generate_Startlocation(self.m_relationset_list[i],self.trajectory_list)]
			
			var_control_x_array=[addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x']) for j in range(sub_num)]
			var_scale_y=[addvar_scale(Type_phi['strokes'][i]['scale_y']) for j in range(sub_num)]
			
			trajectory_list.append=Generate_Trajectory(self.start_location,self.var_control_x_array,self.var_scale_y)

			#for  j in xrange(Type_phi['strokes'][i]['substorekesnum_int']):
			#	var_control_x_array[j]=addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x'])
			#	var_scale_y[j]=addvar_scale(Type_phi['strokes'][i]['scale_y'])			

		I=self.Generate_binaryimages_img(Trajectory)

		return I

	
 












































































































































































































		
