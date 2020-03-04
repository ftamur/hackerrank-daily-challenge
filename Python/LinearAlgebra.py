import numpy

lst = []

for i in range(int(input())):
    lst.append(list(map(float, input().split())))

arr = numpy.array(lst, ndmin=2, dtype=float)

print(round(numpy.linalg.det(arr), 2))

