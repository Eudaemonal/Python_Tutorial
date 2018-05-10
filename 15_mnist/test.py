#!/usr/bin/python3
import sys
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data


'''
Useage:
python3 test.py

Image of digit will be shown, then close it to see the testing result on console
'''


# display handwritten digits in test set
def show_image(mnist):
    batch = mnist.test.next_batch(1)
    imvalue = batch[0]
    plotData = imvalue.reshape(28, 28)
    plt.gray() # use this line if you don't want to see it in color
    plt.imshow(plotData)
    plt.show()

    return imvalue


if __name__=="__main__":
    # load the image dataset
    mnist = input_data.read_data_sets('data/mnist', one_hot=True)

    imvalue = show_image(mnist)


    # Define the model (same as when creating the model file)
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)

    init_op = tf.initialize_all_variables()
    saver = tf.train.Saver()
    
    """
    Load the model.ckpt file
    file is stored in the same directory as this python script is started
    Use the model to predict the integer. Integer is returend as list.
    Based on the documentatoin at
    https://www.tensorflow.org/versions/master/how_tos/variables/index.html
    """
    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, "model.ckpt")
   
        prediction=tf.argmax(y,1)
        print(prediction.eval(feed_dict={x: imvalue}, session=sess))

