#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    # return a[::-1]
    # return reversed(a) 
    # a.reverse()
    # return a
    temp_a = [None] * len(a)
    len_a = len(a) - 1
    for i in range(len(a)-1, -1, -1):
        temp_a[len_a - i] = a[i]

    return temp_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
