# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for i in range(n):

    try:
        a, b= map(int, input().split())
        print(a// b)
    except Exception as e:
        print("Error Code: {}".format(e))