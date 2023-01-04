def maximum_pairwise_product(a_number, b_list):

    b_list_int = [int(i) for i in b_list]
    # a_list_int = [int(i) for i in b]

    b1 = max(b_list_int)
    b_list_int.remove(b1)

    b2 = max(b_list_int)

    result = b1 * b2

    return result


if __name__ == '__main__':
    input1 = input()
    input2 = input().split()
    print(maximum_pairwise_product(input1, input2))

# It takes 0.06 seconds to test in coursera
