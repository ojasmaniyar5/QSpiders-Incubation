// let Username = document.querySelector("#user") // get the input field
// let Password = document.querySelector("#pass") 
// let Form = document.querySelector("#form")
// console.log(Form) // check if the form is selected

// Form.addEventListener("submit", (ele)=>{
//     ele.preventDefault() // prevent default form submission
//     let user = Username.value // get the value of the input field
//     let pass = Password.value 
//     // console.log(user); // check if the value is 
//     // console.log(pass); 

//     let userDetails = {
//         Username : user,
//         Password : pass
//     }
//     console.log(userDetails)
// })

// let input = document.getElementById("user")
// console.log(input);

// input.addEventListener('keypress', (ele)=>{
//     input.style.backgroundColor = 'red'
// })

// input.addEventListener('keyup', (ele)=>{
//     input.style.backgroundColor = 'brown'
// })

// ..............................................................


let  sc = document.getElementById("SelectColor")

sc.addEventListener("change",(e)=>{
    document.body.style.backgroundColor = sc.value
})