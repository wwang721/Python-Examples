import neuralNetwork.neuralNetwork as nn
import numpy as np

# 类名
class_names = ["1st", "2nd", "3rd", "4th"]  
num_classes = len(class_names)

# 训练数据集合
X = np.array([
    [2, 1],
    [-1, 1],
    [-1, -1],
    [1, -1],
    [-3, -4],
    [-2, 5]
])

# 对应的教师标签
t = np.array([0, 1, 2, 3, 2, 1])

input_dim = X.shape[1]  # 输入参数维度
hidden_dim = 50         # 隐藏层维度

reg = 0.001             # 正则化惩罚项系数
epsilon = 0.001         # 梯度下降学习率

# 初始化
quadrant = nn.Neural_network(reg, epsilon, input_dim, hidden_dim, num_classes)

# 开始训练迭代
quadrant.network_train(10000, X, t)

# 测试数据集合
test = np.array([
    [2, 2],
    [-2, 2],
    [-2, -2],
    [2, -2],
    [10, -2],
    [2, 7]
])

# 测试结果
ans = quadrant.network_test(test)
for k in range(test.shape[0]):
        print(test[k, :], "is in the", class_names[ans[k]], "quadrant.")
