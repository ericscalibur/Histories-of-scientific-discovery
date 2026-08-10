# -*- coding: utf-8 -*-
"""Story data: Pigeon Poop Nobel (CMB), Henrietta Leavitt."""

PIGEON = dict(
    title="The Hiss from the Beginning of Time — the Pigeon Poop Nobel Prize",
    h1="✦ The Hiss from the Beginning of Time ✦",
    sub="Two scientists, one giant antenna, a family of stubborn pigeons — and the echo of the Big Bang · 1964",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(especially the pigeons)",
    praise=["Perfectly measured, {name}!", "Bell Labs would hire you on the spot, {name}!",
            "Exactly right, radio astronomer!", "Cleaner than a scrubbed antenna!",
            "{name}, not even the pigeons could distract you!"],
    cert_org="Bell Telephone Laboratories · Holmdel Horn Antenna",
    cert_of="the tale of the cosmic microwave background",
    cert_rank="Listener to the Beginning of Time",
    finale_title="The Oldest Light There Is",
    finale_html="""
<p>In 1978, Arno Penzias and Robert Wilson won the <b>Nobel Prize in Physics</b> — for a discovery they had spent a year trying to make go away. The hiss is called the <b>cosmic microwave background</b>: light released when the universe was just 380,000 years old, stretched by 13.8 billion years of cosmic expansion until it became a faint microwave whisper coming from every direction at once. It is, quite literally, the oldest thing anyone has ever detected — the universe's baby picture.</p>
<p>Later spacecraft (COBE, WMAP, Planck) photographed that baby picture in exquisite detail, and it's now our single best source of information about how the universe began. And one more thing: an old-fashioned TV tuned between channels shows dancing static — about 1% of that static is the cosmic microwave background. You've probably already seen the Big Bang. It looked like snow.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① The Big Bang left an echo, and it's still arriving — a 3-degrees-above-absolute-zero whisper from every direction in the sky.</p>
<p>② Before you claim something amazing, <b>rule out everything boring first</b> — city noise, loose bolts, and yes, pigeon droppings. That's what made the discovery believable.</p>
<p>③ Talk to your neighbors. The team that could explain the hiss was a 45-minute drive away the whole time.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Holmdel, New Jersey · 1964",
            title="The Giant Ear",
            html="""
<p>On a hilltop in New Jersey stood one of the strangest instruments in America: a giant aluminum horn, shaped like an ear trumpet for a titan, 20 feet across at its mouth. Bell Labs had built it to catch radio signals bounced off early satellites. When the satellite work ended, two young radio astronomers — <b>Arno Penzias</b> and <b>Robert Wilson</b> — got permission to point it at the sky and do pure science with it.</p>
<p>A radio telescope doesn't take pictures; it <i>listens</i>. Stars, galaxies, and gas clouds all give off radio waves, and a good antenna can hear them. But first you must know your instrument's own noise — every electronic system hums a little — so Penzias and Wilson began by carefully measuring what the antenna heard when it should have heard <i>almost nothing</i>.</p>
<p>It heard something.</p>""",
            cps=[dict(
                type="num",
                kicker="Size up the ear",
                q="""The horn's opening was about <b>20 feet</b> across. One foot is about <b>30 centimeters</b>. About how many <b>meters</b> is 20 feet? (Remember: 100 cm = 1 m.)""",
                answers=[6], unit="meters",
                hint="20 × 30 = 600 cm. Now turn centimeters into meters.",
            )],
        ),
        dict(
            kicker="Chapter Two · The problem",
            title="The Hiss That Wouldn't Die",
            html="""
<p>Wherever they pointed the horn — up, down, east, west — a faint microwave <b>hiss</b> was always there. Day and night. Summer and winter. It never got louder, never got quieter, never moved. Radio astronomers measure faint signals as a temperature, and this one was tiny: about <b>3 degrees above absolute zero</b>, the coldest temperature possible.</p>
<p>A signal from a star or a galaxy gets stronger when you point at the star and weaker when you point away. This hiss didn't care where they pointed. That left two possibilities: either the antenna itself was making the noise (boring, fixable)… or the <i>entire sky</i> was very faintly glowing (absurd).</p>
<p>Being good scientists, they bet on boring — and set out to destroy their own discovery. Remember Kepler trying seventy times to make circles work before believing something new? Same spirit, opposite direction: <b>before you believe the amazing thing, you must fail to explain it with every ordinary thing.</b></p>""",
            cps=[dict(
                type="num",
                kicker="Almost absolute zero",
                q="""Absolute zero — the coldest anything can be — is about <b>−273°C</b>. The mysterious hiss glowed about <b>3 degrees warmer</b> than that. What temperature is the hiss, in °C? (Your worksheets taught you negative numbers for a reason!)""",
                answers=[-270], unit="°C",
                hint="Start at −273 and go UP by 3. On a number line, warmer means moving toward zero.",
            )],
        ),
        dict(
            kicker="Chapter Three · The investigation",
            title="Suspect Number One: Pigeons",
            html="""
<p>For the better part of a year, Penzias and Wilson hunted the noise. Was it New York City, humming 50 km away? No — the hiss was the same pointing toward the city and away. Military radar? No. A nearby nuclear test's leftovers in the atmosphere? Faded over months — the hiss didn't. Loose joints in the antenna? They taped every seam with aluminum tape. Hiss unchanged.</p>
<p>Then they found the pigeons. A pair had nested deep inside the horn, coating the inside with what their official report gorgeously called <b>"a white dielectric material."</b> (Say it with us: pigeon droppings.) Aha! Warm droppings could glow with microwaves! They evicted the pigeons, shipped them in a crate to another Bell Labs site 50 km away, and scrubbed the whole horn clean.</p>
<p>Two problems. First: they were <i>homing pigeons</i> — the birds flew straight back and moved in again. (The second eviction was… more permanent, and Wilson felt bad about it for decades.) Second, and worse: with the horn scrubbed spotless and pigeon-free, the hiss was <b>still there</b>. Identical. Everywhere. Forever.</p>
<div class="funfact">🕊️ The pigeon trap — a humane cage labeled "Project Echo" — is now in the Smithsonian. It may be the only pigeon trap in history connected to a Nobel Prize.</div>""",
            cps=[dict(
                type="num",
                kicker="The pigeons come home",
                q="""Homing pigeons fly about <b>80 km per hour</b>. Released about <b>40 km</b> from home, how many <b>minutes</b> did the pigeons need to fly back to their nice warm antenna?""",
                answers=[30], unit="minutes",
                hint="40 is half of 80 — so they need half an hour.",
            )],
        ),
        dict(
            kicker="Chapter Four · One phone call",
            title="“Boys, We've Been Scooped”",
            html="""
<p>Out of suspects, Penzias happened to mention the stubborn hiss during a phone call with another astronomer — who said: you need to call <b>Princeton</b>. There, physicist Robert Dicke and his team had predicted that if the universe began in a hot Big Bang, the flash of that beginning should <i>still be arriving</i> — cooled and stretched by billions of years of expansion into faint microwaves coming from <b>every direction in the sky</b>, at a temperature of just a few degrees above absolute zero.</p>
<p>They were, at that very moment, building an antenna to look for it — <b>less than an hour's drive from the hiss</b>.</p>
<p>Penzias called. He described the antenna, the year of checks, the taped seams, the evicted pigeons, the unkillable 3-degree hiss from everywhere. Dicke listened, hung up, and turned to his lab: <i>"Boys, we've been scooped."</i> The signal his team was preparing to hunt had been sitting in Bell Labs' logbooks for a year — labeled as a nuisance.</p>
<p>The two teams published side-by-side papers in 1965: Penzias and Wilson describing the hiss, the Princeton team explaining it. The universe had a beginning, and its afterglow was on the air, on every channel, all the time.</p>
<div class="bigidea">🌟 <b>Big Idea:</b> The pigeon year wasn't wasted — it <i>was</i> the discovery. Because they had ruled out every boring explanation, nobody could wave the hiss away. Doubt your own result harder than anyone else will, and what survives belongs to you.</div>""",
            cps=[dict(
                type="num",
                kicker="Big numbers for a big bang",
                q="""That hiss had been traveling since near the beginning of the universe — about <b>13.8 billion years</b>. Written out, one billion is 1,000,000,000. How many <b>zeros</b> in one billion?""",
                answers=[9], unit="zeros",
                hint="Count them in groups of three: 1,000,000,000.",
            )],
        ),
        dict(
            kicker="Chapter Five · Stockholm, 1978",
            title="The Prize for the Noise",
            html="""
<p>Fourteen years after the hiss first refused to die, Penzias and Wilson stood in Stockholm accepting the Nobel Prize in Physics. Two radio engineers who set out to calibrate an antenna had found the oldest light in existence — by being too honest to ignore a nuisance and too stubborn to stop chasing it.</p>
<p>There's a friendly argument scientists still have about this story: Dicke's team <i>predicted</i> the signal; Penzias and Wilson <i>found</i> it without knowing what it was. Who deserved the prize? Most scientists answer: the discovery went to the ones who did what science demands — they measured something real, checked everything, and refused to fudge. (You may notice this is the third story in a row where that's the moral. It's the only moral science has.)</p>""",
            cps=[dict(
                type="num",
                kicker="Patience, again",
                q="""They first wrestled with the hiss in <b>1964</b> and won the Nobel Prize in <b>1978</b>. How many years did the universe make them wait for the medal?""",
                answers=[14], unit="years",
                hint="1978 − 1964.",
            )],
        ),
    ],
)

LEAVITT = dict(
    title="The Yardstick of the Universe — Henrietta Leavitt",
    h1="✦ The Yardstick of the Universe ✦",
    sub="Henrietta Leavitt, the Harvard Computers, and the discovery that measured the cosmos · 1893–1923",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(the pay really was 25 cents an hour)",
    praise=["Perfectly measured, {name}!", "Miss Leavitt would double-check and approve, {name}!",
            "Exactly right, computer!", "Precise as a glass plate under a magnifier!",
            "{name}, best mind at the Observatory!"],
    cert_org="Harvard College Observatory",
    cert_of="the tale of Henrietta Leavitt",
    cert_rank="Harvard Computer, First Class",
    finale_title="The Woman Who Handed Us the Universe",
    finale_html="""
<p>In 1923, Edwin Hubble found a Cepheid star blinking in the Andromeda "nebula," applied Leavitt's law, and proved Andromeda was not a cloud inside our galaxy but <b>another galaxy entirely</b> — an island of hundreds of billions of stars, unimaginably far away. The universe went from one galaxy to billions, almost overnight, and the tool that did it was Leavitt's yardstick. Hubble himself said she deserved the Nobel Prize.</p>
<p>The Nobel committee agreed — too late. In 1925 a Swedish mathematician began paperwork to nominate her, and only then learned she had died of cancer in 1921, at 53. Nobel Prizes are never given to those who have passed away. She never knew what her law would do: today, when astronomers say a galaxy is 50 million light-years away, somewhere at the bottom of that measurement is Henrietta Leavitt, at a wooden desk, being paid 25 cents an hour, noticing a pattern no one else had the patience to see.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① Some stars blink in a code: <b>the slower the blink, the brighter the star truly is</b> — Leavitt's law.</p>
<p>② That law turns brightness into <b>distance</b> — it's the yardstick that measured the Milky Way, Andromeda, and the expanding universe.</p>
<p>③ Titles and paychecks measure a person's job. They do not measure a person's contribution.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Harvard College Observatory · 1890s",
            title="The Computers Wore Skirts",
            html="""
<p>Before "computer" meant a machine, it meant a <b>person who computes</b>. At Harvard's observatory, the director hired a room full of them — all women, because (he openly admitted) he could pay women a fraction of what men demanded: about <b>25 cents an hour</b>. The men worked the telescopes at night; the women were handed the glass photographs the telescopes produced and told to measure, catalog, and calculate. They were expected to be careful, quiet, and unimportant.</p>
<p>The room had other plans. Williamina Fleming, hired away from work as the director's maid, ended up classifying ten thousand stars and discovering the Horsehead Nebula. Annie Jump Cannon, nearly deaf since childhood, invented the system for sorting stars (O-B-A-F-G-K-M) that every astronomer on Earth still memorizes today. And at one desk sat a minister's daughter from Massachusetts, also nearly deaf after an illness: <b>Henrietta Swan Leavitt</b>. Colleagues remembered her as the quietest person in the room, and the hardest working. One astronomer called her "possessed of the best mind at the Observatory."</p>""",
            cps=[dict(
                type="num",
                kicker="A computer's paycheck",
                q="""At <b>25 cents</b> an hour, how many <b>dollars</b> did a Harvard computer earn in an <b>8-hour</b> day? (100 cents = 1 dollar.)""",
                answers=[2], unit="dollars",
                hint="25 × 8 = 200 cents. Now make it dollars.",
            )],
        ),
        dict(
            kicker="Chapter Two · Glass universes",
            title="Ten Years of Blinking Dots",
            html="""
<p>Leavitt's assignment sounded numbing: compare photographs of the same patch of sky taken on different nights, and find stars that <b>changed brightness</b> — variable stars. The photos came from Harvard's southern station in Peru and showed the <b>Magellanic Clouds</b>, two little companion galaxies of the Milky Way (southern-sky neighbors of Crux, which you've plotted).</p>
<p>Her method was a marvel of patience: lay a negative plate from one night over a positive plate from another; any star that changed brightness pops out as a mismatched dot among tens of thousands. Dot by dot, plate by plate, year after year, Leavitt found them — eventually <b>2,400 variable stars</b>, roughly half of all the variable stars known to humanity at the time. A Princeton astronomer, half-joking and half-awed, called her a "variable-star fiend."</p>
<p>Among her variables was one special breed: <b>Cepheids</b>, stars that pulse like slow heartbeats — brightening, dimming, brightening again on a steady rhythm of days or weeks, each star keeping its own faithful period like a lighthouse with its own signature.</p>""",
            cps=[dict(
                type="num",
                kicker="The patience budget",
                q="""Leavitt cataloged about <b>2,400</b> variable stars over roughly <b>10 years</b> of plate work. On average, about how many per year is that?""",
                answers=[240], unit="stars per year",
                hint="2,400 ÷ 10 — just knock off one zero.",
            )],
        ),
        dict(
            kicker="Chapter Three · 1908–1912",
            title="The Pattern in the Blinking",
            html="""
<p>Here's the problem Leavitt solved without anyone asking her to. Normally, you can't tell if a star looks bright because it <i>is</i> bright, or just because it's <i>close</i> — a candle nearby outshines a lighthouse far away. Brightness alone tells you nothing about distance. This is why nobody knew how big anything in the universe was.</p>
<p>But Leavitt noticed her Small Magellanic Cloud Cepheids had a hidden advantage: they're all in the same faraway cloud, so they're all at <b>practically the same distance</b> from us — like streetlights in one distant town. Same distance means the comparison is fair: if one looks brighter than another, it truly <i>is</i> brighter.</p>
<p>So she compared 25 of them, and there it was — a pattern so clean it looks like a law of nature, because it is one. <b>The longer a Cepheid's blink cycle, the brighter the star truly is.</b> A 3-day blinker is modest; a 30-day blinker is a monster thousands of times brighter than the Sun. Plot period against brightness and the stars fall obediently along a single line.</p>
<svg class="illus" width="440" height="240" viewBox="0 0 440 240" role="img" aria-label="Chart: Cepheid blink period versus true brightness, points rising along a line">
  <rect width="440" height="240" fill="#0d1330" rx="10"/>
  <line x1="56" y1="192" x2="404" y2="192" stroke="#3a4a86" stroke-width="1.5"/>
  <line x1="56" y1="192" x2="56" y2="28" stroke="#3a4a86" stroke-width="1.5"/>
  <text x="230" y="222" fill="#8f9cc4" font-size="12" text-anchor="middle" font-family="Georgia">blink period (days) →</text>
  <text x="30" y="110" fill="#8f9cc4" font-size="12" text-anchor="middle" font-family="Georgia" transform="rotate(-90 30 110)">true brightness →</text>
  <line x1="70" y1="176" x2="390" y2="44" stroke="#3a5da8" stroke-width="1.5" stroke-dasharray="5 5"/>
  <g fill="#e8a90c" stroke="#8a6400" stroke-width="0.8">
    <circle cx="80" cy="174" r="4.5"/><circle cx="112" cy="158" r="4.5"/><circle cx="140" cy="150" r="4.5"/>
    <circle cx="168" cy="134" r="4.5"/><circle cx="196" cy="126" r="4.5"/><circle cx="224" cy="112" r="4.5"/>
    <circle cx="252" cy="102" r="4.5"/><circle cx="280" cy="88" r="4.5"/><circle cx="308" cy="80" r="4.5"/>
    <circle cx="336" cy="64" r="4.5"/><circle cx="364" cy="56" r="4.5"/>
  </g>
  <text x="96" y="205" fill="#aebadf" font-size="11" font-family="Georgia">quick blinkers: dimmer</text>
  <text x="392" y="40" fill="#aebadf" font-size="11" text-anchor="end" font-family="Georgia">slow blinkers: brighter</text>
</svg>
<div class="bigidea">🌟 <b>Big Idea:</b> Leavitt's discovery came from doing a "boring" job with ferocious care — thousands of comparisons nobody would ever applaud — until a pattern surfaced that nobody else on Earth had the data, or the patience, to see. Tycho would recognize her instantly as one of his own.</div>""",
            cps=[dict(
                type="mc",
                kicker="Read the pattern",
                q="""Three Cepheids, all in the Small Magellanic Cloud (so: all the same distance). Star A blinks every <b>2 days</b>. Star B blinks every <b>10 days</b>. Star C blinks every <b>30 days</b>. According to Leavitt's law, which star is truly the brightest?""",
                mc=[("Star A — the fast blinker", False),
                    ("Star B — the middle one", False),
                    ("Star C — the slow blinker", True)],
                good="Right — slower blink, brighter star. Now flip it around: measure any Cepheid's blink, anywhere in the sky, and Leavitt's law tells you its TRUE brightness. That's about to become the most powerful trick in astronomy.",
                bad="Look at the chart: which side of the line are the slow blinkers on?",
            )],
        ),
        dict(
            kicker="Chapter Four · The yardstick",
            title="How to Measure the Unmeasurable",
            html="""
<p>Why does that pattern matter so much? Because it breaks the candle-versus-lighthouse problem wide open. Think of car headlights: they're all about equally bright, so when you see faint headlights at night, you instantly know the car is <i>far</i>. Faintness becomes distance — <b>once you know the true brightness</b>.</p>
<p>Cepheids are headlights that <i>announce their true brightness</i> — you just have to time the blink. Spot a Cepheid anywhere in the universe: time its period → Leavitt's law gives its true brightness → compare with how faint it looks → out comes the <b>distance</b>. Astronomers finally had a yardstick that reached beyond the solar system, beyond the nearest stars, out into the deep.</p>
<p>Within a few years, astronomers used Leavitt's law to measure the Milky Way itself. Then, in 1923, Edwin Hubble — with the world's new biggest telescope — spotted a Cepheid blinking inside the Andromeda spiral, timed it, applied the law… and the universe grew a thousandfold in one calculation.</p>""",
            cps=[dict(
                type="num",
                kicker="From her desk to Andromeda",
                q="""Leavitt published her period–brightness law in <b>1912</b>. Hubble used it on Andromeda in <b>1923</b>. How many years from her quiet paper to the universe getting bigger?""",
                answers=[11], unit="years",
                hint="1923 − 1912.",
            )],
        ),
        dict(
            kicker="Chapter Five · What she never knew",
            title="The Prize That Came Too Late",
            html="""
<p>Henrietta Leavitt kept working at the Observatory — eventually promoted to head of stellar photometry — through illness, hearing loss, and a salary that never came close to matching her importance. She died of cancer in December <b>1921</b>, at 53. Andromeda's secret fell two years after her death; the expanding universe, a few years after that. All of it stood on her law.</p>
<p>In <b>1925</b>, the Swedish mathematician Gösta Mittag-Leffler began preparing her Nobel Prize nomination — and learned, to his dismay, that he was writing to a woman who had died. The rules were firm then as now: no posthumous prizes. The nomination stopped there.</p>
<p>Remember Kepler waiting decades to keep his promise to Tycho? History kept a small promise to Leavitt too, in its own way: there is a crater on the Moon named <b>Leavitt</b>, an asteroid named for her, and every measured distance in the cosmos carrying her fingerprints. And her story has a warning worth saying out loud: when Jocelyn Bell Burnell found pulsars in 1967, the prize went to her supervisor. Science is a team sport — <b>watch who gets left off the podium.</b></p>""",
            cps=[dict(
                type="num",
                kicker="Four years too late",
                q="""Leavitt died in <b>1921</b>. The Nobel nomination attempt began in <b>1925</b>. By how many years did the world's biggest prize miss the quietest person in the room?""",
                answers=[4], unit="years",
                hint="1925 − 1921.",
            ), dict(
                type="num",
                kicker="One last big number",
                q="""Andromeda — the galaxy Leavitt's yardstick unlocked — is about <b>2.5 million</b> light-years away: the light arriving tonight left it 2,500,000 years ago. How many <b>zeros</b> are in 2,500,000?""",
                answers=[5], unit="zeros",
                hint="Write it out: 2,500,000 — count only the zeros.",
            )],
        ),
    ],
)
