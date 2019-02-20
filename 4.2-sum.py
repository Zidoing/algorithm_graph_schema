#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-20.


def rec_sum(sum_list):
    if not sum_list:
        return 0
    return sum_list[0] + rec_sum(sum_list[1:])


print(rec_sum([1, 2, 3, 4, 5]))
