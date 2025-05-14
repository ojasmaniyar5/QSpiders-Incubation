// Function - the block of code/statemets which performs a some specific task again and again is called as function.
// Function is a reusable block of code that performs a specific task.
// It is a set of statements that can be executed when called.

// Types of functions in JavaScript
// 1. Named Function
// 2. Anonymous Function
// 3. Callback Function
// 4. Higher Order Function


// Syntax of function
let Task = function(x, y) {
    console.log(x + y);
}
Task(10, 20); // Output: 30

// Named Function - A function that is declared with the function keyword is called a function declaration.
function add (x, y) {
    return x + y;
}
console.log(add(10, 20)); // Output: 30


// Anonymous Function - A function that does not have a name is called an anonymous function.
let sum = function (x, y) {
    return x + y;
}
console.log(sum(10, 20)); // Output: 30


// Callback Function - A function that is passed as an argument to another function is called a callback function
function msg () {
    return "Hello World! - "
}

// Higher Order Function - A function that takes another function as an argument or returns a function as its result is called a higher-order function.
function great (greetings, name) {
    console.log(greetings() + name);
}
great(msg, "ABC")
great(msg, "XYZ")
great(msg, "PQR")
great(msg, "LMN")


//--------------------------------------------------------------

// Array - A collection of elements is called an array. It is a data structure that can store multiple values in a single variable.
// An array is a special variable that can hold more than one value at a time.
// It is a list of items that can be of any data type. An array is an ordered collection of values, and it is zero-indexed.
// The first element of an array is at index 0, the second element is at index 1, and so on.
// An array can hold values of different data types, including numbers, strings, objects, and even other arrays.
// An array can be created using the array literal syntax or the array constructor syntax. The array literal syntax is more commonly used.

// Syntax of array
let array = [1, 2, 3, 4, 5]
console.log(array); // Output: [ 1, 2, 3, 4, 5 ]

let place = ["India", "USA", "UK", "China"]
console.log(place); // Output: [ 'India', 'USA', 'UK', 'China' ]

let age = [10, 20, 30, 40, 50]
console.log(age); // Output: [ 10, 20, 30, 40, 50 ]

let studentdetails = ["ABC", 20, "USA", ["Math", "Science"]]
console.log(studentdetails); // Output: [ 'John', 20, 'USA' ]


// Push() - Adds one or more elements to the end of an array and returns the new length of the array.
place.push("Japan")
console.log(place); // Output: [ 'India', 'USA', 'UK', 'China', 'Japan' ]

// Pop() - Removes the last element from an array and returns that element. This method changes the length of the array.
place.pop()
console.log(place); // Output: [ 'India', 'USA', 'UK', 'China' ]

// unshift() - Adds one or more elements to the beginning of an array and returns the new length of the array.
place.unshift("Japan")
console.log(place); // Output: [ 'Japan', 'India', 'USA', 'UK', 'China' ]

// shift() - Removes the first element from an array and returns that removed element. This method changes the length of the array.
place.shift()
console.log(place); // Output: [ 'India', 'USA', 'UK', 'China' ]

//--------------------------------------------------------------

// Slice() - Returns a shallow copy of a portion of an array into a new array object selected from start to end (end not included) where start and end represent the index of items in that array. 
// The original array will not be modified.
console.log(place.slice(1, 3)); // Output: [ 'USA', 'UK' ]

// Splice() - Changes the contents of an array by removing or replacing existing elements and/or adding new elements in place. 
// The original array will be modified.
place.splice(1, 2, "Latur", "Dubai")
console.log(place); // Output: [ 'India', 'Latur', 'Dubai', 'China' ]

//--------------------------------------------------------------

// Itration - The process of going through each element of an array is called iteration.
// Itration Methods - There are several methods available in JavaScript to iterate over an array.
// Some of the commonly used methods are:
// 1. Filter().
// 2. Map().
// 3. Reduce().

// Filter() - Creates a new array with all elements that pass the test implemented by the provided function.
// It is used to filter the elements of an array based on a condition.
// It takes a callback function as an argument, which is called for each element of the array.
// The callback function should return true or false. If it returns true, the element is included in the new array; 
// if it returns false, the element is excluded from the new array.
// The filter() method does not modify the original array; it creates a new array with the filtered elements.
// The filter() method does not execute the function for empty elements
// Example:
// Find Even Numbers from given array.
 let FavNumbers = [5,7,19,18,27,25,10,1,3,6]
console.log(FavNumbers); // Output: [ 5, 7, 19, 18, 27, 25, 10, 1, 3, 6 ]
let evenNumbers = FavNumbers.filter(function(n) {
    return n % 2 == 0;
}
)
console.log(evenNumbers); // Output: [ 18, 10, 6 ]


// Map() - Creates a new array populated with the results of calling a provided function on every element in the calling array.
// It is used to transform the elements of an array into a new array based on a condition.
// It takes a callback function as an argument, which is called for each element of the array.
// The callback function should return the transformed value. The map() method does not modify the original array; 
// it creates a new array with the transformed elements.   
// The map() method does not execute the function for empty elements
// Example1:
let FavNumber = [5,7,19,18,27,25,10,1,3,6]
console.log(FavNumber); // Output: [ 5, 7, 19, 18, 27, 25, 10, 1, 3, 6 ]
let evenNumber = FavNumber.map(function(n) {
    return n % 2 == 0;
}
)
console.log(evenNumber); // Output: [ 0, 0, 0, 1, 0, 0, 1, 0, 0, 1 ]

// Example2:
let FavNum = [5,7,19,18,27,25,10,1,3,6]
console.log(FavNum); // Output: [ 5, 7, 19, 18, 27, 25, 10, 1, 3, 6 ]
let multiplyNum = FavNum.map((n)=> {
    return n * 2
}
)
console.log(multiplyNum); // Output: [ 10, 14, 38, 36, 54, 50, 20, 2, 6, 12 ]


// Reduce() - Executes a reducer function (that you provide) on each element of the array, resulting in a single output value.
// It is used to reduce the elements of an array into a single value based on a condition.
// It takes a callback function as an argument, which is called for each element of the array.
// The callback function should return the reduced value. The reduce() method does not modify the original array;
// it creates a new value with the reduced elements.
// The reduce() method does not execute the function for empty elements
// Example1:
let FavNums = [5, 7, 19, 18, 27, 25, 10, 1, 3, 6];
console.log(FavNums); // Output: [ 5, 7, 19, 18, 27, 25, 10, 1, 3, 6 ]

let sumNum = FavNums.reduce((num, num1) => {
    console.log(num + " --> " + num1);
    return num + num1;
});
console.log(sumNum); // Output: 121

//--------------------------------------------------------------

// Object - A collection of properties is called an object. It is a data structure that can store multiple values in a single variable.
// An object is a collection of key-value pairs, where each key is a string and the value can be of any data type.

// Example:
let students = {
    name: "ABC",
    age: 20,
    country: "India",
    subjects: ["Math", "Science"],
    address : {
        city: "Mumbai",
        state: "Maharashtra",
        country: "India"
    },
    hobbies: ["Reading", "Writing", "Traveling"]
}
console.log(students);
console.log(students.name);
console.log(students.age);
console.log(students.country);
console.log(students.subjects);
console.log(students.address.city);
console.log(students.address.state);
console.log(students.address.country);
console.log(students.hobbies);
console.log(students.hobbies[0]);
console.log(students.hobbies[1]);
console.log(students.hobbies[2]);

// ----------------------------------------------------------------------------------------------------------------------   

let person1 = {
    pname : "OJAS",
    place : "Pune",
    printMsg : function() {
        console.log(`Hello I'm ${this.pname} from ${this.place}`);
    }
}
console.log(person1.pname); // Output: OJAS
console.log(person1.place); // Output: Pune
person1.printMsg(); // Output: Hello I'm OJAS from Pune

let person22 = {
    pname : "ABC",
    place : "Mumbai",
}
person1.printMsg.call(person22); // Output: Hello I'm ABC from Mumbai

// call() method - The call() method is a built-in JavaScript method that allows you to call a function with a specified this value and arguments provided individually.
// It is used to invoke a function with a specific context (this value) and pass arguments to it.
// The call() method is useful for borrowing methods from one object and using them in another object.
// It allows you to set the value of this inside the function to a specific object, enabling you to access properties and methods of that object.
// The call() method takes the first argument as the value of this and the subsequent arguments as the arguments to be passed to the function being called.

// Object - A collection of properties is called an object. It is a data structure that can store multiple values in a single variable.
// An object is a collection of key-value pairs, where each key is a string and the value can be of any data type.

// Example:
let studentdetailss = {
    name: "ABC",
    age: 20,
    country: "India",
    subjects: ["Math", "Science"],
    address : {
        city: "Mumbai",
        state: "Maharashtra",
        country: "India"
    },
    hobbies: ["Reading", "Writing", "Traveling"]
}
console.log(studentdetailss);
console.log(studentdetailss.name);
console.log(studentdetailss.age);
console.log(studentdetailss.country);
console.log(studentdetailss.subjects);
console.log(studentdetailss.address.city);
console.log(studentdetailss.address.state);
console.log(studentdetailss.address.country);
console.log(studentdetailss.hobbies);
console.log(studentdetailss.hobbies[0]);
console.log(studentdetailss.hobbies[1]);
console.log(studentdetailss.hobbies[2]);


// ----------------------------------------------------------------------------------------------------------------------   

let person = {
    pname : "OJAS",
    place : "Pune",
    printMsg : function() {
        console.log(`Hello I'm ${this.pname} from ${this.place}`);
    }
}
console.log(person.pname); // Output: OJAS
console.log(person.place); // Output: Pune
person.printMsg(); // Output: Hello I'm OJAS from Pune

let person2 = {
    pname : "ABC",
    place : "Mumbai",
}
person.printMsg.call(person2); // Output: Hello I'm ABC from Mumbai

// call() method - The call() method is a built-in JavaScript method that allows you to call a function with a specified this value and arguments provided individually.
// It is used to invoke a function with a specific context (this value) and pass arguments to it.
// The call() method is useful for borrowing methods from one object and using them in another object.
// It allows you to set the value of this inside the function to a specific object, enabling you to access properties and methods of that object.
// The call() method takes the first argument as the value of this and the subsequent arguments as the arguments to be passed to the function being called.

// -------------------------------------------------------------------------------------------------------------------

// DOM: