from Trading.Trader import Trader
from data.fetch_data import get_train_test

if __name__ == '__main__':
    X_train, X_test = get_train_test()
    trader1 = Trader()
    trader1.trade(X_train, short=5, long=10)