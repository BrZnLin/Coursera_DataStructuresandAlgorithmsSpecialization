# Money Change Again

"""
Compute the minimum number of coins needed to change the given
value into coins with denominations 1, 3, and 4.
"""

import math


def money_change(money_to_change):

    coins_needed_list = [0]

    for m_value in range(1, money_to_change + 1):

        min_coins_needed = math.inf

        for j in range(len(coins_needed_list)):

            if j + 1 == m_value and coins_needed_list[j] + 1 < min_coins_needed:
                min_coins_needed = coins_needed_list[j] + 1

            if j + 3 == m_value and coins_needed_list[j] + 1 < min_coins_needed:
                min_coins_needed = coins_needed_list[j] + 1

            if j + 4 == m_value and coins_needed_list[j] + 1 < min_coins_needed:
                min_coins_needed = coins_needed_list[j] + 1

        coins_needed_list.append(min_coins_needed)

    return coins_needed_list[money_to_change]


if __name__ == '__main__':
    input1 = int(input())

    print(money_change(input1))
