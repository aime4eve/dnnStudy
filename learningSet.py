import random
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

class learningSet:
    def __init__(self):
        self.training_data = []
        self.test_data = []
        pass

    def create_training_data(self, count=90):
        for i in range(count-1):
            style = random.randint(-1,1)
            x = random.randint(-count,count)
            if style == -1:
                bias = -500
            elif style == 0:
                bias = 500
            else:
                bias = 0

            y = self.my_fuction(x, style) + style * bias
            self.training_data.append([x, y, style])
        pass

    def create_test_data(self, count=10):
        for i in range(count-1):
            b = random.randint(-1,1)
            x = random.randint(-100,100)
            y = self.my_fuction(x) + b * random.randint(-100,100)
            self.test_data.append([x, y, b])
        pass

    def my_fuction(self, x, style):
        if style == -1:
            return (100 ** 2 - x ** 2) ** 0.5
        elif style == 0:
            return 100 * x + 50
        else:
            return x ** 2

    def show_dataset(self, set):

        if set == 'training':
            dataset = self.training_data
        else:
            dataset = self.test_data

        for i in range(len(dataset)):

            x = dataset[i][0]
            y = dataset[i][1]
            b = dataset[i][2]
            print(f'[x={x}, y={y}, b={b}]')
            if b == -1:
                style = 'ro'
            elif b == 0:
                style = 'g^'
            elif b == 1:
                style = 'b+'
            else:
                style = 'k*'

            plt.plot(x, y, style)
            plt.pause(0.1)