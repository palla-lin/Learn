import torch
import torch.nn as nn
import torch.nn.functional as F
device = torch.device('cuda:0')
CONTEXT_SIZE = 2  # 左右各两个词
raw_text ="""We are about to study the idea of a computational process.
Computational processes are abstract beings that inhabit computers.
As they evolve, processes manipulate other abstract things called data.
The evolution of a process is directed by a pattern of rules
called a program. People create programs to direct processes. In effect,
we conjure the spirits of the computer with our spells.
""".split()
# 通过对`raw_text`使用set()函数，我们进行去重操作
vocab = set(raw_text)
vocab_size = len(vocab)
word_to_ix = {word: i for i, word in enumerate(vocab)}
data = []
for i in range(2, len(raw_text) - 2):
    context = [raw_text[i - 2], raw_text[i - 1],

               raw_text[i + 1], raw_text[i + 2]]
    target = raw_text[i]
    data.append((context, target))
print(data[:5])


class CBOW(nn.Module):
    def __init__(self):
        pass
    def forward(self, inputs):
        pass


# 创建模型并且训练。这里有些函数帮你在使用模块之前制作数据。
def make_context_vector(context, word_to_ix):
    idxs = [word_to_ix[w] for w in context]
    return torch.tensor(idxs, dtype=torch.long)
a=make_context_vector(data[0][0], word_to_ix)  # example
print(a)