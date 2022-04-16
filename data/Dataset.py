from torch.utils.data import Dataset
import torch

class my_dataset(Dataset):
    def __init__(self, X_prev, X_today, Y):
        self.data_prev = torch.Tensor(X_prev)
        self.data_today = torch.Tensor(X_today)
        self.label = torch.Tensor(Y)

    def __getitem__(self, index):
        return self.data_prev[index], self.data_today[index], self.label[index]

    def __len__(self):
        return len(self.data_prev)