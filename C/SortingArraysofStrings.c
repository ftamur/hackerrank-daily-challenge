#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int lexicographic_sort(const char* a, const char* b) {

    char lower_a[strlen(a)];
    char lower_b[strlen(b)];

    for (int i=0; i<strlen(a); i++)
        lower_a[i] = tolower(a[i]);

    for (int i=0; i<strlen(b); i++)
        lower_b[i] = tolower(b[i]);

    if (strlen(a) > strlen(b)){
        for (int i=0; i<strlen(b); i++){
            if (lower_b[i] > lower_a[i])
                return 0;
            else if (lower_b[i] < lower_a[i])
                return 1;
        } 

        return 1;

    }else{
        for (int i=0; i<strlen(a); i++){
            if (lower_b[i] > lower_a[i])
                return 0;
            else if (lower_b[i] < lower_a[i])
                return 1;
        }  

        return 0;

    }

}


int lexicographic_sort_reverse(const char* a, const char* b) {
    return !lexicographic_sort(a, b);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {

    char lower_a[strlen(a)];
    char lower_b[strlen(b)];

    for (int i=0; i<strlen(a); i++)
        lower_a[i] = tolower(a[i]);

    for (int i=0; i<strlen(b); i++)
        lower_b[i] = tolower(b[i]);

    char distincts_a[26] = {0};
    char distincts_b[26] = {0};

    int ascii_a = 97;
    
    for (int i=0; i<strlen(a); i++)
        if (distincts_a[(int) lower_a[i] - ascii_a] != 1)
            distincts_a[(int) lower_a[i] - ascii_a] = 1;
        
    for (int i=0; i<strlen(b); i++)
        if (distincts_b[(int) lower_b[i] - ascii_a] != 1)
            distincts_b[(int) lower_b[i] - ascii_a] = 1;

    int a_distincts = 0;
    int b_distincts = 0;

    for (int i=0; i<26; i++){
        if (distincts_a[i] == 1)
            a_distincts++;
        if (distincts_b[i] == 1)
            b_distincts++;
    }
    
    if (a_distincts > b_distincts)
        return 1;
    else if (b_distincts > a_distincts)
        return 0;
    else
        return lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    if (strlen(a) > strlen(b))
        return 1;
    else if (strlen(b) > strlen(a))
        return 0;
    else
        return lexicographic_sort(a, b);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){

    int index, j;
    char *str;

    for (int i=1; i<len; i++){

        str = arr[i];
        j = i - 1;

        while (j >= 0 && cmp_func(arr[j], str)){
            
            arr[j+1] = arr[j];
            j--;

        }

        arr[j+1] = str;

    }

}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}