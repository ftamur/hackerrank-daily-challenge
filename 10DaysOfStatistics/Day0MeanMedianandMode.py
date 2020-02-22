# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats

input()
lst = list(map(int, input().split()))

# print(np.mean(lst))
# print(np.median(lst))
# print(stats.mode(lst)[0][0])

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    lst.sort()
    
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2] + lst[(len(lst)//2) - 1]) / 2
    else:
        return lst[len(lst)//2]

def mode(lst):
    counts = set()
    modes = list()
    [counts.add(lst.count(i)) for i in set(lst)]
    [modes.append(i) for i in set(lst) if lst.count(i) == max(counts)]

    return min(modes)

print("{:.1f}".format(mean(lst)))
print("{:.1f}".format(median(lst)))
print(mode(lst))