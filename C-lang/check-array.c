#include <stdio.h>

void exampleOne() {
    int userAge = 20;
    int num, arrOne[20], arrTwo[20], i, product = 0;

    printf("Enter array size:\n");
    scanf("%d", &num);

    printf("Enter numbers for array one:\n");
    for(i = 0; i < num; i++) {
        scanf("%d", &arrOne[i]);
    }

    printf("Enter numbers for array two:\n");
    for(i = 0; i < num; i++) {
        scanf("%d", &arrTwo[i]);
    }

    printf("Product of two arrays:\n");
    for(i = 0; i < num; i++) {
        product = arrOne[i] * arrTwo[i];
        printf("%d ", product);
    }

    printf("\n");
}

int main() {
    exampleOne();      
    return 0;
}