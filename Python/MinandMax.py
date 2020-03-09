import numpy

n, m = map(int, input().split())

lst = list()

for i in range(n):
    lst.append(list(map(int, input().split())))

np_arr = numpy.array(lst, ndmin=2)

print(numpy.max(numpy.min(np_arr, axis=1)))

