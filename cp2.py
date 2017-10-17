from math import *
from sympy import *
from sympy.abc import x, y
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ode2 import Ode
from ChargeDistribution import ChargeDistribution
from ode4 import Ode2


ChargeDistribution().show()

E = Ode(0.01,400,ChargeDistribution(),0, -2)
Euler = E.euler()
Runge = E.RK4()
E.plottwo(Euler, Runge)

V = Ode2(0.01,400, Runge, 0, -2)
VEuler = V.euler()
V.plot(VEuler)
