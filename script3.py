from matplotlib import pyplot as plt

# Una función bien x

def funcion_x(Xs):
    Ys = [(x-3) ** 2 for x in Xs]
    return Ys

if __name__ == '__main__':
    Xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Ys = funcion_x(Xs)
    plt.plot(Xs, Ys)
    plt.show()
