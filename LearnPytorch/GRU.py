import torch
import torch.nn as nn

# input hidden number_layer
number_layer=2
rnn = nn.GRU(7, 6, num_layers=number_layer ,bidirectional= True)
# Length batch input
input = torch.randn(5, 1, 7)
# number_layer batch hidden
h0 = torch.randn(2*number_layer, 1, 6)
output, hn = rnn(input, h0)

# print(hn.shape,hn[0].shape,hn[1].shape)
print(output.shape)
print(output[:,:,:6].shape)
# print(hn.shape)
# print(hn[-1])

print(output[:,:,6:].shape)
# print(hn)

# print(hn[0])
# print(hn[1])