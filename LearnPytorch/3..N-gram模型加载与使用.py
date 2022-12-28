import torch
import torch.nn as nn
import torch.nn.functional as F
device = torch.device('cuda:0')

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
Proving his beauty by succession thine!
This were to be new made when thou art old,
And see thy blood warm when thou feel'st it cold.""".split()
# 应该对输入变量进行标记，但暂时忽略。
# 创建一系列的元组，每个元组都是([ word_i-2, word_i-1 ], target word)的形式。
vocab = set(test_sentence)
word_to_ix = {word: i for i, word in enumerate(vocab)}
ix_to_word={i:word for word,i in word_to_ix.items()}

#加载模型
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
#         print('log_probs',log_probs)
        return log_probs
model=NGramLanguageModeler(97,10,2)
model.load_state_dict(torch.load('myngram.model'))
model.eval()
model.to(device=device)
#推理预测
trigrams = [([test_sentence[i], test_sentence[i + 1]], test_sentence[i + 2])for i in range(len(test_sentence) - 2)]
for context, target in trigrams:
    context_idxs = torch.tensor([word_to_ix[w] for w in context],
                                dtype=torch.long).to(device)


    log_probs = model(context_idxs)
    _,indice=torch.max(log_probs,dim=1)
    pre_tar=ix_to_word[indice.item()]
    print(context,target,pre_tar)
    count=0
    if pre_tar==target:
        count+=1
    a=count/len(trigrams)
    print(a)




