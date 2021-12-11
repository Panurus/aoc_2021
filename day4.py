from aoc import read_data
import pandas as pd

def format_bingo_data(data):
    sequence_str = data.pop(0)
    sequence_list = sequence_str.split(',')
    sequence = [int(x) for x in sequence_list]

    boards = []

    start_rows = list(range(0,len(data),6))
    stop_rows = list(range(6,len(data)+1,6))

    for i in range(len(start_rows)):
        boards.append(list(data[start_rows[i]:stop_rows[i]]))

    board_dfs = []

    for board in boards:
        board_df = pd.DataFrame(board).iloc[1:,:]
        board_df = board_df[0].str.split(expand = True)
        board_df = board_df.apply(pd.to_numeric)
        board_dfs.append(board_df)

    return sequence, board_dfs

def part_a(sequence:list, board_dfs: list) -> int:

    bingo = False

    print('\nLet game 1 commence!')

    for number in sequence:
        
        # print(number)
        for i in range(len(board_dfs)):
            board = board_dfs[i]
            if not bingo:
                board = board.replace({number:None})

                row_complete = []
                col_complete = []
                rows, columns = board.shape
                for row_n in range(rows):
                    row_complete.append(all(board.iloc[row_n,:].isnull()))

                for col_n in range(columns):
                    col_complete.append(all(board.iloc[:,col_n].isnull()))

                board_dfs[i] = board
                if any(row_complete) or any(col_complete):
                    bingo = True
                    print("\nThat's a bingo!")

                    print(f'\nwinning board: \n{board}\n')

                    winner = number
                    print(f'winning number = {winner}')

                    unmarked_sum = sum(board.sum())
                    print(f'unmarked_sum = {unmarked_sum}')
                    break
            else:
                break
        
        if bingo:
            break

    solution = int(unmarked_sum*winner)

    return(solution)


def part_b(sequence:list, board_dfs: list) -> int:

    n_boards = len(board_dfs)
    bingoed_boards = []
    all_bingoed = False
    print('\nLet game 2 commence!')

    for number in sequence:
        
        # print(number)
        for i in range(len(board_dfs)):
            board = board_dfs[i]
            if not all_bingoed:
                board = board.replace({number:None})

                row_complete = []
                col_complete = []
                rows, columns = board.shape
                for row_n in range(rows):
                    row_complete.append(all(board.iloc[row_n,:].isnull()))

                for col_n in range(columns):
                    col_complete.append(all(board.iloc[:,col_n].isnull()))

                board_dfs[i] = board
                if any(row_complete) or any(col_complete):
                    bingoed_boards.append(i)
                    n_winners = len(set(bingoed_boards))

                    if n_winners == n_boards:

                        print("Everyone has bingoed!\n")

                        print(f'last winning board: \n{board}\n')

                        winner = number
                        print(f'last winning number = {winner}')

                        unmarked_sum = sum(board.sum())
                        print(f'unmarked_sum = {unmarked_sum}\n')
                        all_bingoed = True
                        break
            else:
                break
        
        if all_bingoed:
            break

    solution = int(unmarked_sum*winner)

    return(solution)

def main():
    data = read_data(4, str)

    sequence, boards = format_bingo_data(data)

    parta_solution = part_a(sequence, boards)
    partb_solution = part_b(sequence, boards)

    print(f"Day 4a = {parta_solution}")
    print(f"Day 4b = {partb_solution}")

    return None
if __name__ == "__main__":
    main()
