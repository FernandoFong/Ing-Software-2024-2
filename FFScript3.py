import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    x = ["Graphing", "Strings", "Vs numbers"]
    y = np.array([[1, 2], [3, 4], [5, 6]])
    plt.plot(x, y)
    plt.show()
