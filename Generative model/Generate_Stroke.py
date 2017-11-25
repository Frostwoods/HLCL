# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Generate_Stroke.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2017-10-22 19:25:54
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2017-11-21 20:02:46
"""
Descripition:
	Sample stroke

	Input:
		serial number :i
		number of substrokes : ni
		unkown,

	Output:
		Si = {Si1, ……, Sini}



Change Activity:
	10.22 add pseudo code(undone) by Yang Zhao


"""
'''
zi(1) = Sample_from_distribution（'zi'）

for j in xrange(2, ni):
    zi(j) = Sample_from_distribution('zij|zi(j-1)')

for k in xrange(1, ni):
    xi(k) = Sample_from_distribution（'xik|zik'）
    yi(k) = Sample_from_distribution（'yik|zik'）
    si(k) = {xi(k), yi(k), zi(k)}

si = {si(1), ……, si(ni)}

stroke_dict={'substorekesnum_int':,'sbustrokes_list':}
substrokes_dict={'substrokesid_int': SubstrokesID,'control_x_array':substrokes_control_x,'scale_y':substrokes_Scale_y,}            
       # return Storke_Integrate()
        
'''
class Generate_Stroke(object):
    """docstring for Generate_Sr"""

    def __init__(self, arg):
        pass

    def __call__(self, id, substrokes_num):
        Generate_Substrokes_ID=Generate_Substrokes_ID()
        SubstrokesID(1) = Generate_Substrokes_ID()
        for i in range(2, substrokes_num + 1):
            SubstrokesID(i) = Generate_Substrokes_ID(SubstrokesID(i - 1))
        for i in range(1, substrokes_num + 1):
            substrokes_control_x(i)= Sample_Controlpoints(SubstrokesID(i))
            substrokes_Scale_y(i) = Sample_Scale(SubstrokesID(i))
            substrokes_dictlist(i)={'substrokesid_int': SubstrokesID(i),'control_x_array':substrokes_control_x(i),'scale_y':substrokes_Scale_y(i)}
        
        return {'substorekesnum_int':substrokes_num,'sbustrokes_list':substrokes_dictlist}            
       # return Storke_Integrate()
    '''
    def Storke_Integrate(self):
        Storke={}
        Storke['SubstrokesID']=
        Storke['control_x']=
        Storke['Scale_y']=

        return Storke
        '''

class Generate_Substrokes_ID(object):
    """docstring for Generate_Substrokes_ID"""

    def __init__(self):
        pass
        #super(Generate_Substrokes_ID, self).__init__()
        #self.arg = arg

    def __call__(self, formerid=None):

        if formerid is None:
            current_id = Sample_FirstSubstrokesid()
        else:
            current_id = Sample_Substrokesid(formerid)
        return current_id
