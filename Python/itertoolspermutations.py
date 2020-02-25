# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

def tuple_to_str(tupl):
    s = ""
    for i in tupl:
        s += i

    return s

string, n = input().split()
n = int(n)

twoletters = list()

[twoletters.append(tuple_to_str(per)) for per in list(permutations(string, n))]
twoletters.sort()

[print(per) for per in twoletters]