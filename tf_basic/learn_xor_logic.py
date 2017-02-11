# learn "xor" operations
#
# w1 can be [[1, -1] [-1, 1]] , and w2 can be [1, 1] with relu, but ...
#
from __future__ import print_function

import numpy as np
import tensorflow as tf

learning_rate = 0.01
log_step = 100
end_step = 20000

input_x = np.array([[0., 0.], [1., 0.], [0., 1.], [1., 1.]], np.float)
input_y = np.array([[0.], [1.], [1.], [0.]], np.float)


# Placeholders

x = tf.placeholder("float", [None, 2])
y_ = tf.placeholder("float", [None, 1])


# Variables and Graph

w1 = tf.Variable(tf.random_uniform([2, 2], -1.0, 1.0))
h = tf.tanh(tf.matmul(x, w1))

w2 = tf.Variable(tf.random_uniform([2, 1], -1.0, 1.0))
y = tf.tanh(tf.matmul(h, w2))


# Loss Function

loss = tf.reduce_mean(tf.square(y - y_))


# Train the Model

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

