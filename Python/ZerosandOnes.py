import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=np.int))
print(np.ones(shape, dtype=np.int))

