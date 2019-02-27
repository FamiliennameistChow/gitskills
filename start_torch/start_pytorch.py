# from __future__ import print_function
import torch

# x = torch.empty(5, 3)
# x = torch.rand(5, 3)
# x = torch.zeros(5, 3, dtype=torch.long)
# x = torch.tensor([5.5, 3])
# x = x.new_ones(5, 3, dtype=torch.double)
# x = torch.randn_like(x, dtype=torch.float)
# print(x.size())
# y = torch.rand(5, 3)
# print(x + y)
# print(torch.add(x, y))
# result = torch.empty(5, 3)
# torch.add(x, y, out=result)
# print(result)
# y.add_(x)
# print("y:", y)
# print(y[:, 1])

# x = torch.rand(1)
# print(x)
# print(x.item())
# y = torch.randn(5)
# print(y)

# # resize
# x = torch.randn(4, 4)
# y = x.view(16)
# z = x.view(-1, 8)
# print(x.size(), y.size(), z.size())

# # convert tensor to numpy
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)
# a.add_(1)
# print(a)
# print(b)

# # # convert numpy to tensor
# import numpy as np
# a = np.ones(5)
# b = torch.from_numpy(a)
# # np.add(a, 1, out=a)
# # print(a)
# # print(b)
#
# if torch.cuda.is_available():
#     device = torch.device('cuda')
#     y = torch.ones_like(a, device=device)
#     print("y:", y)

# ***** 2nd chapter******
x = torch.ones(2, 2, requires_grad=True)
print(x)
y = x + 2
print(y)
z = y*y*3
out = z.mean()
print(z, out)
out.backward()
print(x.grad)


