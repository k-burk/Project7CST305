from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def runlorenz():

    # lorenz function to return the next value
    def lorenz(x, y, z, s1, r1, b1):
        '''
        Given:
           x, y, z: a point of interest in three dimensional space
           s, r, b: parameters defining the lorenz attractor
        Returns:
           x_dot, y_dot, z_dot: values of the lorenz attractor's partial
               derivatives at the point x, y, z
        '''
        x_dot = s1 * (y - x)
        y_dot = x * (r1 - z) - y
        z_dot = x * y - b1 * z
        return x_dot, y_dot, z_dot

    dt = 0.01

    # initializing empty values
    # for x, y and z coordinates
    xs, ys, zs = [], [], []

    # Set initial values in kilobytes
    # inital values were gotten from project 5
    xs.append(11.8)
    ys.append(4.4)
    zs.append(2.4)

    # animation function that gets each point to add to the graph
    def animate(i):
        # call lorenz function to calculate values
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], s, r, b)

        xs.append((xs[i] + (x_dot * dt)))
        ys.append((ys[i] + (y_dot * dt)))
        zs.append((zs[i] + (z_dot * dt)))
        print(xs, ys, zs)
        plt.cla()
        plt.plot(xs, ys, zs)

    # plotting graph
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # getting user input
    s = float(input("s value: "))
    r = float(input("r value: "))
    b = float(input("b value: "))

    # calling the animation function
    showAnimation = FuncAnimation(fig, animate, interval=0, blit=False)

    plt.show()
