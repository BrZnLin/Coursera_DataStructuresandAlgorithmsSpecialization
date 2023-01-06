import numpy as np


def car_fueling(d, m, num_stations, d_station_list):

    """
    :param d: distance between the origin and destination
    :param m: the range of this car with a full tank
    :param num_stations: number of gas stations along the way
    :param d_station_list: distance from origin to the gas stations
    :return: the least stops possible to get to destination
    """

    num_stops = 0
    distance_traveled = 0

    d_station_array = np.array(d_station_list)

    d_station_array_and_dest = np.append(d_station_array, [d])
    orig_and_d_station_array = np.append([0], d_station_array)

    if any((d_station_array_and_dest - orig_and_d_station_array) > m):
        return "It is not possible to complete this trip."

    while d > (distance_traveled + m):

        d_station_array = d_station_array[d_station_array > distance_traveled]
        d_station_array_reachable = d_station_array[d_station_array < (distance_traveled + m)]

        # update distance traveled and number of stops
        distance_traveled = d_station_array_reachable[-1]
        num_stops += 1

    return num_stops


if __name__ == '__main__':
    input1_d = int(input())
    input2_m = int(input())
    input3 = int(input())
    input4 = [int(i) for i in input().split()]
    print(car_fueling(input1_d, input2_m, input3, input4))
