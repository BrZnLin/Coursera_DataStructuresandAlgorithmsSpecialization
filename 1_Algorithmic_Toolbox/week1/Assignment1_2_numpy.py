import numpy as np


def maximum_pairwise_product(a_number, b_list):
    b_list_int = list(map(int, b_list))
    # a_list_int = [int(i) for i in b]
    b_array_int_1 = np.unique(b_list_int)
    b1 = max(b_array_int_1)

    b_list_int.remove(b1)
    b_array_int_2 = np.unique(b_list_int)
    b2 = max(b_array_int_2)

    result = b1 * b2

    return result


if __name__ == '__main__':
    input1 = input()
    input2 = input().split()
    print(maximum_pairwise_product(input1, input2))

# It takes 0.38 seconds to test in coursera
