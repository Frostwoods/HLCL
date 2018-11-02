# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: Image2graph.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2018-10-30 14:21:06
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2018-10-31 19:01:42
"""
Descripition:
	HLCL SM 3.1 &3.2

Input:a hand-writing image
Output:a skeleton

This file contains 3 parts
....................................................
Part I
	One pixel thinning process(Thinning or Skeletenization)

	original refer:L. Lam, S.-W. Lee, C. Y. Suen, Thinning methodologies - A comprehensive survey. IEEE Trans. Pattern Anal. Mach. Intell. 14, 869–885 (1992). doi:10.1109/34.161346
	Input:an image of hand-written character
	Output:an skeleton image(one-pixel)


------------------------------------------------------------------
Part II
	Extract undirected graph from thining image(31)

	original refer:K. Liu, Y. S. Huang, C. Y. Suen, Identification of fork points on the skeletons of handwritten Chinese characters. IEEE Trans. Pattern Anal. Mach. Intell. 21, 1095–1100 (1999). doi:10.1109/34.799914
	Input:a skeleton image from Part I
	Output:a graph that contains{
			nodes(with its location) and edges between nodes
	}		
		i.e.:
			graph=[node] a list of node
			node={'id'=i,'Location'=[x,y],edges=[ids of other id]}
			


------------------------------------------------------------------
Part III
	Merge points with the maximum circle criterion(69)

	original refer:C.-W. Liao, J. S. Huang, Stroke segmentation by bernstein-bezier curve fitting. Pattern Recognit. 23, 475–484 (1990). doi:10.1016/0031-3203(90)90068-V
	
	Input:a graph

	Output:a graph of which some nodes were merged


......................................................
Change Activity:



"""