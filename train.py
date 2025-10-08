from model import UNet
from dataset import ISBI_Loader
from torch import optim
import torch.nn as nn
import torch
from torch.utils.tensorboard import SummaryWriter
def train_net(net, device, data_path, epochs=40, batch_size=2, lr=0.00001):
    # 加载训练集
    isbi_dataset = ISBI_Loader(data_path)
    train_loader = torch.utils.data.DataLoader(dataset=isbi_dataset,
                                               batch_size=batch_size,
                                               shuffle=True)
    # 定义RMSprop算法
    optimizer = optim.RMSprop(net.parameters(), lr=lr, weight_decay=1e-8, momentum=0.9)
    # 定义Loss算法
    criterion = nn.BCEWithLogitsLoss()
    # best_loss统计，初始化为正无穷
    best_loss = float('inf')
    # 训练epochs次
    writer = SummaryWriter(log_dir='runs/experiment_1')
    for epoch in range(epochs):
        net.train()
        for batch_idx, (image, label) in enumerate(train_loader):
            optimizer.zero_grad()
            image = image.to(device=device, dtype=torch.float32)
            label = label.to(device=device, dtype=torch.float32)
            pred = net(image)
            loss = criterion(pred, label)
            print('Loss/train', loss.item())

            # Log the loss
            writer.add_scalar('Loss/train', loss.item(), epoch * len(train_loader) + batch_idx)

            if loss < best_loss:
                best_loss = loss
                torch.save(net.state_dict(), 'best_model_666.pth')
            loss.backward()
            optimizer.step()
    writer.close()

if __name__ == "__main__":
    # 选择设备，有cuda用cuda，没有就用cpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # 加载网络，图片单通道1，分类为1。
    net = UNet(n_channels=1, n_classes=1)
    # 将网络拷贝到deivce中
    net.to(device=device)
    # 指定训练集地址，开始训练
    data_path = "D:\\srtp\\img_segAndcorr-master\\dataset4segmentation"
    train_net(net, device, data_path)
