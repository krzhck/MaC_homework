# Homework 4

**周雨豪  2018013399  软件82**



## 实验环境

**操作系统：** macOS 13

**RAM：**16 GB

**Python：**3.9.16

**torch：**2.0.0

**device：**CPU



## 1 运行 Baseline

运行 baseline 没有遇到太大问题，就只有 macOS 系统在数据集目录下有 .DS_Store 文件这个小问题，需要在读数据集的时候忽视该文件。



## 2 实验结果

### 2.1 相同参数对比预训练

参数选择：lr = 5e-4，batchsize = 64，epoch = 30

#### 预训练

<img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518104243306.png" alt="image-20230518104243306" style="zoom:20%;" /><img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518104252197.png" alt="image-20230518104252197" style="zoom:20%;" />

#### 无预训练

<img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518101605222.png" alt="image-20230518101605222" style="zoom:20%;" /><img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518101614644.png" alt="image-20230518101614644" style="zoom:20%;" />

根据数值可以看出预训练的 ResNet18 有大约 30% 的准确率提升

使用三种不同的 learning rate，loss 和 acc 变化曲线如下



### 2.2 不同参数

使用预训练的 ResNet18，控制 batchsize = 64，epoch = 30 不变，取三种不同的 learning rate。

#### lr = 5e-4

<img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518104243306.png" alt="image-20230518104243306" style="zoom:20%;" /><img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518104252197.png" alt="image-20230518104252197" style="zoom:20%;" />

<div style="page-break-after: always;"></div>

#### lr = 5e-3

<img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518162705179.png" alt="image-20230518162705179" style="zoom:20%;" /><img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518162721198.png" alt="image-20230518162721198" style="zoom:20%;" />

#### lr = 0.1

<img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518165235967.png" alt="image-20230518165235967" style="zoom:20%;" /><img src="/Users/krzhck/Library/Application Support/typora-user-images/image-20230518165243224.png" alt="image-20230518165243224" style="zoom:20%;" />

对比看出较低的 learning rate 效果更好。

