import numpy as np

def Jacobi(A,b,alpha):
    
    I=np.identity(8,dtype=float) #identity matrix
    C=I-alpha*A #as we want to solve Cx=b
    
    tolerance=0.0001
    max_iterations=10000
    
    x_prev=np.zeros_like(b) #some random predecided x
    
    for i in range(0,max_iterations):
    
        x_new=np.zeros_like(x_prev)
        
        for j in range(len(C)):
            s1=np.dot(C[j, :j], x_prev[:j])
            s2=np.dot(C[j, j + 1:], x_prev[j + 1:])
            x_new[j]=(b[j]-s1-s2)/C[j,j]

        if np.allclose(x_prev,x_new,rtol=tolerance):
            break #if converges, break out of the loop
            
        x_prev=x_new
        
    print(x_new)
    
A = np.array([[0.,1.,1.,0.,1.,0.,0.,0.],
              [0.,0.,0.,1.,0.,0.,0.,1.],
              [0.,0.,0.,0.,0.,1.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.],
              [0.,0.,0.,0.,0.,0.,0.,0.]])

b = np.array([100.,100.,100.,100.,100.,100.,100.,100.])

alpha=.5

Jacobi(A,b,alpha)
