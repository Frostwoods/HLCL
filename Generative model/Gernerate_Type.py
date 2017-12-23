# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Gernerate_Type.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 14:35:37
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-12-22 10:34:35
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
import sys
sys.path.append('F:\Code\Matlab\HLCL')
from Generative model.Generate_Stroke import *
from Generative model.Generate_Relation import *
from sample.Sample_kappa import *
from sample.Sample_SubstrokesNum import *
from sample.Sample_Relationid import *

class Generate_Type(object):
	"""docstring for Generate_Type"""
	def __init__(self,typepara_dict):
		typepara_dict['']

		self.Generate_Stroke=Generate_Stroke()
		self.Generate_Relation=Generate_Relation()
		self.Sample_kappa=Sample_kappa()
		self.Sample_SubstrokesNum=Sample_SubstrokesNum()
		self.Sample_Relationid=Sample_Relationid()
		pass
				
	def __call__(self,Kappa):
		if Kappa is None	
			Kappa = self.Sample_kappa()
			
		n=[]
		Storke =[] 
		Xi = []
		RelationSet=[]

		for i in range(Kappa):
			#lst con查看是否分离 查一下Reduce
			n.append(self.Sample_SubstorkesNum(self.Kappa))

			Storke.append([self.Generate_Stroke(i,self.n[i])])

			Xi.append(self.Sample_Relationid())

			RelationSet.append( [self.Generate_Relation(Xi[i],Storke,i)])
		
		return {'storekesnum'=Kappa,'relations'=RelationSet,'strokes'=Storke}

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
