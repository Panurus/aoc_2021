from aoc import read_data
import pandas as pd
import numpy as np
from time import sleep

data = [list(x) for x in read_data(11, str)]

data = pd.DataFrame([[int(x) for x in line]for line in data])

def surrounding_octos(octo_coords):
    next_cells = []
    row = octo_coords[0]
    col = octo_coords[1]
    if (row == 0) and (col == 0):
        next_cells = next_cells + [(row+1, col), (row, col+1), (row+1, col+1)]
    elif (row == 9) and (col == 9):
        next_cells = next_cells + [(row-1, col), (row, col-1), (row-1, col-1)]
    elif (row == 0) and (col == 9):
        next_cells = next_cells + [(row+1, col), (row, col-1), (row+1, col-1)]
    elif (row == 9) and (col == 0):
        next_cells = next_cells + [(row-1, col), (row, col+1), (row-1, col+1)]
    elif row == 0:
        next_cells = next_cells + [(row+1, col), (row, col+1), (row, col-1), (row+1, col+1), (row+1, col-1)]
    elif row == 9:
        next_cells = next_cells + [(row-1, col), (row, col+1), (row, col-1), (row-1, col-1), (row-1, col+1)]
    elif col == 0:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col+1), (row+1, col+1), (row-1, col+1)]
    elif col == 9:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col-1), (row+1, col-1), (row-1, col-1)]
    else:
        next_cells = next_cells + [(row+1, col), (row-1, col), (row, col-1), (row, col+1), (row+1, col-1), (row-1, col-1), (row+1, col+1), (row-1, col+1)]

    return next_cells


# 
    return data

def energy_increase(data):
    return data+1

def get_flash_coords(data):

    rows, cols = np.where(data.apply(lambda x: x>9))

    return list(zip(rows,cols))


def flash(flash_coords, data):
    flashes = 0
    while len(flash_coords)>0:
        for flasher in flash_coords:
            neighbours = surrounding_octos(flasher)
            for neighbour in neighbours:
                if data.iloc[neighbour] != 0:
                    data.iloc[neighbour] = data.iloc[neighbour]+1
                else:
                    pass
            data.iloc[flasher] = 0
            flash_coords = get_flash_coords(data)
            flashes+=1

    return data, flashes

def step(data, flashes):
    data = energy_increase(data)
    flash_coords = get_flash_coords(data)
    data, new_flashes = flash(flash_coords,data)
    flashes += new_flashes

    return data, flashes

def parta(data):
    flashes = 0
    step_counter = 0
    while step_counter != 100:
        data, flashes = step(data, flashes)
        step_counter +=1

    return flashes

def parta(data):
    flashes = 0
    step_counter = 0
    while step_counter != 100:
        data, flashes = step(data, flashes)
        step_counter +=1

    return flashes

def partb(data):
    flashes = 0
    step_counter = 0
    ref = 10
    while not data.apply(lambda x: x == ref).all(axis = None):
        data, flashes = step(data, flashes)
        step_counter +=1

        ref = data.iloc[0,0]

    return step_counter

print(f"Day 11a = {parta(data)}")
print(f"Day 11b = {partb(data)}")
# 9808 too high
# 1538 too low