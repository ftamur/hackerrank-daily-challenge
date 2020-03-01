# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

lst = list()

for i in range(int(input())):
    lst.append(input())

count = Counter(lst)

print(len(count.keys()))

for value in count.values():
    print(value, end=" ")
