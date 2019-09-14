import os
import numpy as np
from timeit import default_timer as timer
import neuralNetwork.neuralNetwork as nn

# 类名
class_names = ["acute", "right", "obtuse"]
num_classes = len(class_names)

# 训练数据集合
X = np.reshape(np.arange(1, 180), [179, 1])

# 对应的教师标签
t = np.arange(179)
for k in range(89):
    t[k]=0
    t[k+90]=2
t[89]=1

input_dim = X.shape[1]  # 输入参数维度
hidden_dim = 50        # 隐藏层维度

reg = 0.001             # 正则化惩罚项系数
epsilon = 0.001         # 梯度下降学习率

# 初始化
quadrant = nn.Neural_network(reg, epsilon, input_dim, hidden_dim, num_classes)

start = timer()
# 判断训练是否已经完成
if os.path.exists("angle_Wb.npz") == True:
    # 直接读取训练后的结果
    print("Loading training results...\n")
    Wb = np.load("angle_Wb.npz")

    quadrant.W1 = Wb["w1"]
    quadrant.W2 = Wb["w2"]
    quadrant.b1 = Wb["b1"]
    quadrant.b2 = Wb["b2"]

else:
    # 开始训练迭代
    quadrant.network_train(10000, X, t)
    # 存储训练结果
    np.savez("angle_Wb", w1=quadrant.W1, w2=quadrant.W2, b1=quadrant.b1, b2=quadrant.b2)

# 测试数据集合
test = np.array([
    [99],
    [120],
    [33],
    [87],
    [90],
    [166]
])

#test = 90 * np.ones([100,1])

# 测试结果
ans = quadrant.network_test(test)
for k in range(test.shape[0]):
        print(test[k, :], "degree is a(n)", class_names[ans[k]], "angle.")

runtime = timer() - start
print("\nRun time:", runtime, "s")
