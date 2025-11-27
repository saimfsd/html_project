#include <stdio.h> 
void functionOne(){
    int  i  ; 
    int num[13] = {100 , 900 , 800 , 700 , 600 , 500 , 400 , 50 , 60 , 40 , 80 , 60 , 40 } ;
    char roman[13][3] ={"hh","hh","hh","hh","hh","hh","hh","hh","hh","hh","hh","hh","hh"};
    for(i = 0 ; i < 13 ; i++){
        printf("%d == %s \n" , num[i] , roman[i] );
    }
    
}

int main (){
    functionOne();
    return 0 ; 
}