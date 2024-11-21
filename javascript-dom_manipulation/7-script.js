fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const movies = data.results;
    const listMovies = document.querySelector('#list_movies');
    movies.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch((error) => console.error('Error:', error));
