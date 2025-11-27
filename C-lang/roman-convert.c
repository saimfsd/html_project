// Online C compiler to run C program online
#include <stdio.h>
#include <string.h>

 void functionOne(){

     int i , num ; 
     char c[20] = "I"; 
     char c2[2] = "V" ; 
     char str[20] = "";
     printf("Ente a number : ") ;
     scanf("%d" , &num);
     
     for (i = 0 ; i < num ; i ++){
         strcat(str , c) ; 
         printf("%d = %s \n" , i, str);
     }
     if(num == 4){
         char str[10] = "" ; 
         num = num-3 ; 
         for(int i = 1 ; i <= num ; i ++){
             strcat(str , c ) ; 
             strcat(str , c2 ) ; 
             printf("%d = %s \n , str ) ; 
         }
         
     }
     
 }

int main() {
    // Write C code here
 functionOne();
    printf("Try programiz.pro");

    return 0;
}