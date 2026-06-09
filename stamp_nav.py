"""
stamp_nav.py — Stamps the correct full nav into any mydcacalc.com page.

Usage:
  python3 stamp_nav.py fee-calculator.html
  python3 stamp_nav.py guides/new-guide.html
  python3 stamp_nav.py --all

Run from: ~/Desktop/ClaudeWork/mydcacalc/
"""

import os, re, sys, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# ── CALCULATOR CATEGORIES ─────────────────────────────────────────────────────
CALC_CATEGORIES = [
    ('Investing', [
        ('',                              'DCA calculator'),
        ('dca-backtest.html',             'DCA backtest'),
        ('compound-interest.html',        'Compound interest'),
        ('loss-recovery-calculator.html', 'Loss recovery'),
        ('crypto-cost-basis-calculator.html', 'Crypto cost basis'),
    ]),
    ('Portfolio', [
        ('asset-allocation.html',         'Asset allocation'),
        ('rebalancing-calculator.html',   'Rebalancing'),
        ('position-size.html',            'Position size'),
    ]),
    ('Retirement &amp; Tax', [
        ('fire-calculator.html',              'FIRE calculator'),
        ('fee-calculator.html',               'Fee impact'),
        ('tax-loss-harvesting-calculator.html', 'Tax-loss harvesting'),
    ]),
    ('Income', [
        ('drip-calculator.html',          'DRIP'),
        ('inflation-calculator.html',     'Real returns'),
    ]),
]

# ── GUIDES ────────────────────────────────────────────────────────────────────
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
    ('how-to-build-crypto-dca-portfolio.html',        'Crypto DCA portfolio'),
    ('portfolio-diversification-guide.html',          'Portfolio diversification'),
    ('tax-loss-harvesting-explained.html',            'Tax-loss harvesting'),
]

# ── CSS for grouped dropdowns ─────────────────────────────────────────────────
GROUPED_NAV_CSS = '''
/* ── GROUPED NAV DROPDOWNS ── */
.nav-group { position: relative; }
.nav-group-toggle { font-size: 13px; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; gap: 4px; background: none; border: none; font-family: var(--font-body); padding: 0; transition: color 0.15s; }
.nav-group-toggle:hover, .nav-group-toggle.active { color: var(--text); }
.nav-group-toggle::after { content: "▾"; font-size: 10px; }
.nav-group-menu { display: none; position: absolute; top: 100%; left: 0; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); min-width: 220px; overflow: hidden; z-index: 200; padding: 4px 0; }
.nav-group-menu .group-label { padding: 8px 14px 4px; font-size: 10px; font-family: var(--font-mono); color: var(--accent); letter-spacing: 0.08em; text-transform: uppercase; }
.nav-group-menu a { display: block; padding: 9px 14px; font-size: 13px; color: var(--text-muted); text-decoration: none; border-bottom: 1px solid var(--border); transition: all 0.15s; }
.nav-group-menu a:last-child { border-bottom: none; }
.nav-group-menu a:hover { background: var(--bg-input); color: var(--text); }
.nav-group-menu .group-divider { height: 1px; background: var(--border); margin: 2px 0; }
/* Guides dropdown (right-aligned) */
.dropdown { position: relative; }
.dropdown-toggle { font-size: 13px; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; gap: 4px; background: none; border: none; font-family: var(--font-body); padding: 0; transition: color 0.15s; }
.dropdown-toggle:hover, .dropdown-toggle.active { color: var(--text); }
.dropdown-toggle::after { content: "▾"; font-size: 10px; }
.dropdown-menu { display: none; position: absolute; top: 100%; right: 0; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); min-width: 280px; overflow: hidden; z-index: 200; padding: 4px 0; }
.dropdown-menu a { display: block; padding: 11px 16px; font-size: 13px; color: var(--text-muted); text-decoration: none; border-bottom: 1px solid var(--border); transition: all 0.15s; }
.dropdown-menu a:last-child { border-bottom: none; }
.dropdown-menu a:hover { background: var(--bg-input); color: var(--text); }
'''

NAV_EVENT_JS = '''<script>
window.addEventListener('load', function() {
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
  // Calculator group dropdowns
  document.querySelectorAll('.nav-group').forEach(function(ng) {
    var m = ng.querySelector('.nav-group-menu');
    if (!m) return;
    var t;
    ng.addEventListener('mouseenter', function() { clearTimeout(t); m.style.display = 'block'; });
    ng.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
    m.addEventListener('mouseenter', function() { clearTimeout(t); });
    m.addEventListener('mouseleave', function() { t = setTimeout(function() { m.style.display = 'none'; }, 300); });
  });
  // Guides dropdown
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


def build_nav(root, in_guides, active_href):
    g = root + 'guides/'
    lines = ['<nav>']

    # Calculator category dropdowns
    for cat_name, items in CALC_CATEGORIES:
        # Check if any item in this category is the active page
        cat_active = any(href == active_href for href, label in items)
        active_cls = ' active' if cat_active else ''
        lines.append('  <div class="nav-group">')
        lines.append('    <button class="nav-group-toggle' + active_cls + '">' + cat_name + '</button>')
        lines.append('    <div class="nav-group-menu">')
        for href, label in items:
            active_attr = ' class="active"' if href == active_href else ''
            lines.append('      <a href="' + root + href + '"' + active_attr + '>' + label + '</a>')
        lines.append('    </div>')
        lines.append('  </div>')

    # Guides dropdown (right-aligned)
    guides_active = ' active' if in_guides else ''
    lines.append('  <div class="dropdown">')
    lines.append('    <button class="dropdown-toggle' + guides_active + '">Guides</button>')
    lines.append('    <div class="dropdown-menu">')
    for href, label in GUIDES:
        lines.append('      <a href="' + g + href + '">' + label + '</a>')
    lines.append('      <a href="' + g + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>')
    lines.append('    </div>')
    lines.append('  </div>')

    # Hamburger
    lines.append('</nav>')
    lines.append('<button class="nav-hamburger" id="nav-hamburger" aria-label="Open menu" aria-expanded="false">')
    lines.append('  <span></span><span></span><span></span>')
    lines.append('</button>')

    return '\n  '.join(lines)


def build_mobile_menu(root, in_guides):
    g = root + 'guides/'
    lines = ['<div class="nav-mobile-menu" id="nav-mobile-menu">']

    for cat_name, items in CALC_CATEGORIES:
        lines.append('  <span class="mobile-guides-label">' + cat_name.replace('&amp;', '&') + '</span>')
        for href, label in items:
            lines.append('  <a href="' + root + href + '">' + label + '</a>')

    lines.append('  <span class="mobile-guides-label">Guides</span>')
    for href, label in GUIDES:
        lines.append('  <a href="' + g + href + '">' + label + '</a>')
    lines.append('  <a href="' + g + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>')
    lines.append('</div>')
    return '\n'.join(lines)


def ensure_css(c):
    """Inject grouped nav CSS if not already present."""
    if 'nav-group-toggle' not in c:
        c = c.replace('</style>', GROUPED_NAV_CSS + '\n</style>', 1)
    return c


def stamp(filepath):
    path = os.path.join(BASE, filepath) if not os.path.isabs(filepath) else filepath
    if not os.path.exists(path):
        print('  ERROR: not found: ' + path)
        return False

    with open(path) as f:
        c = f.read()

    in_guides = '/guides/' in path.replace(os.sep, '/')
    root = '../' if in_guides else ''
    fname = os.path.basename(path)
    active_href = '' if fname == 'index.html' and not in_guides else fname

    nav_html    = build_nav(root, in_guides, active_href)
    mobile_html = build_mobile_menu(root, in_guides)

    # Inject CSS
    c = ensure_css(c)

    # Replace nav + hamburger
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

    # Replace or add event JS
    c = re.sub(
        r'<script>\s*window\.addEventListener\(\'load\'.*?</script>',
        NAV_EVENT_JS, c, flags=re.DOTALL
    )
    if 'window.addEventListener' not in c:
        c = c.replace('</body>', NAV_EVENT_JS + '\n</body>', 1)

    with open(path, 'w') as f:
        f.write(c)

    print('  ✓ ' + filepath)
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
