from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.utils import plot_model
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


# 适配intel cpu
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    model = Sequential([
        Dense(4, input_shape=(2,)),
        Activation('sigmoid'),
        Dense(1),
        Activation('sigmoid')
    ])

    plot_model(model, to_file='training_model.png', show_shapes=True)
    model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

    training_num = 100
    training_data = np.random.random((training_num, 2))
    labels = [(1 if data[0] < data[1] else 0) for data in training_data]

    # print(training_data)
    test_num = 100
    test_data = np.random.random((test_num, 2))
    expected = [(1 if data[0] < data[1] else 0) for data in test_data]

    epoch_x = []
    acc_y = []

    for nn in range(1, 10):
        print(f'-第{nn}次训练-------------------------------------------------------------')
        model.fit(training_data, np.array(labels), epochs=20 * nn, batch_size=32, verbose=0)
        error = 0
        for i in range(0, test_num):
            data = test_data[i].reshape(1, 2)
            pred = 0 if model.predict(data) < 0.5 else 1

            if (pred != expected[i]):
                error += 1
        acc = 1.0 - error / test_num

        epoch_x.append(20*nn)
        acc_y.append(acc)
        plt.plot(20*nn, acc, 'r.-')
        plt.pause(0.1)

        print(f'total erros:{error}, acc:{acc}')
        print('------------------------------------------------------------------\n')

    print(epoch_x)
    print(acc_y)

    plt.plot(epoch_x,acc_y,'go-')

    plt.pause(5)

