#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int check_arr_equal(int len, char **s, char **s2);
int has_next(int start, int len, char **s);
void copy_array(int len, char **s, char **s2);
void reverse_elements(int i_1, int i_2, char **s);
void array_sort(int start, const int len, char** arr);
void print_array(int len, char **s);
void reversed(int start, int len, char **s);

void algorithm(int start, int n, char **s, int j);

int next_permutation(int n, char **s){
	/**
	* Complete this method
	* Return 0 when there is no next permutation and 1 otherwise
	* Modify array s to its next permutation
	*/

    char **s2 = calloc(n, sizeof(char *));

    for (int i=0; i<n; i++){
         s2[i] = calloc(11, sizeof(char));
    }

    copy_array(n, s, s2);

    if (has_next(0, n, s)){

        do {
            
            algorithm(1, n, s, n-1);
            sleep(1);
        
        }while (check_arr_equal(n, s, s2));

        return 1;
    }

    return 0;
        
}

void algorithm(int start, int n, char **s, int j){

    if (n - start == 2){
  
        if (strcmp(s[n-2], s[n-1]) < 0){
            reverse_elements(n-1, n-2, s);
        }else{

            if (strcmp(s[n-3], s[n-1]) >= 0){
                reverse_elements(n-3, n-2, s);
                reverse_elements(n-2, n-1, s);
            }else{
                reverse_elements(n-3, n-1, s);
                reverse_elements(n-2, n-1, s);
            }

        }

    }else if (has_next(start, n, s)){
        return algorithm(start+1, n, s, n-start);}
    else {
        
       int j = n-1;

        while (strcmp(s[start-1], s[j]) >= 0)
            j--;

        reverse_elements(start-1, j, s);
        array_sort(start, n, s);
        
        j--;
        
    }

}

void reversed(int start, const int len, char **arr){

    for (int i = 0; i<(len-start)/2; i++) {
        reverse_elements(start+i, len-i-1, arr);
    }
    

}

void array_sort(int start, const int len, char** arr){

    int index, j;
    char *str;

    for (int i=start+1; i<len; i++){

        str = arr[i];
        j = i - 1;

        while (j >= start && strcmp(arr[j], str) > 0){
            
            arr[j+1] = arr[j];
            j--;

        }

        arr[j+1] = str;

    }

}

void reverse_elements(int i_1, int i_2, char **s){

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


int check_arr_equal(int len, char **s, char **s2){

    for (int i=0; i<len; i++){
        if (strcmp(s[i], s2[i]) != 0)
            return 0;
    }

    return 1;
}

void copy_array(int len, char **s, char **s2){

    for (int i=0; i<len; i++){
        s2[i] = s[i];
    }

}

void print_array(int len, char **s){
    for (int i=0; i<len-1; i++){
        printf("%s - ", s[i]);
    }
    printf("%s\n", s[len-1]);
}
