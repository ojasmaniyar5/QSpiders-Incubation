// DOM - Stands for Document Object Model is a programming interface that represents an HTML or XML document as a tree of objects..
// It allows JavaScript and other programming languages to access, modify, and interact with the content, structure, and style of web pages dynamically.

// By Using getElementById()
let head = document.getElementById("head")
console.log(head);
head.style.color = 'red'
head.style.backgroundColor = 'cyan'

// By Using getElementsByClassName()
let head2 = document.getElementsByClassName("head2")
console.log(head2);
head2[1].style.color = "red"
head2[1].style.backgroundColor = 'cyan'

// By Using getElementsByTagName()
let div = document.getElementsByTagName("div")
console.log(div);

// By Using querySelectorAll()
let image = document.querySelectorAll(".img")
console.log.apply(image);
image.forEach(element => {
    element.style.border = "3px Solid "
    element.style.borderRadius = "10px"
});

// By Using appendchild() to create any tag using JS to showcase the content or output on web page.
let h1 = document.createElement("h1")
document.body.appendChild(h1)
console.log(h1);
h1.innerHTML = "Hey, I'm Ojas."
h1.style.color = "yello"
h1.style.fontSize = "35px"

// To print img by using JS
let imagee = document.createElement("img")
document.body.appendChild(imagee)
imagee.setAttribute("src", "./RE.avif")
imagee.style.height = ("350px")
imagee.style.border = ("3px Solid")
imagee.style.borderRadius = ("15px")

// To print audio by using js
let audio = document.createElement("audio")
document.body.appendChild(audio)
audio.setAttribute("src", "./Millionaire.m4a")
audio.setAttribute("controls", "true")
audio.style.marginBottom = ("-50px")
audio.style.marginLeft = ("-230px")

// To print video by using js
let video = document.createElement("video")
document.body.appendChild(video)
video.setAttribute("src", "./canvacode.mp4")
video.style.height = ("500px")
video.style.borderRadius = ("15px")


// To print ol and ul tags by using js
let ol = document.createElement("ul")
document.body.appendChild(ol)

let li = document.createElement("li")
ol.appendChild(li)
li.innerHTML = "ABC"

let li2 = document.createElement("li")
ol.appendChild(li2)
li2.innerHTML = "XYZ"

let li3 = document.createElement("li")
ol.appendChild(li3)
li3.innerHTML = "PQR"

ol.setAttribute("type", "circle")


// To print table by using js
let table = document.createElement("table")
document.body.appendChild(table)

let th = document.createElement("th")
table.appendChild(th)
th.innerHTML = "Sr No."

let th1 = document.createElement("th")
table.appendChild(th1)
th1.innerHTML = "Name"

let th2 = document.createElement("th")
table.appendChild(th2)
th2.innerHTML = "Address"

let th3 = document.createElement("th")
table.appendChild(th3)
th3.innerHTML = "Phone No."

table.setAttribute("border", "2")

// Enterd data in table by using js


// Events in js
// 1. onclick : This event is used to call a function when an element is clicked.
function changemsg () {
    let h1 = document.createElement("h1")
    h1.innerHTML = "Welcome to my website/webpage..!"
    document.body.appendChild(h1)

    // To remove the h1 tag
    h1.addEventListener("click", ()=>{
        h1.remove()
    })
}


// Task : create two buttons one for displying an image and second for removeing an image ?

// First button for displaying an image.
let btn1 = document.createElement("button")
btn1.innerHTML = "Display Image"
document.body.appendChild(btn1)

// Second button for removing an image.
let btn2 = document.createElement("button")
btn2.innerHTML = "Remove Image"
document.body.appendChild(btn2)

// Function for displaying an image.
btn1.addEventListener("click", ()=>{
    let img = document.createElement("img")
    img.src = "./RE.avif"
    document.body.appendChild(img)
    img.style.height = "300px"
    img.style.border = "3px Solid"
    img.style.borderRadius = "15px"

    // To remove the image
    btn2.addEventListener("click", ()=>{
        img.remove()
    })
})

// To print the timeout msg by using js ?
// function msg(name, nextName) {
//     setTimeout(()=>{
//         console.log("Hello "+ name);
//         if(nextName){ // if nextName is true then it will print the nextName
//             nextName()
//         }
//     }, 1000) // 1000 is the time in miliseconds
// }
// msg("ABC" , ()=>{ // This is a callback function
//     msg("DEF", ()=>{
//         msg("PQR", ()=>{
//             msg("XYZ")
//         })
//     })
// })


// Promsie in js ?
// Promise is a function that returns an object that has a then method. 
// When the promise is resolved, the then method is called with the resolved value. 
// If the promise is rejected, the then method is called with the reason for the rejection.

let promise = new Promise((resolve, reject)=>{
    let bike = "Bullet"
    if(bike){
        resolve("Bike is available")
    }
    else{
        
        reject("Bike is not available")
    }
})
console.log(promise)
// .then () is used to get the value of the promise
promise.then(() => {
    console.log("Bike is available")
    
})  
// .catch() is used to handle the error
promise.catch(()=>{
        console.log("Bike is not available")
})



// Writig Promise by using function ?
function msg(name, nextName){
    return new Promise((resolve, reject)=>{
        setTimeout(() =>{
            console.log("Hello "+ name);
            if(nextName){ // if nextName is true then it will print the nextName
                nextName()
        }
        resolve()
        }, 1000) // 1000 is the time in miliseconds
    })
}
async function getName() {
    await msg("-> ABC")
    await msg("-> DEF")
    await msg("-> GHI")
    await msg("-> JKL")
    await msg("-> MNO")
    await msg("-> PQR")
    await msg("-> STU")
    await msg("-> VWX")
    await msg("-> YZ..")
}
getName()

// What is the use of await ?
// The await keyword is used to pause the execution of the code until the promise is resolved or rejected .
// It is used with async function to make the code look synchronous.
// It is used to wait for the promise to be resolved or rejected before moving to the next line.

// What is async function ?
// An async function is a function that returns a promise.
// It is used to make the code look synchronous.
// It is used to handle the promise in a more readable way.

// What is the use of async/await ?
// The async/await is used to handle the promise in a more readable way.
// It is used to make the code look synchronous.
// It is used to pause the execution of the code until the promise is resolved or rejected.

// What is callback hell ?
// Callback hell is a situation where we have multiple callbacks inside each other.
// It is a situation where we have multiple nested callbacks.
// It is a situation where we have multiple callbacks inside each other.
// It is a situation where we have multiple nested callbacks.
// It is a situation where we have multiple callbacks inside each other.

