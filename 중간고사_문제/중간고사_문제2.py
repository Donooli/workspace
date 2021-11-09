import numpy as np
import pandas as pd
epsilon = 0.0000001

def step_func(t):
    if t > epsilon:
        return 1
    else:
        return 0
    
X = np.array([
    [0.10, 0.72, 1],
    [0.35, 0.54, 1],
    [0.45, 0.13, 1],
    [0.60, 0.30, 1],
    [0.30, 0.96, 1],
    [0.15, 1.00, 1],
    [0.70, 0.85, 1],
    [0.95, 0.40, 1]
])

y = np.array([0,0,0,0,1,1,1,1])

W = np.zeros(len(X[0]))
print(W)

def perceptron_fit(X, Y, epochs= 10):
    
    global W
    eta = 0.2
    
    for t in range(epochs):
        print("epoch=", t, "======================")
        for i in range(len(X)):
            predict = step_func(np.dot(X[i],W))
            error = Y[i] - predict
            W += eta * error * X[i]
            print("현재 처리 입력 =", X[i], "정답 =", Y[i], "출력 =", predict, "변경된 가중치 =", W)
        print("================================")
        
def perceptron_predict(X,Y):
    global W
    arr = np.empty((0,3), float)
    for x in X:
        arr = np.append(arr,np.array([[x[0],x[1],step_func(np.dot(x,W))]]), axis=0)
    df = pd.DataFrame(arr,columns=['x1','x2','y'])
    print(df)
        
perceptron_fit(X,y,7)
perceptron_predict(X,y)