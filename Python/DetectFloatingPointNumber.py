# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for i in range(int(input())):
    matched = re.fullmatch('^[1-9+-\.][0-9]*(\.\d+)?', input())
    print(bool(matched))

