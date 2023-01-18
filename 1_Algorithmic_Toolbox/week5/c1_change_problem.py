# Change Problem

import math


# Greedy algorithm can't solve with the optimal solution in some cases.
# Such as greedy_change(12, [10, 6, 1])
def greedy_change(money, coins):
    change_coins_count = 0

    for denomination in coins:
        if denomination <= money != 0:
            change_coins_count += money // denomination

            money = money % denomination

    return change_coins_count


# Recursive algorithm can solve with optimal solution,
# but can take very long time.
def recursive_change(money, coins):
    if money == 0:
        return 0

    min_num_coins = float('inf')

    for i in range(len(coins)):
        if money >= coins[i]:
            num_coins = recursive_change(money - coins[i], coins)

            if num_coins + 1 < min_num_coins:
                min_num_coins = num_coins + 1

    return min_num_coins


def dp_change(money, coins):

    # set base case for money = 0
    min_num_coin_list = [0]

    # for m from 1 to money
    for m in range(1, money + 1):
        min_num_coin_list.append(math.inf)

        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coin_list[m - coins[i]] + 1
                if num_coins < min_num_coin_list[m]:
                    min_num_coin_list[m] = num_coins

    return min_num_coin_list[money]


if __name__ == '__main__':
    input1 = int(input())
    input2_list = [int(i) for i in input().split()]

    print(dp_change(input1, input2_list))
