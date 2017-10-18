from math import *
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Ode(object):

    def __init__(self, delta, steps, dist, y0, x0):
        self.delta = delta
        self.steps = steps
        self.dist = dist
        self.y0 = y0
        self.x0 = x0

    def euler(self):
        y0 = self.y0
        x0 = self.x0
        coords = np.array([x0,self.y0])
        for i in range(self.steps):
            y1 = y0 + self.delta*self.dist.evaluate(x0)
            y0 = y1
            x0 = x0 + self.delta
            temp = np.array([x0,y0])
            coords = np.vstack((coords,temp))
        return coords

    def RK4(self):
        y0 = self.y0
        x0 = self.x0
        coords = np.array([x0,self.y0])
        for i in range(self.steps):
            k1 = self.dist.evaluate(x0)
            k2 = self.dist.evaluate(x0 + self.delta*0.5)
            k3 = k2
            k4 = self.dist.evaluate(x0 + self.delta)
            y0 = y0 + self.delta*(float(k1)/6.0 + float(k2)/3.0 + float(k3)/3.0 + float(k4)/6.0)
            x0 = x0 + self.delta
            temp = np.array([x0,y0])
            coords = np.vstack((coords,temp))
        return coords

    def plot(self, coords):
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords[i,0],coords[i,1]), 0.05, color = 'r'))

        plt.axis('equal')

        plt.show()

    def plottwo(self, coords1, coords2):
        ax = plt.axes()
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords1[i,0],coords1[i,1]), 0.005, color = 'r'))
            ax.add_patch(patches.Circle((coords2[i,0],coords2[i,1]), 0.005, color = 'g'))
        plt.axis('equal')

        plt.show()


    def plotDiff(self, coords1, coords2):
        ax = plt.axes()
        #ax.scatter(coords1[0],coords1[1]-coords2[1], c='purple', marker='.')
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords1[i,0],coords1[i,1]-coords2[i,1]), 0.0005, color = 'b'))
        ax.axis("tight")
        #plt.ylim(-0.0105,0.0105)
        #plt.xlim(-2,2)
        plt.show()
