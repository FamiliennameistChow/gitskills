import torch
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt
import torchvision
import torch.nn as nn

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


# # *****************提取****************
# def restore_net():     # 提取整个神经网络
#     net3 = torch.load('net2.pkl')
#     prediction = net3(x)
#
#     # plot result
#     plt.figure()
#     plt.subplot(121)
#     plt.title('Net3')
#     plt.scatter(x.data.numpy(), y.data.numpy())
#     plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
#
#
# def restore_params():    # 提取神经网络的参数，需要建立一个与保存时一致的神经网络模型
#     # 新建net4
#     net4 = torch.nn.Sequential(
#         torch.nn.Linear(1, 10),
#         torch.nn.ReLU(),
#         torch.nn.Linear(10, 1)
#     )
#
#     # 将保存的参数复制到net4中
#     net4.load_state_dict(torch.load('net_params.pkl'))
#     prediction = net4(x)
#
#     # plot net4
#     plt.subplot(122)
#     plt.title('net4')
#     plt.scatter(x.data.numpy(), y.data.numpy())
#     plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
#     plt.show()
#
#
# restore_net()
#
# restore_params()


# 提取模型进行验证
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,  # 输入图片的高度  (1,28,28)
                out_channels=16,  # in_channels * 过滤器的高度 = out_channels
                kernel_size=5,  # 卷积为 5*5
                stride=1,  # 跨度
                padding=2,  # 填充 if stride = 1, padding = (kernel_size -1) / 2
            ),  # -> output(16, 28, 28)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),  # 使用2*2 在空间向下采样, -> (16, 14, 14)
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 5, 1, 2),  # -> (32, 14, 14)
            nn.ReLU(),
            nn.MaxPool2d(2),  # -> (32, 7, 7)
        )
        self.out = nn.Linear(32*7*7, 10)

    @torch.jit.script_method
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)  # -> (batch, 32, 7, 7)
        x = x.view(x.size(0), -1)  # (batch, 32*7*7)
        output = self.out(x)
        return output


cnn = CNN()
# cnn.load_state_dict(torch.load('./mnist_model_param.pt'))


# cnn = torch.load('mnist_model.pt')
# print(cnn)
#
# # test data
# test_data = torchvision.datasets.MNIST(
#     root='./mnist',
#     train=False
# )
#
# test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000]/255
# test_y = test_data.test_labels[:2000]
#
# print(test_x[1].size())
#
# output = cnn(test_x[1])


# test_output = cnn(test_x[:10])
# pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
# print(pred_y, 'prediction number')
# print(test_y[:10].numpy(), 'real number')
#
#
# for i in range(10):
#     plt.imshow(test_data.test_data[i].numpy(), cmap='gray')
#     plt.title('%i' % test_data.test_labels[i])
#     plt.show()

