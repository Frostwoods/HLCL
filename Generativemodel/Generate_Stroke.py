# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Stroke.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:25:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-01-14 23:31:43
"""
Descripition:
	Sample stroke

	Input:
		serial number :i [int]
		number of substrokes : ni [int]
		

	Output:
		Si: [ni_list of dict]



Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao


"""


class Generate_Stroke(object):
    """docstring for Generate_Sr"""
    def __init__(self,sap_id,sap_ctp,sap_scl):
        self.Generate_Substrokes_ID=sap_id
        self.Sample_Controlpoints=sap_ctp
        self.Sample_Scale=sap_scl

    def __call__(self,substrokes_num):
       
        '''
        SubstrokesID += self.Generate_Substrokes_ID()
        for i in range(1, substrokes_num):
            SubstrokesID.append(self.Generate_Substrokes_ID(SubstrokesID[i - 1]))
        '''
        #substrokesid=[self.Generate_Substrokes_ID(i) for i in range(substrokes_num)]
        
        substrokesid=[]
        substrokesid.append(self.Generate_Substrokes_ID(None))
        print substrokesid,'subfirstid',substrokes_num
        for i in range(substrokes_num-1):
            print 'id',i
            substrokesid.append(self.Generate_Substrokes_ID(substrokesid[i]))

        substrokes_ctlp=[self.Sample_Controlpoints(substrokesid[i]) for i in range(substrokes_num)]
        ssubstrokes_scale=[self.Sample_Scale(substrokesid[i]) for i in range(substrokes_num)]
        
        substrokes_dictlist=[{'substrokesid_int': substrokesid[i],
                'control_x_array':substrokes_ctlp[i],
                'scale_y':ssubstrokes_scale[i]} for i in range(substrokes_num)]
        '''  
        for i in range(substrokes_num):
            substrokes_control_x.append(self.Sample_Controlpoints(SubstrokesID[i]))
            substrokes_Scale_y.append(self.Sample_Scale(SubstrokesID[i]))
            substrokes_dictlist.append([{'substrokesid_int': SubstrokesID(i),
                'control_x_array':substrokes_control_x(i),'scale_y':substrokes_Scale_y(i)}])
          '''      
        stroke_dict={'substorekesnum_int':substrokes_num,'sbustrokes_list':substrokes_dictlist} 

        return stroke_dict






        