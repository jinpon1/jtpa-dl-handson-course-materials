# learn any logic operations
#
# now we are predicting class with softmax
#

from __future__ import print_function

import numpy as np
import tensorflow as tf

learning_rate = 0.01
log_step = 100
end_step = 20000
hidden_nodes = 4  # 3 or more is needed

input_x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], np.float)
# input_y = np.array([[1, 0],[0, 1],[0, 1],[0, 1]], np.float)  # or
# input_y = np.array([[1, 0],[1, 0],[1, 0],[0, 1]], np.float)  # and
input_y = np.array([[1, 0], [0, 1], [0, 1], [1, 0]], np.float)  # xor


# Placeholders

x = tf.placeholder("float", [None, 2])
y_ = tf.placeholder("float", [None, 2])


# Variables and Graph

w1 = tf.Variable(tf.random_normal([2, hidden_nodes], stddev=0.5))
b = tf.Variable(tf.zeros([hidden_nodes]))
h = tf.tanh(tf.matmul(x, w1) + b)

w2 = tf.Variable(tf.random_normal([hidden_nodes, 2], stddev=0.5))
y = tf.nn.softmax(tf.matmul(h, w2))


# Loss Function

loss = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())

	for step in range(end_step):

		if step % log_step == 0:
			loss_str = sess.run(loss, feed_dict={x: input_x, y_: input_y})
			print ('Step:%04d loss:%s'% (step, str(loss_str)))

		sess.run(train_step, feed_dict={x: input_x, y_: input_y})

	# when finished, let's see the weights and biases
	print ("w1=", w1.eval())
	print ("w2=", w2.eval())
	print ("y=", sess.run(y, feed_dict={x: input_x, y_: input_y}))

