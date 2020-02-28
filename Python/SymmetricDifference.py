# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
set1 = set(map(int, input().split()))

n = input()
set2 = set(map(int, input().split()))

difference = sorted(list(set1.symmetric_difference(set2)))

[print(i) for i in difference]