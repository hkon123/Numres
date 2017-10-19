from math import *
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from odes import Ode
from ChargeDistribution import ChargeDistribution
from plots import Plotting



ChargeDistribution().show()

E = Ode(0.04,100,False, ChargeDistribution(), False, 0, -2)
Euler = E.euler()
Runge = E.RK4()
Plotting().plottwo(Euler, Runge, 100)
Plotting().plotResidual(Euler, Runge, 100)

V = Ode(0.04,100,False, False, -1*Runge, 0, -2)
VEuler = V.euler()
VRunge = V.RK4()
Plotting().plottwo(VEuler, VRunge, 100)
Plotting().plotResidual(VEuler, VRunge, 100)
