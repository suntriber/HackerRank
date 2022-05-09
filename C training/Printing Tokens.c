/*
https://www.hackerrank.com/challenges/printing-tokens-/problem?isFullScreen=true
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    //Write your logic to print the tokens of the sentence here.
    
    char * token = strtok(s, " ");
   // loop through the string to extract all other tokens
   while( token != NULL ) {
      printf( "%s\n", token ); //printing each token
      token = strtok(NULL, " ");
   }
    return 0;
}