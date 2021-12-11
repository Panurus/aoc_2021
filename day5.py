from aoc import read_data
import pandas as pd
import re
import seaborn as sns

def format_vent_data(data: list) -> list:

    return [[int(y) for y in re.sub(" -> ", ",", x).split(',')] for x in data]

def get_grid(formatted_data: list):

    row_index = list(range(0,1001))
    col_index = list(range(0,1001))

    grid = pd.DataFrame(0, index = row_index, columns=col_index)

    return grid
 

def directional_lines(formatted_data: list) -> dict:
    direction = {}

    direction['vertical'] = [x for x in formatted_data if x[0] == x[2]]
    direction['horizontal'] = [x for x in formatted_data if x[1] == x[3]]
    direction['diagonal'] = [x for x in formatted_data if (x[1] != x[3]) and (x[0] != x[2])]

    return direction



def plot_vertical_lines(vectors: dict, grid: pd.DataFrame) -> pd.DataFrame:

    for v_line in vectors['vertical']:
        x_coord = v_line[0]
        y_start = min([v_line[1], v_line[3]])
        y_end = max([v_line[1], v_line[3]])
        y_coords = list(range(y_start, y_end+1))

        grid.loc[y_coords, x_coord] = grid.loc[y_coords, x_coord]+1

    return grid

def plot_horizontal_lines(vectors: dict, grid: pd.DataFrame) -> pd.DataFrame:

    for h_line in vectors['horizontal']:
        y_coord = h_line[1]
        x_start = min([h_line[0], h_line[2]])
        x_end = max([h_line[0], h_line[2]])
        x_coords = list(range(x_start, x_end+1))

        grid.loc[y_coord, x_coords] = grid.loc[y_coord, x_coords]+1

    return grid

def plot_diagonal_lines(vectors: dict, grid: pd.DataFrame) -> pd.DataFrame:

    coords = []
    for d_line in vectors['diagonal']:
        x1 = d_line[0]
        x2 = d_line[2]
        y1 = d_line[1]
        y2 = d_line[3]

        if (x1 < x2) and (y1 < y2):
            while x1 <= x2 and y1 <= y2:
                coords.append([x1,y1])
                x1 = x1+1
                y1 = y1+1
        elif (x1 > x2) and (y1 < y2):
            while x1 >= x2 and y1 <= y2:
                coords.append([x1,y1])
                x1 = x1-1
                y1 = y1+1

        elif (x1 < x2) and (y1 > y2):
            while x1 <= x2 and y1 >= y2:
                coords.append([x1,y1])
                x1 = x1+1
                y1 = y1-1

        elif (x1 > x2) and (y1 > y2):
             while x1 >= x2 and y1 >= y2:
                coords.append([x1,y1])
                x1 = x1-1
                y1 = y1-1           

    for pair in coords:
        grid.loc[pair[1], pair[0]] = grid.loc[pair[1], pair[0]]+1

    return grid

def binarise(grid: pd.DataFrame):
    
    for col in grid.columns:
        grid[col] = grid[col].apply(lambda x: 0 if x <= 1 else 1)

    return grid
    

def get_solution(inc_diag):
    data = read_data(5,str)
    data = format_vent_data(data)
    grid = get_grid(data)
    data = directional_lines(data)
    grid = plot_vertical_lines(data, grid)
    grid = plot_horizontal_lines(data, grid)
    if inc_diag:
        grid = plot_diagonal_lines(data, grid)
        grid = binarise(grid)
    else:
        grid = binarise(grid)
    

    return sum(grid.sum())

def main():
    solution_5a = get_solution(False)
    solution_5b = get_solution(True)

    print(f"Day 5b = {solution_5a}")
    print(f"Day 5b = {solution_5b}")

if __name__ == "__main__":
    main()
