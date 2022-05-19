import pandas as pd
import numpy as np
import argparse
import sys
import glob
import random

def select_level(level):
    return level


def select_problem(level):
    """
    Select level and choose a prblem randomly.
    """
    data_list = glob.glob(f'dataset/{level}/*.csv')
    data_path = random.choice(data_list)
    return data_path

def make_problem():
    row1 = list(input("row1: "))
    row2 = list(input("row2: "))
    row3 = list(input("row3: "))
    row4 = list(input("row4: "))
    row5 = list(input("row5: "))
    row6 = list(input("row6: "))
    row7 = list(input("row7: "))
    row8 = list(input("row8: "))
    row9 = list(input("row9: "))
    rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    row_data = pd.DataFrame(rows)
    data = row_data.to_csv("dataset/user/user1.csv",index=False)

def preprocess_data_to_display(data_path):
    """
    Converts a problem to a table data to show it on interface.
    Args data_path(str): path 
    Return data_to_display(pd.DataFrame): DataFrame
    """
    problem = pd.read_csv(data_path)
    problem = problem.fillna(0)
    problem = problem.values
    problem = problem.astype("int")
    return problem

def preprocess_data_to_compute(problem):
    data_to_compute = []
    for row in range(0,9):
        for column in range(0,9):
            if problem[row][column] == 0:
                continue
            else:
                value = problem[row][column]
                data_to_compute.append(list([row+1, column+1, value]))
    return data_to_compute

def main(level):
    """
    data_to_display: just to display.
    data_to_compute: This is needed to solve a problem.
    """
    level = select_level(level)
    if level == "user":
        make_problem()
    data_path = select_problem(level)
    problem = preprocess_data_to_display(data_path)
    data_to_compute = preprocess_data_to_compute(problem)
    return problem, data_to_compute

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select Level.")
    parser.add_argument("--level", default="easy", help="select level (easy, medium, hard)")
    args = parser.parse_args()
    level = args.level
    problem, data_to_compute = main(level)
    print("Problem_to_solve: ", problem, sep="\n")
    print("data_to_compute: ", data_to_compute, sep="\n")
