// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // ---------------------------
    // 🔹 VARIABLE DECLARATION
    // ---------------------------
    int age = 21;              // integer variable
    float height = 5.9;        // float variable (decimal value)
    char grade = 'A';          // character variable
    double salary = 50000.75;  // double variable (large decimal)
    int marks[5] = {85, 90, 78, 88, 92}; // array of integers

   
    //  OUTPUT USING printf()

    printf("=== DATA TYPES AND VARIABLES IN C ===\n\n");

    printf("1. Integer (int)       : %d\n", age);
    printf("2. Floating Point (float): %.1f\n", height);
    printf("3. Character (char)    : %c\n", grade);
    printf("4. Double (double)     : %.2lf\n", salary);

    printf("\n5. Array (int marks[5]) : ");
    for(int i = 0; i < 5; i++) {
        printf("%d ", marks[i]);
    }


    //  EXPLANATION (FOR REVISION)
    // ---------------------------
    printf("\n\n===== QUICK NOTES =====\n");



    printf("👉 int     → stores whole numbers (4 bytes)\n");
    printf("👉 float   → stores decimal numbers (4 bytes)\n");
    printf("👉 char    → stores single character (1 byte)\n");
    printf("👉 double  → stores large decimals (8 bytes)\n");
    printf("👉 array   → stores multiple values of same type\n");

    return 0;
};


