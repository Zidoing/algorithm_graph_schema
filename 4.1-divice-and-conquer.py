#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-20.


def split_farm(long, short):
    if long == 2 * short:
        return short

    print(long, short)

    used = (long // short) * short

    long, short = short, long - used
    print(long, short)

    return split_farm(long, short)


print(split_farm(1680, 640))
