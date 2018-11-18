import tensorflow as tf
import pandas as pd
import numpy as np

data_set = pd.read_csv('DataSets.csv')

# Still need to understand how to implement.
# Currently we import the csv file, and at the FOR loop
# we put the features into X (and not x) and the observation to Y (and not y)

x = tf.placeholder(tf.int64, [None, 784])
y_ = tf.placeholder(tf.floar32, [None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W)+b)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(5):
    X = data_set.iloc[i, :-2].values
    Y = data_set.iloc[i, 65:].values
    
    sess.run(train_step, feed_dict={x:X, y_: Y})    
    # batch_xs, batch_ys = mnist.train.next_batch(100) #MB-GD
    # sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
