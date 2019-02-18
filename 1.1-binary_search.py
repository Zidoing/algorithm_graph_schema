#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-18.


def binary_search(_list, item):
    low, high = 0, len(_list) - 1

    while low <= high:
        mid = low + (high - low) // 2  ## 需要注意python3的除法
        if _list[mid] == item:
            return mid
        elif _list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


a = [1, 2, 3, 4, 5, 6]

print(binary_search(a, 6))
print(binary_search(a, -1))
print(binary_search(a, -2))
print(binary_search(a, 1))
