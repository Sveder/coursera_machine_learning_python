"""
Done: plots points.

TODO:
1. Make the cost function plot be a bowl instead of the half bowl it is now. - HINT - if that doesn't work, revert to
one variable like the example, and debug it until I get a U shape.
2. Make a visual linear regression "video" or whatever frame by frame matplot can do.
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

import week1_manual


def plot(data_set):
    plt.scatter(data_set.keys(), data_set.values())
    plt.show()


def plot_cost_function(data_set):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(-2, 6, 0.25)
    Y = np.arange(-2, 6, 0.25)

    X, Y = np.meshgrid(X, Y)

    Z = np.array([week1_manual.cost_function(data_set, week1_manual.hypo_function(x, y)) for x, y in zip(np.ravel(X), np.ravel(Y))])

    print X

    print "-------"

    print Z
    # for i in X:
    #     print "i=", i
    #     for j in Y:
    #         print "j=", i
    #         for k in Z:
    #             print "k=", k
    #             raw_input()

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
             linewidth=0, antialiased=False)

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


plot_cost_function(week1_manual.generate_perfect_data(2, 1, range(20)))

#