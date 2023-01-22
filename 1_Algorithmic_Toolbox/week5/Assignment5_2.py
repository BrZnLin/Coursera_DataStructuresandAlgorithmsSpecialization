# Primitive Calculator

"""
Find the minimum number of operations needed to get a positive integer n from 1
by using only three operations: add 1, multiply by 2, and multiply by 3.
"""

import math


# a slower approach for large target_num
def prime_calculator_slowest(target_num):

    calc_needed_list = [0, 0]
    j_record_list = [[0], [1]]

    for m_value in range(2, target_num + 1):

        min_calc_needed = math.inf
        j_to_record = 0

        for j in range(len(calc_needed_list)):

            if j + 1 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1
                j_to_record = j_record_list[j] + [m_value]

            if j * 2 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1
                j_to_record = j_record_list[j] + [m_value]

            if j * 3 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1
                j_to_record = j_record_list[j] + [m_value]

        calc_needed_list.append(min_calc_needed)
        j_record_list.append(j_to_record)

    return calc_needed_list[target_num], j_record_list[target_num]


# still slow
def prime_calculator_slow(target_num):

    calc_needed_list = [-1, 0]

    for m_value in range(2, target_num + 1):

        min_calc_needed = math.inf

        for j in range(len(calc_needed_list)):

            if j + 1 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1

            if j * 2 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1

            if j * 3 == m_value and calc_needed_list[j] + 1 < min_calc_needed:
                min_calc_needed = calc_needed_list[j] + 1

        calc_needed_list.append(min_calc_needed)

    return calc_needed_list


# still slow
def prime_calculator(target_num):

    calc_needed_list = [-1, 0]

    for m_value in range(2, target_num + 1):

        min_calc_needed = math.inf

        if m_value - 1 >= 1:
            min_calc_needed = min(calc_needed_list[m_value - 1] + 1, min_calc_needed)

        if m_value % 2 == 0:
            min_calc_needed = min(calc_needed_list[int(m_value / 2)] + 1, min_calc_needed)

        if m_value % 3 == 0:
            min_calc_needed = min(calc_needed_list[int(m_value / 3)] + 1, min_calc_needed)

        calc_needed_list.append(min_calc_needed)

    return calc_needed_list


def find_cal_path(target_num):

    all_calc_list = prime_calculator(target_num)
    calc_needed = all_calc_list[target_num]

    calc_record_list = [target_num]

    while calc_needed > 0:
        for j in range(1, target_num):
            if all_calc_list[j] == calc_needed - 1 and (target_num / j == 3
                                                        or target_num / j == 2
                                                        or target_num - j == 1):
                calc_needed = all_calc_list[j]
                target_num = j

                calc_record_list.insert(0, j)

                break

    return calc_record_list


if __name__ == '__main__':
    input1 = int(input())

    # print(prime_calculator(input1))
    track_list = find_cal_path(input1)

    print(len(track_list) - 1)
    print(*track_list)
