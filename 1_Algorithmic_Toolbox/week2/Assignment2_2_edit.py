# Last Digit of Fibonacci Number

"""
constraint:
0 <= n <= 10^6
"""


def fib_listing_2(nth_input):

    second_last_fib = 0
    first_last_fib = 1

    if nth_input == 0:
        return second_last_fib

    for i in range(nth_input + 1):
        if i >= 2:
            update_fib = first_last_fib + second_last_fib
            second_last_fib = first_last_fib
            first_last_fib = update_fib

    return first_last_fib % 10


if __name__ == '__main__':
    input1 = int(input())
    print(fib_listing_2(input1))
