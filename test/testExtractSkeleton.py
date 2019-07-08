

import sys
sys.path.append('../src')
import functools as ft
from skimage import io
from extractSkeleton import *
import networkx as nx
import unittest
from ddt import ddt, data, unpack

class TestExtractSkeleton(unittest.TestCase):
    def setUp(self):
        #creat a Image with given graph
        imageSize = [105,105]        
        pickRandomNode=PickRandomNode(imageSize)
        makePathThroughEdge=MakePathThroughEdge(imageSize)
        pickRandomEdge=PickRandomEdge(imageSize,makePathThroughEdge)               
        self.creatRandomGraph=CreatRandomGraph(pickRandomNode,pickRandomEdge)

        flipProbability=0.1 #0.0001-0.5
        gaussianBlurSigma=1  #uniform 0.5: 16
        inkConvoLookUpTableiionsNumber = 2 # number of convoLookUpTableions
        inkPointsPerpoint = 2      # amount of ink per point
        inkMaxDist = 2 # distance between points to which you get full ink
        inkKernalParameterA = 0.5      # ink parameter 1
        inkKernalParameterB = 6        # ink parameter 2
        self.transferGraphToImage=TransferGraphToImage(flipProbability,gaussianBlurSigma,inkConvoLookUpTableiionsNumber,imageSize,inkPointsPerpoint,inkMaxDist,inkKernalParameterA,inkKernalParameterB)

        otsuThreshold=0.577
        LookUpTableSize=(3,3)
        iterTime=10
        fillLookUpTablePath='F:/Code/Matlab/HLCL/data/preprocessLut/lutfill.mat'
        thinLookUpTable1Path='F:/Code/Matlab/HLCL/data/preprocessLut/lutthin1.mat'
        thinLookUpTable2Path='F:/Code/Matlab/HLCL/data/preprocessLut/lutthin2.mat'
        fillLookUpTable=MakeLookUpTable(fillLookUpTablePath)
        thinLookUpTable1=MakeLookUpTable(thinLookUpTable1Path)
        thinLookUpTable2=MakeLookUpTable(thinLookUpTable2Path)
        makeThin=MakeThinImage(fillLookUpTable,thinLookUpTable1,thinLookUpTable2,otsuThreshold,LookUpTableSize,iterTime)
        
        endPointLookUpTablePath='F:/Code/Matlab/HLCL/data/preprocessLut/lutendpoint.mat'
        endPointLookUpTable=MakeLookUpTable(endPointLookUpTablePath)               
        extractJunctions=ExtractJunctions(endPointLookUpTable,LookUpTableSize)
               
        self.extractSkeleton=ExtractSkeleton(makeThin,extractJunctions,traceGraph)




    @data ((4,2),(8,8))
    @unpack
    def testExtractSkeleton(self,nodeNumber,edgeNumber):
        groundTruthGraph=self.creatRandomGraph(nodeNumber,edgeNumber)
        
        groundTruthNodes=groundTruthGraph.nodes
        groundTruthEdges=groundTruthGraph.edges
        self.assertEqual(len(groundTruthNodes),nodeNumber)
        self.assertEqual(len(groundTruthEdges),edgeNumber)

        Image=self.transferGraphToImage(groundTruthGraph)
        preprocessedResrult=self.extractSkeleton(Image)
        calGraph=preprocessedResrult.graph

        #compare node        
        calNodes=calGraph.nodes
        self.assertEqual(len(groundTruthNodes),len(calNodes))
        [self.assertTrue(node in groundTruthNodes) for node in calNodes]

        #compare edge        
        calEdges=calGraph.edges
        self.assertEqual(len(groundTruthEdges),len(calEdges))
        [self.assertTrue(node in groundTruthEdges) for edge in calEdges]
class CreatRandomGraph():
    #creat random graph on 2-D space with given size 
    def __init__(self,pickRandomNode,pickRandomEdge):        
        self.pickNode=pickRandomNode
        self.pickEdge=pickRandomEdge        

    def __call__(self,nodeNumber,edgeNumber):
        graph=nx.Graph()
        nodes=self.pickNode(nodeNumber)
        edges=self.pickEdge(nodes,edgeNumber)        
        #see NetworkX 2.2 documentation
        graph.add_nodes_from(nodes)
        [graph.add_edge(edge['edge'][0],edge['edge'][1],path=edge['path']) for edge in edges]
        return graph    

import numpy as np
class TransferGraphToImage():
    def __init__(self, flipProbability,gaussianBlurSigma,inkConvoLookUpTableiionsNumber,imageSize,inkPointsPerpoint,inkMaxDist,inkKernalParameterA,inkKernalParameterB):
        self.flipProb=flipProbability
        self.gaussianBlurSigma=blurSigma
        self.inkConvoLookUpTableiionsNumber = inkConvoLookUpTableiionsNumber # number of convoLookUpTableions
        self.imageSize = imageSize # image size
        self.inkPointsPerpoint = inkPointsPerpoint       # amount of ink per point
        self.inkMaxDist = inkMaxDist # distance between points to which you get full ink
        self.inkKernalParameterA = inkKernalParameterA      # ink parameter 1
        self.inkKernalParameterB = inkKernalParameterB       # ink parameter 2
    def __call__(self,graph):
        pass
        return image    

class PickRandomNode():
    """docstring for ClassName"""
    def __init__(self, imageSize):
        self.imageSize = imageSize
    def __call__(self,nodeNumber):
        x=np.random.randint(0,self.imageSize[0],nodeNumber)
        y=np.random.randint(0,self.imageSize[1],nodeNumber)
        return list(zip(x,y)) 
import itertools as it
class PickRandomEdge():    
    """docstring for ClassName"""
    def __init__(self, imageSize,makePathThroughEdge):
        self.imageSize = imageSize
        self.makePath=makePathThroughEdge
    def __call__(self,nodes,edgeNumber):        
        #rejction sampling
        pathList=[]
        allEdges=[edge for edge in it.combinations(nodes,2)]
        allEdgesNumber=len(allEdges)
        for i in range(edgeNumber):
            allEdgesNumber=len(allEdges)
            currentEdge=allEdges[np.random.choice(range(allEdgesNumber),1)[0]]
            currentPath=self.makePath(currentEdge)
            #rejction sampling         
            while hasCrossBetweenPaths(currentPath,pathList):            
                currentEdge=allEdges[np.random.choice(range(allEdgesNumber),1)[0]]
                currentPath=self.makePath(currentEdge)
            allEdges.remove(currentEdge)
            pathList.append(currentPath)                    
        edgelist=[]
        for path in pathList:
            edge={}
            startNode=path[0]
            fnishiNode=path[-1]
            edge['edge']=(tuple(startNode),tuple(fnishiNode))
            edge['path']=path
            edgelist.append(edge)
        return edgelist 
def hasCrossBetweenPaths(currentPath,pathList):
    if pathList==[]:
        return False
    for path in pathList:
        crossList=[node for node in currentPath[1:-2] if node in path[1:-2]] #remove head and tail
        if len(crossList)>0:
            return True
    return False

import cv2 
class MakePathThroughEdge():
    """docstring for ClassName"""
    def __init__(self,imageSize):
        self.imageSize = imageSize                
    def __call__(self,edge):
        img=np.zeros(self.imageSize)
        cv2.line(img,tuple(edge[0]),tuple(edge[1]),1,1)
        jx,jy=np.where(img)
        path=list(zip(jy,jx))
        if not (path[0] in edge):
            dist0=np.abs(np.array(edge[0])-np.array(path[0])).sum()
            dist1=np.abs(np.array(edge[1])-np.array(path[0])).sum()
            if dist0<dist1:
                path.insert(0,edge[0])
            else:
                path.insert(0,edge[1])
        if not (path[-1] in edge):
            dist0=np.abs(np.array(edge[0])-np.array(path[-1])).sum()
            dist1=np.abs(np.array(edge[1])-np.array(path[-1])).sum()
            if dist0<dist1:
                path.append(edge[0])
            else:
                path.append(edge[1]) 
        return path 



def main():

    imageSize = [105,105]    
    pickRandomNode=PickRandomNode(imageSize)
    makePathThroughEdge=MakePathThroughEdge(imageSize)
    pickRandomEdge=PickRandomEdge(imageSize,makePathThroughEdge)
    creatRandomGraph=CreatRandomGraph(pickRandomNode,pickRandomEdge)
    graph=creatRandomGraph(4,2)   
    # print 'start creat random walker'
    # walkRandomInGraph=PenWalker(G.G)
    # print 'PenWalker created successfully,start searching'
    # a,b=walkRandomInGraph()
    # print 'searching success'
    # print 'pasreset=',a
    # print 'strokesset=',b
if  __name__ =='__main__' :
    
    main()