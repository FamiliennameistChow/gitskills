# -*- coding: utf-8 -*-
import torch
import numpy as np
# init
'''
 特别注明：任何可以改变tensor内容的操作都会在方法名后加一个下划线'_'
 例如：x.copy_(y), x.t_(), 这俩都会改变x的值。
'''
input = torch.ones(2, 2, 3, 4)
print(input)
print(input.shape)

# 随机初始化的张量
x = torch.rand(5, 3)
print("x:", x,
      "\nx shape:", x.size())

y = torch.Tensor(5, 3)      # 未初始化的张量
print("y", y)

'''
加法操作
'''
a = torch.ones(2, 2)
b = torch.zeros(2, 2)
# way one:
print(a + b)
# way two:
print(torch.add(a, b))
# way there:
print(b.add_(a))
# way four:
c = torch.Tensor(2,2)
torch.add(a, b, out=c)
print(c)

'''
Numpy桥
'''
a = torch.ones(5)
b = a.numpy()     # tensor转换为array
print("numpy:", b,
      "\nnumpy_size", b.shape,
      "\ntensor_size", a.size())
a.add_(1)
print(b)

print("======================")
a = np.ones(5)
print(a, a.shape)
b = torch.from_numpy(a)   # array转换为tensor
print(b, b.size())
np.add(a, 1, out=a)
print(b)

# 另外除了CharTensor之外，所有的tensor都可以在CPU运算和GPU预算之间相互转换
print("=======cuda=========")
x = torch.ones(2,2)
y = torch.eye(2,2)
if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
print(x,y)

'''
转置
torch.transpose()  torch.transpose(input, dim0, dim1, out=None) → Tensor 二维转置
torch.Tensor.permute(dims) 多维转置
'''
xx = torch.ones(2, 3)
print(xx.size())
print(xx.permute(1, 0).size())

xx = torch.ones(2, 3, 4)
print(xx.size())
print(xx.permute(2, 0, 1).size())

'''
tensor指定值改变
'''
idx = [0, 0, 1, 1]
dis_c = torch.zeros(4, 4, 1, 1)
print(dis_c)
dis_c[[0, 1, 2, 3], idx] = 1.0
print(dis_c)

