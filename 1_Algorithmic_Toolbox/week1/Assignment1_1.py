
def add_two_digits(two_digits):

    a = int(two_digits[0])
    b = int(two_digits[1])

    result = a + b

    return result


if __name__ == '__main__':
    two_input_digits = input().split()
    print(add_two_digits(two_input_digits))

