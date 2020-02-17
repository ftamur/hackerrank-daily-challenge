#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.

    int digit_sum = 0;

    while (n >= 10) {
        digit_sum += n % 10;
        n /= 10;
    }
    
    digit_sum += n;

    printf("%d", digit_sum);

    return 0;
}

