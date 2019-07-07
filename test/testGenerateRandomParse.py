 



 

class TestGenerateRandomParse(unittest.TestCase):
 # Mostly bottom-up method for generating a set of good candidate parses to optimize further.
   
 # Input
 #  image: [n x n bool] binary image
 #  ninit: number of parses to choose
 #  verbose: true/false

 #  Output
 #  bestMP: [ninit x 1 cell] list of best candidate motor programs
 #  score_sorted: [n x 1] score of all parses considered in sorted order



    def setUp(self):
        #creat a Image with given graph



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