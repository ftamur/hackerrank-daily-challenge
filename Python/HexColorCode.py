# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'(#[0-9A-Fa-f]{3,6})\S')

css = ""

for i in range(int(input())):
    for i in re.findall(pattern, input()):
        print(i)

