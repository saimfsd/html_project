// arithmatic operator-------------------------------------------------------------------------

// addition 
//var a = 10;
//var b = 20;
//var c = a + b;
//console.log("The sum of " + a + " and " + b + " is " + c);

// substraction
//var a = 10;
var b = 20;
var c = a - b;
console.log("The substraction of " + a + " and " + b + " is " + c);

// multiplication
var a = 10;
var b = 20;
var c = a * b;
console.log("The multiplication of " + a + " and " + b + " is " + c);

// division
var a = 10;
var b = 20;
var c = a / b;
console.log("The division of " + a + " and " + b + " is " + c);

// modulus
var a = 10;
var b = 20;
var c = a % b;
console.log("The modulus of " + a + " and " + b + " is " + c);

// exponent
var a = 10;
var b = 20;
var c = a ** b;
console.log("The exponent of " + a + " and " + b + " is " + c);

// increment
var a = 10;
var c = a++;
console.log("The increment of " + a + " is " + c);

// decrement
var a = 10;
var c = a--;
console.log("The decrement of " + a + " is " + c);

console.log("==========================================")

// comparison operator-------------------------------------------------------------------------
// greaterthan 
var a = 100;
var b = 20;
var c = a > b;
console.log("The comparison of " + a + " > " + b + " is " + c);

// less than
var a = 100;
var b = 20;
var c = a < b;
console.log("The comparison of " + a + " < " + b + " is " + c);

// greater than equal to
var a = 100;
var b = 20;
var c = a >= b;
console.log("The comparison of " + a + " >= " + b + " is " + c);

// less than equal to
var a = 100;
var b = 20;
var c = a <= b;
console.log("The comparison of " + a + " <= " + b + " is " + c);

// equal to
var a = 100;
var b = 20;
var c = a == b;
console.log("The comparison of " + a + " == " + b + " is " + c);

// not equal to
var a = 100;
var b = 20;
var c = a != b;
console.log("The comparison of " + a + " != " + b + " is " + c);

// triple equal to
var a = 100;
var b = 20;
var c = a === b;
console.log("The comparison of " + a + " === " + b + " is " + c);

console.log("==========================================")

// Assignment operator----------------------------------------------------

// equal to
var a = 100;
var b = 20;
var c = a = b;
console.log("The comparison of " + a + " = " + b + " is " + c);

// addition equal to
var math = 100;
var science = 20;
 var c = math + science;
console.log("The comparison of " + math + " += " + science + " is " + c);

// substraction equal to
var a = 1000;
var b = 200;
var c = a - b;
console.log("The comparison of " + a + " -= " + b + " is " + c);

// multiplication equal to
var a = 100;
var b = 20;
var c = a * b;
console.log("The comparison of " + a + " *= " + b + " is " + c);

// division equal to
var a = 100;
var b = 20;
var c = a / b;
console.log("The comparison of " + a + " /= " + b + " is " + c);

console.log("==========================================")

// Logical operator---------------------------------------------------------------------------

// and
// var a = 110;
// var b = 20;
// var x = a + b;
// var y = 120;
// var d = a > b;
// var e = (x == y) && d;
// console.log("The comparison of " + a + " && " + b + " is " + e);

var username = "user";
var password = "1234";
var x = (username == "user") && (password == "1234");
console.log("The comparison of " + username + " && " + password + " is " + x);

// or
var a = 20;
var b = 100;
var x = a + b;
var d = a > b;
var e = (x == 120) || d;
console.log("The comparison of " + a + " || " + b + " is " + e);

// not
var a = 20;
var b = 0;
var x = a + b;
var e = x !== 20;
console.log("The comparison of " + a + " ! " + b + " is " + e);

// example on logical operator

function discountChecker(){
    var cartPrice = document.getElementById("cartPrice").value;
    var member = document.getElementById("member").checked;

    if(cartPrice >=5000 && member == true){
        document.getElementById("display").innerHTML = "Discount applies";
    }
    else{
        document.getElementById("display").innerHTML = "Discount not applies";
    }
}

// bitwise operators-----------------------------------------------------------------------------------

// bitwise and operator

var a = 10;
if((a & 1) == 0){
    console.log("The number is even");
}
else{
    console.log("The number is odd");
}

// bitwise or operator
var a = 10;
var b = 50;
var c = (a | b)
console.log(c);
