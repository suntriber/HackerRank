/*
https://www.hackerrank.com/challenges/pointer-in-c/problem?isFullScreen=true
*/

#include <stdio.h>

void update(int *a,int *b);

int main(){

    int a, b;
    int *pa = &a, *pb = &b;

    a = 4; b = 5;
    
    // scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}


void update(int *a,int *b) {
    int pa = *a;
    int pb = *b;
     
     pa = *a + *b;
    if (*a - *b < 0) pb = -*a + *b;
    else  pb = *a - *b;

    *a = pa;
    *b = pb;
}
