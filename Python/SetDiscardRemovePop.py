n = int(input())
s = set(map(int, input().split()))

def do_operation(op, s, value=None):
    if op == "remove":
        s.remove(value)
    elif op == "discard":
        s.discard(value)
    else:
        s.pop()

    return s

for i in range(int(input())):
    command = input().split()

    if len(command) == 2:
        s = do_operation(command[0], s, int(command[1]))
    else:
        s = do_operation(command[0], s)

print(sum(s))