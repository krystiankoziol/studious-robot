import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#https://scriptverse.academy/tutorials/python-matplotlib-plot.html

#%% plot of temp
mounths = [1,2,3,4,5,6,7,8,9,10,11,12]
high_temp = [30,31,31,31,31,31,31,31,31,31,30,29] # average high
low_temp = [23,24,24,24,25,24,24,24,24,24,24,23] # average low
plt.plot(mounths,high_temp, 'm-.', mounths, low_temp, 'c:')
plt.xlabel('Months', color='#1e8bc3')
plt.ylabel('Temperature (°C)', color='#e74c3c')
plt.title('Temperature in Singapore', color='#34495e')
high_legend = mpatches.Patch(color='magenta', label='High')
low_legend = mpatches.Patch(color='cyan', label='Low')
plt.legend(handles=[high_legend,low_legend])
plt.show()
#%% build a scatter plot
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


#%% plot versus x as line
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min()*1.1, C.max()*1.1)
plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

plt.show()
