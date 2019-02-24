import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


def f(x, beta):
    return np.tanh(beta*x) - x


init = 1

betas = np.logspace(np.log10(0.7), np.log10(100), 2000)
Ms = []

for b in betas:
    Ms.append(fsolve(f, x0=init, args=[b]))
#    print(b)

Ms = np.array(Ms)

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=11)

plt.xlabel('$1/\\beta$')
plt.ylabel('$\\bar{M}$')
plt.xlim(0, 1.4)
plt.plot(1/betas, Ms, color='k')
plt.plot(1/betas, -Ms, color='k')
plt.savefig('transizione.pdf')
# plt.show()
