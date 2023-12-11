import numpy as np
import matplotlib.pyplot as plt

def Y(x):
    return x**np.sin(10*x)

x_values = np.linspace(1, 10, 100)

y_values = Y(x_values)

plt.plot(x_values, y_values, label='Y(x) = x^sin(10x)', color='red', linewidth=2, linestyle='-')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.title('Графік функції Y(x) = x^sin(10x)')
plt.xlabel('x')
plt.ylabel('Y(x)')

plt.legend()

plt.show()
