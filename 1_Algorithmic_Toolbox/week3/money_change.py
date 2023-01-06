def count_change_coin(change_amount):

    num_coin = 0

    num_coin += change_amount // 10
    change_amount = change_amount % 10

    num_coin += change_amount // 5
    change_amount = change_amount % 5

    num_coin += change_amount

    return num_coin


if __name__ == '__main__':
    input1 = int(input())
    print(count_change_coin(input1))
