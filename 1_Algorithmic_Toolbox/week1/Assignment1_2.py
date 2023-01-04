def maximum_pairwise_product(a_number, b_list):

    b_list_int = [int(i) for i in b_list]

    b1 = 0
    b2 = 0
    for digit in b_list_int:
        if digit > b1:
            b2 = b1
            b1 = digit
        elif digit > b2:
            b2 = digit

    result = b1 * b2

    return result


if __name__ == '__main__':
    input1 = input()
    input2 = input().split()
    print(maximum_pairwise_product(input1, input2))

# It takes 0.07 seconds to test in coursera
