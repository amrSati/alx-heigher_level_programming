#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    sum_of_weights = 0
    for el in my_list:
        score, weight = el
        avg += score * weight
        sum_of_weights += weight

    return (avg / sum_of_weights)
