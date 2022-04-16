from data.factors import add_MA

def MA(df, short=5, long=10):
    #add factors data
    df = add_MA(df, d=short)
    df = add_MA(df, d=long)
    short_name = "MA%s" %short
    long_name = "MA%s" %long

    #drop rows with NA
    df.dropna(inplace=True)

    #if short term average larger than long term average
    df["sll"] = (df[short_name] > df[long_name])

    #get buy, sell and no move decisions
    for i in range(len(df)):
        if i == 0:
            df["action"] = "None"
            continue

        idx = df.index[i]
        prev_idx = df.index[i-1]
        if (df.loc[idx, "sll"] - df.loc[prev_idx, "sll"]) == 1:
            df.loc[idx, "action"] = "Buy"
        elif (df.loc[idx, "sll"] - df.loc[prev_idx, "sll"]) == -1:
            df.loc[idx, "action"] = "Sell"
        else:
            df.loc[idx, "action"] = "None"

    return df["action"]