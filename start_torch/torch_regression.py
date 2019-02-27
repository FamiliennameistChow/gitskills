import torch
import matplotlib.pyplot as plt
from torch.autograd import Variable
import torch.nn.functional as F

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2*torch.rand(x.size())
print(x, y)

x, y = Variable(x), Variable(y)


# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

class Net(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        # 正向传播输入值, 神经网络分析出输出值
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x


net = Net(1, 10, 1)
print(net)

plt.ion()
plt.show()

optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
#
loss_func = torch.nn.MSELoss()  # 预测值和真实值的误差计算公式 (均方差)

for t in range(100):
    predition = net(x)
    loss = loss_func(predition, y)
    optimizer.zero_grad()  # 是把梯度置零，也就是把loss关于weight的导数变成0.
    loss.backward()
    optimizer.step()
    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), predition.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, "LOSS=%.4f" % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)
    plt.ioff()
    plt.show()


