# Enter your code here. Read input from STDIN. Print output to STDOUT

heigth, width = map(int, input().split())

string = ".|."

def upper(width, heigth):
    for i in range(1, heigth, 2):
        print((string*i).center(width, '-'))
    
def lower(width, heigth):
    for i in range(heigth-2, 0, -2):
        print((string*i).center(width, '-'))


upper(width, heigth)
print("WELCOME".center(width, '-'))
lower(width, heigth)  

