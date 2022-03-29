import numpy as np
import scipy
import math
from scipy import integrate
e = math.e
j=[0, 1]
k=[0, -1, 1]
def phi(A, t, s, c):
    if c:
        return (A*e**((-t**2)/2)) * (e ** (1j * s * t)) - (e ** ((-s**2)/2))
    return (A*e**((-t**2)/2)) * (e ** (-1j * s * t)) - (e ** ((-s**2)/2))

def inner_product(func, j, k):
    return 2**(j/2) * scipy.integrate.quad(phi(1, x*2**j, 1, 0)*func, 0, 1)


def testfunct():
    return x**2
def runExpansion(arrJ, arrK):
    currsum = 0
    for p in range(len(arrJ)):
        for q in range(len(arrK)):
            currsum += 2**(arrJ[p]/2)*phi(1, x*2**arrJ[p], 1, 1)*inner_product(testfunct(1), arrJ[p], arrK[q])
    return currsum
runExpansion(j, k)
