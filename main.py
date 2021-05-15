import myDNN
import learningSet
import matplotlib.pyplot as plt

if __name__ == '__main__':

    ds = learningSet.learningSet()
    ds.create_training_data()
    ds.show_dataset('training')

    dataset = [
        [2, 4,  0],
        [3, 4,  0],
        [1, 1,  0],
        [3, 3,  0],
        [7, 2,  1],
        [5, 2,  1],
        [6, 1,  1]
    ]

    test_data = [
        [1, 2,  0],
        [8, -1,  1],
        [7, 3,  1],
    ]

    n_inputs = len(dataset[0]) - 1
    n_hidden = 3
    n_outputs = 2

    dnn = myDNN.DNN(n_inputs, n_hidden, n_outputs)

    # dnn.show_network()
    dnn.train_network(training_data=dataset, learning_rate=0.5, n_epoch=20, n_outputs=n_outputs)
    # dnn.show_network()

    for row in test_data:
        result = dnn.predict(row)
        print('expected: %d, predicted: %d' % (row[-1], result))

    plt.pause(10)