from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.utils import plot_model
import numpy as np
import tensorflow as tf

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

    print(training_data)


    model.fit(training_data, np.array(labels), epochs=20, batch_size=32)

    test_num = 100
    test_data = np.random.random((test_num, 2))
    expected = [(1 if data[0] < data[1] else 0) for data in test_data]

    error = 0
    for i in range(0, test_num):
        data = test_data[i].reshape(1, 2)
        pred = 0 if model.predict(data) < 0.5 else 1

        if (pred != expected[i]):
            error += 1

    print(f'total erros:{error}, acc:{1.0-error/test_num}')
