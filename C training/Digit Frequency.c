/*
https://www.hackerrank.com/challenges/frequency-of-digits-1/problem?isFullScreen=true
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    
    int i, tmp;
    char c;
    
    for(c='0'; c<='9'; c++){
        tmp = 0;
        for(i = 0; i < strlen(s); i++){
            if(s[i] == c)tmp++;
        }
        printf("%d ", tmp);
    }
    
    
      
    return 0;
}
