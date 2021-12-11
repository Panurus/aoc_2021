from aoc import read_data
import itertools

data = read_data(10, str)

openers = ['[', '{', '<', '(']
closers = [']', '}', '>', ')']
pairs = set([openers[i]+ closers[i] for i in range(len(openers))])
unmatched_pairs = set([x[0]+x[1] for x in list(itertools.product(openers, closers))]) - pairs


def parta(data):
    scores = {')':3,']':57,'}':1197,'>':25137}

    all_scores = []

    for row in data:
        while any(pair in row for pair in pairs):
            for pair in pairs:
                row = row.replace(pair, '')

        upair_pos = {}

        for upair in unmatched_pairs:
            if row.find(upair) > -1:
                upair_pos[upair] = row.find(upair)

        if len(upair_pos)>0:
            score = scores[min(upair_pos, key = upair_pos.get)[-1]]
        else:
            score = 0

        all_scores.append(score)
        
    return sum(all_scores)

def partb(data):

    points = {')':1, ']':2, '}':3, '>':4}

    reduced_reversed = []

    for row in data:
        while any(pair in row for pair in pairs):
            for pair in pairs:
                row = row.replace(pair, '')

        if not any(pair in row for pair in unmatched_pairs):
            reduced_reversed.append(row[::-1])

    closing_string = []
    for string in reduced_reversed:
        for i in range(len(openers)):
            string = string.replace(openers[i], closers[i])

        closing_string.append(string)

    string_scores = []
    for string_ in closing_string:
        score = 0
        for char in string_:
            score = score*5
            score += points[char]

        string_scores.append(score)

    string_scores = sorted(string_scores)

    return string_scores[int((len(string_scores) -1)/2)] 
    
print(f"Day 10a = {parta(data)}")
print(f"Day 10b = {partb(data)}")


# 21215586666 too high
# 3987832722 too high