"""Builds index.html, the AEC case-study deck, from the content below.

Edit the text in this file, then run:  python3 build_deck.py
Presenter photos: assets/oliver.jpg and assets/arpan.jpg (4:5). If one is missing,
the slide shows a placeholder rectangle.
"""
import hashlib
import html
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGES = "https://bakshilabs.github.io"
e = html.escape

def v(rel):  # cache-busting version tag, so browsers and the Pages CDN pick up changed files
    f = HERE / rel
    return f"{rel}?v={hashlib.sha1(f.read_bytes()).hexdigest()[:8]}" if f.exists() else rel

# ---------------------------------------------------------------- content
CASES = [
    # lifecycle stage, slug, repo, name, eyebrow, title, challenge, built, features, stat, stack, notes
    ("Win work", "strategic-project-discovery", "StrategicProjectDiscovery-DeltaOps", "Strategic Project Discovery", "Live project search",
     "Live project search, no setup.",
     "Business development teams check the same portals by hand, one sector at a time.",
     "A scanner across 676 procurement sources in seven sectors. Each result is plotted on a map with a fit assessment.",
     [("Seven sectors", "Rail, transit-oriented development, regeneration, data centres, ports, major projects and sustainability."),
      ("Map view", "Each opportunity plotted and coloured by urgency."),
      ("Fit assessment", "Sector, scale and geography fit, with an estimated win probability.")],
     ("676", "procurement sources", "Across 36 categories"),
     ["React", "Leaflet", "Gemini"],
     "A lighter tool for the same task: one web page to run before a pipeline meeting."),
    ("Win work", "growthsignal", "GlobalDataProbe-DeltaOps", "GrowthSignal", "Bid-intelligence database",
     "A bid-intelligence database you own.",
     "Opportunities are spread across hundreds of procurement portals, development bank registers and news sources. Teams often find them late.",
     "A self-hosted database of 29,439 tenders and programmes from over 270 public sources. Claude tags each record with sector, stage, value and location, and the full set is searchable.",
     [("Search", "Keyword and semantic search across tenders, programmes, deals and news."),
      ("Pursuit scoring", "Fit on sector, scale and geography, with an estimated win probability."),
      ("Daily briefing", "A short morning summary of new and changed opportunities.")],
     ("270+", "public sources", "Procurement portals, development banks, filings, news"),
     ["Next.js", "SQLite", "Claude"],
     "Finding work. The practice holds the data itself instead of renting it through a subscription."),
    ("Design", "modelchat", "ModelChat-DeltaOps", "ModelChat", "BIM model queries",
     "Questions to a BIM model in plain English.",
     "Getting answers out of a BIM model usually needs a specialist and a desktop licence.",
     "A browser IFC viewer with a chat panel. Claude answers by querying the model index and operating the viewer: isolate, highlight, section, measure.",
     [("Plain-English questions", "What is the floor area of Level 3? Show only the columns."),
      ("Fourteen model tools", "Index queries and quantity take-offs, plus actions in the viewer."),
      ("Runs in the browser", "No plug-in or API key. The chat uses a local Claude login.")],
     ("14", "model tools available to Claude", "6 on the model index · 8 in the viewer"),
     ["three.js", "web-ifc", "Claude Code"],
     "Anyone on the team can query the model without opening Revit. The walkthrough uses a ten-storey timber office exported from Revit."),
    ("Design", "reference-buildings-explorer", "Reference-Buildings-Explorer-DeltaOps", "Reference Buildings Explorer", "Energy modelling",
     "Energy model results in 3D.",
     "Energy model results sit in spreadsheets and HTML reports that are hard to compare.",
     "The US DOE commercial reference buildings, 16 types in 16 climates, with EnergyPlus geometry and results in six interactive 3D views.",
     [("Model geometry", "Section cuts, exploded floors and zones coloured by result."),
      ("All 256 cases", "Every building and climate combination, compared climate by climate."),
      ("Weather and schedules", "8,760 hours of climate data and hourly operating schedules.")],
     ("256", "building and climate combinations", "DOE reference buildings · ASHRAE 90.1-2004"),
     ["three.js", "EnergyPlus", "Python"],
     "Simulation output in a form a design review can use. One HTML file, no install."),
    ("Design", "materialscan", "MaterialScan-DeltaOps", "MaterialScan", "Material compliance",
     "Material compliance against three standards.",
     "Certification evidence for each product sits in spreadsheets, PDFs and email.",
     "A dashboard that scores each product against LBC 4.1, WELL v2 and the client brief, with the relevant clause and evidence alongside.",
     [("Summary by standard", "Pass, partial, gap and fail counts for each standard."),
      ("Scorecard per material", "The result, the rule behind it and the evidence."),
      ("Outstanding gaps", "The documentation still needed, in priority order.")],
     ("3", "standards checked per product", "LBC 4.1 · WELL v2 · client brief"),
     ["Python", "Static HTML", "Claude Code"],
     "Shows which evidence is missing at the start of the process rather than the end."),
    ("Deliver", "worknodescanvas", "WorkNodesCanvas-DeltaOps", "WorkNodesCanvas", "Document workbench",
     "From source documents to finished reports.",
     "Turning surveys, workshop notes and data into client documents takes hours of copying and rewriting.",
     "A canvas where source files feed Claude analyses, and analyses feed decks, documents and web pages.",
     [("Sources on the canvas", "PDF, image, Markdown and Office files, previewed in place."),
      ("Analyses", "Set an objective and connect sources. Claude reads them and answers."),
      ("Outputs", "Generate a PPTX, DOCX or HTML file from connected analyses.")],
     ("3", "node types on one canvas", "Reference · analysis · presentation"),
     ["Python", "Vanilla JS", "Claude Code"],
     "Report writing during delivery. A live demo runs on the landing page."),
    ("Portfolio", "southwark-retrofit-atlas", "southwark-retrofit-atlas-DeltaOps", "Southwark Retrofit Atlas", "Housing retrofit",
     "Retrofit priorities for 149,062 homes.",
     "Portfolio owners need to know which homes to retrofit first, what it costs, and what a fixed budget covers.",
     "A costed retrofit package for every home in Southwark, ranked on carbon, need and deliverability, with an adjustable prioritisation model.",
     [("Every home mapped", "EPC band now and after retrofit, as points or hexagons."),
      ("Prioritisation", "Set a budget and weights, and the programme re-ranks every home."),
      ("Wards and non-domestic stock", "Need by ward, plus 7,045 non-domestic buildings.")],
     ("149,062", "homes costed", "GLA LBSM 2 · EPC register · ONS"),
     ["d3", "Canvas", "Open data"],
     "Portfolio decisions for clients and local authorities, built on open data."),
]

# ---------------------------------------------------------------- templates
def a(i):  # animation stagger
    return f' data-a style="--i:{i}"'

def frame(kind, body, notes, cls="", foot=True, logo=True):
    logo_src = "assets/logo-white.svg" if kind == "ink" else "assets/logo-dark.svg"
    chrome = ""
    if logo:
        chrome += f'<img class="logo" src="{logo_src}" alt="DeltaOps">'
    if foot:
        chrome += '<div class="foot mono">DeltaOps · Apps and automation for AEC</div><div class="pagenum mono"></div>'
    return f'<section class="slide {kind} {cls}" data-notes="{e(notes)}">{chrome}{body}</section>'

def cover():
    return frame("ink", f'''
      <div class="aurora" style="top:-320px;left:52%"></div>
      <div class="cover-body">
        <div class="eyebrow"{a(0)}>DeltaOps · Architecture, Engineering and Construction</div>
        <h1 class="display"{a(1)}>Apps and automations for AEC.</h1>
        <p class="lede"{a(2)}>Seven tools we have built, from bid screening to portfolio planning. For each one: the problem, what we built, and a short walkthrough.</p>
        <div class="presenters mono"{a(3)}>Oliver Ramirez · Arpan Bakshi &nbsp;·&nbsp; deltaops.consulting</div>
      </div>''', "Seven tools, each shown running. Questions at any point.",
      cls="cover", foot=False)

def presenters():
    people = [("oliver", "Oliver Ramirez", "Founder & CEO", "EMEA operations and cross-continental projects at Amazon, then Google AI. Anthropic certified."),
              ("arpan", "Arpan Bakshi", "AEC apps and automation", "Built the seven tools in this deck: data pipelines, 3D viewers and Claude-based workflows.")]
    cards = "".join(f'''
      <div class="person"{a(3 + i)}>
        <div class="photo"><img src="{v(f'assets/{slug}.jpg')}" alt="{name}" onerror="this.remove()"><span class="mono">Photo · {name.split()[0]}</span></div>
        <div><h3>{name}</h3><div class="role mono">{role}</div><p>{bio}</p></div>
      </div>''' for i, (slug, name, role, bio) in enumerate(people))
    return frame("paper", f'''
      <div class="eyebrow"{a(0)}>About DeltaOps</div>
      <h2 class="title"{a(1)}>Operations and AI consultancy, London.</h2>
      <p class="lede"{a(2)}>We map how work moves through a practice, then build apps and automations to improve it, using the tools already in place.</p>
      <div class="people">{cards}</div>''',
      "Introductions.")

# The two bid-intelligence tools (CASES[0:2]) share chapter 01; the rest get one chapter each.
def chapter_no(i):
    return f"{max(1, i):02d}"

def grid():
    tiles = "".join(f'''
      <a class="tile" href="{PAGES}/{repo}/" target="_blank" rel="noopener"{a(2 + i)}>
        <img src="{v(f'media/{slug}-hero.jpg')}" alt="{name}"><div class="tile-body"><div class="mono tile-stage">{chapter_no(i)} · {stage}</div><div class="tile-name">{name}</div><div class="tile-sub">{eyebrow}</div></div>
      </a>''' for i, (stage, slug, repo, name, eyebrow, *_rest) in enumerate(CASES))
    return frame("paper", f'''
      <div class="eyebrow"{a(0)}>Case studies</div>
      <h2 class="title"{a(1)}>Seven tools across the project lifecycle.</h2>
      <div class="tiles">{tiles}<div class="tile legend"{a(9)}><div class="mono tile-stage">How to read this</div><p>Each tile opens the project page: walkthrough, source code and, where possible, the running app.</p></div></div>''',
      "The seven tools in order. Each tile opens a public project page.", foot=False)

def demo(n, case):
    stage, slug, repo, name, *_ = case
    url = f"{PAGES}/{repo}/"
    return frame("ink", f'''
      <div class="demo-head"><div class="eyebrow"{a(0)}>{n} · Walkthrough</div><h2 class="title-sm"{a(1)}>{e(name)}</h2></div>
      <div class="video"{a(2)}><video src="{v(f'media/{slug}.mp4')}" poster="{v(f'media/{slug}.jpg')}" muted playsinline preload="metadata" controls></video></div>
      <div class="demo-foot mono"{a(3)}>Live at <a href="{url}" target="_blank" rel="noopener">{url.replace("https://", "")}</a> &nbsp;·&nbsp; M to unmute &nbsp;·&nbsp; K to pause</div>''',
      f"Walkthrough of {name}. K pauses the video.", cls="demo")

def chapter(n, case):
    stage, slug, repo, name, eyebrow, title, challenge, built, feats, (sv, st, sc), stack, notes = case
    url = f"{PAGES}/{repo}/"
    divider = frame("paper", f'''
      <div class="divider-body">
        <div>
          <div class="eyebrow"{a(0)}>{n} · {stage} · {e(eyebrow)}</div>
          <h2 class="display"{a(1)}>{title}</h2>
          <div class="rule-strong"{a(2)}></div>
          <p class="lede"{a(3)}>{e(challenge)}</p>
        </div>
        <div class="divider-shot"{a(4)}><img src="{v(f'media/{slug}-hero.jpg')}" alt="{e(name)}"></div>
      </div>''', notes, cls="divider")
    rows = "".join(f'<div class="row"{a(5 + j)}><div class="num mono">{j + 1:02d}</div><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for j, (t, d) in enumerate(feats))
    strap = ' <span class="sep">·</span> '.join(f"<b>{e(s)}</b>" for s in stack)  # link sits at the right edge
    overview = frame("paper", f'''
      <div class="eyebrow"{a(0)}>{n} · {e(name)}</div>
      <div class="two overview">
        <div>
          <div class="label mono"{a(1)}>Problem</div>
          <p class="body-lg"{a(2)}>{e(challenge)}</p>
          <div class="label mono"{a(3)}>What we built</div>
          <p class="body-lg"{a(4)}>{e(built)}</p>
          <div class="stat"{a(8)}><div class="value">{e(sv)}</div><div class="rule"></div><div class="text">{e(st)}<span class="cite">{e(sc)}</span></div></div>
        </div>
        <div class="rows">{rows}</div>
      </div>
      <div class="strap mono"{a(9)}><span class="muted">Built with</span> {strap} <a href="{url}" target="_blank" rel="noopener">{url.replace("https://", "")}</a></div>''',
      f"{built}")
    return divider + overview + demo(n, case)

# Chapter 01: two tools for the same job, presented as two tiers.
COMPARE = [
    ("How it works", "Gemini with Google Search runs a live search across 676 procurement sources on each scan.",
                     "Connectors collect 29,439 tenders and programmes from 270+ public sources on every update run."),
    ("Setup", "None: one web page and an API key.", "A server, a SQLite database and a Claude login."),
    ("Coverage", "Anything web search can find, including portals without a connector.",
                 "Connected sources only, but complete, repeatable and de-duplicated."),
    ("Memory", "Each scan stands alone and saves as a JSON file.", "Full history: record updates, notes and duplicate merging."),
    ("Ranking", "A fit assessment per result: sector, scale and geography, with an estimated win probability.",
                "Sector fit, project stage, value and corroborating sources, set against a firm's target sectors, stages and countries."),
    ("Best for", "A BD lead before a pipeline meeting.", "A BD team running its pipeline every day."),
]

def win_chapter(spd, gs):
    n = "01"
    challenge = gs[6]
    divider = frame("paper", f'''
      <div class="divider-body">
        <div>
          <div class="eyebrow"{a(0)}>{n} · Win work · Bid intelligence</div>
          <h2 class="display"{a(1)}>Finding work, two ways.</h2>
          <div class="rule-strong"{a(2)}></div>
          <p class="lede"{a(3)}>{e(challenge)}</p>
        </div>
        <div class="divider-pair">
          <div class="divider-shot"{a(4)}><img src="{v(f'media/{spd[1]}-hero.jpg')}" alt="{e(spd[3])}"></div>
          <div class="divider-shot"{a(5)}><img src="{v(f'media/{gs[1]}-hero.jpg')}" alt="{e(gs[3])}"></div>
        </div>
      </div>''', "Two tools for the same job. Start with the scan; build the database when the practice wants its own bid intelligence.", cls="divider")
    head = "".join(f'<th><span class="mono">{e(c[4])}</span>{e(c[3])}</th>' for c in (spd, gs))
    body = "".join(f'<tr{a(3 + j)}><td class="k mono">{e(k)}</td><td>{e(x)}</td><td>{e(y)}</td></tr>' for j, (k, x, y) in enumerate(COMPARE))
    compare = frame("paper", f'''
      <div class="eyebrow"{a(0)}>{n} · Two tiers</div>
      <h2 class="title"{a(1)}>A quick scan, or a database you own.</h2>
      <table class="compare"{a(2)}><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>''',
      "Discovery shows value in the first week, with no setup. GrowthSignal is the system a BD team runs every day. They map to the audit and to the retainer.")
    return divider + compare + demo(n, spd) + demo(n, gs)

def together():
    offers = [("1 day · on-site", "Full-day training", "Hands-on AI and automation training for your team, using your own tools and project files."),
              ("Interviews · workshops", "AI audit and discovery", "Interviews with your teams, a map of where time goes, and a prioritised list of what to automate."),
              ("Monthly retainer", "Automation building", "We build and maintain tools for your team, delivered in small increments."),
              ("6 months · 1–2 days a week", "Forward-deployed AI architect", "An AI architect in your office one to two days a week, working with your team.")]
    cards = "".join(f'<div class="card"{a(2 + i)}><div class="num mono">{f}</div><h3>{t}</h3><p>{d}</p></div>' for i, (f, t, d) in enumerate(offers))
    return frame("paper", f'''
      <div class="eyebrow"{a(0)}>Working together</div>
      <h2 class="title"{a(1)}>Ways to work with us.</h2>
      <div class="grid4 offers">{cards}</div>
      <div class="contact mono"{a(6)}>deltaops.consulting &nbsp;·&nbsp; 86–90 Paul Street, London EC2A 4NE</div>''',
      "Four engagement models. Training or the audit are the usual starting points.", foot=False)

slides = ([cover(), presenters(), grid(), win_chapter(CASES[0], CASES[1])]
          + [chapter(chapter_no(i), c) for i, c in enumerate(CASES) if i >= 2] + [together()])

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Apps and automations for AEC · DeltaOps</title>
<meta name="description" content="DeltaOps case studies: seven apps and automations built for architecture, engineering and construction teams.">
<link rel="icon" href="assets/logo-dark.svg">
<link rel="stylesheet" href="{v('deck.css')}">
</head>
<body>
<div class="viewport"><div class="stage" id="stage">
{"".join(slides)}
</div></div>
<div class="progress"><div class="bar" id="bar"></div></div>
<div class="notes" id="notes" hidden></div>
<div class="help mono" id="help" hidden>← → or click: navigate · F: fullscreen · N: speaker notes · M: unmute · K: pause video · Home / End</div>
<script src="{v('deck.js')}"></script>
</body>
</html>
'''
(HERE / "index.html").write_text(page, encoding="utf-8")
print(f"wrote index.html · {page.count('<section')} slides")
