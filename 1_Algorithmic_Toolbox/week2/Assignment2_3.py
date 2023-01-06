# Huge Fibonacci Number

"""
constraint:
0 <= n <= 10^14
2 <= n <= 10^3
"""


# check if there is a pattern of numbers in the num_list
def check_list_pattern(num_list):
    first_half = num_list[:len(num_list) // 2]
    second_half = num_list[len(num_list) // 2:]

    if first_half == second_half:
        return first_half

    return None


# return the remainder of (Fib(nth_input) mod modulo)
def fib_listing_3(nth_input, modulo):
    fib_list = [0, 1]

    for i in range(nth_input + 1):

        if i >= 2:
            update_fib = fib_list[-1] + fib_list[-2]

            if update_fib >= modulo:
                update_fib -= modulo

            fib_list.append(update_fib)

        if len(fib_list) % 2 == 0:
            pattern_result = check_list_pattern(fib_list)

            if pattern_result is not None:
                return pattern_result[nth_input % len(pattern_result)]

    return fib_list[-1] % modulo


if __name__ == '__main__':
    two_inputs = input().split()
    input1 = int(two_inputs[0])
    input2 = int(two_inputs[1])
    print(fib_listing_3(input1, input2))
