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
        ('',                                    'DCA calculator'),
        ('dca-backtest.html',                   'DCA backtest'),
        ('compound-interest.html',              'Compound interest'),
        ('loss-recovery-calculator.html',       'Loss recovery'),
        ('crypto-cost-basis-calculator.html',   'Crypto cost basis'),
    ]),
    ('Portfolio', [
        ('asset-allocation.html',               'Asset allocation'),
        ('rebalancing-calculator.html',         'Rebalancing'),
        ('position-size.html',                  'Position size'),
    ]),
    ('Retirement &amp; Tax', [
        ('fire-calculator.html',                    'FIRE calculator'),
        ('withdrawal-rate-calculator.html',         'Withdrawal rate'),
        ('fee-calculator.html',                     'Fee impact'),
        ('tax-loss-harvesting-calculator.html',     'Tax-loss harvesting'),
    ]),
    ('Income', [
        ('drip-calculator.html',                'DRIP'),
        ('inflation-calculator.html',           'Real returns'),
    ]),
]

# ── GUIDE CATEGORIES (accordion dropdown) ────────────────────────────────────
GUIDE_CATEGORIES = [
    ('DCA &amp; Investing', [
        ('what-is-dollar-cost-averaging.html',            'What is dollar cost averaging?'),
        ('dca-vs-lump-sum.html',                          'DCA vs lump sum'),
        ('how-to-invest-in-a-volatile-market.html',       'Investing in a volatile market'),
        ('best-day-to-dca-bitcoin.html',                  'Best day to DCA Bitcoin'),
        ('bitcoin-dca-strategy.html',                     'Bitcoin DCA strategy'),
        ('fear-greed-index-dca-strategy.html',            'Fear &amp; Greed Index DCA'),
    ]),
    ('Crypto', [
        ('how-to-build-crypto-dca-portfolio.html',        'Crypto DCA portfolio'),
        ('should-you-dca-into-ai-crypto-tokens.html',     'DCA into AI crypto'),
        ('crypto-staking-explained.html',                 'Crypto staking yields'),
        ('ethereum-glamsterdam-upgrade-2026.html',         'Ethereum Glamsterdam'),
        ('ai-stocks-vs-traditional-value.html',           'AI vs Value stocks'),
        ('strategic-bitcoin-reserve-dca.html',            'Strategic Bitcoin Reserve'),
    ]),
    ('Retirement &amp; FIRE', [
        ('4-percent-rule-explained.html',                 'The 4% Rule'),
        ('bond-ladder-retirement.html',                   'Bond ladder strategy'),
        ('portfolio-diversification-guide.html',          'Portfolio diversification'),
        ('tax-loss-harvesting-explained.html',            'Tax-loss harvesting'),
    ]),
    ('Fundamentals', [
        ('how-compound-interest-works.html',              'How compound interest works'),
        ('how-to-calculate-position-size.html',           'Position size'),
        ('what-is-a-good-risk-reward-ratio.html',         'Risk/reward ratio'),
        ('investing-during-high-interest-rates.html',     'High interest rates'),
        ('how-to-invest-during-geopolitical-uncertainty.html', 'Geopolitical uncertainty'),
    ]),
]

# ── CSS ───────────────────────────────────────────────────────────────────────
GROUPED_NAV_CSS = '''
/* ── GROUPED CALC DROPDOWNS ── */
.nav-group { position: relative; }
.nav-group-toggle { font-size: 13px; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; gap: 4px; background: none; border: none; font-family: var(--font-body); padding: 0; transition: color 0.15s; }
.nav-group-toggle:hover, .nav-group-toggle.active { color: var(--text); }
.nav-group-toggle::after { content: "▾"; font-size: 10px; }
.nav-group-menu { display: none; position: absolute; top: 100%; left: 0; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); min-width: 210px; overflow: hidden; z-index: 200; padding: 4px 0; }
.nav-group-menu a { display: block; padding: 9px 14px; font-size: 13px; color: var(--text-muted); text-decoration: none; border-bottom: 1px solid var(--border); transition: all 0.15s; }
.nav-group-menu a:last-child { border-bottom: none; }
.nav-group-menu a:hover { background: var(--bg-input); color: var(--text); }
/* ── ACCORDION GUIDES DROPDOWN ── */
.dropdown { position: relative; }
.dropdown-toggle { font-size: 13px; color: var(--text-muted); cursor: pointer; display: flex; align-items: center; gap: 4px; background: none; border: none; font-family: var(--font-body); padding: 0; transition: color 0.15s; }
.dropdown-toggle:hover, .dropdown-toggle.active { color: var(--text); }
.dropdown-toggle::after { content: "▾"; font-size: 10px; }
.dropdown-menu { display: none; position: absolute; top: 100%; right: 0; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); min-width: 240px; overflow: hidden; z-index: 200; padding: 4px 0; }
.guide-cat-header { display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; font-size: 11px; font-family: var(--font-mono); color: var(--accent); letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer; border-bottom: 1px solid var(--border); user-select: none; transition: background 0.15s; }
.guide-cat-header:hover { background: var(--bg-input); }
.guide-cat-header .cat-arrow { font-size: 10px; transition: transform 0.2s; }
.guide-cat-header.open .cat-arrow { transform: rotate(90deg); }
.guide-cat-links { display: none; }
.guide-cat-links.open { display: block; }
.guide-cat-links a { display: block; padding: 8px 14px 8px 22px; font-size: 12px; color: var(--text-muted); text-decoration: none; border-bottom: 1px solid var(--border); transition: all 0.15s; }
.guide-cat-links a:hover { background: var(--bg-input); color: var(--text); }
.guide-cat-links a:last-child { border-bottom: none; }
.dropdown-menu .all-guides-link { display: block; padding: 10px 14px; font-size: 12px; font-family: var(--font-mono); color: var(--accent); text-decoration: none; text-align: center; border-top: 1px solid var(--border); }
.dropdown-menu .all-guides-link:hover { background: var(--bg-input); }
'''

NAV_EVENT_JS = '''<script>
window.addEventListener('load', function() {
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
      // Close all
      document.querySelectorAll('.guide-cat-header').forEach(function(h) {
        h.classList.remove('open');
        if (h.nextElementSibling) h.nextElementSibling.classList.remove('open');
      });
      // Open clicked if was closed
      if (!isOpen) {
        hdr.classList.add('open');
        if (links) links.classList.add('open');
      }
    });
  });
});
</script>'''


def build_nav(root, in_guides, active_href):
    g = root + 'guides/'
    lines = ['<nav>']

    # Calculator category dropdowns
    for cat_name, items in CALC_CATEGORIES:
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

    # Guides accordion dropdown
    guides_active = ' active' if in_guides else ''
    lines.append('  <div class="dropdown">')
    lines.append('    <button class="dropdown-toggle' + guides_active + '">Guides</button>')
    lines.append('    <div class="dropdown-menu">')
    for cat_name, items in GUIDE_CATEGORIES:
        lines.append('      <div class="guide-cat-header"><span>' + cat_name + '</span><span class="cat-arrow">›</span></div>')
        lines.append('      <div class="guide-cat-links">')
        for href, label in items:
            lines.append('        <a href="' + g + href + '">' + label + '</a>')
        lines.append('      </div>')
    lines.append('      <a href="' + g + 'index.html" class="all-guides-link">All guides &#x2192;</a>')
    lines.append('    </div>')
    lines.append('  </div>')

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

    for cat_name, items in GUIDE_CATEGORIES:
        lines.append('  <span class="mobile-guides-label">' + cat_name.replace('&amp;', '&') + '</span>')
        for href, label in items:
            lines.append('  <a href="' + g + href + '">' + label + '</a>')

    lines.append('  <a href="' + g + 'index.html" style="color:var(--accent);">All guides &#x2192;</a>')
    lines.append('</div>')
    return '\n'.join(lines)


def ensure_css(c):
    if 'guide-cat-header' not in c:
        c = c.replace('</style>', GROUPED_NAV_CSS + '\n</style>', 1)
    else:
        # Update existing CSS
        c = re.sub(r'/\* ── GROUPED CALC DROPDOWNS ──.*?(?=</style>)', GROUPED_NAV_CSS + '\n', c, flags=re.DOTALL)
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

    c = ensure_css(c)

    c = re.sub(
        r'<nav>.*?</nav>\s*<button class="nav-hamburger".*?</button>',
        nav_html, c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<div class="nav-mobile-menu"[^>]*>.*?</div>(?=\s*\n)',
        mobile_html, c, count=1, flags=re.DOTALL
    )
    if 'id="nav-mobile-menu"' not in c:
        c = c.replace('</header>', '</header>\n' + mobile_html, 1)

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
