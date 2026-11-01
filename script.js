// Portfolio site: no build step, no tracking. Smooth scroll for in-page links.
document.querySelectorAll('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
});
console.log('Avinash Nandhyala portfolio loaded.');
