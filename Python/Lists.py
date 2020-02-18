def list_operation(lst, operation):

    if len(operation.split()) == 1:
        if operation.strip() == 'print':
            print(lst)
        elif operation.strip() == 'sort':
            lst.sort()
        elif operation.strip() == 'pop':
            lst.pop()
        elif operation.strip() == 'reverse':
            lst.reverse()

    elif len(operation.split()) == 2:
        if operation.split()[0] == 'remove':
            lst.remove(int(operation.split()[1]))
        elif operation.split()[0] == 'append':
            lst.append(int(operation.split()[1]))

    elif len(operation.split()) == 3:
        if operation.split()[0] == 'insert':
            lst.insert(int(operation.split()[1]), int(operation.split()[2]))

if __name__ == '__main__':
    N = int(input())

    lst = list()

    for i in range(N):
        list_operation(lst, input())

 
