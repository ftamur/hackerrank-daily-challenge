def print_formatted(number):
    # your code goes here
    width_ = len(bin(number)[2:])

    for i in range(1, number+1):
        # print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width_))
        print("{}".format(i).rjust(width_), end=' ')
        print("{}".format(oct(i)[2:]).rjust(width_), end=' ')
        print("{}".format(hex(i)[2:].upper()).rjust(width_), end=' ')
        print("{}".format(bin(i)[2:]).rjust(width_), end='\n')
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)