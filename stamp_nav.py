"""
stamp_nav.py — Stamps the correct full nav into any new mydcacalc.com page.

Usage:
  python3 stamp_nav.py fee-calculator.html
  python3 stamp_nav.py guides/new-guide.html
  python3 stamp_nav.py --all        (re-stamps every page in the project)

Run from: ~/Desktop/ClaudeWork/mydcacalc/
"""

import os, re, sys, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# ── CALCULATORS (add new ones here) ──────────────────────────────────────────
CALCULATORS = [
    ('',                              'DCA'),
    ('position-size.html',            'Position size'),
    ('compound-interest.html',        'Compound interest'),
    ('dca-backtest.html',             'DCA backtest'),
    ('loss-recovery-calculator.html', 'Loss recovery'),
    ('drip-calculator.html',          'DRIP'),
    ('inflation-calculator.html',     'Real returns'),
    ('asset-allocation.html',         'Asset allocation'),
    ('fire-calculator.html',          'FIRE'),
    ('rebalancing-calculator.html',   'Rebalancing'),
    ('fee-calculator.html',           'Fee impact'),
]

# ── GUIDES (add new ones here) ────────────────────────────────────────────────
GUIDES = [
    ('what-is-dollar-cost-averaging.html',            'What is dollar cost averaging?'),
    ('how-compound-interest-works.html',              'How compound interest works'),
    ('dca-vs-lump-sum.html',                          'DCA vs lump sum investing'),
    ('how-to-calculate-position-size.html',           'How to calculate position size'),
    ('how-to-invest-in-a-volatile-market.html',       'How to invest in a volatile market'),
    ('bitcoin-dca-strategy.html',                     'Bitcoin DCA strategy'),
    ('how-to-invest-during-geopolitical-uncertainty.html', 'Investing during uncertainty'),
    ('fear-greed-index-dca-strategy.html',            'Fear &amp; Greed Index DCA'),
    ('what-is-a-good-risk-reward-ratio.html',         'Risk/reward ratio'),
    ('strategic-bitcoin-reserve-dca.html',            'Strategic Bitcoin Reserve'),
    ('investing-during-high-interest-rates.html',     'High interest rates'),
    ('ethereum-glamsterdam-upgrade-2026.html',         'Ethereum Glamsterdam'),
    ('ai-stocks-vs-traditional-value.html',           'AI vs Value stocks'),
    ('should-you-dca-into-ai-crypto-tokens.html',     'DCA into AI crypto'),
    ('best-day-to-dca-bitcoin.html',                  'Best day to DCA'),
    ('4-percent-rule-explained.html',                 'The 4% Rule'),
    ('how-to-build-crypto-dca-portfolio.html',      'Crypto DCA portfolio'),
    ('portfolio-diversification-guide.html',        'Portfolio diversification'),
]


def build_nav(root, active_href, in_guides):
    g = root + 'guides/'
    lines = []
    for href, label in CALCULATORS:
        active = ' class="active"' if href == active_href else ''
        lines.append('<a href="' + root + href + '"' + active + '>' + label + '</a>')
    calc_links = '\n    '.join(lines)

    dlines = []
    for href, label in GUIDES:
        dlines.append('<a href="' + g + href + '">' + label + '</a>')
    dlines.append('<a href="' + g + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>')
    dropdown_items = '\n        '.join(dlines)

    active_cls = ' active' if in_guides else ''
    return (
        '<nav>\n    ' + calc_links +
        '\n    <div class="dropdown">'
        '\n      <button class="dropdown-toggle' + active_cls + '">Guides</button>'
        '\n      <div class="dropdown-menu">\n        ' + dropdown_items +
        '\n      </div>\n    </div>\n  </nav>'
        '\n  <button class="nav-hamburger" id="nav-hamburger" aria-label="Open menu" aria-expanded="false">'
        '\n    <span></span><span></span><span></span>\n  </button>'
    )


def build_mobile_menu(root, in_guides):
    g = root + 'guides/'
    calc_lines = []
    for href, label in CALCULATORS:
        calc_lines.append('<a href="' + root + href + '">' + label + '</a>')
    guide_lines = []
    for href, label in GUIDES:
        guide_lines.append('<a href="' + g + href + '">' + label + '</a>')
    guide_lines.append('<a href="' + g + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>')

    return (
        '<div class="nav-mobile-menu" id="nav-mobile-menu">\n  ' +
        '\n  '.join(calc_lines) +
        '\n  <span class="mobile-guides-label">Guides</span>\n  ' +
        '\n  '.join(guide_lines) +
        '\n</div>'
    )


NAV_EVENT_JS = '''<script>
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
</script>'''


def stamp(filepath):
    path = os.path.join(BASE, filepath) if not os.path.isabs(filepath) else filepath
    if not os.path.exists(path):
        print('  ERROR: file not found: ' + path)
        return False

    with open(path) as f:
        c = f.read()

    in_guides = '/guides/' in path.replace(os.sep, '/')
    root = '../' if in_guides else ''
    fname = os.path.basename(path)
    active_href = '' if fname == 'index.html' and not in_guides else fname

    nav_html    = build_nav(root, active_href, in_guides)
    mobile_html = build_mobile_menu(root, in_guides)

    # Replace nav + hamburger button
    c = re.sub(
        r'<nav>.*?</nav>\s*<button class="nav-hamburger".*?</button>',
        nav_html, c, count=1, flags=re.DOTALL
    )
    # Handle old nav-root placeholder
    c = re.sub(
        r'<div id="nav-root"></div><script src="[^"]*nav\.js"></script>\s*<button class="nav-hamburger".*?</button>',
        nav_html, c, count=1, flags=re.DOTALL
    )

    # Replace mobile menu
    c = re.sub(
        r'<div class="nav-mobile-menu"[^>]*>.*?</div>(?=\s*\n)',
        mobile_html, c, count=1, flags=re.DOTALL
    )
    if 'id="nav-mobile-menu"' not in c:
        c = c.replace('</header>', '</header>\n' + mobile_html, 1)

    # Replace or add event listener JS
    c = re.sub(
        r'<script>\s*window\.addEventListener\(\'load\'.*?</script>',
        NAV_EVENT_JS, c, flags=re.DOTALL
    )
    if 'window.addEventListener' not in c:
        c = c.replace('</body>', NAV_EVENT_JS + '\n</body>', 1)

    with open(path, 'w') as f:
        f.write(c)

    print('  ✓ Stamped: ' + filepath)
    return True


def main():
    args = sys.argv[1:]
    if not args or '--help' in args:
        print(__doc__)
        return

    if '--all' in args:
        files = (
            [os.path.relpath(p, BASE) for p in glob.glob(os.path.join(BASE, '*.html'))] +
            [os.path.relpath(p, BASE) for p in glob.glob(os.path.join(BASE, 'guides', '*.html'))]
        )
        skip = {'privacy.html', 'terms.html'}
        files = [f for f in files if os.path.basename(f) not in skip]
        print('Stamping ' + str(len(files)) + ' files...')
        for f in sorted(files):
            stamp(f)
        print('\nDone — ' + str(len(files)) + ' files updated.')
    else:
        for arg in args:
            stamp(arg)
        print('Done.')


if __name__ == '__main__':
    main()
