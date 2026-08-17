# -*- coding: utf-8 -*-
"""Story data: Eratosthenes, 1919 Eclipse, Le Gentil."""

ERATOSTHENES = dict(
    title="The Man Who Measured the World — Eratosthenes",
    h1="✦ The Man Who Measured the World ✦",
    sub="How Eratosthenes measured the entire Earth with a stick, a shadow, and a very long walk — 2,200 years ago",
    footer="Companion lesson to the Constellation Plotting Worksheets · Alexandria, ~240 BC<br>(the step-counters were real)",
    praise=["Perfectly measured, {name}!", "The Library would hire you on the spot, {name}!",
            "Exactly right, geometer!", "Sharp as a noonday shadow!",
            "Even \"Beta\" never counted better, {name}!"],
    cert_org="The Great Library of Alexandria",
    cert_of="the tale of Eratosthenes",
    cert_rank="Chief Surveyor of the Round Earth",
    finale_title="A Stick, a Shadow, and the Whole World",
    finale_html="""
<p>Think about what just happened in this story. No telescope — not invented for another 1,850 years. No satellites, no lasers, no computers. One curious librarian measured <b>the entire planet</b> using a shadow, an angle, and a well-counted walk — and got within a couple of percent of the answer we use today. When astronauts finally saw the round Earth from space in the 20th century, they were looking at something a librarian had already measured with a stick.</p>
<p>Eratosthenes went on to invent the word <i>geography</i>, draw some of the best maps of the ancient world, and build a famous trick for finding prime numbers (the "Sieve of Eratosthenes" — your math teacher still uses it). Not bad for a man whose nickname meant "second place."</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① You can measure something enormous by measuring something small — <b>if you pick the right small thing</b>.</p>
<p>② The same sunbeam, hitting two cities differently, proves the Earth is curved — evidence you can check with two sticks.</p>
<p>③ Simple tools plus a clever question beat fancy tools with no question. Every time.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Alexandria, Egypt · about 240 BC",
            title="Mr. Second Place",
            html="""
<p>Two thousand two hundred years ago, the greatest building in the world wasn't a palace or a temple. It was a <b>library</b>. The Great Library of Alexandria tried to collect a copy of every scroll ever written — hundreds of thousands of them. Ships docking in the harbor were searched, not for treasure, but for <i>books</i>, which were borrowed and copied before being returned.</p>
<p>The man in charge of all of it was <b>Eratosthenes</b>. He studied everything: poetry, history, math, maps, the stars. His friends teasingly nicknamed him <b>"Beta"</b> — the second letter of the Greek alphabet — because they said he was the <i>second-best</i> in the world at everything, champion of nothing. The nickname was supposed to be an insult.</p>
<p>Keep that nickname in mind. Because the man who was "second-best at everything" was about to do something nobody — no specialist, no champion — had ever done: measure the size of the entire Earth without leaving Egypt.</p>
<div class="funfact">📜 Educated Greeks already knew the Earth was round — they saw its curved shadow on the Moon during eclipses, and watched ships disappear bottom-first over the horizon. But <b>nobody knew how big it was</b>. It could have been cozy, or endless. Nobody knew.</div>""",
            cps=[dict(
                type="num",
                kicker="Welcome to the Library",
                q="""Nobody knows exactly how many scrolls the Library held, so let's suppose it was <b>400,000</b>, stored equally in <b>40,000-scroll halls</b>. How many halls would that take?""",
                answers=[10], unit="halls",
                hint="How many times does 40,000 fit into 400,000? Try covering up matching zeros.",
            )],
        ),
        dict(
            kicker="Chapter Two · A traveler's tale",
            title="The Well with No Shadow",
            html="""
<p>One day a traveler told Eratosthenes something odd about the city of <b>Syene</b>, far to the south (today it's called Aswan). On one special day each year — the longest day of summer, at exactly noon — the sun shone <b>straight down to the bottom of the deepest wells</b>. Columns cast no shadow at all. The sun stood perfectly overhead.</p>
<p>Most people would say "huh, neat" and move on. Eratosthenes froze. Because he knew for a fact that in Alexandria, on that <i>same day</i> at that <i>same noon</i>, sticks and columns <b>do</b> cast a shadow. Short — but definitely there.</p>
<p>Now think like a librarian who reads everything. The Sun is far, far away, so its rays arrive at Earth practically <b>parallel</b> — like lines of rain falling straight down together. If the Earth were <b>flat</b>, parallel rays would hit every city at the same angle, and every stick everywhere would cast the <i>same</i> shadow at the same moment.</p>
<p>But Syene had no shadow while Alexandria had one. Same moment, same sun, different shadows. There was only one explanation: the ground itself must be <b>tilted</b> between the two cities. The Earth's surface <i>curves</i>.</p>
<svg class="illus" width="480" height="210" viewBox="0 0 480 210" role="img" aria-label="Curved Earth with two sticks: parallel sun rays make no shadow at Syene but a shadow at Alexandria">
  <rect width="480" height="210" fill="#0d1330" rx="10"/>
  <path d="M 40 210 A 260 260 0 0 1 440 210" fill="#1b2a55" stroke="#3a4a86" stroke-width="2"/>
  <g stroke="#ffd97a" stroke-width="2" opacity=".85">
    <line x1="150" y1="14" x2="150" y2="120"/>
    <line x1="205" y1="14" x2="205" y2="106"/>
    <line x1="275" y1="14" x2="275" y2="106"/>
    <line x1="330" y1="14" x2="330" y2="122"/>
  </g>
  <text x="416" y="26" fill="#ffd97a" font-size="12" text-anchor="end" font-family="Georgia">sunlight (parallel rays)</text>
  <line x1="240" y1="116" x2="240" y2="72" stroke="#f9f3e4" stroke-width="4"/>
  <text x="240" y="144" fill="#aebadf" font-size="12" text-anchor="middle" font-family="Georgia">Syene: no shadow</text>
  <line x1="120" y1="145" x2="101" y2="109" stroke="#f9f3e4" stroke-width="4"/>
  <line x1="120" y1="145" x2="100" y2="157" stroke="#e8a90c" stroke-width="3.5"/>
  <text x="106" y="182" fill="#aebadf" font-size="12" text-anchor="middle" font-family="Georgia">Alexandria: shadow!</text>
</svg>""",
            cps=[dict(
                type="mc",
                kicker="Flat-Earth test",
                q="""The Sun is so far away that its rays hit Earth as <b>parallel lines</b>. IF the Earth were flat, what would two identical sticks in Syene and Alexandria do at the same noon moment?""",
                mc=[("Cast exactly the same shadow", True),
                    ("Cast different shadows", False),
                    ("Cast no shadows at all", False)],
                good="Right! Flat ground + parallel rays = identical shadows everywhere. So DIFFERENT shadows meant the ground must curve. Two sticks just proved the Earth is round.",
                bad="Careful — picture parallel rain hitting a flat table: every spot gets hit at the same angle. So a flat Earth would give identical shadows. But that's not what happens…",
            )],
        ),
        dict(
            kicker="Chapter Three · Noon, the longest day of the year",
            title="The Stick and the Angle",
            html="""
<p>Curved how much, though? That's the genius part. On the next summer solstice, at exact noon, Eratosthenes measured the shadow of a vertical stick (a <i>gnomon</i>) in Alexandria and worked out the angle of the sunbeam: <b>7.2 degrees</b> away from straight overhead.</p>
<p>Remember your sky-measuring units: a full circle — all the way around the Earth and back — is <b>360 degrees</b>. And 7.2° is a very special slice of 360°…</p>
<p>Here's the picture in Eratosthenes' head: since the sun stood exactly overhead at Syene and 7.2° off-overhead at Alexandria, then walking from Syene to Alexandria bends you <b>7.2° around the curve of the Earth</b>. That walk is one slice of the full journey around the world.</p>""",
            cps=[dict(
                type="num",
                kicker="The magic slice",
                q="""How many times does <b>7.2°</b> fit into a full circle of <b>360°</b>? (In other words: the Syene–Alexandria distance is 1/? of the way around the whole Earth.)""",
                answers=[50], unit="times",
                hint="Try 7.2 × 10 = 72. Then how many 72s make 360? Multiply your two answers.",
            )],
        ),
        dict(
            kicker="Chapter Four · The road south",
            title="The Men Who Walked in Perfect Steps",
            html="""
<p>So the whole Earth is 50 of those slices. Now Eratosthenes needed just one more number: <b>how far is it from Syene to Alexandria?</b></p>
<p>No cars. No maps with distance markers. Egypt's answer: <b>bematists</b> — professional step-counters. These were trained surveyors who walked with perfectly even strides, counting every single step, for days and weeks, across the desert beside the Nile. (Camels were involved. Camels do not walk in even steps. The humans did the counting.)</p>
<p>The official distance came back: <b>5,000 stadia</b> — the stadion being the length of a Greek stadium racetrack. Now Eratosthenes had everything: the walk was 1/50 of the way around the world, and the walk was 5,000 stadia long.</p>
<div class="funfact">👣 Bematists were astonishingly good. Records from Alexander the Great's step-counters show their measured distances over hundreds of kilometers were often within 1–2% of modern values. Careful counting was a real profession — Tycho would have approved.</div>""",
            cps=[dict(
                type="num",
                kicker="Around the world in one multiplication",
                q="""If <b>1/50</b> of the way around the Earth is <b>5,000 stadia</b>, how many stadia is the <b>whole</b> way around?""",
                answers=[250000], unit="stadia",
                hint="50 × 5,000. Do 5 × 5 first, then bring back all five zeros.",
            )],
        ),
        dict(
            kicker="Chapter Five · The answer",
            title="How Close Did He Get?",
            html="""
<p><b>250,000 stadia.</b> Convert the ancient stadion to modern units (about 157.5 meters each, by the most common reckoning) and Eratosthenes' Earth comes out to roughly <b>39,000 kilometers</b> around.</p>
<p>The modern measured value, with satellites and lasers? <b>About 40,000 km.</b></p>
<p>Sit with that for a second. A man in sandals, using a stick, a shadow, a well, and a hired walker, measured the planet — and landed within about 2% of the space-age answer. It would stand as one of the greatest measurements in history for over a thousand years.</p>
<div class="bigidea">🌟 <b>Big Idea:</b> Eratosthenes never saw the Earth from space. He didn't need to. A great measurement is a <b>chain of small, checkable steps</b>: an angle anyone can re-measure, a distance anyone can re-walk, and arithmetic anyone can re-do. That's what makes it science — every link of the chain is open for checking.</div>""",
            cps=[dict(
                type="num",
                kicker="Grading a 2,200-year-old homework",
                q="""Eratosthenes got about <b>39,000 km</b>. The modern value is about <b>40,000 km</b>. By how many kilometers was the librarian off?""",
                answers=[1000], unit="km",
                hint="40,000 − 39,000.",
            )],
        ),
    ],
)

ECLIPSE_1919 = dict(
    title="The Day the Stars Moved — Einstein, Eddington & the 1919 Eclipse",
    h1="✦ The Day the Stars Moved ✦",
    sub="Einstein, Eddington, and the six minutes of darkness that changed physics — May 29, 1919",
    footer="Companion lesson to the Constellation Plotting Worksheets · All dates and measurements are historical<br>(yes, even the melted telescope)",
    praise=["Perfectly measured, {name}!", "Eddington would trust you with the plates, {name}!",
            "Exactly right, astronomer!", "Precise as a brass micrometer!",
            "{name}, the Royal Society approves!"],
    cert_org="Joint Eclipse Expedition · Royal Astronomical Society",
    cert_of="the tale of the 1919 eclipse",
    cert_rank="Fellow of the Eclipse Expedition",
    finale_title="Overnight, the World Changed",
    finale_html="""
<p>On November 7, 1919, the London <i>Times</i> ran the headline: <b>"REVOLUTION IN SCIENCE — New Theory of the Universe — Newtonian Ideas Overthrown."</b> Albert Einstein woke up the most famous scientist on Earth, and stayed that way for the rest of his life — <b>36 more years</b>. (People sometimes remember this test happening after he died. It's the opposite: this is the moment that made him <i>Einstein</i>.)</p>
<p>And it wasn't just a stunt. Today, the GPS satellites your phone talks to would drift off by kilometers every day if engineers didn't correct for exactly the effects Einstein predicted and Eddington confirmed. Every map app is quietly running 1919's homework.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① Gravity bends light — mass curves space itself, and starlight follows the curve.</p>
<p>② A theory earns trust by making a <b>risky prediction</b> — a number it must hit — and hitting it.</p>
<p>③ Science crosses enemy lines: a British pacifist proved a German physicist right, months after their countries stopped shooting at each other.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Berlin, November 1915",
            title="The Man Who Bent Light with His Mind",
            html="""
<p>In the middle of World War I, in Berlin, a physicist named <b>Albert Einstein</b> finished the strangest idea anyone had had about the universe in 250 years. Isaac Newton had said gravity was a force, pulling apples and planets. Einstein said something wilder: <b>massive objects bend space itself</b>, the way a bowling ball dents a trampoline — and everything, even <b>light</b>, follows the dents.</p>
<p>Kepler would have loved this part: Einstein's theory didn't just <i>say</i> things, it <b>predicted a number</b>. Starlight grazing the edge of the Sun should be bent by exactly <b>1.75 arcseconds</b>. Newton's old physics, pushed as far as it could go, predicted about half that: <b>0.87</b>. Two theories, two different numbers, one universe. All you had to do was measure.</p>
<p>One problem: to see stars <i>next to</i> the Sun, you have to look at the sky right beside the Sun — which is impossible. Unless something blocks the Sun out perfectly, for a few precious minutes…</p>
<div class="funfact">🌑 A <b>total solar eclipse</b> is a cosmic coincidence: the Moon is 400× smaller than the Sun but also 400× closer, so it covers the Sun almost exactly. No other planet we know gets eclipses this perfect.</div>""",
            cps=[dict(
                type="num",
                kicker="The waiting game",
                q="""Einstein published his theory in <b>1915</b>. The eclipse that could test it came in <b>1919</b>. How many years did the theory wait for its trial?""",
                answers=[4], unit="years",
                hint="1919 − 1915.",
            )],
        ),
        dict(
            kicker="Chapter Two · England, 1917–1919",
            title="Enemy Science",
            html="""
<p>Here's what makes this story bigger than physics. Britain and Germany had just spent four years in the most terrible war the world had seen. Millions were dead. British newspapers wouldn't even print German music reviews. And now a British team was preparing to spend a fortune to test — maybe to <i>prove</i> — the theory of a <b>German</b> scientist.</p>
<p>The man leading the charge was <b>Arthur Eddington</b>, one of Britain's best astronomers and a <b>Quaker</b> — his faith forbade him from fighting. He nearly went to a work camp for refusing the army; the Astronomer Royal, Frank Dyson, saved him by telling the government Eddington was needed for a scientific mission. Eddington believed science should heal what war had broken: if a British expedition confirmed a German's theory, it would prove that <b>truth is loyal to no nation</b>.</p>
<p>And the measurement itself? Brutally hard. The predicted shift — 1.75 arcseconds — is a <i>tiny</i> angle. Climb the ladder of sky-angles: a circle has 360 <b>degrees</b>; each degree has 60 <b>arcminutes</b>; and each arcminute splits into 60 <b>arcseconds</b>. They were hunting a shift about a thousand times smaller than the width of the full Moon — on glass photographs, with 1919 telescopes, in the field, in a hurry.</p>""",
            cps=[dict(
                type="num",
                kicker="Climbing down the angle ladder",
                q="""The full Moon spans about <b>30 arcminutes</b>, and each arcminute is <b>60 arcseconds</b>. How many <b>arcseconds</b> wide is the full Moon?""",
                answers=[1800], unit="arcseconds",
                hint="30 × 60. (3 × 6, then add the zeros back.) Compare that to the 1.75-arcsecond shift they were hunting!",
            )],
        ),
        dict(
            kicker="Chapter Three · Two ships, February 1919",
            title="Double or Nothing",
            html="""
<p>Dyson and Eddington knew one golden rule of great measurements (Tycho's rule, really): <b>never trust a single observation</b>. Clouds, broken instruments, bad luck — any one site could fail. So they sent <b>two expeditions</b> to stand in the Moon's shadow on May 29, 1919:</p>
<p>• <b>Eddington</b> sailed to <b>Príncipe</b>, a tiny island off the coast of West Africa.<br>
• <b>Crommelin and Davidson</b> sailed to <b>Sobral</b>, in the dry backlands of Brazil.</p>
<p>Fate had dealt them a lucky card: on eclipse day the Sun would sit right in front of the <b>Hyades</b> — a bright star cluster. Plenty of measurable stars right beside the blocked-out Sun. And this eclipse was a monster — near its peak, totality lasted almost <b>7 minutes</b>, one of the longest of the century.</p>
<p>The plan: photograph the star field during totality, then photograph the <i>same stars</i> months later at night, when the Sun was elsewhere. Lay the glass plates side by side, measure with microscopes. If Einstein was right, the stars near the Sun's edge would sit <i>visibly out of place</i> — pushed outward by the Sun's dent in space.</p>""",
            cps=[dict(
                type="num",
                kicker="Every second counts",
                q="""At its longest, totality lasted <b>6 minutes 51 seconds</b>. How many <b>seconds</b> is that?""",
                answers=[411], unit="seconds",
                hint="6 × 60 = 360, then add the 51.",
            )],
        ),
        dict(
            kicker="Chapter Four · Eclipse day, May 29, 1919",
            title="Clouds, Heat, and a Melted Lens",
            html="""
<p>On Príncipe, eclipse morning opened with a <b>thunderstorm</b>. Eddington had sailed 5,000 km for six minutes of sky, and the sky was solid cloud. He set up anyway. As totality began, the clouds thinned — he never even looked up, just swapped photographic plates as fast as hands allowed, sixteen exposures, praying some caught stars through the gaps. Out of <b>16 plates, only 2</b> showed enough stars to measure.</p>
<p>In Sobral, the sky was perfect — and that was the trap. The tropical heat had warped the mirror feeding their main camera, smearing every star image into mush. The expedition's backup — a humble little <b>4-inch telescope</b>, the kind an amateur might own — quietly took the sharpest pictures of the whole enterprise.</p>
<p>Months of microscope work followed. Then the numbers came out of the arithmetic, one plate at a time. Sobral's little backup telescope: a deflection of about <b>1.98</b> arcseconds. Eddington's two cloudy-day plates from Príncipe: about <b>1.61</b>. Einstein's prediction: <b>1.75</b>. Newton's: <b>0.87</b>.</p>
<div class="bigidea">🌟 <b>Big Idea:</b> Notice what saved the whole mission — <i>backups and honesty</i>. Two sites instead of one. A humble spare telescope. And when the fancy instrument failed, they said so and threw out its data. Sound familiar? It's Kepler refusing to fudge 8 arcminutes, all over again.</div>""",
            cps=[dict(
                type="num",
                kicker="Slim pickings",
                q="""Eddington exposed <b>16</b> plates but only <b>2</b> were usable. That's 1 usable plate out of every…?""",
                answers=[8], unit="plates",
                hint="16 ÷ 2.",
            ), dict(
                type="mc",
                kicker="The verdict",
                q="""Put the numbers side by side. Newton's physics predicted a shift of <b>0.87</b> arcseconds. Einstein predicted <b>1.75</b>. The measurements came in at about <b>1.98</b> and <b>1.61</b>. Which theory did the universe vote for?""",
                mc=[("Newton's — the old champion", False),
                    ("Einstein's — space really bends", True),
                    ("Neither — the data was useless", False)],
                good="Yes. Both measurements landed around Einstein's number and nowhere near Newton's half-value. When Einstein was asked what he'd have done if the eclipse said otherwise, he joked: \"Then I would feel sorry for the dear Lord — the theory is correct.\" (Confidence! But note: he still had to pass the test.)",
                bad="Look again: 1.98 and 1.61 — are those closer to 0.87, or to 1.75?",
            )],
        ),
        dict(
            kicker="Chapter Five · London, November 6, 1919",
            title="The Announcement",
            html="""
<p>The results were announced at a packed joint meeting of the Royal Society and the Royal Astronomical Society, under a portrait of Isaac Newton himself. The room understood exactly what was happening: Newton's picture of gravity — unbeaten for 232 years — was being <i>corrected</i>, in his own house, by measurements of six minutes of darkness.</p>
<p>Nobody sneered at Newton. That's not how science treats its giants. His equations still fly our spacecraft today; they're beautifully accurate for almost everything. Einstein's theory simply sees <i>deeper</i> — and the eclipse proved it where the two disagreed. The philosopher of science Karl Popper later said this moment taught him what real science <i>is</i>: Einstein's theory stuck its neck out. It named a number in advance and said <i>measure me</i>. It could have failed. It didn't.</p>
<p>A British pacifist had proven a German physicist right, one year after the armistice. Eddington called it the best thing that could have happened for science — and maybe not just for science.</p>""",
            cps=[dict(
                type="num",
                kicker="Fame, measured in years",
                q="""People sometimes misremember this test as happening after Einstein died. In fact he became world-famous in <b>1919</b> and lived until <b>1955</b>. How many years did he get to enjoy being proven right?""",
                answers=[36], unit="years",
                hint="1955 − 1919.",
            )],
        ),
    ],
)

LE_GENTIL = dict(
    title="The Unluckiest Astronomer — Le Gentil & the Transit of Venus",
    h1="✦ The Unluckiest Astronomer ✦",
    sub="Le Gentil, the transit of Venus, and humanity's first worldwide science project — 1761 & 1769",
    footer="Companion lesson to the Constellation Plotting Worksheets · All dates and misfortunes are historical<br>(yes, even the single cloud)",
    praise=["Perfectly measured, {name}!", "The Academy salutes you, {name}!", "Exactly right, voyager!",
            "Sharper than a ship's chronometer!", "Le Gentil would trade his luck for yours, {name}!"],
    cert_org="Académie Royale des Sciences · Worldwide Transit Expedition",
    cert_of="the tale of the transit of Venus",
    cert_rank="Member of the Worldwide Transit Corps",
    finale_title="The Mission That No Cloud Could Stop",
    finale_html="""
<p>Combining timings from observers scattered across the planet — Tahiti, Norway, Hudson Bay, Baja California, India — astronomers computed the distance from the Earth to the Sun: about <b>153 million kilometers</b>. The modern value is <b>149.6 million</b>. Within about 2%, humanity had measured the solar system — using the same parallax trick Tycho used on the comet, stretched across the whole Earth.</p>
<p>And Le Gentil? France's Academy had given him up for dead; his relatives were dividing his property; his job had been handed to someone else. He fought his way back, the King himself took his side, he married, raised a daughter he adored, and spent 21 more years writing his adventures — which became, of course, a bestseller. Transits of Venus come in pairs 8 years apart, separated by more than a century: after 1769 came 1874 and 1882, then 2004 and 2012. The next one is <b>December 2117</b>. Somewhere out there is a kid — maybe doing a worksheet like yours — who will see it.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① The size of the solar system was first measured by <b>teamwork</b> — dozens of observers on every continent timing the same 6 hours.</p>
<p>② In a worldwide team, no single storm, war, or heartbreak can sink the mission. Shared data is unsinkable — the lesson Tycho learned almost too late.</p>
<p>③ You can do everything right and still fail. That's not the end of the story — Le Gentil's life proves it.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · London, 1716",
            title="Homework from Beyond the Grave",
            html="""
<p>Edmond Halley — the comet man — had one more great idea in him, and he knew he wouldn't live to see it tested. Astronomers of his day had a humiliating secret: they knew the <i>shape</i> of the solar system perfectly (thank you, Kepler), but not its <b>size</b>. They knew Mars was 1.5 times farther from the Sun than Earth — but 1.5 times <i>what</i>? Nobody knew if the Sun was 50 million kilometers away or 250 million.</p>
<p>Halley's plan: on rare occasions, <b>Venus crosses directly in front of the Sun</b> — a little black dot sliding across the bright disk for about six hours. If observers watch this <i>transit</i> from places far apart on Earth — the top of the world and the bottom — they'll see Venus trace <b>slightly different paths</b> across the Sun, at slightly different timings. That difference is parallax — your old friend, the thumb-blink trick — and from it, with geometry, you can calculate the actual distance to the Sun.</p>
<p>In 1716, Halley published detailed instructions addressed to astronomers <i>not yet born</i>, begging them to scatter across the Earth for the transits he had calculated would come in <b>1761 and 1769</b>. He died in 1742, nineteen years too soon. The world took his homework seriously: for the first time in history, dozens of nations — some actively at war — sent scientists to the ends of the Earth <b>for the same measurement</b>. It was humanity's first global science project.</p>""",
            cps=[dict(
                type="num",
                kicker="Halley's long bet",
                q="""Halley died in <b>1742</b>. The first transit of his great experiment came in <b>1761</b>. How many years after his death did his homework come due?""",
                answers=[19], unit="years",
                hint="1761 − 1742.",
            )],
        ),
        dict(
            kicker="Chapter Two · The trick, planet-sized",
            title="Two Eyes for the Whole Earth",
            html="""
<p>Remember Tycho's parallax: thumb up, eyes fixed on the far background (not the thumb!), blink left eye, blink right eye — the thumb jumps against that background. Your two eyes see from slightly different places, so nearby things shift more than faraway things.</p>
<p>Halley's plan simply made the "eyes" bigger. One observer near the top of the world and one near the bottom are like two eyes <b>thousands of kilometers apart</b>. Venus is the thumb; the Sun's face is the background. Each observer times precisely when Venus enters and leaves the Sun's disk, and notes the path it takes. Compare the two records → geometry → <b>the distance to the Sun</b>.</p>
<svg class="illus" width="480" height="200" viewBox="0 0 480 200" role="img" aria-label="Two observers on Earth see Venus cross the Sun along slightly different paths">
  <rect width="480" height="200" fill="#0d1330" rx="10"/>
  <circle cx="60" cy="100" r="34" fill="#1b2a55" stroke="#3a4a86" stroke-width="2"/>
  <circle cx="60" cy="78" r="5" fill="#7fe0a7"/><text x="26" y="66" fill="#7fe0a7" font-size="11" font-family="Georgia">observer N</text>
  <circle cx="60" cy="122" r="5" fill="#ff9d6e"/><text x="26" y="146" fill="#ff9d6e" font-size="11" font-family="Georgia">observer S</text>
  <circle cx="250" cy="100" r="7" fill="#f9f3e4"/><text x="250" y="84" fill="#cdd6ee" font-size="11" text-anchor="middle" font-family="Georgia">Venus</text>
  <circle cx="400" cy="100" r="58" fill="#ffe9b0"/>
  <line x1="60" y1="78" x2="452" y2="118" stroke="#7fe0a7" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="60" y1="122" x2="452" y2="82" stroke="#ff9d6e" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="352" y1="112" x2="448" y2="117" stroke="#2a6b45" stroke-width="2.5"/>
  <line x1="352" y1="88" x2="448" y2="83" stroke="#a04a20" stroke-width="2.5"/>
  <text x="400" y="176" fill="#8f9cc4" font-size="11.5" text-anchor="middle" font-family="Georgia">two viewpoints → two paths across the Sun</text>
</svg>""",
            cps=[dict(
                type="mc",
                kicker="Bigger baseline, better blink",
                q="""With the thumb trick, your eyes are a few centimeters apart. What happens to the shift you see if the two "eyes" (observers) move <b>farther apart</b> — say, Norway and Tahiti?""",
                mc=[("The shift gets bigger — easier to measure", True),
                    ("The shift gets smaller — harder to measure", False),
                    ("Nothing changes", False)],
                good="Exactly. A wider baseline exaggerates the shift, like having eyes on opposite sides of the planet. That's WHY they had to sail to the ends of the Earth — the whole point was to get far apart.",
                bad="Try the thumb trick and then imagine your eyes moving apart. Would the thumb jump more, or less?",
            )],
        ),
        dict(
            kicker="Chapter Three · 1760–1761 · The first try",
            title="War Gets in the Way",
            html="""
<p>Enter our hero: <b>Guillaume Le Gentil</b>, French astronomer, 35 years old, sailing for the French colony of <b>Pondicherry, India</b>, over a year early, to be safely in position for the transit of June 6, 1761. Nothing could go wrong.</p>
<p>Everything went wrong. France and Britain were fighting the Seven Years' War — a true world war fought on five continents. As his ship neared India, news came: <b>Pondicherry had fallen to the British.</b> There was nowhere to land. On transit day, Le Gentil was stuck on the heaving deck of a ship in the Indian Ocean. He could <i>see</i> Venus, a perfect black dot on the Sun — but a transit measurement is a <b>precise timing</b> from a <b>precisely known location</b>, and he had neither: no steady telescope, no fixed position, a clock made useless by the rolling sea. He watched the whole thing, helpless, knowing every second of it was scientifically worthless.</p>
<p>Then he made the decision that made him a legend. The second transit of the pair was coming. He wrote to Paris, in effect: <i>I'm not coming home. I'll wait for the next one.</i></p>""",
            cps=[dict(
                type="num",
                kicker="The stubborn calendar",
                q="""Transits of Venus come in pairs <b>8 years apart</b>. Le Gentil missed the transit of <b>1761</b>. In what year was his second — and last — chance?""",
                answers=[1769], unit="",
                hint="1761 + 8.",
            )],
        ),
        dict(
            kicker="Chapter Four · 1761–1769 · The wait",
            title="Eight Years in the Indian Ocean",
            html="""
<p>Le Gentil did not sulk for eight years. He mapped the coasts of Madagascar. He studied tides, winds, and monsoons. He sailed to Manila, decided the Spanish governor there couldn't be trusted, and — when Pondicherry returned to French hands with the peace — sailed back to India. The colony welcomed him; the governor helped him build a small, perfect observatory on the ruins of the fort, with a masonry pier for his telescope, his clocks checked night after night.</p>
<p>He was ready absurdly early. And the sky cooperated: all through May 1769, morning after morning dawned <b>flawlessly clear</b>. The transit would come on the morning of <b>June 4</b> (local date). The evening before, the sky was so beautiful he could hardly sleep.</p>
<div class="funfact">🗓️ Add it up: he left France in March 1760 and would finally step back onto French soil in October 1771 — more than eleven years, for two mornings of astronomy.</div>""",
            cps=[dict(
                type="num",
                kicker="A long time from home",
                q="""Le Gentil was away for about <b>11 years and 6 months</b>. How many <b>months</b> is that?""",
                answers=[138], unit="months",
                hint="11 × 12 = 132, then add the 6.",
            )],
        ),
        dict(
            kicker="Chapter Five · The morning of June 4, 1769",
            title="One Cloud",
            html="""
<p>In the pre-dawn dark, the stars shone. Le Gentil took his post. And then, as sunrise approached — after <i>weeks</i> of perfect skies — a haze drifted in from the sea, thickening into cloud, and parked itself <b>in front of the Sun</b>.</p>
<p>It stayed there for almost exactly the length of the transit. As Venus slid off the Sun's face — the last contact he had crossed the world twice and waited eight years to time — the sky was a white blank. Within the hour, the cloud dissolved. The Sun blazed down on Pondicherry for the rest of the day, brilliant and useless.</p>
<p>Le Gentil wrote in his journal that he could barely hold his pen: <i>"That is the fate which often awaits astronomers… I had traveled more than ten thousand leagues, only to be the spectator of a fatal cloud."</i> For two weeks he couldn't bring himself to write up the record. (Cruelest of all: in Manila, the city he'd left, the morning was perfectly clear.)</p>
<p>But here is the thing about a <b>worldwide</b> experiment: Le Gentil's cloud didn't kill it. That same morning, Captain Cook's team timed the transit from <b>Tahiti</b>; others succeeded in Norway, in Hudson Bay, in Baja California, in Russia. The data poured back to Europe from every corner of the Earth and was <b>shared</b> — added up into one answer no single observer, however unlucky, could have reached alone.</p>
<div class="bigidea">🌟 <b>Big Idea:</b> Tycho hoarded his data and nearly took it to the grave. Halley's generation flipped the model: <b>plan together, measure everywhere, share everything.</b> When science works like that, one cloud — or one war, or one heartbreak — can't stop it.</div>""",
            cps=[dict(
                type="num",
                kicker="The team's answer",
                q="""Combining everyone's timings, astronomers calculated the Earth–Sun distance at about <b>153 million km</b>. The modern value is about <b>150 million km</b>. By how many <b>million km</b> did the 1769 team miss?""",
                answers=[3], unit="million km",
                hint="153 − 150.",
            )],
        ),
        dict(
            kicker="Chapter Six · Paris, October 1771",
            title="The Dead Man Comes Home",
            html="""
<p>The voyage home nearly finished him — dysentery, storms, a hurricane, missed ships. When Le Gentil finally walked back into Paris after eleven and a half years, he discovered the final insult: he had been <b>declared legally dead</b>. His relatives were busily dividing up his estate. His seat in the Academy of Sciences had been given to another man. His mail had been lost or stolen for years; as far as France was concerned, he was a ghost.</p>
<p>A lesser man would have shattered. Le Gentil went to court, and eventually the King himself intervened to restore his place. He married a woman named Madame Potier, had a daughter he utterly adored, was welcomed back into the Academy, and spent two happy decades writing the story of his voyage — clouds, pirates, monsoons, and all. He outlived nearly every misfortune the universe had thrown at him, and by every account, he died content.</p>
<p>Astronomers still tell his story to each other, half as a joke and half as a prayer. But notice: <b>the experiment he suffered for worked.</b> His name is stitched into the first true measurement of the solar system — not because his telescope succeeded, but because he was part of the team that did.</p>""",
            cps=[dict(
                type="num",
                kicker="Mark your calendar (or your great-great-grandchild's)",
                q="""After a transit pair, the next pair doesn't come for over a century. The transits of 1761 &amp; 1769 were followed by 1874 &amp; 1882, then 2004 &amp; 2012. The next transit is <b>105 years after 2012</b>. What year should your great-great-grandchildren be ready?""",
                answers=[2117], unit="",
                hint="2012 + 105.",
            )],
        ),
    ],
)
