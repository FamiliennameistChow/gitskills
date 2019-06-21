# -*- coding: utf-8 -*-
import numpy as np
import torch
import torch.nn as nn


'''
用于计算卷积层参数

'''


'''
逆卷积层参数计算
torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride=1, padding=0, output_padding=0, 
groups=1, bias=True, dilation=1, padding_mode='zeros')

https://blog.csdn.net/qq_27261889/article/details/86304061
H_out = (H_in - 1)*Stride-2*padding+size 
## H_out=(H_in − 1)∗stride[0]−2∗padding[0]+kernel_size[0]+output_padding[0]

'''

# 卷积核设置
# kernel = [size, stride, padding]
# kernel = [4, 1, 0]
# 输出channel设置
# out_channel_list = [in_channel, out_channel_1, out_channel_2, out_channel_3, out_channel_4,...]


# ########################参数设置##################################
# tensor = [100, 74, 1, 1]   # 输入tensor size
# kernel = [[1, 1, 0],
#           [7, 1, 0],
#           [4, 2, 1],
#           [4, 2, 1]]
# out_channel_list = [74, 1024, 128, 64, 1]
# LAYER_NUM = 4


tensor = [1, 100, 1, 1]   # 输入tensor size
kernel = [[4, 1, 0],
          [4, 2, 1],
          [4, 2, 1],
          [4, 2, 1],
          [4, 2, 1]]
out_channel_list = [100, 64*8, 64*4, 64*2, 64, 3]
LAYER_NUM = 5

###################################################################


def fs_conv(tensor, out_chanel, kernel):
    h_out = (tensor[2] - 1)*kernel[1]-2*kernel[2]+kernel[0]
    w_out = (tensor[3] - 1)*kernel[1]-2*kernel[2]+kernel[0]
    out = [tensor[0], out_chanel, h_out, w_out]
    return out


for i in range(LAYER_NUM):
    if i == 0:
        layer_sizes = tensor
    layer_sizes = fs_conv(layer_sizes, out_channel_list[i+1], kernel[i])
    print("the {} layer size: {}".format(i+1, layer_sizes))


'''
卷积过程
class torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True) 
参考：https://blog.csdn.net/u014525760/article/details/80647339
H_{out}=floor((H_{in}+2padding[0]-dilation[0](kernerl_size[0]-1)-1)/stride[0]+1)

'''

print("======conv result========")

def calcu_conv(tensor, out_chanel, kernel):
    h_out = (tensor[2] + 2 * kernel[2] - (kernel[0]-1) - 1) / kernel[1] + 1
    w_out = (tensor[3] + 2 * kernel[2] - (kernel[0]-1) - 1) / kernel[1] + 1
    out = [tensor[0], out_chanel, int(h_out), int(w_out)]
    return out


tensor = [1, 3, 64, 64]   # 输入tensor size
kernel = [[4, 2, 1],
          [4, 2, 1],
          [4, 2, 1],
          [4, 2, 1],
          [4, 1, 0]]
out_channel_list = [3, 64, 128, 256, 512, 1]
LAYER_NUM = 5
pool_size = 2
Pool = False

for i in range(LAYER_NUM):
    if i == 0:
        layer_sizes = tensor
    layer_sizes = calcu_conv(layer_sizes, out_channel_list[i+1], kernel[i])
    if Pool == True:
        layer_sizes[2] = int(layer_sizes[2] / pool_size)
        layer_sizes[3] = int(layer_sizes[3] / pool_size)
    print("the {} layer size: {}".format(i+1, layer_sizes))
