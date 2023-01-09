# Maximum Salary

"""
Compile the largest number by concatenating the given numbers.
"""


def find_best_number(number_list):

    # record the first digits
    first_digit_list = []
    for number in number_list:
        if number // 100 != 0:
            first_digit_list.append(number // 100)
        elif number // 10 != 0:
            first_digit_list.append(number // 10)
        else:
            first_digit_list.append(number)

    # list the numbers with their first digit
    # as the largest first digit in the given numbers
    largest_first_digit = max(first_digit_list)
    candidate_number_list = []
    for jth_digit in range(len(first_digit_list)):
        if first_digit_list[jth_digit] == largest_first_digit:
            candidate_number_list.append(number_list[jth_digit])

    largest_second_digit = 0
    best_1_digit_number = 0
    best_2_digit_number = 0
    best_3_digit_number = 0

    for candidate in candidate_number_list:
        if len(str(candidate)) == 1:
            best_1_digit_number = candidate
        elif len(str(candidate)) == 2:
            if candidate // 10 >= largest_second_digit:
                largest_second_digit = candidate // 10
                best_2_digit_number = candidate
        else:
            best_3_digit_number = candidate

    if (best_1_digit_number >= largest_second_digit) and (best_1_digit_number > 0):
        best_number = best_1_digit_number
    elif largest_second_digit > best_1_digit_number:
        best_number = best_2_digit_number
    else:
        best_number = best_3_digit_number

    return best_number


def max_salary(number_list):

    result = ''

    while len(number_list) > 0:
        best_num = find_best_number(number_list)
        result += str(best_num)
        number_list.remove(best_num)

    return result


if __name__ == '__main__':
    input1 = int(input())
    input2_list = [int(i) for i in input().split()]
    print(max_salary(input2_list))
