#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    char str[100];
    int count = 0;

    printf("Enter a string : ");
    fgets(str, 5, stdin);

    for(i = 0; i <= strlen(str); i++){
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' 
        && str[i+1] == 'a' || str[i+1] == 'e' || str[i+1] == 'i' || str[i+1] == 'o' || str[i+1] == 'u'
        )
        count++;
    }
}