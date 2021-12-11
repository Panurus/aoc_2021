from aoc import read_data

def n_increase(data):
    data_shift = [0]+data
    data = data+[0]
    direction = []
    for i in range(len(data)):
        if data[i]>data_shift[i]:
            direction.append(1)
        else:
            direction.append(0)
    return sum(direction[1:-1])

def window_sum(data, n_sum=3):

    shifts = []
    for shift in range(n_sum):
        shifts.append(([0]*shift)+data+([0]*((n_sum-shift)-1)))

    window_vals = []
    for i in range(len(shifts[0])):
        window_element = []
        for j in range(len(shifts)):
            window_element.append(shifts[j][i])
            if len(window_element) == n_sum:
                window_vals.append(window_element)

    window_sums = []
    for window in window_vals:
        window_sums.append(sum(window))

    redundant = n_sum-1
    window_sums = window_sums[redundant:-(redundant)]
    return window_sums

def main():
    data = read_data(1)

    day1a = n_increase(data)
    day1b = n_increase(window_sum(data, 3))

    print(f'Day 1a = {day1a}')
    print(f'Day 1b = {day1b}')

    return None

if __name__ == "__main__":
    main()




