# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
from torch.jit import ScriptModule, script_method, trace

# x = torch.ones(100, 74, 1, 1)
#
# print(x.size())
#
# tconv1 = nn.ConvTranspose2d(74, 1024, 1, 1, bias=False)
# output = tconv1(x)
# print(output.size())




class CNN_C(ScriptModule):
    def __init__(self):
        super(CNN_C, self).__init__()
        self.conv1 = trace(nn.Conv2d(1, 16, 5, 1, 2), torch.rand(1, 1, 28, 28))
        self.pool1 = trace(nn.MaxPool2d(2), torch.rand())
        self.conv2 = trace(nn.Conv2d(16, 32, 5, 1, 2), torch.rand(1, 16, 14, 14))
        self.out = trace(nn.Linear(32*7*7, 10), torch.rand())

