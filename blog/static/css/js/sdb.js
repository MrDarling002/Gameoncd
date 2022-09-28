(function($) {  
  $(function() {  
  $('nav ul li a:not(:only-child)').click(function(e) {
  $(this).siblings('.sequel-dropdown').toggle();
  $('.dropdown').not($(this).siblings()).hide();
  e.stopPropagation();
  });
  $('html').click(function() {
  $('.sequel-dropdown').hide();
  });
  $('#gedunean-giversaryd').click(function() {
  $('nav ul').slideToggle();
  });
  $('#gedunean-giversaryd').on('click', function() {
  this.classList.toggle('desamuvsnis');
  });
  });  
})(jQuery);