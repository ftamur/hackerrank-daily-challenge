# Enter your code here. Read input from STDIN. Print output to STDOUT
inp_lst = list(input())

lowers, uppers, digits = list(), list(), list()
order = '1357902468'

for i in inp_lst:
    if i.islower(): lowers.append(i)
    elif i.isupper(): uppers.append(i)
    elif i.isdigit(): digits.append(i)

inp_lst_sorted = sorted(lowers) + sorted(uppers) + sorted(digits, key=order.index)

print("".join(inp_lst_sorted))
