// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here
    int arr[20],i,num ;
    printf("Enter an a number : ");
    scanf("%d", &num);
    
    printf("Enter a number: \n");
    for(int i = 0 ; i < num ; i++){
        scanf("%d", &arr[i]);
    }
    for (int i = 0 ; i < num ; i++ ){
        printf("%d" , &arr[i]);
    }
    return 0 ;
}