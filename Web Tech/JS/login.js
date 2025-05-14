// let button = document.getElementById("button")

// button.addEventListener("click", (ele) =>{
//     ele.preventDefault()
//     console.log(ele);
//     console.log(window.location.pathname);
//     window.location.pathname = "dom.html"
// })

let button = document.getElementById("btn");

button.addEventListener("click", (event) => {
    event.preventDefault(); // prevents default behavior (like form submission)
    console.log(event); // logs the event object
    console.log(window.location.pathname); // current path
    window.location.pathname = "dom.html"; // navigates to dom.html
});



// // Input
let arr = [1,2,3,4,5,6,7,8,9]

// // output
// [3,2,1,6,5,4,9,8,7]


let first = arr.slice(0,3).reverse()
let second = arr.slice(3,6).reverse()
let third = arr.slice(6.9).reverse()
let result = first.concat(second,third)
console.log(result);