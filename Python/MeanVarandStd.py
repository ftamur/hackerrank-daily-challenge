import numpy

n, m = map(int, input().split())

lst = list()

for i in range(n):
    lst.append(list(map(int, input().split())))

numpy.set_printoptions(legacy='1.13')
np_arr = numpy.array(lst, ndmin=2)

print(numpy.mean(np_arr, axis=1))
print(numpy.var(np_arr, axis=0))
print(numpy.std(np_arr))

