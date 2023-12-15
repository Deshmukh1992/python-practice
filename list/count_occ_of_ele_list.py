
def count_occ_of_ele_list_mtd_1(input_list, input_ele):
    """

    :param input_ele: 10
    :param input_list: [15, 6, 7, 10, 12, 20, 10, 28, 10]
    :return: 3

    This is method 1 - Using list comprehension

    """

    new_list = [i for i in input_list if i == input_ele]

    return len(new_list)


# print(count_occ_of_ele_list_mtd_1([15, 6, 7, 10, 12, 20, 10, 28, 10], 10))


def count_occ_of_ele_list_mtd_2(input_list, input_ele):
    """

    :param input_ele: 10
    :param input_list: [15, 6, 7, 10, 12, 20, 10, 28, 10]
    :return: 3

    This is method 2 - Using Dictionary Comprehension

    """

    occ_dict = {item: input_list.count(item) for item in input_list}

    return occ_dict[input_ele]


print(count_occ_of_ele_list_mtd_2([15, 6, 7, 10, 12, 20, 10, 28, 10], 10))


def count_occ_of_ele_list_mtd_3(input_list, input_ele):
    """

    :param input_ele: 10
    :param input_list: [15, 6, 7, 10, 12, 20, 10, 28, 10]
    :return: 3

    This is method 3 - Using list count() method

    """

    return input_list.count(input_ele)


# print(count_occ_of_ele_list_mtd_3([15, 6, 7, 10, 12, 20, 10, 28, 10], 10))