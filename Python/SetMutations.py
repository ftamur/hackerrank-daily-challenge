# Enter your code here. Read input from STDIN. Print output to STDOUT

def do_set_operations(operation, set1, set2):

    if operation == "intersection_update":
        set1.intersection_update(set2)
    elif operation == "update":
        set1.update(set2)
    elif operation == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    elif operation == "difference_update":
        set1.difference_update(set2)

    return set1

input()
set_1 = set(map(int, input().split()))

for i in range(int(input())):
    operand, n = input().split()
    set_1 = do_set_operations(operand, set_1, set(map(int, input().split())))

print(sum(set_1))
