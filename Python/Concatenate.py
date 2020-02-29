import numpy as np

n, m, p = map(int, input().split())

array = np.array(input().split(), dtype=int, ndmin=2)

for i in range(m+n-1):
    array = np.concatenate((array, np.array(input().split(), dtype=int, ndmin=2)), axis=0)

print(array)

