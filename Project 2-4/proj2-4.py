import sys
import numpy
import csv

# Class: CPSC 475
# Team Member 1: James Stevenson
# Submitted By: James Stevenson
# GU Username: jstevenson4
# File Name: proj2-4.py
# Description: Program finds minimum edit distance between two strings
# To Execute: python3 proj2-4.py <source string> <target string>

up_arrow = "\u2191"
left_arrow = "\u2190"
diagonal_left_arrow = "\u2196"


"""
Creates two tables, one for the minimum distance calculations based on the algorithm provided
    and the other for the pathing to follow
Pre: source and target are strings
Post: distance table and path tables are returned
"""
def create_tables(n, m, source, target):
    # dist_table is len(source+1) by len(target+1) 2D list
    #   filled with zeroes
    dist_table = numpy.zeros((n + 1, m + 1), dtype=int)

    # path_table is storing the first character of each
    # process, initialized to x with the letters meaning it is/they are a valid path
    path_table = [["" for col in range(0, m + 1)] for row in range(0, n + 1)]

    # initializing first column of path_table
    for row in range(1, n + 1):
        path_table[row][0] = up_arrow

    # initializing first row of path_table
    for col in range(1, m + 1):
        path_table[0][col] = left_arrow

    for row in range(1, n + 1):
        # deletion cost = 1
        dist_table[row, 0] = dist_table[row - 1, 0] + 1

    for col in range(1, m + 1):
        # insertion cost = 1
        dist_table[0, col] = dist_table[0, col - 1] + 1

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            # deletion cost = 1
            del_val = dist_table[row-1, col] + 1
            sub_val = dist_table[row-1, col-1] + sub_cost(source[row - 1], target[col - 1])
            # insertion cost = 1
            ins_val = dist_table[row, col-1] + 1

            # set minimum computation value
            dist_table[row, col] = min(del_val, sub_val, ins_val)

            # dictionary with each letter corresponding to its value for deletion, sub, and insert
            d = {diagonal_left_arrow: sub_val, left_arrow: ins_val, up_arrow: del_val}

            # list of all computation first letters that share the minimum value
            min_letters = [letter for letter in d if d[letter] == dist_table[row, col]]

            for letter in min_letters:
                path_table[row][col] += letter

    return dist_table, path_table


"""
Calculates the cost of substituting two characters
Pre: source and target are characters
Post: returns 2 if the characters are different, 0 otherwise
"""
def sub_cost(source, target):
    if source != target:
        return 2
    else:
        return 0


"""
Displays alignment as expected
Pre: arguments are passed in as defined and expected
Post: prints alignment to terminal
"""
def display_alignment(path_table, n, m, source, target):
    source_str = ''
    target_str = ''
    operation_str = ''
    cost_str = ''

    source_index = n - 1
    target_index = m - 1

    while m > 0 or n > 0:
        if left_arrow in path_table[n][m]:
            source_str += ' *'
            target_str += ' ' + target[target_index]
            target_index -= 1
            operation_str += ' I'
            cost_str += ' 1'
            m -= 1
        elif up_arrow in path_table[n][m]:
            target_str += ' *'
            source_str += ' ' + source[source_index]
            source_index -= 1
            operation_str += ' D'
            cost_str += ' 1'
            n -= 1
        else:
            if source[source_index] == target[target_index]:
                cost_str += ' 0'
                operation_str += '  '
            else:
                cost_str += ' 2'
                operation_str += ' S'
            source_str += ' ' + source[source_index]
            source_index -= 1
            target_str += ' ' + target[target_index]
            target_index -= 1
            n -= 1
            m -= 1

    print(source_str[::-1])
    print(target_str[::-1])
    print(operation_str[::-1])
    print(cost_str[::-1])
    print()


"""
Saves path to csv file for use in a table
Pre: arguments are passed in as defined and expected
Post: alignmnt.csv is filled with proper table values
"""
def print_path_to_csv(path_table, n, m, source, target):
    source_index = n - 1
    target_index = m - 1

    alignment_file = open('alignment.csv', mode='w')
    alignment_writer = csv.writer(alignment_file, delimiter=',')

    alignment_writer.writerow(['Current cell', 'Operation', 'Previous cell', 'Cost'])

    while m > 0 or n > 0:
        row = []
        row.append(f'({n},{m})')
        if left_arrow in path_table[n][m]:
            row.append(f'i(*,{target[target_index]})')
            target_index -= 1
            m -= 1
            cost = '1'
        elif up_arrow in path_table[n][m]:
            row.append(f'd({source[source_index]},*)')
            source_index -= 1
            n -= 1
            cost = '1'
        else:
            if source[source_index] == target[target_index]:
                cost = '0'
            else:
                cost = '2'
            row.append(f's({source[source_index]},{target[target_index]})')
            source_index -= 1
            target_index -= 1
            n -= 1
            m -= 1
        row.append(f'({n},{m})')
        row.append(cost)
        alignment_writer.writerow(row)

    alignment_writer.writerow(['(0,0)'])
    alignment_file.close()


def main():
    source = sys.argv[1]
    target = sys.argv[2]

    n = len(source)
    m = len(target)

    dist_table, path_table = create_tables(n, m, source, target)
    display_table = [[(path_table[row][col] + ' ' + str(dist_table[row, col])) for col in range(0, m + 1)] for row in range(0, n + 1)]

    print('Minimum edit distance:', str(dist_table[n, m]) + '\n')

    display_alignment(path_table, n, m, source, target)
    # print_path_to_csv(path_table, n, m, source, target)

    for row in display_table:
        print(row)


main()