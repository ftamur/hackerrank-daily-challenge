# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())

rows = list()

for i in range(x):
    rows.append(list(map(float, input().split())))

for i in zip(*rows):
    print(sum(i) / x)