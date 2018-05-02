#!/usr/bin/python3
import sys
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data


'''
Tensorflow MNIST, handwritten digit recognition

Requires tensroflow installed
https://www.tensorflow.org/install/


Useage:
python3 train.py

Network model will be saved, it can be used for testing

'''


if __name__=="__main__":
    learning_rate = 0.5
    
    # load the image dataset
    mnist = input_data.read_data_sets('data/mnist', one_hot=True)
    
    # each image has shape 28x28, flatten to an array of 1x784
    x = tf.placeholder(dtype=tf.float32, shape=[None, 784],name="image_input")

    # each image corresponds to digit 0-9, result in an array of 1x10
    y = tf.placeholder(dtype=tf.float32, shape=[None, 10],name="image_target_onehot")

    # create a simple one layer network
    W = tf.Variable(tf.zeros([784 , 10]))
    b = tf.Variable(tf.zeros([10]))

    y = tf.nn.softmax(tf.matmul(x, W) + b)

    # a new placeholder to input the correct answers
    y_ = tf.placeholder(tf.float32, [None, 10])

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
    
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
    
    saver = tf.train.Saver()
    # Get started
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    for _ in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))    
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) 


    # save the model
    save_path = saver.save(sess, "./model.ckpt")
    
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    
    # Clean up
    sess.close()
