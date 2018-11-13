# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: likelyhood.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-11-12 18:55:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-11-12 23:16:32
"""
Input type level parameter phi={k,S,R}

Output prob P(phi)
Descripition:



Change Activity:



"""
import numpy as np
import scipy.stats 
def Multinoial_likelyhood(var_num,p_list):
	p=np.array(p_list)
	return p[var_num]/p.sum()


def Multigaussian_likelyhood():
	pass

def Markov_likelyhood():
	pass

def Gamma_likelyhood(x,beta,alpha):

	#return (beta**alpha)*(x**(alpha-1))*(np.e**(-beta*x))/()
	return scipy.stats.Gamma.pdf(x,alpha,scale=1.0/beta)
def Uniform_likelyhood():
	pass




