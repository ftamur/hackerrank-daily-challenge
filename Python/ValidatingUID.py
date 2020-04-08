# Enter your code here. Read input from STDIN. Print output to STDOUT

import string

def is_valid(u_id):

    alphabet = list(string.ascii_lowercase)
    alphabet.extend(list(string.ascii_uppercase))
    alphabet.extend(list(string.digits))

    if len(u_id) != 10:
        return False

    digits = 0
    uppers = 0

    for i in range(len(u_id)):
        if u_id[i] in alphabet:
            alphabet.remove(u_id[i])
        else:
            return False

        if u_id[i].isdigit():
            digits += 1

        if u_id[i].isupper():
            uppers += 1

    if digits < 3 or uppers < 2:
        return False

    return True


for i in range(int(input())):
    print("Valid") if is_valid(input()) else print("Invalid")



    