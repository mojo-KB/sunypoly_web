// document.getElementById("myinputred").oninput = function() {
//     var value = (this.value - this.min) / (this.max - this.min) * 100
//     this.style.background = 'linear-gradient(to right, #ff0000 0%, #ff0000 ' + value + '%, #fff ' + value + '%, white 100%)'
// };
// document.getElementById("myinputgreen").oninput = function() {
//     var value = (this.value - this.min) / (this.max - this.min) * 100
//     this.style.background = 'linear-gradient(to right, #00ff00 0%, #00ff00 ' + value + '%, #fff ' + value + '%, white 100%)'
// };
// document.getElementById("myinputblue").oninput = function() {
//     var value = (this.value - this.min) / (this.max - this.min) * 100
//     this.style.background = 'linear-gradient(to right, #00ff 0%, #00f ' + value + '%, #fff ' + value + '%, white 100%)'
// };


const button = document.querySelector('button');
const h1 = document.querySelector('h1');


button.addEventListener('click', function() {
    const newColor = randomColor();
    document.body.style.backgroundColor = newColor;
    h1.innerText = newColor;
})

const randomColor = () => {
    const r = Math.floor(Math.random() * 255);
    const g = Math.floor(Math.random() * 255);
    const b = Math.floor(Math.random() * 255);
    return `rgb(${r}, ${g}, ${b})`;
}