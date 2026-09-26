# AEC presentation · DeltaOps

A 16:9 HTML slide presentation for meetings with architecture, engineering and construction (AEC) practices in London. It introduces DeltaOps and the presenters, then walks through seven apps and automations built for AEC teams, one chapter per case study, each with an embedded walkthrough video.

**Live:** https://bakshilabs.github.io/aec-presentation/

## Presenting

- **Online:** open the live link.
- **Offline (recommended in client offices):** download or clone this repo and open `index.html` in Chrome. Fonts and videos are bundled, so no connection is needed (links to the live apps still need one).

| Key | Action |
|---|---|
| → / Space / click | Next slide (click the left third to go back) |
| ← | Previous slide |
| F | Fullscreen |
| N | Speaker notes |
| K | Pause or play the video |
| M | Unmute the video |
| Home / End | First / last slide |
| ? | Show the key help |

Swipe works on touch screens. The URL hash tracks the slide (`#12`), so you can link straight to a chapter.

To export a PDF, print from Chrome (Save as PDF). Each slide prints on its own 16:9 page, with the video poster frames in place of the videos.

## Structure (23 slides)

1. Cover, and about DeltaOps with the presenters
2. Case-study grid: each tile opens that repository's landing page
3. Chapter 01, winning work: Strategic Project Discovery (live search, no setup) and GrowthSignal
   (a bid-intelligence database the practice owns), with one divider, a side-by-side comparison and both walkthroughs
4. Chapters 02–06 (divider, problem and what we built, walkthrough video):
   ModelChat · Reference Buildings Explorer · MaterialScan · WorkNodesCanvas · Southwark Retrofit Atlas
5. Working together: full-day training, AI audit and discovery, automation building on retainer, forward-deployed AI architect

## Editing

All text lives in `build_deck.py`. Edit it, then run `python3 build_deck.py` to regenerate `index.html`. Styles are in `deck.css` (DeltaOps design system tokens); navigation and animation in `deck.js`.

**Presenter photos:** `assets/oliver.jpg` and `assets/arpan.jpg` (portrait, 4:5, 720×900). Replace a file and rebuild to update it; if one is missing the slide shows a placeholder rectangle.

## Case studies

| App | Landing page |
|---|---|
| Strategic Project Discovery | https://bakshilabs.github.io/StrategicProjectDiscovery-DeltaOps/ |
| GrowthSignal | https://bakshilabs.github.io/GlobalDataProbe-DeltaOps/ |
| ModelChat | https://bakshilabs.github.io/ModelChat-DeltaOps/ |
| Reference Buildings Explorer | https://bakshilabs.github.io/Reference-Buildings-Explorer-DeltaOps/ |
| MaterialScan | https://bakshilabs.github.io/MaterialScan-DeltaOps/ |
| WorkNodesCanvas | https://bakshilabs.github.io/WorkNodesCanvas-DeltaOps/ |
| Southwark Retrofit Atlas | https://bakshilabs.github.io/southwark-retrofit-atlas-DeltaOps/ |

DeltaOps · deltaops.consulting · 86–90 Paul Street, London EC2A 4NE
