from aoc import read_data


data = read_data(8, str)

def parta(data):

    output = [x.split('| ')[1] for x in data]

    digits = [y.split(' ') for y in output]

    digit_lens = [[len(a) for a in z] for z in digits]

    all_digit_lens = [item for sublist in digit_lens for item in sublist]

    unique = [2,3,4,7]

    easy = [num for num in all_digit_lens if num in unique]

    return len(easy)


def decode_easy(code_list, d_map):
    decoded = {}
    for code in code_list:
        code = ''.join(sorted(code))
        for length in d_map:
            if len(code) == length:
                decoded[code] = d_map[length]
            else:
                pass
    
    return decoded

def six_logic(code_dict):

    for code, number in code_dict.items():
        if number == 4:
            four = code
        elif number == 1:
            one = code
        else:
            pass

    for code in code_dict:
        if len(code) == 6:
            if set(four).issubset(set(code)):
                code_dict[code] = 9
            elif set(one).issubset(set(code)):
                code_dict[code] = 0
            else:
                code_dict[code] = 6

    return code_dict

def five_logic(code_dict):

    for code, number in code_dict.items():
        if number == 7:
            seven = code
        elif number == 6:
            six = code
        else:
            pass

    for code in code_dict:
        if len(code) == 5:
            if set(seven).issubset(set(code)):
                code_dict[code] = 3
            elif set(code).issubset(set(six)):
                code_dict[code] = 5
            else:
                code_dict[code] = 2

    assert(len(code_dict.values()) == len(set(code_dict.values()))), 'There are duplicate values here'
    return code_dict

def partb(data):

    digit_map = {2: 1, 3: 7, 4: 4, 5:[2,3,5], 6: [0,6,9], 7:8}

    output_all = [x.split(' | ') for x in data]

    output_all_split = [[z.split(' ') for z in y] for y in output_all]

    final = []

    for display in output_all_split:
        a = display.copy()

        b = decode_easy(a[0], digit_map)
            
        c = six_logic(b)

        a.append(five_logic(c))

        final.append([a[2][''.join(sorted(code))] for code in a[1]])

    final_list = [int(''.join([str(int) for int in x])) for x in final]
            
    return sum(final_list)

if __name__ == "__main__":
    print(f"Day 8a = {parta(data)}")
    print(f"Day 8b = {partb(data)}")