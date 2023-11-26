from matplotlib import pyplot as plt
import numpy as np

x = 3.67
c = np.arange(-10, 1, 0.25)
print(c)
l = np.abs(2 * x - c) ** 0.6 + 0.567
print(l)

max = l.max()
min = l.min()
aver = l.mean()
count = l.size()
print(max)
print(min)
print(aver)
print(count)
l.argsort()
print(l)
plt.plot(c, l, color="cyan", marker='0', markersize=8)
l = c + aver - c
plt.plot(c, l)
plt.xlabel('OX')
plt.ylabel('OY')
plt.title('График функции')
plt.yscale(value='log')
plt.show()