if __name__ == '__main__':
    s = input()

    alphanum = False
    alpha = False
    digit = False
    upper = False
    lower = False

    for i in s:
        if i.isalnum(): alphanum = True
        if i.isalpha(): alpha = True
        if i.isdigit(): digit = True
        if i.islower(): lower = True
        if i.isupper(): upper = True
        
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)