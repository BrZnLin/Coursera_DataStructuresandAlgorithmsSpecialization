# Binary Search

"""
Note during coding
binary_search_recur can sometimes fail on its first run without any syntax issue
so,
binary_search_iter is also worked here
"""


def binary_search_recur(sorted_list, key):

    mid_index = int(len(sorted_list) / 2)

    if sorted_list[mid_index] == key:
        return mid_index
    elif sorted_list[mid_index] > key:
        return binary_search_recur(sorted_list[:mid_index], key)
    else:
        return mid_index + 1 + binary_search_recur(sorted_list[mid_index + 1:], key)


def binary_search_iter(sorted_list, key):

    left_index = 0
    right_index = len(sorted_list) - 1

    mid_index = int((left_index + right_index) / 2)

    while key != sorted_list[mid_index]:

        if left_index >= right_index:
            return -1

        if key < sorted_list[mid_index]:
            right_index = mid_index - 1

        else:
            left_index = mid_index + 1

        mid_index = int((left_index + right_index) / 2)

    return mid_index


if __name__ == '__main__':
    input1 = int(input())
    input2_list = [int(i) for i in input().split()]
    input3 = int(input())
    input4_list = [int(i) for i in input().split()]

    output_list = []

    for num in input4_list:
        output_list.append(binary_search_iter(input2_list, num))

    print(*output_list)
