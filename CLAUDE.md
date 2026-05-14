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

## Hosting & Deployment
- **Domain registrar:** Namecheap
- **Hosting:** Hostinger
- **GitHub repo:** https://github.com/richn33-sys/mydcacalc (public)
- **Local files:** `~/Desktop/ClaudeWork/mydcacalc/`
- **Deploy command:** `python3 ~/Desktop/ClaudeWork/mydcacalc/deploy.py "message"`
- **After deploy:** Hostinger → mydcacalc.com → Advanced → Git → Deploy (manual trigger required)
- **Test in:** Safari (Brave caches aggressively)
- **Never test from:** local downloaded files (shows file:/// paths)

### Common deployment issues:
- Hostinger doesn't always auto-pull — always click Deploy manually after git push
- Check for bad paths before deploying: `grep -r "file:///" ~/Desktop/ClaudeWork/mydcacalc/ --include="*.html"`
- If Hostinger is out of sync: delete Git connection, empty public_html, reconnect and redeploy
- **Image rename gotcha:** Git won't track a rename unless you use `git rm old-name && git add new-name` — a local rename alone won't update the repo

---

## File Structure
```
~/Desktop/ClaudeWork/mydcacalc/
├── index.html                                    ← DCA Calculator (homepage)
├── position-size.html                            ← Position Size Calculator
├── compound-interest.html                        ← Compound Interest Calculator
├── about.html                                    ← About page (includes Meet the Authors section)
├── privacy.html                                  ← Privacy policy
├── terms.html                                    ← Terms of use
├── sitemap.xml                                   ← Sitemap (submitted to GSC)
├── deploy.py                                     ← Deploy script
├── .gitignore                                    ← Ignores .DS_Store
├── personas.md                                   ← Author persona definitions
├── authors/
│   ├── james-colter.html                         ← James Colter author page
│   ├── james-colter.jpg                          ← James Colter profile photo (AI-generated)
│   ├── sara-kline.html                           ← Sara Kline author page
│   └── sara-kline.jpg                            ← Sara Kline profile photo (AI-generated)
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
- **Primary font:** Sora (Google Fonts)
- **Mono font:** DM Mono (Google Fonts)
- **Background:** `#0c0c0e`
- **Card background:** `#141416`
- **Input background:** `#1a1a1e`
- **Accent:** `#c8f060` (yellow-green)
- **Positive:** `#3ecf8e` (green)
- **Negative:** `#f06060` (red)
- **Muted text:** `#888884`
- **Borders:** `rgba(255,255,255,0.08)`
- **Border radius:** 10px (components), 16px (cards)
- **Favicon:** SVG data URI — dark bg, "DCA" in accent green

### Nav structure:
- Header: DCA · Position size · Compound interest · Guides ▾
- Guides dropdown: 4 guides + "All guides →"
- Root pages: `href="guides/page.html"` for guide links
- Guide pages: `href="../page.html"` for root, `href="page.html"` for guides
- Authors pages: `href="../page.html"` for root, `href="../guides/page.html"` for guides
- Dropdown: JS hover with 300ms delay

### Nav update script (run when new guides added):
```bash
python3 << 'EOF'
import os, re
base = os.path.expanduser('~/Desktop/ClaudeWork/mydcacalc')
# Update old_menu/new_menu strings and run on root files
# Guide pages need separate script with different relative paths
EOF
```

---

## Pages & Calculators

### index.html — DCA Calculator
- Forward projection + Historical backtest (S&P 500 ~10%, Nasdaq ~13%, Bitcoin ~60%)
- Asset toggles: Stocks/ETFs, Crypto
- Chart.js 4.4.1 bar chart
- **Keywords:** dca calculator, dollar cost averaging calculator

### position-size.html — Position Size Calculator
- Formula: (Account × Risk%) ÷ (Entry − Stop loss)
- Stocks/Crypto/Forex tabs, risk meter, breakdown table, R/R ratio
- **Keywords:** position size calculator, risk management calculator

### compound-interest.html — Compound Interest Calculator
- Principal, monthly contributions, rate, years, frequency, inflation, milestones
- Stacked bar chart — deposits vs interest
- **Keywords:** compound interest calculator, savings calculator

---

## Author Personas

### James Colter — Long-term Investor & Personal Finance Writer
- **Age:** 38 | **Location:** Denver, CO
- **X/Twitter:** @jamescolter_ | **Email:** jamescolter@proton.me
- **Author page:** mydcacalc.com/authors/james-colter.html
- **Photo:** `authors/james-colter.jpg` (AI-generated, square crop, 400x400px approx)
- **Tagline:** "Wealth isn't built in a day. It's built in decades."
- **Covers:** DCA, compound interest, lump sum vs DCA, long-term investing, behavioral finance
- **Voice:** Patient, evidence-based, uses real numbers, never condescending
- **Articles:** what-is-dollar-cost-averaging, how-compound-interest-works, dca-vs-lump-sum
- **Prohibited:** "guaranteed returns", "beat the market", market timing claims

### Sara Kline — Active Trader & Risk Management Specialist
- **Age:** 31 | **Location:** Chicago, IL
- **X/Twitter:** @sarakline_trades | **Email:** sarakline@proton.me
- **Author page:** mydcacalc.com/authors/sara-kline.html
- **Photo:** `authors/sara-kline.jpg` (AI-generated, square crop, 400x400px approx)
- **Tagline:** "Every trade has a price. Know yours before you enter."
- **Covers:** Position sizing, stop loss, risk/reward, trading psychology, crypto trading
- **Voice:** Direct, no-nonsense, practical, blunt about mistakes
- **Articles:** how-to-calculate-position-size
- **Prohibited:** "guaranteed profits", "can't lose", specific trade recommendations

### Attribution rule:
- Investing/DCA/long-term guides → James Colter
- Trading/risk management guides → Sara Kline

### Author bio box:
- Added to bottom of each guide above the disclaimer
- Links to author page
- CSS class: `.author-bio-box`

### Author page structure:
- Hero: circular photo (100x100px, accent border, `object-fit: cover`) + name, title, location, social links
- Bio: 3 paragraphs
- Topics covered: pill tags
- Articles by [author]: linked cards
- Photo src is just the filename (e.g. `james-colter.jpg`) — same folder as the HTML

### About page — Meet the Authors section:
- Added between "Who built this" and "Contact"
- Two clickable author cards with 64x64px circular photo, name, title, one-line bio, arrow
- Photo src: `authors/james-colter.jpg` and `authors/sara-kline.jpg` (relative from root)
- CSS class: `.authors-grid`, `.author-card`, `.author-card-avatar`

---

## Guides Section

### guides/index.html — Guides Landing Page
- Stats: 4 guides published, 3 calculators, 0 sign-ups
- Active cards (linked, featured class) + coming soon cards (greyed out)
- **Update on every new guide:** activate card, update counter, add new coming soon card, update nav on ALL pages, update sitemap

### Published guides:
| File | Author | Keyword | Status |
|------|--------|---------|--------|
| what-is-dollar-cost-averaging.html | James Colter | what is dollar cost averaging | ✅ Live |
| how-compound-interest-works.html | James Colter | how compound interest works | ✅ Live |
| dca-vs-lump-sum.html | James Colter | dca vs lump sum | ✅ Live |
| how-to-calculate-position-size.html | Sara Kline | how to calculate position size | ✅ Live |

---

## Content Pipeline (every article)

### Writing brief:
1. People-first — answer the reader's question genuinely
2. E-E-A-T — expertise, authority, trust
3. Original insights — not a rehash
4. Complete answers — reader doesn't need to go elsewhere
5. YMYL aware — accurate, disclaim where needed
6. No fluff — no padding or keyword stuffing
7. Humanized — varied sentence length, natural phrasing

### Review process:
1. Claude writes + self-reviews (Python fact-check all figures)
2. Rich runs through Perplexity — fact-check
3. Claude applies Perplexity corrections
4. Rich runs through Grammarly
5. Claude applies final corrections
6. Rich final read
7. Save to `~/Desktop/ClaudeWork/mydcacalc/guides/`
8. Add author bio box (use correct persona)
9. Update Article schema with author
10. Update guides/index.html (activate card, update counter)
11. Update nav dropdown on ALL pages + guide pages
12. Update sitemap.xml
13. `python3 ~/Desktop/ClaudeWork/mydcacalc/deploy.py "add new guide"`
14. Hostinger → Advanced → Git → Deploy
15. Request indexing in Google Search Console

---

## Content Roadmap

### Published ✅
- [x] What is dollar cost averaging? (James)
- [x] How compound interest works (James)
- [x] DCA vs lump sum investing (James)
- [x] How to calculate position size (Sara)

### Next to write:
- [ ] How to DCA Bitcoin (James)
- [ ] How to DCA the S&P 500 (James)
- [ ] What is a good risk/reward ratio? (Sara)
- [ ] The Rule of 72 explained (James)
- [ ] 7 investing mistakes beginners make (James)
- [ ] How much do I need to invest to reach $1 million? (James)

---

## Video Automation Pipeline ✅ LIVE

### Accounts & Tools
- **n8n cloud:** app.n8n.cloud — instance: richnash33
- **ElevenLabs:** Creator plan — Voice: Dan — Voice ID: `fvVBPXuE7f1iX3dZLKFy`
- **YouTube:** MyDCACalc channel
- **Google Drive folder:** MyDCACalc Videos
- **Google Sheet:** MyDCACalc Topics (Topic, Status, YouTubeTitle, Hashtags, DateProcessed, DriveLink)

### Workflow: "MyDCACalc Video Automation"
**Schedule:** Monday, Wednesday, Friday at 9am — **Active ✅**

**Flow:**
```
Schedule Trigger → Get Next Topic (Google Sheets, first Pending row)
→ Topic Found? (IF)
  → true: Code in JavaScript (Claude API generates script)
    → HTTP Request 1 (ElevenLabs MP3)
      → Save Voiceover to Drive
        → Send Email (richn33@gmail.com with script + Drive link)
  → false: No Topics Alert email
```

### Key node configs:
- **Code node:** `this.helpers.httpRequest` → Anthropic API, model `claude-sonnet-4-6`
- **Prompt:** write ONLY spoken words, no labels/brackets/markdown
- **ElevenLabs:** HTTP Request, `xi-api-key` header, Response Format: File
- **Text field:** `={{ $('Code in JavaScript').item.json.script }}`
- **Mark topic Done:** manual — update Google Sheet Status to "Done" after each run

### Video assembly (~10 mins your part):
1. Check email Mon/Wed/Fri 9am
2. Review script, download MP3
3. QuickTime screen record of calculator
4. CapCut: combine recording + MP3, mute video audio, add auto-captions
5. Export 9:16 vertical 1080p
6. Upload YouTube Shorts + TikTok
7. Mark topic Done in Google Sheet
8. See capcut-assembly-guide.md for full instructions

---

## Marketing

### Product Hunt Launch
- **File:** producthunt-launch.md (on Desktop)
- **Account created:** ✅ (created May 2026 — needs 1 week seasoning before launch)
- **Tagline:** "Calculate your DCA strategy for stocks and crypto" (49 chars)
- **Backup taglines:** "Project your investing future — free, no sign-up" / "Free DCA + position size calculators for investors"
- **Description:** See producthunt-launch.md — use the full description in the file, not a shorter version
- **First comment:** Pre-written in producthunt-launch.md — paste immediately when live
- **Best days:** Tuesday–Thursday, 12:01am PST
- **Key rule:** Ask for feedback not upvotes — never ask for upvotes
- **Gallery images needed:** 4 × 1270x760px screenshots + 1 × 240x240px thumbnail (not yet created)
- **Seasoning tasks:** Upvote and comment on 5–10 other products before launching

### Reddit (self-promotion not allowed — use instead):
- Answer questions where calculator solves the problem
- Post guide articles as educational content
- Engage in comments and drop link naturally
- Consider Hacker News "Show HN" post

### Social accounts:
- **Email:** hello@mydcacalc.com, youtube@mydcacalc.com, social@mydcacalc.com
- **TikTok scripts:** 10 pre-written in tiktok-scripts.md
- **CapCut guide:** capcut-assembly-guide.md

---

## Monetization

### Affiliate links (all placeholder — sign up when traffic established):
| Platform | Notes |
|----------|-------|
| Alpaca | Featured on all pages |
| Robinhood | Standard |
| Coinbase | Standard |
| Fidelity | Standard |

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
- Helpful Content baked into core ranking (March 2024) — pipeline aligned
- Original calculators = structural SEO advantage
- YMYL site — accuracy critical, all articles Perplexity fact-checked
- Consistent publishing = freshness signal
- Product Hunt launch = quality backlink

### Sitemap (11 pages, last updated 2025-04-28):
All calculators, guides landing, 4 guides, about, privacy, terms

---

## Roadmap

### Done ✅
- [x] 3 calculators live
- [x] About, Privacy, Terms, Favicon, SSL
- [x] Google Search Console + sitemap
- [x] Guides section with 4 published articles
- [x] Author personas (James Colter, Sara Kline)
- [x] Author pages live
- [x] Author bio boxes on all guides
- [x] Dropdown nav across all pages
- [x] GitHub + Hostinger Git auto-deploy
- [x] deploy.py script
- [x] Video automation (n8n + Claude + ElevenLabs)
- [x] YouTube channel
- [x] 10 TikTok scripts + CapCut guide
- [x] Product Hunt launch assets written
- [x] Product Hunt account created (May 2026)
- [x] AI-generated profile photos for James Colter and Sara Kline
- [x] Author pages updated with real photos (circular crop, accent border)
- [x] About page updated with Meet the Authors section

### Next session priorities:
- [ ] Product Hunt seasoning (upvote/comment on 5-10 products) then launch
- [ ] Create Product Hunt gallery images (4 × 1270x760) and thumbnail (240x240)
- [ ] Sign up for affiliate programs when traffic established
- [ ] Set up hello@mydcacalc.com in Hostinger
- [ ] Write next 2 guides (How to DCA Bitcoin + Risk/reward ratio)
- [ ] Lump Sum vs DCA calculator (4th calculator)
- [ ] Apply to Ezoic at 10k visits
