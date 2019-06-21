import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import matplotlib.pyplot as plt
import torchvision

# Hyper Parameters
EPOCH = 3
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = False

train_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),  # (0, 1)
    download=DOWNLOAD_MNIST
)

# print(train_data.train_data.size())
# print(train_data.train_labels.size())
#
# # 显示第一张图
plt.imshow(train_data.data[1].numpy(), cmap='gray')
plt.title('%i' % train_data.targets[1])
plt.show()



# data loader
train_loader = Data.DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# test data
test_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=False
)

# print(test_data.test_data.size(),
#       "\n test label:", test_data.test_labels.size()
#       )

# 选取前2000个数据做测试
# shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
test_x = torch.unsqueeze(test_data.data, dim=1).type(torch.FloatTensor)[:2000]/255
test_y = test_data.targets[:2000]


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

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)  # -> (batch, 32, 7, 7)
        x = x.view(x.size(0), -1)  # (batch, 32*7*7)
        output = self.out(x)
        return output


cnn = CNN()
# print(cnn)

# 生成一个样本供网络前向传播 forward()
example = torch.rand(1, 1, 28, 28)

# 使用 torch.jit.trace 生成 torch.jit.ScriptModule 来跟踪
traced_script_module = torch.jit.trace(cnn, example)

optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
loss_func = nn.CrossEntropyLoss()

for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):
        # output = cnn(b_x)
        output = traced_script_module(b_x)
        loss = loss_func(output, b_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0:
            test_output = cnn(test_x)
            pred_y = torch.max(test_output, 1)[1].data.numpy()
            accuracy = float((pred_y == test_y.data.numpy()).astype(int).sum()) / float(test_y.size(0))
            print(
                'Epoch:', epoch, "|train loss:", loss.data.numpy(), "| test accuracy: %.2f" % accuracy
            )


# torch.save(cnn.state_dict(), './mnist_model_param.pt')
# torch.save(cnn, 'mnist_model.pt')
traced_script_module.save('mnist_model.pt')

test_output = cnn(test_x[:10])
pred_y = torch.max(test_output, 1)[1].data.numpy().squeeze()
print(pred_y, 'prediction number')
print(test_y[:10].numpy(), 'real number')


for i in range(10):
    plt.imshow(train_data.data[i].numpy(), cmap='gray')
    plt.title('%i' % train_data.targets[i])
    plt.show()
