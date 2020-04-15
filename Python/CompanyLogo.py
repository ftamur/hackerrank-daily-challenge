#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()

    c = Counter(sorted(s))
    [print(i[0], i[1]) for i in c.most_common(3)]