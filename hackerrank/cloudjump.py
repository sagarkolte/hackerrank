import math
import os
import random
import re
import sys
import itertools
import functools
import operator


def functools_reduce_iconcat(a):
    print("flattening lists")
    return functools.reduce(operator.iconcat, a, [])


def partition(n):
    print("constructing partitions")
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]





def get_permutations(lst):
    print("getting all permutations")
    perms = [list(set(list(itertools.permutations(l)))) for l in lst]
    perms = functools_reduce_iconcat(perms)
    perms = list(map(list,perms))
    return perms


def path_filter(path_lst):
    print("filtering paths")
    f = lambda x: True if set(x).issubset(set([1,2])) else False
    filtered_list = list(filter(f,path_lst))
    return filtered_list


def get_thunder_index(lst):
    print("locating thunder")
    indices = [i for i, val in enumerate(lst) if val==1]
    return indices


def get_cum_path(path):
    print("getting cum paths")
    cum_path = [sum(path[0:i+1]) for i in range(len(path))]
    return cum_path


def danger_filter(clouds):
    print("filtering danger")
    thunder = get_thunder_index(clouds)
    possible_paths = get_permutations(partition(len(clouds)-1))
    possible_paths = path_filter(possible_paths)
    cum_paths = [get_cum_path(path) for path in possible_paths]
    paths = list(zip(possible_paths,cum_paths))
    f = lambda x: False if (set(x[1]) & set(thunder)) else True
    safe_paths = list(filter(f,paths))
    safe_paths = min([len(safe_paths[i][0]) for i in range(len(safe_paths))])
    return safe_paths


#c = '0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0'
#c = list(map(int, c.rstrip().split()))


#print(danger_filter(c))
print(list(partition(5)))