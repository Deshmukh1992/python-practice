
def swap_first_last(input_list):

    """
    :param input_list: [12, 35, 9, 56, 24]
    :return: [24, 35, 9, 56, 12]

    Time Complexity: O(1)
    Space Complexity: O(n), where n is length of list

    """

    new_list = input_list

    new_list[0], new_list[-1] = input_list[-1], input_list[0]

    return new_list


print(swap_first_last([12, 35, 9, 56, 24]))



