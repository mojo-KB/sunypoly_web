// function start() {
//     document.getElementById("category_list").addEventListener("change", addActivityItem, false);
// }

// function addActivityItem() {

//     //alert("yeah");
// }

// window.addEventListener("load", start, false);

// const categoryList = document.querySelector('#category_list');
// categoryList.addEventListener('change', (e) => {
//     e.preventDefault();
//     let form = document.getElementById('main_form');
//     let inputHTML = document.createElement('input');
//     inputHTML.name = 'userInput';
//     inputHTML.id = 'userInput';
//     inputHTML.placeholder = 'Enter Item';
//     let buttonHTML = document.createElement('button');
//     buttonHTML.innerHTML = 'submit';
//     form.append(inputHTML, buttonHTML);

//     let ulHTML = document.createElement('ul');
//     ulHTML.id('input_list');
//     form.append(ulHTML);

// });


// const categoryList = document.getElementById('category_list');
// categoryList.addEventListener('change', (e) => {
//     e.preventDefault();
//     document.querySelector('input').placeholder = "Enter item";
//     document.querySelector('button').disabled = false;
// }, false);







// document.querySelector('input').placeholder = "Enter item";
// document.querySelector('button').disabled = false;

// const inputDiv = document.querySelector('#input');
// const inputList = document.querySelector('#input_list');
// const form = document.querySelector('form');


// form.addEventListener('submit', function(e) {
//     e.preventDefault();
//     //alert("hello");
//     const userInput = document.getElementById('userInput');
//     const newItem = document.createElement('li');
//     newItem.append(userInput.value);
//     inputList.append(newItem);
//     //addItem(userInput);
//     userInput.value = '';

// });


// const addItem = (userInput) => {
//     const newItem = document.createElement('li');
//     newItem.append(userInput.value);
//     inputList.append(newItem);
// }

// // event listener for select

const form = document.getElementById('main_form');
const list = document.querySelector('#input_list');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.querySelector('#userInput');
    const newitem = document.createElement('li');
    newitem.innerHTML(input.value);
    list.append(newitem);
    input.value = '';
})