/*
https://www.hackerrank.com/challenges/reverse-array-c/problem?isFullScreen=true
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    // int num, *arr, i;
    // scanf("%d", &num);
    // arr = (int*) malloc(num * sizeof(int));
    // for(i = 0; i < num; i++) {
    //     scanf("%d", arr + i);
    // }
    int num = 5;
    int arr[] = {5,4,3,2,1};
    int i;


    /* Write the logic to reverse the array. */

    int temp;
    for(int i = 0; i<num/2; i++){
        temp = arr[i];
        arr[i] = arr[num-i-1];
        arr[num-i-1] = temp;
    }


    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}