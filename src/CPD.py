
# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: CPD.py
# @Author: Yang Zhao
# @Emial: frostwoods@foxmail.com
# @Date:   2019-04-16 18:34:12
# @Last Modified by:   Yang Zhao
# @Last Modified time: 2019-06-11 15:56:26
"""
Descripition:



Change Activity:



"""
from scipy.stats import  binom,norm,gamma,multivariate_normal,norm,multinomial,dirichlet
import numpy as np
from random import uniform

def sampleNumber(pkappa,nsamp=1):
	for x in xrange(0, nsamp):
            onesample = multinomial.rvs(1 , pkappa)
            samps[x] = np.where(onesample == 1)[0]   
        return samps
	return samps

def scoreNumber(pkappa,data):

	return np.log(pkappa(data))

def sampleNsub(ns,nsubdata):
	nsub=np.where(multinomial.rvs(1 , nsubdata[ns])==1)[0]

	return nsub
def sampleSequence(markovT,logstart,ns,nsub,nsamp=1):
	sq=[]
	for x in xrange(0, nsamp):
		cursq=[]
		cursq.append(np.where(multinomial.rvs(1 ,10^logstart)==1)[0])
		for y in xrange(2,nsub):
			cursq.append(np.where(multinomial.rvs(1 ,10^markovT[cursq[-1]])==1)[0])
		sq.append(cursq)
	return sq
def scoreSequence(markovT,logstart,nsubdata ,sequence,ns):
	nsub=len(sequence)
	sz=nsubdata.shape
	if ns <0:
		lp=0
	elif ns>sz[0] || nsub>sz[1]:
		lp=-np.inf
	else:
		lp=np.log(nsubdata[ns][sequence])
	lv=[]
	lv.append(logstart[sequence[0]])
	for y in xrange(1,nsub):
		lv.append(markovT[sequence[y-1][sequence[y]]])
	score=lp+np.array(lv).sum
	return score

def sampleShapeType(shapemu,shapesigma,subids):
	bsplinestack=[]
	lenth=len(subids)
	for id in subids:
		cpt=multivariate_normal.rvs(shapemu[:,:,id],shapesigma[:,:,id],1)
		bsplinestack.append(cpt.reshape((-1,2,lenth)))
	return bsplinestack
def scoreShapeType(shapemu,shapesigma,bsplinestack,subids,regcov):
	
	score = scoreShapeTypehelper(shapemu,shapesigma,bsplinestack,subids,regcov)
	return score

def scoreShapeTypehelper(shapemu,shapesigma,bsplinestack,subids,regcov=0):
	scorelist=[]
	size=len(subids)
	for (index,subid) in enumerate(subids):
		sd=np.sqrt(np.power(shapesigma[:,:,id],2)+regcov)
		cpt=multivariate_normal.logpdf(bsplinestack.reshape((-1,10)),shapemu[:,:,id],sd,1)
		scorelist.append(cpt.reshape((1,-1)))
	return np.array(scorelist).sum()
def sampleShapeToken(tokenshapesigma,bsplinestack):
	#bspline_stack: (ncpt x 2 x k) shapes of bsplines 
	sz=bsplinestack.shape
	bsplinestacktoken=bsplinestack+\
			tokenshapesigma*np.random.randn(sz[0],sz[1],sz[2])
	return bsplinestacktoken
def scoreShapeToken(shapesigma,bsplinestacktoken,bsplinestacktype):
	#spline_stack_type: (ncpt x 2 x k) shapes of bsplines
    #bspline_stack_token: (ncpt x 2 x k) shapes of bsplines
    
    sizek=bsplinestacktype.shape[2]
    scorelist=[]
    for i in range(sizek)
    	x=bsplinestacktoken[:,:,i].reshape(1,-1)[0]
    	mean=bsplinestacktype[:,:,i].reshape(1,-1)[0]
    	sd=shapesigma*np.ones(mean.size)
		cpt=multivariate_normal.logpdf(x,mean,sd)
		scorelist.append(cpt)

	return cpt.sum()


def scoreShapeMarginalize(shapemu,shapesigma,bsplinestacktoken,subids,regcov=tokenshapesigma^2):
	score = scoreShapeTypehelper(shapemu,shapesigma,bsplinestacktoken,subids,regcov)
	return score

def sampleInvscaleType(scaletheta,subids):
	
	invscales=[gamma.rvs(scaletheta[i][0], scale=1.0 /scaletheata[i][1] ) for i in subids]

	return invscales
def scoreInvscaleType(scaletheta,invscaletype,subids):
	probs=[gamma.logpdf(invscaletype[num],scaletheta[i][0],\
			scale=1.0 /scaletheata[i][1])\
			for (num,i) in enumerate(subids)
				]

	return score

def sampleInvscaleToken(sigmainvscale,invscalestype):
	# Gaussian noise, but don't allow negative scales.
    #Sampling is done by rejection sampling
	invscalestoken=[scale+norm.rvs(scale,sigmainvscale,1) for scale in invscalestype]
	while (invscalestoken<=0).sum()>0:
		invscalestoken=[scale+norm.rvs(scale,sigmainvscale,1) for scale in invscalestype]

	return invscalestoken
def scoreInvscaleToken(sigmainvscale,invscalestype,invscalestoken):
	sz=invscalestoken.size
	sd=sigmainvscale
	scorelist=[]
	
	for i in range(sz):
		x=invscalestoken[i]
		mean=invscalestype[i]
		prob=norm.logpdf(x,mean,sd)
		if prob<=0:
			prob=-np.inf
		pbelow=norm.logcdf(0,mean,sd)
		pabove=1-pbelow
		prob=prob-pabove
		scorelist.append(prob)
	return scorelist


def sampleRelationType(relationmixprob,previousstrokes):
	#R={} R['nprev'] R['type']

	nprev=len(previousstrokes)
	relationtypes = ('unihist','start','end','mid')
	if nprev==0:
		indx=1
	else:
		indx=np.where(multinomial.rvs(1 ,relationmixprob)==1)[0]
	
	if relationtypes[indx]=='unihist':


	elif:relationtypes[indx] in ('start','end')

	elif:relationtypes[indx]=='mid':

	else：
		print 'norelation'
	
	return R

def scoreRelationType(relationmixprob,R):
	strokenum=R['nprev']+1
	relationtypes = ('unihist','start','end','mid')
	logp=np.log(relationmixprob)
	if strokenum>1:
		indx=relationtypes.index(R['type'])
		score=logp(indx)
	else:
		score=0

	if R['type']=='unihist':
		#score = score + libclass.Spatial.score(R.gpos,stroke_num);

	elif:R['type'] in ('start','end')
		score = score - log(R['nprev'])
	elif:R['type']=='mid':
		score = score - log(R['nprev'])
		score = score - log(R['nsub']);
        eval_missing = isempty(R.eval_spot_type);
#        if ~eval_missing:
 #           ncpt = libclass.ncpt
 #           [~,lb,ub] = bspline_gen_s(ncpt,1);
   #         ll = ll - log(ub-lb)
 #           if (R.eval_spot_type < lb || R.eval_spot_type > ub):
     #           ll = -inf
                 	
	return score
def sampleRelationToken():
	
	pass
def scoreRelationToken():
	pass
def scoreRelationTokenApproxMarginalize():
	pass
def samplePosition():
	pass
def scorePosition():
	pass
def sampleImageBlur(minblursigma,maxblursigma):
	return uniform(minblursigma,maxblursigma)
def scoreImageBlur(minblursigma,maxblursigma,blursigma):
	if blursigma<minblursigma or blursigma>maxblursigma
		score=-np.inf
	else:
		score=-np.log(maxblursigma-minblursigma)
	return score
def sampleImageNoise(minepsilon,maxepsilon):
	return uniform(minepsilon,maxepsilon)
def scoreImageNoise(minepsilon,maxepsilon,epsilon):
	if epsilon<minepsilon or epsilon>maxepsilon
		score=-np.inf
	else:
		score=-np.log(maxepsilon-minepsilon)
	return score
def sampleImage(pimg):
	I=binom.rvs(1,pimg)
	return I==1
def scoreImage(I,pimg):
	probon = pimg;
	on = I>0.5
    off = I<0.5
    score=np.log(probon[on]).sum()+np.log(1-probon(off)).sum()
	return score
def sampleAffine():
	pass
def scoreAffine():
	pass
