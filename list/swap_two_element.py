
def swap_two_element(input_list, pos1, pos2):
    """
    :param pos2: 1
    :param pos1: 3
    :param input_list: [12, 35, 9, 56, 24]
    :return: [9, 35, 12, 56, 24]

    Time Complexity: O(1)
    Space Complexity: O(n), where n is length of list

    """

    input_list[pos1], input_list[pos2] = input_list[pos2], input_list[pos1]

    return input_list



input_list = [12, 35, 9, 56, 24]

pos1 = 1

pos2 = 3


print(swap_two_element(input_list, pos1-1, pos2-1))