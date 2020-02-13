import re

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input());
all_text = ""

for i in range(n):

    line = input()
    all_text += line
    all_text += '\n'

all_text_and = re.sub('\s&&(?= )', ' and', all_text)
print(re.sub('\s\|\|(?= )', ' or', all_text_and))