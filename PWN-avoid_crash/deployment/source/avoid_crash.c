#include <stdio.h>
#include <unistd.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

double m=5.965e+24, r=6400.0;
double M, R;
double pi = 3.141592653589793;

double get_rocky_limit(){
    double res = 1.0;
    double rho_M, rho_m;
    if (M==0 || R==0){
        printf("It is ridiculous!\n");
        return 0;
    }
    else{
        rho_M = 3.0*M/(4*pi*R*R*R);
        rho_m = 3.0*m/(4*pi*r*r*r);
        res = pow(2*rho_M/rho_m, 1.0/3) * R;
        return res;
    }
}

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    srand(time(0));
}

int randint(int min, int max){
    return rand()%(max-min) + min;
}

double randfloat(int min, int max){
    double prefix = randint(1000, 10000)/1000.0;
    int power = randint(min, max);
    return prefix * pow(10, power);
}

void banner(){
    M = randfloat(25, 30);
    R = randfloat(3, 6);
    printf("The earth is moving towards the deep space of the universe and encounters a new planet.\n");
    printf("As we all know, the mass of the earth is %Ekg, and the radius of the earth is %.1fkm.\n", m, r);
    //printf("The mass of the new planet is %Ekg, and the radius of the new planet is %.1fkm\n", M, R);
}

int check(){
    char rocky_limit[1024];
    char caculated_data[1024];
    int len;
    for(int i=0; i<10; i++){
        memset(rocky_limit, 0, 1024);
        memset(caculated_data, 0, 1024);
        printf("Wandering...\n");
        banner();
        sprintf(rocky_limit, "%e", get_rocky_limit());
        //printf("%s\n", rocky_limit);
        printf("The rocky limit is: ");
        len = read(0, caculated_data, 1024);
        caculated_data[len-1]=0;
        if(strcmp(rocky_limit, caculated_data)==0){
            continue;
        }else{
            printf("The value you caculated is wrong!\n");
            return 0;
        }

    }
    return 1;
}

void main(){
    init();
    if(check()){
        FILE *fp;
        char FLAG[256];
        if((fp=fopen("flag", "r"))!=NULL){
            fgets(FLAG, 256, fp);
            printf("Congratulations! The flag is %s\n", FLAG);
        }
    }
}