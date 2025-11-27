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