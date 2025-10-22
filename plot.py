import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 30, 45) # задаем диапазон значений x
y = x**3 + 1 # вычисляем значения y
plt.plot(x, y) # строим график
plt.show() # отображаем график
