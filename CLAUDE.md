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
| Email | Resend — domain verified ✅ noreply@mydcacalc.com |
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
- Domain verified ✅ — welcome emails firing automatically on new signups
### CTA on mydcacalc.com
- Green banner added to top of all 8 calculator pages: index.html, position-size.html, compound-interest.html, dca-backtest.html, inflation-calculator.html, asset-allocation.html, drip-calculator.html, loss-recovery-calculator.html
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
- **After deploy:** Hostinger → mydcacalc.com → Advanced → Git → Redeploy (auto-deploy now on)
- **Test in:** Safari (Brave caches aggressively)
- **Never test from:** local downloaded files (shows file:/// paths)
### Common deployment issues:
- Hostinger doesn't always auto-pull — click Redeploy manually if needed
- Check for bad paths before deploying: `grep -r "file:///" ~/Desktop/ClaudeWork/mydcacalc/ --include="*.html"`
- GitHub token expires — embed in remote URL: `git remote set-url origin https://richn33-sys:TOKEN@github.com/richn33-sys/mydcacalc.git`
- If Hostinger is out of sync: delete Git connection, empty public_html, reconnect and redeploy
---
## File Structure
```
~/Desktop/ClaudeWork/mydcacalc/
├── index.html                                    ← DCA Calculator (homepage)
├── position-size.html                            ← Position Size Calculator
├── compound-interest.html                        ← Compound Interest Calculator
├── dca-backtest.html                             ← DCA Backtest Simulator (NEW May 19)
├── inflation-calculator.html                     ← Inflation-Adjusted Returns Calculator (NEW May 21)
├── asset-allocation.html                         ← Asset Allocation & Risk Tolerance Quiz (NEW May 22)
├── drip-calculator.html                          ← DRIP Dividend Reinvestment Calculator (NEW May 27)
├── loss-recovery-calculator.html                 ← Investment Loss Recovery / Break-Even Calculator (NEW May 28)
├── fire-calculator.html                          ← FIRE Calculator (9th calculator, NEW Jun 1)
├── rebalancing-calculator.html                   ← Portfolio Rebalancing Calculator (10th calculator, NEW Jun 1)
├── fee-calculator.html                           ← Investment Fee Impact Calculator (11th calculator, NEW Jun 3)
├── stamp_nav.py                                  ← Single script to stamp correct full nav into any page
├── about.html
├── privacy.html
├── terms.html
├── sitemap.xml
├── deploy.py
├── .gitignore
├── personas.md
├── producthunt-launch.md                         ← PH launch assets (targets DCA Pro)
├── authors/
│   ├── james-colter.html + james-colter.jpg
│   └── sara-kline.html + sara-kline.jpg
├── guides/
│   ├── index.html                                ← 16 guides published; counter reads 16 ✅
│   ├── what-is-dollar-cost-averaging.html
│   ├── how-compound-interest-works.html
│   ├── dca-vs-lump-sum.html
│   ├── how-to-calculate-position-size.html
│   ├── how-to-invest-in-a-volatile-market.html
│   ├── bitcoin-dca-strategy.html                 ← NEW May 18
│   ├── how-to-invest-during-geopolitical-uncertainty.html  ← NEW May 19
│   ├── fear-greed-index-dca-strategy.html        ← NEW May 19
│   ├── what-is-a-good-risk-reward-ratio.html     ← NEW May 19
│   ├── strategic-bitcoin-reserve-dca.html        ← NEW May 20
│   ├── investing-during-high-interest-rates.html ← NEW May 26
│   ├── ethereum-glamsterdam-upgrade-2026.html    ← NEW May 28
│   ├── ai-stocks-vs-traditional-value.html       ← NEW May 29
│   ├── should-you-dca-into-ai-crypto-tokens.html ← NEW Jun 1 (14th guide)
│   ├── best-day-to-dca-bitcoin.html              ← NEW Jun 1 (15th guide)
│   └── 4-percent-rule-explained.html             ← NEW Jun 1 (16th guide)
└── CLAUDE.md
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
### Nav structure (as of Jun 2 2026):
- `nav.js` was ABANDONED and DELETED (Jun 2 2026) — no page ever loaded it (`grep -L "nav.js"` confirmed 0 script references). It is gone from the repo; nav is hardcoded per-page (see below).
- Nav is now HARDCODED into every page, updated via Python regex scripts when a calculator or guide is added.
- Header (calculators order): DCA · Position size · Compound interest · DCA backtest · Loss recovery · DRIP · Real returns · Asset allocation · FIRE · Rebalancing · Guides ▾
- Guides dropdown: 16 guides + "All guides →"
- Root pages: `href="guides/page.html"` for guide links
- Guide pages: `href="../page.html"` for root, `href="page.html"` for guides
- Authors pages: `href="../page.html"` for root, `href="../guides/page.html"` for guides
- Dropdown: JS hover with 300ms delay
- Mobile hamburger menu fixed site-wide Jun 1 — confirmed working on iOS
### Updating nav across all pages:
Nav is hardcoded per-page. Use `stamp_nav.py` — a single script that stamps the correct full nav into any page (handles relative path differences between root, guide, and author pages automatically). Do NOT rely on nav.js (abandoned, deleted) and do NOT hand-edit each file individually.

**Workflow to add a calculator or guide:**
1. Add the item to the CALCULATORS / GUIDES arrays in `stamp_nav.py`
2. Run `python3 stamp_nav.py --all` to re-stamp the nav across every page
3. Deploy: `python3 deploy.py "message"`
---
## Pages & Calculators
### index.html — DCA Calculator
- Forward projection + Historical backtest (S&P 500 ~10%, Nasdaq ~13%, Bitcoin ~60%)
- Asset toggles: Stocks/ETFs, Crypto
- Chart.js 4.4.1 bar chart
- **Pro CTA banner:** Added ✅
- **Keywords:** dca calculator, dollar cost averaging calculator

### position-size.html — Position Size Calculator
- Formula: (Account × Risk%) ÷ (Entry − Stop loss)
- Stocks/Crypto/Forex tabs, risk meter, breakdown table, R/R ratio
- **Pro CTA banner:** Added ✅
- **Keywords:** position size calculator, risk management calculator

### compound-interest.html — Compound Interest Calculator
- Principal, monthly contributions, rate, years, frequency, inflation, milestones
- Stacked bar chart — deposits vs interest
- **Pro CTA banner:** Added ✅
- **Keywords:** compound interest calculator, savings calculator

### dca-backtest.html — DCA Backtest Simulator (NEW May 19 2026)
- **4 assets:** BTC, ETH, S&P 500 (SPY), Nasdaq 100 (QQQ)
- **3 frequencies:** Weekly / Monthly / Quarterly
- **Return modes:** Historical avg / Conservative / Optimistic / Custom
- Inputs: amount per contribution, starting lump sum, time period (1–20yr slider)
- Outputs: total invested, final value, total return stat cards
- Live Chart.js area chart — portfolio growth vs amount invested
- Comparison table — all 4 assets ranked by final value for same inputs
- Pro CTA at bottom
- **Competitive edge:** dcaBTC.com only does Bitcoin — this does 4 assets
- **Keywords:** dca backtest calculator, bitcoin dca backtest, S&P 500 DCA calculator
- **Sitemap:** Added at priority 0.9

### fire-calculator.html — FIRE Calculator (9th calculator, NEW Jun 1 2026)
- Financial Independence / Retire Early calculator
- Inputs: current age, savings, annual income/expenses, savings rate, expected return
- Outputs: FIRE number, years to FI, projected retirement age
- **Keywords:** FIRE calculator, financial independence retire early calculator

### rebalancing-calculator.html — Portfolio Rebalancing Calculator (10th calculator, NEW Jun 1 2026)
- Calculates buy/sell amounts to return a portfolio to target allocation
- Inputs: holdings + current values, target % per asset, new contribution
- Outputs: per-asset drift and rebalancing trades
- **Keywords:** portfolio rebalancing calculator, asset allocation rebalance

### fee-calculator.html — Investment Fee Impact Calculator (11th calculator, NEW Jun 3 2026)
- Shows how expense ratios and advisory fees erode long-term returns
- Inputs: initial investment, annual contribution, years, expected return, fee %
- Outputs: final value with vs without fees, total dollars lost to fees, drag on returns
- **Keywords:** investment fee calculator, expense ratio impact calculator, fee drag calculator
---
## Author Personas
### James Colter — Long-term Investor & Personal Finance Writer
- Covers: DCA, compound interest, lump sum vs DCA, long-term investing, crypto investing
- Voice: Patient, evidence-based, uses real numbers
- Articles: all DCA/investing guides

### Sara Kline — Active Trader & Risk Management Specialist
- Covers: Position sizing, stop loss, risk/reward, trading psychology
- Voice: Direct, no-nonsense, practical
- Articles: how-to-calculate-position-size, what-is-a-good-risk-reward-ratio

### Attribution rule:
- Investing/DCA/long-term guides → James Colter
- Trading/risk management guides → Sara Kline
---
## Guides Section (16 published as of Jun 1 2026)
| File | Author | Status | Published |
|------|--------|--------|-----------|
| what-is-dollar-cost-averaging.html | James Colter | ✅ Live | Apr 2025 |
| how-compound-interest-works.html | James Colter | ✅ Live | Apr 2025 |
| dca-vs-lump-sum.html | James Colter | ✅ Live | Apr 2025 |
| how-to-calculate-position-size.html | Sara Kline | ✅ Live | Apr 2025 |
| how-to-invest-in-a-volatile-market.html | James Colter | ✅ Live | May 2026 |
| bitcoin-dca-strategy.html | James Colter | ✅ Live | May 18 2026 |
| how-to-invest-during-geopolitical-uncertainty.html | James Colter | ✅ Live | May 19 2026 |
| fear-greed-index-dca-strategy.html | James Colter | ✅ Live | May 19 2026 |
| what-is-a-good-risk-reward-ratio.html | Sara Kline | ✅ Live | May 19 2026 |
| strategic-bitcoin-reserve-dca.html | James Colter | ✅ Live | May 20 2026 |
| investing-during-high-interest-rates.html | James Colter | ✅ Live | May 26 2026 |
| ethereum-glamsterdam-upgrade-2026.html | James Colter | ✅ Live | May 28 2026 |
| ai-stocks-vs-traditional-value.html | James Colter | ✅ Live | May 29 2026 |
| should-you-dca-into-ai-crypto-tokens.html | James Colter | ✅ Live | Jun 1 2026 |
| best-day-to-dca-bitcoin.html | James Colter | ✅ Live | Jun 1 2026 |
| 4-percent-rule-explained.html | James Colter | ✅ Live | Jun 1 2026 |

### Content pipeline (every guide):
1. Claude writes + self-fact-checks
2. Rich runs through Perplexity — fact-check
3. Claude applies corrections
4. Rich runs through Grammarly
5. Claude applies final corrections
6. Rich final read → copy to guides/ folder
7. Run nav/index/sitemap update Python scripts
8. Deploy: `python3 deploy.py "message"`
9. Submit URL to Google Search Console
10. Update CURRENT_GUIDES in research_agent.py
---
## Video Automation Pipeline ✅ LIVE
- **n8n cloud:** app.n8n.cloud — instance: richnash33
- **ElevenLabs:** Creator plan — Voice: Dan — Voice ID: `fvVBPXuE7f1iX3dZLKFy`
- **Schedule:** Monday, Wednesday, Friday at 9am
- **Delivers to:** richn33@gmail.com
- **Model:** claude-sonnet-4-6
---
## Marketing

### Product Hunt Launch — THURSDAY MAY 22 2026
- **Launch URL:** https://www.producthunt.com/posts/new
- **Launch time:** 12:01am PST / 3:01am EST — macOS reminders set ✅
- **Launch file:** producthunt-launch.md (targets DCA Pro — not just free calculators)

### Product Hunt account (as of May 19 2026):
- **Username:** rich_nashawaty ✅
- **Headline:** Solo builder · Free investing tools ✅
- **Bio:** Written and saved ✅
- **Website link:** richnashawaty.com ✅
- **Avatar:** Still default — **upload headshot before May 22** ⚠️
- **Day streak:** 3 days ✅
- **Karma Points:** 1 KP
- **Badges:** Tastemaker ✅, Gone Streaking ✅

### Gallery image files (PNG — ready to upload on launch day):
- `ph-gallery-1-dca-calculator.png` — 1270×760
- `ph-gallery-2-position-size.png` — 1270×760
- `ph-gallery-3-compound-interest.png` — 1270×760
- `ph-gallery-4-guides.png` — 1270×760
- `ph-thumbnail-240x240.png` — 240×240

### Product Hunt engagement log:
| Date | Product | Upvoted | Commented | Maker Replied | We Replied Back |
|------|---------|---------|-----------|---------------|-----------------|
| May 18 | Shadow | ✅ | ✅ | ✅ | ✅ |
| May 18 | Draft | ✅ | ✅ | ✅ | ✅ |
| May 18 | Moody | ✅ | ✅ | ✅ | ✅ |
| May 18 | QuickRight | ✅ | ✅ | — | — |
| May 18 | Krea 2 | ✅ | ✅ | — | — |
| May 19 | AutoShelf | ✅ | ✅ | ✅ | ✅ |
| May 19 | Haystack | ✅ | ✅ | ✅ | ✅ |
| May 19 | Trainer | ✅ | ✅ | — | — |

### Seasoning schedule:
- May 18 ✅ — 5 upvotes, 5 comments
- May 19 ✅ — 3 upvotes, 3 comments + maker reply-backs
- **May 20 — 2–3 more comments + reply to any new maker replies**
- May 21 — rest day
- **May 22 — LAUNCH DAY**

### Launch day checklist (May 22):
- [ ] Upload profile photo (headshot) before going live
- [ ] Go live at 12:01am PST (3:01am EST)
- [ ] Go to producthunt.com/posts/new — enter https://mydcacalc.com
- [ ] Upload 5 gallery PNGs + thumbnail
- [ ] Paste tagline, description, first comment from producthunt-launch.md
- [ ] Mark yourself as Maker
- [ ] Post first comment immediately when live
- [ ] Share X post from personal account at 8am
- [ ] Reply to every comment within first hour
- [ ] Check in at 8am, noon, 6pm EST
- [ ] Do NOT ask for upvotes — ask for feedback
- [ ] Stay active in comments all day

### Content Research Agent (Gumroad product):
- Packaged and ready to sell at $39
- Files: `content-research-agent.zip` + `content-research-agent-sales-copy.md`
- Platform: Gumroad (upload zip, paste sales copy, set price)
- Proof point: runs live on mydcacalc.com, same-day published guide on first run

### Reddit strategy:
- r/SideProject, r/IndieHackers, r/passive_income — self-promotion allowed
- r/personalfinance, r/CryptoCurrency, r/Daytrading — answer questions only, drop link naturally
---
## Monetization
### DCA Pro (primary)
- $9/month or $79/year — Live at pro.mydcacalc.com ✅
- First real payment processed ✅
- Target: 200 users = $1,800 MRR → sell on Flippa at 20-30x

### Content Research Agent (Gumroad)
- $39 one-time — ready to list ✅
- Automated weekly research brief powered by Claude API

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
| dca-backtest.html | dca backtest calculator |
| drip-calculator.html | DRIP calculator dividend reinvestment |
| inflation-calculator.html | inflation adjusted returns calculator |
| asset-allocation.html | asset allocation calculator risk tolerance quiz |
| loss-recovery-calculator.html | investment loss recovery calculator / break even calculator |
| fire-calculator.html | FIRE calculator / financial independence retire early |
| rebalancing-calculator.html | portfolio rebalancing calculator |
| fee-calculator.html | investment fee calculator / expense ratio impact |
| guides/what-is-dollar-cost-averaging.html | what is dollar cost averaging |
| guides/how-compound-interest-works.html | how compound interest works |
| guides/dca-vs-lump-sum.html | dca vs lump sum |
| guides/how-to-calculate-position-size.html | how to calculate position size |
| guides/how-to-invest-in-a-volatile-market.html | how to invest in a volatile market |
| guides/bitcoin-dca-strategy.html | bitcoin dca strategy |
| guides/how-to-invest-during-geopolitical-uncertainty.html | investing during geopolitical uncertainty |
| guides/fear-greed-index-dca-strategy.html | fear greed index dca |
| guides/what-is-a-good-risk-reward-ratio.html | risk reward ratio trading |
| guides/strategic-bitcoin-reserve-dca.html | strategic bitcoin reserve DCA |
| guides/investing-during-high-interest-rates.html | investing during high interest rates |
| guides/ethereum-glamsterdam-upgrade-2026.html | ethereum glamsterdam upgrade 2026 |
| guides/ai-stocks-vs-traditional-value.html | ai stocks vs value stocks |
| guides/should-you-dca-into-ai-crypto-tokens.html | should you dca into ai crypto tokens |
| guides/best-day-to-dca-bitcoin.html | best day to dca bitcoin |
| guides/4-percent-rule-explained.html | 4 percent rule retirement withdrawal |

---
## Google AI Optimization Guidelines (May 2026)
> Source: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
> Shared and reviewed in session — applies to every guide and calculator page.

### What Google's AI systems reward:
- **Non-commodity content is critical** — unique point of view, expert-led, goes beyond common knowledge. Generic "7 tips" style content won't appear in AI Overviews. Content that goes beyond what any generative AI could produce does.
- **Standard SEO still applies** — AI Overviews and AI Mode are powered by core Search ranking systems. Fundamental SEO is still the foundation.
- **Images per guide** — Google AI features surface images. Add 1–2 relevant visuals per guide (charts, diagrams, custom visuals — not stock photos). Current guides lack images — this is the main gap to close.
- **Videos embedded on guide pages** — YouTube Shorts from the video pipeline should eventually be embedded on relevant guides.
- **Pure static HTML is an advantage** — fully crawlable, no JS rendering issues. mydcacalc.com is well-positioned here.
- **Structured data** — Article schema already in place on all guides. Consider adding FAQPage schema to guides with clear Q&A sections.
- **Agentic experiences** — clean semantic HTML (already done) is the right foundation for AI agents browsing the web.

### What to ignore (Google explicitly says don't bother):
- llms.txt files — waste of time
- "Chunking" content for AI — unnecessary
- Rewriting copy with "AI-friendly" language — waste of time
- Chasing inauthentic mentions — won't work

### What this means for every new guide:
1. Every guide needs a unique angle no one else has taken — not just a summary of existing content
2. Fact-check with Perplexity before publishing (already in pipeline ✅)
3. Add at least 1 Chart.js chart or visual diagram per guide
4. Honest caveats and accuracy matter — YMYL site, errors damage trust signals
5. Author attribution (James Colter / Sara Kline) supports E-E-A-T signals


### Google Ranking Systems Guide (second key reference)
> Source: https://developers.google.com/search/docs/appearance/ranking-systems-guide

Google uses multiple overlapping ranking systems simultaneously — not a single algorithm. Understanding which ones apply to mydcacalc.com helps prioritize what to optimize.

**Core systems that directly affect mydcacalc.com:**

- **Helpful Content System** — continuously running (not just during updates). Rewards content created for people, not for search engines. Our content pipeline is aligned with this. Guides must have genuine expert perspective, not recycled information.
- **BERT** — AI system that understands how combinations of words express meaning and intent. Rewards naturally written, semantically rich content. Write for humans — BERT penalizes keyword stuffing and rewards conversational clarity.
- **Neural Matching** — matches concepts in queries to concepts in pages, not just keywords. A page about "DCA during a crash" can rank for "should I keep investing when markets fall" — concept matching, not exact keywords.
- **RankBrain** — machine learning system for interpreting unfamiliar queries. Original, specific content that answers niche questions benefits from this.
- **MUM (Multitask Unified Model)** — understands information across topics and formats. Embedding YouTube Shorts on guide pages (video pipeline content) strengthens multi-format signals.
- **Freshness system** — rewards timely content for queries where recency matters. Timely guides (geopolitical uncertainty, Fear & Greed Index) benefit from being published close to the triggering news event.
- **Original Content system** — shows original reporting and research ahead of those who merely cite it. Our unique backtested data, charts, and original analysis are a direct ranking advantage here.
- **E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)** — not a single system but a quality evaluator used across systems. Author personas (James Colter, Sara Kline) with author pages, bios, and consistent attribution directly support this.

**What this means for content strategy:**
- Original data, charts, and analysis > summaries of other people's research
- Author attribution on every guide is not optional — it's an E-E-A-T signal
- Timely guides should be published fast — the freshness system rewards proximity to the triggering event
- Embedding YouTube videos on guide pages will eventually strengthen MUM signals
- Conceptual depth matters more than keyword density — write about the concept fully

**Systems we can mostly ignore:**
- Crisis systems — not relevant to investing content
- Exact Match Domain system — mydcacalc.com is already good here
- Deduplication system — no duplicate content issues on the site

### YMYL (Your Money or Your Life) requirements:
- mydcacalc.com is a finance site — Google applies higher accuracy standards
- All numerical claims must be fact-checked before publishing
- Disclaimers required on all guides and calculators
- Never publish specific investment recommendations
- Always include "past performance does not guarantee future results" language
---
## Research Agent ✅ LIVE
- **Location:** `~/Desktop/ClaudeWork/mydcacalc_research/`
- **Schedule:** Every Monday at 8am via launchd
- **Delivers to:** richn33@gmail.com
- **Model:** claude-opus-4-5 with web search
- **Run manually:** `python3 ~/Desktop/ClaudeWork/mydcacalc_research/research_agent.py`
- **Update CURRENT_GUIDES** whenever a new guide is published
- **Update CURRENT_CALCULATORS** whenever a new calculator is published
- **Prompt updates (Jun 1 2026):** retuned to EVERGREEN-ONLY focus (12+ month search relevance, deprioritize news/"this week" topics) + explicit NO-REPEAT instruction (do not recommend any topic already in CURRENT_GUIDES)

### Current CURRENT_GUIDES (as of Jun 2 2026 — verified against disk, 16 guides):
```python
CURRENT_GUIDES = [
    "What is dollar cost averaging",
    "How compound interest works",
    "DCA vs lump sum investing",
    "How to calculate position size",
    "How to invest in a volatile market",
    "Bitcoin DCA strategy: best day, frequency and backtested returns",
    "How to invest during geopolitical uncertainty",
    "How to use the Fear and Greed Index to optimize your DCA strategy",
    "What is a good risk reward ratio in trading",
    "What the Strategic Bitcoin Reserve means for DCA investors",
    "How to invest when interest rates are high and cuts keep getting delayed",
    "Ethereum Glamsterdam upgrade 2026: what it means for ETH investors",
    "AI stocks vs traditional value: how to balance your portfolio in 2026",
    "Should you DCA into AI crypto tokens",
    "The best day to DCA Bitcoin: why Monday has historically outperformed",
    "The 4% rule explained: is it still valid in 2026",
]
```

### Current CURRENT_CALCULATORS (as of Jun 3 2026 — verified against disk, 11 calculators):
```python
CURRENT_CALCULATORS = [
    "DCA calculator",
    "Position size calculator",
    "Compound interest calculator",
    "DCA backtest simulator (multi-asset: BTC, ETH, S&P 500, Nasdaq)",
    "Inflation-adjusted returns calculator (real return calculator)",
    "Asset allocation and risk tolerance quiz",
    "DRIP calculator (dividend reinvestment calculator)",
    "Investment loss recovery / break-even calculator",
    "FIRE calculator (financial independence, retire early)",
    "Portfolio rebalancing calculator",
    "Investment fee impact calculator",
]
```
---
## Roadmap
### Done ✅
- [x] Investment Fee Impact Calculator (11th calculator) — Jun 3 2026
- [x] stamp_nav.py — single nav-stamping script created and committed — Jun 3 2026
- [x] FIRE Calculator (9th calculator) — Jun 1 2026
- [x] Portfolio Rebalancing Calculator (10th calculator) — Jun 1 2026
- [x] Should you DCA into AI crypto tokens guide (14th guide) — Jun 1 2026
- [x] Best day to DCA Bitcoin guide (15th guide) — Jun 1 2026
- [x] The 4% rule explained guide (16th guide) — Jun 1 2026
- [x] Mobile hamburger menu fixed site-wide — confirmed working on iOS (Jun 1)
- [x] FIRE + Rebalancing calculators added to all page navs (Jun 1)
- [x] Research agent retuned — evergreen-only focus + no-repeat instruction
- [x] 3 original calculators live
- [x] DCA Backtest Simulator (4th calculator) — May 19 2026
- [x] Inflation-Adjusted Returns Calculator (5th calculator) — May 21 2026
- [x] Asset Allocation & Risk Tolerance Quiz (6th calculator) — May 22 2026
- [x] DRIP Dividend Reinvestment Calculator (7th calculator) — May 27 2026
- [x] Investment Loss Recovery / Break-Even Calculator (8th calculator) — May 28 2026
- [x] How to invest during high interest rates guide (11th guide) — May 26 2026
- [x] Ethereum Glamsterdam upgrade guide (12th guide) — May 28 2026
- [x] AI stocks vs traditional value guide (13th guide) — May 29 2026
- [x] Nav centralized in nav.js (single source across all pages) — fixes prior nav inconsistencies
- [x] Product Hunt launched — May 27 2026 (3 upvotes, 4 followers, permanent backlink)
- [x] Reddit account created — needs karma before posting
- [x] Guides index grid fixed — all 11 guides showing
- [x] Nav duplicate fix — High interest rates was showing twice on some pages
- [x] Product Hunt draft complete — launching Tuesday May 27 2026
- [x] Research agent fixed — Python path updated to /usr/local/bin/python3, confirmed working
- [x] Research agent email truncation fixed — max_tokens reduced to 1500, conciseness prompt added
- [x] Strategic Bitcoin Reserve guide (10th guide) — May 20 2026
- [x] Canonical duplicate fixed — all href="index.html" replaced with href="/"
- [x] About, Privacy, Terms, Favicon, SSL
- [x] Google Search Console + sitemap
- [x] 9 guides published (see guides table above)
- [x] Author personas (James Colter, Sara Kline) + author pages
- [x] Dropdown nav across all pages — updated to 10 guides + backtest + real returns + asset allocation
- [x] GitHub + Hostinger Git auto-deploy
- [x] Video automation (n8n + Claude + ElevenLabs)
- [x] YouTube channel + 10 TikTok scripts
- [x] Product Hunt account created + seasoned — launch May 22 ✅
- [x] PH profile complete + gallery images ready ✅
- [x] Weekly research agent live (Monday 8am)
- [x] DCA Pro built and launched (May 17 2026) ✅
- [x] Stripe live payments active ✅
- [x] Pro CTA banner on all calculator pages ✅
- [x] Welcome email via Resend — domain verified ✅
- [x] Content Research Agent packaged for Gumroad ($39) ✅

### Next session priorities:
- [x] **Product Hunt launched May 27** ✅
- [x] High interest rates guide published ✅
- [x] DRIP Calculator built and deployed ✅
- [x] **Fix nav inconsistency** — resolved by centralizing nav in nav.js (all pages now share one source) ✅
- [x] **Ethereum Glamsterdam upgrade guide** — published May 28 2026 (12th guide) ✅
- [x] **Break-Even Recovery Calculator** — built and deployed as loss-recovery-calculator.html (8th calculator), May 28 2026 ✅
- [x] **AI stocks vs traditional value guide** — published May 29 2026 (13th guide) ✅
- [x] **FIRE Calculator** — built and deployed (9th calculator), Jun 1 2026 ✅
- [x] **Portfolio Rebalancing Calculator** — built and deployed (10th calculator), Jun 1 2026 ✅
- [x] **Mobile hamburger menu fix** — fixed site-wide, working on iOS (Jun 1) ✅
- [x] **Investment Fee Impact Calculator** — built and deployed as fee-calculator.html (11th calculator), Jun 3 2026 ✅
- [ ] **Crypto DCA Portfolio guide (BTC/ETH/SOL)** — next guide to write
- [ ] **Portfolio Diversification Guide 2026** — write after the Crypto DCA Portfolio guide
- [ ] **Submit new pages to GSC** — fee-calculator, rebalancing-calculator, fire-calculator, 4-percent-rule, best-day-to-dca, should-you-dca-into-ai-crypto-tokens
- [x] **Fix guides/index.html counter** — fixed to 16 (Jun 2) ✅
- [x] **Delete vestigial nav.js** — deleted; was dead code, no page loaded it (Jun 2) ✅
- [ ] **Build Reddit karma** — new account needs comments before posting
- [ ] Update Strategic Bitcoin Reserve guide when announcement drops
- [ ] List Content Research Agent on Gumroad ($39)
- [ ] Add bottom upgrade card CTA to calculator pages (only banner exists)
- [ ] Add images to guides (Google AI optimization — 1-2 per guide)
- [ ] Sign up for affiliate programs when traffic established
- [ ] Set up hello@mydcacalc.com in Hostinger
- [ ] Post-launch: r/SideProject + r/IndieHackers posts
- [ ] Apply to Ezoic at 10k visits
---
## Session History

### Jun 3 2026 — Fee Calculator + Nav Tooling Session
- Investment Fee Impact Calculator built and deployed (fee-calculator.html, 11th calculator) — shows how expense ratios and advisory fees erode long-term returns
- **stamp_nav.py created and committed** — single script that stamps the correct full nav into any page, handling root/guide/author relative-path differences automatically
- New nav workflow established: add item to CALCULATORS/GUIDES arrays in stamp_nav.py → run `python3 stamp_nav.py --all` → deploy
- All 29 pages re-stamped with consistent nav via `stamp_nav.py --all`
- research_agent.py CURRENT_CALCULATORS updated — added "Investment fee impact calculator" (now 11 calculators)
- Next priorities set: Crypto DCA Portfolio guide, Portfolio Diversification guide, submit outstanding pages to GSC (fee-calculator, rebalancing-calculator, fire-calculator, 4-percent-rule, best-day-to-dca, should-you-dca-into-ai-crypto-tokens)

### Jun 2 2026 — Calculators + Guides Build Session
- FIRE Calculator built and deployed (9th calculator, fire-calculator.html) — Jun 1
- Portfolio Rebalancing Calculator built and deployed (10th calculator, rebalancing-calculator.html) — Jun 1
- Should you DCA into AI crypto tokens guide published (James Colter, 14th guide) — Jun 1
- Best day to DCA Bitcoin guide published (James Colter, 15th guide) — Jun 1
- The 4% rule explained guide published (James Colter, 16th guide) — Jun 1
- Mobile hamburger menu fixed site-wide — confirmed working on iOS
- FIRE + Rebalancing calculators added to all page navs
- Research agent retuned: evergreen-only focus + no-repeat instruction added to prompt
- **nav.js abandoned** — centralization attempt reverted; no page loads nav.js anymore, nav is hardcoded per-page and updated via Python regex scripts. nav.js left in repo as vestigial (flagged for deletion).
- Sitemap now ~30 URLs (27 `<loc>` entries confirmed on disk)
- Next priorities set: Investment Fee Impact Calculator, Crypto DCA Portfolio guide, Portfolio Diversification guide
- **Audit (research_agent.py vs disk):** CURRENT_GUIDES was stale (only 10 of 16) and CURRENT_CALCULATORS had a duplicate "Portfolio rebalancing calculator" entry + was missing asset-allocation and FIRE — both lists corrected to match disk (16 guides / 10 calculators)
- ⚠️ **Numbering note:** disk holds exactly 10 calculator pages, so FIRE = 9th and Rebalancing = 10th (not 10th/11th)
- ✅ **guides/index.html counter fixed** to 16 (was showing 13)
- ✅ **3 missing guide cards added** to guides/index.html: should-you-dca-into-ai-crypto-tokens, best-day-to-dca-bitcoin, 4-percent-rule-explained
- ✅ **nav.js deleted** — was dead code, no pages were loading it
- ✅ **Portfolio rebalancing calculator confirmed live** at mydcacalc.com/rebalancing-calculator.html
- ✅ **All navs updated** with Rebalancing link

### May 30 2026 — Post-Launch Build Session
- Loss Recovery / Break-Even Calculator built and deployed (8th calculator) — May 28
- Ethereum Glamsterdam upgrade guide published (James Colter, 12th guide) — May 28
- AI stocks vs traditional value guide published (James Colter, 13th guide) — May 29
- Nav centralized into nav.js — all pages now share one calculators/guides source; old per-page nav inconsistency resolved
- nav.js calculators order: DCA · Position size · Compound interest · DCA backtest · Loss recovery · DRIP · Real returns · Asset allocation
- Sitemap updated — 25 total URLs (8 calculators + guides index + 13 guides + about/privacy/terms)
- Guides index counter now reads 13
- Research agent updated: 8 calculators + 13 guides registered (CURRENT_GUIDES / CURRENT_CALCULATORS)
- CLAUDE.md audited and corrected against disk (file structure, counts, nav, SEO table, priorities)

### May 27 2026 — Launch Day Session
- Product Hunt launched — 3 upvotes, 4 followers, permanent backlink secured
- Reddit account created — posts auto-removed due to new account, needs karma building
- r/SideProject and r/IndieHackers posts written and ready for when karma is established
- How to invest during high interest rates guide published (11th guide) — May 26
- DRIP Dividend Reinvestment Calculator built and deployed (7th calculator) — May 27
- Guides index grid fixed — all 11 guide cards showing
- Nav inconsistency identified — drip-calculator.html and asset-allocation.html need fix next session
- Research agent confirmed current — 7 calculators, 11 guides registered

### May 25 2026 — Memorial Day Weekend Session
- Asset Allocation & Risk Tolerance Quiz built and deployed (6th calculator) — May 22
- Product Hunt draft finalized — launching Tuesday May 27 at 3:01am EST
- PH submission complete: name, tagline, description, tags, gallery images, shoutouts, first comment, investor section
- Research agent fixed: Python path updated from /usr/bin/python3 to /usr/local/bin/python3
- Research agent email truncation fixed: max_tokens=1500, conciseness instruction added to prompt
- Research agent confirmed working — May 25 brief delivered successfully
- Research agent fix instructions documented for use on other project agents
- May 25 research brief highlights: Fed rate hike guide (HIGH), Ethereum Glamsterdam guide (HIGH), DRIP calculator (HIGH), Break-Even Recovery calculator (MEDIUM)

### May 21 2026 — Pre-Launch Blitz
- Strategic Bitcoin Reserve guide published (James Colter) — May 20
- Inflation-Adjusted Returns Calculator (5th calculator) — May 21
- Canonical duplicate fixed: all `href="index.html"` replaced with `href="/"` site-wide
- GSC canonical issue resolved — "Alternate page with proper canonical tag" error cleared
- Nav updated to include Real Returns calculator across all pages
- Sitemap updated — 15 total URLs
- Research agent updated: 10 guides + 5 calculators registered
- CLAUDE.md fully updated with both Google guideline documents

### May 19 2026 — Content & Calculator Blitz
- Bitcoin DCA Strategy guide published (James Colter) — May 18
- Geopolitical uncertainty guide published (James Colter) — May 19
- Fear & Greed Index DCA guide published (James Colter) — May 19
- Risk/Reward Ratio guide published (Sara Kline) — May 19
- DCA Backtest Simulator built and deployed — 4 assets, comparison table, Chart.js
- Nav updated across all pages (root + all 9 guide pages) via Python regex
- Sitemap updated — 13 total URLs now
- All 9 guides + 4 calculators registered in research_agent.py
- Google Search Console submissions: all new URLs submitted
- Content Research Agent packaged as Gumroad product with sales copy

### May 19 2026 — Product Hunt Seasoning Session
- PH profile completed: headline, bio, website link
- Gallery images (4 × 1270×760) + thumbnail (240×240) ready
- 3 more products upvoted + commented
- Maker replies received and replied back
- Account at 3-day streak, Tastemaker + Gone Streaking badges
- Launch confirmed: Thursday May 22 at 12:01am PST

### May 17 2026 — DCA Pro Launch Session
- Market research → chose DCA Pro as #1 opportunity
- Supabase schema, Stripe live payments, auth system
- Dashboard, portfolio tracker, schedule manager, scenarios page
- Claude API weekly AI signal, CoinGecko live prices
- Pro CTA banner on all calculator pages
- Welcome email via Resend (now verified)
- First real payment processed ✅
