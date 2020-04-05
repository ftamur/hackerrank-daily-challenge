# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})[^AEIOUaeiou]')

result = re.findall(pattern, input())

if len(result) == 0:
    print(-1)
else:
    [print(x) for x in result]


