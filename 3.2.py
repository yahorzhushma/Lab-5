import numpy as np
from matplotlib import pyplot as plt

def set_labels():
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1)
plt.title('График функции z1')
set_labels()
plt.show()

z2 = x**2 - y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z2)
plt.title('График функции z2')
set_labels()
plt.show()

z3 = 2*x + 3*y
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z3)
plt.title('График функции z3')
set_labels()
plt.show()

z4 = x**2 + y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z4)
plt.title('График функции z4')
set_labels()
plt.show()

z5 = 2 + 2*x + 2*y - x**2 - y**2
surf = plt.figure()
ax = surf.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z5)
plt.title('График функции z5')
set_labels()
plt.show()