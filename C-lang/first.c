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

//#include <stdio.h>
int main() {
    printf("Hello Saim!");
    return 0;
}
    
// agar int liya hai function me return karna jaruri hai 

// return version value 

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

// No return value 

#include <stdio.h>

void var(){
    int a = 10;
    int b = 10;
    int sum = a + b;
    printf("Sum = %d\n", sum);
}

int main() {
    var();  // function call
    printf("Try programiz.pro");
    return 0;
}


// basic input output

#include <stdio.h>

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num); // address diya jaha value store hogi
    printf("You entered: %d", num);
    return 0;
}

// basic program

#include <stdio.h>

int main() {
    int n;
    printf("Enter number: ");
    scanf("%d", &n); // input lene ke liye & lagaya
    printf("Value: %d\n", n); // print karte waqt & nahi lagaya
    printf("Address: %p\n", &n); // address print karne ke liye & lagaya
    return 0;
}