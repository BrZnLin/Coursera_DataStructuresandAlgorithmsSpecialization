# Fibonacci Number

"""
constraint:
0 <= n <= 45
"""


def fib_listing_1(nth_input):

    fib_list = [0]

    for i in range(nth_input + 1):
        if i == 1:
            fib_list.append(1)

        elif i >= 2:
            fib_list.append(fib_list[0] + fib_list[1])
            fib_list.pop(0)

    return fib_list[-1]


if __name__ == '__main__':
    input1 = int(input())
    print(fib_listing_1(input1))
