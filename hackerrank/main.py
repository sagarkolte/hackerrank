#!/bin/python3

import math
import os
import random
import re
import sys


hike = 'DDUUDDDUDUUDUDDDUUDDUDDDUDDDUDUUDDUUDDDUDDDUDDDUUUDUDDDUDUDUDUUDDUDUDUDUDUUUUDDUDDUUDUUDUUDUUUUUUUUU'


def make_signed_list(hike):
    f = lambda k: 1 if k=='U' else -1
    signed_list = [f(hike[i]) for i in range(len(hike))]
    return signed_list


def make_cum_list(hike):
    signed_list = make_signed_list(hike)
    cum_list = [sum(signed_list[0:i+1]) for i in range(len(signed_list))]
    return cum_list


def make_cum_str(hike):
    hike = [str(i) for i in make_cum_list(hike)]
    hike_str = ','.join(hike)
    print(hike_str)
    return hike_str


def get_mount_valleys(hike):
    hike_str = make_cum_str(hike)
    hike_list = re.split("\D0\D?", hike_str)
    hike_list = [s.strip(',') for s in hike_list]
    return hike_list



def check_mount_valley(sub_hike):
    if len(sub_hike)==0:
        return False
    else:
        sub_hike_list = sub_hike.split(',')
        sub_hike_list = [int(i) for i in sub_hike_list]
        list_check = [i < 0 for i in sub_hike_list]
        return not(False in set(list_check))


def counting_valleys(steps, path):
    hike = path
    mount_valley_list = make_cum_str(hike)
    valleys = re.findall(r'(,?-\d)+', mount_valley_list)

    return len(valleys)


#print(make_signed_list(hike))
#print(make_cum_list(hike))
#print(make_cum_str(hike))
#print(get_mount_valleys(hike))
#print(check_mount_valley('-1'))
print(counting_valleys(10,hike))