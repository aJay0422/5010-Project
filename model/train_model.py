import torch


def train(model, epochs, trainloader, testloader, optimizer, criterion):

    for epoch in range(epochs):
        for X_prev_batch, X_today_batch, Y_batch in trainloader:
            #forward
            output = model(X_prev_batch, X_today_batch)
            loss = criterion(output.squeeze(), Y_batch)
            #backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


        #Evaluatoin
        with torch.no_grad():
            print("Epoch {} / {}".format(epoch + 1, epochs), end="  ")
            #evaluate train
            abs_diff = 0
            total = 0
            for X_prev_batch, X_today_batch, Y_batch in trainloader:
                output = model(X_prev_batch, X_today_batch)
                y_pred = output.squeeze()
                total += len(y_pred)
                abs_diff += torch.sum(abs(y_pred - Y_batch)).item()
            print("Train_acc = {}".format(abs_diff / total), end="  ")
            #evaluate test
            abs_diff = 0
            total = 0
            for X_prev_batch, X_today_batch, Y_batch in testloader:
                output = model(X_prev_batch, X_today_batch)
                y_pred = torch.argmax(output, dim=1)
                total += len(y_pred)
                abs_diff += torch.sum(abs(y_pred - Y_batch)).item()
            print("Test_acc = {}".format(abs_diff / total))
