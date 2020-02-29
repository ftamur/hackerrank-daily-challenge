import numpy as np
 
n = list(map(int, input().split()))
els = list()

for i in range(n[0]):   
    els.extend(list(map(int, input().split())))

arr = np.array(els, int)
arr = arr.reshape(n[0], n[1])

print(np.transpose(arr))
print(arr.flatten())

