// Day 1

//What is JavaScript?
// JavaScript is a high-level, dynamic, untyped, and interpreted programming language.
// It is a multi-paradigm language, supporting event-driven, functional, and imperative programming styles.
// JavaScript is a prototype-based language, and it has first-class functions. 
// It is widely used for web development, server-side development, and game development.
// It is an essential part of web applications, enabling interactive web pages and dynamic content.
// JavaScript is an ECMAScript standard, and it is supported by all modern web browsers.
// ECMAScript stands for European Computer Manufacturers Association Script, and it is a standard for scripting languages.
// The first edition of ECMAScript was published in 1997, and it has gone through several revisions since then.
// The latest version of ECMAScript is ES2023, which was released in June 2023.
// JavaScript is a versatile language, and it can be used for both front-end and back-end development.
// It is commonly used with HTML and CSS to create interactive web pages.
// JavaScript can also be used with frameworks and libraries such as React, Angular, and Vue.js for front-end development.
// For back-end development, JavaScript can be used with Node.js, which is a JavaScript runtime built on Chrome's V8 engine.


//--------------------------------------------------------------
// Declaration of variables
var a

// Initialization of variables
a = 1

// Re-Initialization of variables
a = 2

// Re-Declaration of variables
var a = 3

console.log(a) // Output: 3

//--------------------------------------------------------------
// list down the data types in JavaScript
// 1. Number
// 2. String
// 3. Boolean
// 4. Undefined
// 5. Null
// 6. Symbol
// 7. Object
// 8. BigInt (added in ES2020
// 9. Literal (added in ES2020) also known as Template Literals.


// Basic program by using Number data type
var a = 10 // Number
var b = 2 // Number
var c = a + b // Number
console.log(c) // Output: 12


// Basic program by using String data type
var name = "ABC" // String
console.log(name) // Output: ABC


// Basic program by using Boolean data type
var isTrue = true // Boolean
var isFalse = false // Boolean
var isEqual = (a == b) // Boolean
var isNotEqual = (a != b) // Boolean
console.log(isTrue) // Output: true
console.log(isFalse) // Output: false
console.log(isEqual) // Output: false
console.log(isNotEqual) // Output: true


// Basic program by using Undefined data type
// Undefined - A variable that has been declared but has not yet been assigned a value is called undefined.
// It is a special value that indicates the absence of a value or an uninitialized variable.
var x // Undefined
console.log(x) // Output: undefined


// Basic program by using Null data type
// Null - A variable that has been assigned a null value is called null. It is a special value that indicates the absence of any object value.
// It is a primitive value that represents the intentional absence of any object value.
var y = null // Null
console.log(y) // Output: null


// Basic program by using Symbol data type
// Symbol - A unique and immutable primitive value that can be used as the key of an object property. It is a new data type introduced in ES6 (ECMAScript 2015).
// Symbols are often used to create private properties in objects, as they are not accessible by any other code.
var sym = Symbol("description") // Symbol
console.log(sym) // Output: Symbol(description)


// Basic program by using Object data type
// Object - A collection of key-value pairs. It is a complex data type that can store multiple values in a single variable.
// An object is a collection of properties, where each property has a name (key) and a value. The value can be of any data type, including other objects.
var obj = { name: "OJAS", age: 21 } // Object
console.log(obj) // Output: { name: 'OJAS', age: 21 }


// Basic program by using BigInt data type
// BigInt - A built-in object that provides a way to represent whole numbers larger than 2^53 - 1. It is a new data type introduced in ES2020 (ECMAScript 2020).
// BigInt is used for large integers that cannot be represented by the Number data type. It is created by appending "n" to the end of an integer literal or by using the BigInt() constructor.
var bigInt = 8010782571400125791346n // BigInt
console.log(bigInt) // Output: 8010782571400125791346n


// Basic program by using Literal data type
// Literal - A literal is a fixed value that is represented directly in the code. It is a way to represent a value in the source code.
// Literals can be of different types, including numeric literals, string literals, boolean literals, and object literals. They are used to represent constant values in the code.
var literal = 10 // Literal
console.log(literal) // Output: 10

// Day 2

//--------------------------------------------------------------

// Hoisting in JavaScript
// Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compile phase.
// This means that you can use variables and functions before they are declared in the code. 
// In summary, hoisting is a JavaScript mechanism that allows you to use variables and functions before they are declared in the code.
// Is hoisting is possible in JavaScript? Yes, hoisting is possible in JavaScript because of the way JavaScript handles variable and function declarations during the compile phase.

// Example of hoisting:
var x = 5; // Variable declaration and initialization
console.log(x); // Output: 5


//--------------------------------------------------------------

// Function - the block of code/statemets which performs a some specific task again and again is called as function.
// Function is a reusable block of code that performs a specific task.
// It is a set of statements that can be executed when called.

// Advantages of functions in JavaScript:
// 1. Code Reusability: Functions allow you to write code once and reuse it multiple times, reducing redundancy and improving maintainability.
// 2. Modularity: Functions help break down complex tasks into smaller, manageable pieces, making the code easier to understand and maintain.
// 3. Abstraction: Functions provide a way to hide implementation details, allowing you to focus on the high-level logic of your code.
// 4. Scope: Functions create their own scope, which helps avoid variable name conflicts and keeps the global scope clean.
// 5. Testing and Debugging: Functions can be tested and debugged independently, making it easier to identify and fix issues in your code.

// Disadvantages of functions in JavaScript:
// 1. Performance Overhead: Function calls can introduce a performance overhead, especially if they are called frequently or in tight loops.
// 2. Complexity: Overusing functions can lead to code that is difficult to follow, especially if the functions are not well-named or documented.
// 3. Scope Issues: Functions create their own scope, which can lead to confusion if not properly managed, especially with closures and variable hoisting.
// 4. Callback Hell: Using too many nested functions or callbacks can lead to "callback hell," making the code difficult to read and maintain.
// 5. Memory Usage: Functions can consume memory, especially if they create closures or retain references to large objects, leading to potential memory leaks.


//--------------------------------------------------------------

// Syntax of function
// let FunctionName = function (parameters) {
//     // Function body
// }
// FunctionName(arguments) // Function call

// What is parameter and argument in JavaScript?
// Parameter - A parameter is a variable that is used in the function definition. 
// It acts as a placeholder for the value that will be passed to the function when it is called.
// Parameters are defined in the function declaration and are used to receive input values when the function is invoked.

// Argument - An argument is the actual value that is passed to the function when it is called.
// Arguments are the real values that are passed to the function when it is invoked.
// They are the data that the function uses to perform its task. Arguments can be literals, variables, or expressions.

//--------------------------------------------------------------

// Example of function declaration
function add(x, y) {
    console.log(x + y); // Output: 30    
}
add(50, 20); // Function call with arguments 10 and 20.

//--------------------------------------------------------------
// Nan:
// NaN - NaN stands for "Not a Number." It is a special value in JavaScript that represents an undefined or unrepresentable value in numerical calculations.
// NaN is a property of the global object, and it is a number type. 
// It is used to indicate that a value is not a valid number or cannot be represented as a number.
// NaN is the result of an invalid mathematical operation, such as dividing zero by zero or trying to parse a non-numeric string as a number.
// It is important to note that NaN is not equal to any value, including itself.
// This means that the expression NaN === NaN will return false.
// To check if a value is NaN, you can use the isNaN() function or the Number.isNaN() method.
// The isNaN() function checks if a value is NaN or not, while the Number.isNaN() method checks if a value is NaN and of type number.

//--------------------------------------------------------------
// Example of function expression:
function Task (a = 10, b = 20) {
    // Function declaration with default parameters
    console.log(a + b); // Output: 30
}
Task(100, 200); // Function call with arguments 100 and 200.
// Explaination: In this example, the function Task is declared with two parameters a and b, which have default values of 10 and 20 respectively.
// When the function is called with arguments 100 and 200, the values of a and b are overridden by the provided arguments, resulting in an output of 300.


//--------------------------------------------------------------

function Task (m, n) {
    var m = 50;
    var n = 80;
    console.log(m + n);
    console.log(m - n);
}
Task()
// Explaination: In this example, the function Task is declared with two parameters m and n. 
// Inside the function, the variables m and n are re-declared and assigned new values of 50 and 80 respectively.
// When the function is called without any arguments, the default values of m and n are used, resulting in an output of 130 for addition and -30 for subtraction.


// --------------------------------------------------------------

// Types of functions in JavaScript
// 1. Named Function.
// 2. Anonymous Function.
// 3. First-Class Function : Also Called as First Citizen Function and Funtion with Expression.


// ---------------------------------------------------------------

// 1. Named Function - A function that has a name is called a named function.
// It is declared using the function keyword followed by the function name and parentheses.
// Named functions are hoisted, meaning they can be called before they are declared in the code.
// Named functions are useful for creating reusable code and improving code readability.
// Example of named function:
function ope(name) {
    console.log(`hello ${name}`); // Output: hello OJAS
}
ope("ABC"); // Function call with argument "ABC"


// 2. Anonymous Function - A function that does not have a name is called an anonymous function.
// It is declared using the function keyword followed by parentheses and is often assigned to a variable or passed as an argument to another function.
// Anonymous functions are not hoisted, meaning they cannot be called before they are declared in the code.
// Anonymous functions are useful for creating one-time-use functions or callbacks.

// 3. First-Class Function - A function that can be treated as a value is called a first-class function.
// It means that functions can be assigned to variables, passed as arguments to other functions, and returned from other functions.
// First-class functions are a key feature of JavaScript and enable functional programming techniques.


// ---------------------------------------------------------------

// Arrow Function - A concise way to write functions in JavaScript using the arrow syntax introduced in ES6 (ECMAScript 2015).
// This is most used funtion in javascript.
// Arrow functions are anonymous functions that do not have their own this context, making them useful for certain use cases, such as callbacks and higher-order functions.
// Syntax of arrow function:
// const functionName = (parameters) => {
//     // Function body
// }
// Example of arrow function:
let pqr = (p, q) => {
    console.log(p + q); // Output: 30
}
pqr(20, 20) // Function call with arguments 10 and 20.


// ---------------------------------------------------------------

// Nested Function - A function that is defined inside another function is called a nested function.
// Nested functions can access variables and parameters of their parent function, creating a closure.
// This allows for encapsulation and data hiding, as the inner function can access the outer function's variables but not vice versa.

// Syntax of nested function:
// function outerFunction() {
//     function innerFunction() {
//         // Inner function body
//     }
//     // Outer function body
// }
// }

// Example of nested function:
function outerFunction() {
    console.log("Outer function"); // Output: Outer function
    function innerFunction() {
        console.log("Inner function"); // Output: Inner function
    }
    innerFunction(); // Calling inner function
}
outerFunction(); // Calling outer function


// ---------------------------------------------------------------

