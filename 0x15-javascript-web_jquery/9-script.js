$(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (data, textStatus) {
    $('div#hello').text(data.hello);
  });
});
