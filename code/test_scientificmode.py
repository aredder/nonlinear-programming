import numpy as np
import matplotlib.pyplot as plt

#%%
s = np.linspace(0,1,100)
u_s = s**2
plt.figure(figsize=(8, 6))
plt.xlabel('s')
plt.ylabel('u(s)')
plt.plot(s,u_s, label = r'$u(s) = s^2$')
plt.legend()
plt.show()

#%%
s = np.linspace(0,1,100)
g_s = np.exp(0-s)*s**2
plt.figure(figsize=(8, 6))
plt.xlabel('s')
plt.ylabel('g(s)')
plt.plot(s,g_s, label = r'$e^{-s}s^2$')
plt.legend()
plt.show()