# -*- coding: utf-8 -*-
import tensorflow as tf


W = tf.Variable(tf.random_uniform([1], -1.0,1.0))
b = tf.Variable(tf.random_uniform([1], -1.0,1.0))


# 방법 1.
x_data = [1,2,3]
y_data = [1.,2.,3.]
hypothesis = W * x_data + b
cost = tf.reduce_mean( tf.square(hypothesis - y_data ))

# 방법 2
X = tf.placeholder( tf.float32 )
Y = tf.placeholder( tf.float32 )
hypothesis = W * X + b
cost = tf.reduce_mean( tf.square(hypothesis - Y ))


a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize( cost )

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run( init )

for step in xrange(2001):
    sess.run( train, feed_dict = { X: x_data, Y : y_data } )
    #if step%20 == 0:
    #    print step, sess.run( cost ), sess.run( W ), sess.run(b)

    # placeholder 를 이용하면 쉽게 테스트를 변경해가며 써볼 수 있다.
    print sess.run( hypothesis, feed_dict = {X:5} )
    print sess.run( hypothesis, feed_dict = {X:2.5} )
