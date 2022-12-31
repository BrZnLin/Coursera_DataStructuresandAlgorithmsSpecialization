
def add_two_digits():

    two_input_digits = input().split()
    a = int(two_input_digits[0])
    b = int(two_input_digits[1])

    result = a + b

    return result


if __name__ == '__main__':
    print(add_two_digits())

