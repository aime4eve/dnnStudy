# import numpy as np
import math
import random


class DNN:

    def __init__(self, n_inputs, n_hidden, n_outputs):
        self.network = list()  # 深度神经网络定义
        # 第1个隐含层初始化
        hidden_layer_1 = [
            {'weights': [random.random() for i in range(n_inputs + 1)], 'output': 0.0, 'delta': 0.0} for i in
            range(n_hidden)
        ]
        self.network.append(hidden_layer_1)

        # 第n-1个隐含层初始化
        if n_hidden > 1:
            for k in range(n_hidden - 1):
                hidden_layer_n = [
                    {'weights': [random.random() for i in range(n_hidden + 1)], 'output': 0.0, 'delta': 0.0} for i in
                    range(n_hidden)
                ]
                self.network.append(hidden_layer_n)

        # 输出层初始化
        output_layer = [
            {'weights': [random.random() for i in range(n_hidden + 1)], 'output': 0.0, 'delta': 0.0} for i in
            range(n_outputs)
        ]
        self.network.append(output_layer)

    def show_network(self):
        k = 0
        for layer in self.network:
            print(f'layer:{k}')
            k += 1
            for i in range(len(layer)):
                print(layer[i])

    def net_input(self, weights, inputs):  # weights比inputs多一个数，代表w0
        total_input = weights[-1]
        for i in range(len(weights) - 1):
            total_input += weights[i] * inputs[i]

        # total_input = weights[:-2] * inputs[:] + weights[-1]
        return total_input

    def activation(self, total_input):
        return 1.0 / (1.0 + math.exp(-total_input))  # sigmoid

    def forward_propagate(self, row):
        inputs = row
        for layer in self.network:
            outputs = []
            for neuron in layer:
                total_input = self.net_input(neuron['weights'], inputs)
                neuron['output'] = self.activation(total_input)
                outputs.append(neuron['output'])
            inputs = outputs
        return inputs

    def cost_function(self, expected, outputs):
        n = len(expected)
        total_error = 0.0
        for i in range(n):
            total_error += (expected[i] - outputs[i]) ** 2
        return total_error

    def transfer_derivative(self, output):
        return output * (1.0 - output)  # sigmoid函数求导

    def backward_propagate(self, expected):  # network是list数据类型，expected包含结果的真实分类
        for i in reversed(range(len(self.network))):
            layer = self.network[i]
            errors = list()

            if i == len(self.network) - 1:  # 判断是否为输出层
                for j in range(len(layer)):
                    neuron = layer[j]
                    error = -2 * (expected[j] - neuron['output'])
                    errors.append(error)
                    pass
            else:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in self.network[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
                    pass

            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * self.transfer_derivative(neuron['output'])

    def update_weights(self, row, learning_rate):
        for i in range(len(self.network)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in self.network[i - 1]]
            for neuron in self.network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] -= learning_rate * neuron['delta'] * inputs[j]
                neuron['weights'][-1] -= learning_rate * neuron['delta']

    def train_network(self, training_data, learning_rate, n_epoch, n_outputs):
        for epoch in range(n_epoch):
            sum_error = 0
            for row in training_data:
                outputs = self.forward_propagate(row)
                expected = [0 for i in range(n_outputs)]
                expected[row[-1]] = 1
                sum_error += self.cost_function(expected, outputs)
                self.backward_propagate(expected)
                self.update_weights(row, learning_rate)
            print('>epoch:%d,learning rate: %.3f, error: %.3f' % (epoch, learning_rate, sum_error))

    def predict(self, row):
        outputs = self.forward_propagate(row)
        return outputs.index(max(outputs))
#
#
# if __name__ == '__main__':
#     dataset = [
#         [2, 4, 8, 0],
#         [3, 4, 10, 0],
#         [1, 1, 3, 0],
#         [3, 3, 0, 0],
#         [7, 2, -2, 1],
#         [5, 2, -4, 1],
#         [6, 1, -5, 1]
#     ]
#
#     test_data = [
#         [1, 2,  3, 0],
#         [8, -1, 5, 1],
#         [7, 3, -2,1],
#     ]
#
#     n_inputs = len(dataset[0]) - 1
#     n_hidden = 3
#     n_outputs = 2
#
#     network = initialize_network(n_inputs, n_hidden, n_outputs)
#
#     k = 0
#     for layer in network:
#         print(f'layer:{k}')
#         k += 1
#         for i in range(len(layer)):
#             print(layer[i])
#
#
#
#     train_network(network, training_data=dataset, learning_rate=0.5, n_epoch= 20, n_outputs=n_outputs)
#
#     k = 0
#     for layer in network:
#         print(f'layer:{k}')
#         k += 1
#         for i in range(len(layer)):
#             print(layer[i])
#
#     for row in test_data:
#         result = predict(network,row)
#         print('expected: %d, predicted: %d' % (row[-1], result))
