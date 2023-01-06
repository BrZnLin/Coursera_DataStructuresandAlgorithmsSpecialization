# Last Digit of the Sum of Squares of Fibonacci Numbers

def GCD_7(gcd_input_a, gcd_input_b):

    a_remainder = gcd_input_a % gcd_input_b

    if a_remainder == 0:
        return gcd_input_b
    else:
        return GCD_7(gcd_input_b, a_remainder)


def LCM_8(input_a, input_b):

    gcd_num = GCD_7(input_a, input_b)

    return int(input_a * input_b / gcd_num)


if __name__ == '__main__':
    two_inputs = input().split()
    input1 = int(two_inputs[0])
    input2 = int(two_inputs[1])
    print(LCM_8(input1, input2))
