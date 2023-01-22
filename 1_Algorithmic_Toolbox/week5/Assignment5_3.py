# Edit Distance

"""
Compute the edit distance between two strings.
"""

# compute the edit distance
# 1 for insert and delete
# 1 for mismatch
# 0 for match


def edit_distance(text_list_1, text_list_2):

    # editing
    # text_list_1  ->  n_rows  ->  i
    # distance
    # text_list_2  ->  n_cols  ->  j

    n_cols = len(text_list_2)
    n_rows = len(text_list_1)
    distance_matrix = [[0] * (n_cols + 1) for _ in range(n_rows + 1)]

    for i in range(1, n_rows + 1):
        distance_matrix[i][0] = i

    for j in range(1, n_cols + 1):
        distance_matrix[0][j] = j

    for j in range(1, n_cols + 1):
        for i in range(1, n_rows + 1):
            insertion = distance_matrix[i][j - 1] + 1
            deletion = distance_matrix[i - 1][j] + 1
            match = distance_matrix[i - 1][j - 1]
            mismatch = distance_matrix[i - 1][j - 1] + 1

            if text_list_1[i - 1] == text_list_2[j - 1]:
                distance_matrix[i][j] = min(insertion, deletion, match)
            else:
                distance_matrix[i][j] = min(insertion, deletion, mismatch)

    return distance_matrix[-1][-1]


if __name__ == '__main__':
    input1_string = input()
    input2_string = input()

    distance_m = edit_distance(input1_string, input2_string)

    print(distance_m)