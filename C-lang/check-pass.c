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