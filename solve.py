import pulp
import itertools

import pandas as pd
import numpy as np


# Import dataset
from preprocess import data, pre_data
print("Prepared Data", data, "-----------------------------", sep="\n")

# Definite LP
prob = pulp.LpProblem("sudoku_solver", pulp.LpMinimize)

# Objective Function (Dummy)
# In this case, we do not need a specific objective function
prob += 0

# Variables
rows = [i for i in range(1,10)]
columns = [i for i in range(1,10)]
values = [i for i in range(1,10)]

cells = pulp.LpVariable.dicts("cell", (rows, columns, values),0,1,"Binary")

# Constraint
## (1) fulfills blans with prepared data
for coodinate in pre_data:
    row = coodinate[0]
    column = coodinate[1]
    value = coodinate[2]
    prob += cells[row][column][value] == 1


## (2) for cells
for row in rows:
    for column in columns:
        prob += pulp.lpSum([cells[row][column][value] for value in values]) == 1

## (3) for rows
for row in rows:
    for value in values:
        prob += pulp.lpSum([cells[row][column][value] for column in columns]) == 1

## (4) for columns
for column in columns:
    for value in values:
        prob += pulp.lpSum([cells[row][column][value] for row in rows]) == 1

## (5) for chunks
chunk1 = [[row, column] for row in [1,2,3] for column in [1,2,3]]
chunk2 = [[row, column] for row in [1,2,3] for column in [4,5,6]]
chunk3 = [[row, column] for row in [1,2,3] for column in [7,8,9]]
chunk4 = [[row, column] for row in [4,5,6] for column in [1,2,3]]
chunk5 = [[row, column] for row in [4,5,6] for column in [4,5,6]]
chunk6 = [[row, column] for row in [4,5,6] for column in [7,8,9]]
chunk7 = [[row, column] for row in [7,8,9] for column in [1,2,3]]
chunk8 = [[row, column] for row in [7,8,9] for column in [4,5,6]]
chunk9 = [[row, column] for row in [7,8,9] for column in [7,8,9]]

chunks = {"chunk1":chunk1, "chunk2":chunk2, "chunk3":chunk3,
          "chunk4":chunk4, "chunk5":chunk5, "chunk6":chunk6,
          "chunk7":chunk7, "chunk8":chunk8, "chunk9":chunk9,
          }
for chunk, coodinates in chunks.items():
    for value in values:
        prob += pulp.lpSum([cells[coodinate[0]][coodinate[1]][value] for coodinate in coodinates]) == 1

# solver
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# output
print("Result")
print("Status: ", pulp.LpStatus[status])

result = []
for row in rows:
    for column in columns:
        for value in values:
            cell = cells[row][column][value]
            if  cell.value() == 1.0:
                result.append(cell)
result_in_num = []
for i in result:
    i = int(str(i)[-1])
    result_in_num.append(i)

raw_table = []
for i in range(0,81,9):
    raw_table.append(list(result_in_num[i:i+9]))

table = pd.DataFrame(raw_table).T
print(table, "-----------------------------", sep="\n")