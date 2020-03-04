import numpy

n, size = map(int, input().split())

lst_1 = []
lst_2 = []

for i in range(n):
    lst_1.append(list(map(int, input().split())))

for i in range(n):
    lst_2.append(list(map(int, input().split())))

arr_1 = numpy.array(lst_1, ndmin=2)
arr_2 = numpy.array(lst_2, ndmin=2)

print(arr_1 + arr_2)
print(arr_1 - arr_2)
print(arr_1 * arr_2)
print(arr_1 // arr_2)
print(arr_1 % arr_2)
print(arr_1 ** arr_2)

