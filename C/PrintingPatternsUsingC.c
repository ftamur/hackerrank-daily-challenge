#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.

    int n_matrix[2*n-1][2*n-1];

    // This is not a good solution we have big time complexity.
    // But it is a clean solution. 

    for (int k=n; k>1; k--){

        for (int i=0; i<2*k-1; i++) {
            for (int j=0; j<2*k-1; j++) {

                if (i == 0 || i == 2*k-2 || j == 0 || j == 2*k-2){
                    n_matrix[i+(n-k)][j+(n-k)] = k;
                }else{
                    n_matrix[i+(n-k)][j+(n-k)] = k-1;
                }
                    
            }
        }
    }

    for (int i=0; i<2*n-1; i++) {
        for (int j=0; j<2*n-1; j++) {
            printf("%d ", n_matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}

