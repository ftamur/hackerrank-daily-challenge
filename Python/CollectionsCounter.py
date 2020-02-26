# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
shoe_lst = list(map(int, input().split()))
shoe_counter = Counter(shoe_lst)
n_customer = int(input())

profit = 0

for i in range(n_customer):

    shoe, price = map(int, input().split())
    
    if shoe_counter[shoe] > 0:
        profit += price
        shoe_counter[shoe] -= 1
    
    
print(profit)