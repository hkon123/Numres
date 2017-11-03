from math import *
import numpy as np
import os
import time
import scipy.optimize as opt
import matplotlib.pyplot as plt


'''
Class for minimizing chi^2 for a straight line through a set of given datapoints with errors
and find the errors on m and c
'''

class Minimiser(object):

    #initialiser setting some basic inital values to launch the minimizer
    def __init__(self, treshHold, initialStep, dataPoints):
        self.treshHold = treshHold
        self.dataPoints = dataPoints
        self.step = initialStep

    #method for calculating the value of the function given an x, m and c
    #returns the value of the function
    def valueOfFunction(self,x , m, c):
        return m*x + c

    #method for calculating the value of chi^2 given an m and a c
    #returns the value of chi^2
    def valueOfChi(self, m, c):
        d = 0
        for i in range(10):
            d += (float(self.dataPoints[i,1] - self.valueOfFunction(self.dataPoints[i,0], m, c))/self.dataPoints[i,2])**2
        return d

    '''
    minimiser method. minimizes by testing if the value of chi^2 gets smaller when m, c or both changes
    by a given increment( positive or negative).
    if the value of chi^2 gets smaller, it changes the current value of chi^2 to the new value,
    changes the variable that was changed to its new value, and restarts the process.
    if chi^2 does not get smaller with any of the changes, the increment of the change is halfed
    untill it reaches a given treshold.
    the priority of the test is: change in m->change in m and c->change in c
    the method returns the smallest value of chi^2, number of iterations needed to reach it,
    best fit value of m and best fit value of c
    '''
    def minimize(self,m ,c ):
        currentValue = self.valueOfChi(m, c)
        iterations = 0
        self.coords = np.array([m, c, currentValue])
        while self.step > self.treshHold:
            self.coords = np.vstack((self.coords, np.array([m, c, currentValue])))
            iterations +=1
            testValue = self.valueOfChi(m + self.step, c)
            if testValue > currentValue:
                testValue = self.valueOfChi(m - self.step, c)
            else:
                m += self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m + self.step, c + self.step)
            else:
                m -= self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m - self.step, c + self.step)
            else:
                m += self.step
                c += self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m + self.step, c - self.step)
            else:
                m -= self.step
                c += self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m - self.step, c - self.step)
            else:
                m += self.step
                c -= self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m, c + self.step)
            else:
                m -= self.step
                c -= self.step
                currentValue = testValue
                continue
            if testValue > currentValue:
                testValue = self.valueOfChi(m, c - self.step)
            else:
                c += self.step
                currentValue = testValue
                continue
            if testValue > currentValue:

                self.step = self.step/2.0
                continue
            else:
                c -= self.step
                currentValue = testValue
                continue
        self.iterations = iterations
        return currentValue, iterations, m , c



    #method for calling the scipy.otimize.minimize, returns the results from the minimizer package
    def package(self):
        filename = 'testData.txt'

        data = np.loadtxt(open(filename,"r"),delimiter="  ")

        global yValues
        global xValues
        global error

        xValues = data[:,0]
        yValues = data[:,1]
        error = data[:,2]


        x0 = np.array([1,1])

        result =  opt.minimize(self.chisqfunc, x0)
        return result

    #method passed to ccipy.optimize.minimize that it uses to find the value of the function
    def chisqfunc(a, b):
        yPred = b[1] + b[0]*xValues
        chisq = np.sum(((yValues - yPred)/error)**2)
        return chisq


    #method for creating values of chi^2 around the true values found by the minimizer
    #returns coordinates for m vs chi^2/ c vs chi^2
    def createSpace(self,value, points, delta, othervalue, m = True):
        start = value - delta
        end = value + delta
        valuePoints = np.linspace(start, end, points)
        if m == True:
            coords = np.array([valuePoints[0],self.valueOfChi(valuePoints[0],othervalue)])
            for i in range(1,valuePoints.size):
                coords = np.vstack((coords, np.array([valuePoints[i], self.valueOfChi(valuePoints[i], othervalue)])))
        else:
            coords = np.array([valuePoints[0],self.valueOfChi(othervalue, valuePoints[0])])
            for i in range(1,valuePoints.size):
                coords = np.vstack((coords, np.array([valuePoints[i], self.valueOfChi(othervalue, valuePoints[i],)])))
        return coords

    #method for calculating the error of the found values of m and c by checking where the line
    # y = chi^2(minimum)+1 crosses the function of m/c vs chi^2 and returns the change in m/c at that point
    def getError(self, chi, value, coords, steps):
        for i in range(steps-1):
            if( coords[i,1]> (chi+1) and coords[i+1,1]< (chi+1)):
                return sqrt(((coords[i,0] + coords[i+1,0])/2 - value)**2)
