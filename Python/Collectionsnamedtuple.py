sum_marks, n, index = 0, int(input()), input().split().index('MARKS')

for i in range(n):
    sum_marks += int(input().split()[index])

print(sum_marks/n)



