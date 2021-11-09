import numpy as np
import matplotlib.pyplot as plt

learning_rate = float(input('learning_rate : '))

def gradient_descent(learning_rate):
    x = 10
    learning_rate = learning_rate
    precision = 0.00001
    max_iterations = 100
    
    loss_func = lambda x: 𝑥**2-6*𝑥+4
    
    gradient = lambda x: 2*x-6
    
    x_ax = np.arange(0,10.2,0.2)
    y_ax = np.array([])

    for i in x_ax:
        y_ax = np.append(y_ax,np.array([loss_func(i)]))

    for i in range(max_iterations):
        x = x - learning_rate * gradient(x)
        #print("손실함수값 (", x, ")=", loss_func(x))
        plt.scatter(x,loss_func(x), marker='*', color= 'orange')
    print("최소값 = ", x)

    plt.plot(x_ax,y_ax)
    plt.show()

#for i in [0.2,0.5,0.8,0.95]:
gradient_descent(i)
