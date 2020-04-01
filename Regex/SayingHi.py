# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'^[Hh][Ii]\s[^Dd]+')

for i in range(int(input())):
    line = input()
    if re.match(pattern, line):
        print(line)