if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_ = sorted(list(set(arr)))
    print(arr_[-2])
    