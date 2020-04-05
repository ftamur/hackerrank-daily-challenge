from collections import deque

d = deque()

for i in range(int(input())):
    command, *attrs = input().split()
    getattr(d, command)(*attrs)

[print(x, end=' ') for x in d]