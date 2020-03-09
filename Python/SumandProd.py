import numpy

n, m = map(int, input().split())

lst = list()

for i in range(n):
    lst.append(list(map(int, input().split())))

np_arr = numpy.array(lst, ndmin=2)

print(numpy.prod(numpy.sum(np_arr, axis=0), axis=0))


