#!/usr/bin/env python

given_knowns = {3: {3: 1,  4: 1,  12: 1,  13: 1,  21: 1},
                8: {6: 1,  7: 1,  10: 1,  14: 1,  15: 1,  18: 1},
                16: {6: 1,  11: 1,  16: 1,  20: 1},
                21: {3: 1, 4: 1, 9: 1, 10: 1, 15: 1, 20: 1, 21: 1}}

predicted_knowns = {
    0: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 17: 0, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1},
    1: {0: 1, 6: 1, 7: 0, 17: 0, 18: 1, 24: 1},
    2: {0: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 0, 17: 0, 18: 1, 20: 1, 21: 1, 22: 1, 24: 1},
    3: {0: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 0, 17: 0, 18: 1, 20: 1, 21: 1, 22: 1, 24: 1},
    4: {0: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 0, 17: 0, 18: 1, 20: 1, 21: 1, 22: 1, 24: 1},
    5: {0: 1, 6: 1, 7: 0, 17: 0, 18: 1, 24: 1},
    6: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 10: 1, 12: 1, 14: 1, 16: 1, 17: 0, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1},
    7: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0},
    17: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0},
    18: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0},
    19: {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0},
    20: {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 0},
    21: {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 0},
    22: {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 1, 7: 0},
    23: {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0},
    24: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0},
}

knowns = given_knowns.copy()

for row_num, col_values in predicted_knowns.iteritems():
    given_row_nums = given_knowns.get(row_num)

    if given_row_nums:
        knowns[row_num].update(col_values)
    else:
        knowns[row_num] = col_values

cols = [[7, 2, 1, 1, 7],
        [1, 1, 2, 2, 1, 1],
        [1, 3, 1, 3, 1, 3, 1, 3, 1],
        [1, 3, 1, 1, 5, 1, 3, 1],
        [1, 3, 1, 1, 4, 1, 3, 1],
        [1, 1, 1, 2, 1, 1],
        [7, 1, 1, 1, 1, 1, 7],
        [1, 1, 3],
        [2, 1, 2, 1, 8, 2, 1],
        [2, 2, 1, 2, 1, 1, 1, 2],
        [1, 7, 3, 2, 1],
        [1, 2, 3, 1, 1, 1, 1, 1],
        [4, 1, 1, 2, 6],
        [3, 3, 1, 1, 1, 3, 1],
        [1, 2, 5, 2, 2],
        [2, 2, 1, 1, 1, 1, 1, 2, 1],
        [1, 3, 3, 2, 1, 8, 1],
        [6, 2, 1],
        [7, 1, 4, 1, 1, 3],
        [1, 1, 1, 1, 4],
        [1, 3, 1, 3, 7, 1],
        [1, 3, 1, 1, 1, 2, 1, 1, 4],
        [1, 3, 1, 4, 3, 3],
        [1, 1, 2, 2, 2, 6, 1],
        [7, 1, 3, 2, 1, 1]]

rows = [[7, 3, 1, 1, 7],
        [1, 1, 2, 2, 1, 1],
        [1, 3, 1, 3, 1, 1, 3, 1],
        [1, 3, 1, 1, 6, 1, 3, 1],
        [1, 3, 1, 5, 2, 1, 3, 1],
        [1, 1, 2, 1, 1],
        [7, 1, 1, 1, 1, 1, 7],
        [3, 3],
        [1, 2, 3, 1, 1, 3, 1, 1, 2],
        [1, 1, 3, 2, 1, 1],
        [4, 1, 4, 2, 1, 2],
        [1, 1, 1, 1, 1, 4, 1, 3],
        [2, 1, 1, 1, 2, 5],
        [3, 2, 2, 6, 3, 1],
        [1, 9, 1, 1, 2, 1],
        [2, 1, 2, 2, 3, 1],
        [3, 1, 1, 1, 1, 5, 1],
        [1, 2, 2, 5],
        [7, 1, 2, 1, 1, 1, 3],
        [1, 1, 2, 1, 2, 2, 1],
        [1, 3, 1, 4, 5, 1],
        [1, 3, 1, 3, 10, 2],
        [1, 3, 1, 1, 6, 6],
        [1, 1, 2, 1, 1, 2],
        [7, 2, 1, 2, 5]]
