import csv

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale, StandardScaler
from sklearn.utils import shuffle

data_set_path = 'sample/K1135_20_allflow_version3.csv'
data = []
i = 1
with open(data_set_path, 'r') as f:
    for line in f:
        sample = line.strip().split(',')
        if len(sample) == 15 and i >= 577:
            # time, flow,风向,天气
            data.append([sample[0],float(sample[1]), float(sample[2]), float(sample[3]),
                         float(sample[4]), float(sample[5]), float(sample[6]),
                         float(sample[7]), float(sample[8]), float(sample[9]),
                         float(sample[10]), float(sample[11]), float(sample[12]),
                         ])
        i += 1
data = np.array(data)


with open("data.csv", "w+") as f:
    f_csv = csv.writer(f, )
    f_csv.writerows(data)


# filename_queue = tf.train.string_input_producer(['test.csv'])
#
# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
#
# record_defaults = [[0.0], [0.0], [0.0]]
# col1, col2, col3 = tf.decode_csv(value, record_defaults=record_defaults)
# example = tf.stack([col2, col3], 0)
# label = tf.stack([col1], 0)
#
# with tf.Session() as sess:
#     # Start populating the filename queue.
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#     for i in range(26496):
#         x, y = sess.run((example, label))
#         print(example)
#         plt.plot(i % 288, y,  'r')
#         if i % 287 == 0 and i != 0:
#             plt.savefig('/home/fate/Desktop/Traffic-flow/day%d.png' % (i/287))
#             plt.close()
#             plt.figure()
#     coord.request_stop()
#     coord.join(threads)


# def read_from_csv(filename_queue):
#     reader = tf.TextLineReader(skip_header_lines=1)
#     key, value = reader.read(filename_queue)
#     record_defaults = [[0.0], [0.0]]
#     example, label = tf.decode_csv(value, record_defaults=record_defaults)
#     return example, label
#
#
# def input_pipeline(file_name, batch_size, num_epochs=None):
#     file_name_queue = tf.train.string_input_producer([file_name], num_epochs=num_epochs, shuffle=True)
#     example, label = read_from_csv(file_name_queue)
#     min_after_dequeue = 100
#     capacity = min_after_dequeue + 3 * batch_size
#     example_batch, label_batch = tf.train.shuffle_batch(
#         [example, label], batch_size=batch_size, capacity=capacity,
#         min_after_dequeue=min_after_dequeue)
#     return example_batch, label_batch
#
#
# file_n = 'k1135_20_11test.csv'
# examples, labels = input_pipeline(file_n, 20)
#
#
# with tf.Session() as sess:
#     opt = tf.global_variables_initializer()
#     sess.run(opt)
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#     try:
#         while not coord.should_stop():
#             example_batch, label_batch = sess.run([examples, labels])
#             print(example_batch)
#     except tf.errors.OutOfRangeError:
#         print('Done training, epoch reached')
#     finally:
#         coord.request_stop()
#     coord.join(threads)







# from sklearn import preprocessing
# import numpy as np
#
# dataset = np.loadtxt("K1135_20_test.csv", delimiter=",")
# X = dataset[:, 4]
# Y = dataset[:, 5]
# print(X)
# print(Y)
# #Z = dataset[:, 4]
# print(dataset.shape)
# print(X.size)
# print(Y.size)
# standardize_X = preprocessing.scale(X.reshape(-1, 1))
# normalized_X = preprocessing.normalize(X.reshape(-1, 1))
# normalized_Y = preprocessing.scale(Y.reshape(-1, 1))
# print(standardize_X.shape)
# print(normalized_X.shape)
# print(normalized_Y.shape)
# #
# # print(normalized_X[1,1])
# # print(standardize_X)
# # print(normalized_X)
# # print(dataset.shape)
# # print(dataset.size)
# plt.figure(1)
# plt.title("sum of car")
# ax1 = plt.subplot(2, 2, 1)
# ax2 = plt.subplot(2, 2, 2)
# ax3 = plt.subplot(2, 2, 3)
# ax4 = plt.subplot(2, 2, 4)
# for i in range(288):
#     plt.plot(i, X[i], 'r-+')
#     plt.sca(ax1)
#     ax1.set_title("first day")
#     plt.plot(i+288, X[i+288], 'r-+')
#     plt.sca(ax2)
#     ax2.set_title("second day")
#     plt.plot(i + 288*2, X[i + 288*2], 'r-+')
#     plt.sca(ax3)
#     ax3.set_title("three")
#     plt.plot(i + 288*3, X[i + 288*3], 'r-+')
#     plt.sca(ax4)
#     ax4.set_title("four")
# plt.show()






