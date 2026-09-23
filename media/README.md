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
- **Socrates, Plato & Aristotle:** Socrates bust (Louvre Ma 59), bronze Athenian juror
  ballots, David's *Death of Socrates* (Met original), Plato bust (Capitoline MC1377),
  the Pompeii Academy mosaic, Kepler's 1596 nested solids (shared with the Tycho
  lesson), nine of Leonardo's 1498 polyhedron plates, Saenredam's 1604 cave engraving,
  Raphael's *School of Athens*, Aristotle bust (Palazzo Altemps), the Pompeii marine
  mosaic, and a four-frame lunar eclipse. Twelve of thirteen slots filled; Chapter
  Seven's is deliberately empty (see below).

## Wish list — Great Coincidence (Sun/Moon) lesson

- A total-eclipse corona photograph (NASA's are public domain).
- An annular "ring of fire" photograph.
- The "diamond ring" moment.
- An Apollo lunar retroreflector on the surface (NASA, public domain) — for the
  laser-ranging / 3.8 cm-per-year chapter.

## Wish list — Galileo lesson

- Justus Sustermans' portrait of Galileo (1636) — Uffizi; high-res on Wikimedia Commons.
- Galileo's two surviving telescopes (Museo Galileo, Florence).
- His wash drawings of the Moon from *Sidereus Nuncius* (1610), and the notebook
  pages tracking Jupiter's moons night by night (little stars beside a circle).
- The frontispiece of the *Dialogue* (1632) — the three philosophers arguing.
- His middle finger, preserved in a glass reliquary at the Museo Galileo (really).

## Wish list — Socrates, Plato & Aristotle lesson

Slots are already wired in `src/figs.py`; drop a file in with the exact name and
rebuild. Missing files are skipped with a printed warning, so partial sets build
fine. Captions in `figs.py` are drafted for the canonical artifact — **verify each
against the file you actually pull** before shipping.

| Save as | What to find |
|---|---|
| `socrates-bust.jpg` | Roman marble bust of Socrates (Louvre Ma 59, or the British Museum / Naples copy) |
| `juror-ballots.jpg` | Bronze Athenian juror ballots, 4th c. BC, Ancient Agora Museum (hollow vs. solid axle) |
| `death-of-socrates-david.jpg` | Jacques-Louis David, *The Death of Socrates*, 1787 (Met, open access) |
| `plato-bust.jpg` | Roman bust of Plato after Silanion (Capitoline MC1377, or Vatican / Munich copy) |
| `academy-mosaic-pompeii.jpg` | "Plato's Academy" mosaic from Pompeii, 1st c. BC (Naples Archaeological Museum) |
| `pacioli-polyhedra.jpg` | Leonardo's polyhedra plates from Pacioli, *De divina proportione*, 1509 |
| `saenredam-plato-cave-1604.jpg` | Jan Saenredam's 1604 engraving of the cave, after Cornelis van Haarlem |
| `school-of-athens-detail.jpg` | Raphael, *School of Athens* (1511) — central detail, Plato up / Aristotle down |
| `aristotle-bust.jpg` | Roman bust of Aristotle after Lysippos (Palazzo Altemps / Ludovisi) |
| `roman-marine-mosaic.jpg` | Roman marine-life mosaic from Pompeii (octopus, moray, lobster), Naples |
| `lunar-eclipse-sequence.jpg` | Composite/sequence photo of a lunar eclipse showing Earth's curved shadow |
| ~~`square-of-opposition.jpg`~~ | **Dropped on purpose.** The square of opposition is about contradiction among *all/none/some* statements — not about syllogisms, which is what Chapter Seven actually teaches. It is also not Aristotle's diagram (Apuleius, Boethius, then medieval scribes), and at margin width it is four Latin words and some lines. If Ch7 ever wants art: the Lyceum excavation site in Athens, or a page of the Aldine Greek Aristotle (Venice, 1495–98). |
| `galileo-dialogo-1632-frontispiece.jpg` | Frontispiece of Galileo's *Dialogo* (1632) — the three philosophers |
| `alexander-mosaic-pompeii.jpg` | The Alexander Mosaic, House of the Faun, Pompeii, c. 100 BC (Naples Archaeological Museum) — Alexander charging at Darius; full mosaic or the Alexander detail |

Attribution notes: the bust and mosaic photographs are museum photography of
public-domain objects — credit the photographer where Commons names one. The
lunar-eclipse composite is the one item likely to be a modern copyrighted
photograph; prefer a NASA/APOD public-domain image or a Commons CC file and
credit it.

Already embedded: Kepler's 1596 nested-solids engraving (`keplers-nested-solids.png`,
shared with the Tycho lesson — captioned honestly as Kepler's drawing of Plato's shapes).

## Not embedded (kept for reference only)

These files sit in this folder but are deliberately **not** used in any lesson:

- `lunar-eclipses.webp` — stock composite; the shadow edges do not run in one
  consistent direction, so it cannot carry the round-shadow claim
- `partial-lunar-eclipse.jpg` — signed, copyrighted astrophotograph, and half the
  frame is deliberately blown out (replaced by `partial-lunar-eclipse-nasa.jpg`)
- `pacioli-polyhedra.jpg` — labelled *Ycocedron Abscisus Vacuus*: the truncated
  icosahedron, an Archimedean solid, **not** one of Plato's five
- `Part-of-a-Roman-mosaic...webp` supersedes `roman-marine-mosaic.jpeg` (larger,
  and the filename carries the full findspot)
- `David_and_studio,_...The_Death_of_Socrates,_after_1787.jpg` — workshop version;
  replaced by `The_Death_of_Socrates.jpg`, the Metropolitan Museum original

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
