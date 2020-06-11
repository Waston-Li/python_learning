import tensorflow as tf

print(tf.__version__)
tf.compat.v1.disable_eager_execution() #使tensor2.0版本兼容1.0的sess
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
