# solving linear equation with two unknowns
#
# please note matmul() and mul() is different
# requires numpy

from __future__ import print_function

import numpy as np
import tensorflow as tf

print ("numpy version: %s" % np.__version__)
print ("tensorflow version: %s" % tf.__version__)


train_x = np.array([[3., 1.], [2., 2.]])
train_y = np.array([[560.], [640]])

sess = tf.Session()


# Placeholders

x = tf.placeholder(tf.float32, shape=(None, 2), name="x")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y")


# Variables and Graph

a = tf.Variable(tf.zeros((2, 1)), name="a")
y = tf.matmul(x, a)


# Loss Function

loss = tf.reduce_mean(tf.square(y_ - y))


# Train the Model

train_step = tf.train.GradientDescentOptimizer(0.02).minimize(loss)

sess.run(tf.global_variables_initializer())

for i in range(1000):
  _, l, a_ = sess.run([train_step, loss, a], feed_dict={x: train_x, y_: train_y})
  print("step=%3d, apple=%6.2f, banana=%6.2f, loss=%.2f" % (i + 1, a_[0], a_[1], l))
