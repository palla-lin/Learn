import torch
import torch.nn as nn

import torch
import torch.nn as nn
import torch.nn.functional as F
# import torch.optim as optim
# torch.manual_seed(1)
lstm = nn.LSTM(4, 3)  # 输入维度为3维，输出维度为3维
# inputs = [torch.randn(1, 4) for _ in range(5)]  # 生成一个长度为5的序列
# # 初始化隐藏状态.
# hidden = (torch.randn(1, 1, 3), torch.randn(1, 1, 3))
# for i in inputs:
#     # 将序列中的元素逐个输入到LSTM.
#     # 经过每步操作,hidden 的值包含了隐藏状态的信息.
#
#     out, hidden = lstm(i.view(1, 4,-1), hidden)
#     # 另外我们可以对一整个序列进行训练.
#     # LSTM第一个返回的第一个值是所有时刻的隐藏状态
#     # 第二个返回值是最后一个时刻的隐藏状态
#     # (所以"out"的最后一个和"hidden"是一样的)
#     # 之所以这样设计:
#     # 通过"out"你能取得任何一个时刻的隐藏状态，而"hidden"的值是用来进行序列的反向传播运算, 具体方式就是将它作为参数传入后面的 LSTM 网络.
#     # 增加额外的第二个维度.
# # inputs = torch.cat(inputs).view(len(inputs), 1, -1)
# # hidden = (torch.randn(1, 1, 3), torch.randn(1, 1, 3)) # 清空隐藏状态.
# # out, hidden = lstm(inputs, hidden)
#     print(i)
#     print(i.view(1, 2,-1))
#     print(out)
#     print(hidden)
#     break
# a=2
# torch.manual_seed(1)
# p=torch.tensor([[1,2,3],[4,5,6]])
# q=torch.tensor([[10,20,30],[40,50,60]])
# print(p)
# print(q)
# p.add_(-a,q)
# print(p)

# import nltk
#
# from nltk.tokenize import word_tokenize

# mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
#
# print()
# import wandb
# import os
#
# wandb.init(project="77",name='98')
# os.environ['WANDB_MODE'] = 'dryrun'  # position 3
# for i in range(10,20):
#   wandb.log({'num':i})
a = torch.randn(2,3)
b = torch.randn(4,3)
c = a+b
print(c,c.shape)