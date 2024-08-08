
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    translate(lang)
  })
})

const translate = (lang) => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;
  $.ajax({
    type: 'GET',
    url: url,
    success: function(result) {
      console.log('here')
      console.log(result)
     $('DIV#hello').text(result.hello);
    }
  })
}

