import numpy as np

from LSTM.lstm import My_LSTM


def load_data(filename='data/data.csv'):
    data = []
    i = 1
    with open(filename, 'r') as f:
        for line in f:
            sample = line.strip().split(',')
            if len(sample) == 15 and i >= 577:
                data.append([float(sample[1]), float(sample[2]), float(sample[3]),
                            float(sample[4]), float(sample[5]), float(sample[6]),
                            float(sample[7]), float(sample[8]), float(sample[9]),
                            float(sample[10]), float(sample[11]), float(sample[12]),
                            float(sample[13]), float(sample[14])])
            i += 1
    data = np.array(data)
    return data


data = load_data()
lstm = My_LSTM(rnn_unit=10, input_size=11, time_step=20, output_size=3, lr=0.006, data=data)
# lstm.train_lstm()
# lstm.verify()

predict_x = [[259, 253, 274, 258, 242, 223, 252, 250, 251, 234, 185, 203, 51, 33],
             [253, 274, 254, 242, 223, 252, 250, 251, 259, 185, 203, 171, 51, 33],
             [274, 254, 258, 223, 252, 250, 251, 259, 253, 203, 171, 186, 51, 33],
             [254, 258, 231, 252, 250, 251, 259, 253, 274, 171, 186, 165, 51, 33],
             [258, 231, 252, 250, 251, 259, 253, 274, 254, 186, 165, 214, 51, 33],
             [231, 252, 242, 251, 259, 253, 274, 254, 258, 165, 214, 216, 51, 33],
             [252, 242, 239, 259, 253, 274, 254, 258, 231, 214, 216, 326, 51, 33],
             [242, 239, 203, 253, 274, 254, 258, 231, 252, 216, 326, 254, 51, 33],
             [239, 203, 206, 274, 254, 258, 231, 252, 242, 326, 254, 280, 51, 33],
             [203, 206, 196, 254, 258, 231, 252, 242, 239, 254, 280, 325, 51, 33],
             [206, 196, 212, 258, 231, 252, 242, 239, 203, 280, 325, 218, 51, 33],
             [196, 212, 191, 231, 252, 242, 239, 203, 206, 325, 218, 199, 51, 33],
             [212, 191, 184, 252, 242, 239, 203, 206, 196, 218, 199, 192, 51, 33],
             [191, 184, 161, 242, 239, 203, 206, 196, 212, 199, 192, 176, 51, 33],
             [184, 161, 190, 239, 203, 206, 196, 212, 191, 192, 176, 188, 51, 33],
             [161, 190, 181, 203, 206, 196, 212, 191, 184, 176, 188, 213, 51, 33],
             [190, 181, 178, 206, 196, 212, 191, 184, 161, 188, 213, 198, 51, 33],
             [181, 178, 192, 196, 212, 191, 184, 161, 190, 213, 198, 182, 51, 33],
             [178, 192, 148, 212, 191, 184, 161, 190, 181, 198, 182, 191, 51, 33],
             [192, 148, 173, 191, 184, 161, 190, 181, 178, 182, 191, 187, 51, 33]]
predict_x = np.array(predict_x)

predict_y_lstm = lstm.prediction(predict_x[:, :11])
print(predict_y_lstm)