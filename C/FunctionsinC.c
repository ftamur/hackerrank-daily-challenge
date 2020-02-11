#include <stdio.h>

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max(int a, int b) {

    if (a <= b)
        return b;
    
    return a;

}

int max_of_four(int a, int b, int c, int d) {

    int big_1 = max(a, b);
    int big_2 = max(c, d);

    return max(big_1, big_2);
}

int main() {
    
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

