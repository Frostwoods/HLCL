import numpy as np
import matplotlib.pyplot as plt

#% Fit a bspline using least-squares
#% 
#% Input
#%   sval: time points (N x 1)
#%   X: data points (N x 2)
#%   L: number of control points to fit
#% 
#% Output:
#%   P: (L x 2) optimal control points

#function P = bspline_fit(sval,X,L)
#    sval = sval(:);
#    ns = length(sval);
#    assert(isequal(size(X),[ns 2]));
#   
#    S = repmat(sval,[1 L]);
#    I = repmat(0:L-1,[ns 1]);
#    A = vectorized_bspline_coeff(I,S);
#    
#    sumA = sum(A,2);
#    Cof = A ./ repmat(sumA,[1 L]);
#    P = (Cof'*Cof)\Cof'*X;
#    %P = inv(Cof'*Cof)*Cof'*X;
#end

def bSplineFit(sval, dataPoints, numOfControlPoints = 5):
    S = np.tile(sval, (numOfControlPoints, 1)).T
    I = np.tile(np.arange(numOfControlPoints), (len(sval), 1))

    A = np.matrix(vectorizedBsplineCoeff(I, S))
    sumA = np.sum(A, 1)
    Coeff = A / np.matrix(np.tile(sumA, (1, numOfControlPoints)))
#    P  = ((Coeff.T * Coeff) / Coeff.T) * dataPoints
    P = np.linalg.inv(Coeff.T * Coeff) * Coeff.T * dataPoints
    return P

#% function vectorized_bspline_coeff
#% ------
#% 
#% Input
#%  vi [n x m] 
#%  vs: [n x m]

#%
#% Output
#%   C [n x 1]: the coefficients
#function C = vectorized_bspline_coeff(vi,vs)
#    
#    assert(isequal(size(vi),size(vs)));
#    
#    % Go through conditions 
#    C = zeros(size(vi));
#    
#    sel1 = vs >= vi & vs < vi+1;
#    C(sel1) = (1/6)*(vs(sel1)-vi(sel1)).^3;
#    
#    sel2 = vs >= vi+1 & vs < vi+2;
#    C(sel2) = (1/6)*(-3*(vs(sel2)-vi(sel2)-1).^3 + 3*(vs(sel2)-vi(sel2)-1).^2 + 3*(vs(sel2)-vi(sel2)-1)+1);
#    
#    sel3 = vs >= vi+2 & vs < vi+3;
#    C(sel3) = (1/6)*(3*(vs(sel3)-vi(sel3)-2).^3 - 6*(vs(sel3)-vi(sel3)-2).^2 + 4);
#    
#    sel4 = vs >= vi+3 & vs < vi+4;
#    C(sel4) = (1/6)*(1-(vs(sel4)-vi(sel4)-3)).^3;
#
#end

def vectorizedBsplineCoeff(vi, vs):

    C = np.zeros(vi.shape)+1e-6
    bool1 = (vs >= vi).astype(int)
    bool2 = (vs < (vi + 1)).astype(int)
    bool3 = (vs >= (vi + 1)).astype(int)
    bool4 = (vs < (vi + 2)).astype(int)
    bool5 = (vs >= (vi + 2)).astype(int)
    bool6 = (vs < (vi + 3)).astype(int)
    bool7 = (vs >= (vi + 3)).astype(int)
    bool8 = (vs < (vi + 4)).astype(int)

    sel1 = (bool1 * bool2).astype(bool)
#    sel1 = (vs >= vi) 
    C[sel1] = (1/6)*(vs[sel1]-vi[sel1]) ** 3

    sel2 = (bool3 * bool4).astype(bool)
    C[sel2] = (1/6)*(-3*(vs[sel2]-vi[sel2]-1)**3 + 3*(vs[sel2]-vi[sel2]-1)**2 + 3*(vs[sel2]-vi[sel2]-1) + 1)

    sel3 = (bool5 * bool6).astype(bool)
    C[sel3] = (1/6)*(3*(vs[sel3]-vi[sel3]-2)**3 - 6*(vs[sel3]-vi[sel3]-2)**2 + 4)

    sel4 = (bool7 * bool8).astype(bool)
    C[sel4] = (1/6)*(1-(vs[sel4]-vi[sel4]-3))**3 

    return C

sval = np.arange(9)
#dataPoints = np.array([[0,1], [1,1], [2,4], [3,9], [4, 16], [5,25], [6,36], [7,49], [8,64],[9,81]])
dataPoints = np.array([[-1,0], [-0.866,0.5], [-0.707,0.707], [-0.5,0.866], [0,1], [0.5, 0.866],[0.707,0.707], [0.866,0.5], [1,0]])
#dataPoints = np.array([[0,0], [1,1], [2,2], [3,3], [4, 4], [5,5], [6,6], [7,7], [8,8],[9,9]])
ctp = bSplineFit(sval,dataPoints).T
x = np.array(ctp[0].flatten())
y = np.array(ctp[1].flatten())
plt.scatter(x,y)
plt.show()
