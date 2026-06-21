(function() {
  function init() {
    // Hamburger
    var btn = document.getElementById('nav-hamburger');
    var menu = document.getElementById('nav-mobile-menu');
    if (btn && menu) {
      btn.addEventListener('click', function() {
        var open = menu.classList.toggle('open');
        btn.classList.toggle('open', open);
        btn.setAttribute('aria-expanded', String(open));
        document.body.style.overflow = open ? 'hidden' : '';
      });
      menu.querySelectorAll('a').forEach(function(a) {
        a.addEventListener('click', function() {
          menu.classList.remove('open');
          btn.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        });
      });
    }
    // Dropdowns
    function hookDropdown(selector, menuSelector) {
      document.querySelectorAll(selector).forEach(function(el) {
        var m = el.querySelector(menuSelector);
        if (!m) return;
        var t;
        el.addEventListener('mouseenter', function() { clearTimeout(t); m.style.display = 'block'; });
        el.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
        m.addEventListener('mouseenter', function() { clearTimeout(t); });
        m.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
      });
    }
    hookDropdown('.nav-group', '.nav-group-menu');
    hookDropdown('.dropdown', '.dropdown-menu');
    // Accordion guide categories
    document.querySelectorAll('.guide-cat-header').forEach(function(hdr) {
      hdr.addEventListener('click', function(e) {
        e.stopPropagation();
        var links = hdr.nextElementSibling;
        var isOpen = hdr.classList.contains('open');
        document.querySelectorAll('.guide-cat-header').forEach(function(h) {
          h.classList.remove('open');
          if (h.nextElementSibling) h.nextElementSibling.classList.remove('open');
        });
        if (!isOpen) {
          hdr.classList.add('open');
          if (links) links.classList.add('open');
        }
      });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
