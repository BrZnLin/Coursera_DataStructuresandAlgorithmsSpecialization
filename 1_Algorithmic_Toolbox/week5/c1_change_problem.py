# Change Problem

# further modify the function from c1_binary_search
def change_problem(number_list, key):

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
