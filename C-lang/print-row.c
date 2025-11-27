#include <stdio.h>

int main() {
    int i, j;

    for (i = 1; i <= 5; i++) {        // Row control
        for (j = 1; j <= (2*i - 1); j++) {  // Number of times to print per row
            printf("%d", i);           // Print the same number in a row
        }
        printf("\n");                  // New line after each row
    }

    return 0;
}