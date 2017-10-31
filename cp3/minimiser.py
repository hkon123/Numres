from math import *
import numpy as np
import os
import time
import scipy.optimize as opt
import matplotlib.pyplot as plt


class Minimiser(object):

    def __init__(self, treshHold, initialStep, dataPoints):
        self.treshHold = treshHold
        self.dataPoints = dataPoints
        self.step = initialStep

    def valueOfFunction(self,x , m, c):
        return m*x + c

    def valueOfChi(self, m, c):
        d = 0
        for i in range(10):
            d += (float(self.dataPoints[i,1] - self.valueOfFunction(self.dataPoints[i,0], m, c))/self.dataPoints[i,2])**2
        return d

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

    def chisqfunc(a, b):
        yPred = b[1] + b[0]*xValues
        chisq = np.sum(((yValues - yPred)/error)**2)
        return chisq


    def plot(self):
        ax = plt.axes()
        mCoords = []
        cCoords = []
        chiCoords = []
        for i in range(1, self.iterations):
            mCoords.append(self.coords[i,0])
            cCoords.append(self.coords[i,1])
            chiCoords.append(self.coords[i,2])
        ax.scatter(mCoords,chiCoords, c='purple', marker='.', edgecolor = 'face')
        #ax.scatter(cCoords,chiCoords, c='b', marker='.', edgecolor = 'face')
        plt.axis('tight')
        plt.show()
