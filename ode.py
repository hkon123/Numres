from math import *
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Ode(object):

    def __init__(self, delta, steps, func, y0):
        self.delta = delta
        self.steps = steps
        self.func = func
        self.y0 = y0

    def euler(self):
        y0 = self.y0
        f = lambdify((x), self.func)
        x0 = 0
        coords = np.array([x0,self.y0])
        for i in range(self.steps):
            y1 = y0 + self.delta*f(x0)
            y0 = y1
            x0 = x0 + self.delta
            temp = np.array([x0,y0])
            coords = np.vstack((coords,temp))
        return coords

    def RK4(self):
        y0 = self.y0
        f = lambdify((x), self.func)
        x0 = 0
        coords = np.array([x0,self.y0])
        for i in range(self.steps):
            k1 = f(x0)
            k2 = f(x0 + self.delta*0.5)
            k3 = k2
            k4 = f(x0 + self.delta)
            y0 = y0 + self.delta*(float(k1)/6.0 + float(k2)/3.0 + float(k3)/3.0 + float(k4)/6.0)
            x0 = x0 + self.delta
            temp = np.array([x0,y0])
            coords = np.vstack((coords,temp))
        return coords

    def plot(self, coords):
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords[i,0],coords[i,1]), 0.05, color = 'r'))

        plt.axis('scaled')

        plt.show()

    def plottwo(self, coords1, coords2):
        ax = plt.axes()
        for i in range(self.steps):
            ax.add_patch(patches.Circle((coords1[i,0],coords1[i,1]), 0.01, color = 'r'))
            ax.add_patch(patches.Circle((coords2[i,0],coords2[i,1]), 0.01, color = 'g'))
        plt.axis('scaled')

        plt.show()


A= Ode(0.01, 750, cos(x), 0)
a = A.euler()
b = A.RK4()
A.plottwo(a,b)
