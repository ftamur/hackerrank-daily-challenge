#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int has_next(int start, int len, char **s);
void swap(int i_1, int i_2, char **s);
void reversed(int start, const int len, char **arr);
void algorithm(int start, int n, char **s);

int next_permutation(int n, char **s){
    /**
    * Complete this method
    * Return 0 when there is no next permutation and 1 otherwise
    * Modify array s to its next permutation
    */

    if (has_next(0, n, s)){   
        algorithm(1, n, s);
        return 1;
    }

    return 0;
        
}

void algorithm(int start, int n, char **s){

    if (n - start == 2){
  
        if (strcmp(s[n-2], s[n-1]) < 0){
          swap(n - 1, n - 2, s);
        }else{

            if (strcmp(s[n-3], s[n-1]) >= 0){
              swap(n - 3, n - 2, s);
              swap(n - 2, n - 1, s);
            }else{
              swap(n - 3, n - 1, s);
              swap(n - 2, n - 1, s);
            }

        }

    }else if (has_next(start, n, s))
        return algorithm(start+1, n, s);
    else {
        int j = n-1;

        while (strcmp(s[start-1], s[j]) >= 0)
            --j;

        swap(start - 1, j, s);
        reversed(start, n, s); 

    }
}

void swap(int i_1, int i_2, char **s) {
    char *temp = s[i_1];
    s[i_1] = s[i_2];
    s[i_2] = temp;
}

int has_next(int start, int len, char **s){

    for (int i=start; i<len-1; i++)
        if (strcmp(s[i], s[i+1]) < 0)
            return 1;

    return 0;

}

void reversed(int start, const int len, char **arr){

    for (int i = 0; i<(len-start)/2; i++) {
      swap(start + i, len - i - 1, arr);
    }
    
}


int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}