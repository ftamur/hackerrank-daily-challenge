cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    fibons = list()

    nth = 0
    first = 0
    second = 1

    for i in range(n):
        
        nth = first + second
        fibons.append(first)
        first = second
        second = nth

    return fibons

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))