const button = document.querySelector('.edit-button');
const emptyForm = document.querySelector('.edit-form');

button.addEventListener("click", () => {
  emptyForm.classList.toggle('edit-comment')
})