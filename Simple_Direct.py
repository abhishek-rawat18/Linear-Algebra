import numpy as np
import pandas as pd

def solution(A,b,alpha,players):
    
    I=np.identity(8,dtype=float) #identity matrix
    C=I-alpha*A
    
    x = np.linalg.solve(C, b)

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


solution(A,b,alpha,players)
