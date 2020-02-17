# Enter your code here. Read input from STDIN. Print output to STDOUT

n_case = int(input())

for i in range(n_case):

    size_a = input()
    a = set(sorted(input().split()))

    size_b = input()
    b = set(sorted(input().split()))

    subset = True

    for elm in a:
        if elm not in b:
            subset = False
            break

    print(subset)

