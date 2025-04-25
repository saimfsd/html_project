#include <stdio.h>
int main(){
    int a,b,c, temp;


    a = 100;
    b = 200;

    printf("a = %d \n", a);
    printf("b = %d \n", b);

    temp = a ;
    a = b;
    b = temp;

    printf("upadated a = %d \n", a);
    printf("upadated b = %d \n", b);

return 0;

}