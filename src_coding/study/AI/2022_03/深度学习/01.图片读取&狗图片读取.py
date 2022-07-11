'''
@author king_xiong
@date 2022-03-11 15:01
'''
import tensorflow as tf
import os


def read_picture():
    """
    读取狗图片案例
    :return:
    """
    # 1、构造文件名队列
    # 构造文件名列表
    filename_list = os.listdir("F:/some_learning_materials/机器学习/Python深度学习之神经网络资料/深度学习day2资料/02-代码/dog")
    # 给文件名加上路径
    file_list = [os.path.join("./dog/", i) for i in filename_list]
    # print("file_list:\n", file_list)
    # print("filename_list:\n", filename_list)
    file_queue = tf.train.string_input_producer(file_list)

    # 2、读取与解码
    # 读取
    reader = tf.WholeFileReader()
    key, value = reader.read(file_queue)
    print("key:\n", key)
    print("value:\n", value)

    # 解码
    image_decoded = tf.image.decode_jpeg(value)
    print("image_decoded:\n", image_decoded)

    # 将图片缩放到同一个大小
    image_resized = tf.image.resize_images(image_decoded, [200, 200])
    print("image_resized_before:\n", image_resized)
    # 更新静态形状
    image_resized.set_shape([200, 200, 3])
    print("image_resized_after:\n", image_resized)


    # 3、批处理队列
    image_batch = tf.train.batch([image_resized], batch_size=100, num_threads=2, capacity=100)
    print("image_batch:\n", image_batch)

    # 开启会话
    with tf.Session() as sess:
        # 开启线程
        # 构造线程协调器
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        # 运行
        filename, sample, image, n_image = sess.run([key, value, image_resized, image_batch])
        print("filename:\n", filename)
        print("sample:\n", sample)
        print("image:\n", image)
        print("n_image:\n", n_image)

        coord.request_stop()
        coord.join(threads)


    return None

if __name__ == "__main__":
    # 代码1：读取狗图片案例
    read_picture()