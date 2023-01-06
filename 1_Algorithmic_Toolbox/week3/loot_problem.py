import numpy as np


def loot_strategy(capacity, cost_list, weight_list):

    """
    :param capacity: weight of stuff that the backpack can take
    :param weight_list: available amount of the items in a list
    :param cost_list: total value of a certain item, not value in unit weight
    :return: highest possible value to loot
    """

    total_value = 0

    np_cost_array = np.array(cost_list)
    np_weight_array = np.array(weight_list)
    unit_value_array = np_cost_array / np_weight_array

    while capacity > 0 and any(np_weight_array):
        id_best_item = np.argmax(unit_value_array)

        if np_weight_array[id_best_item] <= capacity:
            total_value += np_cost_array[id_best_item]
            capacity -= np_weight_array[id_best_item]
            unit_value_array[id_best_item] = 0
            np_weight_array[id_best_item] = 0

        else:
            total_value += unit_value_array[id_best_item] * capacity
            capacity -= np_weight_array[id_best_item]

    return total_value


if __name__ == '__main__':

    input1_values = input('Number of items, Capacity: ').split()
    num_of_items = int(input1_values[0])
    capacity_input = int(input1_values[1])

    cost_input_list = []
    weight_input_list = []

    for i in range(num_of_items):
        (ith_item_cost, ith_item_weight) = input(f"{i+1}th item's cost and weight: ").split()
        cost_input_list.append(ith_item_cost)
        weight_input_list.append(ith_item_weight)

    cost_input_list_int = [int(i) for i in cost_input_list]
    weight_input_list_int = [int(j) for j in weight_input_list]

    print(loot_strategy(capacity_input, cost_input_list_int, weight_input_list_int))
