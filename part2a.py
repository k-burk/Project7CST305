import numpy as np
import matplotlib.pyplot as plt
def runa():
    # Arrival Rate
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # Service Duration
    sd = [2.22, 1.76, 2.13, 0.14, 0.76, 0.7, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27]
    # Service start time
    sst = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
    # Exit time
    et = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]
    # Time In Queue
    tq = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]
    # Number in System
    ns = [3, 3, 5, 4, 4, 3, 3, 2, 1, 3, 2, 2, 2, 1, 1]
    # Number in Queue
    nq = [2, 2, 4, 3, 3, 2, 2, 1, 0, 2, 1, 1, 1, 0, 0]

    fig, ax = plt.subplots(2, 3, constrained_layout=True)
    # arrival time vs start time
    ax[0,0].plot(ar, sst)
    ax[0,0].set_title("arrival time vs start time")
    # the customer arrival time as a function of exit time
    ax[0,1].plot(ar, et)
    ax[0,1].set_title("arrival time vs exit time")
    # the customer arrival time as a function of time in queue
    #plt.subplot(2, 3, 3)
    ax[0,2].plot(ar, tq)
    ax[0,2].set_title("arrival time vs time in queue")
    # the customer arrival time as a function of the number of customers in system
    #plt.subplot(2, 3, 4)
    ax[1,0].plot(ar, ns)
    ax[1,0].set_title("arrival time vs # in system")
    # the customer arrival time as a function of number of customers in queue.
    ax[1,1].plot(ar, nq)
    ax[1,1].set_title("arrival time vs # in queue")

    plt.show()
