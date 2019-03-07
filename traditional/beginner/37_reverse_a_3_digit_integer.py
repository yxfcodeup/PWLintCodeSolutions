# -*- coding: utf-8 -*-
"""
=====================================================================================

    Filename:  
        37_reverse_a_3_digit_integer.py
    Version:
    Created:  
    Revision:
    Compiler:  
    Author:  
        Ployo Wiself
    Organization:  
    Description:  
        你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000，并
        将其翻转
        Example1:
            Input:  123
            Output: 321
        Example2:
            Input:  900
            Output: 9

=====================================================================================
"""

import os
import sys
import timeit

def reverse3DInteger(in_int) :
    if (in_int >= 100 and in_int < 1000) :
        return in_int // 100 + in_int // 10 % 10 * 10 + in_int % 10 * 100
    else :
        return -1

    """
    if (in_int >= 100 and in_int < 1000) :
        rst = 0
        while in_int != 0 :
            rst = rst * 10 + in_int % 10
            in_int = in_int // 10
        return rst
    else :
        return -1
    """


if "__main__" == __name__ :
    print(reverse3DInteger(123))
    print(timeit.timeit("reverse3DInteger(123)" , "from __main__ import reverse3DInteger" , number=1000) * 1000)
