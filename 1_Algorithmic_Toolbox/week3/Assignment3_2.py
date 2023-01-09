# Maximum Value of the Loot

"""
Find the maximal value of items that fit into the backpack.
"""


def max_loot(W, cost_list, weight_list, unit_value_list):

    loot_value = 0

    while W > 0 and any([(weight > 0) for weight in weight_list]):
        max_unit_value = max(unit_value_list)
        id_best_compound = unit_value_list.index(max_unit_value)

        if weight_list[id_best_compound] < W:

            W -= weight_list[id_best_compound]
            loot_value += cost_list[id_best_compound]

            # update info in 3 lists
            cost_list[id_best_compound] = 0
            weight_list[id_best_compound] = 0
            unit_value_list[id_best_compound] = 0

        else:
            loot_value += unit_value_list[id_best_compound] * W
            W -= W

    return loot_value


if __name__ == '__main__':

    input1_digits = input().split()
    n_compound = int(input1_digits[0])
    W_capacity = int(input1_digits[1])

    compound_cost_list = []
    compound_weight_list = []
    compound_unit_value_list = []

    for i in range(n_compound):
        compound_info = input().split()
        compound_cost_list.append(int(compound_info[0]))
        compound_weight_list.append(int(compound_info[1]))
        compound_unit_value_list.append(int(compound_info[0]) / int(compound_info[1]))

    print(max_loot(W_capacity, compound_cost_list, compound_weight_list, compound_unit_value_list))
