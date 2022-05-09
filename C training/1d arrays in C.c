/*
https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=true
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int num, *arr, i;
    printf("Enter how many nums:");
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        printf("Enter num #%d:", i+1);
        scanf("%d", arr + i);
    }
    
    int sum = 0;
    
    for(i = 0; i < num; i++)sum+=arr[i];
    printf("%d\n", sum);
        
    return 0;
}