// Scope i JS :

// 1. Global Scope.
// 2. Function Scope or Local Scope.
// 3. Nested Scope.
// 4. Block Scope


// 1. Global Scope:
// console.console.log(place);
var place = "Pune"
console.log(place);
{
    let place = "satara"
    console.log(place);
    console.log(place);
}
console.log(place);


// 2. Function Scope or Local Scope
var native = 'Pune'
function msg() {
    var native = "satara"
    console.log("Hello " + native);
}
msg()
console.log(native);


// 3. Nested Scope.
function parent () {
    console.log("I'm Parent Function...");
    let name = "ABC"

    function child () {
        console .log("I'm Child Function...");
        console.log(name);

        let name2 = "XYZ"
        console.log(name2);     
    }
    child()
}
parent()


// 4. Block Scope:
// Which has been introduced newly.
function outer() {
    let place3 = "Mumbai"
    if(true){
        console.log("Nice City " + place3);
    }
    console.log(place3);
}
outer()
// console.log(place3); // Error will be occur, bcoz it is not define outside the function.

