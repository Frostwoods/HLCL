# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: testExtractSkeleton.py
# @Author: Yang Zhao psy
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-09 14:39:44
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-24 01:53:50
"""
Descripition:



Change Activity:



"""


import sys
sys.path.append('../src')
from skimage import io
from extractSkeleton import *
def main():
   
    filename='F:/Code/Matlab/HLCL/data/testpic/zhe.png'
    I =  io.imread( filename,as_grey=True)
    G=extractSkeleton(I)
    plotUGraph(G)

    # print 'start creat random walker'
    # walkRandomInGraph=PenWalker(G.G)
    # print 'PenWalker created successfully,start searching'
    # a,b=walkRandomInGraph()
    # print 'searching success'
    # print 'pasreset=',a
    # print 'strokesset=',b
if  __name__ =='__main__' :
    
    main()