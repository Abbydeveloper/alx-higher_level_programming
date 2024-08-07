$(function() { 
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(films){
      $.each(films.results, (i, film) => {
        console.log(film.title)
      });
    }
  })
})
