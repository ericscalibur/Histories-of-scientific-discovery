# -*- coding: utf-8 -*-
"""Story data: Isaac Newton."""

NEWTON = dict(
    title="The Apple and the Moon — Isaac Newton",
    h1="✦ The Apple and the Moon ✦",
    sub="Isaac Newton, the plague year, and the force that runs the universe · 1642–1727",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(the apple is real; the bonk on the head is not)",
    praise=["Perfectly calculated, {name}!", "Trinity College would take you on the spot, {name}!",
            "Exactly right, natural philosopher!", "Sharp as a Woolsthorpe prism!",
            "{name}, Halley would publish that answer!"],
    cert_org="Trinity College, Cambridge · Woolsthorpe Manor",
    cert_of="the tale of Isaac Newton",
    cert_rank="Fellow of the Royal Society, Apprentice Class",
    finale_title="On the Shoulders of Giants",
    finale_html="""
<p>Newton once wrote to a rival: <i>"If I have seen further, it is by standing on the shoulders of giants."</i> You have now met the giants he meant. <b>Tycho</b> measured the sky like nobody before him. <b>Kepler</b> found the three laws hiding in Tycho's numbers. And <b>Newton</b> explained why those laws are true — one force, one set of rules, from a falling apple to the farthest planet. Three lifetimes, one relay race, and the baton was always the same thing: <b>honest measurement, honestly reasoned about</b>.</p>
<p>He died in 1727, famous beyond any scientist who had ever lived, and was buried like a king in Westminster Abbey. He was also — say it plainly — a strange and difficult man: secretive, jealous in his feuds, obsessed with alchemy and hidden codes. Genius is not sainthood. Near the end he described himself as a boy playing on the seashore, finding a smoother pebble now and then, <i>"whilst the great ocean of truth lay all undiscovered before me."</i></p>
<p>Two hundred years later, an eclipse expedition proved that even Newton's gravity was only <i>almost</i> right — Einstein saw deeper, exactly the way Newton had seen deeper than Kepler. That's not a defeat. That's the system working. There is always more ocean.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① <b>First Law:</b> things keep doing what they're doing unless a force acts on them.</p>
<p>② <b>Second Law:</b> force = mass × acceleration — the recipe connecting push, stuff, and speed-up.</p>
<p>③ <b>Third Law:</b> every push gets an equal push back, in the opposite direction.</p>
<p>④ And <b>one universal gravity</b>, weakening with the square of distance, runs the apple, the Moon, and every world Kepler ever mapped.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Woolsthorpe, England · Christmas 1642",
            title="The Christmas Boy",
            html="""
<p>In the same year the old, blind Galileo died under house arrest in Italy, a farm widow in Lincolnshire, England had a baby on Christmas morning — so small and so early that his mother said he could have fit inside a quart mug, and so weak that two women sent to fetch supplies didn't hurry back, certain he'd be dead before they returned. His father — a farmer who could not sign his own name — had died three months before he was born. The baby's name was <b>Isaac Newton</b>. He lived to be 84 and changed the universe.</p>
<p>His childhood was lonely in ways that marked him forever. When Isaac was three, his mother married a rich old minister who wanted her but not her son — Isaac was left behind at the farmhouse with his grandmother. He grew into a strange, quiet, furiously clever boy: he built water clocks, sundials so accurate the neighbors set their days by them, kites carrying lanterns at night (which terrified the countryside), and a working model windmill powered by a mouse he called the miller.</p>
<p>At sixteen his mother — widowed again — pulled him out of school to run the family farm. He was magnificently terrible at it. Sheep wandered into neighbors' fields while Isaac read books under hedges and built models in the barn. His uncle and his old schoolmaster staged a rescue: this boy must go to <b>Cambridge</b>. In 1661 he enrolled at Trinity College as a "subsizar" — a poor student who paid his way by serving meals to richer ones.</p>
<div class="funfact">📅 Astronomy's torch relay, in dates: Tycho died in 1601 holding the data. Kepler died in 1630 holding the laws. Galileo died in 1642 holding the telescope. And that Christmas, Newton arrived to pick everything up.</div>""",
            cps=[dict(
                type="num",
                kicker="The torch relay",
                q="""Kepler died in <b>1630</b>, his three laws written but unexplained. Newton was born in <b>1642</b>. How many years did the laws wait between the man who found them and the birth of the man who would prove them?""",
                answers=[12], unit="years",
                hint="1642 − 1630.",
            )],
        ),
        dict(
            kicker="Chapter Two · 1665–1666",
            title="The Year of Wonders",
            html="""
<p>In 1665, death came to England. The <b>Great Plague</b> tore through London, killing on a scale almost impossible to imagine — roughly <b>100,000 people</b> in a city of about <b>400,000</b>. Fleas, rats, quarantine crosses painted on doors. Cambridge University did the only sensible thing: it closed, and sent everyone home.</p>
<p>So a 23-year-old scholarship student packed his books and rode back to the farmhouse where he was born. He stayed at Woolsthorpe, on and off, for about eighteen months — no professors, no classes, no one to talk to. Just a farmhouse, an orchard, and the most dangerous thing in the world: <b>an unsupervised Newton with nothing but time</b>.</p>
<p>In those eighteen months, alone, he: bought a glass prism at a country fair and discovered that white sunlight is <b>all the colors mixed together</b>; invented a completely new branch of mathematics; and asked the question about the apple and the Moon that this story is named for. Scientists still call 1666 the <i>annus mirabilis</i> — the year of wonders. Newton said later of that time: "I was in the prime of my age for invention, and minded mathematics and philosophy more than at any time since."</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> The greatest year in the history of science happened to a student locked out of school, bored, at his mum's farm. Empty time isn't empty — it's where long thoughts finally fit.</div>""",
            cps=[dict(
                type="num",
                kicker="Plague arithmetic",
                q="""London held about <b>400,000</b> people; the plague killed about <b>100,000</b> of them. That's one person out of every…?""",
                answers=[4], unit="people",
                hint="How many 100,000s fit into 400,000?",
            )],
        ),
        dict(
            kicker="Chapter Three · The orchard at Woolsthorpe · 1666",
            title="The Apple",
            html="""
<p>Yes — the apple is real. Newton told the story himself, as an old man, to his friend William Stukeley over tea <i>under apple trees</i>: the idea of gravity came to him "occasioned by the fall of an apple, as he sat in a contemplative mood." (The apple bonking him on the head? Invented later. You now know to check.)</p>
<p>Here is what made it genius. Everyone had seen apples fall. Newton asked the childish question seriously: why does it fall <b>straight down</b> — never sideways, never up — always toward the <i>center</i> of the Earth? And if this pulling power reaches from the ground to the top of the tree… does it reach the mountaintops? Does it reach the clouds? How high does it go? And then the thought that changed everything:</p>
<p style="text-align:center; font-size:1.12rem;"><i>"Could it be that the force that pulls the apple to the ground is the very same force that holds the Moon in orbit around the Earth?"</i></p>
<p>It sounds absurd — the heavens were still supposed to run on different rules than the dirty Earth (some habits of thought survived even Tycho's broken crystal spheres). But Newton could <b>test it</b>. He guessed the pull weakens with the <b>square of the distance</b>: twice as far, four times weaker; ten times as far, a hundred times weaker. The apple hangs about one Earth-radius from the Earth's center. The Moon orbits about <b>60 Earth-radii</b> out. So gravity out at the Moon should be weaker by 60 × 60…</p>""",
            cps=[dict(
                type="num",
                kicker="Newton's Moon test — do his actual calculation",
                q="""If gravity weakens with the <b>square</b> of distance, and the Moon is <b>60 times</b> farther from Earth's center than the apple, gravity at the Moon is how many times weaker?""",
                answers=[3600], unit="times weaker",
                hint="60 × 60. (6 × 6, then bring back both zeros.)",
            ), dict(
                type="mc",
                kicker="So why doesn't the Moon crash?",
                q="""Newton checked the numbers: a falling apple drops about <b>5 meters</b> in its first second. Gravity 3,600× weaker should make the Moon "fall" about 1.4 <i>millimeters</i> every second — and when he computed the Moon's actual path, it curves toward Earth by <b>almost exactly that much</b>. He said the numbers answered "pretty nearly." But wait — if the Moon is falling toward us every second, why doesn't it ever arrive?""",
                mc=[("Gravity is too weak to ever pull it all the way in", False),
                    ("It falls — but it moves sideways so fast it keeps missing the Earth", True),
                    ("There is no gravity in space", False)],
                good="Exactly. The Moon falls 1.4 mm toward Earth every second — while also flying about a kilometer sideways. So the ground curves away beneath it as fast as it falls. An orbit is just falling forever and missing forever. (Astronauts float for the same reason: they're not beyond gravity — they're falling around the Earth.)",
                bad="Careful — Newton's whole point was that gravity DOES reach the Moon, and the Moon IS falling. The question is what its sideways motion does to that fall…",
            )],
        ),
        dict(
            kicker="Chapter Four · Also 1666, same farmhouse",
            title="“Guess I'll Invent Calculus”",
            html="""
<p>There was a problem with checking the apple-Moon idea properly: <b>the mathematics he needed did not exist.</b> A falling apple doesn't move at one tidy speed — it moves faster every instant. The Moon's direction changes every instant. All the math of the day handled frozen, unchanging things: triangles, circles, fixed distances. Nobody had math for <i>things in the middle of changing</i>.</p>
<p>So — pause and appreciate the audacity of a 23-year-old alone at a farm — he invented it. He called it the method of <b>fluxions</b>, because it handled things in flux; today we call it <b>calculus</b>, and it is the mathematics of change itself: every rocket launch, every weather forecast, every curve of every bridge runs on it. He scribbled it into notebooks and then, being Newton, <b>told almost no one for decades</b> — which later ignited a lifelong feud with the German mathematician Leibniz, who invented calculus independently. (Historians' verdict: both invented it; Newton was first; Leibniz published first; both behaved badly.)</p>
<p>Calculus grew from patterns like this one, which Galileo had spotted by rolling balls down ramps. A falling object covers more distance each second, and the total falls into a beautiful rhythm — the running total is always <b>5 × (seconds × seconds)</b>:</p>
<p style="text-align:center; font-size:1.1rem;">after 1 second: <b>5 m</b> · after 2 seconds: <b>20 m</b> · after 3 seconds: <b>45 m</b> · after 4 seconds: <b>?</b></p>
<div class="bigidea">🌟 <b>Big Idea #2:</b> When the tool you need doesn't exist, a scientist's move is to build the tool. Tycho built instruments. Kepler built new astronomy. Newton built new <i>mathematics</i>.</div>""",
            cps=[dict(
                type="num",
                kicker="Think in Galileo's pattern",
                q="""A dropped stone has fallen <b>5 m</b> after 1 second, <b>20 m</b> after 2 seconds, <b>45 m</b> after 3 seconds — always 5 × (seconds × seconds). How many meters has it fallen after <b>4 seconds</b>?""",
                answers=[80], unit="meters",
                hint="5 × (4 × 4). Check the pattern: 5×1=5 ✓, 5×4=20 ✓, 5×9=45 ✓…",
            )],
        ),
        dict(
            kicker="Chapter Five · London & Cambridge · 1684–1687",
            title="Halley Knocks",
            html="""
<p>Newton went back to Cambridge, became a professor at 26, built the world's first working <b>reflecting telescope</b> (astronomers still use his design), got into a bruising fight about light with a scientist named Robert Hooke, and retreated into his rooms like a hermit — gravity unpublished, calculus unpublished, the greatest discoveries in history sitting in a drawer for <b>eighteen years</b>.</p>
<p>Then, in August 1684, came the knock. In a London coffeehouse, the astronomer <b>Edmond Halley</b> (the comet man — you know him from the transit-of-Venus story) had been arguing with Hooke and Christopher Wren: what path would a planet follow if the Sun pulled on it with a force weakening as the square of distance? Nobody could prove it. So Halley rode to Cambridge and put the question to the strange professor. Newton answered instantly: <b>"An ellipse."</b> How could he know? <b>"I have calculated it."</b></p>
<p>Sit with that. Kepler had found the ellipse in Tycho's data 75 years earlier but could never say <i>why</i>. Newton had <b>proven why</b> — gravity plus his laws of motion <i>force</i> planets into ellipses, sweeping equal areas, obeying T × T = a × a × a. All three of Kepler's laws tumble out of one law of gravity, like harvest from a single seed. And he'd been sitting on it.</p>
<p>Halley — history's greatest scientific midwife — begged, flattered, and organized until Newton wrote it all down properly: eighteen months of furious work that became the <b><i>Principia Mathematica</i></b> (1687), probably the most important science book ever printed. Final twist: the Royal Society had blown its publishing budget on a lavish flop called <i>The History of Fishes</i> — so Halley, who wasn't rich, <b>paid for the printing himself</b>.</p>
<div class="bigidea">🌟 <b>Big Idea #3:</b> "I have calculated it" — four words that separate science from opinion. A claim is cheap. The calculation is the receipt. (And notice: without a friend who knocked, nagged, and paid the printer, the receipt might have stayed in the drawer. Science is a team sport, even for hermits.)</div>""",
            cps=[dict(
                type="num",
                kicker="The idea in the drawer",
                q="""Newton had the apple-and-Moon insight in <b>1666</b>. The <i>Principia</i> finally published it in <b>1687</b>. How many years did the answer to the universe sit in a drawer?""",
                answers=[21], unit="years",
                hint="1687 − 1666.",
            )],
        ),
        dict(
            kicker="Chapter Six · From the Principia · The rules of all motion",
            title="Newton's Three Laws",
            html="""
<p>The <i>Principia</i> opens with three laws — not about planets or apples, but about <b>everything that moves</b>. Skateboards, cannonballs, comets, you. Astronomers memorize Kepler's three; the whole rest of physics memorizes these:</p>
<div class="bigidea">⚖️ <b>FIRST LAW (inertia):</b> A thing keeps doing exactly what it's doing — sitting still, or gliding straight at steady speed — unless a <b>force</b> acts on it.</div>""",
            cps=[dict(
                type="num",
                kicker="Use the First Law",
                q="""A hockey puck glides across perfectly frictionless ice in a straight line at a steady speed. How many newtons of force are needed to <b>keep it moving</b> exactly like that? <i>(Careful — this tests whether you believe the law!)</i>""",
                answers=[0], unit="newtons",
                hint="Read the law again: no force is needed to KEEP moving — force is only needed to CHANGE motion. That's why planets coast around the Sun forever without engines.",
            )],
        ),
        dict(
            kicker="Chapter Six & a half · The second and third laws",
            title="Push, Mass, and Push-Back",
            html="""
<div class="bigidea">⚖️ <b>SECOND LAW:</b> Force = mass × acceleration (<b>F = m × a</b>). The harder you push, the faster something speeds up; the heavier it is, the more force the same speed-up costs. Force is measured in <b>newtons</b> — yes, they named the unit after him.</div>
<p>One law, three knobs: know any two of force, mass, and acceleration, and the third has nowhere to hide. This is the equation NASA uses to size rocket engines — literally this one.</p>""",
            cps=[dict(
                type="num",
                kicker="Use the Second Law",
                q="""A go-kart with a mass of <b>6</b> (in mass units, kilograms) needs to accelerate at <b>5</b> (meters per second, every second) to win the race. How many <b>newtons</b> of force must its motor push with? (F = m × a)""",
                answers=[30], unit="newtons",
                hint="6 × 5.",
            ), dict(
                type="num",
                kicker="Use the Third Law",
                q="""<b>THIRD LAW:</b> for every action there is an equal and opposite reaction — every push gets pushed back, exactly as hard, the other way. An astronaut floating in the space station pushes on the wall with <b>40 newtons</b>. How many newtons does the wall push back on her (sending her gliding across the module)?""",
                answers=[40], unit="newtons",
                hint="EQUAL and opposite. This is also how rockets work: the engine throws hot gas down, the gas pushes the rocket up — exactly as hard. A rocket doesn't push against the air; it pushes against its own exhaust, which is why it works in empty space.",
            )],
        ),
        dict(
            kicker="Chapter Seven · The punchline of the whole series",
            title="One Law to Rule the Sky",
            html="""
<p>Now the finale of the argument that began with Tycho's shattered crystal spheres. Newton's gravity is <b>universal</b>: the same force, following the same rule, everywhere. The apple. The Moon. Every planet Kepler mapped. The comet of 1577. Halley used these very laws to predict his comet's return, 53 years ahead — dead on time. There is no separate physics for the heavens. There is just physics.</p>
<p>And the rule is the one you tested in the orchard: gravity weakens with the <b>square</b> of the distance. Twice as far → 2 × 2 = 4 times weaker. The Moon, 60 times farther → 3,600 times weaker. It never reaches zero — the apple pulls on the Moon, and you, right now, are very gently tugging on Jupiter.</p>
<div class="bigidea">🌟 <b>Big Idea #4:</b> "Universal" is the most radical word in science. One set of rules for palace and farmhouse, Earth and heaven, apple and galaxy — no exceptions, no permission slips, and anyone with mathematics can check the rules for themselves.</div>""",
            cps=[dict(
                type="num",
                kicker="The inverse-square rule, one more time",
                q="""A space probe triples its distance from the Sun — it's now <b>3 times</b> farther away. By how many times has the Sun's gravity on it grown weaker?""",
                answers=[9], unit="times weaker",
                hint="Square it: 3 × 3.",
            )],
        ),
    ],
)
