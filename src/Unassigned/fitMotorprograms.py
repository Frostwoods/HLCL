# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: fitMotorprograms.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-11 18:48:52
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-16 23:54:49
"""
Descripition:



Change Activity:



"""
from classes.extractSkeleton import *
def fitMotorprograms(I,K,verbose,includemcmc,fastmode):	
	initMP=generateRandomPrase(I,lib,K,verbose)
	initscores=[scoreMPNoRel(MP) for MP in initMP]	
	finalMP=[searchForParse(MP,lib,verbose,fast_mode) \
			for MP in initMP]
	finalscores=[scoreMPNoRel(MP) for MP in finalMP]
	if verbose:
		pass #visual

	if includemcmc:
		samplestype=[]
		for MP in finalMP:
			samplesM=RunMCMCType(MP,*arg)
#			for i=1:nsamp
#                samplesM{i}.lightweight; % reduce memory size         
#            samples_type{j} = samplesM;
			samplestype.append(samplesM)	
	G={}
	G['models']=finalMP
	G['scores']=finalscores
	G['samplestype']=samplestype
	G['img']=I
	G['PM']=ps


	return G
def generateRandomPrase(I,K=5,verbose=True):
	G=extractSkeleton(I,verbose)
	RW=randomWalker(G)
	PP=processParses(I,verbose)
	[bestMP,score_sorted] = parses2MPs(I,PP,ninit,lib,verbose)
	return bestMP
