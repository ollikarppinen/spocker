$(function() {
  $('.image-container').hide();
  imagesLoaded('.image-container', function() {
    $('.image-container').show();
    var $container = $('.image-container').masonry({
      itemSelector: '.grid-item',
      columnWidth:'.grid-item',
    });
    $('.fa-spinner').hide();
  });
});
