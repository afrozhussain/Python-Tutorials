# -*- coding: utf-8 -*-
"""
Implementing Covariance and Correlation in Python
Created on Mon Jan 11 20:28:20 2016

@author: Afroz Hussain
"""


def cov(x,y):

    if len(x) != len(y):
        return 
        
    n = len(x)
    
    xy = [x[i]*y[i] for i in range(n)]
    
    mean_x = sum(x)/float(n)
    mean_y = sum(y)/float(n)
    
    return (sum(xy) - n*mean_x * mean_y) / float(n)
    # following code is can also be used to calculate the same result
    #return sum([(x[i]-mean_x)*(y[i]-mean_y) for i in range(n)])


x = [1,2,3,4,5,6,7,8,9 ,10]
y = [0.1, 0.2,0.3, 0.4, 0.5,0.6, 0.7,0.8,0.9,1.0]

print ('Covariance : ' + str(cov(x,y)) ) 


def sd(x):
    if len(x) == 0:
        return 0
    n = len(x)
    
    mean_x = sum(x)/float(n)    
    variance = sum( [(x[i] - mean_x)**2 for i in range(n)])/float(n)
    return variance**0.5
    
def corr(x,y):
    if len(x) != len(y):
        return
        
    correlation = cov(x,y) / float(sd(x)*sd(y))
    return correlation


print ('Correlation of X and Y is ' + str(corr(x,y)))