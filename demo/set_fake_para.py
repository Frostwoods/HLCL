# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: set_fake_para.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-06 21:19:50
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-03-11 18:15:48
"""
Descripition:



Change Activity:




"""
import pickle
import numpy as np
def save_obj(obj, name ,path):
    with open(path+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)        
def main():
	path='F:/Code/Matlab/HLCL/demo/'
	fakepara_t={}
	kappara_p=[0.3,0.3,0.4]
	fakepara_t['kappa']={'num':3,'p':kappara_p}


	subnum1={'num':3,'p':kappara_p}
	subnum2={'num':3,'p':kappara_p}
	subnum3={'num':3,'p':kappara_p}
	fakepara_t['subnum']=[subnum1,subnum2,subnum3]

	pri_num=3
	m_p=[0.3,0.4,0.3]
	markovmat={0:m_p,1:m_p,2:m_p}
	fakepara_t['fst_id']={'num':3,'p':m_p}
	fakepara_t['subid']={'markovmat':markovmat,'num':3}

	fakepara_t['ctlp']={}

	substrokesctplist=[]
	substrokesctplist.append(np.array([0, 0,4, -2,2, -5,0, -8,4, -9]))
	substrokesctplist.append(np.array([0, 0, 1, 2, 3, 0, 2, -3, 0, -5]))
	substrokesctplist.append(np.array([0, 0, 0, -1, 0, -2, 0, -3, 0, -4]))
	substrokesctplist.append(np.array([0, 0, 1, 2, 2, 0, 3, -2, 4, 0]))
	
	fakepara_t['ctlp']['mean']=substrokesctplist
	fakepara_t['ctlp']['cov']=[np.eye(10) for i in range(4)]

	fakepara_t['scl']={}
	fakepara_t['scl']['alpha']=[1,2,3]
	fakepara_t['scl']['beta']=[3,2,1]

	fakepara_t['rlt']={}
	fakepara_t['rlt']['ind']={}
	fakepara_t['rlt']['ind']['mat']=[[0.1,0.2],[0.4,0.3]]


	save_obj(fakepara_t,'faketypepara',path)

	faketoken_t={}

	faketoken_t['strloc']=[np.eye(2)] #cov_mat
	faketoken_t['nspara']={}
	faketoken_t['nspara']['rlt']=[[1,0],[0,1]]
	faketoken_t['nspara']['ctp']=[np.eye(10)]
	faketoken_t['nspara']['scl']=[1]
	save_obj(faketoken_t,'faketokenpara',path)








if __name__ =='__main__' :
	main()

