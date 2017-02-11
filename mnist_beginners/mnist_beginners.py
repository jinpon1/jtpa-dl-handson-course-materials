# tf mnist sample for beginners

from __future__ import print_function

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Placeholders

x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 10])


# Variables

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


# Predicted Class and Loss Function

y = tf.nn.softmax(tf.matmul(x, W) + b)
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))


# Train the Model

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


# Evaluate the Model

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# Training

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):

  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  if i % 10 == 0:
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

