# -*- coding: utf-8 -*-
import tensorflow as tf

# 모든 것이 연산(operation)이다.
a = tf.constant(2)
b = tf.constant(5)
c = a+b

print tf.Session().run( c )

# Placeholder

# 데이터 타입만 정의하고...
a = tf.placeholder( tf.int16 )
b = tf.placeholder( tf.int16 )

# 모델을 정의하고..
add = tf.add(a, b)
mul = tf.mul(a, b)

# 실행 시점에 데이터를 입력
with tf.Session() as sess:
    print "addition : %i"%sess.run(add, feed_dict={a:2,b:3})
    print "multiplication : %i"%sess.run(add, feed_dict={a:2,b:3})
