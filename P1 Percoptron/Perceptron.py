import random

class Perceptron:

    def __init__(self, bias, weight):
        self.weights = weight
        self.bias = bias

        def feed_forward(self):
            global som
            som = 0
            for x in range(0, len(self.weights)):
                som += self.weights[x] * self.inputs[x]
            return som # placeholder

        def activate(self):
            if ((som*weight) + self.bias) < 0:
                return 0
            else:
                return 1

        def __str__(self):
            return ('test')



Perceptron(0, 0)