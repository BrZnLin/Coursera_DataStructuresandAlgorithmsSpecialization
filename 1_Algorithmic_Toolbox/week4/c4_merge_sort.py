"""
Split into halves recursively,
and then sort
"""


def merge_sort(number_list):

    if len(number_list) == 1:
        return number_list

    m = int(len(number_list) / 2)
    num_list_1h = merge_sort(number_list[:m])
    num_list_2h = merge_sort(number_list[m:])

    sorted_num_list = merge(num_list_1h, num_list_2h)

    return sorted_num_list


def merge(first_half, second_half):

    merged_num_list = []

    while len(first_half) + len(second_half) > 0:

        if len(first_half) > 0 and len(second_half) > 0:

            if first_half[0] <= second_half[0]:
                merged_num_list.append(first_half[0])
                first_half.pop(0)
            else:
                merged_num_list.append(second_half[0])
                second_half.pop(0)

        elif len(first_half) == 0:
            merged_num_list.append(second_half[0])
            second_half.pop(0)

        elif len(second_half) == 0:
            merged_num_list.append(first_half[0])
            first_half.pop(0)

    return merged_num_list


if __name__ == '__main__':
    input_list = [int(i) for i in input().split()]
    print(*merge_sort(input_list))
