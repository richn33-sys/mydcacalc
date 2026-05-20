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
- Green banner added to top of index.html, position-size.html, compound-interest.html, dca-backtest.html
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
│   ├── index.html                                ← 9 guides published, counter = 9
│   ├── what-is-dollar-cost-averaging.html
│   ├── how-compound-interest-works.html
│   ├── dca-vs-lump-sum.html
│   ├── how-to-calculate-position-size.html
│   ├── how-to-invest-in-a-volatile-market.html
│   ├── bitcoin-dca-strategy.html                 ← NEW May 18
│   ├── how-to-invest-during-geopolitical-uncertainty.html  ← NEW May 19
│   ├── fear-greed-index-dca-strategy.html        ← NEW May 19
│   └── what-is-a-good-risk-reward-ratio.html     ← NEW May 19
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
### Nav structure (as of May 19 2026):
- Header: DCA · Position size · Compound interest · DCA backtest · Guides ▾
- Guides dropdown: 9 guides + "All guides →"
- Root pages: `href="guides/page.html"` for guide links
- Guide pages: `href="../page.html"` for root, `href="page.html"` for guides
- Authors pages: `href="../page.html"` for root, `href="../guides/page.html"` for guides
- Dropdown: JS hover with 300ms delay
### Updating nav across all pages:
When adding a new guide or calculator, use Python regex to update all pages at once — see session history for the exact script pattern. Do NOT manually edit each file.
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
## Guides Section (9 published as of May 19 2026)
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
| guides/what-is-dollar-cost-averaging.html | what is dollar cost averaging |
| guides/how-compound-interest-works.html | how compound interest works |
| guides/dca-vs-lump-sum.html | dca vs lump sum |
| guides/how-to-calculate-position-size.html | how to calculate position size |
| guides/how-to-invest-in-a-volatile-market.html | how to invest in a volatile market |
| guides/bitcoin-dca-strategy.html | bitcoin dca strategy |
| guides/how-to-invest-during-geopolitical-uncertainty.html | investing during geopolitical uncertainty |
| guides/fear-greed-index-dca-strategy.html | fear greed index dca |
| guides/what-is-a-good-risk-reward-ratio.html | risk reward ratio trading |

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

### Current CURRENT_GUIDES (as of May 19 2026):
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
]
```

### Current CURRENT_CALCULATORS (as of May 19 2026):
```python
CURRENT_CALCULATORS = [
    "DCA calculator",
    "Position size calculator",
    "Compound interest calculator",
    "DCA backtest simulator (multi-asset: BTC, ETH, S&P 500, Nasdaq)",
]
```
---
## Roadmap
### Done ✅
- [x] 3 original calculators live
- [x] DCA Backtest Simulator (4th calculator) — May 19 2026
- [x] About, Privacy, Terms, Favicon, SSL
- [x] Google Search Console + sitemap
- [x] 9 guides published (see guides table above)
- [x] Author personas (James Colter, Sara Kline) + author pages
- [x] Dropdown nav across all pages — updated to 9 guides + backtest
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
- [ ] **May 20 — 2–3 more PH comments + reply to new maker replies**
- [ ] **May 20 — Upload profile photo to PH (headshot)**
- [ ] **May 22 — PRODUCT HUNT LAUNCH DAY**
- [ ] List Content Research Agent on Gumroad ($39)
- [ ] Strategic Bitcoin Reserve guide — timely, write before announcement drops
- [ ] Add bottom upgrade card CTA to calculator pages (only banner exists)
- [ ] Add images to guides (Google AI optimization — 1-2 per guide)
- [ ] Sign up for affiliate programs when traffic established
- [ ] Set up hello@mydcacalc.com in Hostinger
- [ ] Apply to Ezoic at 10k visits
---
## Session History

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
