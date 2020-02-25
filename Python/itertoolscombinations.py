# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

def tuple_to_str(tupl):
    s = ""
    for i in sorted(list(tupl)):
        s += i

    return s

string, n = input().split()
n = int(n)

combins = list()

for i in range(1, n+1):
    parts = list()
    [parts.append(tuple_to_str(per)) for per in list(combinations(string, i))]
    parts.sort()
    combins.extend(parts)

    
[print(per) for per in combins]