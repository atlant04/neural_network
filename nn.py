import math

from matrix import Matrix


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def dsigmoid(x):
    dVal = sigmoid(x)
    return dVal * (1 - dVal)


class NN:

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(hidden_nodes, input_nodes)
        self.weights_ho = Matrix(output_nodes, hidden_nodes)

        self.weights_ih.randomize(start=-1, end=1)
        self.weights_ho.randomize(start=-1, end=1)

        self.lr = 0.01

    def predict(self, input_matrix):
        output = self.weights_ih * input_matrix
        output.map(sigmoid)
        output = self.weights_ho * output
        output.map(sigmoid)
        return output

    def train(self, input_matrix, actual_matrix):
        predicted = self.predict(input_matrix)
        error = (actual - predicted)**2
        error_ho = actual - predicted
        input_ho = self.weights_ih * input_matrix
        input_ho.map(sigmoid)
        deltas_ho = error_ho * (self.weights_ho * input_ho).map(dsigmoid) * self.lr
        deltas_ho = Matrix.transpose(self.weights_ho) * deltas_ho
        print(self.weights_ho)
        print(deltas_ho)
        # self.weights_ho -= deltas_ho
        return Matrix.transpose(self.weights_ho)

nn = NN(3, 2, 1)

inputs = Matrix.from_array([1, 2, 3])
actual = Matrix.from_array([4])

print(nn.train(inputs, actual))


