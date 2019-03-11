import torch
import torch.utils.data as Data

BATCH_SIZE = 8

x = torch.linspace(1, 10, 10)
y = torch.linspace(10, 1, 10)

torch_dataset = Data.TensorDataset(x, y)
loader = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,  # 打乱data的循序
    # num_workers=2,
)

for epoch in range(3):
    for step, (batch_x, batch_y) in enumerate(loader):
        # training
        print('Epoch:', epoch, '| Step: ', step, '| batch_x: ',
              batch_x.numpy(), '| batch_y: ', batch_y.numpy())

