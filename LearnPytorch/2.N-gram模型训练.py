import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
torch.manual_seed(1)

device = torch.device('cuda:0')
CONTEXT_SIZE = 2
EMBEDDING_DIM = 10
# 我们用莎士比亚的十四行诗 Sonnet 2
test_sentence = """When forty winters shall besiege thy brow,
And dig deep trenches in thy beauty's field,
Thy youth's proud livery so gazed on now,
Will be a totter'd weed of small worth held:
Then being asked, where all thy beauty lies,
Where all the treasure of thy lusty days;
To say, within thine own deep sunken eyes,
Were an all-eating shame, and thriftless praise.
How much more praise deserv'd thy beauty's use,
If thou couldst answer 'This fair child of mine
Shall sum my count, and make my old excuse,
'
Proving his beauty by succession thine!
This were to be new made when thou art old,
And see thy blood warm when thou feel'st it cold.""".split()
# 应该对输入变量进行标记，但暂时忽略。
# 创建一系列的元组，每个元组都是([ word_i-2, word_i-1 ], target word)的形式。

print(test_sentence)
trigrams = [([test_sentence[i], test_sentence[i + 1]], test_sentence[i + 2])for i in range(len(test_sentence) - 2)]
# 输出前3行，先看下是什么样子。
print(trigrams[:3])
vocab = set(test_sentence)
word_to_ix = {word: i for i, word in enumerate(vocab)}

print('kkkkkkkkkkkkk',len(vocab))
class NGramLanguageModeler(nn.Module):
    def __init__(self, vocab_size, embedding_dim, context_size):
        super(NGramLanguageModeler, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(context_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, vocab_size)
    def forward(self, inputs):
        embeds = self.embeddings(inputs)#inputs一个上下文的索引，embeds是上下文对应的向量

        embeds=embeds.view((1, -1))#这一步其实把两个向量拼接在一起，(2,10)->(1,20)
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)

        log_probs = F.log_softmax(out, dim=1)
        # print('log_probs',log_probs)
        return log_probs
        
losses = []
loss_function = nn.NLLLoss()
model = NGramLanguageModeler(len(vocab), EMBEDDING_DIM, CONTEXT_SIZE)
model.to(device=device)
optimizer = optim.SGD(model.parameters(), lr=0.001)
for epoch in range(10):
    total_loss = 0
    for context, target in trigrams:
        # 步骤 1\. 准备好进入模型的数据 (例如将单词转换成整数索引,并将其封装在变量中)
        context_idxs = torch.tensor([word_to_ix[w] for w in context],
                                dtype=torch.long)
        # 步骤 2\. 回调torch累乘梯度
        # 在传入一个新实例之前，需要把旧实例的梯度置零。
        optimizer.zero_grad()
        # 步骤 3\. 继续运行代码，得到单词的log概率值。
        context_idxs=context_idxs.to(device)
        print('context',context_idxs)
        log_probs = model(context_idxs)
        print('log_',log_probs.shape)
        print('target',target,torch.tensor([word_to_ix[target]]))
        # 步骤 4\. 计算损失函数（再次注意，Torch需要将目标单词封装在变量里）。
        loss = loss_function(log_probs, torch.tensor([word_to_ix[target]],
                                                 dtype=torch.long).to(device))
        # 步骤 5\. 反向传播更新梯度
        loss.backward()
        optimizer.step()
        # 通过调tensor.item()得到单个Python数值。
        total_loss += loss.item()
        break
    losses.append(total_loss)
    break
print('losses',losses)  # 用训练数据每次迭代，损失函数都会下降。
