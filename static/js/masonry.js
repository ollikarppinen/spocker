$(function() {
  imagesLoaded('.image-container', function() {
    var $container = $('.image-container').masonry({
      itemSelector: '.grid-item',
      columnWidth:'.grid-item',
    });
  });
});
