#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-19.


def selectSort(arr):
    length = len(arr)

    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr


print(selectSort([2, 4, 1, 2, 5, 5, 2, 4, 5, 1, 88, 3]))
print(selectSort([0, 0]))
print(selectSort([3, 2, 1]))
