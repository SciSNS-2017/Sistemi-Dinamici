import numpy as np
import matplotlib.pyplot as plt


n = 1000
 
j = 0

for e in np.linspace(0, 2, num=20):
    for y0 in np.linspace(-0.4, 0.4, num=10):
        for x0 in np.linspace(0., 2*np.pi, num=100):
            x = [x0]
            y = [y0]
            for i in range(n-1):
                y.append(e*np.sin(x[i]) + y[i])
                x.append(np.mod(x[i] + y[i + 1], 2*np.pi))
            plt.plot(x, y, 'b,')
    plt.savefig('sm'+str(j)+'.png', dpi=900)
    plt.close()
    j += 1