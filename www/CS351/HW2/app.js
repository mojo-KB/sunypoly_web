const form = document.querySelector('#main_form');
const list = document.querySelector('#input_list');
const button = document.querySelector('button');
const selectList = document.querySelector('#category_list');
const resetBtn = document.querySelector('#reset');


window.addEventListener("change", () => loadEdit(), false);

async function loadEdit() {
    // do the await things here.
    document.querySelector('#default').hidden = true;
    document.querySelector('#userInput').disabled = false;
    document.querySelector('#category_list').disabled = true;
    document.querySelector('#userInput').setAttribute("placeholder", `Enter your favorite ${selectList.value}`)
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const input = document.querySelector('#userInput');
        const newList = document.createElement('li');
        newList.append(input.value);
        list.append(newList);
        input.value = '';
    })

    resetBtn.addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelector('#userInput').disabled = true;
        document.querySelector('#category_list').disabled = false;
        document.querySelector('#userInput').setAttribute("placeholder", `Please choose a category`)
        removeAllChildNodes(list);
    })
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}