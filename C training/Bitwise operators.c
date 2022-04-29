/*
https://www.hackerrank.com/challenges/bitwise-operators-in-c/problem?isFullScreen=true
*/

#include <stdio.h>

/*
* For each number i from 1 through n
* Find the maximum value of and, or, xor
* When compared to all integers greater than i
* Consider a value only if the comparison results
* is less than k
*/

void calculate_the_maximum(int n, int k);

int main() {
    int n, k;
  
    // scanf("%d %d", &n, &k);
    n = 5;
    k = 4;

    calculate_the_maximum(n, k);
 
    return 0;
}

void calculate_the_maximum(int n, int k) {
    int maxAnd = 0;
    int maxOr = 0;
    int maxXor = 0;

    for (int i = 1; i <= n; i++){

      for (int j = i+1; j <= n; j++){

        if ((i & j) > maxAnd && (i & j) < k) maxAnd = (i & j);
        if ((i | j) > maxOr && (i | j) < k) maxOr = (i | j);
        if ((i ^ j) > maxXor && (i ^ j) < k) maxXor = (i ^ j);

      }
    }
    printf("%d\n", maxAnd);
    printf("%d\n", maxOr);
    printf("%d\n", maxXor);

}