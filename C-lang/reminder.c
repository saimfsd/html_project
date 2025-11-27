#include <stdio.h>
    void function (){
          int array[16], input, i = 0;
    printf("Enter a number: ");
    scanf("%d", &input);

    while (input > 0) {
        array[i] = input % 2;  // remainder store karo
        input = input / 2;     // divide by 2
        i++;
    }

    printf("Binary number: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", array[j]);
    }
    }
int main() {
function () ; 
    return 0;
}

c logic