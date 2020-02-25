# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

[print(prod, end=' ') for prod in list(product(lst1, lst2))]

