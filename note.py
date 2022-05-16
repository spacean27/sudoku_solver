import glob
import random

def select_level():
    level = input("Select a Level (easy,medium,hard): ")
    data_list = glob.glob(f'dataset/{level}/*.csv')
    data_path = random.choice(data_list)
    return data_path

print(select_level())