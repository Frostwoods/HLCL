# -*- coding: utf-8 -*-
# @Poroject Name: .
# @File Name: Sample_Substrokesid.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-11-02 09:53:22
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-20 15:12:32
"""
Descripition:



Change Activity:
Markov


"""
import scipy.io as sio   
matfn = '/home/weiliu/workspace/python/matlab/mat4py.mat'  

class Sample_Substrokesid(object):
    """docstring for sampel_"""

    def __init__(self, SampleMode = Sample_Multinomial):
        #!!!! 
        self.read_all_parameter()
        self.Sample = SampleMode()

    def __call__(self,Former_SubStroke_id):
    	#self.read_parameter(Former_SubStroke_id)
        read_parameter(Former_SubStroke_id)
        return self.Sample(self.NUM, self.P)

    def read_all_parameter(self):
        #set_all_parameter
		#pass dict?
        self.markov_mat=sio.loadmat(matfn) 
    def read_parameter(self,Former_SubStroke_id):
        
        self.P = self.markov_mat[:,Former_SubStroke_id]
        self.NUM=len(self.P)