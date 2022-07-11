'''
@author king_xiong
@date 2022-03-07 15:03
'''
import tensorflow as tf


if __name__ == '__main__':
    t1=tf.constant(21)
    # 查看t1的值
    print(t1.numpy())
    t2=tf.constant(20)
    print(t1+t2)