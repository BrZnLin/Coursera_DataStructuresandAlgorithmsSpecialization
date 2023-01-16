# Speeding-up RandomizedQuickSort

"""
Sort a given sequence of numbers (that may contain duplicates) using
a modification of RandomizedQuickSort that works in O(nlogn) expected time.
"""


import random


def quick_sort(number_list, l, r):

    if l >= r:
        return

    m = partition(number_list, l, r)
    # so that number_list[m] is in its final position

    quick_sort(number_list, l, m - 1)
    quick_sort(number_list, m + 1, r)


def partition(number_list, l, r):

    # define a pivot x
    # randomize the location for pivot
    random_id = random.randint(l, r)
    x = number_list[random_id]

    # j will record the location that the pivot value x should be at
    # everytime an element with value smaller than pivot value x is found, j += 1
    j = l

    # search from the second element to last element in this list
    for i in range(l, r + 1):

        # avoid swapping with pivot
        if i == random_id:
            continue

        if number_list[i] <= x:

            # avoid swapping with pivot
            if j == random_id:
                j += 1
            # swapping
            (number_list[i], number_list[j]) = (number_list[j], number_list[i])
            j += 1
        # so that
        # if there is no x present in number_list
        # number_list[l:j] <= x
        # number_list[j:i+1] > x

    if random_id >= j:
        (number_list[j], number_list[random_id]) = (number_list[random_id], number_list[j])
        return j
    else:
        (number_list[j - 1], number_list[random_id]) = (number_list[random_id], number_list[j - 1])
        return j - 1


if __name__ == '__main__':
    input1 = int(input())
    input_list = [int(i) for i in input().split()]
    quick_sort(input_list, 0, len(input_list) - 1)
    print(*input_list)
