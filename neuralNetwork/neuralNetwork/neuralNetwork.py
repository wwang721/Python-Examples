import numpy as np

class Neural_network(object):

    def __init__(self, reg, epsilon, input_dim, hidden_dim, num_classes):
        """

        :param reg: 正则化惩罚项系数
        :param epsilon: 梯度下降学习率
        :param input_dim: 输入参数维度
        :param hidden_dim: 隐藏层维度
        :param num_classes: 输出参数维度
        """
        self.loss = 10.0  # Cross Entropy Error 交叉熵损失 初始

        self.reg = reg
        self.epsilon = epsilon

        np.random.seed(1)
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.W2 = np.random.randn(hidden_dim, num_classes)
        self.b1 = np.zeros((1, hidden_dim))
        self.b2 = np.zeros((1, num_classes))

    def affine_forward(self, x, w, b):
        """ 仿射-正向传播 H=X*W+b
        """
        out = None
        N = x.shape[0]
        x_row = x.reshape(N, -1)    # 重置输入参数形状，将每个参数将为1维
        out = np.dot(x_row, w) + b
        cache = (x, w, b)
        return out, cache

    def affine_backward(self, dout, cache):
        """ 仿射-反向传播 
        """
        x, w, b = cache
        dx, dw, db = None, None, None
        dx = np.dot(dout, w.T)
        dx = np.reshape(dx, x.shape)
        x_row = x.reshape(x.shape[0], -1)
        dw = np.dot(x_row.T, dout)
        db = np.sum(dout, axis=0, keepdims=True)
        return dx, dw, db

    def network_forward(self, X):
        """ 神经网络-正向传播 

        :param X: 输入值
        """
        H, self.fc_cache = self.affine_forward(X, self.W1, self.b1)     # 第一层向前传播
        H = np.maximum(0, H)                                            # 激活层--ReLu函数
        self.relu_cache = H                                             # 缓存激活后的结果
        self.Y, self.cachey = self.affine_forward(H, self.W2, self.b2)  # 第二层向前传播

        #Softmax层
        self.probs = np.exp(self.Y - np.max(self.Y, axis=1, keepdims=True)) 
        self.probs /= np.sum(self.probs, axis=1, keepdims=True)         # Softmax算法计算概率

    def network_backward(self, t):
        """ 神经网络-反向传播 

        :param t: 标签值
        """
        # Cross Entropy Error 交叉熵损失
        N = self.Y.shape[0]
        self.loss = -np.sum(np.log(self.probs[np.arange(N), t] + 1e-5)) # 防止对数为无穷

        dx = self.probs.copy()
        dx[np.arange(N), t] -= 1
        dx /= N                                                     # 反向传播到Softmax层前
        dh1, dW2, db2 = self.affine_backward(dx, self.cachey)       # 反向传播到第二层前
        dh1[self.relu_cache <= 0] = 0                               # 反向传播到激活层前
        dX, dW1, db1 = self.affine_backward(dh1, self.fc_cache)     # 反向传播到第一层前

        # 参数更新
        dW2 += self.reg * self.W2
        dW1 += self.reg * self.W1
        self.W2 += -self.epsilon * dW2
        self.b2 += -self.epsilon * db2
        self.W1 += -self.epsilon * dW1
        self.b1 += -self.epsilon * db1

    def network_train(self, num, X, t):
        """ 神经网络-训练和迭代

        :param num: 迭代次数
        :param X: 输入值
        :param t: 标签值
        """
        j = 0
        for i in range(num):
            if i == j * num // 100:
                print(j, "% finished.")
                j += 1
            self.network_forward(X)
            self.network_backward(t)

        print("After training:")
        print("probs:", self.probs[np.arange(X.shape[0]), t])
        print("loss:", self.loss)
        print()

    def network_test(self, X):
        """ 神经网络-测试
        """
        self.network_forward(X)
        return np.argmax(self.probs, axis=1)
