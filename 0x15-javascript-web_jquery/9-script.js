$(function () {
  const lang = $('html').attr('lang');
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
  $.get(url, function (data, textStatus) {
    $('div#hello').text(data.hello);
  });
});
