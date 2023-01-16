# Binary Search with Duplicates

"""
Find the index of the first occurrence of a key in a sorted array.
"""


# iterative
def binary_search_first_dup(sorted_list, key):

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

    # checking if the element to the left of the current element has the same value
    left_element_index = mid_index - 1
    while key == sorted_list[left_element_index]:
        mid_index = left_element_index
        left_element_index = mid_index - 1

    return mid_index


# modify the function from c1_binary_search
def binary_search_iterative(number_list, key):

    low = 0
    high = len(number_list) - 1

    while low <= high:
        mid = int(low + (high - low) // 2)

        if number_list[mid] == key:

            while key == number_list[mid - 1]:
                mid -= 1

            return mid

        elif number_list[mid] > key:
            high = mid - 1

        else:
            low = mid + 1

    # if key is not present in the list, return -1
    return -1


# further modify the function from c1_binary_search
def binary_search_iterative_further(number_list, key):

    low = 0
    high = len(number_list) - 1

    start_index = -1

    while low <= high:
        mid = int(low + (high - low) // 2)

        if number_list[mid] == key:

            start_index = mid

            high = mid - 1

        elif number_list[mid] > key:
            high = mid - 1

        else:
            low = mid + 1

    # if key is not present in the list, return -1
    return start_index


if __name__ == '__main__':
    input1 = int(input())
    input2_list = [int(i) for i in input().split()]
    input3 = int(input())
    input4_list = [int(i) for i in input().split()]

    output_list = []

    for num in input4_list:
        output_list.append(binary_search_iterative_further(input2_list, num))

    print(*output_list)
