import numpy as np
from matplotlib import pyplot as plt

def plotter(f):
    def wrapper(*args, **kwargs):
        x = np.linspace(0,50,100)
        fig = plt.figure(figsize=(14,7))
        plt.suptitle('A nice plot', fontsize=18)
        plt.title('f(x)', fontsize=10, fontstyle='italic')
        plt.subplots_adjust(top = 0.8)
        plt.ylabel('y')
        plt.xlabel('x')
        plt.plot(x,f(x),color='cornflowerblue')
        ax = plt.axes()
        ax.set_facecolor('lightsteelblue')
        plt.legend(["f(x)"], loc='upper right',framealpha=1, frameon=True, fancybox=True,shadow=True)
        plt.show()
    return wrapper


@plotter
def f(x):
    return np.cos(x)*np.exp(-0.1*x)

if __name__ == '__main__':
    f()
