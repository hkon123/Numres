import numpy as np
from minimiser import Minimiser
import scipy.optimize as opt

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

A = Read('testData.txt')
#print(A.dataPoints)

B = Minimiser(1e-9, 1, A.dataPoints)
chi, it, m, c = B.minimize(1,1)
print("Chi squared = " + str(chi))
print(str(it) + " iterations")
print("func = " + str(m) + "x + " + str(c))
chi2 = B.package()
print(chi2)
B.plot()

'''
def package():
    filename = 'testData.txt'

    data = np.loadtxt(open(filename,"r"),delimiter="  ")

    stress = data[:,0]
    strain = data[:,1]
    err_stress = data[:,2]
    print(data)
    x0 = np.array([0,1])

    result =  opt.minimize(chisqfunc, x0)
    return result

def chisqfunc(a, b):
    model = a + b*strain
    chisq = np.sum(((stress - model)/err_stress)**2)
    return chisq


print(package())
'''
