from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches



class Plotting(object):

    def plot(self, coords,steps):
        ax = plt.axes()
        xcoords = []
        ycoords = []
        for i in range(steps):
            xcoords.append(coords[i,0])
            ycoords.append(coords[i,1])
        ax.scatter(xcoords,ycoords, c='purple', marker='.')
        plt.axis('tight')

        plt.show()

    def plottwo(self, coords1, coords2, steps):
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
        ax.scatter(xcoords1,ycoords1, c='r', marker='.')
        ax.scatter(xcoords2,ycoords2, c='g', marker='.')
        plt.axis('tight')
        plt.show()

    def plotResidual(self,coords1, coords2, steps):
        ax = plt.axes()
        xcoords = []
        ycoords = []
        for i in range(steps):
            xcoords.append(coords1[i,0])
            ycoords.append(coords1[i,1]-coords2[i,1])
        ax.scatter(xcoords,ycoords, c='purple', marker='.')
        plt.axis('tight')

        plt.show()
