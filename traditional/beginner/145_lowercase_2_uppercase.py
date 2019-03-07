# -*- coding: utf-8 -*-
"""
=====================================================================================

    Filename:  
        145_lowercase_2_uppercase.py
    Version:
    Created:  
    Revision:
    Compiler:  
    Author:  
        Ployo Wiself
    Organization:  
    Description:  
        你可以假设输入一定在小写字母 a ~ z 之间，将一个字符由小写字母转换为大写字母
        Example1:
            Input:  'a'
            Output: 'A'
        Example2:
            Input:  'b'
            Output: 'B'

=====================================================================================
"""

import os
import sys
import timeit

def convertLower2Upper(character) :
    return chr(ord(char)-32)


if "__main__" == __name__ :
    print(timeit.timeit("convertLower2Upper('a')" , "from __main__ import convertLower2Upper" , number=1000) * 1000)
