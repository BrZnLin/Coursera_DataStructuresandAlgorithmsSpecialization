# Maximum Number of Prizes

from math import sqrt

"""
Represent a positive integer as the sum of the maximum
number of pairwise distinct positive integers.
"""


def distinct_int_listing(one_positive_integer):

    # Use equation summation = (1 + n) * n / 2
    # which can be re-written as 0 = n**2 + n + (-2 * summation)
    # Set "summation = one_positive_integer" to find an approximate n
    # 0 = n**2 + n - 2 * one_positive_integer
    # n = (-1 + sqrt(1 ** 2 - 4 * 1 * (-2 * one_positive_integer))) / (2 * 1)

    n = (-1 + sqrt(1 ** 2 - 4 * 1 * (-2 * one_positive_integer))) / (2 * 1)

    # use int to floor the float number to the closest integer
    distinct_int_list = list(range(1, int(n+1)))

    while sum(distinct_int_list) < one_positive_integer:

        potential_append = distinct_int_list[-1] + 1

        if sum(distinct_int_list) + potential_append > one_positive_integer:
            distinct_int_list[-1] = one_positive_integer - sum(distinct_int_list[:-1])
        else:
            distinct_int_list.append(potential_append)

    return distinct_int_list


if __name__ == '__main__':
    input1 = int(input())
    integer_list = distinct_int_listing(input1)
    print(len(integer_list))
    print(*integer_list)
