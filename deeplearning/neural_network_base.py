import numpy  as  np

# 1 .标量（0D 张量

x = np.array(12)

print(x)  # -->12

print(x.ndim)  # 维度属性  ->0

# 2.向量（1D 张量）

'''
数字组成的数组叫作向量（vector）或一维张量（1D 张量）。一维张量只有一个轴。下面是
一个 Numpy 向量。
'''

# 加载 Keras 中的 MNIST 数据集
'''
MNIST 数据集预先加载在 Keras 库中，其中包括 4 个 Numpy 数组 

train_images 和 train_labels 组成了训练集（training set），模型将从这些数据中进行
学习。然后在测试集（test set，即 test_images 和 test_labels ）上对模型进行测试。
图像被编码为 Numpy 数组，而标签是数字数组，取值范围为 0~9。图像和标签一一对应
'''

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)  # -->(60000, 28, 28)

print(len(train_labels))  # -->   60000

print(train_labels)  # -->[5 0 4 ... 5 6 8]

