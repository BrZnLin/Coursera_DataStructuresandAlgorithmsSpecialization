def EnclidGCD(a, b):
    if b == 0:
        return a

    a_remainder = a % b

    return EnclidGCD(b, a_remainder)


if __name__ == '__main__':
    input1 = int(input())
    input2 = int(input())
    print(EnclidGCD(input1, input2))


# This algorithm is based on a key lemma
