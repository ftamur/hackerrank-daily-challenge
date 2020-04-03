#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

float _area(triangle tr);

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    int j;
    for (int i=1; i<n; i++) {

        triangle key = tr[i];
        j = i - 1;

        while (j >= 0 && _area(key) < _area(tr[j])){
            
            tr[j+1] = tr[j];
            j--;

        } 

        tr[j+1] = key;

    }

}

float _area(triangle tr){
    float p = (tr.a + tr.b + tr.c) / 2.0;
    return sqrt(p * (p - tr.a) * (p - tr.b) * (p - tr.c));

}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}