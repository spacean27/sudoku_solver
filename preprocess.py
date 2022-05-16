import pandas as pd
import numpy as np
import sys
import glob
import random

def select_level(level):
    data_list = glob.glob(f'dataset/{level}/*.csv')
    data_path = random.choice(data_list)
    return data_path

def preprocess_data_to_display(data_path):
    data = pd.read_csv(data_path)
    data = data.fillna(0)
    data = data.values
    data = pd.DataFrame(data)
    data_to_display = data.astype("int")
    return data_to_display

def preprocess_data_to_compute(data):
    data_to_compute = []
    for row in range(0,9):
        for column in range(0,9):
            if data[row][column] == 0:
                continue
            else:
                value = data[row][column]
                data_to_compute.append(list([row+1, column+1, value]))
    return data_to_compute

def main(level):
    """
    data_to_display: just to display.
    data_to_compute: This is needed to solve a problem.
    """
    data_path = select_level(level)
    data_to_display = preprocess_data_to_display(data_path)
    data_to_compute = preprocess_data_to_compute(data_to_display)
    print("data_to_display: ", data_to_display, sep="\n")
    print("data_to_compute: ", data_to_compute, sep="\n")

if __name__ == "__main__":
    args = sys.argv
    level = args[1]
    main(level)