#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void num_to_str(int number) {

    if (number == 1)
        puts("one");
    else if (number == 2)
        puts("two");
    else if (number == 3)
        puts("three");
    else if (number == 4)
        puts("four");
    else if (number == 5)
        puts("five");
    else if (number == 6)
        puts("six");
    else if (number == 7)
        puts("seven");
    else if (number == 8)
        puts("eight");
    else if (number == 9)
        puts("nine");
    else{
        if (number % 2 == 0)
            puts("even");
        else
            puts("odd");
    }
    
}

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.

    for (int i=a; i <b+1; i++) {
        num_to_str(i);
    }
    

    return 0;
}

