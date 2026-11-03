// Portfolio site: no build step, no tracking, no external resources.
// Smooth scroll, scroll reveal, and project filter.
document.querySelectorAll('a[href^="#"]').forEach(function(a){
  a.addEventListener('click', function(e){
    var t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
});

// Scroll reveal: sections fade in as you scroll to them.
var sections = document.querySelectorAll('main section');
sections.forEach(function(s){ s.classList.add('reveal'); });
if ('IntersectionObserver' in window) {
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {threshold: 0.12});
  sections.forEach(function(s){ observer.observe(s); });
} else {
  sections.forEach(function(s){ s.classList.add('visible'); });
}

// Project filter: All / Advanced / Platform / SRE
var buttons = document.querySelectorAll('.filter-btn');
var cards = document.querySelectorAll('#projects .card');
buttons.forEach(function(btn){
  btn.addEventListener('click', function(){
    buttons.forEach(function(b){ b.classList.remove('active'); });
    btn.classList.add('active');
    var filter = btn.getAttribute('data-filter');
    cards.forEach(function(card){
      var cats = (card.getAttribute('data-category') || '').split(' ');
      card.style.display = (filter === 'all' || cats.indexOf(filter) !== -1) ? '' : 'none';
    });
  });
});
console.log('Avinash Nandhyala portfolio loaded.');
