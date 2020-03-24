import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv('Linear_X_Train.csv').values
Y = pd.read_csv('Linear_Y_Train.csv').values

theta = np.load('ThetaList.npy')

T0 = theta[:, 0]
T1 = theta[:, 1]

# interactive plot
plt.ion()

for i in range(0, 50, 3):
    y_ = T1[i]*X + T0
    
    plt.scatter(X, Y)
    plt.plot(X, y_, 'red')
    
    plt.draw()
    plt.pause(1)
    plt.clf()
    