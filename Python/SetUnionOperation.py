# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
st1 = set(input().split())

n2 = input()
st2 = set(input().split())

print(len(st1.union(st2)))