#!/usr/bin/python3
import sys


'''
y = c/b - a/b x

y[i] = (w0, w1)[i] * (x0, x1)[i] + b[i]

'''

class SVMTrainer(object):
    def __init__(self, kernel, c):
        self._kernel = kernel
        self._c = c

    def train(self, X, y):
        lagrange_multipliers = self._compute_multipliers(X, y)
        return self._construct_predictor(X, y, lagrange_multipliers)

    def _gram_matrix(self, X):
        n_samples, n_features = X.shape
        K = np.zeros((n_samples, n_samples))
        for i, x_i in enumerate(X):
            for j, x_j in enumerate(X):
                K[i, j] = self._kernel(x_i, x_j)
        return K


if __name__=="__main__":
    for line in sys.stdin:
        print(line)
