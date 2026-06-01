(function() {
  var path = window.location.pathname;
  var inGuides = path.indexOf('/guides/') !== -1;
  var root = inGuides ? '../' : '';
  var guideRoot = root + 'guides/';

  var calculators = [
    { href: '',                              label: 'DCA' },
    { href: 'position-size.html',            label: 'Position size' },
    { href: 'compound-interest.html',        label: 'Compound interest' },
    { href: 'dca-backtest.html',             label: 'DCA backtest' },
    { href: 'loss-recovery-calculator.html', label: 'Loss recovery' },
    { href: 'drip-calculator.html',          label: 'DRIP' },
    { href: 'inflation-calculator.html',     label: 'Real returns' },
    { href: 'asset-allocation.html',         label: 'Asset allocation' },
    { href: 'fire-calculator.html',          label: 'FIRE' }
  ];

  var guides = [
    { href: 'what-is-dollar-cost-averaging.html',            label: 'What is dollar cost averaging?' },
    { href: 'how-compound-interest-works.html',              label: 'How compound interest works' },
    { href: 'dca-vs-lump-sum.html',                          label: 'DCA vs lump sum investing' },
    { href: 'how-to-calculate-position-size.html',           label: 'How to calculate position size' },
    { href: 'how-to-invest-in-a-volatile-market.html',       label: 'How to invest in a volatile market' },
    { href: 'bitcoin-dca-strategy.html',                     label: 'Bitcoin DCA strategy' },
    { href: 'how-to-invest-during-geopolitical-uncertainty.html', label: 'Investing during uncertainty' },
    { href: 'fear-greed-index-dca-strategy.html',            label: 'Fear &amp; Greed Index DCA' },
    { href: 'what-is-a-good-risk-reward-ratio.html',         label: 'Risk/reward ratio' },
    { href: 'strategic-bitcoin-reserve-dca.html',            label: 'Strategic Bitcoin Reserve' },
    { href: 'investing-during-high-interest-rates.html',     label: 'High interest rates' },
    { href: 'ethereum-glamsterdam-upgrade-2026.html',         label: 'Ethereum Glamsterdam' },
    { href: 'ai-stocks-vs-traditional-value.html',           label: 'AI vs Value stocks' },
    { href: 'should-you-dca-into-ai-crypto-tokens.html',     label: 'DCA into AI crypto' },
    { href: 'best-day-to-dca-bitcoin.html',                  label: 'Best day to DCA' }
  ];

  // Build desktop nav links
  var calcLinks = calculators.map(function(c) {
    return '<a href="' + root + c.href + '">' + c.label + '</a>';
  }).join('\n    ');

  // Build dropdown items
  var dropdownItems = guides.map(function(g) {
    return '<a href="' + guideRoot + g.href + '">' + g.label + '</a>';
  }).join('\n        ');
  dropdownItems += '\n        <a href="' + guideRoot + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>';

  // Build mobile menu links
  var mobileCalcLinks = calculators.map(function(c) {
    return '<a href="' + root + c.href + '">' + c.label + '</a>';
  }).join('\n  ');

  var mobileGuideLinks = guides.map(function(g) {
    return '<a href="' + guideRoot + g.href + '">' + g.label + '</a>';
  }).join('\n  ');
  mobileGuideLinks += '\n  <a href="' + guideRoot + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>';

  // Desktop nav HTML (goes inside header via nav-root)
  var navHtml = '<nav>\n    ' + calcLinks
    + '\n    <div class="dropdown">'
    + '\n      <button class="dropdown-toggle' + (inGuides ? ' active' : '') + '">Guides</button>'
    + '\n      <div class="dropdown-menu">\n        ' + dropdownItems
    + '\n      </div>\n    </div>\n  </nav>'
    + '\n  <button class="nav-hamburger" id="nav-hamburger" aria-label="Open menu" aria-expanded="false">'
    + '\n    <span></span><span></span><span></span>\n  </button>';

  // Mobile menu HTML (must go AFTER header)
  var mobileHtml = '<div class="nav-mobile-menu" id="nav-mobile-menu">\n  '
    + mobileCalcLinks
    + '\n  <span class="mobile-guides-label">Guides</span>\n  '
    + mobileGuideLinks
    + '\n</div>';

  // Inject nav into header
  var el = document.getElementById('nav-root');
  if (el) {
    el.outerHTML = navHtml;
    // Inject mobile menu after header
    var header = document.querySelector('header');
    if (header) {
      var existing = document.getElementById('nav-mobile-menu');
      if (existing) existing.parentNode.removeChild(existing);
      header.insertAdjacentHTML('afterend', mobileHtml);
    }
  }

  // Wire up events after DOM is ready
  document.addEventListener('DOMContentLoaded', function() {
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
    // Dropdown hover
    document.querySelectorAll('.dropdown').forEach(function(dd) {
      var m = dd.querySelector('.dropdown-menu');
      if (!m) return;
      var t;
      dd.addEventListener('mouseenter', function() { clearTimeout(t); m.style.display = 'block'; });
      dd.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
      m.addEventListener('mouseenter', function() { clearTimeout(t); });
      m.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
    });
  });

})();
