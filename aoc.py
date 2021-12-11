def read_data(day: int = 1, d_type: type = int) -> list:
    path = f'inputs/day{day}.txt'
    with open(path, encoding='utf8') as inp:
        data = inp.readlines()
    data = [d_type(line.rstrip()) for line in data]

    return data