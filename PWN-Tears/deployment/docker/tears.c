#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// gcc -m32 --static -Wl,--omagic -o tears tears.c
// echo 0 > /proc/sys/kernel/randomize_va_space

void hack(){
    system("echo flag");
}

int main(){

    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    alarm(30);

    int lucky_number = 0xdeadbeef;
    int i;
    long long unsigned int *index;
    int value;

    printf("==============================================\n");
    printf("      /\\                                      \n");
    printf("   /\\/ .\\ /\\      Three lines of tears        \n");
    printf("  / .\\   | .\\                                 \n");
    printf(" |    |_/    |             @Keenan            \n");
    printf("  \\__/   \\__/                                 \n");
    printf("==============================================\n");

	printf("Your relative:%p\n", &lucky_number);

    for(i = 0; i < 3; i++){
        printf("Eye  >");
        scanf("%llx", &index);
        printf("Tear >");
        scanf("%d", &value);
        *index = value;
    }

    return 0;
}
