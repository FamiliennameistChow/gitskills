import numpy as np


def normalEqn(X, y):
    theta = np.linalg.inv(X.T@X)@X.T@y
    return theta