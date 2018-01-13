# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: set_fake_para.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-01-06 21:19:50
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-11 22:01:32
"""
Descripition:



Change Activity:




"""
import pickle
def save_obj(obj, name ,path):
    with open(path+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)        
def main():
	path='F:/Code/Matlab/HLCL/demo/'
	fakepara_t={}
	kappara_p=[0.3,0.3,0.4]
	fakepara_t['kappa']={'num':3,'p':kappara_p}


	pri_num=3
	m_p=[0.3,0.3,0.4]
	markovmat={0:m_p,1:m_p,2:m_p}
	fakepara_t['fst_id']={'num':3,'p':m_p}
	fakepara_t['subid']={'markovmat':markovmat,'num':3}

	fakepara_t['ctlp']={}
	mean=[[23,12,15,12,12,15,15,12,12,12] for i in range(pri_num)]
	fakepara_t['ctlp']['mean']=mean

	fakepara_t['scl']={}
	fakepara_t['scl']['alpha']=[1,2,3]
	fakepara_t['scl']['beta']=[3,2,1]

	fakepara_t['rlt']={}
	fakepara_t['rlt']['ind']={}
	['ind']['mat']=[[0.1,0.2],[0.4,0.3]]


	save_obj(fakepara_t,'faketypepara',path)

	faketoken_t={}

	faketoken_t['strloc_cov']=[[12,0],[0,12]] #cov_mat
	faketoken_t['nspara']={}
	tokenpara_dict['nspara']['rlt']=[[1,0],[0,1]]









if __name__ =='__main__' :
	main()

