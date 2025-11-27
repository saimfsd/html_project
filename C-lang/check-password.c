#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
    bool ispresent = false; 
    char string[30];
    int i;

    printf("Enter a string: ");
    scanf("%s", string);

    for (i = 0; string[i] != '\0'; i++) {
        if (string[i] >= '0' && string[i] <= '9') {
            ispresent = true;
            break; // no need to continue
        }
    }

    if (ispresent == true) {
        printf("Number is present in password");
    } else {
        printf("No number in password");
    }

    return 0;
}