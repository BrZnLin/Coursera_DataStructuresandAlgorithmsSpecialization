# Knapsack with repetitions

import math


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
