import yfinance as yf


def get_train_test(ticker="^GSPC",
                   trainstart="2000-01-01", trainend="2018-12-31",
                   teststart="2017-01-01", testend="2019-12-31"):

    trainset = yf.download(ticker, start=trainstart, end=trainend)
    testset = yf.download(ticker, start=teststart, end=testend)
    alldata = trainset.append(testset)
    alldata = (alldata - alldata.min()) / (alldata.max() - alldata.min())

    return trainset, testset