# Number of Inversions

"""
Compute the number of inversions in a sequence of integers.
"""


def count_inverse(number_list):

    count = 0

    if len(number_list) == 0:
        return count

    id_min = number_list.index(min(number_list))

    if id_min != 0 and number_list[0] != min(number_list):
        (number_list[0], number_list[id_min]) = (number_list[id_min], number_list[0])
        count += 1

    return count + count_inverse(number_list[1:])


if __name__ == '__main__':
    # input1 = int(input())
    input_list = [int(i) for i in input().split()]
    # merge_sort(input_list)
    print(count_inverse(input_list))
