import numpy as np
from numpy import size
from array import array
import matplotlib.pyplot as plt
import random
from PyQt4.QtGui import *
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import fill


height = 350
width =  650




# def feedForward(inputs, N):
#     weights = np.random.randn(N)  
#     summe = np.sum (inputs * weights)
#     return summe
    

def func(x):
    return 2*x + 1
    


#===============================================================================
# def setup():
#     N = 1000 
#     answer = 1
#     training = []
#     for _ in range(N):
#         x = random.randint(-width/2, width/2)
#         y = random.randint(-height/2, height/2)
#         if (y < func(x)):
#             answer = -1
#         training.append(Training(x, y, answer))
#===============================================================================

        
                           
def setup_And_draw():
    input_number = 3
    p = Perceptron(input_number)
    N = 400                
    answer = 1
    training = []
    

    a = np.linspace(-width, width, 10)
    b = np.linspace(-height, height, 10)
    np.vstack((a,b))
    plt.plot(a, -b, '-')
    #w =np.random.randn(3)
    for i in range(N):
        x = random.randint(-width/2, width/2)
        y = random.randint(-height/2, height/2)
        if (y < func(x)):
            answer = -1
        training.append(Training(x, y, answer))
        guess = p.feedForward(training[i].inputs) 
        p.weights += p.train(training[i].inputs, training[i].a)#
        if (guess > 0 ):
            plt.plot(training[i].inputs[0]- (width/2) , training[i].inputs[1]- (height/2), 'ro') 
            plt.hold(True)  
             
        else: 
            plt.plot(training[i].inputs[0]+ (width/2) , training[i].inputs[1]+ (height/2), 'g*')
            plt.hold(True)
            
    plt.plot(p.weights, -y*p.weights)
     
    
    plt.show()
   
   
class Perceptron(object):
   
    def __init__(self, N):

        self.N = N
        self.weights = np.random.randn(3)
    
    def feedForward(self, inputs): 
        summe = np.sum (inputs * self.weights)
        if(summe >= 0):
            return 1
        else:
            return -1 
        
    def train(self, inputs, desired):  
        #self.weights = np.random.randn(3)
        #self.weights = np.array([0,0,0])
        c = 0.01
        self.guess = self.feedForward(inputs) 
        self.error = desired - self.guess
        self.weights = c * self.error * inputs 
        return self.weights   


class Training(object):

    
    a = 0
    
    def __init__(self, x, y, answer):
        self.inputs = np.array([0,0,0])
        self.inputs[0] = x
        self.inputs[1] = y
        self.inputs[2] = 1      # bias
        self.a = answer
  
   
   
'Main Method'
 
if __name__ == '__main__':
    
    #p = Perceptron(3)
    setup_And_draw()


    
                