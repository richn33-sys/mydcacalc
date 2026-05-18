# MyDCACalc.com — Project Reference

## Overview
A free dollar-cost averaging (DCA) calculator for stocks and crypto. Pure static HTML/CSS/JS — no framework, no backend. Monetized via DCA Pro subscription ($9/month) and future affiliate/display ads. Part of a broader passive income site portfolio alongside aitoolgrade.com and trading bots.

---

## Live Site
- **URL:** https://mydcacalc.com
- **Status:** Live ✅
- **SSL:** Active ✅
- **Google Search Console:** Verified ✅
- **Sitemap:** Submitted ✅

---

## DCA Pro — Paid Product (NEW May 2026)

### Overview
DCA Pro is a paid SaaS layer built on top of mydcacalc.com. Live at https://pro.mydcacalc.com.

### Pricing
- $9/month or $79/year
- 7-day free trial (no credit card required)
- Stripe live mode — real payments active ✅

### Features
- Portfolio tracker — log DCA purchases, auto-calculates avg cost
- Live P&L per asset via CoinGecko API
- Weekly AI signal via Claude API (cached weekly per user)
- DCA schedule manager with reminders
- Scenario comparison — what-if analysis
- CSV/PDF export (designed, not yet built)

### Tech stack
| Layer | Tool |
|-------|------|
| Hosting | Hostinger subdomain: pro.mydcacalc.com |
| Server path | /home/u877849432/domains/mydcacalc.com/public_html/dca-pro/ |
| Auth + DB | Supabase (project: durfesxqhlfxpjwxdmde) |
| Payments | Stripe live mode |
| AI signal | Claude API (claude-sonnet-4-20250514) |
| Live prices | CoinGecko free API |
| Email | Resend (domain verification pending as of May 17 2026) |
| Version control | GitHub: richn33-sys/dca-pro (private) |

### File structure
```
dca-pro/
├── CLAUDE.md
├── config.js               ← API keys (gitignored)
├── login.html
├── upgrade.html
├── dashboard.html
├── portfolio.html
├── schedule.html
├── scenarios.html
├── src/
│   ├── auth.js
│   ├── stripe.js
│   └── styles.css
├── api/
│   ├── create-checkout.php
│   ├── stripe-webhook.php
│   ├── generate-signal.php
│   ├── send-welcome.php
│   └── vendor/             ← Stripe PHP SDK (composer)
└── database/
    ├── schema.sql
    └── update-001.sql
```

### Deploy workflow
```bash
# From Mac:
cd ~/Desktop/ClaudeWork/dca-pro
git add .
git commit -m "message"
git push origin main

# Then SSH pull:
ssh -p 65002 u877849432@145.79.4.163
cd /home/u877849432/domains/mydcacalc.com/public_html/dca-pro
git pull origin main

# Emergency single file deploy (bypass git):
scp -P 65002 ~/Desktop/ClaudeWork/dca-pro/filename.html u877849432@145.79.4.163:/home/u877849432/domains/mydcacalc.com/public_html/dca-pro/filename.html
```

### Critical conventions
- All pages use `(async () => { ... })();` IIFE wrapper — bare top-level await causes "Illegal return statement" in some browsers
- Buttons must use `addEventListener` not inline `onclick` — module scope doesn't expose functions to global onclick
- config.js is gitignored — never commit, always SCP manually
- PHP files are gitignored — always SCP manually
- Stripe PHP SDK lives at `api/vendor/autoload.php`
- Server path is `/home/u877849432/domains/mydcacalc.com/public_html/dca-pro/` NOT `/home/u877849432/public_html/dca-pro/`

### Supabase tables
profiles, assets, purchases, schedules, signals — all with RLS enabled

### To manually set user as Pro (testing):
Supabase → Table Editor → profiles → find row → set subscription_status = 'pro'

### Welcome email (Resend)
- From: noreply@mydcacalc.com
- Triggered by Stripe webhook on checkout.session.completed
- DNS verification pending on Hostinger (may take a few hours)
- Once verified, all new signups get welcome email automatically

### CTA on mydcacalc.com
- Green banner added to top of index.html, position-size.html, compound-interest.html
- Links to https://pro.mydcacalc.com/upgrade.html
- Added May 17 2026

### Exit strategy
- Target: 200 users = $1,800 MRR
- Sellable on Flippa at 20-30x MRR = $36K-$54K
- Sell as package with mydcacalc.com for higher combined valuation

---

## Hosting & Deployment (mydcacalc.com)
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
├── producthunt-launch.md                         ← PH launch assets (updated for DCA Pro)
├── authors/
│   ├── james-colter.html
│   ├── james-colter.jpg
│   ├── sara-kline.html
│   └── sara-kline.jpg
├── guides/
│   ├── index.html
│   ├── what-is-dollar-cost-averaging.html
│   ├── how-compound-interest-works.html
│   ├── dca-vs-lump-sum.html
│   ├── how-to-calculate-position-size.html
│   └── how-to-invest-in-a-volatile-market.html
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
- Guides dropdown: 5 guides + "All guides →"
- Root pages: `href="guides/page.html"` for guide links
- Guide pages: `href="../page.html"` for root, `href="page.html"` for guides
- Authors pages: `href="../page.html"` for root, `href="../guides/page.html"` for guides
- Dropdown: JS hover with 300ms delay

---

## Pages & Calculators

### index.html — DCA Calculator
- Forward projection + Historical backtest (S&P 500 ~10%, Nasdaq ~13%, Bitcoin ~60%)
- Asset toggles: Stocks/ETFs, Crypto
- Chart.js 4.4.1 bar chart
- **Pro CTA banner:** Added at top ✅
- **Keywords:** dca calculator, dollar cost averaging calculator

### position-size.html — Position Size Calculator
- Formula: (Account × Risk%) ÷ (Entry − Stop loss)
- Stocks/Crypto/Forex tabs, risk meter, breakdown table, R/R ratio
- **Pro CTA banner:** Added at top ✅
- **Keywords:** position size calculator, risk management calculator

### compound-interest.html — Compound Interest Calculator
- Principal, monthly contributions, rate, years, frequency, inflation, milestones
- Stacked bar chart — deposits vs interest
- **Pro CTA banner:** Added at top ✅
- **Keywords:** compound interest calculator, savings calculator

---

## Author Personas

### James Colter — Long-term Investor & Personal Finance Writer
- **Age:** 38 | **Location:** Denver, CO
- **X/Twitter:** @jamescolter_ | **Email:** jamescolter@proton.me
- **Author page:** mydcacalc.com/authors/james-colter.html
- **Tagline:** "Wealth isn't built in a day. It's built in decades."
- **Covers:** DCA, compound interest, lump sum vs DCA, long-term investing, behavioral finance
- **Voice:** Patient, evidence-based, uses real numbers, never condescending
- **Articles:** what-is-dollar-cost-averaging, how-compound-interest-works, dca-vs-lump-sum
- **Prohibited:** "guaranteed returns", "beat the market", market timing claims

### Sara Kline — Active Trader & Risk Management Specialist
- **Age:** 31 | **Location:** Chicago, IL
- **X/Twitter:** @sarakline_trades | **Email:** sarakline@proton.me
- **Author page:** mydcacalc.com/authors/sara-kline.html
- **Tagline:** "Every trade has a price. Know yours before you enter."
- **Covers:** Position sizing, stop loss, risk/reward, trading psychology, crypto trading
- **Voice:** Direct, no-nonsense, practical, blunt about mistakes
- **Articles:** how-to-calculate-position-size
- **Prohibited:** "guaranteed profits", "can't lose", specific trade recommendations

### Attribution rule:
- Investing/DCA/long-term guides → James Colter
- Trading/risk management guides → Sara Kline

---

## Guides Section

### Published guides:
| File | Author | Status |
|------|--------|--------|
| what-is-dollar-cost-averaging.html | James Colter | ✅ Live |
| how-compound-interest-works.html | James Colter | ✅ Live |
| dca-vs-lump-sum.html | James Colter | ✅ Live |
| how-to-calculate-position-size.html | Sara Kline | ✅ Live |
| how-to-invest-in-a-volatile-market.html | James Colter | ✅ Live |

---

## Content Pipeline (every article)
1. Claude writes + self-reviews
2. Rich runs through Perplexity — fact-check
3. Claude applies corrections
4. Rich runs through Grammarly
5. Claude applies final corrections
6. Rich final read → deploy
7. Update guides/index.html, nav, sitemap
8. Request indexing in Google Search Console

---

## Video Automation Pipeline ✅ LIVE
- **n8n cloud:** app.n8n.cloud — instance: richnash33
- **ElevenLabs:** Creator plan — Voice: Dan — Voice ID: `fvVBPXuE7f1iX3dZLKFy`
- **Schedule:** Monday, Wednesday, Friday at 9am
- **Delivers to:** richn33@gmail.com
- **Model:** claude-sonnet-4-6

---

## Marketing

### Product Hunt
- **Updated launch file:** producthunt-launch.md (now targets DCA Pro, not just free calculators)
- **Account created:** ✅ May 2026 — needs seasoning (upvote/comment 5-10 products)
- **Best days:** Tuesday–Thursday, 12:01am PST
- **Key rule:** Ask for feedback not upvotes
- **Gallery images needed:** 4 × 1270x760px Pro dashboard screenshots + thumbnail

### Reddit strategy (self-promotion not allowed):
- Answer questions where calculator solves the problem
- Drop link naturally in context
- Good subs: r/SideProject, r/IndieHackers, r/passive_income — self-promotion allowed there
- r/personalfinance, r/CryptoCurrency, r/Daytrading — answer questions only

---

## Monetization

### DCA Pro (primary — NEW)
- $9/month or $79/year
- Live at pro.mydcacalc.com ✅
- Target: 200 users = $1,800 MRR → sell on Flippa

### Affiliate links (placeholder — sign up when traffic established):
- Alpaca, Robinhood, Coinbase, Fidelity

### Display ads: Ezoic at ~10k visits, Mediavine at ~50k visits

---

## SEO
| Page | Keyword |
|------|---------|
| index.html | dca calculator |
| position-size.html | position size calculator |
| compound-interest.html | compound interest calculator |
| guides/what-is-dollar-cost-averaging.html | what is dollar cost averaging |
| guides/how-compound-interest-works.html | how compound interest works |
| guides/dca-vs-lump-sum.html | dca vs lump sum |
| guides/how-to-calculate-position-size.html | how to calculate position size |
| guides/how-to-invest-in-a-volatile-market.html | how to invest in a volatile market |

---

## Research Agent ✅ LIVE
- **Location:** `~/Desktop/ClaudeWork/mydcacalc_research/`
- **Schedule:** Every Monday at 8am via launchd
- **Delivers to:** richn33@gmail.com
- **Model:** claude-opus-4-5 with web search
- **Run manually:** `python3 ~/Desktop/ClaudeWork/mydcacalc_research/research_agent.py`
- **Update CURRENT_GUIDES** whenever a new guide is published

---

## Roadmap

### Done ✅
- [x] 3 calculators live
- [x] About, Privacy, Terms, Favicon, SSL
- [x] Google Search Console + sitemap
- [x] Guides section with 5 published articles
- [x] Author personas (James Colter, Sara Kline)
- [x] Author pages + bio boxes on all guides
- [x] Dropdown nav across all pages
- [x] GitHub + Hostinger Git auto-deploy
- [x] Video automation (n8n + Claude + ElevenLabs)
- [x] YouTube channel + 10 TikTok scripts
- [x] Product Hunt account created (May 2026)
- [x] Weekly research agent live
- [x] **DCA Pro built and launched (May 17 2026)** ✅
- [x] **Stripe live payments active** ✅
- [x] **Pro CTA banner on all 3 calculator pages** ✅
- [x] **Welcome email via Resend (pending DNS verification)** ✅

### Next session priorities:
- [ ] Confirm Resend domain verified → test welcome email
- [ ] Update CURRENT_GUIDES in research_agent.py (volatile market guide)
- [ ] Product Hunt seasoning → launch (target DCA Pro, not free calculators)
- [ ] Create PH gallery images (4 × 1270x760 Pro dashboard screenshots)
- [ ] Add bottom upgrade card CTA to calculator pages (banner added, card not yet)
- [ ] Write next guide: Best Day to DCA Bitcoin (James)
- [ ] Add images to guides (Google AI optimization)
- [ ] Sign up for affiliate programs when traffic established
- [ ] Set up hello@mydcacalc.com in Hostinger
- [ ] Lump Sum vs DCA calculator (4th calculator)
- [ ] Apply to Ezoic at 10k visits

---

## Session History

### May 17 2026 — DCA Pro Launch Session
Built and launched DCA Pro from scratch in one session:
- Market research → ranked 5 opportunities → chose DCA Pro
- Built full UI mockup
- Supabase schema (5 tables, RLS)
- Stripe live payments + webhook
- Auth system (login, signup, forgot password)
- Dashboard, portfolio tracker, schedule manager, scenarios page
- Claude API weekly AI signal (cached)
- CoinGecko live price integration
- Pro CTA banner deployed to all 3 calculator pages
- Welcome email via Resend (DNS pending)
- Product Hunt launch kit updated for DCA Pro
- CLAUDE.md created for dca-pro project
- First real payment processed ✅
