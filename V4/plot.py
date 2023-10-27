import matplotlib.pyplot as plt
import numpy as np
lst = [[0,3.50], [1,2.97],[2,2.62],[3,7.90],[4,6.92],[5,7.24],[6,8.98]]
lst2 = []
lst3 = []
for i in lst:
    lst2.append(i[0])
    lst3.append(i[1])
print(lst2)
m, b = np.polyfit(lst2, lst3, 1)
def plot_slope_intercept(slope, intercept):
    x = np.linspace(-10, 10, 100)
    y = slope * x + intercept
    plt.plot(x, y)
plot_slope_intercept(m, b)
plt.scatter(x=lst2, y=lst3)
plt.xlim(0)
plt.show()