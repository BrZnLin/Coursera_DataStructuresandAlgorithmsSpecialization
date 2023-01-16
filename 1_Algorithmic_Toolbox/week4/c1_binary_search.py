# Present both recursive and iterative binary searching method

# omitting recursive function for now

def binary_search_iterative(number_list, key):

    # num_updates = 0       # just to see how many times mid is updated
    low = 0
    high = len(number_list) - 1

    while low < high:
        mid = int(low + (high - low) // 2)
        # num_updates += 1
        # print(num_updates)
        if number_list[mid] == key:
            return mid

        elif number_list[mid] > key:
            high = mid - 1

        else:
            low = mid + 1

    # if key is not present in the list, return the id with number just below key
    return low - 1


if __name__ == '__main__':
    input_list = [int(i) for i in input().split()]
    input3 = int(input())
    print(binary_search_iterative(input_list, input3))
