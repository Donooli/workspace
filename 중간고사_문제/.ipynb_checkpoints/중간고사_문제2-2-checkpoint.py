import numpy as np
import pandas as pd
epsilon = 0.0000001

def perceptron_or(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.17, 0.18])
    B = -0.2
    tmp = np.dot(W,X) + B
    if tmp > epsilon:
        return 1
    else:
        return 0
    
arr = np.array([
    [0.10, 0.72, perceptron_or(0.10, 0.72)],
    [0.35, 0.54, perceptron_or(0.35, 0.54)],
    [0.45, 0.13, perceptron_or(0.45, 0.13)],
    [0.60, 0.30, perceptron_or(0.60, 0.30)],
    [0.30, 0.96, perceptron_or(0.30, 0.96)],
    [0.15, 1.00, perceptron_or(0.15, 1.00)],
    [0.70, 0.85, perceptron_or(0.70, 0.85)],
    [0.95, 0.40, perceptron_or(0.95, 0.40)]
])

df = pd.DataFrame(arr,columns=['x1','x2','y'])
print(df)

