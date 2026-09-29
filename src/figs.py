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
    # Chapter indices are 0-based. With Socrates now at chapter one:
    #   0 Socrates · 1 Plato & the Academy · 2 Forms & solids · 3 The Cave
    #   4 Aristotle arrives · 5 Lesbos & the round Earth · 6 Logic · 7 The spell
    #   8 Alexander
    # Entries whose image file is not in ../media/ yet are skipped by attach()
    # with a printed warning — drop the file in, rebuild, and it appears.
    # Captions below are written for the canonical artifact; verify each one
    # against the file you actually pull before shipping (project rule #1).

    # ---- Chapter One · Socrates ----
    (0, dict(
        img="Socrates_Louvre.jpg",
        side="left", top=80,
        alt="Roman marble bust of Socrates, a copy after a lost Greek original",
        title="Socrates — a Roman copy of a lost Greek portrait",
        scroll=("No portrait made from life survives. This is a <b>Roman marble copy</b> "
                "of a Greek original carved generations after his death &mdash; a copy "
                "of a copy of a memory. Look at the face anyway: snub nose, wide flat "
                "features, heavy brow. Ancient writers teased him for looking like a "
                "satyr off a garden fountain, and the sculptors kept the joke instead of "
                "prettifying him. Even the portrait is an argument: the ugliest man in "
                "Athens was the one worth listening to."))),
    (0, dict(
        img="Athenian_Secret_Ballot.jpg",
        side="right", top=620,
        alt="Six bronze Athenian juror ballots, 4th century BC, Ancient Agora Museum",
        title="The actual ballots an Athenian jury used",
        scroll=("Bronze voting disks from the Athenian Agora, the same century as the "
                "trial. Each juror got <b>two</b>: one with a <b>hollow</b> axle "
                "(guilty) and one with a <b>solid</b> axle (not guilty). Find the disk "
                "at the lower left &mdash; you can see straight down the hole through "
                "the middle of it, and then compare the solid pegs on the others. You "
                "pinched the ends between thumb and finger so nobody could see which "
                "one you were dropping. The Greek scratched around the rims reads "
                "<i>PSEPHOS DEMOSIA</i> &mdash; &ldquo;public ballot.&rdquo; About 501 "
                "men held these on the day they voted on Socrates: roughly 280 hollow, "
                "221 solid, and a swing of 30 would have sent him home."))),
    (0, dict(
        img="The_Death_of_Socrates.jpg",
        side="left", top=1150,
        alt="Jacques-Louis David, The Death of Socrates, 1787",
        title="The Death of Socrates — David, 1787",
        scroll=("Painted in <b>1787</b> by Jacques-Louis David &mdash; twenty-one "
                "centuries after the event, so this is a painter's imagining, not a "
                "record. Socrates reaches for the poison cup without looking at it; his "
                "other hand is still in mid-argument. The man handing it over turns his "
                "face away. And that old man sitting at the foot of the bed is labelled "
                "Plato &mdash; who was 28 at the time and, by his own account, not even "
                "in the room. A masterpiece <i>and</i> not evidence. Check every "
                "caption."))),

    # ---- Chapter Two · Plato & the Academy ----
    (1, dict(
        img="Plato_Silanion_Musei_Capitolini_MC1377.jpg",
        side="right", top=70,
        alt="Roman marble bust of Plato, a copy after the Greek sculptor Silanion",
        title="Plato — Roman copy after Silanion",
        scroll=("A <b>Roman marble copy</b> after a lost bronze by Silanion, who is said "
                "to have made the original for the Academy itself, from life. If that is "
                "true, this heavy-browed face is roughly what his students saw at the "
                "front of the olive grove. The name on it is a nickname: ancient sources "
                "say his given name was Aristocles, and that <i>Plato</i> &mdash; "
                "&ldquo;broad&rdquo; &mdash; came from his wrestler's shoulders."))),
    (1, dict(
        img="plato's_academy_mosaic.jpg",
        side="left", top=520,
        alt="Roman mosaic of Plato's Academy from Pompeii, 1st century BC",
        title="Plato's Academy, in a Pompeii floor",
        scroll=("A mosaic pulled out of a villa at <b>Pompeii</b>, made in the first "
                "century BC &mdash; three hundred years after Plato, and buried by "
                "Vesuvius a century after it was laid. Seven men sit under a tree with a "
                "sundial and a walled city behind them, arguing over a globe on the "
                "ground. Nobody can prove which figure is meant to be Plato. What it does "
                "prove is stranger: three centuries on, a rich Roman wanted a picture of "
                "<i>people thinking</i> on his floor."))),

    # ---- Chapter Three · Forms & the five solids ----
    (2, dict(
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
    (2, dict(
        img="Leonardo davinci dodecahedron.jpg",
        side="left", top=520,
        alt="Nine of Leonardo da Vinci's polyhedron plates for Pacioli's De divina proportione",
        title="Leonardo's plates — now count carefully",
        scroll=("Nine plates from Luca Pacioli's <i>De divina proportione</i>, laid side "
                "by side. The designs are <b>Leonardo da Vinci's</b>, made around "
                "<b>1498</b> while he and Pacioli were living in the same household in "
                "Milan; these coloured versions come from the handwritten copies, and "
                "the printed edition of 1509 reduced them to plain black woodcuts. "
                "Leonardo invented something in order to draw these: the <b>skeletal "
                "solid</b>, all struts and holes, so you can see the back faces straight "
                "through the front. Nobody had drawn a solid that way before. Now read "
                "the Latin labels, because only <b>four of these nine</b> are Plato's "
                "shapes at all. <i>Duodecedron</i> is the twelve-pentagon dodecahedron "
                "and <i>Ycocedron</i> the twenty-triangle icosahedron &mdash; those "
                "count. The ones labelled <i>Vigintisex Basium</i> (twenty-six faces) "
                "and <i>Septuaginta Duarum Basium</i> (seventy-two) are something else "
                "entirely. Even a book about perfect shapes mixes them in with the rest. "
                "Check every label."))),

    # ---- Chapter Four · The Cave ----
    (3, dict(
        img="Platon_Cave_Sanraedam.jpg",
        side="right", top=70,
        alt="Jan Saenredam's 1604 engraving of Plato's allegory of the cave",
        title="The cave, engraved in 1604",
        scroll=("Engraved by <b>Jan Saenredam in 1604</b> after a design by Cornelis van "
                "Haarlem &mdash; the picture most people have in their heads when they "
                "hear &ldquo;Plato's cave,&rdquo; and it is Dutch, not Greek, and two "
                "thousand years late. Find the crowd staring at the lit wall, the figures "
                "casting the shapes, and the small bright opening with the world outside. "
                "An illustration of a thought experiment is itself a kind of shadow on a "
                "wall &mdash; a copy of something that only ever existed in a mind."))),

    # ---- Chapter Five · Aristotle arrives ----
    (4, dict(
        img="_The_School_of_Athens__by_Raffaello_Sanzio_da_Urbino.jpg",
        side="right", top=70,
        alt="Detail of Raphael's School of Athens: Plato pointing up, Aristotle palm down",
        title="Two hands, two roads to truth — Raphael, 1511",
        scroll=("Raphael's <i>School of Athens</i>, painted on a Vatican wall in "
                "<b>1511</b> &mdash; click it and go straight to the two men walking "
                "out of the archway at the centre. On the left, <b>Plato</b> points "
                "<b>up</b>, to the Forms, the perfect world behind this one, carrying "
                "his <i>Timaeus</i>. On the right, <b>Aristotle</b> holds his palm "
                "<b>down</b> toward the ground: <i>here</i>, look at <i>this</i>, and "
                "his book is the <i>Ethics</i>. Everyone else in that crowded hall is "
                "arguing about something. Those two are arguing about where to look."))),
    (4, dict(
        img="Aristotle_Bust.jpg",
        side="left", top=520,
        alt="Roman marble bust of Aristotle at Palazzo Altemps, with a modern alabaster mantle",
        title="Aristotle — ancient head, modern robe",
        scroll=("Palazzo Altemps in Rome, inventory 8575: a <b>Roman marble copy</b> of "
                "a lost Greek bronze credited to Lysippos &mdash; the same sculptor "
                "Alexander the Great used for his own portraits, which is a small clue "
                "about how close the tutor and the pupil stayed. Now look where the "
                "white stops. The head is ancient; that <b>golden-brown alabaster robe "
                "is modern</b>, added centuries later by a restorer who wanted a tidy "
                "bust. Half of what you are looking at is a guess. Check every "
                "caption &mdash; including the ones carved in stone."))),

    # ---- Chapter Six · Lesbos & the round Earth ----
    (5, dict(
        img="Part-of-a-Roman-mosaic-from-Pompeii-house-n-16-insula-2-Regio-VIII-first-century-CE.webp",
        side="right", top=70,
        alt="Roman marine-life mosaic from Pompeii, first century AD, with octopus, lobster and moray eel",
        title="The lagoon, in Roman tile",
        scroll=("A floor mosaic from a house in <b>Pompeii</b>, first century AD, buried "
                "by Vesuvius. Count what the tile-setter knew: an <b>octopus</b> in the "
                "middle with a spiny lobster locked in its arms, a <b>moray eel</b> "
                "twisting in from the right, a squid, a ray, a sea bass, red mullet, "
                "sea bream. It is nearly a checklist of the animals Aristotle hauled out "
                "of the water at Lesbos three hundred years earlier and described so "
                "exactly that modern zoologists can still put names to his species. He "
                "is the reason the octopus in this picture has a name at all &mdash; and "
                "he is the one who noticed it changes colour to vanish against the "
                "rocks."))),
    (5, dict(
        img="partial-lunar-eclipse-nasa.jpg",
        side="left", top=520,
        alt="Four frames of a lunar eclipse showing Earth's round shadow advancing across the Moon",
        title="Aristotle's proof, photographed",
        scroll=("One eclipse, four moments. That dark edge creeping across the Moon is "
                "the <b>shadow of the Earth</b> &mdash; and look at it: a clean, smooth "
                "<b>curve</b>, the same curve in every frame, advancing steadily from "
                "one side. It is the same curve in every eclipse, at every hour of the "
                "night, from every place on Earth, year after year. Only a ball manages "
                "that. A flat disc would throw an oval as it tilted, and a thin line "
                "when it turned edge-on. Aristotle worked this out around 350 BC with no "
                "camera and no telescope &mdash; he simply kept watching, and noticed "
                "that the shadow never changed its mind. (And the red in the last frame? "
                "That is sunlight bent around the edge of the Earth and through our air: "
                "every sunrise and every sunset happening at that moment, all of them at "
                "once, falling on the Moon.)"))),

    # ---- Chapter Seven · The logic machine ----
    (6, dict(
        img="square-of-opposition.jpg",
        side="right", top=70,
        alt="Medieval manuscript diagram of the square of opposition",
        title="The machine, drawn as a diagram",
        scroll=("Aristotle's logic, drawn by medieval scribes as the <b>square of "
                "opposition</b>: <i>all are</i>, <i>none are</i>, <i>some are</i>, "
                "<i>some are not</i>, wired corner to corner by which statements can be "
                "true together and which cannot. It is a circuit diagram &mdash; drawn "
                "with a quill, a thousand years before electricity, for a machine made "
                "entirely of words."))),

    # ---- Chapter Eight · The spell of authority ----
    (7, dict(
        img="Galileos_Dialogue.png",
        side="right", top=70,
        alt="Frontispiece of Galileo's Dialogue Concerning the Two Chief World Systems, 1632",
        title="The spell breaking — Galileo's Dialogo, 1632",
        scroll=("The frontispiece of Galileo's <i>Dialogo</i>, printed in <b>1632</b>: "
                "three men in conversation, labelled <b>Aristotle</b>, <b>Ptolemy</b> and "
                "<b>Copernicus</b> &mdash; two of them dead for eighteen centuries, "
                "arguing anyway. That is the whole trick of the book, and of this chapter: "
                "the greatest minds get invited into the room and then <i>questioned</i>, "
                "not obeyed. It cost Galileo the rest of his freedom."))),

    # ---- Chapter Nine · Alexander ----
    (8, dict(
        img="alexander-mosaic-pompeii.jpg",
        side="right", top=70,
        alt="The Alexander Mosaic from the House of the Faun, Pompeii: Alexander on horseback charging at Darius",
        title="Alexander at the charge — a Roman floor, about 100 BC",
        scroll=("The <b>Alexander Mosaic</b>, laid into a floor of the House of the Faun "
                "at Pompeii around <b>100 BC</b> and buried by Vesuvius in AD 79 &mdash; "
                "more than a million tiny stones, thought to copy a lost Greek painting "
                "made within living memory of the battle. Alexander is the bare-headed "
                "rider on the left, driving straight at the Persian king Darius, who "
                "turns in his chariot on the right. Click it and look at Alexander's "
                "eye: whoever painted the original had been told it was large and "
                "unsettling, and did not soften it. The pupil of Aristotle, portrayed "
                "the way his teacher would have wanted: as he actually looked."))),
]

GALILEO_FIGS = []  # margin art pending — see media/README.md wish list

SUN_MOON_FIGS = []  # margin art pending — see media/README.md wish list

PYTHAGORAS_FIGS = [
    # ---- Chapter One · the man behind the curtain ----
    (0, dict(
        img="Pythagoras_Bust_Capitoline.jpg",
        side="left", top=80,
        alt="Roman marble bust of a bearded man in a wrapped headcloth, labelled as Pythagoras, Capitoline Museums",
        title="&ldquo;Pythagoras&rdquo;, carved centuries too late",
        scroll=("A marble bust in the Capitoline Museums in Rome, traditionally called "
                "<b>Pythagoras</b> because of the wrapped headcloth that ancient artists gave "
                "him. Now do the arithmetic: it is a <b>Roman</b> carving, made some six "
                "hundred years after he died, by a sculptor who had never seen him and had no "
                "portrait to work from. Nobody knows what Pythagoras looked like. What you are "
                "looking at is what later centuries thought a wise man <i>ought</i> to look "
                "like: a portrait of a reputation."))),
    # ---- Chapter Two · all is number ----
    (1, dict(
        img="Pythagoras_School_of_Athens_detail.jpg",
        side="left", top=70,
        alt="Detail of Raphael's School of Athens: a man writing in a large book while a boy holds up a slate with a diagram",
        title="Raphael's Pythagoras, and the slate at his feet",
        scroll=("A corner of Raphael's <i>School of Athens</i>, painted on a Vatican wall in "
                "<b>1511</b>. The man writing in the big book has been identified as "
                "Pythagoras for centuries, and the reason is the <b>slate</b> the boy is "
                "holding up. Click to enlarge and look at it: the looping curves at the "
                "top tie together the numbers of the musical intervals, and underneath sits "
                "a small triangle of strokes (one, two, three, four) with an "
                "<b>X</b>, the Roman ten, below it. That is the <b>tetractys</b>. Raphael painted this two "
                "thousand years after the man died. It is a picture of the ideas, not the face."))),
    (1, dict(
        img="Gaffurio_Theorica_musicae_1492.png",
        side="right", top=520,
        alt="Woodcut in four panels: smiths hammering at a forge, and a robed man testing bells, water glasses, weighted strings and pipes, all marked with numbers",
        title="The hammer story, printed in 1492",
        scroll=("A woodcut from Franchino Gaffurio's <i>Theorica musicae</i>, printed in Milan "
                "in <b>1492</b>. Read the labels. Three panels say <b>PYTAGORA</b> or "
                "<b>PITAGORAS</b>: he strikes bells, taps glasses of water, plucks strings "
                "stretched by weights, and tries pipes with a partner labelled "
                "<b>PHYLOLAUS</b>. Everything carries the same numbers: 4, 6, 8, 9, 12, "
                "16. But the forge, top left, is labelled <b>IUBAL</b>: Jubal, the Bible's "
                "first musician. By 1492 the hammer story had been told so often that it had "
                "two heroes. And here is the catch: apart from the pipes, <b>none of these "
                "experiments works</b> as drawn. Weights in those ratios do not tune strings "
                "to those notes. For two thousand years it was easier to copy the picture "
                "than to pick up a hammer."))),
    (1, dict(
        img="Caravaggio_Lute_Player_Hermitage.jpg",
        side="left", top=1000,
        alt="Painting of a young musician in a white shirt playing a lute, with a violin, music books, fruit and flowers on the table",
        title="A lute in Italy, painted about 1596",
        scroll=("<i>The Lute Player</i>, painted by <b>Caravaggio</b> in Rome around "
                "<b>1596</b> and now in the Hermitage Museum in St Petersburg. This is the "
                "instrument Vincenzo Galilei played and wrote books about. Look at how the "
                "head of the lute bends sharply backwards, with a row of pegs down each "
                "side. The strings run in pairs, and each pair is tuned by stretching it "
                "tighter or looser with its peg. That is why a lute player was the right "
                "person to ask how much pull it takes to raise a string by an octave: he "
                "did it by hand every time he tuned up."))),
    # ---- Chapter Four · a thousand years too early ----
    (3, dict(
        img="Plimpton_322.jpg",
        side="right", top=70,
        alt="The clay tablet Plimpton 322, covered in rows and columns of cuneiform numbers, with a corner broken away",
        title="Plimpton 322, Babylon, about 1800 BC",
        scroll=("<b>Plimpton 322</b>, now at Columbia University in New York: clay, about 13 "
                "centimeters wide, written around <b>1800 BC</b>. The scribe ruled it into "
                "columns with a straight edge (you can still see the lines) and "
                "filled fifteen rows with numbers in base 60, pressed in with the corner of a "
                "reed. The left edge is broken off, and traces of glue suggest the missing "
                "piece was lost in modern times. Scholars still argue about what it was "
                "<i>for</i>. One strong suggestion: a teacher's list, for setting "
                "right-triangle problems that were certain to come out in whole numbers."))),
    (3, dict(
        img="YBC_7289_obverse.jpg",
        side="left", top=470,
        alt="A small round clay tablet showing a square with both diagonals drawn and cuneiform numbers written along them",
        title="A student's tablet: the diagonal of a square",
        scroll=("<b>YBC 7289</b>, in the Yale Babylonian Collection, about 8 centimeters "
                "across, small enough to sit in a palm, and round like the practice tablets "
                "Babylonian students used. The square is drawn tilted, standing on one corner, "
                "with both diagonals. Near the top-left edge are three wedges: <b>30</b>, the "
                "length of the side. Along the level diagonal run the numbers <b>1, 24, 51, "
                "10</b>, the square root of 2 in base 60, and beneath them "
                "<b>42, 25, 35</b>: the diagonal itself, 30 times as long. A value that "
                "good was not worked out on the spot: it was copied from a table, the way "
                "you might look a number up today."))),
    # ---- Chapter Six · the bowstring diagram ----
    (5, dict(
        img="Zhoubi_Suanjing_xian_tu.jpg",
        side="right", top=70,
        alt="Chinese woodblock print: a tilted square inside a seven by seven grid, divided into four triangles around a small central square, with a line of Chinese characters beside it",
        title="The bowstring diagram, from the Zhoubi Suanjing",
        scroll=("The <i>xian tu</i> as printed in a later edition of the <i>Zhoubi "
                "Suanjing</i>. Count the grid: it is <b>7 by 7</b>, and the tilted square "
                "inside it is the square on the hypotenuse of a 3-4-5 triangle. The column "
                "of writing on the left reads, roughly: <i>&ldquo;the squares on gou and gu, "
                "joined together, make the square on xian.&rdquo;</i> The labels inside "
                "follow Zhao Shuang's instructions: &#26417; (<i>zhu</i>, red) on the "
                "triangles, &#40643; (<i>huang</i>, yellow) on the little square in the "
                "middle. Look closely and you will find <b>both</b> of this lesson's picture "
                "proofs in the one drawing."))),
    # ---- Chapter Seven · Euclid's windmill ----
    (6, dict(
        img="Euclid_Vat_gr_190_I_47.jpg",
        side="left", top=70,
        alt="Two facing pages of a Greek manuscript, with the windmill diagram of a triangle and three squares drawn in the middle of the right-hand page",
        title="Proposition 47, copied by hand about 1,100 years ago",
        scroll=("Two pages of <b>Vatican manuscript Greek 190</b>, written out by hand in "
                "the 800s or 900s AD, one of the oldest complete copies of Euclid's "
                "<i>Elements</i> on Earth. Find the <b>windmill</b> in the middle of the "
                "right-hand page. Then look in the margins and along the bottom: later "
                "readers, over centuries, squeezed in their own notes and their own little "
                "diagrams. Nothing in Euclid's handwriting survives; this copy was made more "
                "than a thousand years after he died. The proof survived by being copied, "
                "scribe after scribe, and because any reader, at any time, could check "
                "every step without taking anybody's word for it."))),
    # ---- Chapter Eight · the congressman and the schoolboy ----
    (7, dict(
        img="James_Garfield_Brady-Handy.jpg",
        side="right", top=70,
        alt="Photograph of James A. Garfield, a bearded man in a dark coat",
        title="James A. Garfield: teacher, general, President",
        scroll=("<b>James A. Garfield</b>, in a portrait from the Brady-Handy collection "
                "at the Library of Congress. Born in a log cabin in Ohio in 1831, he worked his way through "
                "school, taught Greek and Latin, and was running a college at twenty-six. His "
                "trapezoid proof was printed on <b>April 1, 1876</b>, while he sat in "
                "Congress. He became President in March 1881, was shot by an assassin that "
                "July, and died in September, two hundred days after taking office. The "
                "proof has lasted rather longer."))),
    (7, dict(
        img="Einstein_about_age_14.jpg",
        side="left", top=520,
        alt="Studio photograph of Albert Einstein as a boy of about fourteen, seated in front of a painted backdrop",
        title="Albert Einstein at about fourteen",
        scroll=("<b>Albert Einstein</b> at about fourteen, in a studio photograph taken "
                "around 1893. The lake, the hills and the little sailing boat behind "
                "him are a painted backdrop. This is roughly two years after he fought his "
                "way to a proof of the theorem. He later wrote that at twelve he was given a "
                "small geometry book and was astonished that statements could be proved "
                "<i>&ldquo;with such certainty that any doubt appeared to be out of the "
                "question.&rdquo;</i> He called it his &ldquo;holy geometry booklet.&rdquo;"))),
]

FIGS = {
    "PYTHAGORAS": PYTHAGORAS_FIGS,
    "NEWTON": NEWTON_FIGS,
    "PLATO_ARISTOTLE": PLATO_ARISTOTLE_FIGS,
    "GALILEO": GALILEO_FIGS,
    "SUN_MOON": SUN_MOON_FIGS,
    "ERATOSTHENES": ERATOSTHENES_FIGS,
    "ECLIPSE_1919": ECLIPSE_FIGS,
    "LE_GENTIL": LE_GENTIL_FIGS,
    "PIGEON": PIGEON_FIGS,
    "LEAVITT": LEAVITT_FIGS,
}

def attach(story, key, media_dir=None):
    """Attach margin figures to a story dict (idempotent).

    If media_dir is given, figures whose image file is not present are skipped
    with a warning — so a planned figure can sit in this file waiting for its
    artwork, and start appearing the moment the file lands in media/.
    """
    import os as _os
    for ch_i, fig in FIGS[key]:
        if media_dir and not _os.path.exists(_os.path.join(media_dir, fig["img"])):
            print("  ..skipping %s ch%d: media/%s not found yet" % (key, ch_i, fig["img"]))
            continue
        figs = story["chapters"][ch_i].setdefault("figs", [])
        if fig not in figs:
            figs.append(fig)
