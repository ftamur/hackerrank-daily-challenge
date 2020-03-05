# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
flag = True

for i in range(int(input())):
    b = set(map(int, input().split()))
    if not a.issuperset(b) or a == b:
        flag = False
    
print(flag)

