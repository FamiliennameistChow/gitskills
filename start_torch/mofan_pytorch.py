import torch
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F
import matplotlib.pyplot as plt


# np_data = np.arange(6).reshape(2, 3)
# torch_data = torch.from_numpy(np_data)
# tensor2np = torch_data.numpy()
# print(
#     "np_data:\n", np_data,
#     "\ntorch_data:\n", torch_data,
#     "\ntensor2np:\n", tensor2np,
# )

# # abs
# data = [-1, -2, 2, 1]
# tensor = torch.FloatTensor(data)
# print(tensor)
# print(
#     "\nabs",
#     "\nnumpy:", np.sin(data),
#     "\ntorch:", np.sin(tensor),
# )

# # matrix
# data = [[1,2], [3,4]]
# tensor = torch.FloatTensor(data)
# print(
#     "\nnumpy:", np.matmul(data, data),
#     "\ntorch:", torch.mm(tensor, tensor),
# )

# # ****variable****
# tensor = torch.FloatTensor([[1,2],[3,4]])
# variable = Variable(tensor, requires_grad=True)
# t_out = torch.mean(tensor*tensor)
# v_out = torch.mean(variable*variable)
# print(
#     tensor,
#     "\nvariable:", variable,
#     "\nt_out:", t_out,
#     "\nv_out:", v_out
# )
#
# v_out.backward()
# # v_out = 1/4 *sum(variable*variable)
# # d(v_out)/d(variable) = 1/4 *2*variable = variable/2
# print(variable)
# print(variable.grad)
# print(variable.data)
# print(variable.data.numpy())


# ***Activation Function****
x = torch.linspace(-5, 5, 200, requires_grad=True)
x_np = x.data.numpy()
print(x)
print(x_np)

y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()

plt.figure(1, figsize=(8, 6))

plt.subplot(221)
plt.plot(x_np, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x_np, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x_np, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x_np, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()
