#include <stdio.h>
#include <string.h>

int main() {
    char str1[50], str2[50];

    printf("Enter first string: ");
    scanf("%s", str1);

    printf("Enter second string: ");
    scanf("%s", str2);

    // Compare the strings
    if (strcmp(str1, str2) == 0) {
        printf("Both strings are equal.\n");
    } 
    else {
        printf("Strings are not equal.\n");
    }

    return 0;
}

// Second example 
#include <stdio.h>
#include <string.h>

int main() {
    char password[20];

    printf("Enter your password: ");
    scanf("%s", password);

    if (strcmp(password, "Saim123") == 0) {
        printf("Access Granted ✅\n");
    } else {
        printf("Access Denied ❌\n");
    }

    return 0;
}

// City problems 
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