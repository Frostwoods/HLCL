
from classes.extractSkeleton import *
def fitMotorprograms(I,K,verbose,includemcmc,fastmode):	

	initMP=generateRandomPrase(I,lib,K,verbose)

	initscores=[scoreMPNoRel(MP) for MP in initMP]	

	finalMP=[searchForParse(MP,lib,verbose,fast_mode) \
			for MP in initMP]
	finalscores=[scoreMPNoRel(MP) for MP in finalMP]
	if verbose:
		pass #visual

	if includemcmc:
		samplestype = [runMCMCType(MP,*arg) for MP in finalMP]

	G={}
	G['models']=finalMP
	G['scores']=finalscores
	G['samplestype']=samplestype
	G['img']=I
	G['PM']=ps


	return G
def generateRandomPrase(I,K=5,verbose=True):
	G=extractSkeleton(I,verbose)
	RW=randomWalker(G)
	PP=processParses(I,verbose)
	[bestMP,score_sorted] = parses2MPs(I,PP,ninit,lib,verbose)
	return bestMP
