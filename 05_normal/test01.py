#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

'''
require matplotlib and numpy to run
install using pip3

'''

if __name__=="__main__":
    mu, sigma = 0, 0.1 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000) # generate 1000 normal random number
    
    # plot histogram
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
             linewidth=2, color='r')
    plt.show()
