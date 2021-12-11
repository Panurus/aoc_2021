from aoc import read_data

def calc_fuel(start, position):
    if start != position:
        fuel = abs(start - position)
    else:
        fuel = 0
    return fuel

def fuel_map(positions):
    max_moves = max(positions)
    moves = list(range(1,max_moves+1))
    fuel_map_ = {n_moves: [sum(moves[0:x]) for x in range(0, n_moves+1)][-1] for n_moves in moves}

    return fuel_map_

def calc_fuel_2(start, position, fuel_map):
    if start != position:
        moves = abs(start - position)
        fuel = fuel_map[moves]
    else:
        fuel = 0
    return fuel

if __name__ == "__main__":
    data = read_data(7,str)
    data = [int(x) for x in data[0].split(',')]
    positions = set(data)
    fuel_ = [sum(calc_fuel(x, y) for x in data) for y in positions]
    solution1 = min(fuel_)

    fuel_map_ = fuel_map(positions)
    fuel_2 = [sum(calc_fuel_2(x, y, fuel_map_) for x in data) for y in positions]
    solution2 = min(fuel_2)


    print(f"Day 7a = {solution1}")
    print(f"Day 7b = {solution2}")

    