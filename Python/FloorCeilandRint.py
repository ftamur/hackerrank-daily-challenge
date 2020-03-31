import numpy

array = numpy.array(list(map(float, input().split())))

numpy.set_printoptions(sign=' ')

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
