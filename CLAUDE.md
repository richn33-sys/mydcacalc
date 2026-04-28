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
- **File location on Hostinger:** `public_html/` inside the mydcacalc.com site

---

## File Structure
```
public_html/
├── index.html                                    ← DCA Calculator (homepage)
├── position-size.html                            ← Position Size Calculator
├── compound-interest.html                        ← Compound Interest Calculator
├── about.html                                    ← About page
├── privacy.html                                  ← Privacy policy
├── terms.html                                    ← Terms of use
├── sitemap.xml                                   ← Sitemap (submitted to GSC)
├── guides/
│   ├── index.html                                ← Guides landing page
│   ├── what-is-dollar-cost-averaging.html        ← Article: What is DCA?
│   ├── how-compound-interest-works.html          ← Article: How compound interest works
│   ├── dca-vs-lump-sum.html                      ← Article: DCA vs lump sum
│   └── how-to-calculate-position-size.html       ← Article: How to calculate position size
└── CLAUDE.md                                     ← This file (do not upload to Hostinger)
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

### Shared UI patterns:
- Sticky header with logo + nav links
- Nav: DCA · Position size · Compound interest · Guides (dropdown)
- Guides dropdown uses JS hover with 300ms delay
- All internal links use relative paths — root pages `href="page.html"`, guide pages `href="../page.html"`
- Affiliate bar (Alpaca featured), consistent footer

### File management notes:
- **CLAUDE.md local path:** `/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/CLAUDE.md`
- When Chrome extension is connected: write files directly to Desktop via Python script
- When not connected: files go to `/mnt/user-data/outputs/` — download and upload manually
- Guides subfolder files get prefixed with `guides-` for zip download — rename after downloading
- Never test HTML files locally — always upload and test from live URL
- To update nav across multiple files use the Terminal Python script approach

### Nav update Python script (run in Terminal when nav needs updating):
```python
import os, re

files = [
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/index.html',
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/position-size.html',
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/compound-interest.html',
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/about.html',
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/privacy.html',
    '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc/terms.html',
]
# Update old_menu and new_menu strings as needed
# Run: python3 ~/Desktop/update_nav.py
```

---

## Pages & Calculators

### index.html — DCA Calculator
**Two modes:** Forward projection + Historical backtest (S&P 500 ~10%, Nasdaq ~13%, Bitcoin ~60%)
**Asset toggles:** Stocks/ETFs (default 10%), Crypto (default 30%)
**Chart:** Chart.js 4.4.1 bar chart — portfolio value vs total contributed
**Keywords:** dca calculator, dollar cost averaging calculator, crypto dca, bitcoin dca

### position-size.html — Position Size Calculator
**Formula:** (Account × Risk%) ÷ (Entry − Stop loss)
**Features:** Stocks/Crypto/Forex tabs, risk meter bar, breakdown table, R/R ratio
**Keywords:** position size calculator, risk management calculator, stop loss calculator

### compound-interest.html — Compound Interest Calculator
**Features:** Principal, monthly contributions, rate, years, frequency, inflation, milestones
**Chart:** Stacked bar — deposits vs interest
**Keywords:** compound interest calculator, savings calculator

---

## Guides Section

### guides/index.html — Guides Landing Page
- Hero with unique editorial content explaining accuracy-first approach
- Stats bar: 4 guides published, 3 calculators, 0 sign-ups required
- Published guide cards (linked, featured class) + coming soon cards (greyed out)
- Philosophy section + calculator CTA section
- **Update every time a new guide is published:**
  - Change coming soon card → active linked card
  - Update stats counter
  - Add new coming soon card for next guide
  - Update dropdown nav on ALL pages

### guides/what-is-dollar-cost-averaging.html
- **Keyword:** what is dollar cost averaging
- **Length:** ~1,800 words, 8 min read
- **CTA:** Links to index.html (DCA calculator)
- **Pipeline:** Written ✅ → Perplexity ✅ → Final review ✅

### guides/how-compound-interest-works.html
- **Keyword:** how compound interest works
- **Length:** ~1,900 words, 9 min read
- **CTA:** Links to compound-interest.html
- **Pipeline:** Written ✅ → Perplexity ✅ → Final review ✅
- **Key corrections:** Frequency impact (3% → ~9-10%), contributions multiplier (7x → 4x)

### guides/dca-vs-lump-sum.html
- **Keyword:** dca vs lump sum
- **Length:** ~1,800 words, 9 min read
- **CTA:** Links to index.html (DCA calculator)
- **Pipeline:** Written ✅ → Perplexity ✅ → Final review ✅
- **Key corrections:** Two-thirds claim given Vanguard range (62-74%), Scenario 2 path dependency disclaimer added, behavioral framing updated

### guides/how-to-calculate-position-size.html
- **Keyword:** how to calculate position size
- **Length:** ~2,000 words, 10 min read
- **CTA:** Links to position-size.html
- **Pipeline:** Written ✅ → Perplexity ✅ → Final review ✅
- **Key corrections:** 1% rule softened to "rule of thumb not universal standard", losing streak framing made factual, fees/slippage caveat added, win rate guarantee softened

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
1. Claude writes + self-reviews (verifies all figures with Python before writing)
2. Rich runs through Perplexity — fact-check
3. Claude applies Perplexity corrections
4. Rich runs through Grammarly — polish
5. Claude applies final corrections
6. Rich does final read → upload → request indexing in GSC
7. Update guides/index.html (activate card, update counter)
8. Update nav dropdown on ALL pages
9. Update sitemap.xml

---

## Content Roadmap

### Published ✅
- [x] What is dollar cost averaging?
- [x] How compound interest works
- [x] DCA vs lump sum investing
- [x] How to calculate position size

### Next to write:
- [ ] How to DCA Bitcoin — a step by step guide
- [ ] How to DCA the S&P 500
- [ ] What is a good risk/reward ratio in trading?
- [ ] The Rule of 72 explained
- [ ] 7 investing mistakes beginners make
- [ ] How much do I need to invest to reach $1 million?

---

## Video Automation Pipeline ✅ LIVE

### Accounts & Tools
- **n8n cloud:** app.n8n.cloud — instance: richnash33
- **ElevenLabs:** Creator plan — Voice: Dan — Voice ID: `fvVBPXuE7f1iX3dZLKFy`
- **YouTube channel:** MyDCACalc (brand channel under personal Google account)
- **Google Drive folder:** MyDCACalc Videos
- **Google Sheet:** MyDCACalc Topics (columns: Topic, Status, YouTubeTitle, Hashtags, DateProcessed, DriveLink)

### Workflow — "MyDCACalc Video Automation"
**Schedule:** Monday, Wednesday, Friday at 9am
**Status:** Active ✅

**Node flow:**
```
Schedule Trigger
    ↓
Get Next Topic (Google Sheets — first Pending row)
    ↓
Topic Found? (IF node)
    ↓ true
Code in JavaScript (Claude API — generates clean voiceover script)
    ├→ HTTP Request 1 (ElevenLabs — generates MP3)
    │       ↓
    │   Save Voiceover to Drive
    │       ↓
    └→ Send Email Notification (Gmail → richn33@gmail.com)
    ↓ false
No Topics Alert (Gmail)
```

### Key node configs:
- **Code in JavaScript:** Uses `this.helpers.httpRequest` to call Anthropic API
  - Model: `claude-sonnet-4-6`
  - Prompt instructs Claude to write ONLY spoken words — no labels, brackets, or markdown
- **ElevenLabs node:** HTTP Request, auth via `xi-api-key` header, Response Format: File
  - Text field: `={{ $('Code in JavaScript').item.json.script }}`
- **Mark Topic Done:** Not working — manually update Google Sheet Status to "Done" after each run
- **Email:** Sends to richn33@gmail.com with script text and Drive link

### Video assembly (your part — ~10 mins):
1. Check email Mon/Wed/Fri 9am
2. Review script, download MP3 from Drive link
3. Record screen capture of calculator (QuickTime → New Screen Recording)
4. Open CapCut — combine screen recording + MP3, mute video audio
5. Add auto-captions, export 9:16 vertical 1080p
6. Upload to YouTube Shorts + TikTok
7. Mark topic as Done in Google Sheet
8. See `capcut-assembly-guide.md` for full instructions

### Topic queue: 15 pre-loaded topics in Google Sheet. Add more with Status=Pending.

---

## Social & Branding
- **YouTube:** MyDCACalc channel
- **Email accounts:** hello@mydcacalc.com, youtube@mydcacalc.com, social@mydcacalc.com
- **10 pre-written TikTok scripts:** saved in `tiktok-scripts.md`
- **CapCut guide:** saved in `capcut-assembly-guide.md`

---

## Monetization

### Affiliate links (placeholder — replace with real URLs):
| Platform | URL | Notes |
|----------|-----|-------|
| Alpaca | https://alpaca.markets | Featured on all pages |
| Robinhood | https://robinhood.com | Standard |
| Coinbase | https://www.coinbase.com | Standard |
| Fidelity | https://www.fidelity.com | Standard |

> **TODO:** Sign up for affiliate programs and replace placeholder hrefs on ALL pages

### Display ads (future):
- Ezoic at ~10k monthly visits
- Mediavine at ~50k monthly visits

---

## SEO

### Per-page targets:
| Page | Primary keyword |
|------|----------------|
| index.html | dca calculator |
| position-size.html | position size calculator |
| compound-interest.html | compound interest calculator |
| guides/ | investing guides |
| guides/what-is-dollar-cost-averaging.html | what is dollar cost averaging |
| guides/how-compound-interest-works.html | how compound interest works |
| guides/dca-vs-lump-sum.html | dca vs lump sum |
| guides/how-to-calculate-position-size.html | how to calculate position size |

- Schema.org `WebApplication` on calculators, `Article` on guides, `CollectionPage` on guides/index
- Canonical URLs on all pages
- Internal linking: calculators ↔ guides
- All pages in sitemap.xml

### Google Ranking Strategy
- **Helpful Content** is baked into core ranking (March 2024) — our writing pipeline is aligned
- **Original content** — calculators are genuinely unique tools, structural advantage
- **PageRank** — Reddit posts are highest ROI for early backlinks
- **YMYL** — accuracy critical, all articles fact-checked via Perplexity
- **Key actions:** Reddit posts, consistent guide publishing, accurate content, internal linking

---

## Sitemap — current URLs:
- https://mydcacalc.com/index.html (1.0)
- https://mydcacalc.com/position-size.html (0.9)
- https://mydcacalc.com/compound-interest.html (0.9)
- https://mydcacalc.com/guides/ (0.8)
- https://mydcacalc.com/guides/what-is-dollar-cost-averaging.html (0.8)
- https://mydcacalc.com/guides/how-compound-interest-works.html (0.8)
- https://mydcacalc.com/guides/dca-vs-lump-sum.html (0.8)
- https://mydcacalc.com/guides/how-to-calculate-position-size.html (0.8)
- https://mydcacalc.com/about.html (0.5)
- https://mydcacalc.com/privacy.html (0.3)
- https://mydcacalc.com/terms.html (0.3)

---

## Roadmap

### Done ✅
- [x] 3 calculators live
- [x] About, Privacy, Terms pages
- [x] Favicon, SSL, sitemap
- [x] Google Search Console verified
- [x] Guides section with /guides/ subfolder
- [x] Guides landing page
- [x] 4 articles written, reviewed and published
- [x] Dropdown nav with hover delay
- [x] Video automation pipeline (n8n + Claude + ElevenLabs)
- [x] YouTube channel created
- [x] 10 TikTok scripts written
- [x] CapCut assembly guide written

### Next
- [ ] Sign up for affiliate programs + replace placeholder links on all pages
- [ ] Set up hello@mydcacalc.com email in Hostinger
- [ ] Post on Reddit (r/personalfinance, r/investing, r/CryptoCurrency, r/Daytrading)
- [ ] First video assembled and posted to YouTube Shorts + TikTok
- [ ] Write next 2 guides
- [ ] Apply to Ezoic at 10k monthly visits
