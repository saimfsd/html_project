#include <stdio.h>

int main() {
    int array[5];
    int i, inputMark;
    int totalMarks = 0;
    float percentage;

    // Taking 5 inputs
    for (i = 0; i < 5; i++) {
        printf("Enter a number: ");
        scanf("%d", &inputMark);
        array[i] = inputMark;
    }

    // Calculate total
    for (i = 0; i < 5; i++) {
        totalMarks += array[i];
    }

    // Calculate percentage
    percentage = (totalMarks / 500.0) * 100;

    // Output
    printf("Total Marks = %d\n", totalMarks);
    printf("Percentage = %.2f\n", percentage);

    return 0;
}
