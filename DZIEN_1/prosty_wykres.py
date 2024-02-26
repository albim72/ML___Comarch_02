import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2*np.pi*t)

fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas[s]',ylabel='napięcie prądu [mV]', title='pomiar napięcia prądu w czasie t')
ax.grid(True)
fig.savefig('current.png')
plt.show()
