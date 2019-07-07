import sys
sys.path.append('../src')
import conditionalProbabilityDistribution as targetCode
import unittest
from ddt import ddt, data, unpack
import numpy as np
@ddt
class TestStrokeNumber(unittest.TestCase):
    def setUp(self):
        self.pKappa = np.array((0.1,0.2,0.3,0.4))
      	self.nSamp=1000

    @data (((2,2,3),np.log([0.2,0.2,0.3])),((4,1,1),np.log([0.4,0.1,0.1])))
    @unpack
    def testCalStrokeNumberLikehood(self,strokeNumberlist,groundTruthScore):
        calScore=targetCode.calStrokeNumberLikehood(self.pKappa,strokeNumberlist)
        truthValue=calScore==groundTruthScore
        self.assertTrue(truthValue.all())
  
    def testSampleNumber(self):
        samps = targetCode.sampleNumber(self.pKappa,nSamp=self.nSamp)   
        frequency=np.array([(len(samps[samps==(i+1)]))*1.0/self.nSamp for i in range(len(self.pKappa))])
        # frequency=np.zeros(self.pKappa.shape)
        # for i in range(len(self.pKappa)):
        #     frequency[i]=(len(samps[samps==(i+1)]))*1.0/self.nSamp
        self.assertTrue(np.allclose(frequency,self.pKappa,rtol=0.1))

# class  TestSubstrokeSequence(unittest.TestCase):
# 	"""docstring for  Test"""
# 	def setUp(self):
# 	        self.nSubData = 
# 	      	self.nSamp=1000

# 	    @data (((2,2,3),np.log([0.2,0.2,0.3])),((4,1,1),np.log([0.4,0.1,0.1])))
# 	    @unpack
# 	    def testSampleNsub(self,data,groundtruth_score):
# 	        cal_score=targetCode.scoreNumber(self.pKappa,data)
# 	        truthValue=cal_score==groundtruth_score
# 	        self.assertTrue(truthValue.all())

# 	    def testSampleSequence
if __name__ == '__main__':
    unittest.main()