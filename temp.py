import matplotlib.pyplot as plt
import pandas as pd
for i in range(1):
    #i.replace("\n", "")
    print(i)
    with pd.HDFStore("./data/etf.hdf5") as store:
        try:
            df = store.get("classidx_"+ str(1577))
        except:
            pass
        else:
            print(i)
df = df.reset_index()
df3 = pd.DataFrame({})
for k in range(50):
    i = 0
    while i < 100000:
        i = 500*i + k
        inf, sup = float(df["現在値"][i])* 0.8,float(df["現在値"][i])* 1.2
        df2 = df.loc[i]
        df2 = pd.DataFrame.join(df2,pd.DataFrame({"":"", "下限":[inf],"上限":[sup]}))
        df3 = df3.append(df2)
        print(df3)
        if i > 100000:
            break
