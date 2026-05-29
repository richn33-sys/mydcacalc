import os

base = '/Users/richardnashawaty/Desktop/ClaudeWork/mydcacalc'

content = {}

content['index.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the DCA calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Dollar-cost averaging (DCA) means investing a fixed amount at regular intervals regardless of price. This calculator projects what your portfolio could be worth over time based on your contribution amount, frequency, expected return rate, and time horizon. Switch to backtest mode to see what the same strategy would have returned historically against real S&P 500, Nasdaq, or Bitcoin price data.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">The forward projection uses compound growth math — your contributions earn returns, those returns earn more returns, and so on. The power of DCA is not just in the compounding but in the behavioral discipline it creates: because you invest the same amount regardless of market conditions, you automatically buy more shares when prices are low and fewer when prices are high.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Enter your initial lump sum (or leave at $0 to start fresh) and your regular contribution amount.</li>
      <li style="margin-bottom:10px;">Set your expected annual return rate. The S&P 500 has averaged approximately 10% annually over long periods; a more conservative estimate is 6-7% after inflation.</li>
      <li style="margin-bottom:10px;">Adjust the time horizon to see how compounding accelerates over longer periods.</li>
      <li style="margin-bottom:10px;">Switch to backtest mode to see historical results instead of projections.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">Want to understand DCA more deeply? Read our guide on <a href="guides/what-is-dollar-cost-averaging.html" style="color:#c8f060;text-decoration:none;">what dollar-cost averaging is</a> and how it compares to <a href="guides/dca-vs-lump-sum.html" style="color:#c8f060;text-decoration:none;">lump sum investing</a>.</p>
  </div>
'''

content['position-size.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the position size calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Position sizing answers the question: how many shares or coins should I buy on this trade? The calculation is driven by three inputs: your account size, the percentage of that account you are willing to risk on a single trade, and the distance between your entry price and your stop loss. The formula is: <strong style="color:#f0efe8;">Position size = (Account x Risk%) / (Entry - Stop loss)</strong>.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Most professional traders risk between 0.5% and 2% of their account per trade. Risking more than 2% per trade means a string of losses can cause severe drawdowns that are difficult to recover from. Risking less than 0.5% often makes the potential reward too small to justify the trade.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Enter your total account size — the full amount you have available to trade, not just what you plan to put in this trade.</li>
      <li style="margin-bottom:10px;">Set your risk percentage. Start with 1% if you are unsure.</li>
      <li style="margin-bottom:10px;">Enter your entry price and your stop loss price. The stop loss is where you would exit if the trade goes against you.</li>
      <li style="margin-bottom:10px;">The calculator tells you exactly how many shares or units to buy so your total risk equals your set percentage.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">Learn more about how position sizing fits into a complete risk management framework in our guide on <a href="guides/what-is-a-good-risk-reward-ratio.html" style="color:#c8f060;text-decoration:none;">risk/reward ratios</a>.</p>
  </div>
'''

content['compound-interest.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the compound interest calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Compound interest is growth on top of growth. Unlike simple interest, which only calculates returns on your original principal, compound interest calculates returns on your principal plus all previously earned returns. Over long periods, this creates exponential rather than linear growth. The Rule of 72 gives you a quick mental estimate: divide 72 by your annual return rate to find how many years it takes to double your money. At 7% your money doubles roughly every 10 years. At 10%, roughly every 7 years.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">The difference between starting at 25 vs 35 — just 10 years — is typically more than one full doubling cycle. Time in the market is the most powerful variable in the compound interest equation, which is why early consistent investing consistently outperforms larger contributions started later.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Enter your initial investment and any regular monthly contribution.</li>
      <li style="margin-bottom:10px;">Set your expected annual return rate and compounding frequency. Monthly compounding is the most common for investment accounts.</li>
      <li style="margin-bottom:10px;">Adjust the time period to see how dramatically longer horizons improve outcomes.</li>
      <li style="margin-bottom:10px;">The milestone markers show you when you hit key portfolio values — useful for visualizing the acceleration effect in the later years.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">Read our full guide on <a href="guides/how-compound-interest-works.html" style="color:#c8f060;text-decoration:none;">how compound interest works</a> for a deeper explanation with real-world examples.</p>
  </div>
'''

content['dca-backtest.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the DCA backtest simulator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">This simulator shows what would have happened if you had DCA'd a fixed monthly amount into Bitcoin, Ethereum, S&P 500, or Nasdaq over historical periods. Unlike a forward projection that uses assumed return rates, a backtest uses actual historical price data — giving you a concrete sense of what DCA returns have looked like across different market cycles including crashes, recoveries, and bull runs.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">The side-by-side comparison lets you see how the same DCA strategy performs across very different asset classes. Bitcoin's historical DCA returns have been dramatically higher than the S&P 500 but with far greater volatility. The backtest makes that comparison concrete with real numbers rather than projections.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this simulator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Select the asset you want to backtest: BTC, ETH, S&P 500, or Nasdaq.</li>
      <li style="margin-bottom:10px;">Set your monthly contribution amount and the time period for your backtest.</li>
      <li style="margin-bottom:10px;">The results show total invested, current value, and return percentage based on historical data.</li>
      <li style="margin-bottom:10px;">Use the comparison view to run the same strategy across multiple assets simultaneously.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">For strategy context, read our guides on <a href="guides/bitcoin-dca-strategy.html" style="color:#c8f060;text-decoration:none;">Bitcoin DCA strategy</a> and <a href="guides/fear-greed-index-dca-strategy.html" style="color:#c8f060;text-decoration:none;">how to use the Fear &amp; Greed Index to optimize your DCA timing</a>.</p>
  </div>
'''

content['inflation-calculator.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the inflation-adjusted returns calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Your nominal return is what your portfolio shows on paper. Your real return is what that growth is actually worth in purchasing power after accounting for inflation. If your portfolio returns 7% in a year when inflation runs at 3%, your real return is approximately 4%. This calculator uses the Fisher equation to show both figures side by side: nominal value, real value in today's dollars, and how much purchasing power is silently eroded over time.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">The U.S. historical average inflation rate is approximately 3.5% from 1926 through 2024, though it has varied significantly. The Fed's current target is 2%. Using 3-3.5% as a long-term planning assumption is reasonable. Using 0% ignores inflation entirely and will overstate your real wealth accumulation.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Enter your initial investment, monthly contribution, and expected annual return rate.</li>
      <li style="margin-bottom:10px;">Set your inflation assumption using the presets: 2% (Fed target), 3.5% (historical average), or 7% (high inflation environment).</li>
      <li style="margin-bottom:10px;">The chart shows both your nominal value and your real value in today's dollars — the gap between them is purchasing power lost to inflation.</li>
      <li style="margin-bottom:10px;">The breakdown table shows the divergence at 5-year intervals across your full time horizon.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">For more context on investing in inflationary environments, read our guide on <a href="guides/investing-during-high-interest-rates.html" style="color:#c8f060;text-decoration:none;">how to invest when interest rates are high</a>.</p>
  </div>
'''

content['asset-allocation.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the asset allocation quiz works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Asset allocation is how you divide your portfolio among different asset classes: stocks, bonds, cash, and crypto. It is the single most important investment decision most people make, yet most people never make it deliberately. Research consistently shows that asset allocation accounts for the majority of long-term portfolio variance — more than individual security selection or market timing.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">This quiz scores your responses across eight dimensions — time horizon, investment goal, loss tolerance, experience level, income stability, emergency fund status, risk attitude, and crypto interest — to recommend one of six portfolio profiles ranging from Capital Preservation to High-Growth Crypto. Each profile includes expected return ranges, historical worst-year estimates, and a recommended breakdown across all four asset classes.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this quiz</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Answer all 8 questions honestly — particularly the crash scenario question, which is the most revealing indicator of real risk tolerance.</li>
      <li style="margin-bottom:10px;">Your recommended allocation is a starting point, not a prescription. Adjust based on your specific circumstances and goals.</li>
      <li style="margin-bottom:10px;">Retake the quiz periodically — your risk tolerance and time horizon change as your life circumstances evolve.</li>
      <li style="margin-bottom:10px;">Use the backtest link in your results to see how similar historical portfolios have performed.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">For more on managing volatility within your chosen allocation, see our guide on <a href="guides/how-to-invest-in-a-volatile-market.html" style="color:#c8f060;text-decoration:none;">how to invest in a volatile market</a>.</p>
  </div>
'''

content['drip-calculator.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the DRIP calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">A Dividend Reinvestment Plan (DRIP) automatically uses dividend payments to purchase additional shares rather than paying them out as cash. This creates a compounding effect: more shares generate more dividends, which buy more shares. Over decades, the difference between taking dividends as cash and reinvesting them can be substantial — reinvested dividends have historically contributed a significant portion of total equity returns over long holding periods.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">This calculator separates three variables that are often conflated: dividend yield (the percentage of share price paid as dividends annually), dividend growth rate (how fast the dividend payment grows each year), and stock price appreciation (capital gains). Running all three simultaneously shows the true compounding power of DRIP versus taking dividends as cash.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Use the presets to start with common scenarios: S&P 500 average, a typical dividend stock, or a high-yield position.</li>
      <li style="margin-bottom:10px;">Adjust the sliders to match a specific stock or ETF you are evaluating.</li>
      <li style="margin-bottom:10px;">The chart compares DRIP vs taking cash dividends with the same price appreciation — the gap shows the pure compounding value of reinvestment.</li>
      <li style="margin-bottom:10px;">The annual income figure in the final year shows what your dividend income stream looks like at the end of the period — useful for retirement income planning.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">DRIP investing pairs well with a consistent DCA strategy. Use the <a href="/" style="color:#c8f060;text-decoration:none;">DCA calculator</a> to model your contribution schedule alongside dividend reinvestment for a complete picture.</p>
  </div>
'''

content['loss-recovery-calculator.html'] = '''
  <div class="content-section" style="max-width:860px;margin:0 auto;padding:0 24px 60px;">
    <h2 style="font-size:20px;font-weight:600;letter-spacing:-0.02em;margin-bottom:16px;color:#f0efe8;">How the loss recovery calculator works</h2>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">Investment losses require a disproportionately larger gain to recover — this is one of the most counterintuitive facts in personal finance. A 50% loss requires a 100% gain to break even. A 70% loss requires a 233% gain. The math is asymmetric because you are earning returns on a smaller base after the loss. This calculator shows exactly what gain is needed for any loss level and how long recovery takes at different return rates.</p>
    <p style="color:#888884;font-weight:300;margin-bottom:16px;line-height:1.75;">The DCA effect is where this calculator becomes particularly useful. By continuing to invest after a market decline, you are buying additional shares at lower prices — which lowers your average cost basis. A lower average cost means you need a smaller price recovery to reach break-even. The calculator compares recovery time with and without ongoing DCA contributions to show how much faster break-even arrives when you keep investing through the downturn.</p>
    <h3 style="font-size:16px;font-weight:500;color:#f0efe8;margin:28px 0 12px;">How to use this calculator</h3>
    <ul style="color:#888884;font-weight:300;padding-left:22px;line-height:1.75;">
      <li style="margin-bottom:10px;">Use the quick-select presets or slider to set your loss percentage. Try the scenario presets for real-world examples like the 2022 bear market or a Bitcoin cycle crash.</li>
      <li style="margin-bottom:10px;">Set your expected annual return rate for the recovery period and any monthly DCA contribution you plan to make.</li>
      <li style="margin-bottom:10px;">Compare recovery time without DCA vs with DCA to see how much your contributions accelerate break-even.</li>
      <li style="margin-bottom:10px;">The reference table at the bottom shows all loss levels side by side — useful for understanding the asymmetric nature of losses across the full range.</li>
    </ul>
    <p style="color:#888884;font-weight:300;margin-bottom:0;line-height:1.75;">For strategy context on investing through downturns, read our guide on <a href="guides/how-to-invest-in-a-volatile-market.html" style="color:#c8f060;text-decoration:none;">how to invest in a volatile market</a> and <a href="guides/fear-greed-index-dca-strategy.html" style="color:#c8f060;text-decoration:none;">using the Fear &amp; Greed Index for DCA timing</a>.</p>
  </div>
'''

# Insert before </main> or <footer> in each file
for fname, section in content.items():
    path = f'{base}/{fname}'
    if not os.path.exists(path):
        print(f"SKIP (not found): {fname}")
        continue
    with open(path) as f: c = f.read()
    if section.strip()[:30] in c:
        print(f"Already has content: {fname}")
        continue
    if '<footer>' in c:
        c = c.replace('<footer>', section + '\n<footer>')
        with open(path, 'w') as f: f.write(c)
        print(f"Added content: {fname}")
    else:
        print(f"No footer found: {fname}")

print("\nAll done!")
