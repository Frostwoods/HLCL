# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: extractSkeleton.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-03 13:12:08
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-07-07 23:33:22
"""
Descripition:
	Input:image
	Output:skelenton and graph 


Change Activity:



"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage
import scipy.io as sio
import networkx as nx

class ExtractSkeleton():
	"""docstring for ClassName"""
	def __init__(self, makeThin,extractJunctions,traceGraph):
		self.makeThin=makeThin
		self.extractJunctions=extractJunctions
		self.traceGraph=traceGraph
	def __call__(self,image):
		thinImage = self.makeThin(image)
		junctionImage = self.extractJunctions(thinImage)
		characterGraph = self.traceGraph(thinImage, junctionImage, image)
		return characterGraph 	

#callable class style
class MakeThinImage():
	"""docstring for ClassName"""
	def __init__(self,fillLookUpTable,thinLookUpTable1,thinLookUpTable2,otsuThreshold,LookUpTableSize,iterTime):
		self.fillLookUpTable=fillLookUpTable    
		self.thinLookUpTable1=thinLookUpTable1
		self.thinLookUpTable2=thinLookUpTable2
		self.LookUpTableSize=LookUpTableSize
		self.iterTime=iterTime
		self.otsuThreshold=otsuThreshold
	def  __call__(self,image):
		binaryImage = image < self.otsuThreshold
		skelentonImage = ndimage.generic_filter(binaryImage, self.fillLookUpTable, size=self.LookUpTableSize)    
		for i in range(self.iterTime):
			skelentonImage=ndimage.generic_filter(skelentonImage, self.thinLookUpTable1, size=self.LookUpTableSize)
			skelentonImage=ndimage.generic_filter(skelentonImage, self.thinLookUpTable2, size=self.LookUpTableSize)
		return skelentonImage

class ExtractJunctions():
	"""docstring for ClassName"""
	def __init__(self,endPointLookUpTable, LookUpTableSize):
		self.endPointLookUpTable=endPointLookUpTable    
		self.LookUpTableSize=LookUpTableSize

	def  __call__(self,thinImage):		    
	    
	    endPoints = ndimage.generic_filter(thinImage, self.endPointLookUpTable, size=self.LookUpTableSize) # SE
	    orginalPath = thinImage #SB
	    size = thinImage.shape[0];
	    forkPoints = ndimage.generic_filter(thinImage, findForks, size=self.LookUpTableSize)#S3
	    junctionImage = endPoints | (orginalPath & forkPoints);	 
	    from scipy.ndimage import label
	    labeled, n = label(thinImage, np.ones(self.LookUpTableSize))
	    for i in range(1,n+1):
	        pid= (labeled==i)
	        if (junctionImage[pid].sum()) == 0:
	            [irow, icol] = ind2sub(size, pid)
	            sel = np.argmin(irow)
	            junctionImage[pid[sel]] = True

		return junctionImage
def findForks(P):
	#FS3#
    crossNumber = findCrossNumber(P) #NC
    blackPoint = P==1 #PM
    blackPoint[5] = False
    blackNumber = blackPoint.sum() #NB
    Y = (crossNumber >= 3) or (blackNumber >= 4)
    return Y

def findCrossNumber(P):
	#FNC
    s = 0
    for i in range(8):
        s = s + np.abs( P[fIP(i+1)] - P[fIP(i)]) 
    Y = s/2
    return Y

def fIP(lindx):
	case=[[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[0,0],[0,1]]
	i,j=case[lindx]
	newlindx=sub2ind([3,3],i,j)
	return newlindx
def sub2ind(array_shape, rows, cols):
    return rows*array_shape[1] + cols	

def ind2sub(array_shape, ind):
    ind[ind < 0] = -1
    ind[ind >= array_shape[0]*array_shape[1]] = -1
    rows = (ind.astype('int') / array_shape[1])
    cols = ind % array_shape[1]
    return (rows, cols)   
# def extractJunctions(thinImage,
# 					 endPointLookUpTablePath='F:/Code/Matlab/HLCL/data/prepocessLookUpTable/LookUpTableendpoint.mat',
# 					 LookUpTableSize=(3,3)):

#     findEndLookUpTable = MakeLookUpTable(path=endPointLookUpTablePath)
#     SE = ndimage.generic_filter(thinImage, findEndLookUpTable, size=LookUpTableSize)

#     SB = thinImage
#     sz = thinImage.shape[0];
#     S3 = ndimage.generic_filter(thinImage, fS3, size=LookUpTableSize)

#     junctionImage = SE | (SB & S3);
 
#     from scipy.ndimage import label
#     labeled, n = label(thinImage, np.ones(LookUpTableSize))
#     for i in range(1,n+1):
#         pid= (labeled==i)
#         if (junctionImage[pid].sum()) == 0:
#             [irow, icol] = ind2sub(sz, pid)
#             sel = np.argmin(irow)
#             junctionImage[pid[sel]] = True
#     return junctionImage

class MakeLookUpTable(object):
	def __init__(self,path):		
		self.lookUpTable=sio.loadmat(path)['lut'][0] 
		self.lookupTableIndexTransition=np.array([1,8,64,2,16,128,4,32,256])
	def __call__(self,P):
		index=(P*self.lookupTableIndexTransition).sum()
		return self.lookUpTable[int(index)]

	
def traceGraph(thinImage,junctionImage,image):
	
	pathList=[]
	graphHelper=GraphHelper(thinImage,junctionImage,image)
	jx,jy=np.where(graphHelper.junctionImage)
	for (i,pt) in enumerate(zip(jx,jy)):
		start=pt
		blist=graphHelper.NF[i]
		for br in blist:
			if graphHelper.zeroImage[br[0]][br[1]]==0 :  
				path= [start,br] 
				if graphHelper.junctionImage[br[0]][br[1]]:
					# criteria so each junction-to-junction is added once
					if lind(br,graphHelper.junctionImage) > lind(start,graphHelper.junctionImage):
						continue
				else:					
					graphHelper.zeroImage[br[0]][br[1]] = True
					tabu = np.ones(graphHelper.thinImage.shape)==0
					for br2 in blist:
						tabu[br2[0]][br2[1]] = True
					# other branch points from that junction
					tabu[start[0]][start[1]] = True
					path,graphHelper = continuePath(path,graphHelper,tabu)    
				 #Update adjacency matrix
				pathList.append(path)
	characterGraph = UGraph(pathList,graphHelper);
	return characterGraph



class GraphHelper(object):
	def __init__(self,thinImage,junctionImage,image):
		self.thinImage=thinImage|junctionImage
		self.junctionImage=junctionImage
		self.image=image
		self.zeroImage=np.ones(thinImage.shape)==0
		jx,jy=np.where(junctionImage)
		self.NF=getForks(jx,jy,thinImage)
	

class UGraph(object):
	"""docstring for MakeGraph"""
	def __init__(self,pathList,graphHelper):
		self.graph=nx.Graph()
		self.image=graphHelper.image
		self.thinImage=graphHelper.thinImage
		self.junctionImage=graphHelper.junctionImage
		nodelist=junction2Nodes(graphHelper.junctionImage)

		self.graph.add_nodes_from(nodelist)
 		self.pathList=pathList
		edgelist=pathlist2edges(pathList)
		for edge in edgelist:
			self.graph.add_edge(edge['edge'][0],edge['edge'][1],path=edge['path'])
		for node in self.graph.nodes:
			self.graph.nodes[node]['Location']=node 
		


def junction2Nodes(junctionImage):
	jx,jy=np.where(junctionImage)
	nodelist=list(zip(jx,jy))
	return nodelist
def pathlist2edges(pathList):
	edgelist=[]
	for path in pathList:
		edge={}
		startNode=path[0]
		fnishiNode=path[1]
		edge['edge']=(tuple(startNode),tuple(fnishiNode))
		edge['path']=path
		edgelist.append(edge)
	return edgelist
		
def getForks(jx,jy,t):
	nf=[]
	for (i,pt) in enumerate(zip(jx,jy)):
		nf.append(getNeibours(pt,t))
	return nf
def lind(pts,T):
	return sub2ind(T.shape,pts[0],pts[1])
def continuePath(path,graphHelper,tabu):
	nxpt=path[-1]

	while graphHelper.junctionImage[nxpt[0]][nxpt[1]]==0:
		nxpt=pathStep(nxpt,graphHelper,tabu)
		graphHelper.zeroImage[nxpt[0]][nxpt[1]]=True
		path.append(nxpt)
		tabu=np.ones(tabu.shape)==0
	graphHelper.zeroImage[graphHelper.junctionImage]=False
	return path,graphHelper

def pathStep(curr,graphHelper,tabu):
	nxpt=getNeibours(curr,graphHelper.thinImage & ~graphHelper.zeroImage & ~tabu)

	num=len(nxpt)
	if num==0:
		print'error no neighbors to continue path'
	elif num>1:
		isj=np.array([graphHelper.junctionImage[x][y] for (x,y) in nxpt])	
		if isj.any():
			nxpt=[nxpt[p] for p in np.where(isj)[0]]
		dists=abs(np.array(curr)-np.array(nxpt)).sum(1)
		jindx=dists.argmin()
		return nxpt[jindx]
	else:
		return nxpt[0]


def getNeibours(indx,v):
	#get 3*3 neibours of indx on v
	i=indx[0]
	j=indx[1]
	import copy
	vII=copy.deepcopy(v)
	vII[i][j]=False
	iteri=range(max(i-1,0),min(i+1,v.shape[0])+1)
	iterj=range(max(j-1,0),min(j+1,v.shape[0])+1)
	subI=vII[min(iteri):max(iteri)+1,min(iterj):max(iterj)+1]
	jx,jy=np.where(subI)
	neighbours=[(iteri[k],iterj[l]) for (k,l) in zip(jx,jy)]

	return neighbours

def plotUGraph(UG):
	fig = plt.figure()
	ax1 = fig.add_subplot(231)
	ax1.imshow(UG.image, cmap=plt.cm.gray)
	ax1.set_title('Original binary image')
	ax1.axis('off')

	ax2 = fig.add_subplot(232)
	ax2.imshow(UG.thinImage, cmap=plt.cm.gray)
	ax2.set_title('Thin Image')
	ax2.axis('off')

	ax3 = fig.add_subplot(233)
	ax3.imshow(UG.junctionImage, cmap=plt.cm.gray)
	ax3.set_title('KeyNodes')
	ax3.axis('off')

	ax4 = fig.add_subplot(234) 		
	plt.axis([0,UG.thinImage.shape[0],0,UG.thinImage.shape[1]])
	ax4.invert_yaxis()
	# ax4.invert_xaxis()
	k=len(UG.graph.edges)
	import matplotlib.cm as cm
	colormap = cm.rainbow(np.linspace(0, 1, k))
	for (i,edge) in enumerate(UG.graph.edges):

		path=np.array(UG.graph.edges[edge]['path']).T
		plt.scatter(path[1], # x
					path[0], # y
					s = 30, # 设置点的大小 
					c = colormap[i], # 设置点的颜色
					marker = 's', # 设置点的形状
					alpha = 0.9, # 设置点的透明度
					linewidths = 0, # 设置散点边界的粗细
					edgecolors = 'red' # 设置散点边界的颜色
					)
	loc=np.array(UG.graph.nodes).T 
	plt.scatter(loc[1], # x
				loc[0], # y
				s = 30, # 设置点的大小 
				c = 'red', # 设置点的颜色
				marker = 's', # 设置点的形状
				alpha = 0.9, # 设置点的透明度
				linewidths = 0, # 设置散点边界的粗细
				edgecolors = 'red' # 设置散点边界的颜色
				)
	ax4.set_title('Graph Before Merge')
	ax5 = fig.add_subplot(235)
	ax5.set_title('BestInitPrase:LogP=')
	# ax5.axis('off')
	ax6 = fig.add_subplot(236)
	ax6.set_title('BestInitPrase:LogP=')
	# ax6.axis('off')
	plt.show()




def main():
	from skimage import io
	filename='F:/Code/Matlab/HLCL/data/testPic/zhe.png'
	I =  io.imread( filename,as_grey=True)

	fillLookUpTablePath='F:/Code/Matlab/HLCL/data/preprocessLut/lutfill.mat'
	thinLookUpTable1Path='F:/Code/Matlab/HLCL/data/preprocessLut/lutthin1.mat'
	thinLookUpTable2Path='F:/Code/Matlab/HLCL/data/preprocessLut/lutthin2.mat'
	fillLookUpTable=MakeLookUpTable(fillLookUpTablePath)
	thinLookUpTable1=MakeLookUpTable(thinLookUpTable1Path)
	thinLookUpTable2=MakeLookUpTable(thinLookUpTable2Path)

	otsuThreshold=0.577
	LookUpTableSize=(3,3)
	iterTime=10
	makeThin=MakeThinImage(fillLookUpTable,
	                        thinLookUpTable1,
	                        thinLookUpTable2,
	                        otsuThreshold,
	                        LookUpTableSize,
	                        iterTime)

	endPointLookUpTablePath='F:/Code/Matlab/HLCL/data/preprocessLut/lutendpoint.mat'
	endPointLookUpTable=MakeLookUpTable(endPointLookUpTablePath)               
	extractJunctions=ExtractJunctions(endPointLookUpTable,LookUpTableSize)
	        
	extractSkeleton=ExtractSkeleton(makeThin,extractJunctions,traceGraph)

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