# Majority Element

"""
Check whether a given sequence of numbers contains an element
that appears more than half of the times (n).
"""


def major_search_iter(n, un_sorted_list):

    unique_ele_list = []
    unique_ele_count = []
    for ele in un_sorted_list:
        if ele not in unique_ele_list:
            unique_ele_list.append(ele)
            unique_ele_count.append(1)
        else:
            ele_index = unique_ele_list.index(ele)
            unique_ele_count[ele_index] += 1

            if unique_ele_count[ele_index] > n / 2:
                return 1

    return 0


if __name__ == '__main__':
    input1 = int(input())
    input2_list = [int(i) for i in input().split()]

    print(major_search_iter(input1, input2_list))
