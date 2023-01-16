# Number of Inversions

"""
Compute the number of inversions in a sequence of integers.
"""


def merge_sort(number_list):

    count = 0

    if len(number_list) == 1:
        return 0, number_list

    else:
        mid = int(len(number_list) / 2)

        (count_h1, sorted_h1) = merge_sort(number_list[:mid])
        (count_h2, sorted_h2) = merge_sort(number_list[mid:])

        (merge_result_count, merge_result_list) = merge(sorted_h1, sorted_h2)

        count += merge_result_count + count_h1 + count_h2

        return count, merge_result_list


def count_inverse(number_list):

    for i in range(len(number_list) - 1):
        if number_list[i] > number_list[i + 1]:

            sorted_h1 = number_list[:i + 1]
            sorted_h2 = merge_sort(number_list[i + 1:])

            return merge(sorted_h1, sorted_h2)

        # base case
        elif i + 1 == len(number_list) and number_list[i] <= number_list[i + 1]:
            return number_list


def merge(list_1, list_2):

    inverse_in_this_merge = 0
    sorted_list = []

    while len(list_1) + len(list_2) > 0:

        if len(list_1) == 0:
            sorted_list.append(list_2[0])
            list_2.pop(0)

        elif len(list_2) == 0:
            sorted_list.append(list_1[0])

            list_1.pop(0)

        elif list_1[0] <= list_2[0]:
            sorted_list.append(list_1[0])
            list_1.pop(0)

        else:
            sorted_list.append(list_2[0])
            list_2.pop(0)

            inverse_in_this_merge += len(list_1)

            for num_id in range(len(list_1) - 1):
                if list_1[num_id] == list_1[num_id + 1]:
                    inverse_in_this_merge -= 1
                else:
                    break

    return inverse_in_this_merge, sorted_list


if __name__ == '__main__':
    input1 = int(input())
    input_list = [int(i) for i in input().split()]
    # merge_sort(input_list)

    (inverse_count, sorted_list) = merge_sort(input_list)
    print(inverse_count)
