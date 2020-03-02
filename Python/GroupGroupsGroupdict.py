# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

reg = r"([a-zA-Z0-9])\1+"

inp = input()
m = re.search(reg, inp)

# print(m)

if m:
    print(m.group(0)[1])
else:
    print(-1)