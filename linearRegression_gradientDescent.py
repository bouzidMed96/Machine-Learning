# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:03:27 2019

@author: bouzidMed
"""""

from numpy import *

def error_compute(b,m,data):
    error = 0
    for i in range(0,len(data)):
        x = data[i,0]
        y = data[i,1]
        error += (y - (m*x +b)) **2
    
    return error/float(len(data))       
    
def gradientDescentCalculus(b,m,data,epsilon):
    gradient_b = 0
    gradient_m = 0
    for i in range(len(data)):
        x = data[i,0]
        y = data[i,1]
        gradient_b += -(2/float(len(data))) * (y - ((m * x) + b))
        gradient_m += -(2/float(len(data))) * x * (y - ((m * x) + b))
    corrected_b = b - (epsilon * gradient_b)
    corrected_m = m - (epsilon * gradient_m)
    return [corrected_b,corrected_m]

def gradientDescent(data,b_start,m_start,epsilon,numIteration):
    b = b_start
    m = m_start
    for i in range(numIteration):
        b, m = gradientDescentCalculus(b, m, array(data), epsilon)
    print ([b,m])
    return [b, m]
    
    
    
    
    
    
def A():
    #loading data
    dataset = genfromtxt('data.csv',delimiter=',')
    #hyperparameters
    epsilon = 0.0001
    start_m = 0
    start_b = 0
    numIteration = 1000
    
    start_error = error_compute(start_b,start_m,dataset)
    print("before applying gradient descent b was 0 m was 0 and the error was ",start_error)
    [b,m] = gradientDescent(dataset,start_b,start_m,epsilon,numIteration)
    end_error = error_compute(b,m,dataset)
    print('after applying gradient descent b is {0} m is {1} and the error is {2}'.format(b,m,error_compute(b,m,dataset)))










if __name__ == '__main__':
    A()


        
