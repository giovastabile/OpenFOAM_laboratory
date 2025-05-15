import numpy as np
import matplotlib.pyplot as plt

res = np.loadtxt("logs/pFinalRes_1")
plt.plot(res[:,0],res[:,1])
plt.show()