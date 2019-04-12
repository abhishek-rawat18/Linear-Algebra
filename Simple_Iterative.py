import numpy as np
import pandas as pd

def SimpleIterative(A,b,alpha,players):
    
    tolerance=0.0001
    max_iterations=10000
    
    x_prev=np.zeros_like(b) #some random predecided x

    A=alpha*A #We want to compute x = alpha*Ax + b
    
    for i in range(0,max_iterations):
        
        x_new=np.dot(A,x_prev)+b
                
        if np.allclose(x_prev,x_new,rtol=tolerance):
            break
            
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


SimpleIterative(A,b,alpha,players)

