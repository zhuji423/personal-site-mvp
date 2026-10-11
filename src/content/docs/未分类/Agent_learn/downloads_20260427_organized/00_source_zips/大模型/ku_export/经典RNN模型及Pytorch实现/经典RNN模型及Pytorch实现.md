---
title: "经典RNN模型及Pytorch实现"
description: "论文：Serial Order : a parallel distributed processing approach （1986）"
date: "2026-10-11"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\00_source_zips\\大模型\\ku_export\\经典RNN模型及Pytorch实现\\经典RNN模型及Pytorch实现.md"
---
# 经典RNN模型及Pytorch实现
一、RNN1. 介绍RNN（Recurrent Neural Network）是一类用于处理序列数据的神经网络。在不同时间点上收集到的数据，反映了某一事物、现象等随时间的变化状态或程度，比如文字序列，简单总结就是后面的数据跟前面的数据有关系。

论文：Serial Order : a parallel distributed processing approach （1986）

2. 结构分析RNN![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=49efd5d0b17849c48b93b41e4bd47c5f&docGuid=tQlIqth_Pf778Z)

模型输入（inputs）RNN模型主要应用于时序型的数据，常见的应用类型为

a.如自然语言：你恰饭了没啊，x1为你，x2为恰…以此类推

b.股票价格，每日天气情况等

对于该类数据，传统模型无法表达前一个状态与后一个状态之间的连续性，故一般采用序列型的模型。

隐藏层（hidden）![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=5377624dc3964fe0a5893a19ac8bce71&docGuid=tQlIqth_Pf778Z)

ht为t时刻输入x对应的隐藏单元

ht为t时刻时输入对应的隐藏单元的值U是输入层到隐藏层的权重矩阵W就是上一次隐藏层的值ht-1作为本次输入的权值矩阵b为偏置量输出层（output）![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=864948c2130e414facd2752d1d800e0e&docGuid=tQlIqth_Pf778Z)

得到隐藏层的内容后即可计算输出结果

V是隐藏层到输出层的权重矩阵c为偏置量注：在计算时，每一步使用的参数U、W、V、b、c都是一样的，也就是说每个步骤的参数都是共享的

BiRNN双向循环神经网络，即可以从过去的时间点获取记忆，又可以从未来的时间点获取信息。基本思想是提出每一个训练序列向前和向后分别是两个循环神经网络（RNN），而且这两个都连接着一个输出层。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=79cc7a35e0e84d6eac0fa1753ccb154c&docGuid=tQlIqth_Pf778Z)

3. 代码实现import torchimport torch.nn as nnclass RNN(nn.Module):    def __init__(self, input_size, class_num, hidden_size, num_layers):        super().__init__()        """        input_size    – 输入x中预期特征的数量        hidden_size   – 隐藏状态h的特征数量        num_layers    - 循环层数。例如，设置 num_layers=2意味着将两个RNN 堆叠在一起形成一个堆叠的RNN，第二个RNN接收第一个RNN的输出并计算最终结果。默认值：1        nonlinearity  – 隐藏层函数，可以是“tanh”或“relu”。默认值：'tanh'        bias 		  - 如果为 False，则该层不使用偏差权重。默认值：真        batch_first   - 输入特征是不是批量输入。默认值False        dropout 	  - 是否要引入Dropout层，dropout概率等于dropout。默认值：0        bidirectional – 如果为真，则成为双向 RNN。默认值：假        """        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, batch_first=True)        self.linear = nn.Linear(hidden_size, class_num)    def forward(self, x):        rnn_output, hidden = self.rnn(x)        output = self.linear(rnn_output[:, -1, :])        # output = self.linear(hidden[-1])        return outputclass BiRNN(nn.Module):    def __init__(self, input_size, class_num, hidden_size, num_layers):        super().__init__()        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True, bidirectional=True)        self.linear = nn.Linear(2 * hidden_size, class_num)    def forward(self, x):        rnn_output, hidden = self.rnn(x)        # concat the last hidden state from two direction        hidden_out = torch.cat((hidden[-2, :, :], hidden[-1, :, :]), 1)        output = self.linear(hidden_out)        return output4. 训练通过最小化损失误差（即输出的y与真实类别之间的距离），可以不断训练网络，使得循环神经网络可以准确地预测文本所属的类别，达到分类目的。相比于卷积神经网络等前馈神经网络，循环神经网络由于具备对序列顺序信息的刻画能力，往往能得到更准确的结果。

RNN的训练算法为：BPTT 

BPTT的基本原理和BP算法是一样的，同样是三步：

前向计算每个神经元的输出值；反向计算每个神经元的误差项值，它是误差函数E对神经元j的加权输入的偏导数；计算每个权重的梯度。最后再用随机梯度下降算法更新权重。

5. 局限性长期依赖问题：而RNN虽然在理论上可以保留所有历史时刻的信息，但在实际使用时，信息的传递往往会因为时间间隔太长而逐渐衰减，传递一段时刻以后其信息的作用效果就大大降低了。因此，普通RNN对于信息的长期依赖问题没有很好的处理办法。

二、LSTM 长短期记忆网络1. 介绍长短期记忆（Long short-term memory, LSTM）是一种特殊的RNN，主要是为了解决长序列训练过程中的梯度消失和梯度爆炸问题。简单来说，就是相比普通的RNN，LSTM能够在更长的序列中有更好的表现。

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=43c26037eb984a3780caaf81e53721e9&docGuid=tQlIqth_Pf778Z)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f076469e40c3466a848a78d192ee77e6&docGuid=tQlIqth_Pf778Z)

LSTM和GRU具有称为门（gate）的内部机制，它可以调节信息流。这些门可以了解序列中哪些数据重要以进行保留或丢弃。这样，它可以将相关信息传递到长序列中进行预测。现有的基于RNN的几乎所有技术结果都是通过LSTM和GRU这两个网络实现的。LSTM和GRU进行语音识别，语音合成和文本生成，甚至可以使用它们为视频生成字幕。

论文：Long Short-Term Memory（1997）

2. 结构分析在LSTM中，采用专门设计的“门”来引入或者去除细胞状态 Ct 中的信息。门是一种让信息选择性通过的方法。

与传统的循环神经网络相比，LSTM仍然是基于xt和ht−1来计算ht，只不过对内部的结构进行了更加精心的设计，加入了输入门it 、遗忘门ft以及输出门ot三个门和一个内部记忆单元ct。当前的LSTM接收来自上一个时刻的细胞状态 Ct-1，并与当前LSTM接收的信号输入 xt 共同作用产生当前LSTM的细胞状态 Ct

sigmoid激活作用

它类似于tanh激活，但不是在-1和1之间压缩值，而是在0和1之间取值。这有助于更新或忘记数据，因为任何数字乘以0都是0，使值消失或者说被“遗忘”。任何数字乘以1都是相同的值，因此值保持相同”。网络可以了解哪些数据不重要可以被遗忘，或者哪些数据需要保存。

遗忘门![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=bd867b22e7f14313a48f67d4183638ac&docGuid=tQlIqth_Pf778Z)

记忆门![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=ae9da4c5be1243099c4e83f611c5cd3e&docGuid=tQlIqth_Pf778Z)

更新细胞状态![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=212631b70d7a488c859ef48658ba87a6&docGuid=tQlIqth_Pf778Z)

输出门![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=625abff1046348a480fe953b5c721577&docGuid=tQlIqth_Pf778Z)

3. 代码实现import torch.nn as nnclass LSTM(nn.Module):    def __init__(self, input_size, class_num, hidden_size):        super().__init__()        self.lstm = nn.LSTM(input_size, hidden_size, num_layers=1, batch_first=True)        self.linear = nn.Linear(hidden_size, class_num)    def forward(self, x):        lstm_output, (h_n, c_n) = self.lstm(x)        output = self.linear(lstm_output[:, -1, :])        # output = self.linear(h_n[-1])        return outputclass BiLSTM(nn.Module):    def __init__(self, input_size, class_num, hidden_size):        super().__init__()        self.lstm = nn.LSTM(input_size, hidden_size, num_layers=1, batch_first=True)        self.linear = nn.Linear(2 * hidden_size, class_num)    def forward(self, x):        lstm_output, (h_n, c_n) = self.lstm(x)        output = self.linear(lstm_output[:, -1, :])        # output = self.linear(torch.cat((h_n[-2], h_n[-1]), 1))        return output4. 变体![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=cc834b2faf454e83b2fa823d06efdc42&docGuid=tQlIqth_Pf778Z)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=784324d9483a4eb19619bb0da402bfbd&docGuid=tQlIqth_Pf778Z)

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f8936b73f5134e1ca8ca8c8183e70ae7&docGuid=tQlIqth_Pf778Z)

三、GRU 门控循环单元1. 介绍相比LSTM，使用GRU能够达到相当的效果，并且相比之下更容易进行训练，能够很大程度上提高训练效率，因此很多时候会更倾向于使用GRU。

论文：Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation（2014）

2. 结构分析![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=f076469e40c3466a848a78d192ee77e6&docGuid=tQlIqth_Pf778Z)

更新门更新门的作用类似于LSTM的遗忘和输入门。它决定要丢弃哪些信息和要添加哪些新信息。

重置门重置门是另一个用来决定要忘记多少过去的信息的门。

计算过程

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=4cfc2dd6a7eb4e348158c7cf7f2f8969&docGuid=tQlIqth_Pf778Z)

首先同样会计算一个量 nt 作为最终隐层状态 ht 的部分，计算规则如下：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=594026517570413a8040d046d13e63c7&docGuid=tQlIqth_Pf778Z)

其中 ht 就是 GRU 中的隐层状态，计算规则如下：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=62eb9c30ce3349a5a1f0dfa9af47a624&docGuid=tQlIqth_Pf778Z)

至此未给出定义的量还有 rt , zt ，在 GRU 中分别称为重置门 reset 和更新门 update，它们的计算规则一致，如下所示：

![](https://rte.weiyun.baidu.com/wiki/attach/image/api/imageDownloadAddress?attachId=b35b6a2e2547417caa3e312a2f9bd39f&docGuid=tQlIqth_Pf778Z)

GRU 将 LSTM 中的三个门控简化为两个，并且没有记忆单元 ct 在网络时间流中传递。

GRU的张量操作较少，训练速度要比LSTM快一些。如果将重置门设置为 1，更新门设置为 0，那么将再次获得标准 RNN 模型。

3. 代码实现import torchimport torch.nn as nnclass GRU(nn.Module):    def __init__(self, input_size, class_num, hidden_size):        super().__init__()        self.gru = nn.GRU(input_size, hidden_size, num_layers=1, batch_first=True)        self.linear = nn.Linear(hidden_size, class_num)    def forward(self, x):        gru_output, hidden = self.gru(x)        output = self.linear(gru_output[:, -1, :])        # output = self.linear(hidden[-1])        return outputclass BiGRU(nn.Module):    def __init__(self, input_size, class_num, hidden_size):        super().__init__()        self.gru = nn.GRU(input_size, hidden_size, batch_first=True, bidirectional=True)        self.linear = nn.Linear(2 * hidden_size, class_num)    def forward(self, x):        gru_output, hidden = self.gru(x)        # concat the last hidden state from two direction        hidden_out = torch.cat((hidden[-2, :, :], hidden[-1, :, :]), 1)        output = self.linear(hidden_out)        # output = self.linear(gru_output[:, -1, :])        return output四、实际应用| 模型 | 参数及loss图 | 序列图 |
| --- | --- | --- |
| RNN | EPOCHS = 100，hidden_size = 8，运行时长2.89秒loss_func = nn.MSELoss()opt = torch.optim.Adam(model.parameters(), lr=1e-2) |  |
| LSTM | EPOCHS = 100，hidden_size = 8，运行时长10.89秒loss_func = nn.MSELoss()opt = torch.optim.Adam(model.parameters(), lr=1e-2) |  |
| GRU | EPOCHS = 100，hidden_size = 8，运行时长5.77秒loss_func = nn.MSELoss()opt = torch.optim.Adam(model.parameters(), lr=1e-2) |  |

import timeimport numpy as npimport tushare as tsimport torchfrom torch import nnimport matplotlib.pyplot as pltfrom models.RNN.RNN import RNNfrom models.RNN.LSTM import LSTMfrom models.RNN.GRU import GRUdef create_dataset(data, days_for_train=5) -> (np.array, np.array):    dataset_x, dataset_y = [], []    for i in range(len(data) - days_for_train):        _x = data[i:(i + days_for_train)]        dataset_x.append(_x)        dataset_y.append(data[i + days_for_train])    return (np.array(dataset_x), np.array(dataset_y))def load_data(data_close, DAYS_FOR_TRAIN):    dataset_x, dataset_y = create_dataset(data_close, DAYS_FOR_TRAIN)    # 划分训练集和测试集，70%作为训练集    train_size = int(len(dataset_x) * 0.7)    train_x = dataset_x[:train_size]    train_y = dataset_y[:train_size]    # 将数据改变形状，RNN 读入的数据维度是 (seq_size, batch_size, feature_size)    train_x = train_x.reshape(-1, 1, DAYS_FOR_TRAIN)    train_y = train_y.reshape(-1, 1, 1)    # 转为pytorch的tensor对象    train_x = torch.from_numpy(train_x)    train_y = torch.from_numpy(train_y)    return dataset_x, train_x, train_ydef download_dataset():    # 获取上证指数从20180101开始的收盘价的np.ndarray    data_close = ts.get_k_data('000001', start='2018-01-01', index=True)['close'].values    data_close = data_close.astype('float32')  # 转换数据类型    # 将价格标准化到0~1    max_value = np.max(data_close)    min_value = np.min(data_close)    data_close = (data_close - min_value) / (max_value - min_value)    return data_closedef plot_lost(loss_list, model_name):    """    可视化损失变化    """    plt.figure(figsize=(10, 5))    freqs = [i for i in range(len(loss_list))]    # 绘制训练损失变化曲线    plt.plot(freqs, loss_list, color='#e4007f', label="%s Train loss" % model_name)    # 绘制坐标轴和图例    plt.ylabel("loss", fontsize='large')    plt.xlabel("freq", fontsize='large')    plt.legend(loc='upper right', fontsize='x-large')    plt.savefig("output/img/loss_%s.jpg" % model_name)def plot_all_data(pred_test, data_close, train_size, model_name):    plt.figure()    plt.plot(pred_test, 'r', label='prediction')    plt.plot(data_close, 'b', label='real')    plt.plot((train_size, train_size), (0, 1), 'g--')    plt.legend(loc='best')    plt.savefig("output/img/plot_seq_%s.jpg" % model_name)def train(model, device, train_x, train_y, opt, loss_func, epoch):    model.train()    train_x, train_y = train_x.to(device), train_y.to(device)    opt.zero_grad()    out = model(train_x)    loss = loss_func(out, train_y)    loss.backward()    opt.step()    loss_list.append(loss.item())    if (epoch + 1) % 20 == 0:        print('Epoch: {}, Loss:{:.5f}'.format(epoch + 1, loss.item()))def test(model, device, dataset_x, DAYS_FOR_TRAIN):    model = model.eval()  # 转换成测试模式    # 注意这里用的是全集 模型的输出长度会比原数据少DAYS_FOR_TRAIN 填充使长度相等再作图    dataset_x = dataset_x.reshape(-1, 1, DAYS_FOR_TRAIN)  # (seq_size, batch_size, feature_size)    dataset_x = torch.from_numpy(dataset_x)    dataset_x = dataset_x.to(device)    pred_test = model(dataset_x)  # 全量训练集的模型输出 (seq_size, batch_size, output_size)    pred_test = pred_test.view(-1).data.numpy()    pred_test = np.concatenate((np.zeros(DAYS_FOR_TRAIN), pred_test))  # 填充0 使长度相同    assert len(pred_test) == len(data_close)    return pred_testif __name__ == '__main__':    T1 = time.time()    EPOCHS = 100    DAYS_FOR_TRAIN = 10    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")    loss_list = []    # 加载数据    data_close = download_dataset()    dataset_x, train_x, train_y = load_data(data_close, DAYS_FOR_TRAIN)    model = RNN(DAYS_FOR_TRAIN, 8)    # model = LSTM(DAYS_FOR_TRAIN, 8)    # model = GRU(DAYS_FOR_TRAIN, 8)    loss_func = nn.MSELoss()    opt = torch.optim.Adam(model.parameters(), lr=1e-2)    for epoch in range(1, EPOCHS + 1):        train(model, DEVICE, train_x, train_y, opt, loss_func, epoch)    pred_test = test(model, DEVICE, dataset_x, DAYS_FOR_TRAIN)    model_name = model.__class__.__name__    # 保存模型参数    torch.save(model.state_dict(), 'output/%s.pth' % model_name)    # 可视化损失变化    plot_lost(loss_list, model_name)    # 可视化整体序列    train_size = int(len(dataset_x) * 0.7)    plot_all_data(pred_test, data_close, train_size, model_name)    T2 = time.time()    print('程序运行时间:%s秒' % (round(T2 - T1, 6)))class RNN(nn.Module):    def __init__(self, input_size, hidden_size, output_size=1, num_layers=1):        super().__init__()        self.rnn = nn.RNN(input_size, hidden_size, num_layers)        self.fc = nn.Linear(hidden_size, output_size)    def forward(self, _x):        x, _ = self.rnn(_x)  # _x is input, size (seq_len, batch, input_size)        s, b, h = x.shape  # x is output, size (seq_len, batch, hidden_size)        x = x.view(s * b, h)        x = self.fc(x)        x = x.view(s, b, -1)  # 把形状改回来        return xclass LSTM(nn.Module):    def __init__(self, input_size, hidden_size, output_size=1, num_layers=2):        super().__init__()        self.lstm = nn.LSTM(input_size, hidden_size, num_layers)        self.fc = nn.Linear(hidden_size, output_size)    def forward(self, _x):        x, _ = self.lstm(_x)  # _x is input, size (seq_len, batch, input_size)        s, b, h = x.shape  # x is output, size (seq_len, batch, hidden_size)        x = x.view(s * b, h)        x = self.fc(x)        x = x.view(s, b, -1)  # 把形状改回来        return xclass GRU(nn.Module):    def __init__(self, input_size, hidden_size, output_size=1, num_layers=1):        super().__init__()        self.gru = nn.GRU(input_size, hidden_size, num_layers)        self.fc = nn.Linear(hidden_size, output_size)    def forward(self, _x):        x, _ = self.gru(_x)  # _x is input, size (seq_len, batch, input_size)        s, b, h = x.shape  # x is output, size (seq_len, batch, hidden_size)        x = x.view(s * b, h)        x = self.fc(x)        x = x.view(s, b, -1)  # 把形状改回来        return x

