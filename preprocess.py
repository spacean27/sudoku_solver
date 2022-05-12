import pandas as pd
import numpy as np

# dataset
data = pd.read_csv("dataset/sample1.csv")
data = data.fillna(0)

data_list = data.values

print(data_list)