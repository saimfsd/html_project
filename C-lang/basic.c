switch (day) {
    case 1: printf("Monday\n"); break;
    case 2: printf("Tuesday\n"); break;
    default: printf("Invalid day\n");
}

// second 
if (marks >= 75) {
    printf("Distinction\n");
} else if (marks >= 60) {
    printf("First Class\n");
} else if (marks >= 40) {
    printf("Pass\n");
} else {
    printf("Fail\n");
}

// THird
#include <stdio.h>
#include <string.h>

int main() {
    char city1[30], city2[30];

    printf("Enter first city: ");
    scanf("%s", city1);

    printf("Enter second city: ");
    scanf("%s", city2);

    if (strcmp(city1, city2) == 0) {
        printf("Both cities are same.\n");
    } else {
        printf("Cities are different.\n");
    }

    return 0;
}

//Four 
#include <stdio.h>   // Header file (for input-output functions)

int main() {         // Main function (program execution starts here)
    
    // Variable declaration
    int a, b, sum;
    
    // Input
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    
    // Processing
    sum = a + b;
    
    // Output
    printf("Sum = %d", sum);
    
    return 0;        // End of main function
}


//Sum 
#include <stdio.h>

int var(){
    int a = 10; 
    int b = 10; 
    int sum = a + b; 
    printf("Sum = %d\n", sum);
    return sum;
}

int main() {
    int result = var();   // function call
    printf("Returned value = %d\n", result);
    return 0;
}