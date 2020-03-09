import numpy

lst_1 = list()
lst_2 = list()

n = int(input())

for i in range(n * 2):
    if i >= n:
        lst_2.append(list(map(int, input().split())))
    else:
        lst_1.append(list(map(int, input().split())))


np_arr_1 = numpy.array(lst_1, ndmin=2)
np_arr_2 = numpy.array(lst_2, ndmin=2)

print(numpy.matmul(np_arr_1, np_arr_2))

