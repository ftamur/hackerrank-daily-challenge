# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
rooms = list(map(int, input().split()))

unique = set(rooms)

rooms_total = sum(rooms)
unique_total = sum(unique)

print((k * unique_total - rooms_total) // (k-1))



