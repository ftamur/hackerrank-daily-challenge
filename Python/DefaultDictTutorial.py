# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

dict_lst = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    dict_lst['n'].append(input())

for i in range(m):
    dict_lst['m'].append(input())

for i in dict_lst['m']:
    indexes = ""
    if i in dict_lst['n']:
        for j in range(len(dict_lst['n'])):
            if i == dict_lst['n'][j]:
                indexes += str(j+1) + " "
        print(indexes)
    else:
        print("-1")
