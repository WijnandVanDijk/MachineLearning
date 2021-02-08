import random

class Perceptron:

    def __init__(self):
        self.weights = []
        self.bias = None
        self.inputs = []

        for i in range(4):
            self.inputs.append(random.randint(0, 1))

        for i in range(4):
            self.weights.append(random.random())

        def feed_forward(self):
            global som
            som = 0
            for x in range(0, len(self.weights)):
                som += self.weights[x] * self.inputs[x]
            return som # placeholder

        feed_forward(self)

        if som > 0:
            return 1
        else:
            return -1

Perceptron()