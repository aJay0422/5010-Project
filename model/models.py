import numpy as np
import torch
import torch.nn as nn
import torch.functional as F

class LSTM(nn.Module):
    def __init__(self, input_size=4, hidden_size=64, num_layers=1):
        super(LSTM, self).__init__()

        self.lstm = nn.LSTM(
            input_size = input_size,
            hidden_size = hidden_size,
            num_layers = num_layers,
            batch_first = True
        )

        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(hidden_size + 1, 32),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(32, 1),
        )

    def forward(self, X_prev, X_today):
        r_out, (h_n, h_c) = self.lstm(X_prev, None)
        h_n = torch.squeeze(h_n)
        X_today = torch.unsqueeze(X_today, dim=1)
        out = self.classifier(torch.cat((h_n, X_today), dim=1))

        return out

class GRU(nn.Module):
    def __init__(self, input_size=4, hidden_size=64, num_layers=1):
        super(GRU, self).__init__()

        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(hidden_size + 1, 32),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(32, 1),
        )

    def forward(self, X_prev, X_today):
        r_out, (h_n) = self.gru(X_prev, None)
        h_n = torch.squeeze(h_n)
        X_today = torch.unsqueeze(X_today, dim=1)
        out = self.classifier(torch.cat((h_n, X_today), dim=1))

        return out