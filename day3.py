from aoc import read_data
import pandas as pd

def pivot_binary(data):
    
    len_binary = range(len(data[0]))
    datasplit = []

    for i in len_binary:
        element = []
        for code in data:
            element.append(int(code[i]))
        datasplit.append(element)


    return datasplit

def gamma(pivot: list) -> list:

    if len(pivot[0]) % 2 == 0:
        midpoint = len(pivot[0])/2
        majority = midpoint+1
    else:
        majority = int((len(pivot[0])/2)+0.5)
    
    majority_digit = []

    for element in pivot:
        if sum(element) == midpoint:
            majority_digit.append(1)
        elif sum(element) >= majority:
            majority_digit.append(1)
        else:
            majority_digit.append(0)

    return majority_digit

def epsilon(pivot: list) -> list:

    if len(pivot[0]) % 2 == 0:
        majority = (len(pivot[0])/2)+1
    else:
        majority = int((len(pivot[0])/2)+0.5)
    
    majority_digit = []

    for element in pivot:
        if sum(element) < majority:
            majority_digit.append(1)
        else:
            majority_digit.append(0)

    return majority_digit

def majority_to_decimal(majority_list: list):

    elements_ascending = majority_list.copy()
    elements_ascending.reverse()

    components = []
    if type(elements_ascending[0]) == int:
        for i in range(len(elements_ascending)):
            components.append(elements_ascending[i]*(2**i))
    elif type(elements_ascending[0]) == str:
        for i in range(len(elements_ascending[0])):
            components.append(int(elements_ascending[0][i])*(2**i))
        else:
            pass

    return sum(components)

def o2_gen_rating(data: list):

    df = pd.DataFrame(data, columns=['binaries'])

    split_df = df['binaries'].str.split(expand=True, pat = '').iloc[:, 1:-1]
    split_df = split_df.apply(pd.to_numeric)

    df = df.merge(split_df, left_index=True, right_index=True, how = 'inner')

    for i in range(1,13):

        n_rows, n_cols = df.shape

        n_ones = df.iloc[:,i].sum(axis = 0)
        n_zeroes = n_rows - n_ones

        if n_ones >= n_zeroes:
            keep = 1
        else:
            keep = 0

        df = df[df.iloc[:,i] == keep]

    binary_np = list(df.iloc[0,1:])

    binary = [int(x) for x in binary_np]
    decimal = majority_to_decimal(binary)

    
    return decimal


def co2_scrub_rating(data: list):

    df = pd.DataFrame(data, columns=['binaries'])

    split_df = df['binaries'].str.split(expand=True, pat = '').iloc[:, 1:-1]
    split_df = split_df.apply(pd.to_numeric)

    df = df.merge(split_df, left_index=True, right_index=True, how = 'inner')

    for i in range(1,13):

        n_rows, n_cols = df.shape
        if n_rows > 1:
            n_ones = df.iloc[:,i].sum(axis = 0)
            n_zeroes = n_rows - n_ones

            if n_ones < n_zeroes:
                keep = 1
            else:
                keep = 0

            df = df[df.iloc[:,i] == keep]

            n_rows = df.shape[0]
        else:
            break

    binary_np = list(df.iloc[0,1:])

    binary = [int(x) for x in binary_np]
    decimal = majority_to_decimal(binary)

    
    return decimal

def main():
    data = read_data(3, str)
    split = pivot_binary(data)
    gamma_val = gamma(split)
    epsilon_val = epsilon(split)
    decimal_gamma = majority_to_decimal(gamma_val)
    decimal_epsilon =majority_to_decimal(epsilon_val)
    power_consumption = decimal_gamma*decimal_epsilon

    gen_rating = o2_gen_rating(data)
    scrub_rating = co2_scrub_rating(data)
    life_support = gen_rating*scrub_rating

    print(f"Day 3a = {power_consumption}")
    print(f"Day 3b = {life_support}")

    return None

if __name__ == "__main__":
    main()
 