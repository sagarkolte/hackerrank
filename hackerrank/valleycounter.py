#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def make_signed_list(hike):
    hike = hike.replace('D', ',-1')
    hike = hike.replace('U', ',1')
    hike = hike.strip(',')
    signed_list = hike.split(',')
    signed_list = list(map(int, signed_list))
    return signed_list


def make_cum_list(hike):
    signed_list = make_signed_list(hike)
    #cum_list = [sum(signed_list[0:i + 1]) for i in range(len(signed_list))]
    cum_list = list(np.cumsum(signed_list))
    return cum_list


def make_cum_str(hike):
    hike = [str(i) for i in make_cum_list(hike)]
    hike_str = ','.join(hike)
    return hike_str


def get_mount_valleys(hike):
    hike_str = make_cum_str(hike)
    hike_list = re.split("\D0\D?", hike_str)
    hike_list = [s.strip(',') for s in hike_list]
    return hike_list


def check_mount_valley(sub_hike):
    if len(sub_hike) == 0:
        return False
    else:
        sub_hike_list = sub_hike.split(',')
        sub_hike_list = [int(i) for i in sub_hike_list]
        list_check = [i < 0 for i in sub_hike_list]
        return not (False in set(list_check))


def countingValleys(steps, path):
    hike = path
    mount_valley_list = make_cum_str(hike)
    valleys = re.findall(r'(,?-\d+)+', mount_valley_list)

    return len(valleys)

hike = 'DDUUDDUDUUUD'
steps = len(hike)

print(countingValleys(steps,hike))