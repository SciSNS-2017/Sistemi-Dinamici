import numpy as np


def Em(m, x):
    return np.modf(m*x)[0]


def sigma(E):
    E = np.roll(E, -1)
    E = np.delete(E, np.size(E)-1)
    return E


def prj(m, E):
    sum = 0
    for i in range(0, np.size(E)):
        sum += E[i]*m**(-i-1)
    return sum


def dynSymbol(m, N, x):
    X = [x]
    L = [int(x*m)]
    for i in range(1, N):
        X.append(Em(m, X[i-1]))
        L.append(int(X[i]*m))
    return L


m = 17
N = 100

x0 = 1/np.pi

print("Em =\t\t\t%.20f" % (Em(m, x0)))
print("prj circ sigma circ l =\t%.20f" %
      (prj(m, sigma(dynSymbol(m, N, x0)))))

# E = (np.random.rand(1, N)[0]*m).astype(int)
# print(E)

# print("Em circ prj =\t" + str(Em(m, prj(m, E))))
# print("prg circ sigma =\t" + str(prj(m, sigma(E))))
