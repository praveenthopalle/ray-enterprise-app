from ray import serve
import torch

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

serve.start()

@serve.deployment
class ModelDeployment:
    def __init__(self):
        self.model = SimpleModel()
        self.model.load_state_dict(torch.load("trained_model.pth"))
        self.model.eval()

    def __call__(self, request):
        return {"message": "Model Ready for Inference"}

model_handle = ModelDeployment.deploy()
