const button = document.getElementById('button-from');
const form1 = document.querySelector('#form1');
const inputUser = document.querySelector('#inputUser');
const user = document.querySelector('#user');
form1.addEventListener('submit', function(e) {
    e.preventDefault();
    user.innerText = inputUser.value;
})


const addButton = document.querySelector('#addButton');
const post = document.querySelector('#post');
const categoryList = document.querySelector('#category_list');
const main_form = document.querySelector('#main_form');
const table = document.querySelector('#table');

main_form.addEventListener("submit", e => {
    e.preventDefault();
    //alert(categoryList.value)
    const newRow = document.createElement('tr');
    const newName = document.createElement('td');
    newName.innerText = Name;
    const newTopic = document.createElement('td');
    newTopic = categoryList.value;
    const newData = document.createElement('td');
    newData = post.value;
    newRow.append(newName);
    newRow.append(newTopic);
    newRow.append(newData);
    table.append(newRow);
})