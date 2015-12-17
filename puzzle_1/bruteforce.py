#!/usr/bin/env python

import clues

import re
from sets import Set
import row_combinations
import copy
from operator import itemgetter

QR_DIMENSION = 25

#all_bin_rows = ["".join(seq) for seq in itertools.product("01", repeat=QR_DIMENSION)]


def build_search_regex(search_seq):
    search_regex = "^0*"  # Our search regex

    for idx, val in enumerate(search_seq):
        search_regex = search_regex + "1{%i}0" % val

        if idx < len(search_seq) - 1:
            search_regex = search_regex + "+"
        else:
            search_regex = search_regex + "*$"

    return search_regex


# filter combinations based on input clues (i.e. the filled in blackbits)
# further filter combinations that wont work with rows / columns that are known
def filter_clue(row_arr, col_arr, clues):

    poss_col_combs_new = copy.deepcopy(col_arr)
    poss_row_combs_new = copy.deepcopy(row_arr)

    # Filter rows that dont match the filled in squares
    # possible combinations come from regex filtered binary seq
    for row_num, col_values in clues.iteritems():

        curr_poss_row_values = row_arr[row_num]

        for column_num, cell_value in col_values.iteritems():
            curr_poss_col_values = col_arr[column_num]

            for curr_comb in curr_poss_col_values:
                if str(curr_comb[row_num]) != str(cell_value):
                        if curr_comb in poss_col_combs_new[column_num]:
                            poss_col_combs_new[column_num].remove(curr_comb)

            for curr_comb in curr_poss_row_values:
                if str(curr_comb[column_num]) != str(cell_value):
                        if curr_comb in poss_row_combs_new[row_num]:
                            poss_row_combs_new[row_num].remove(curr_comb)

    # take rows with one combination and eliminate columns that dont fit
    known_rows = []
    for idx, curr_row in enumerate(poss_row_combs_new):
        if len(curr_row) == 1:
            known_rows.append(idx)

    poss_col_combs_mat = copy.deepcopy(poss_col_combs_new)
    for known_row_num in known_rows:
        known_row = list(list(poss_row_combs_new[known_row_num])[0])
        for col_num, exp_val in enumerate(known_row):
            poss_col_vals = poss_col_combs_new[col_num]
            for curr_col_bin_seq in list(poss_col_vals):
                if list(curr_col_bin_seq)[known_row_num] != exp_val:
                    if poss_col_combs_mat[col_num]:
                        da_set = poss_col_combs_mat[col_num]
                        if curr_col_bin_seq in da_set:
                            da_set.remove(curr_col_bin_seq)

    known_cols = []
    for idx, curr_col in enumerate(poss_col_combs_mat):
        if len(curr_col) == 1:
            known_cols.append(idx)

    poss_row_combs_mat = copy.deepcopy(poss_row_combs_new)
    for known_col_num in known_cols:
        known_col = list(list(poss_col_combs_mat[known_col_num])[0])
        for row_num, exp_val in enumerate(known_col):
            poss_row_vals = poss_row_combs_mat[row_num]
            for curr_row_bin_seq in list(poss_row_vals):
                if list(curr_row_bin_seq)[known_col_num] != exp_val:
                    if poss_row_combs_mat[row_num]:
                        da_set = poss_row_combs_mat[row_num]
                        if curr_row_bin_seq in da_set:
                            da_set.remove(curr_row_bin_seq)

    return (poss_row_combs_mat, poss_col_combs_mat)


def eliminate_combinations(row_arr, col_arr, print_it):
    row_sort_order = []
    for rid, row in enumerate(row_arr):
        row_sort_order.append([rid, len(row)])
    row_sort_order = sorted(row_sort_order, key=itemgetter(1))

    col_sort_order = []
    for cid, col in enumerate(col_arr):
        col_sort_order.append([cid, len(col)])
    col_sort_order = sorted(col_sort_order, key=itemgetter(1))

    new_row_arr = copy.deepcopy(row_arr)
    new_col_arr = copy.deepcopy(col_arr)

    for ri, r_sort_val in enumerate(row_sort_order):
        current_row_num = r_sort_val[0]
        current_row_combinations = r_sort_val[1]

        # For each row, look at each of the possible combinations.
        # Check to see if any of the combinations would eliminate all possible column combinations
        # Bin the row if so
        for r_combination_index, row_vals in enumerate(row_arr[current_row_num]):
            curr_row_vals = list(row_vals)

            for ci, c_sort_val in enumerate(col_sort_order):
                current_col_num = c_sort_val[0]
                current_col_combinations = c_sort_val[1]

                valid_combinations = current_col_combinations
                for c_combination_index, col_vals in enumerate(col_arr[current_col_num]):
                    curr_col_vals = list(col_vals)

                    if curr_row_vals[current_col_num] != curr_col_vals[current_row_num]:
                        valid_combinations = valid_combinations - 1

                    if valid_combinations == 0:
                        comb_matrix = new_row_arr[current_row_num]

                        if row_vals in comb_matrix:
                            comb_matrix.remove(row_vals)

    for ci, c_sort_val in enumerate(col_sort_order):
        current_col_num = c_sort_val[0]
        current_col_combinations = c_sort_val[1]

        for c_combination_index, col_vals in enumerate(col_arr[current_col_num]):
            curr_col_vals = list(col_vals)

            for ri, r_sort_val in enumerate(row_sort_order):
                current_row_num = r_sort_val[0]
                current_row_combinations = r_sort_val[1]

                valid_combinations = current_row_combinations
                for r_combination_index, row_vals in enumerate(row_arr[current_row_num]):
                    curr_row_vals = list(row_vals)

                    if curr_col_vals[current_row_num] != curr_row_vals[current_col_num]:
                        valid_combinations = valid_combinations - 1

                    if valid_combinations == 0:
                        comb_matrix = new_col_arr[current_col_num]

                        if col_vals in comb_matrix:
                            comb_matrix.remove(col_vals)

    if print_it:
        print "eliminate_combinations result:"
        for idx, curr_row in enumerate(new_row_arr):
            append = ""
            if len(curr_row) == 1: 
                append = str(next(iter(curr_row)))

            print "row %02d: %s" % (idx, str(len(curr_row)).rjust(4)) + " combinations (%i filtered) %s" % (len(row_arr[idx]) - len(curr_row), append)

        for idx, curr_col in enumerate(new_col_arr):
            append = ""
            if len(curr_col) == 1: 
                append = str(next(iter(curr_col)))

            print "col %02d: %s" % (idx, str(len(curr_col)).rjust(4)) + " combinations (%i filtered) %s" % (len(col_arr[idx]) - len(curr_col), append)  

        print 'qr data:'
        for idx, curr_row in enumerate(new_row_arr):
            append = ""
            if len(curr_row) == 1:
                append = str(next(iter(curr_row)))

            print ', '.join(list(append))

    return (new_row_arr, new_col_arr)


col_regex = []
for col_num, col_data in enumerate(clues.cols):
    col_regex.insert(col_num, build_search_regex(col_data))

row_regex = []
for row_num, row_data in enumerate(clues.rows):
    row_regex.insert(row_num, build_search_regex(row_data))

all_regex = col_regex + row_regex

# Pull out our possible solutions for each row/col
poss_col_combs = []
for col_num, col_regex in enumerate(col_regex):
    poss_combs = row_combinations.row_combs_dict.get(col_regex)

    poss_col_combs.insert(col_num, poss_combs)

poss_row_combs = []
for row_num, row_regex in enumerate(row_regex):
    poss_combs = row_combinations.row_combs_dict.get(row_regex)

    poss_row_combs.insert(row_num, poss_combs)



pass_result_tuple = filter_clue(poss_row_combs, poss_col_combs, clues.knowns)
r1 = eliminate_combinations(pass_result_tuple[0], pass_result_tuple[1], False)
r2 = eliminate_combinations(r1[0], r1[1], False)
r3 = eliminate_combinations(r2[0], r2[1], False)
r4 = eliminate_combinations(r3[0], r3[1], False)
r5 = eliminate_combinations(r4[0], r4[1], False)
r6 = eliminate_combinations(r5[0], r5[1], True)
