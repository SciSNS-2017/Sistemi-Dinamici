import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=11)


n = 1000
j = 0

for e in np.linspace(0.01, 1, num=6):
    for y0 in np.linspace(-0.4, 0.4, num=20):
        print('y0 = %.2f' %y0)
        for x0 in np.linspace(0., 2*np.pi, num=100):
            x = [x0]
            y = [y0]
            for i in range(n):
                y.append(e*np.sin(x[i]) + y[i])
                x.append(np.mod(x[i] + y[i + 1], 2*np.pi))
            plt.plot(x, y, 'b,')
    plt.title(r'$ \varepsilon = %.2f $' %e)
    plt.xlabel('$ x $')
    plt.ylabel('$ y $')
    plt.savefig('sm'+str(j)+'.png', dpi=300)
    plt.close()
    j += 1
