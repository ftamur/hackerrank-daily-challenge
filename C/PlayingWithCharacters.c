#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char ch;
    char word[10];
    char sentence[100];

    scanf("%c\n", &ch);
    scanf("%s\n", word);
    scanf("%[^\n]%*c\n", sentence);

    printf("%c\n", ch);
    printf("%s\n", word);
    printf("%s\n", sentence);

    return 0;

}

