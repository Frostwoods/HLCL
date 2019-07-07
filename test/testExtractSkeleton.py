

import sys
sys.path.append('../src')
import functools as ft
from skimage import io
from extractSkeleton import *
import networkx as nx
class CreatRandomGraph():
    #creat random graph on 2-D space with given size 
    def __init__(self,pickRandomNode,pickRandomEdge,makePathThroughEdge):
        
        self.pickNode=pickRandomNode
        self.pickEdge=pickRandomEdge
        self.makePath=makePathThroughEdge

    def __call__(self,nodeNumber,edgeNumber):
        graph=nx.Graph()
        nodes=self.pickNode(nodeNumber)
        edges=self.pickEdge(nodes,edgeNumber)
        path=self.makePath(edges)

        #see NetworkX 2.2 documentation
        graph.add_nodes_from(nodes)
        [graph.add_edge(edge['edge'][0],edge['edge'][1],path=edge['path']) for edge in edges]


        return graph    

class TransferGraphToImage():
    #creat a Image with given graph
    #see www.cs.toronto.edu/∼ hinton/code 404
    #see render_image.m
    # Each point on the trajectory T(m) contributes up to two "units" of ink to
    # the four closest pixels using bilinear interpolation, where the ink units decrease linearly
    # from 1 to 0 if two points are less than two pixel units apart. This method
    # creates a thin line of ink, which is expanded out by convolving the image twice with
    # the filter
    def __init__(self, flipProbability,gaussianBlurSigma,inkConvolutiionsNumber,imageSize,inkPointsPerpoint,inkMaxDist,inkKernalParameterA,inkKernalParameterB):
        self.flipProb=flipProbability
        self.gaussianBlurSigma=blurSigma
        self.inkConvolutiionsNumber = inkConvolutiionsNumber # number of convolutions
        self.imageSize = imageSize # image size
        self.inkPointsPerpoint = inkPointsPerpoint       # amount of ink per point
        self.inkMaxDist = inkMaxDist # distance between points to which you get full ink
        self.inkKernalParameterA = inkKernalParameterA      # ink parameter 1
        self.inkKernalParameterB = inkKernalParameterB       # ink parameter 2

    def __call__(self,graph):
        return image    

class TestExtractSkeleton(unittest.TestCase):
    def setUp(self):
        #creat a Image with given graph
        pickRandomNode=
        pickRandomEdge=
        makePathThroughEdge=
        self.creatRandomGraph=CreatRandomGraph(pickRandomNode,pickRandomEdge,makePathThroughEdge)





        flipProbability=0.1 #uniform(.0001：0.5).
        gaussianBlurSigma=1 #uniform(0.5: 16)
        inkConvolutiionsNumber = 2 # number of convolutions
        imageSize = [105 105] # image size
        inkPointsPerpoint = 2      # amount of ink per point
        inkMaxDist = 2 # distance between points to which you get full ink
        inkKernalParameterA = 0.5      # ink parameter 1
        inkKernalParameterB = 6        # ink parameter 2
        self.transferGraphToImage=TransferGraphToImage(flipProbability,gaussianBlurSigma,inkConvolutiionsNumber,imageSize,inkPointsPerpoint,inkMaxDist,inkKernalParameterA,inkKernalParameterB)



        fillLutPath='F:/Code/Matlab/HLCL/data/prepocessLut/lutfill.mat'
        thinLut1Path='F:/Code/Matlab/HLCL/data/prepocessLut/lutthin1.mat'
        thinLut2Path='F:/Code/Matlab/HLCL/data/prepocessLut/lutthin2.mat'
        otsuThreshold=0.577
        lutSize=(3,3)
        iterTime=10
        makeThin=MakeThinImage(fillLutPath,
                                thinLut1Path,
                                thinLut2Path,
                                otsuThreshold,
                                lutSize,
                                iterTime)
        
        self.makeGraph=ft.partial(extractSkeleton,makeThin=makeThin,extractJunctions=extractJunctions,traceGraph=traceGraph)

    @data ((4,2),(8,8))
    @unpack
    def testExtractSkeleton(self,nodeNumber,edgeNumber):
        groundTruthGraph=self.creatRandomGraph(nodeNumber,edgeNumber)
        Image=self.transferGraphToImage(groundTruthGraph)
        preprocessedResrult=self.makeGraph(Image)
        calGraph=preprocessedResrult.graph

        #compare node
        groundTruthNodes=groundTruthGraph.nodes
        calNodes=calGraph.nodes

        # truthValue=cal_score==groundtruth_score
        # self.assertTrue(truthValue.all())

        #compare edge
        groundTruthEdges=groundTruthGraph.edges
        calEdges=calGraph.edges

# class  TestSubstrokeSequence(unittest.TestCase):
#   """docstring for  Test"""
#   def setUp(self):
#           self.nSubData = 
#           self.nSamp=1000

#       @data (((2,2,3),np.log([0.2,0.2,0.3])),((4,1,1),np.log([0.4,0.1,0.1])))
#       @unpack
#       def testSampleNsub(self,data,groundtruth_score):
#           cal_score=targetCode.scoreNumber(self.pKappa,data)
#           truthValue=cal_score==groundtruth_score
#           self.assertTrue(truthValue.all())

#       def testSampleSequence
def main():

    filename='F:/Code/Matlab/HLCL/data/testPic/zhe.png'
    I =  io.imread( filename,as_grey=True)

    fillLutPath='F:/Code/Matlab/HLCL/data/prepocessLut/lutfill.mat'
    thinLut1Path='F:/Code/Matlab/HLCL/data/prepocessLut/lutthin1.mat'
    thinLut2Path='F:/Code/Matlab/HLCL/data/prepocessLut/lutthin2.mat'
    otsuThreshold=0.577
    lutSize=(3,3)
    iterTime=10
    makeThin=MakeThinImage(fillLutPath,
                            thinLut1Path,
                            thinLut2Path,
                            otsuThreshold,
                            lutSize,
                            iterTime)
    
    makeGraph=ft.partial(extractSkeleton,makeThin=makeThin,extractJunctions=extractJunctions,traceGraph=traceGraph)
    G=makeGraph(I)
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