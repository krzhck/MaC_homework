from torch import nn
import torch.nn.functional as F

class BasicBlock(nn.Module):
    def __init__(self,in_channels,out_channels,stride=[1,1],padding=1) -> None:
        super(BasicBlock, self).__init__()

        # 这里是需要自行补全的部分
        # layer和shortcut分别代表两个分支
        # layer：3*3卷积->BatchNorm2d->ReLU->3*3卷积->BatchNorm2d
        self.layer = nn.Sequential(
            # Your code here



        )

        # 输入输出通道相等时，shortcut不需要任何操作
        self.shortcut = nn.Sequential()
        # 不相等时，需要通过1*1卷积和BatchNorm2d
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                # Your code here



            )
        # 可在CSDN上看nn中的基本函数用法：https://blog.csdn.net/weixin_42495721/article/details/111518564

    def forward(self, x):
        out = self.layer(x)
        out += self.shortcut(x)
        out = F.relu(out)
        return out

class ResNet18(nn.Module):
    def __init__(self, BasicBlock, num_classes=10) -> None:
        super(ResNet18, self).__init__()
        self.in_channels = 64
        # 第一层没有残差快
        self.conv1 = nn.Sequential(
            nn.Conv2d(3,64,kernel_size=7,stride=2,padding=3,bias=False),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        self.conv2 = self._make_layer(BasicBlock,64,[[1,1],[1,1]])
        self.conv3 = self._make_layer(BasicBlock,128,[[2,1],[1,1]])
        self.conv4 = self._make_layer(BasicBlock,256,[[2,1],[1,1]])
        self.conv5 = self._make_layer(BasicBlock,512,[[2,1],[1,1]])
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(512, num_classes)

    def _make_layer(self, block, out_channels, strides):
        layers = []
        for stride in strides:
            layers.append(block(self.in_channels, out_channels, stride))
            self.in_channels = out_channels
        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.conv5(out)
        out = self.avgpool(out)
        out = out.reshape(x.shape[0], -1)
        out = self.fc(out)
        return out
