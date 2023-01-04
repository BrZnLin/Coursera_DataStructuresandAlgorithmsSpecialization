def FibRecurs(n):
    if n <= 1:
        return n
    else:
        return FibRecurs(n - 1) + FibRecurs(n - 2)


if __name__ == '__main__':
    input1 = int(input())
    print(FibRecurs(input1))
