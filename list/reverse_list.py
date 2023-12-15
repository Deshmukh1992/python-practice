

def reverse_list_mtd_1(input_list):
    """

    :param input_list: [10, 11, 12, 13, 14, 15]
    :return: [15, 14, 13, 12, 11, 10]


    This is method 1 - reverse list using index slicing

    Time Complexity: O(1)
    Space Complexity: O(n), where n is length of list

    """

    return input_list[::-1]


# print(reverse_list_mtd_1([10, 11, 12, 13, 14, 15]))


def reverse_list_mtd_2(input_list):
    """

    :param input_list: [10, 11, 12, 13, 14, 15]
    :return: [15, 14, 13, 12, 11, 10]


    This is method 2 - reverse list using reverse method

    The input_list.reverse() method returns None because it mutates the original list.
    Most methods that mutate an object in place return None in Python.

    Time Complexity: O(1)
    Space Complexity: O(n), where n is length of list

    """

    input_list.reverse()

    return input_list


# print(reverse_list_mtd_2([10, 11, 12, 13, 14, 15]))


def reverse_list_mtd_3(input_list):
    """

    :param input_list: [10, 11, 12, 13, 14, 15]
    :return: [15, 14, 13, 12, 11, 10]

    This is method 3 - reverse list using reversed() method

    If you want to reverse the list without mutating it in place, use the reversed() function.

    Time Complexity: O(1)
    Space Complexity: O(n), where n is length of list

    """

    new_list = list(reversed(input_list))

    return new_list


print(reverse_list_mtd_3([10, 11, 12, 13, 14, 15]))