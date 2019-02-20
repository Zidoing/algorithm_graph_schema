#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-20.
import copy


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [item for item in arr[1:] if item <= pivot]
    greater = [item for item in arr[1:] if item > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = copy.copy(a)
import random

random.shuffle(a)

print(a, b)

assert quick_sort(a) == b
