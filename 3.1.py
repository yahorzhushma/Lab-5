from matplotlib import pyplot as plt
import numpy as np

def f(x, c):
    return np.abs(2 * x - c) ** 0.6 + 0.567

x = np.linspace(-10, 10, 100)
c = np.arange(-10, 1, 0.25)
fx = f(3.67, c)

for i in range(len(c)):
    print(f"c = {c[i]}, f(x) = {fx[i]}")

max = np.max(fx)
min = np.min(fx)
mean = np.mean(fx)
num = len(fx)

sorted_ind = np.argsort(fx)[::-1]
sorted_c = c[sorted_ind]
sorted_fx = fx[sorted_ind]

plt.figure(figsize=(10, 6))
plt.plot(c, fx, marker='o', label='f(x)')
plt.axhline(mean, color='r', linestyle='-', label='Среднее f(x)')
plt.xlabel('c')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.legend()
plt.grid(True)
plt.show()