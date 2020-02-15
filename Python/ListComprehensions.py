if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # coordinates = list()

    # # easy way to solve not really smart.
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i + j + k != n:
    #                 coordinates.append([i,j,k])


    # print(coordinates)

    coordinates_smart = list()
    # complicated way and smart one.
    [coordinates_smart.append([i,j,k]) for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

    print(coordinates_smart)
