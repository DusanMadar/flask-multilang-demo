$(document).ready(function() {
  $('#lang-selector a').click(function(e) {
    e.preventDefault();
    var langCurrent = window.location.pathname.split('/')[1];
    var langNext = $(this).attr('href').replace('#', '');
    var hrefNext = window.location.href.replace('/' + langCurrent + '/', '/' + langNext + '/');

    var cookieExpires = new Date();
    cookieExpires.setMonth(cookieExpires.getMonth() + 12);
    document.cookie = 'lang=' + langNext + ';expires=' + cookieExpires + ';domain=' + window.location.hostname + ';path=/';
    window.location.replace(hrefNext);
  });
});
