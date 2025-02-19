import ray
import torch
import torch.nn as nn
import torch.optim as optim

ray.init()

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

@ray.remote
def train_model(batch_size):
    model = SimpleModel()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()

    for _ in range(10):  # Simulate 10 epochs
        x = torch.randn(batch_size, 10)
        y = torch.randn(batch_size, 1)
        pred = model(x)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), "trained_model.pth")
    return loss.item()

if __name__ == "__main__":
    batch_sizes = [16, 32, 64, 128]
    results = ray.get([train_model.remote(bs) for bs in batch_sizes])
    print("Training Losses:", results)
