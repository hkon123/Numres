from math import *
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Ode2(object):

    def __init__(self, delta, steps, discrete, y0, x0):
        self.delta = delta
        self.steps = steps
        self.discrete = -1*discrete
        self.y0 = y0
        self.x0 = x0

    def euler(self):
        y0 = self.y0
        x0 = self.x0
        coords = np.array([x0,self.y0])
        for i in range(self.steps):
            y1 = y0 + self.delta*self.discrete[i,1]
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
            k1 = self.discrete[i,1]
            dy = self.discrete[i+1,1]-self.discrete[i,1]
            k2 = self.discrete[i,1] + dy/2
            k3 = k2
            k4 = self.discrete[i+1,1]
            y0 = y0 + self.delta*(float(k1)/6.0 + float(k2)/3.0 + float(k3)/3.0 + float(k4)/6.0)
            x0 = x0 + self.delta
            temp = np.array([x0,y0])
            coords = np.vstack((coords,temp))
        return coords

    def plot(self, coords):
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords[i,0],coords[i,1]), 0.005, color = 'r'))

        plt.axis('scaled')

        plt.show()

    def plottwo(self, coords1, coords2):
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords1[i,0],coords1[i,1]), 0.005, color = 'r'))
            ax.add_patch(patches.Circle((coords2[i,0],coords2[i,1]), 0.005, color = 'g'))
        plt.axis('scaled')

        plt.show()
