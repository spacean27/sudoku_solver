import pandas as pd
import numpy as np

# dataset
data = pd.read_csv("dataset/sample1.csv")
data = data.fillna(0)

data_list = data.values
data = pd.DataFrame(data_list)
data = data.astype("int")

pre_data = []
for row in range(0,9):
    for column in range(0,9):
        if data[row][column] == 0:
            continue
        else:
            value = data[row][column]
            pre_data.append(list([row+1, column+1, value]))

