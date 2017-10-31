from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

'''
Class for plotting the resultant function from the ODE and the residual between the two methods used
'''

class Plotting(object):

    #Method for plotting one set of discrete values
    def plot(self, coords,steps):
        ax = plt.axes()
        xcoords = []
        ycoords = []
        for i in range(steps):
            xcoords.append(coords[i,0])
            ycoords.append(coords[i,1])
        ax.scatter(xcoords,ycoords, c='purple', marker='.', edgecolor = 'face')
        plt.axis('tight')

        plt.show()


    #Method for plotting two sets of discrete values
    def plottwo(self, coords1, coords2, steps, title):
        ax = plt.axes()
        xcoords1 = []
        ycoords1 = []
        xcoords2 = []
        ycoords2 = []
        for i in range(steps):
            xcoords1.append(coords1[i,0])
            ycoords1.append(coords1[i,1])
            xcoords2.append(coords2[i,0])
            ycoords2.append(coords2[i,1])
        ax.scatter(xcoords1,ycoords1, c='r', marker='.', edgecolor = 'face', label = 'euler')
        ax.scatter(xcoords2,ycoords2, c='b', marker='.', edgecolor = 'face', label = 'rk4')
        plt.axis('tight')
        ax.legend('ER', 'right')
        plt.title(title)
        plt.show()

    #method for plotting the residual of two descrete sets of values
    def plotResidual(self,coords1, coords2, steps, title):
        ax = plt.axes()
        xcoords = []
        ycoords = []
        for i in range(steps):
            xcoords.append(coords1[i,0])
            ycoords.append(coords1[i,1]-coords2[i,1])
        ax.scatter(xcoords,ycoords, c='purple', marker='.', edgecolor = 'face')
        plt.axis('tight')
        plt.title(title)
        plt.show()
