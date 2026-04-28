# MyDCACalc.com — Project Reference

## Overview
A free dollar-cost averaging (DCA) calculator for stocks and crypto. Pure static HTML/CSS/JS — no framework, no backend. Monetized via affiliate links and display ads (future). Part of a broader passive income site portfolio alongside aitoolgrade.com and trading bots.

---

## Live Site
- **URL:** https://mydcacalc.com
- **Status:** Live ✅
- **SSL:** Active ✅
- **Google Search Console:** Verified ✅
- **Sitemap:** Submitted ✅

---

## Hosting & Domain
- **Domain registrar:** Namecheap
- **Hosting:** Hostinger (same account as aitoolgrade.com)
- **Nameservers:** Hostinger nameservers (set in Namecheap)
- **GitHub repo:** https://github.com/richn33-sys/mydcacalc (public)
- **Deployment:** GitHub → Hostinger Git auto-deploy

---

## Deployment Workflow ✅ AUTOMATED

### How it works:
```
Claude writes/updates files to ~/Desktop/ClaudeWork/mydcacalc/
    ↓
Run deploy script in Terminal
    ↓
GitHub receives push
    ↓
Hostinger auto-deploys from GitHub
    ↓
Site live at mydcacalc.com
```

### Deploy command (run after every session):
```bash
python3 ~/Desktop/ClaudeWork/mydcacalc/deploy.py "describe what changed"
```

### Deploy script location:
`~/Desktop/ClaudeWork/mydcacalc/deploy.py`

### Manual Hostinger deploy (if needed):
Hostinger → mydcacalc.com → Advanced → Git → Deploy

### Important notes:
- Repo is **public** on GitHub (required for Hostinger free Git integration)
- No API keys or sensitive data in any files — safe to be public
- If Hostinger shows "nothing to commit" but files look wrong → delete repo connection, empty public_html, reconnect
- Brave browser caches aggressively — test in Safari if changes don't appear
- Never upload files manually to Hostinger anymore — always use git push

---

## File Structure
```
~/Desktop/ClaudeWork/mydcacalc/  (local)
public_html/  (Hostinger — mirrors GitHub)
├── index.html                                    ← DCA Calculator (homepage)
├── position-size.html                            ← Position Size Calculator
├── compound-interest.html                        ← Compound Interest Calculator
├── about.html                                    ← About page
├── privacy.html                                  ← Privacy policy
├── terms.html                                    ← Terms of use
├── sitemap.xml                                   ← Sitemap (submitted to GSC)
├── deploy.py                                     ← Deploy script (local only)
├── .gitignore                                    ← Ignores .DS_Store files
├── guides/
│   ├── index.html                                ← Guides landing page
│   ├── what-is-dollar-cost-averaging.html        ← Article: What is DCA?
│   ├── how-compound-interest-works.html          ← Article: How compound interest works
│   ├── dca-vs-lump-sum.html                      ← Article: DCA vs lump sum
│   └── how-to-calculate-position-size.html       ← Article: How to calculate position size
└── CLAUDE.md                                     ← This file (not pushed to GitHub)
```

---

## Design System
- **Theme:** Dark, minimal, monospace-accented
- **Primary font:** Sora (Google Fonts) — body/headings
- **Mono font:** DM Mono (Google Fonts) — labels, metrics, code-like elements
- **Background:** `#0c0c0e`
- **Card background:** `#141416`
- **Input background:** `#1a1a1e`
- **Accent color:** `#c8f060` (yellow-green)
- **Positive values:** `#3ecf8e` (green)
- **Negative values:** `#f06060` (red)
- **Blue accent:** `#5b9cf6`
- **Muted text:** `#888884`
- **Borders:** `rgba(255,255,255,0.08)`
- **Border radius:** 10px (components), 16px (cards)
- **Favicon:** SVG data URI — dark bg with "DCA" in accent green, monospace

### Nav structure (all pages):
- Header: DCA · Position size · Compound interest · Guides ▾
- Guides dropdown: 4 guides + "All guides →"
- Root pages use `href="guides/page.html"` for guide links
- Guide pages use `href="../page.html"` for root links and `href="page.html"` for guide links
- Dropdown uses JS hover with 300ms delay

### Nav update script (when new guides are added):
```bash
python3 << 'EOF'
import os
base = os.path.expanduser('~/Desktop/ClaudeWork/mydcacalc')
# Update old_menu and new_menu strings to match current nav
# Run on all root files + guide files separately (different relative paths)
EOF
```

---

## Pages & Calculators

### index.html — DCA Calculator
**Two modes:** Forward projection + Historical backtest (S&P 500 ~10%, Nasdaq ~13%, Bitcoin ~60%)
**Chart:** Chart.js 4.4.1 bar chart
**Keywords:** dca calculator, dollar cost averaging calculator

### position-size.html — Position Size Calculator
**Formula:** (Account × Risk%) ÷ (Entry − Stop loss)
**Features:** Stocks/Crypto/Forex tabs, risk meter, breakdown table, R/R ratio
**Keywords:** position size calculator, risk management calculator

### compound-interest.html — Compound Interest Calculator
**Features:** Principal, monthly contributions, rate, years, frequency, inflation, milestones
**Chart:** Stacked bar — deposits vs interest
**Keywords:** compound interest calculator, savings calculator

---

## Guides Section

### guides/index.html — Guides Landing Page
- Stats: 4 guides published, 3 calculators, 0 sign-ups
- Active cards (linked, featured class) + coming soon cards (greyed out)
- **Update on every new guide:** activate card, update counter, add new coming soon card

### Published guides:
| File | Keyword | Length | Status |
|------|---------|--------|--------|
| what-is-dollar-cost-averaging.html | what is dollar cost averaging | 8 min | ✅ Live |
| how-compound-interest-works.html | how compound interest works | 9 min | ✅ Live |
| dca-vs-lump-sum.html | dca vs lump sum | 9 min | ✅ Live |
| how-to-calculate-position-size.html | how to calculate position size | 10 min | ✅ Live |

---

## Content Pipeline (every article)

### Writing brief:
1. People-first — answer the reader's question genuinely
2. E-E-A-T — experience, expertise, authority, trust
3. Original insights — not a rehash
4. Complete answers — reader doesn't need to go elsewhere
5. YMYL aware — accurate, disclaim where needed
6. No fluff — no padding or keyword stuffing
7. Humanized — varied sentence length, natural phrasing, organic transitions

### Review process:
1. Claude writes + self-reviews (verifies all figures with Python)
2. Rich runs through Perplexity — fact-check
3. Claude applies Perplexity corrections
4. Rich runs through Grammarly — polish
5. Claude applies final corrections
6. Rich does final read
7. Claude saves file to `~/Desktop/ClaudeWork/mydcacalc/guides/`
8. Claude updates guides/index.html (activate card, update counter)
9. Claude updates nav dropdown on ALL pages
10. Claude updates sitemap.xml
11. Rich runs: `python3 ~/Desktop/ClaudeWork/mydcacalc/deploy.py "add new guide"`
12. Request indexing in Google Search Console

---

## Content Roadmap

### Published ✅
- [x] What is dollar cost averaging?
- [x] How compound interest works
- [x] DCA vs lump sum investing
- [x] How to calculate position size

### Next to write:
- [ ] How to DCA Bitcoin
- [ ] How to DCA the S&P 500
- [ ] What is a good risk/reward ratio?
- [ ] The Rule of 72 explained
- [ ] 7 investing mistakes beginners make
- [ ] How much do I need to invest to reach $1 million?

---

## Video Automation Pipeline ✅ LIVE

### Accounts & Tools
- **n8n cloud:** app.n8n.cloud — instance: richnash33
- **ElevenLabs:** Creator plan — Voice: Dan — Voice ID: `fvVBPXuE7f1iX3dZLKFy`
- **YouTube:** MyDCACalc channel
- **Google Drive folder:** MyDCACalc Videos
- **Google Sheet:** MyDCACalc Topics

### Workflow schedule: Monday, Wednesday, Friday at 9am
### Key nodes: Schedule → Get Next Topic → Code in JavaScript (Claude API) → ElevenLabs HTTP Request → Save to Drive → Email notification
### Mark topic Done: manually update Google Sheet after each run
### See capcut-assembly-guide.md for video assembly instructions

---

## Social & Branding
- **Email accounts:** hello@mydcacalc.com, youtube@mydcacalc.com, social@mydcacalc.com
- **10 TikTok scripts:** tiktok-scripts.md
- **CapCut guide:** capcut-assembly-guide.md

---

## Monetization

### Affiliate links (placeholder — replace with real URLs):
| Platform | Notes |
|----------|-------|
| Alpaca | Featured on all pages |
| Robinhood | Standard |
| Coinbase | Standard |
| Fidelity | Standard |

> **TODO:** Sign up for affiliate programs and replace placeholder hrefs on ALL pages

### Display ads: Ezoic at ~10k visits, Mediavine at ~50k visits

---

## SEO

### Keyword targets:
| Page | Keyword |
|------|---------|
| index.html | dca calculator |
| position-size.html | position size calculator |
| compound-interest.html | compound interest calculator |
| guides/ | investing guides |
| guides/what-is-dollar-cost-averaging.html | what is dollar cost averaging |
| guides/how-compound-interest-works.html | how compound interest works |
| guides/dca-vs-lump-sum.html | dca vs lump sum |
| guides/how-to-calculate-position-size.html | how to calculate position size |

### Google Ranking Strategy:
- Helpful Content baked into core ranking (March 2024) — our pipeline is aligned
- Original calculators = structural SEO advantage
- Reddit posts = highest ROI for early backlinks
- YMYL site — accuracy critical, all articles Perplexity fact-checked
- Consistent guide publishing = freshness signal

### Sitemap URLs (11 pages — last updated 2025-04-28):
All calculator pages, guides landing, 4 guide articles, about, privacy, terms

---

## Roadmap

### Done ✅
- [x] 3 calculators live
- [x] About, Privacy, Terms, Favicon, SSL
- [x] Google Search Console + sitemap
- [x] Guides section with 4 published articles
- [x] Dropdown nav across all pages
- [x] GitHub repo + Hostinger Git auto-deploy
- [x] deploy.py script
- [x] Video automation (n8n + Claude + ElevenLabs)
- [x] YouTube channel
- [x] 10 TikTok scripts + CapCut guide

### Next session:
- [ ] Sign up for affiliate programs + replace placeholder links
- [ ] Set up hello@mydcacalc.com in Hostinger
- [ ] Post on Reddit
- [ ] First video assembled and posted
- [ ] Write next 2 guides
- [ ] Apply to Ezoic at 10k visits
