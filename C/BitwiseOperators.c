#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

void calculate_the_maximum(int n, int k) {
    //Write your code here.

    int and = 0, or = 0, xor = 0;
    int and_max = 0, or_max = 0, xor_max = 0;

    for (int i=1; i<n; i++){
        for (int j=i+1; j<=n; j++){
            // printf("i: %d, j: %d, &: %d\n", i, j, i&j);

            and= i & j;
            or = i | j;
            xor = i ^ j;

            if (and < k && and > and_max)
                and_max = and;
               
            if (or < k && or > or_max)
                or_max = or;
                
            if (xor < k && xor > xor_max)
                xor_max = xor;
        }
    }

    printf("%d\n%d\n%d", and_max, or_max, xor_max);

}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
