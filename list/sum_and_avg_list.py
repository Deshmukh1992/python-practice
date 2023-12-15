
def sum_and_avg_list_mtd_1(input_list):
    """

    :param input_list: [4, 5, 1, 2, 9, 7, 10, 8]
    :return: Sum: 46, Average: 5.75

    This is method 1 - Using Naive method

    """

    list_sum = 0

    for i in input_list:
        list_sum += i


    list_avg = list_sum/len(input_list)

    return list_sum, list_avg


# ele_sum, ele_avg = sum_and_avg_list_mtd_1([4, 5, 1, 2, 9, 7, 10, 8])
#
# print(ele_sum, ele_avg)


def sum_and_avg_list_mtd_2(input_list):
    """

    :param input_list: [4, 5, 1, 2, 9, 7, 10, 8]
    :return: Sum: 46, Average: 5.75

    This is method 2 - Using sum() method

    """

    list_sum = sum(input_list)

    list_avg = list_sum / len(input_list)

    return list_sum, list_avg


ele_sum, ele_avg = sum_and_avg_list_mtd_1([4, 5, 1, 2, 9, 7, 10, 8])

print(ele_sum, ele_avg)