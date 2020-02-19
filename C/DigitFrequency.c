#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  

    char str[1000];
    scanf("%s", str);
   
    for (int i=0; i<10; i++) {
        int sum_digit = 0;

        for (int j=0; j<strlen(str); j++) {
            
            // (int) convert char to ascii values. 
            // ascii values of digits from 48 to 57.
            if ((i+48) == (int) str[j])
                sum_digit++;
        
        }

        printf("%d ", sum_digit);
    }

    return 0;
}
