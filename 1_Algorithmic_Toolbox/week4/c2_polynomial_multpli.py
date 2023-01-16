

def mult_poly_naive(A_factors, B_factors, n):

    product_factor_list = [0] * (2 * n - 1)

    for i in range(0, n):
        for j in range(0, n):
            product_factor_list[i + j] += A_factors[i] * B_factors[j]

    return product_factor_list


"""Need a fix later"""
def mult_poly_dnc_naive(A_factors, B_factors, n, a_index, b_index):

    product_factor_list = [0] * int(2 * n - 1)

    # base case
    if n == 1:
        product_factor_list[0] = A_factors[a_index] * B_factors[b_index]
        return product_factor_list

    # Other cases and variants
    product_factor_list[0: n - 1] = mult_poly_dnc_naive(A_factors,
                                                        B_factors,
                                                        int(n / 2),
                                                        a_index,
                                                        b_index)
    product_factor_list[0: 2 * n - 1] = mult_poly_dnc_naive(A_factors,
                                                            B_factors,
                                                            int(n / 2),
                                                            int(a_index + n / 2),
                                                            int(b_index + n / 2))

    D0E1 = mult_poly_dnc_naive(A_factors,
                               B_factors,
                               int(n / 2),
                               a_index,
                               int(b_index + n / 2))
    D1E0 = mult_poly_dnc_naive(A_factors,
                               B_factors,
                               int(n / 2),
                               int(a_index + n / 2),
                               b_index)

    product_factor_list[int(n / 2): int(n + n / 2 - 1)] += D0E1 + D1E0

    return product_factor_list


def mult_poly_dnc_upgrade():

    return


if __name__ == '__main__':
    input_list_A = [int(num) for num in input().split()]
    input_list_B = [int(num) for num in input().split()]
    input3 = int(input())
    print(*mult_poly_naive(input_list_A, input_list_B, input3))
    print(*mult_poly_dnc_naive(input_list_A, input_list_B, input3, 0, 0))
