# Car Fueling

"""
Compute the minimum number of gas tank
refills to get from one city to another.
"""


def count_min_fuel_stops(d, m, n, stops_list):

    min_stop_count = 0

    stops_list.append(d)
    current_location = 0

    while current_location < d:

        possible_stops = []

        for stop in stops_list:
            if current_location < stop < (current_location + m):
                possible_stops.append(stop)

        if len(possible_stops) > 0:
            current_location = max(possible_stops)
            min_stop_count += 1
            # this would include the stop at destination
        else:
            return -1

    return int(min_stop_count-1)
    # subtract 1 for the stop at destination


if __name__ == '__main__':
    input1 = int(input())
    input2 = int(input())
    input3 = int(input())
    input4_list = [int(i) for i in input().split()]
    print(count_min_fuel_stops(input1, input2, input3, input4_list))
