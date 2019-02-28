import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt

#
# # ************网络搭建**************
# # method 1
# class Net(torch.nn.Module):
#     def __init__(self, n_features, n_hidden, n_output):
#         super(Net, self).__init__()
#         self.hidden = torch.nn.Linear(n_features, n_hidden)
#         self.predict = torch.nn.Linear(n_hidden, n_output)
#
#     def forward(self, x):
#         # 正向传播输入值, 神经网络分析出输出值
#         x = F.relu(self.hidden(x))
#         x = self.predict(x)
#         return x
#
#
# net1 = Net(2, 10, 2)
#
# fake data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())  # noisy y data (tensor), shape=(100, 1)

x, y = Variable(x), Variable(y)

# # method 2
# net2 = torch.nn.Sequential(
#     torch.nn.Linear(1, 10),
#     torch.nn.ReLU(),
#     torch.nn.Linear(10, 1),
# )
#
# print(
#     "\nnet1", net1,
#     "\nnet2", net2
# )
#
# optimizer = torch.optim.SGD(net2.parameters(), lr=0.5)
# loss_func = torch.nn.MSELoss()
# # ****************训练***********************
# for t in range(100):
#     prediction = net2(x)
#     loss = loss_func(prediction, y)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()
#
# # ***************保存***********************
# torch.save(net2, 'net2.pkl')  # entire net
# torch.save(net2.state_dict(), 'net_params.pkl')  # parameters


# *****************提取****************
def restore_net():     # 提取整个神经网络
    net3 = torch.load('net2.pkl')
    prediction = net3(x)

    # plot result
    plt.figure()
    plt.subplot(121)
    plt.title('Net3')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)


def restore_params():    # 提取神经网络的参数，需要建立一个与保存时一致的神经网络模型
    # 新建net4
    net4 = torch.nn.Sequential(
        torch.nn.Linear(1, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 1)
    )

    # 将保存的参数复制到net4中
    net4.load_state_dict(torch.load('net_params.pkl'))
    prediction = net4(x)

    # plot net4
    plt.subplot(122)
    plt.title('net4')
    plt.scatter(x.data.numpy(), y.data.numpy())
    plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
    plt.show()


restore_net()

restore_params()

