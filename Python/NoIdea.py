# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())

array = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happines = 0

print(sum([(i in A) - (i in B) for i in array]))

# for i in array:
#     if i in A:
#         happines += 1
#     if i in B:
#         happines += -1

