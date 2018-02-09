import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




x = np.arange(0, 1000000, 1000)
y = np.arange(0,1000000, 1000)

plt.ylabel('Proportion')
plt.xlabel('Range')
plt.plot(y, x)
plt.show()
