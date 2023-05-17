import os
import torch
from PIL import Image
import numpy as np
from torch.utils.data.dataset import Dataset
from torch.utils.data.dataloader import DataLoader
import torchvision.transforms as transforms
from torchvision import models
from model import BasicBlock, ResNet18
import matplotlib.pyplot as plt

# 到数据集的路径
img_dir_train='./iNaturalist/train'
img_dir_val='./iNaturalist/val'

# 定义torch的数据集
class NatureDataset(Dataset):
    def __init__(self, img_dir, img_size=[32, 32], if_train=True):
        self.img_dir = img_dir
        self.class_list = os.listdir(self.img_dir)
        self.num_classes = len(self.class_list)
        if if_train is True:
            self.transform = transforms.Compose([
                transforms.Resize(img_size),
                transforms.RandomHorizontalFlip(),
                transforms.RandomVerticalFlip(),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        else:
            self.transform = transforms.Compose([
                transforms.Resize(img_size),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        self.data = []
        self.anno = []
        for i, cls in enumerate(self.class_list):
            if cls == '.DS_Store':
                continue
            img_names = os.listdir(os.path.join(self.img_dir, cls))
            for img_name in img_names:
                self.data.append(os.path.join(self.img_dir, cls, img_name))
                self.anno.append(i)

    def __len__(self):
        return len(self.anno)

    def __getitem__(self, index):
        img = Image.open(self.data[index])
        img = img.convert('RGB')
        img = self.transform(img)
        label = self.anno[index]
        label = torch.from_numpy(np.array(label))
        label = label.long()
        return img, label

# 可设置的参数
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
epochs = 30
lr = 5e-4
batch_size = 64

# 加载数据集
train_dataset = NatureDataset(img_dir_train)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataset = NatureDataset(img_dir_val, if_train=False)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# 如果使用编写的ResNet18
#model = ResNet18(BasicBlock, num_classes=train_dataset.num_classes)

# 如果使用预训练的ResNet18
model = models.resnet18(pretrained=True)
num_features = model.fc.in_features
model.fc = torch.nn.Linear(num_features, train_dataset.num_classes)
model = model.to(device)

# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

loss_list = []
acc_list = []
# 训练和验证
for epoch in range(epochs):
    model.train()
    for batch_idx, (img, label) in enumerate(train_loader):
        img, label = img.to(device), label.to(device)
        logits = model(img)
        loss = criterion(logits, label)
        optimizer.zero_grad()
        # 这里的loss是每个batch的loss，绘图时需要将一轮内所有batch的加起来或取平均
        loss.backward()
        optimizer.step()
        print('training:', epoch+1, batch_idx*batch_size, '/', len(train_dataset), '  loss:', loss.item())
    model.eval()
    with torch.no_grad():
        total_correct = 0
        total_num = 0
        for img, label in val_loader:
            img, label = img.to(device), label.to(device)
            logits = model(img)
            pred = logits.argmax(dim=1)
            correct = torch.eq(pred, label).float().sum().item()
            total_correct += correct
            total_num += img.size(0)

    acc = total_correct / total_num
    loss_list.append(loss.item())
    acc_list.append(acc)
    print(epoch+1, 'test acc:', acc)

plt.plot(range(epochs), loss_list)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.title("loss")
plt.show()

plt.plot(range(epochs), acc_list)
plt.xlabel("epoch")
plt.ylabel("acc")
plt.title("acc")
plt.show()
