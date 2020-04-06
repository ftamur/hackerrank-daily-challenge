# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils

pattern = re.compile(r'^[A-Za-z][a-zA-Z0-9_.-]+@[A-Za-z]+\.[A-Za-z]{1,3}$')

for i in range(int(input())):
    inp = input()
    name, email_addr = email.utils.parseaddr(inp)
    
    # print(name)
    # print(email_addr)

    if (re.match(pattern, email_addr)):
        print(inp)

