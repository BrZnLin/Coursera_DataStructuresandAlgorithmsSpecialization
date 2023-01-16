"""
This sorting algorithm is dependent on data size,
not dependent on data sequence type
"""


def selection_sort(number_list):

    for i in range(len(number_list)):
        min_index = i

        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[min_index]:
                min_index = j

        median_for_swap = number_list[i]
        number_list[i] = number_list[min_index]
        number_list[min_index] = median_for_swap

    return number_list


if __name__ == '__main__':
    input_list = [int(i) for i in input().split()]
    print(*selection_sort(input_list))
