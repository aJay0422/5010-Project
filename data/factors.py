import pandas as pd
import numpy as np

def add_MA(df, col="Open", d=5):
    df["MA%s" % d] = df[col].rolling(d).mean()