"""
implement_nav_js.py
Run from: ~/Desktop/ClaudeWork/mydcacalc/
Usage: python3 ~/Downloads/implement_nav_js.py
"""
import os, re, glob

base = '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc'

# ── 1. CREATE nav.js ──────────────────────────────────────────────────────────
nav_js = r"""(function() {
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
    { href: 'ai-stocks-vs-traditional-value.html',           label: 'AI vs Value stocks' }
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
"""

with open(f'{base}/nav.js', 'w') as f:
    f.write(nav_js)
print("Created: nav.js")

# ── 2. EVENT LISTENER SCRIPT (goes before </body>) ───────────────────────────
NAV_EVENT_JS = """<script>
window.addEventListener('load', function() {
  var btn = document.getElementById('nav-hamburger');
  var menu = document.getElementById('nav-mobile-menu');
  if (!btn || !menu) return;
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
</script>"""

# ── 3. REGEX PATTERNS TO STRIP ───────────────────────────────────────────────
# Match existing hardcoded nav block (desktop nav + hamburger btn)
NAV_PATTERN = re.compile(
    r'<nav>.*?</nav>\s*<button class="nav-hamburger".*?</button>',
    re.DOTALL
)
# Match mobile menu div
MOBILE_MENU_PATTERN = re.compile(
    r'<div class="nav-mobile-menu"[^>]*>.*?</div>',
    re.DOTALL
)
# Match old inline toggleMenu / dropdown JS scripts before </body>
OLD_JS_PATTERN = re.compile(
    r'<script>\s*function toggleMenu\(\).*?</script>\s*',
    re.DOTALL
)
OLD_JS_PATTERN2 = re.compile(
    r'<script>\s*window\.addEventListener\(\'load\'.*?</script>\s*',
    re.DOTALL
)
OLD_DROPDOWN_PATTERN = re.compile(
    r'<script>\s*[\(\[]?.*?dropdown.*?</script>\s*',
    re.DOTALL
)

# ── 4. PROCESS ALL HTML FILES ─────────────────────────────────────────────────
root_files = glob.glob(f'{base}/*.html')
guide_files = glob.glob(f'{base}/guides/*.html')
all_files = root_files + guide_files

fixed = 0
for path in all_files:
    fname = os.path.basename(path)
    in_guides = '/guides/' in path
    rel = '../nav.js' if in_guides else 'nav.js'

    with open(path) as f: c = f.read()

    # Skip non-calculator/guide pages
    if fname in ('privacy.html', 'terms.html'):
        print(f'Skip: {fname}')
        continue

    # A) Replace nav + hamburger btn with nav-root placeholder + script tag
    new_nav = f'<div id="nav-root"></div><script src="{rel}"></script>'
    c2 = NAV_PATTERN.sub('', c)  # remove old nav first
    # Insert nav-root right after <header> opening tag's logo link
    c2 = re.sub(r'(<a [^>]*class="logo"[^>]*>.*?</a>)\s*', r'\1\n  ' + new_nav + '\n  ', c2, count=1)

    # B) Remove old mobile menu div
    c2 = MOBILE_MENU_PATTERN.sub('', c2)

    # C) Remove old inline JS (toggleMenu, load listener, dropdown listeners)
    c2 = OLD_JS_PATTERN.sub('', c2)
    c2 = OLD_JS_PATTERN2.sub('', c2)

    # D) Add new event listener script before </body>
    if 'window.addEventListener' not in c2 or 'nav-hamburger' not in c2:
        c2 = c2.replace('</body>', NAV_EVENT_JS + '\n</body>')

    if c2 != c:
        with open(path, 'w') as f: f.write(c2)
        print(f'Updated: {fname}')
        fixed += 1
    else:
        print(f'No change: {fname}')

print(f'\nDone. {fixed} files updated.')
print('\nNext step: deploy')
print('  cd ~/Desktop/ClaudeWork/mydcacalc')
print('  python3 deploy.py "Implement single-source nav.js"')
