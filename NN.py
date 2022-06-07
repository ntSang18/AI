import numpy as np


class NN():
    def __init__(self, layers):
        self.layers = layers
        self.L = len(layers)
        self.w = [np.random.randn(l2, l1 + 1)
                  for l2, l1 in zip(layers[1:], layers[:-1])]

    def feedforward(self, x):
        z = []
        a = [self.add_bias(x)]
        for l in range(1, self.L):
            z_l = np.dot(self.w[l], a[l-1])
            a_l = self.sigmoid(z_l)
            if l < self.L - 1:
                a_l = self.add_bias(a_l)

            z.append(z_l)
            a.append(a_l)

        return (z, a)

    def backprop(self, x, y):
        w_grad = [np.zeros(W.shape) for W in self.w]
        z, a = self.feedforward(x)
        dz = a[-1] - y
        for _l in range(1, self.L):
            l = -_l
            if l < -1:
                da = self.sigmoid_grad(z[l])
                dz = np.dot(self.w[l+1][:, 1:].transpose(), dz) * da
            w_grad[l] = np.dot(dz, a[l-1].transpose())
        return w_grad

    def add_bias(self, a):
        return np.insert(a, 0, 1, axis=0)

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def sigmoid_grad(self, z):
        s = self.sigmoid(z)
        return s * (1 - s)
