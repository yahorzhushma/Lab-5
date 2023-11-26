import numpy as np

x = 0.75
y = (np.sin(np.pi / 8 - 1) ** 2 + (3 + x ** 2) ** (1 / 4)) / (np.arcsin(x / 2) - 5.236 * 10 ** (-2)) + np.log(
    np.abs(3.12 - x))
print(y)
