document.querySelector('#add_item').addEventListener('click', function () {
  let newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(newItem);
});
