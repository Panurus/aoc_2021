from aoc import read_data

def count_fish(n_days, data):

    d = [0]*9
    
    for fish in data:
        d[fish]+=1

    for day in range(n_days):
        it68 = (d[7]+d[0],d[0])
        for it in range(8):
            d[it] = d[it+1]
        d[6], d[8] = it68

    return sum(d)

def main():
    data_raw = [int(x) for x  in read_data(6, str)[0].split(',')]

    solution_6a = count_fish(80, data_raw)
    solution_6b = count_fish(256, data_raw)

    print(f"Day 6a = {solution_6a}")
    print(f"Day 6b = {solution_6b}")

if __name__ == "__main__":
    main()


    


