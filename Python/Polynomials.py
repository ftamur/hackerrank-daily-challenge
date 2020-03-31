import numpy

coeffs = list(map(float, input().split()))
val = float(input())

print(numpy.polyval(coeffs, val))

