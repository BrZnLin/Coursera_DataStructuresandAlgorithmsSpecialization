# Money Change

"""
Compute the minimum number of coins needed to change
the given value into coins with denominations 1, 5, and 10.
"""


def money_change(change_amount):

    coin_1 = change_amount

    # if any combination of coin_1 can form a value of 5,
    # it is better to use the denomination of 5
    coin_5 = coin_1 // (5 / 1)
    # update coin_1
    coin_1 -= coin_5 * (5 / 1)

    # similarly,
    # if any combination of coin_5 can form a value of 10,
    # it is better to use the denomination of 10
    coin_10 = coin_5 // (10 / 5)
    # update coin_5
    coin_5 -= coin_10 * (10 / 5)

    return int(coin_1 + coin_5 + coin_10)


if __name__ == '__main__':
    input1 = int(input())
    print(money_change(input1))
