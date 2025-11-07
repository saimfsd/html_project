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

// Check Even or odd
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
 //Check number postitive or negative

 #include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num > 0)
        printf("Positive number.\n");
    else if (num < 0)
        printf("Negative number.\n");
    else
        printf("Number is Zero.\n");

    return 0;
}
//Check below number 

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

// Check leap year 
#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        printf("%d is a Leap Year.\n", year);
    else
        printf("%d is NOT a Leap Year.\n", year);

    return 0;
//Ladder



    if (marks >= 75) {
    printf("Distinction\n");
} else if (marks >= 60) {
    printf("First Class\n");
} else if (marks >= 40) {
    printf("Pass\n");
} else {
    printf("Fail\n");
}

//Switch off 
switch (day) {
    case 1: printf("Monday\n"); break;
    case 2: printf("Tuesday\n"); break;
    default: printf("Invalid day\n");
}



}