import numpy as np
from matplotlib import pyplot as plt


def create_surface(z, title):
    surf = plt.figure()
    ax = surf.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z)
    plt.title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

x, y = np.meshgrid(x, y)

z1 = x**0.25 + y**0.25
create_surface(z1, 'График функции z1')

z2 = x**2 - y**2
create_surface(z2, 'График функции z2')

z3 = 2*x + 3*y
create_surface(z3, 'График функции z3')

z4 = x**2 + y**2
create_surface(z4, 'График функции z4')

z5 = 2 + 2*x + 2*y - x**2 - y**2
create_surface(z5, 'График функции z5')