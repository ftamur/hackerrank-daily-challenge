def upperPart(ln, letters):
    lines = ""
    for i in range(1, len(letters)+1):
        lines = "".join(letters[-1:-i:-1]) + "".join(letters[-i:])
        print("-".join(lines).center(ln, '-'))


def lowerPart(ln, letters):
    lines = ""
    for i in range(len(letters), 0, -1):
        lines = "".join(letters[-1:-i:-1]) + "".join(letters[-i:])
        print("-".join(lines).center(ln, '-'))


def print_rangoli(size):
    # your code goes here
    import string
    alphabet = list(string.ascii_letters[:26])

    upperPart(size*4-3, alphabet[0:size])
    lowerPart(size*4-3, alphabet[1:size])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)