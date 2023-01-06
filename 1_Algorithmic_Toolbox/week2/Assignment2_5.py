# Last Digit of the Partial Sum of Fibonacci Numbers

"""
constraint:
0 <= n <= 10^14
"""


# check if there is a pattern of numbers in the num_list
def check_list_pattern(num_list):
    first_half = num_list[:len(num_list) // 2]
    second_half = num_list[len(num_list) // 2:]

    if first_half == second_half:
        return first_half

    return None


def fib_listing_4(nth_input):

    fib_list = [0]
    sum_list = [0]

    for i in range(nth_input + 1):
        if i == 1:
            fib_list.append(1)
            sum_list.append(1)

        elif i >= 2:
            fib_list.append(fib_list[-1] + fib_list[-2])
            # fib_list.pop(0)
            # append only one digit
            sum_list.append((sum_list[-1] + fib_list[-1]) % 10)

        if len(sum_list) % 2 == 0:
            pattern_result = check_list_pattern(sum_list)

            if pattern_result is not None:
                return pattern_result[nth_input % len(pattern_result)]

    return sum_list[-1] % 10


def fib_listing_5(mth_subtract, nth_input):

    sum_fib = fib_listing_4(nth_input)
    to_subtract = fib_listing_4(mth_subtract - 1)

    if sum_fib >= to_subtract:
        return sum_fib - to_subtract

    else:
        return sum_fib - to_subtract + 10


if __name__ == '__main__':
    two_inputs = input().split()
    input1 = int(two_inputs[0])
    input2 = int(two_inputs[1])
    print(fib_listing_5(input1, input2))
