def FibListing(n):
    fib_list = []

    for i in range(n + 1):
        if i <= 1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list[-1]


if __name__ == '__main__':
    input1 = int(input())
    print(FibListing(input1))
