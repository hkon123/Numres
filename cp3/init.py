import numpy as np
from minimiser import Minimiser
import scipy.optimize as opt
from plots import Plotting

'''
class for reading in information from the text file
Creates a numpy 3xn numpy array
'''

class Read(object):

    def __init__(self, fileName):
        data= []
        with open(fileName, 'r') as f:
            for line in f:
                for word in line.split():
                    data.append(word)

        self.dataPoints = np.zeros((len(data)/3, 3))
        i = 0
        k = 0
        while i<len(data):
            self.dataPoints[k,0] = data[i]
            self.dataPoints[k,1] = data[i+1]
            self.dataPoints[k,2] = data[i+2]
            i += 3
            k += 1

'''
script for calling the methods from the minimising class
'''


A = Read('testData.txt')

B = Minimiser(1e-9, 1, A.dataPoints)
chi, it, m, c = B.minimize(1,1)
print("Chi squared = " + str(chi))
print(str(it) + " iterations")
print("func = " + str(m) + "x + " + str(c))
chi2 = B.package()
print(chi2)
mcoords = B.createSpace(m, 1000, 0.002, c)
Plotting().plot(mcoords, 1000, "plot of m agaist chi^2 around the true value of m")
ccoords = B.createSpace(c, 1000, 0.01, m, m = False)
Plotting().plot(ccoords, 1000, "plot of c agaist chi^2 around the true value of c")
mError = B.getError(chi, m, mcoords, 1000)
cError = B.getError(chi, c, ccoords, 1000)
print("error in m is: " + str(mError))
print("error in c is: " + str(cError))
