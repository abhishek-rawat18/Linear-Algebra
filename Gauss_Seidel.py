import numpy as np
import pandas as pd

def GaussSeidel(A,b,alpha,players):
    
    I=np.identity(8,dtype=float) #identity matrix
    C=I-alpha*A #as we want to solve Cx=b
    
    tolerance=0.0001
    max_iterations=10000
    
    x_prev=np.zeros_like(b) #some random predecided x
    
    for i in range(0,max_iterations):

        x_new=np.zeros_like(x_prev)
        
        for j in range(len(C)):
            s1=np.dot(C[j, :j], x_new[:j])
            s2=np.dot(C[j, j + 1:], x_prev[j + 1:])
            x_new[j]=(b[j]-s1-s2)/C[j,j]

        if np.allclose(x_prev,x_new,rtol=tolerance):
            break #if converges, break out of the loop
            
        x_prev=x_new
        
    df=pd.DataFrame()
    df["Players"]=players
    df["Initial"]=list(map(int,b)) #initial points
    df["Final"]=list(map(int,x_new)) #final points after all matches
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

GaussSeidel(A,b,alpha,players)
