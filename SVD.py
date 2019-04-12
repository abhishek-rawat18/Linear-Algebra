import numpy as np
import pandas as pd

def SVD(A,b,alpha,players):

    n=len(players)
    I=np.identity(n,dtype=float) #identity matrix
    C=I-alpha*A
    
    U,s,V = np.linalg.svd(C) # SVD decomposition of A , s=sigma

    # Solving Cx=b using the equation V'x=w
    # V'=transpose(V) ,U'=transpose(U)
    # w computed from sigma.w=D
    # x computed using V'x=w
    
    D = np.dot(U.T,b) # D = U^t*b
    w = np.linalg.solve(np.diag(s),D) # w = V^t*D
    x = np.linalg.solve(V,w) # V'x=w

    df=pd.DataFrame()
    df["Players"]=players
    df["Initial"]=list(map(int,b)) #initial points
    df["Final"]=list(map(int,x)) #final points after all matches
    print(df)

A = np.array([[0.,0.,0.,0.,1.,1.,0.,1.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,1.,1.,0.,0.,0.,0.,0.]])

players=["A","B","C","D","E","F","G","H"]
b = np.array([300.,300.,275.,260.,255.,220.,200.,190.]) 
alpha=.25

SVD(A,b,alpha,players)
