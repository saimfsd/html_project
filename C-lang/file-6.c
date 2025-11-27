// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // -----------------------------------------
    // 🔹 STEP 1: Variable Declaration
    // -----------------------------------------
    int age;           // for whole number
    float marks;       // for decimal number
    char grade;        // for single character

    // -----------------------------------------
    // 🔹 STEP 2: Taking Input from User
    // -----------------------------------------
    printf("=== INPUT SECTION ===\n");

    printf("Enter your age (integer): ");
    scanf("%d", &age);          // & means "address of variable age"

    printf("Enter your marks (float): ");
    scanf("%f", &marks);        // & means "address of variable marks"

    printf("Enter your grade (character): ");
    scanf(" %c", &grade);       // space before %c to skip newline

    // -----------------------------------------
    // 🔹 STEP 3: Displaying Output on Screen
    // -----------------------------------------
    printf("\n=== OUTPUT SECTION ===\n");
    printf("Your Age   : %d\n", age);
    printf("Your Marks : %.2f\n", marks);
    printf("Your Grade : %c\n", grade);

    // -----------------------------------------
    // 🔹 STEP 4: Revision Notes
    // -----------------------------------------
    printf("\n=== QUICK NOTES ===\n");
    printf("👉 scanf() is used for INPUT.\n");
    printf("👉 printf() is used for OUTPUT.\n");
    printf("👉 '&' gives the address of variable (needed in scanf).\n");
    printf("👉 Format Specifiers:\n");
    printf("   %%d = int, %%f = float, %%c = char, %%lf = double.\n");

    return 0;
}