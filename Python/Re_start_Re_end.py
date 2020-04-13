# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input() 
pattern = input()

r = re.compile(pattern)

m = r.search(string, pos=0)

if m:

    while m:
        print((m.start(), m.end()-1))
        m = r.search(string, pos=m.start()+1)

else:
    print((-1, -1))