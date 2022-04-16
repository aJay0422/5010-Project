import pandas as pd
import numpy as np
from data.fetch_data import get_train_test
from sklearn.preprocessing import MinMaxScaler

def generate_data_by_n_days(series, n=20):
    """
    Get value of one statistics from the previous n days
    """
    df = pd.DataFrame()
    for i in range(n):
        df["c%d" % i] = series.tolist()[i : -(n - i)]

    return df

def make_dataset(n=20):
    X_train, X_test = get_train_test()
    X_train_scaled = (X_train - X_train.min()) / (X_train.max() - X_train.min())
    X_test = (X_test - X_train.min()) / (X_train.max() - X_train.min())
    X_train = X_train_scaled

    #get train
    X_train_prev_open = generate_data_by_n_days(X_train["Open"], n).to_numpy()
    X_train_prev_high = generate_data_by_n_days(X_train["High"], n).to_numpy()
    X_train_prev_low = generate_data_by_n_days(X_train["Low"], n).to_numpy()
    X_train_prev_close = generate_data_by_n_days(X_train["Close"], n).to_numpy()
    X_train_today_open = X_train["Open"].to_numpy()[n:]
    X_train_today_close = X_train["Close"].to_numpy()[n:]
    Y_train = X_train_today_close
    X_train_prev_all = np.stack([X_train_prev_open,
                                X_train_prev_high,
                                X_train_prev_low,
                                X_train_prev_close],
                                axis=2)

    #get test
    X_test_prev_open = generate_data_by_n_days(X_test["Open"], n).to_numpy()
    X_test_prev_high = generate_data_by_n_days(X_test["High"], n).to_numpy()
    X_test_prev_low = generate_data_by_n_days(X_test["Low"], n).to_numpy()
    X_test_prev_close = generate_data_by_n_days(X_test["Close"], n).to_numpy()
    X_test_today_open = X_test["Open"].to_numpy()[n:]
    X_test_today_close = X_test["Close"].to_numpy()[n:]
    Y_test = X_test_today_close
    X_test_prev_all = np.stack([X_test_prev_open,
                                 X_test_prev_high,
                                 X_test_prev_low,
                                 X_test_prev_close],
                                axis=2)


    return X_train_prev_all, X_train_today_open, Y_train, X_test_prev_all, X_test_today_open, Y_test

