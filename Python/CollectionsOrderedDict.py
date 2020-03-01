# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ord_dict = OrderedDict()

for i in range(int(input())):
    item = input().split()
    if " ".join(item[:-1]) in ord_dict.keys():
        ord_dict[" ".join(item[:-1])] += int(item[-1])
    else:
        ord_dict[" ".join(item[:-1])] = int(item[-1])

for item in ord_dict.keys():
    print(item, ord_dict[item])





