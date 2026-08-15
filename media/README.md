# Media sourcing notes

Policy for this project: **photographs of real historical objects and period artwork
only** — museum artifacts, period engravings and woodcuts, original book plates. No
AI-generated imagery, no modern reconstructions presented as period work, and no
mislabeled images (every caption is verified against the artwork itself).

All artwork used is old enough to be public domain as *artwork*. Practical notes for
redistribution:

1. **Images are embedded, not linked.** Lessons embed images as data URLs so each HTML
   file stays fully self-contained and offline-capable. To replace an image, re-embed
   it via `src/figs.py` + `src/build_all.py` (generated lessons) rather than adding
   external links. The Tycho lesson is hand-maintained; see its source for the pattern.
2. **Attribution.** Most embeds are public-domain period artwork or US-government
   photos (NASA/LOC). Two modern photographs of ancient/historic objects deserve
   credit before wide redistribution: the Karnak obelisk photo
   (`Obelisk_Hatschepsut.JPG`, Wikimedia Commons, CC license — credit the
   photographer) and the Woolsthorpe apple tree photo (`newtons_apple_tree_...jpg`).
   The reflecting-telescope and Rhind papyrus photos are museum photographs of
   public-domain objects.

## What's embedded where

- **Tycho & Kepler:** armillary sphere, sextant, four 1577-comet artworks, mural
  quadrant, Mysterium solids, Tycho & Kepler portraits, *De Nova Stella* nova map
  (clean Wikimedia scan), Rudolphine Tables frontispiece.
- **Newton:** Kneller portrait (1689), prism sketch, Woolsthorpe apple tree,
  *Principia* title page (1687), reflecting telescope.
- **Eratosthenes:** Rhind Mathematical Papyrus, Hatshepsut's obelisk at Karnak,
  Syene plate from the *Description de l'Égypte*.
- **1919 Eclipse:** Sobral eclipse plate (ESO re-scan), *The Times* Nov 7 1919,
  Einstein & Eddington (1930).
- **Le Gentil:** Fort Venus engraving (1773), Cook & Green's black-drop drawings (1769).
- **Pigeon Poop Nobel:** Holmdel horn antenna (NASA), the Smithsonian pigeon trap,
  Penzias & Wilson, Planck CMB map (ESA).
- **Leavitt:** her portrait, the Harvard computers workroom (~1891), a glass plate of
  Andromeda, Harvard Circular 173 p.3 (the 1912 period–luminosity figures).

## Not embedded (kept for reference only)

These files sit in this folder but are deliberately **not** used in any lesson:

- `obelisk.jpg` — 19th-c. engraving, stock-agency watermark (replaced by
  `Obelisk_Hatschepsut.JPG`)
- `papyrus.jpeg` — Rhind papyrus, stock-agency watermark (replaced by
  `Rhind_Mathematical_Papyrus.jpg`)
- `aswan.webp` — modern travel photo, unclear copyright (replaced by the
  *Description de l'Égypte* plate)
- `Point_Venus_Lighthouse...jpg` — lighthouse built 1867, a century after Cook
  (replaced by the Fort Venus engraving)
- `Appearance of Venus.jpeg` — correct 1769 plate but tiny file
  (`black-drop-effect.png` is the better copy, which is embedded)
- `tycho-brahes-drawing-of-the-supernova.jpg` — the watermarked working copy the
  clean `Tycho_Cassiopeia.jpg` scan replaced
