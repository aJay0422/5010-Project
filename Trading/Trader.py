from Trading.Strategies import *
import pandas as pd



class Trader:
    def __init__(self, cash=1000000):
        print("trader initialized")
        self.cash = 1000000
        self.share = 0

    def trade(self, history_data, strategy="MA", **kwargs):
        self.pf_record = history_data[["Open"]]

        if strategy == "MA":
            short = kwargs["short"]
            long = kwargs["long"]
            self.decisions = MA(history_data, short, long)

            for i in range(len(self.decisions)):
                date = self.decisions.index[i]
                if i == 0:
                    self.pf_record.loc[date, "cash"] = self.cash
                    self.pf_record.loc[date, "share"] = self.share
                    continue

                if self.decisions[date] == "None":
                    self.pf_record.loc[date, "cash"] = self.cash
                    self.pf_record.loc[date, "share"] = self.share
                    continue
                elif self.decisions[date] == "Buy":
                    price = history_data.loc[date, "Open"]
                    cash_out = self.cash
                    share_in = cash_out / price
                    self.cash -= cash_out
                    self.share += share_in
                    self.pf_record.loc[date, "cash"] = self.cash
                    self.pf_record.loc[date, "share"] = self.share
                elif self.decisions[date] == "Sell":
                    price = history_data.loc[date, "Open"]
                    share_out = self.share
                    cash_in = share_out * price
                    self.share -= share_out
                    self.cash += cash_in
                    self.pf_record.loc[date, "cash"] = self.cash
                    self.pf_record.loc[date, "share"] = self.share
                else:
                    print(date, "error")


