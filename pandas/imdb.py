import pandas as pd
import numpy as np

df=pd.read_csv("pandas/datasets/imdb.csv")
print(round(df["Rating"].mean(),2))
print("bombo")