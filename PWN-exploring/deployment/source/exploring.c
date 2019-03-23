#include <stdio.h>
#include <stdlib.h>

int main(){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    printf("The Earth is moving towards the deep space!\n");
    printf("We should explore the unknown!\n");
    char text[64];
    fgets(text,64,stdin);
    printf(text);
    fgets(text,64,stdin);
    printf(text);
    return 0;
}
