# Last Digit of the Sum of Squares of Fibonacci Numbers

def GCD_7(input_a, input_b):

    a_remainder = input_a % input_b

    if a_remainder == 0:
        return input_b
    else:
        return GCD_7(input_b, a_remainder)


if __name__ == '__main__':
    two_inputs = input().split()
    input1 = int(two_inputs[0])
    input2 = int(two_inputs[1])
    print(GCD_7(input1, input2))
