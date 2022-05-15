#include <stdio.h>
#define MAX 64

int main() 
{

    char c; char s[MAX]; char sen[MAX*2];
    c = getchar();
    getchar();
    printf("%c\n", c);
    
    gets(s);
    puts(s);

    gets(sen);
    puts(sen);
    
    return 0;
}