from sympy.abc import x, y
from odes import Ode
from ChargeDistribution import ChargeDistribution
from plots import Plotting

'''
calling the ODE class and the plotting class
'''

ChargeDistribution().show()

E = Ode(0.04,100,False, ChargeDistribution(), False, 0, -2)
Euler = E.euler()
Runge = E.RK4()
Plotting().plottwo(Euler, Runge, 100, 'Plot of E field')
Plotting().plotResidual(Euler, Runge, 100, 'Residual of the E Field')

V = Ode(0.04,100,False, False, -1*Runge, 0, -2)
VEuler = V.euler()
VRunge = V.RK4()
Plotting().plottwo(VEuler, VRunge, 100, 'Plot of V field')
Plotting().plotResidual(VEuler, VRunge, 100, 'Residual of V field')
