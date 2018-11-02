import numpy as np
import matplotlib.pyplot as plt


def E(x, y):
    return 0.5*(y**2) + np.cos(x)
    
n = 1000

x_ = np.linspace(0, 2*np.pi, num=n)
y_ = np.linspace(-2, 2, num=n)
x, y = np.meshgrid(x_, y_)

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=11)
plt.rcParams['contour.negative_linestyle'] = 'solid'

plt.contour(x, y, E(x, y),  60, colors='b', linewidths=0.3)
plt.xlabel('$ x $')
plt.ylabel('$ y $')
plt.savefig('fase-pendolo.png', dpi=300)
plt.close()
