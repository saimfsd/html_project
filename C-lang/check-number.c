#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    if (a > b)
        printf("%d is greater.\n", a);
    else if (b > a)
        printf("%d is greater.\n", b);
    else
        printf("Both numbers are equal.\n");

    return 0;
}

//Second
#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 2 == 0)
        printf("Number is Even.\n");
    else
        printf("Number is Odd.\n");

    return 0;
}

// Third 
#include <stdio.h>

int main() {
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);

    if (age >= 18) {
        printf("You are eligible to vote.\n");
    } else {
        printf("You are NOT eligible to vote.\n");
    }

    return 0;
}