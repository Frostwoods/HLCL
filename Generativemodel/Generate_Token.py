# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Token.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:46:53
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 18:25:04
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
		self.addvar_relation=adv_rl
		self.addvar_controlpoint=adv_ctp
		self.addvar_scale=adv_scl
		self.Generate_Trajectory=gen_trj
		self.Generate_binaryimages_img=noi_img

	def __call__(self,Type_phi):
		kappa=Type_phi['storekesnum']
		m_relationset_list=Type_phi['relations']
		trajectory_list=[]
		start_loc=[]



		for i in xrange(kappa):
			#1:Indenpent 2:Start 3:End 4 :along
			if m_relationset_list[i]['relationid']==4:
				m_relationset_list[i]['relationpar']=self.addvar_relation(m_relationset_list[i]['relationpar'][2],std)
			
			sub_num=Type_phi['strokes'][i]['substorekesnum_int']
			start_loc.append=[self.Generate_Startlocation(m_relationset_list[i],trajectory_list)]
			
			var_control_x_array=[self.addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x']) for j in range(sub_num)]
			var_scale_y=[self.addvar_scale(Type_phi['strokes'][i]['scale_y']) for j in range(sub_num)]
			
			trajectory_list.append=self.Generate_Trajectory(self.start_location,self.var_control_x_array,self.var_scale_y)

			#for  j in xrange(Type_phi['strokes'][i]['substorekesnum_int']):
			#	var_control_x_array[j]=addvar_controlpoint(Type_phi['strokes'][i]['substrokes_control_x'])
			#	var_scale_y[j]=addvar_scale(Type_phi['strokes'][i]['scale_y'])			

		#I=self.Generate_binaryimages_img(Trajectory)

		return {'staloc':start_loc,'trajectory':trajectory_list}

	
 












































































































































































































		
