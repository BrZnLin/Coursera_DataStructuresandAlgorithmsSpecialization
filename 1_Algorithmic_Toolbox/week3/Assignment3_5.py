# Collecting Signatures

"""
Find the minimum number of points needed to
cover all given segments on a line.
"""


def visit_strategy(num_segments, start_list, end_list):

    visit_time_list = []
    segments_crossed_list = []

    while len(segments_crossed_list) < num_segments:

        remaining_start_list = []
        remaining_end_list = []
        segments_NOT_crossed_list = []

        for ith_segment in range(num_segments):

            if ith_segment not in segments_crossed_list:
                remaining_start_list.append(start_list[ith_segment])
                remaining_end_list.append(end_list[ith_segment])

                segments_NOT_crossed_list.append(ith_segment)

        # each visit happens at the earliest ending time in remaining_end_list
        earliest_ending = min(remaining_end_list)
        visit_time_list.append(earliest_ending)

        for jth_segment in segments_NOT_crossed_list:

            if start_list[jth_segment] <= earliest_ending <= end_list[jth_segment]\
                    and jth_segment not in segments_crossed_list:
                segments_crossed_list.append(jth_segment)

    return visit_time_list


if __name__ == '__main__':
    input1_n = int(input())

    segment_start_list = []
    segment_end_list = []

    for i in range(input1_n):
        input_i = [int(i) for i in input().split()]
        ith_start = input_i[0]
        ith_end = input_i[1]

        segment_start_list.append(ith_start)
        segment_end_list.append(ith_end)

    visit_plan = visit_strategy(input1_n, segment_start_list, segment_end_list)

    print(len(visit_plan))
    print(*visit_plan)
