$('div#add_item').click(function () {
  const listItem = $('<li></li>').text('Item');
  $('ul.my_list').append(listItem);
});
