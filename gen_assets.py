#!/usr/bin/env python3
import os

OUT = "/home/alexa/Desktop/tor/profile-assets"

def header(idx, code, label, accent):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 64" width="1200" height="64" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="hg{idx}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="{accent}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <filter id="hf{idx}" x="-30%" y="-100%" width="160%" height="300%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="hgrid{idx}" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0H0V20" fill="none" stroke="#0e1c28" stroke-width="1" opacity="0.5"/>
    </pattern>
  </defs>
  <rect width="1200" height="64" fill="#060b12"/>
  <rect width="1200" height="64" fill="url(#hgrid{idx})"/>
  <rect x="0" y="0" width="1200" height="64" fill="url(#hg{idx})" opacity="0.25"/>
  <rect x="0" y="62" width="1200" height="2" fill="url(#hg{idx})" filter="url(#hf{idx})"/>
  <g filter="url(#hf{idx})">
    <rect x="10" y="20" width="5" height="24" fill="{accent}"/>
    <rect x="22" y="20" width="5" height="24" fill="{accent}" opacity="0.5"/>
  </g>
  <text x="44" y="40" font-family="'JetBrains Mono',monospace" font-size="22" font-weight="800"
        fill="#f1f7ff" letter-spacing="3">{label}</text>
  <text x="1190" y="40" text-anchor="end" font-family="'JetBrains Mono',monospace" font-size="13"
        fill="{accent}" letter-spacing="2">{code}</text>
  <g stroke="{accent}" stroke-width="2" fill="none" opacity="0.8">
    <path d="M0 0 L18 0 M0 0 L0 18"/>
    <path d="M1200 64 L1182 64 M1200 64 L1200 46"/>
  </g>
</svg>
'''

sections = [
    ("identity.svg", "01", "// IDENTITY", "#00ffa3"),
    ("stack.svg",    "02", "// ARSENAL",  "#00e5ff"),
    ("activity.svg", "03", "// SIGNALS",  "#ff2d55"),
]

for fn, idx, label, accent in sections:
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(header(idx, f"SYS::{idx}", label, accent))
    print("wrote", fn)

# Terminal window panel (professional console card)
term = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="terminal">
  <defs>
    <linearGradient id="tbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a1018"/>
      <stop offset="100%" stop-color="#05080d"/>
    </linearGradient>
    <filter id="tglow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect x="2" y="2" width="996" height="296" rx="12" fill="url(#tbg)" stroke="#12222f" stroke-width="2"/>
  <rect x="2" y="2" width="996" height="40" rx="12" fill="#0c1420" stroke="#12222f" stroke-width="2"/>
  <rect x="2" y="30" width="996" height="14" fill="#0c1420"/>
  <circle cx="30" cy="22" r="6" fill="#ff2d55"/>
  <circle cx="52" cy="22" r="6" fill="#ff7a18"/>
  <circle cx="74" cy="22" r="6" fill="#00ffa3"/>
  <text x="986" y="28" text-anchor="end" font-family="'JetBrains Mono',monospace" font-size="12"
        fill="#4d6a7a" letter-spacing="2">operator@dev-whale ~ zsh</text>
  <g font-family="'JetBrains Mono',monospace" font-size="16">
    <text x="28" y="78" fill="#00ffa3">$ whoami</text>
    <text x="28" y="104" fill="#d7e6f2">sanjaya@dev-whale &#183; Software Engineer + DevOps</text>
    <text x="28" y="140" fill="#00ffa3">$ cat profile.json</text>
    <text x="28" y="166" fill="#9fb4c7">{</text>
    <text x="48" y="186" fill="#7f95a8">"role"      : <tspan fill="#00e5ff">"Software Engineer + DevOps"</tspan>,</text>
    <text x="48" y="206" fill="#7f95a8">"focus"     : <tspan fill="#00e5ff">["cloud-native", "automation", "security"]</tspan>,</text>
    <text x="48" y="226" fill="#7f95a8">"community" : <tspan fill="#00e5ff">"Open Source Developers Community (OSDC)"</tspan>,</text>
    <text x="48" y="246" fill="#7f95a8">"location"  : <tspan fill="#00e5ff">"Badulla District, Uva Province, Sri Lanka"</tspan></text>
    <text x="28" y="266" fill="#9fb4c7">}</text>
  </g>
  <rect x="500" y="252" width="10" height="18" fill="#00ffa3">
    <animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>
</svg>
'''
with open(os.path.join(OUT, "terminal.svg"), "w") as f:
    f.write(term)
print("wrote terminal.svg")
