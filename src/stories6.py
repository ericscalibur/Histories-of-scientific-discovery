# -*- coding: utf-8 -*-
"""Story data: the Sun-Moon size coincidence."""

SKY_SIM = '''<div style="background:#fdf9ee; border:1.5px solid #c9b57e; border-radius:12px; padding:14px 16px; margin:14px 0;">
  <div style="text-align:center; font-size:.8rem; letter-spacing:2px; text-transform:uppercase; color:#8a6400; font-weight:bold; margin-bottom:8px;">Your sky simulator &middot; discs drawn to true relative scale, magnified together</div>
  <div style="text-align:center;">
    <svg id="ss-sky" width="340" height="230" viewBox="0 0 340 230" style="background:#04070f; border-radius:10px; max-width:100%;">
      <circle id="ss-glow" cx="170" cy="115" r="70" fill="#ffe9b0" opacity="0.12"/>
      <circle id="ss-sun" cx="170" cy="115" r="58" fill="#e8a90c" stroke="#ffe9b0" stroke-width="1"/>
      <circle id="ss-moon" cx="170" cy="115" r="55" fill="#0d1016" stroke="#3a4460" stroke-width="1"/>
    </svg>
  </div>
  <div style="display:flex; justify-content:center; gap:26px; margin:10px 0 2px; font-size:1.02rem; color:#3d3320;">
    <span>Sun in the sky: <b id="ss-sunout">–</b></span>
    <span>Moon in the sky: <b id="ss-moonout">–</b></span>
  </div>
  <div id="ss-verdict" style="text-align:center; font-weight:bold; font-size:1.05rem; margin:6px 0 12px;">&nbsp;</div>
  <div style="max-width:480px; margin:0 auto;">
    <label style="display:block; font-size:.92rem; color:#3d3320; margin-bottom:2px;">Earth &rarr; Sun distance: <b id="ss-sund">149.6 million km</b></label>
    <input id="ss-sunslider" type="range" min="1471" max="1521" value="1496" style="width:100%;">
    <div style="display:flex; justify-content:space-between; font-size:.76rem; color:#8a6400; margin-bottom:10px;"><span>147.1 million km &middot; perihelion (early January)</span><span>aphelion (early July) &middot; 152.1 million km</span></div>
    <label style="display:block; font-size:.92rem; color:#3d3320; margin-bottom:2px;">Earth &rarr; Moon distance: <b id="ss-moond">384,400 km</b></label>
    <input id="ss-moonslider" type="range" min="3565" max="4067" value="3844" style="width:100%;">
    <div style="display:flex; justify-content:space-between; font-size:.76rem; color:#8a6400;"><span>356,500 km &middot; perigee (closest)</span><span>apogee (farthest) &middot; 406,700 km</span></div>
  </div>
  <div style="text-align:center; margin-top:12px; display:flex; gap:8px; flex-wrap:wrap; justify-content:center;">
    <button type="button" class="ss-preset" data-sun="1471" data-moon="3565" style="font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;">Biggest of both</button>
    <button type="button" class="ss-preset" data-sun="1521" data-moon="3565" style="font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;">Big Moon, small Sun</button>
    <button type="button" class="ss-preset" data-sun="1471" data-moon="4067" style="font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;">Small Moon, big Sun</button>
    <button type="button" class="ss-preset" data-sun="1496" data-moon="3844" style="font-family:Georgia,serif; cursor:pointer; background:#fff8e6; border:1.5px solid #c9b57e; border-radius:8px; padding:7px 12px; font-size:.85rem; color:#5a4a1a;">Average day</button>
  </div>
</div>
<script>
(function(){
  var SUN_D = 1392700, MOON_D = 3474.8, PX = 3.55;
  var sunS = document.getElementById('ss-sunslider');
  var moonS = document.getElementById('ss-moonslider');
  if (!sunS) return;
  function arcmin(diam, dist){ return (diam / dist) * 3437.75; }
  function update(){
    var dSun = sunS.value * 100000;             // slider is in 0.1-million-km units
    var dMoon = moonS.value * 100;              // slider is in 100-km units
    var aSun = arcmin(SUN_D, dSun), aMoon = arcmin(MOON_D, dMoon);
    document.getElementById('ss-sunout').textContent = aSun.toFixed(1) + '\\u2032 across';
    document.getElementById('ss-moonout').textContent = aMoon.toFixed(1) + '\\u2032 across';
    document.getElementById('ss-sund').textContent = (sunS.value/10).toFixed(1) + ' million km';
    document.getElementById('ss-moond').textContent = Number(dMoon).toLocaleString('en-US') + ' km';
    document.getElementById('ss-sun').setAttribute('r', (aSun * PX / 2).toFixed(1));
    document.getElementById('ss-moon').setAttribute('r', (aMoon * PX / 2).toFixed(1));
    document.getElementById('ss-glow').setAttribute('r', (aSun * PX / 2 + 11).toFixed(1));
    var v = document.getElementById('ss-verdict');
    if (aMoon >= aSun){
      v.textContent = '\\u2600 Eclipse today would be TOTAL \\u2014 the Moon covers the whole Sun (corona time!)';
      v.style.color = '#1e7d43';
    } else {
      v.textContent = '\\u26AA Eclipse today would be ANNULAR \\u2014 the Moon is too small; a blazing ring is left';
      v.style.color = '#b03030';
    }
  }
  sunS.addEventListener('input', update);
  moonS.addEventListener('input', update);
  document.querySelectorAll('.ss-preset').forEach(function(b){
    b.addEventListener('click', function(){
      sunS.value = b.dataset.sun; moonS.value = b.dataset.moon; update();
    });
  });
  update();
})();
</script>'''

SUN_MOON = dict(
    title="The Great Coincidence — The Sun, the Moon, and Half a Degree",
    h1="✦ The Great Coincidence ✦",
    sub="Why the Moon fits the Sun so perfectly in our sky — the luckiest accident in the solar system",
    footer="Companion lesson to the Constellation Plotting Worksheets · All numbers are real<br>(and so is the luck)",
    praise=["Measured to the arcminute, {name}!", "The corona salutes you, {name}!",
            "Exactly right, eclipse chaser!", "{name}, the shadow falls where you said it would!",
            "Perfect fit, {name} — just like the Moon!"],
    cert_org="The Fellowship of the Corona",
    cert_of="the tale of the great coincidence",
    cert_rank="Master of the Half-Degree",
    finale_title="Twice Lucky",
    finale_html="""
<p>Here is what makes this story different from every law of nature ever discovered. Kepler's third law has a <i>reason</i> — gravity forces it to be true. Galileo's falling law has a reason. But the two 400s? As far as anyone knows, <b>there is no reason at all</b>. The Moon didn't have to be that size. It didn't have to sit at that distance. Astronomers have searched the solar system's hundreds of moons, and no other moon-planet pairing produces such a perfect match. It's not a law. It's not a plan. It's a <b>coincidence</b> — and learning to tell laws from coincidences is one of the sharpest tools a thinking person ever owns.</p>
<p>And we are lucky twice. Because the fit isn't just perfect in space — it's perfect in <i>time</i>. The Moon is drifting away, so the match only works for a cosmic moment. A few hundred million years ago the Moon hung bigger and blotted the Sun out completely, corona and all hidden. A few hundred million years from now, every eclipse will be a ring. We happen to live in the narrow age when the fit is exact — <b>and</b> we happen to be the first species on this planet able to look up, notice, measure it, and predict the next one to the minute.</p>
<p>So the next time totality sweeps across some lucky stripe of the Earth, and day becomes night, and the corona blazes out around a black circle in the sky — remember what you're really seeing. A furnace 400 times wider than a rock, parked 400 times farther away, lining up to the arcminute. Nobody arranged it. Nothing requires it. The universe simply dealt us a perfect hand, and we — measurers that we are — noticed.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① <b>Apparent size = true size ÷ distance.</b> A coin at arm's length can cover a mountain — or the Sun.</p>
<p>② The Sun is ~400× wider than the Moon AND ~400× farther away — the two 400s cancel. Said most sharply: <b>each sits about 109 of its own widths from your eye</b>, so both discs span about half a degree (30 arcminutes).</p>
<p>③ Both orbits are ovals, so the fit wobbles: big Moon + small Sun = <b>total</b> eclipse; small Moon + big Sun = <b>annular</b> "ring of fire."</p>
<p>④ Laws have reasons; coincidences don't. Knowing the difference is a scientific superpower.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · A battlefield in Anatolia · May 28, 585 BC",
            title="The Day the War Stopped",
            html="""
<p>Two armies — the Medes and the Lydians — had been at war for five brutal years. On this afternoon they were locked in battle yet again when, without warning, <b>the day turned into night</b>. The Sun was devoured, a black disc where it should have been, stars snapping out in the afternoon sky. The ancient historian Herodotus tells us what happened next: both armies stopped fighting on the spot, took it as a message no general could overrule, and made peace — sealed with a double wedding between the royal families.</p>
<p>That afternoon was a <b>total eclipse of the Sun</b>, and it hides a question so obvious that almost nobody thinks to ask it. For the Moon to blot out the Sun <i>exactly</i> — not too small, leaving blinding fire around the edges, and not so large that it swallows the spectacle — the two discs must appear <b>almost precisely the same size</b> in our sky. And they do. Hold a small coin at arm's length: it neatly covers the full Moon. The <i>same coin</i>, at the same arm's length, neatly covers the Sun.</p>
<p>Both discs span about <b>half a degree</b> of sky. Ancient people could be forgiven for assuming they were two similar objects — two lamps of roughly equal size, wheeling overhead. The truth, as you're about to calculate, is so lopsided it sounds like a misprint.</p>""",
            cps=[dict(
                type="num",
                kicker="Half a degree, in astronomer's units",
                q="""Astronomers slice each degree into 60 <b>arcminutes</b>. The Sun and Moon each span about <b>half a degree</b> of sky. How many arcminutes is that?""",
                answers=[30], unit="arcminutes",
                hint="Half of 60.",
            )],
        ),
        dict(
            kicker="Chapter Two · The numbers behind the trick",
            title="The Two 400s",
            html="""
<p>Here are the real measurements. The Moon is a rock about <b>3,500 km</b> across — you could drive around it in a long summer. The Sun is a fusion furnace about <b>1,400,000 km</b> across — more than a million Earths would fit inside it. These two objects could not be less alike. So how can they possibly look identical in our sky?</p>
<p>Because of the oldest rule of seeing there is: <b>apparent size = true size ÷ distance</b>. Your thumb is tiny, but held close to your eye it can blot out a mountain. Every child who has ever "squished" a distant friend's head between two fingers has used the rule. Distance shrinks everything, in exact mathematical proportion.</p>
<p>Now watch the miracle happen — it comes in two halves. First: the Sun is about <b>400 times wider</b> than the Moon (check it yourself below). Second: the Sun is also about <b>400 times farther away</b>. One 400 makes the Sun's disc enormous; the other 400 shrinks it right back down. The two 400s <b>cancel</b>, and the furnace and the rock arrive at your eye wearing the same disguise.</p>
<p>And here is the coincidence in its purest, sharpest form. Forget kilometers — measure each object's distance <b>in its own widths</b>. How many Moon-widths away is the Moon? How many Sun-widths away is the Sun? Two completely different divisions, dividing numbers thousands of times apart — work them both below and watch <b>the same answer</b> fall out of each: roughly <b>109 of its own widths</b>. That is all "looking the same size" ever means. Any object, of any size anywhere, parked about 109 of its own widths from your eye, shows exactly a half-degree disc. A one-centimeter button held 110 centimeters away covers the full Moon. Try it tonight — you'll be holding the great coincidence between your fingers.</p>
<div class="funfact">🌗 It didn't have to be this way — and elsewhere, it isn't. From Mars, the little moon Phobos covers barely a third of the Sun: its "eclipses" are a fast, unimpressive potato-shaped shadow. Of all the hundreds of moons in the solar system, ours is the one that fits.</div>
<div class="funfact">🎲 Bonus coincidence, completely unrelated: the Sun also happens to be about <b>109 Earths</b> wide. Different measurement, same number. The universe apparently likes 109 — and no, nobody knows why. Coincidences don't need reasons.</div>""",
            cps=[dict(
                type="num",
                kicker="How much wider?",
                q="""Sun: about <b>1,400,000 km</b> across. Moon: about <b>3,500 km</b> across. How many times wider is the Sun?""",
                answers=[400], unit="times wider",
                hint="1,400,000 ÷ 3,500. Try covering matching zeros: 1,400,000 ÷ 3,500 is the same as 1,400 ÷ 3.5.",
            ), dict(
                type="num",
                kicker="Measure the Moon in Moons",
                q="""The Moon sits about <b>385,000 km</b> away and is <b>3,500 km</b> wide. How many of its own widths away is the Moon?""",
                answers=[110], unit="Moon-widths",
                hint="385,000 ÷ 3,500. Drop matching zeros: 385 ÷ 3.5 — same as 770 ÷ 7.",
            ), dict(
                type="num",
                kicker="Measure the Sun in Suns",
                q="""The Sun sits about <b>150,000,000 km</b> away and is <b>1,400,000 km</b> wide. How many of its own widths away is the Sun? (Round to a whole number — then compare with your Moon answer.)""",
                answers=[107, 108], unit="Sun-widths",
                hint="150,000,000 ÷ 1,400,000. Drop five zeros from each: 1,500 ÷ 14 ≈ 107. Practically the same as the Moon's 110 — THAT is the great coincidence, in one number.",
            )],
        ),
        dict(
            kicker="Chapter Three · Both orbits are ovals",
            title="Your Own Sky Simulator",
            html="""
<p>"About the same size" hides one more layer of the story — because <b>nothing in the sky moves in a perfect circle</b>. The Earth's path around the Sun is a slight oval: in early January we're at <b>perihelion</b> (closest, 147.1 million km) and in early July at <b>aphelion</b> (farthest, 152.1 million km) — so the Sun's disc quietly swells and shrinks by a few percent over the year. The Moon's orbit is a stronger oval: at <b>perigee</b> it comes within about 356,500 km, and at <b>apogee</b> it drifts out to about 406,700 km — a difference you can actually photograph.</p>
<p>So the two half-degree discs are forever wobbling past each other in size — sometimes the Moon's disc is a whisker bigger than the Sun's, sometimes a whisker smaller. Play with the real numbers below. Drag both sliders to their extremes and watch what kind of eclipse each combination would produce.</p>
""" + SKY_SIM + """
<p>Notice how <i>close</i> the contest always is — the discs never differ by more than a few arcminutes. That knife-edge is the whole coincidence, live on your screen.</p>""",
            cps=[dict(
                type="mc",
                kicker="Read your simulator like an astronomer",
                q="""An <b>annular</b> eclipse — the "ring of fire," where the Moon sits inside the Sun's disc leaving a blazing circle — is <i>guaranteed</i> by which combination of extremes?""",
                mc=[("Moon at apogee (farthest) + Earth at perihelion (Sun closest): smallest Moon against the biggest Sun", True),
                    ("Moon at perigee (closest) + Earth at aphelion (Sun farthest): biggest Moon against the smallest Sun", False),
                    ("The combination doesn't matter — eclipses are all alike", False)],
                good="Exactly, {name}. Farthest Moon = smallest Moon-disc; closest Sun = biggest Sun-disc; the Moon can't cover it, and a ring of fire remains. Flip both extremes and you get the longest, darkest total eclipses instead.",
                bad="Go back to the sliders and push them to the extremes — which combination makes the dark disc SMALLER than the bright one?",
            )],
        ),
        dict(
            kicker="Chapter Four · The knife-edge shadow",
            title="Just Barely Reaching",
            html="""
<p>Here's another way to feel how absurdly fine the balance is. The Moon casts a cone of darkness — its <b>umbra</b> — stretching away behind it like a wizard's hat, about <b>375,000 km</b> long. For a total eclipse, the <i>tip of that cone</i> has to physically touch the Earth's surface. Compare that to the Moon's distance and you'll see the truth: the shadow of the Moon <b>just barely reaches us</b>. When the Moon is near apogee, the cone runs out of length in empty space, the tip never lands — and watchers below see a ring instead of darkness.</p>
<p>When the tip <i>does</i> land, you get the greatest free show in nature. The sky goes purple-black in the middle of the day. Stars come out. The temperature drops. Animals fall silent, birds go to roost. And around the black disc blazes the <b>corona</b> — the Sun's outer atmosphere, a ghostly white crown of streamers — which is <i>only visible from Earth during totality</i>, because the coincidence trims the Sun's blinding face away exactly, and not one arcminute more. Astronomers spent centuries scheduling expeditions around those few minutes: the corona, the Sun's chemistry, and — in 1919 — a famous test of how much the Sun's gravity bends starlight, were all captured inside the Moon's knife-edge shadow.</p>""",
            cps=[dict(
                type="num",
                kicker="Does the shadow land?",
                q="""The Moon's shadow-cone is about <b>375,000 km</b> long. At perigee the Moon is about <b>357,000 km</b> away. The tip reaches Earth with how many kilometers to spare?""",
                answers=[18000], unit="km",
                hint="375,000 − 357,000. (Only about 18,000 km of slack — that's barely more than the Earth itself is wide. A knife-edge in cosmic terms.)",
            )],
        ),
        dict(
            kicker="Chapter Five · The clock is running",
            title="Enjoy It While It Lasts",
            html="""
<p>One more twist: the coincidence has an <b>expiration date</b>. When the Apollo astronauts visited the Moon, they left behind racks of special mirrors. Ever since, observatories on Earth have fired lasers at those mirrors and timed the reflection — measuring the Moon's distance to within millimeters. The verdict is unambiguous: <b>the Moon is drifting away from us at about 3.8 centimeters per year</b> — roughly the speed your fingernails grow.</p>
<p>It sounds like nothing. But the sky plays long games. Run the clock backwards and the Moon looms larger: in the deep past, eclipses were longer and blacker, with no ring of fire possible at all. Run it forward, and the Moon's disc keeps shrinking until — around <b>600 million years</b> from now — even a perigee Moon at aphelion Sun won't cover the disc. On that day the last total solar eclipse in Earth's history will end, the corona will take its final bow, and every eclipse afterward, forever, will be a ring.</p>
<p>Think about what that means. This perfect fit isn't a permanent feature of the sky. It's a <b>moment</b> — a few hundred million years wide, in a story billions of years long — and intelligent eyes opened on this planet just in time to catch it.</p>""",
            cps=[dict(
                type="num",
                kicker="The long goodbye — a real astronomer's conversion",
                q="""The Moon retreats about <b>3.8 cm per year</b>. In <b>100 million years</b>, how many <b>kilometers</b> farther away will it be? (Work in steps: centimeters first, then convert — 100,000 cm make 1 km.)""",
                answers=[3800], unit="km",
                hint="3.8 cm × 100,000,000 years = 380,000,000 cm. Now divide by 100,000 to reach kilometers.",
            )],
        ),
    ],
)
