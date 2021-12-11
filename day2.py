from aoc import read_data

def split_dirs(data):
    directions = []

    for instruction in data:
        direction = instruction[:-2]
        unit = int(instruction[-1])
        directions.append((direction, unit))

    return directions

def destination(route):
    horizontal = []
    depth = []

    for move in route:
        if move[0] == 'forward':
            horizontal.append(move[1])
        elif move[0] == 'down':
            depth.append(move[1])
        else:
            depth.append(-move[1])

    final_hor = sum(horizontal)
    final_dep = sum(depth)

    return final_hor*final_dep

def aim_destination(route):

    aim = 0
    horizontal = 0
    depth = 0

    for move in route:
        if move[0] == 'down':
            aim = aim+move[1]
        elif move[0] == 'up':
            aim = aim-move[1]
        elif move[0] == 'forward':
            horizontal = horizontal+move[1]
            depth = depth + aim*move[1]
        else:
            pass

    return depth*horizontal

def main():
    data = read_data(2, str)
    course = split_dirs(data)
    location = destination(course)
    new_location = aim_destination(course)

    print(f'Day 2a = {location}')
    print(f'Day 2b = {new_location}')

    return None

if __name__ == '__main__':
    main()

