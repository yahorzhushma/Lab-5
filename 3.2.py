import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, cmap='viridis')
plt.title('График функции z1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

z2 = x**2 - y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z2, cmap='viridis')
plt.title('График функции z2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

z3 = 2*x + 3*y
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z3, cmap='viridis')
plt.title('График функции z3')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

z4 = x**2 + y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z4, cmap='viridis')
plt.title('График функции z4')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

z5 = 2 + 2*x + 2*y - x**2 - y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z5, cmap='viridis')
plt.title('График функции z5')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
