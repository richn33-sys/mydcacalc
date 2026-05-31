(function() {
  var path = window.location.pathname;
  var inGuides = path.indexOf('/guides/') !== -1;
  var root = inGuides ? '../' : '';

  var calculators = [
    { href: '',                              label: 'DCA calculator' },
    { href: 'position-size.html',            label: 'Position size' },
    { href: 'compound-interest.html',        label: 'Compound interest' },
    { href: 'dca-backtest.html',             label: 'DCA backtest' },
    { href: 'loss-recovery-calculator.html', label: 'Loss recovery' },
    { href: 'drip-calculator.html',          label: 'DRIP' },
    { href: 'inflation-calculator.html',     label: 'Real returns' },
    { href: 'asset-allocation.html',         label: 'Asset allocation' }
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
    { href: 'should-you-dca-into-ai-crypto-tokens.html',    label: 'DCA into AI crypto' }
  ];

  var guideRoot = root + 'guides/';

  // Build desktop nav links
  var calcLinks = calculators.map(function(c) {
    return '<a href="' + root + c.href + '">' + c.label + '</a>';
  }).join('\n    ');

  // Build dropdown items
  var dropdownItems = guides.map(function(g) {
    return '<a href="' + guideRoot + g.href + '">' + g.label + '</a>';
  }).join('\n        ');
  dropdownItems += '\n        <a href="' + guideRoot + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>';

  // Build mobile menu calc links
  var mobileCalcLinks = calculators.map(function(c) {
    return '<a href="' + root + c.href + '">' + c.label + '</a>';
  }).join('\n  ');

  // Build mobile menu guide links
  var mobileGuideLinks = guides.map(function(g) {
    return '<a href="' + guideRoot + g.href + '">' + g.label + '</a>';
  }).join('\n  ');
  mobileGuideLinks += '\n  <a href="' + guideRoot + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>';

  var html = '<nav>\n    ' + calcLinks + '\n    <div class="dropdown">'
    + '\n      <button class="dropdown-toggle' + (inGuides ? ' active' : '') + '">Guides</button>'
    + '\n      <div class="dropdown-menu">\n        ' + dropdownItems
    + '\n      </div>\n    </div>\n  </nav>'
    + '\n  <button class="nav-hamburger" id="nav-hamburger" aria-label="Open menu" aria-expanded="false">'
    + '\n    <span></span><span></span><span></span>\n  </button>'
    + '\n  <div class="nav-mobile-menu" id="nav-mobile-menu">\n  '
    + mobileCalcLinks
    + '\n  <span class="mobile-guides-label">Guides</span>\n  '
    + mobileGuideLinks
    + '\n  </div>';

  var el = document.getElementById('nav-root');
  if (el) {
    el.outerHTML = html;
  } else {
    document.write(html);
  }
})();
