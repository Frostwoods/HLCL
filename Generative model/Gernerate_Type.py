# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Gernerate_Type.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 14:35:37
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-21 20:02:46
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

	S(x) = Generate_Stroke(x, n(x))

	ξ(x) = Sample_from_distribution('ξ')

	R(x) = Sample_from_distribution('Ri|ξ, S1, ……, Sx')
φ = {k, R, S}


return φ
"""

class Generate_Type(object):
	"""docstring for Generate_Type"""
	def __init__(self):
		self.Kappa = Sample_kappa()

	def __call__(self):	
		self.Generate_wrap()
		return Type_Integrate()


	def Generate_wrap(self,Sample_SubstorkesNum,Generate_Stroke,Sample_Relationid,Generate_Relation):
		for i in xrange(1,self.Kappa):

			self.n(i) = Sample_SubstorkesNum(self.Kappa)

			self.Storke(i) = Generate_Stroke(i,self.n(i))

			self.Xi(i) = Sample_Relationid()

			self.RelationSet(i) = Generate_Relation(Xi(i), self.Storke , i-1)




	def Type_Integrate(self):
		Type_phi={}
		Type_phi['storekesnum']=self.Kappa
		Type_phi['relations']=self.RelationSet
		Type_phi['strokes']=self.Storke
		return Type_phi
				
"""
Kappa = Sample_kappa()

for i in xrange(1,Kappa)

	self.n(i) = Sample_SubstorkesNum(Kappa)

	self.Storke(i) = Generate_Stroke(i,n(i))

	self.Xi(i) = Sample_Relationid()

	self.RelationSet(i) = Generate_Relation(Xi(i), Relation)


Type_phi = Type_Integrate(Kappa, Relation， Storke)  
"""
