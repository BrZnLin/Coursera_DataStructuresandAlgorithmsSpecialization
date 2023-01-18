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

    return distance_matrix


#
def output_alignment(i, j, distance_matrix, text_list_1, text_list_2, edited_text1, edited_text2):

    if i == 0 and j == 0:
        return

    if i > 0 and distance_matrix[i][j] == distance_matrix[i - 1][j]:
        output_alignment(i - 1, j, distance_matrix, text_list_1, text_list_2, edited_text1, edited_text2)
        edited_text1.append(text_list_1[i])
        edited_text2.append('_')

    elif j > 0 and distance_matrix[i][j] == distance_matrix[i][j - 1]:
        output_alignment(i, j - 1, distance_matrix, text_list_1, text_list_2, edited_text1, edited_text2)
        edited_text1.append('_')
        edited_text2.append(text_list_2[j])

    else:
        output_alignment(i - 1, j - 1, distance_matrix, text_list_1, text_list_2, edited_text1, edited_text2)
        edited_text1.append(text_list_1[i])
        edited_text2.append(text_list_2[j])

    return


if __name__ == '__main__':
    input1_string = input()
    input2_string = input()

    distance_m = edit_distance(input1_string, input2_string)

    print(distance_m)

    i = len(input1_string)
    j = len(input2_string)

    edited_text_1 = []
    edited_text_2 = []

    # output_alignment(i, j, distance_m, input1_string, input2_string, edited_text_1, edited_text_2)

    # print(*edited_text_1)
    # print(*edited_text_2)
