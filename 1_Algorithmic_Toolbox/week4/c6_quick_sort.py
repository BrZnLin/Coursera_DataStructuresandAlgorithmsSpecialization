"""
Runtime
n ^ 2 on average
n log(n) on worst case for few unique value list

Other modifications like tail recursion elimination was introduced in Final remarks
"""


def quick_sort(number_list, l, r):

    if l >= r:
        return

    m = partition(number_list, l, r)
    # so that number_list[m] is in its final position

    quick_sort(number_list, l, m - 1)
    quick_sort(number_list, m + 1, r)


def partition(number_list, l, r):

    # define a pivot x
    x = number_list[l]

    # j will record the location that the pivot value x should be at
    # everytime an element with value smaller than pivot value x is found, j += 1
    j = l

    # search from the second element to last element in this list
    for i in range(l + 1, r + 1):

        if number_list[i] <= x:
            j = j + 1

            # swapping
            (number_list[i], number_list[j]) = (number_list[j], number_list[i])
        # so that
        # number_list[l+1:j+1] <= x
        # number_list[j+1:i+1] > x

    (number_list[j], number_list[l]) = (number_list[l], number_list[j])

    return j


if __name__ == '__main__':
    input_list = [int(i) for i in input().split()]
    quick_sort(input_list, 0, len(input_list) - 1)
    print(*input_list)
