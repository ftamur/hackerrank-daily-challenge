import numpy

lst_1 = list(map(float, input().split()))
lst_2 = list(map(float, input().split()))

A = numpy.array(lst_1)
B = numpy.array(lst_2)

print(numpy.inner(A, B).astype(int))
print(numpy.outer(A, B).astype(int))