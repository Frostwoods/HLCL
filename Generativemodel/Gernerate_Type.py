# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Gernerate_Type.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 14:35:37
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-08 10:57:19
"""
Descripition:
	part of Generative model for character
	type level
	Generate a new character type

	Input:
		unkown

	Output:
		Character type
		φ = {κ, S, R}
		κ: number of strokes
		S: strokes {S1, ……, Sκ}
		R: relations between strokes {R1, ……, Rκ}

Usage:


Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao


"""
"""
κ = Sample_from_distribution('k')

for x in xrange(1,k):

	n(x) = Sample_from_distribution('n(x)|k')

	S(x) = self.Generate_Stroke(x, n(x))

	ξ(x) = Sample_from_distribution('ξ')

	R(x) = Sample_from_distribution('Ri|ξ, S1, ……, Sx')
φ = {k, R, S}


return φ
"""


class Generate_Type(object):
	"""docstring for Generate_Type"""
	def __init__(self,sap_kappa,gen_subnum,gen_stroke,sap_rlid,gen_rl):		
		self.sample_kappa=sap_kappa

		self.sample_substrokesNum=gen_subnum
		self.generate_stroke=gen_stroke

		self.sample_Relationid=sap_rlid
		self.generate_Relation=gen_rl

				
	def __call__(self,kappa=None):
		if kappa is None:	
			kappa = self.sample_kappa()

		n= [self.sample_substrokesNum(i) for i in  range(kappa)]
		
		storke= [self.generate_stroke(ni) for ni in n]
		#

		relaitonid=[self.sample_Relationid(i) for i in range(kappa)]
		relationset=[[self.generate_Relation(relaitonid[i],storke,i)] for i in range(kappa)]

		relationset=[self.generate_Relation(item,storke,i) for (i,item) in enumerate(relaitonid)]

		type_dict={'storekesnum':kappa,'relations':relationset,'strokes':storke}
		return type_dict

'''
	def Generate_wrap(self,Kappa):
		#,Sample_SubstorkesNum,self.Generate_Stroke,Sample_Relationid,Generate_Relation
		n=[]
		Storke =[] 
		Xi = []
		RelationSet=[]
		for i in range(Kappa):

			self.n += self.Sample_SubstorkesNum(self.Kappa)

			self.Storke += [self.Generate_Stroke(i,self.n[i])]

			self.Xi += self.Sample_Relationid()

			self.RelationSet += [self.Generate_Relation(Xi[i], self.Storke , i)]
		return n,Storke,Xi,RelationSet

'''
				
"""
Kappa = Sample_kappa()

for i in xrange(1,Kappa)

	self.n(i) = Sample_SubstorkesNum(Kappa)

	self.Storke(i) = self.Generate_Stroke(i,n(i))

	self.Xi(i) = Sample_Relationid()

	self.RelationSet(i) = Generate_Relation(Xi(i), Relation)


Type_phi = Type_Integrate(Kappa, Relation， Storke)  
"""
