from data.fetch_data import get_train_test
from data.preprocess import *
from data.Dataset import my_dataset
from model.models import LSTM, GRU
from torch.utils.data import DataLoader
from model.train_model import train
import torch.optim as optim
import torch.nn as nn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    (X_train_prev,
     X_train_today,
     Y_train,
     X_test_prev,
     X_test_today,
     Y_test) = make_dataset()

    trainset = my_dataset(X_train_prev, X_train_today, Y_train)
    trainloader = DataLoader(trainset, batch_size=20, shuffle=True)
    testset = my_dataset(X_test_prev, X_test_today, Y_test)
    testloader = DataLoader(testset, batch_size=20)

    #train model
    model = GRU()
    EPOCHS = 100
    LR = 0.001
    WD = 0.0001  #weight decat
    optimizer = optim.Adam(model.parameters(), lr=LR, weight_decay=WD)
    criterion = nn.MSELoss()

    train(model, EPOCHS, trainloader, testloader, optimizer, criterion)



