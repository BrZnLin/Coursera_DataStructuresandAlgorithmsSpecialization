# Find the minimum number of operations needed to get a positive integer

import math


def dp_min_operation(target_number):

    # initial number = 1
    # it takes 0 operations to get 1
    operation_count_list = [0, 0]

    # for m from 2 to target number
    for number in range(2, target_number + 1):
        num_operations = math.inf

        # 3 types of operations
        if number % 3 == 0:
            num_operations = min(num_operations, operation_count_list[int(number / 3)] + 1)

        if number % 2 == 0:
            num_operations = min(num_operations, operation_count_list[int(number / 2)] + 1)

        if number - 1 > 0:
            num_operations = min(num_operations, operation_count_list[number - 1] + 1)

        operation_count_list.append(num_operations)

    print(operation_count_list)
    return operation_count_list[target_number]


if __name__ == '__main__':
    input1 = int(input())
    # input2_list = [int(i) for i in input().split()]

    print(dp_min_operation(input1))
