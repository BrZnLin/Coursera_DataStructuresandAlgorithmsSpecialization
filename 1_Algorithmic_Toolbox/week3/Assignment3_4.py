# Maximum Advertisement Revenue

"""
Find the maximum dot product of two sequences of numbers.
"""


def max_revenue(n, price_list, clicks_list):

    revenue = 0

    for i in range(n):
        ith_high_price = max(price_list)
        ith_high_clicks = max(clicks_list)

        price_list.remove(ith_high_price)
        clicks_list.remove(ith_high_clicks)

        revenue += ith_high_price * ith_high_clicks

    return int(revenue)


if __name__ == '__main__':
    input1 = int(input())
    input2 = [int(i) for i in input().split()]
    input3 = [int(i) for i in input().split()]
    print(max_revenue(input1, input2, input3))
