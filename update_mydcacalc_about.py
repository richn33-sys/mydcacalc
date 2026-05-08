#!/usr/bin/env python3
"""
Updates ~/Desktop/ClaudeWork/mydcacalc/about.html
Adds a "Built by" / creator section before the contact section.
Run from anywhere: python3 update_mydcacalc_about.py
"""

import os

path = os.path.expanduser("~/Desktop/ClaudeWork/mydcacalc/about.html")
content = open(path).read()

new_section = """
  <h2>Who built this</h2>
  <p>MyDCACalc was built by <a href="https://richnashawaty.com" target="_blank" rel="noopener" style="color: var(--accent); text-decoration: none;">Rich Nashawaty</a>, an SEO consultant and AI automation specialist based in Boston, MA. Rich has 20 years of experience across freelance, agency, and enterprise organizations — including leading SEO strategy across global platforms with millions of pages. He builds tools, automation systems, and content properties as part of his broader work helping businesses grow through search and AI. MyDCACalc is one of several independent projects he has built to provide free, useful resources for everyday investors.</p>

"""

old = "  <h2>Contact</h2>"
new = new_section + "  <h2>Contact</h2>"

if old in content:
    content = content.replace(old, new)
    open(path, "w").write(content)
    print("✅ MyDCACalc about.html updated successfully")
    print("   Added 'Who built this' section with link to richnashawaty.com")
else:
    print("❌ Could not find insertion point — check the file manually")
    print("   Looking for: 'Contact'")
