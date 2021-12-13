import random
import numpy as np
import matplotlib.pyplot as plt

def runc():
    x = np.linspace(0, 99, 100)  # gives 0-100 for plots
    k = (random.random()) * 10  # giving a random k value to show that no matter the k value the graphs will be the same shape

    # utilization
    p_old = []
    p_new = []
    wait_time1 = []
    wait_time2 = []
    # l and mu values are from part 2a
    l = 125
    mu = 500
    for i in range(100):
        l = l + (i / 10)  # increase job/sec by .1
        mu = mu + (i / 10)
        p_old.append(l / mu)
        p_new.append((k * l) / (k * mu))
        wait_time1.append((1 / mu) / (1 - p_new[i]))
        wait_time2.append((1 / mu) / (1 - p_old[i]))

    # graphing to compare old and new values
    plt.plot(p_old, wait_time2, label="p old")
    plt.plot(p_new, wait_time1, label="p new", linestyle="--")
    plt.title("Utilization")
    plt.show()

    # throughput
    l = 125
    Xold = []
    Xnew = []
    for i in range(100):
        l = l + i  # increase job/sec by one
        Xold.append(l)
        Xnew.append(k * l)
    # graphing to compare old and new values
    plt.plot(Xnew, x, label="Xnew")
    plt.plot(Xold, x, label="Xold", linestyle="--")
    plt.title("Throughput")
    plt.show()

    # mean number in system
    l = 125
    mu = 500
    ENold = []
    ENnew = []
    for i in range(100):
        ENold.append(p_old[i] / (1 - p_old[i]))
        ENnew.append(p_new[i] / (1 - p_new[i]))
    # graphing to compare old and new values
    plt.plot(ENnew, x, label="E[N]new")
    plt.plot(ENold, x, label="E[N]old", linestyle="--")
    plt.title("mean number in system")
    plt.show()

    # mean time in system
    l = 125
    mu = 500
    ETold = []
    ETnew = []
    for i in range(100):
        l = l + (i * 100)  # increase job/sec by 100
        mu = mu + (i * 100)
        ETold.append(1 / (mu - l))
        ETnew.append(1 / (k * (mu - l)))
    # graphing to compare old and new values
    plt.plot(ETnew, x, label="E[T]new")
    plt.plot(ETold, x, label="E[T]old", linestyle="--")
    plt.title("mean time in system")
    plt.show()
