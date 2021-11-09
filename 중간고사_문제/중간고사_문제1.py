import numpy as np
import pandas as pd
epsilon = 0.0000001

def perceptron_or(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    B = -0.2
    tmp = np.dot(W,X) + B
    if tmp > epsilon:
        return 1
    else:
        return 0
    
arr = np.array([
    [0,0,perceptron_or(0,0)],
    [0,1,perceptron_or(0,1)],
    [1,0,perceptron_or(1,0)],
    [1,1,perceptron_or(1,1)]
])

df = pd.DataFrame(arr,columns=['x1','x2','y'])
print(df)