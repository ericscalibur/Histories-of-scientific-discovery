"""Margin figures for the generated lessons.

Each entry: story key -> list of (chapter_index, fig) where fig is
{img, side, top, alt, title, scroll}. Images live in ../media/.
Captions are verified against the artwork itself — see media/README.md.
"""

NEWTON_FIGS = [
    (0, dict(
        img="Portrait_of_Sir_Isaac_Newton,_1689_(brightened).jpg",
        side="left", top=80,
        alt="Portrait of Isaac Newton at age 46, painted by Godfrey Kneller in 1689",
        title="Isaac Newton in 1689, by Godfrey Kneller",
        scroll=("Isaac Newton at 46, painted by Godfrey Kneller in 1689 &mdash; two years "
                "after the <i>Principia</i> made him famous. Many consider it the truest "
                "portrait of him ever made. That's his own shoulder-length hair, already "
                "silver &mdash; not a wig. Look at the eyes: people who met him said he "
                "seemed to be listening to something no one else could hear."))),
    (1, dict(
        img="Newtons-sketch.jpg",
        side="right", top=70,
        alt="Newton's own sketch of sunlight split by prisms",
        title="Newton's own sketch of his prism experiment",
        scroll=("Newton's own drawing of his famous experiment: sunlight enters through a "
                "hole in the window shutter, passes through a prism, and fans out into "
                "colors. Then &mdash; the clever part &mdash; a <b>second</b> prism catches "
                "just one color and bends it again. The note in his handwriting says "
                "<i>Nec variat lux fracta colorem</i> &mdash; &ldquo;refracted light does "
                "not change its color.&rdquo; Once split, blue stays blue. White light was "
                "never pure &mdash; it was all the colors, hiding together."))),
    (2, dict(
        img="newtons_apple_tree_at_woolsthorpe_manor_arthurmarris.jpg",
        side="left", top=70,
        alt="The surviving apple tree at Woolsthorpe Manor",
        title="THE apple tree, still alive at Woolsthorpe",
        scroll=("This is not a descendant. This is <b>the tree</b> &mdash; a cooking-apple "
                "variety called Flower of Kent, growing at Woolsthorpe Manor since before "
                "Newton was born. A storm knocked it flat around 1820; instead of dying it "
                "re-rooted itself and kept growing sideways, which is why it looks so "
                "strange. It still makes apples. You can visit it &mdash; scientists' "
                "pilgrimage to this tree has been going on for two centuries."))),
    (5, dict(
        img="Newton's_Principia_title_page.png",
        side="right", top=70,
        alt="Title page of the first edition of Newton's Principia, 1687",
        title="Title page of the Principia, 1687",
        scroll=("The title page of the first edition, 1687: <i>Philosophi&aelig; Naturalis "
                "Principia Mathematica</i> &mdash; &ldquo;Mathematical Principles of Natural "
                "Philosophy.&rdquo; Read the fine print near the top: <b>IMPRIMATUR, "
                "S. PEPYS</b> &mdash; the printing license, signed by Samuel Pepys, president "
                "of the Royal Society (and history's most famous diary-keeper). The Society "
                "had no money to print it, so Edmond Halley &mdash; the comet Halley &mdash; "
                "paid for it out of his own pocket."))),
    (5, dict(
        img="reflecting-telescope.jpg",
        side="left", top=420,
        alt="Newton's reflecting telescope, preserved at the Royal Society",
        title="Newton's little reflecting telescope",
        scroll=("The little telescope that first made Newton famous &mdash; preserved at the "
                "Royal Society in London. Every telescope before it used lenses, which smear "
                "starlight into rainbow fringes (Newton's prism work told him why). So he "
                "built one around a curved <b>mirror</b> instead &mdash; grinding and "
                "polishing the metal mirror with his own hands. It was six inches long and "
                "magnified 40 times. When the Royal Society saw this design in 1672, they "
                "elected him a Fellow within weeks. Nearly every great telescope today "
                "&mdash; including the ones in space &mdash; is a reflector, his idea."))),
]

ERATOSTHENES_FIGS = [
    (0, dict(
        img="Rhind_Mathematical_Papyrus.jpg",
        side="right", top=70,
        alt="The Rhind Mathematical Papyrus, an ancient Egyptian math scroll",
        title="An Egyptian math scroll, ~1550 BC",
        scroll=("A real Egyptian math scroll &mdash; the Rhind Mathematical Papyrus, copied "
                "out around 1550 BC by a scribe named Ahmes, from a text older still. It "
                "opens with a boast: <i>&ldquo;Accurate reckoning: the entrance into "
                "knowledge of all existing things and all obscure secrets.&rdquo;</i> Inside "
                "are 84 worked problems &mdash; fractions, triangles, the slope of a pyramid. "
                "Math like this was already <b>thirteen centuries old</b> when Eratosthenes "
                "ran the Library of Alexandria. It lives in the British Museum today."))),
    (2, dict(
        img="Obelisk_Hatschepsut.JPG",
        side="left", top=70,
        alt="The obelisk of Hatshepsut standing at Karnak",
        title="Hatshepsut's obelisk at Karnak &mdash; a giant gnomon",
        scroll=("The obelisk of Pharaoh Hatshepsut at Karnak &mdash; a <b>single piece</b> of "
                "pink granite nearly 30 meters tall, raised around 1457 BC and still standing. "
                "To Egyptians it honored the Sun god. To a geometer it is something else: a "
                "perfect <b>gnomon</b> &mdash; a shadow-caster. A stick works just as well, "
                "but an obelisk makes the point beautifully: plant something straight up, "
                "watch its shadow, and the sky becomes an instrument you can read."))),
    (3, dict(
        img="Description de l'Égypte Syène.jpg",
        side="right", top=70,
        alt="Engraving of the Nile at Syene from the Description de l'Egypte",
        title="Syene on the Nile, drawn 1799",
        scroll=("Syene itself &mdash; today's Aswan &mdash; where the famous well was. This "
                "engraving was made for the <i>Description de l'&Eacute;gypte</i>, the giant "
                "survey Napoleon's 160 scholars made of Egypt starting in 1798. They drew it "
                "some <b>two thousand years after Eratosthenes</b>, and the Nile, the rocks, "
                "and the fierce noon Sun were exactly where he'd left them. On the solstice, "
                "sunlight still drops straight down the wells here at midday."))),
]

ECLIPSE_FIGS = [
    (3, dict(
        img="1919eclipse.jpg",
        side="left", top=70,
        alt="Photograph of the May 29, 1919 total solar eclipse with measured star positions marked",
        title="An actual 1919 eclipse photograph",
        scroll=("One of the actual photographs from May 29, 1919 &mdash; taken with the "
                "expedition's instruments in Sobral, Brazil, and re-scanned from the original "
                "a century later. The short horizontal dashes are the important part: they "
                "flag the <b>stars</b> whose positions were measured against where those same "
                "stars sit in the night sky. The differences came out to about two thousandths "
                "of a millimeter on the plate. That smudge of measurement is what made "
                "Einstein famous."))),
    (4, dict(
        img="november-7th-1919-on-7-einstein.webp",
        side="right", top=70,
        alt="The Times of London, November 7, 1919: Revolution in Science",
        title="The Times, November 7, 1919",
        scroll=("<i>The Times</i> of London, November 7, 1919 &mdash; the morning after the "
                "results were announced: <b>&ldquo;REVOLUTION IN SCIENCE &mdash; NEW THEORY OF "
                "THE UNIVERSE &mdash; NEWTONIAN IDEAS OVERTHROWN.&rdquo;</b> Einstein went to "
                "bed a physicist and woke up the most famous scientist on Earth. Note what "
                "made the revolution: not an argument, not an opinion &mdash; a "
                "<b>measurement</b>, checked against a prediction written down four years "
                "before."))),
    (4, dict(
        img="einstein-eddington.jpg",
        side="left", top=380,
        alt="Einstein and Eddington sitting together in Cambridge, 1930",
        title="Einstein &amp; Eddington, Cambridge 1930",
        scroll=("The two men of this story, photographed together in Cambridge in 1930 "
                "&mdash; eleven years after the eclipse. Einstein made the prediction; "
                "Eddington sailed to the island of Pr&iacute;ncipe to test it. They were "
                "citizens of countries that had just spent four years at war with each "
                "other. Science, Eddington insisted, belongs to no flag: a German's theory "
                "was worth an Englishman's voyage to check."))),
]

LE_GENTIL_FIGS = [
    (4, dict(
        img="Fort_Venus.jpg",
        side="right", top=70,
        alt="1773 engraving of Fort Venus, the Endeavour expedition's transit observatory in Tahiti",
        title="Fort Venus, Tahiti &mdash; a fortress built for a telescope",
        scroll=("&ldquo;Venus Fort, Erected by the Endeavour's People, to secure themselves "
                "during the Observation of the Transit of Venus, at Otaheite&rdquo; &mdash; "
                "the caption engraved on this plate, published in 1773 in the official "
                "account of Cook's voyage, from a drawing made on the spot by the ship's "
                "artist. Look at it: walls, tents, a flag, guards &mdash; a <b>fortress "
                "built to protect a telescope</b>. That is how much one measurement "
                "mattered to the world in 1769."))),
    (4, dict(
        img="black-drop-effect.png",
        side="left", top=400,
        alt="Cook's and Green's 1769 drawings of the black drop effect during the transit of Venus",
        title="The 'black drop' &mdash; drawn by Cook himself",
        scroll=("The villain of the whole expedition, drawn by Captain Cook and his "
                "astronomer Charles Green as they watched: the <b>black drop effect</b>. "
                "Just when Venus should have separated cleanly from the Sun's edge, it "
                "seemed to stretch toward it like a drop of tar. Cook and Green, side by "
                "side with identical telescopes, recorded times differing by many seconds "
                "&mdash; and the whole method depended on timing that exact moment. They "
                "had sailed across the world to time something that refused to be timed."))),
]

PIGEON_FIGS = [
    (0, dict(
        img="Horn_Antenna-in_Holmdel,_New_Jersey_-_restoration1.jpg",
        side="right", top=70,
        alt="The 15-meter horn antenna at Holmdel, New Jersey",
        title="The horn antenna at Holmdel, New Jersey",
        scroll=("The instrument that heard the beginning of time: a 15-meter horn-reflector "
                "antenna at Bell Labs in Holmdel, New Jersey &mdash; built in 1959 not for "
                "astronomy at all, but to catch radio signals bounced off early satellites. "
                "That's the two astronomers on it in this NASA photo. The horn shape scoops "
                "up radio waves from one precise patch of sky and shields out everything "
                "else &mdash; which is exactly why a faint hiss coming from <b>every</b> "
                "direction refused to make sense."))),
    (2, dict(
        img="pigeon-trap.jpg",
        side="left", top=70,
        alt="The pigeon trap used at the Holmdel horn antenna, now in the Smithsonian",
        title="The actual pigeon trap &mdash; now in the Smithsonian",
        scroll=("Yes, this is the <b>actual pigeon trap</b>. Penzias and Wilson used it to "
                "catch the two pigeons roosting inside the horn &mdash; the prime suspects "
                "for the mystery noise, since they had coated the antenna's throat with "
                "what the scientists politely called &ldquo;white dielectric material.&rdquo; "
                "The pigeons were caught, the antenna was scrubbed&hellip; and the hiss "
                "stayed. Today the trap sits in the Smithsonian &mdash; a monument to "
                "checking <i>every</i> explanation, even the ridiculous ones."))),
    (3, dict(
        img="penzias-wilson.jpg",
        side="right", top=70,
        alt="Arno Penzias and Robert Wilson standing before the Holmdel horn antenna",
        title="Penzias &amp; Wilson at the horn",
        scroll=("Arno Penzias and Robert Wilson in front of their horn antenna. Neither of "
                "them was looking for the origin of the universe &mdash; they were radio "
                "astronomers trying to get a clean, quiet instrument. Their superpower was "
                "stubbornness: they refused to ignore a tiny, boring, persistent error "
                "that wouldn't go away. The pigeon poop got scrubbed; the hiss survived "
                "every test; and one phone call to Princeton turned an annoyance into "
                "a Nobel Prize."))),
    (4, dict(
        img="Cosmic_Microwave_Background_(CMB).jpeg",
        side="left", top=70,
        alt="The Planck satellite's all-sky map of the cosmic microwave background",
        title="The baby picture of the universe",
        scroll=("What Penzias and Wilson heard as a hiss, drawn as a picture: the <b>cosmic "
                "microwave background</b> across the entire sky, mapped by the Planck "
                "satellite (2013). This is the oldest light there is &mdash; released when "
                "the universe was 380,000 years old. The speckles are temperature ripples "
                "of a few <i>hundred-thousandths</i> of a degree; those tiny lumps grew up "
                "to become galaxies, including ours. Their hiss turned out to be the "
                "universe's baby picture."))),
]

LEAVITT_FIGS = [
    (0, dict(
        img="Henrietta_Swan_Leavitt.jpg",
        side="left", top=70,
        alt="Photograph of Henrietta Swan Leavitt",
        title="Henrietta Swan Leavitt",
        scroll=("Henrietta Swan Leavitt (1868&ndash;1921). After college an illness took "
                "most of her hearing; colleagues remembered her as quiet, precise, and "
                "impossible to distract. Harvard paid her about <b>30 cents an hour</b> "
                "to measure the brightness of stars on glass photographs &mdash; work "
                "considered too tedious for the male astronomers. With it, she found "
                "the yardstick that measures the universe."))),
    (1, dict(
        img="Computers harvard women.jpg",
        side="right", top=70,
        alt="The Harvard computers at work in the observatory workroom, about 1891",
        title="The Harvard 'computers' at work, ~1891",
        scroll=("Before the word meant a machine, a <b>computer was a person</b> &mdash; "
                "and at Harvard, the computers were women. Here they are around 1891: "
                "magnifiers over glass plates, ledgers filling with numbers. Williamina "
                "Fleming &mdash; standing &mdash; began as the observatory director's maid "
                "and ended up classifying ten thousand stars. Look at the wall: that framed "
                "zig-zag is a chart of a star's changing brightness, dated December 1889. "
                "They decorated with data."))),
    (1, dict(
        img="glassplate.webp",
        side="left", top=380,
        alt="An astronomical glass photographic plate showing the Andromeda nebula",
        title="A glass universe: photographic plate of Andromeda",
        scroll=("The sky, caught on glass: an astronomical photographic plate of the "
                "Andromeda nebula. Each black speck is a star (plates record light as "
                "dark); the whirlpool in the middle is Andromeda itself. Plates like "
                "these were the hard drives of the 1900s &mdash; Harvard collected half "
                "a million. And Andromeda is the perfect one to show here: a few years "
                "after Leavitt died, Edwin Hubble found one of her variable stars on a "
                "plate of this very nebula, used her yardstick&hellip; and proved it "
                "was another <b>galaxy</b>."))),
    (2, dict(
        img="luminosity-plot-pickering.webp",
        side="right", top=70,
        alt="Page 3 of Harvard Circular 173 (1912) with Leavitt's period-luminosity figures",
        title="The discovery itself &mdash; published March 3, 1912",
        scroll=("The discovery, exactly as the world first saw it: page 3 of Harvard "
                "Circular 173, dated March 3, 1912. Those two little graphs are Leavitt's "
                "period&ndash;luminosity law &mdash; the longer a Cepheid star takes to "
                "pulse, the brighter it truly is. Now read the signature at the bottom: "
                "<b>&ldquo;EDWARD C. PICKERING.&rdquo;</b> Her discovery, her figures, her "
                "years of measuring &mdash; published under the observatory director's "
                "name, as was the custom for women's work in 1912. Check every caption; "
                "ask who really did the work."))),
]

PLATO_ARISTOTLE_FIGS = [
    (1, dict(
        img="keplers-nested-solids.png",
        side="right", top=70,
        alt="Kepler's 1596 model of the solar system built from the five Platonic solids",
        title="Plato's five solids, still casting spells in 1596",
        scroll=("The five Platonic solids &mdash; drawn not by Plato, but by <b>Johannes "
                "Kepler in 1596</b>, two thousand years later. Kepler was so enchanted by "
                "Plato's perfect shapes that he tried to build the entire solar system out "
                "of them, nesting the five solids between the orbits of the six known "
                "planets like Russian dolls. The model was beautiful &mdash; and wrong &mdash; "
                "and discovering <i>exactly how</i> it was wrong drove Kepler to the true "
                "laws of the planets. That is the reach of an idea born in an Athenian "
                "olive grove."))),
]

GALILEO_FIGS = []  # margin art pending — see media/README.md wish list

FIGS = {
    "NEWTON": NEWTON_FIGS,
    "PLATO_ARISTOTLE": PLATO_ARISTOTLE_FIGS,
    "GALILEO": GALILEO_FIGS,
    "ERATOSTHENES": ERATOSTHENES_FIGS,
    "ECLIPSE_1919": ECLIPSE_FIGS,
    "LE_GENTIL": LE_GENTIL_FIGS,
    "PIGEON": PIGEON_FIGS,
    "LEAVITT": LEAVITT_FIGS,
}

def attach(story, key):
    """Attach margin figures to a story dict (idempotent)."""
    for ch_i, fig in FIGS[key]:
        figs = story["chapters"][ch_i].setdefault("figs", [])
        if fig not in figs:
            figs.append(fig)
