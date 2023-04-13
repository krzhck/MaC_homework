import torch
from torch import nn

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(2, 3, bias=False), nn.Sigmoid(), nn.Linear(3, 2, bias=False))
        self.net[0].weight = nn.parameter.Parameter(torch.Tensor([[1.0, 2.0], [0.5, 1.2], [-0.5, 1.0]]))
        self.net[2].weight = nn.parameter.Parameter(torch.Tensor([[-0.5, 1.0, 0.5], [1.0, -0.5, 0.2]]))

    def forward(self, x):
        print('-----Input-----')
        print(x)
        
        x = self.net[0](x)
        print('-----Linear_1-----')

        print(x)
        
        x = self.net[1](x)
        print('-----Sigmoid-----')
        print(x)
        
        x = self.net[2](x)
        print('-----Linear_2-----')
        print(x)
        return x

model = MLP()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(10):
    print('-----epoch %d-----' % epoch)
    pred = model(torch.Tensor([[0.2, 0.5]]))
    target = torch.Tensor([[1.0, 0.0]])
    loss = nn.functional.cross_entropy(pred, target)
    print('-----Loss-----')
    print(loss)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    print('-----After BP-----')
    for p in model.parameters():
        print(p)
    print('\n\n')
