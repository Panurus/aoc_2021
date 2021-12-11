from aoc import read_data
import pandas as pd
import math

data = read_data(9,str)

data_split_str = [list(row) for row in data]
data_split = [[int(x) for x in row] for row in data]

df = pd.DataFrame(data_split)
risk_df = pd.DataFrame(0, index = range(100), columns=range(100))

# PART 1
# corners

# topleft
if (df.iloc[0,0] < df.iloc[0,1]) and (df.iloc[0,0] < df.iloc[1,0]):
    risk_df.iloc[0,0] = df.iloc[0,0] + 1
else:
    pass

# topright
if (df.iloc[0,99] < df.iloc[0,98]) and df.iloc[0,99] < df.iloc[1,99]:
    risk_df.iloc[0,0] = df.iloc[0,0] + 1
else:
    pass

# bottomleft
if (df.iloc[99,0] < df.iloc[98,0]) and df.iloc[99,0] < df.iloc[98,0]:
    risk_df.iloc[0,0] = df.iloc[0,0] + 1
else:
    pass

# edges

# top
for col in range(1,99):
    cell = df.iloc[0,col]
    bottom = df.iloc[1,col]
    left = df.iloc[0,col-1]
    right = df.iloc[0,col+1]
    if (cell<bottom) and (cell<left) and (cell<right):
        risk_df.iloc[0,col] = cell + 1
else:
    pass

# bottom
for col in range(1,99):
    cell = df.iloc[99,col]
    top = df.iloc[98,col]
    left = df.iloc[99,col-1]
    right = df.iloc[99,col+1]
    if (cell<top) and (cell<left) and (cell<right):
        risk_df.iloc[99,col] = cell + 1

# left
for row in range(1,99):
    cell = df.iloc[row,0]
    top = df.iloc[row-1,0]
    bottom = df.iloc[row+1,0]
    right = df.iloc[row,1]
    if (cell<bottom) and (cell<top) and (cell<right):
        risk_df.iloc[row,0] = cell + 1
else:
    pass

# right
for row in range(1,99):
    cell = df.iloc[row,99]
    top = df.iloc[row-1,99]
    bottom = df.iloc[row+1,99]
    left = df.iloc[row,98]
    if (cell<bottom) and (cell<top) and (cell<left):
        risk_df.iloc[row,99] = cell + 1
else:
    pass

# middle
for col in range(1,99):
    for row in range(1,99):
        cell = df.iloc[row,col]
        top = df.iloc[row-1,col]
        bottom = df.iloc[row+1,col]
        left = df.iloc[row,col-1]
        right = df.iloc[row,col+1]
        if (cell<bottom) and (cell<top) and (cell<left) and (cell<right):
            risk_df.iloc[row,col] = cell + 1       

answer1 = sum(risk_df.sum())

# PART 2 

# binary risk map

for col in range(100):
    for row in range(100):
        if risk_df.iloc[row,col] > 0:
            risk_df.iloc[row,col] = 1
        else:
            risk_df.iloc[row,col] = 0

#  get coords of low points as basin seeds
basins = []
for col in range(100):
    for row in range(100):
        if risk_df.iloc[row,col] == 1:
            basins.append((row,col))

# get basin boundaries as binary
basin_boundary_df = pd.DataFrame(0, index = range(100), columns=range(100))

for col in range(100):
    for row in range(100):
        if df.iloc[row,col] == 9:
            basin_boundary_df.iloc[row,col] = 1
        else:
            basin_boundary_df.iloc[row,col] = 0

def next_cell_coords(coord_pair):
    next_cells = []
    row = coord_pair[0]
    col = coord_pair[1]
    if (row == 0) and (col == 0):
        next_cells = next_cells + [(row+1, col), (row, col+1)]
    elif (row == 99) and (col == 99):
        next_cells = next_cells + [(row-1, col), (row, col-1)]
    elif (row == 0) and (col == 99):
        next_cells = next_cells + [(row+1, col), (row, col-1)]
    elif (row == 99) and (col == 0):
        next_cells = next_cells + [(row-1, col), (row, col+1)]
    elif row == 0:
        next_cells = next_cells + [(row+1, col), (row, col+1), (row, col-1)]
    elif row == 99:
        next_cells = next_cells + [(row-1, col), (row, col+1), (row, col-1)]
    elif col == 0:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col+1)]
    elif col == 99:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col-1)]
    else:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]

    return next_cells

def next_cell_no_highs(seed):
    return [coords for coords in next_cell_coords(seed) if basin_boundary_df.iloc[coords] == 0]

def basin_size(seed):
    seed = [seed]
    lena = 0
    lenb = 1
    basin = set(seed)
    while lena != lenb:
        basin.update(set(sum([next_cell_no_highs(x) for x in basin], [])))
        basin2 = set(sum([next_cell_no_highs(x) for x in basin], []))
        lena = len(basin)
        basin.update(basin2)
        lenb = len(basin)

    return lenb

basin_sizes = sorted([basin_size(coords) for coords in basins])

answer2 = math.prod(basin_sizes[-3:])


print(f"Day 9a = {answer1}")
print(f"Day 9b = {answer2}")
