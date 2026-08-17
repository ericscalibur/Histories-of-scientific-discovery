# -*- coding: utf-8 -*-
"""Story data: Plato & Aristotle."""

PLATO_ARISTOTLE = dict(
    title="The School of Athens — Plato & Aristotle",
    h1="✦ The School of Athens ✦",
    sub="Plato, Aristotle, and the birth of thinking about thinking · Athens, 427–322 BC",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(the cave is a story Plato told on purpose — that's what makes it a thought experiment)",
    praise=["Flawlessly reasoned, {name}!", "The Academy would carve that over the door, {name}!",
            "Exactly right, philosopher!", "{name}, Aristotle would write that down!",
            "Logic accepts your answer, {name}!"],
    cert_org="The Academy of Athens · The Lyceum",
    cert_of="the tale of Plato & Aristotle",
    cert_rank="Philosopher of Nature, First Class",
    finale_title="The Mother of Science",
    finale_html="""
<p>Everything science has done in the twenty-three centuries since — every careful measurement of the sky, every law found hiding in the numbers, every theory forced to face the evidence — has happened inside a workshop that these two men built. <b>Plato</b> supplied the faith that the world runs on mathematics, and that patient thinking can climb out of the cave. <b>Aristotle</b> supplied the other half: <i>go and look</i>. Collect, compare, classify, and reason by rules that anyone can check. Science wasn't born yet — but its two parents had met.</p>
<p>For centuries, what we call science was simply named <b>natural philosophy</b> — philosophy aimed at nature. When Newton published the greatest science book ever written, he titled it <i>Mathematical Principles of Natural Philosophy</i>. The word "scientist" wasn't even invented until 1833. So what's the difference? A <b>philosopher</b> asks the deepest questions and reasons carefully about them. A <b>scientist</b> does that too — and then makes nature answer, with experiments and measurements that anyone can repeat. A philosopher can argue forever. A measurement ends the argument.</p>
<p>And the thought experiment — the laboratory that runs inside your head, which Plato's cave opened for business — never closed. Galileo used one to break Aristotle's law of falling. Newton fired an imaginary cannonball into orbit. Einstein chased a beam of light. Every one of them was doing what a barefoot Athenian did first: <i>thinking about thinking, on purpose</i>.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① <b>Plato's Forms:</b> the perfect circle exists nowhere you can point — yet mathematics lets you reason about it exactly. Math is the ladder out of the cave.</p>
<p>② <b>Aristotle's move:</b> truth doesn't live behind the world; it lives <i>in</i> it. Go look. Collect. Compare. Classify.</p>
<p>③ <b>Logic:</b> an argument is a machine — if the parts are true and the machine is built right, the conclusion is guaranteed. If not, it's just noise that sounds confident.</p>
<p>④ <b>The thought experiment:</b> a laboratory in your head — and the warning that even a genius's untested "obvious" idea can be wrong for 2,000 years.</p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Athens · 399 BC",
            title="The Death That Started It",
            html="""
<p>This story begins with an execution. In 399 BC, the city of Athens put an old man on trial. His crime, roughly: <b>asking too many questions</b>. His name was <b>Socrates</b>, and he had spent his life wandering the market square, asking generals what courage really was, and priests what goodness really was — until the important men of Athens discovered they couldn't answer. A jury voted, and Socrates was handed a cup of hemlock poison. He drank it, calmly, still talking philosophy with his friends.</p>
<p>Watching all this was his student — a broad-shouldered 28-year-old wrestler from a rich family, nicknamed <b>Plato</b> ("Broady," probably for those shoulders). The lesson Plato took from the poison cup shaped everything after: a city can vote to kill a man, but that doesn't make the man wrong. <b>Truth is not decided by the crowd.</b> So where <i>is</i> it decided?</p>
<p>Around 387 BC, Plato bought a grove of olive trees outside Athens and founded something the world had never seen: a permanent school for pure thinking, named after the grove — the <b>Academy</b>. (Every "academy" since, including the word itself, is that olive grove echoing.) Legend says a warning was carved over its door: <i>"Let no one ignorant of geometry enter here."</i></p>
<div class="funfact">📅 Careful — BC years count <b>backwards</b>: 399 BC came <i>before</i> 387 BC. The number gets smaller as time moves forward, until it hits 1 BC and flips to AD. It's like a rocket countdown before the launch.</div>""",
            cps=[dict(
                type="num",
                kicker="Countdown arithmetic",
                q="""Socrates drank the hemlock in <b>399 BC</b>. Plato founded the Academy in <b>387 BC</b>. How many years passed in between?""",
                answers=[12], unit="years",
                hint="BC counts down: 399 − 387.",
            )],
        ),
        dict(
            kicker="Chapter Two · The Academy · about 387 BC",
            title="The World Behind the World",
            html="""
<p>Here is Plato's big idea — maybe the biggest "what if" ever asked. Take a compass and draw a circle. Look closely: the line wobbles. Zoom in and it's worse — bumpy ink on rough paper. In fact, <b>no one in history has ever seen a perfect circle</b>. Not one exists anywhere on Earth. And yet — you know <i>exactly</i> what a perfect circle is. You can reason about it, calculate with it, prove things about it that are true forever.</p>
<p>So Plato asked: if the perfect circle isn't <i>here</i>… where is it? His answer: there is a world behind the world — a realm of perfect <b>Forms</b> — and everything we see is a rough, wobbly copy of it. Every drawn circle is a shadow of <i>the</i> Circle. Every act of kindness, a shadow of Goodness itself. And mathematics? Mathematics is the <b>ladder</b> — the one human activity that climbs past the wobbly copies and touches the perfect things directly. That's why geometry guarded the Academy's door.</p>
<p>Plato especially loved five shapes — the only five solids whose faces are all identical perfect shapes: the pyramid-like <b>tetrahedron</b> (4 triangle faces), the <b>cube</b> (6 squares), the <b>octahedron</b> (8 triangles), the <b>dodecahedron</b> (12 pentagons), and the <b>icosahedron</b> (20 triangles). We still call them the <b>Platonic solids</b>. He matched them to fire, earth, air, water, and the cosmos itself — and two thousand years later, young Johannes Kepler was still so enchanted that he tried to build the solar system out of them.</p>
<p>One warning, though, hidden in a puzzle Plato wrote down. A student is asked: take a square, and build a new square with <b>double the area</b>. Easy, says the student — double the side! Plato's point: the "obvious" answer, unchecked, is a trap. Try it yourself below.</p>""",
            cps=[dict(
                type="num",
                kicker="Plato's trap (from his dialogue Meno)",
                q="""A square courtyard is 5 × 5 = <b>25</b> square meters. To double the area to 50, a student doubles the side to 10. What area does a 10 × 10 square actually have?""",
                answers=[100], unit="square meters",
                hint="10 × 10. Notice: doubling the side didn't double the area — it quadrupled it!",
            ), dict(
                type="num",
                kicker="A perfect-shape secret Plato never knew",
                q="""Count on a cube: <b>8</b> corners, <b>12</b> edges, <b>6</b> faces. Now compute corners − edges + faces: 8 − 12 + 6 = ? (Here's the magic: you get the same answer for ALL five Platonic solids — a secret only discovered 2,000 years later.)""",
                answers=[2], unit="",
                hint="8 − 12 is −4. Then −4 + 6.",
            )],
        ),
        dict(
            kicker="Chapter Three · A story Plato told · from his book The Republic",
            title="The Cave",
            html="""
<p>To explain what learning <i>feels</i> like, Plato told a story — the most famous story in the history of philosophy. Imagine prisoners chained in a cave since birth, facing a blank wall. Behind them burns a fire, and between the fire and their backs, people carry objects whose <b>shadows</b> fall on the wall. The prisoners have never seen anything else. For them, the shadows aren't <i>like</i> reality — the shadows <b>are</b> reality. They give the shadows names. They hold contests in shadow-guessing, with prizes.</p>
<p>Now one prisoner is unchained. He turns — and the firelight stabs his eyes. Dragged up out of the cave, he's blinded by the sun; it <i>hurts</i>. But slowly his eyes adjust, and he sees trees, water, stars — and finally understands the shadows were only copies of copies. Then comes Plato's cruelest twist: the freed prisoner goes back down to tell the others… and they think he's gone mad. His eyes, ruined by the light, are now bad at the shadow-guessing game. And Plato — who watched Athens hand his teacher the poison cup — has the prisoners say that anyone who tries to unchain them <b>deserves to die</b>.</p>
<p>Notice what Plato just did. He didn't run an experiment. He built an imaginary world, set the rules, and let it run — to test an idea about <i>knowledge itself</i>. There's a name for that: a <b>thought experiment</b> — a laboratory that runs inside your head. It became one of science's most powerful tools. Galileo will use one to topple a 2,000-year-old law. Newton will fire an imaginary cannonball into orbit. Einstein will chase an imaginary beam of light. All of them are borrowing Plato's cave-shaped laboratory.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> Some experiments need no equipment. A thought experiment sets up an imaginary situation with strict rules and asks: <i>what MUST happen?</i> The cave was the first great one — and it's about why learning hurts, and why crowds laugh at people who've seen more.</div>""",
            cps=[dict(
                type="mc",
                kicker="Read the cave like a philosopher",
                q="""In Plato's story, what do the <b>shadows on the wall</b> stand for?""",
                mc=[("The everyday world we see — wobbly copies of deeper truths", True),
                    ("Ghosts that Plato believed lived under Athens", False),
                    ("Bad dreams that go away when you wake up", False)],
                good="Exactly, {name}. The cave is the visible world; the sunlit world above is Plato's realm of perfect Forms; and the painful climb is education itself. You've just read the story the way the Academy did.",
                bad="Remember — Plato told this story on purpose, as a picture of something. What did HE think we're all staring at, mistaking for the full truth?",
            )],
        ),
        dict(
            kicker="Chapter Four · The Academy · 367–347 BC",
            title="The Student Who Argued Back",
            html="""
<p>In 367 BC a seventeen-year-old arrived at the Academy from Stagira, a small town in the north. His father had been a king's doctor; the boy had grown up around medicine, blood, bone, and the stubborn facts of bodies. His name was <b>Aristotle</b>, and he stayed <b>twenty years</b> — Plato is said to have called him "the Mind of the school."</p>
<p>But the Mind argued with the master. Plato taught: truth lives <i>behind</i> the world — turn away from your lying eyes and climb the ladder of pure reason. Aristotle, the doctor's son, couldn't accept it. Where are these perfect Forms? he asked. What work do they do? You learn what a horse is from <b>horses</b> — from this world, the one in front of us: look at it, cut it open, count its teeth, compare, classify. Truth doesn't live behind the world. <b>It lives in it.</b></p>
<p>A saying has been passed down in his name for over two thousand years: <i>"Plato is my friend — but truth is a better friend."</i> He meant no insult. He meant that loyalty to a person, even the greatest teacher alive, must never outrank loyalty to what's true. (Two thousand years later, a stubborn student named Isaac Newton copied a version of that motto into his college notebook.)</p>
<p>In a famous painting of these two, Plato points <b>up</b> — toward the Forms — while Aristotle holds his palm <b>down</b>, toward the ground, as if to say: <i>here</i>. Two hand gestures; two roads to truth. Science would eventually need both.</p>""",
            cps=[dict(
                type="num",
                kicker="The long apprenticeship",
                q="""Aristotle arrived at the Academy in <b>367 BC</b> and stayed until Plato died in <b>347 BC</b>. How many years did the student study with the master?""",
                answers=[20], unit="years",
                hint="BC counts down: 367 − 347.",
            )],
        ),
        dict(
            kicker="Chapter Five · The island of Lesbos · about 345 BC",
            title="The Man Who Looked",
            html="""
<p>After Plato died, Aristotle left Athens and did something no philosopher had ever bothered to do: he went to a lagoon on the island of <b>Lesbos</b>, rolled up his robes, and started pulling things out of the water. For two years he dissected, described, and compared: sea urchins, cuttlefish, sponges, birds, bees. He recorded about <b>500 species</b>. He described how the octopus changes color to vanish against the rocks. He noticed that dolphins breathe air and feed their babies milk — and concluded they belong with the beasts of the land, <b>not with the fish</b>. It took the rest of the world two thousand years to agree.</p>
<p>This was a new kind of thinking: not asking what a perfect animal would be, but cataloguing what animals <i>are</i> — collect, compare, group, and then hunt for the <b>causes</b>. It isn't yet the full scientific method (that needs experiments and measurement — wait for Galileo), but it is its direct ancestor. Every field guide, every museum drawer, every biology class descends from that lagoon.</p>
<p>And when Aristotle aimed that method at the sky, he nailed one of the biggest facts there is: <b>the Earth is a sphere</b>. His proofs still work. Travel south, and new stars climb above the horizon — that only happens on a curved surface. Better: during a lunar eclipse, the Earth's shadow creeps across the Moon, and that shadow is <b>always round, every single time</b>. Educated people have known the Earth is round ever since — Columbus's sailors knew it too, despite what the internet tells you.</p>
<div class="funfact">👑 In 343 BC, King Philip of Macedon hired Aristotle for the most consequential tutoring job in history: teaching his 13-year-old son. The boy grew up to be <b>Alexander the Great</b> — and legend has him sending his old teacher biological specimens from conquered lands as far away as India.</div>""",
            cps=[dict(
                type="mc",
                kicker="Prove the Earth is round from your backyard",
                q="""Aristotle's best proof: in every lunar eclipse, Earth's shadow on the Moon is <b>round</b>. Why does that clinch it? Think about what a flat disc would do.""",
                mc=[("Only a sphere casts a round shadow from every angle — a flat disc caught edge-on would cast a thin line", True),
                    ("Shadows are always round, no matter the object", False),
                    ("Because the Moon is round, the shadow must be too", False)],
                good="Perfect reasoning, {name}. A disc casts a circle only when it's facing you head-on; tilt it and the shadow squashes to an oval, then a line. Eclipse after eclipse, at all hours and angles, the shadow stays a circle. Only a sphere manages that.",
                bad="Careful — test the flat-Earth disc in your head (a thought experiment!). What shadow does a coin cast when you turn it edge-on to the light?",
            )],
        ),
        dict(
            kicker="Chapter Six · The Lyceum, Athens · 335 BC",
            title="The Logic Machine",
            html="""
<p>Back in Athens, Aristotle opened his own school, the <b>Lyceum</b>. He liked to teach while strolling the covered walkways, so his students got nicknamed the <i>peripatetics</i> — "the walkers." And there he built his most astonishing invention. Not a machine of bronze or wood — a machine made of <b>words</b>.</p>
<p>He asked: forget <i>what</i> we're arguing about — what makes an argument itself <b>valid</b>? And he found rules. The most famous pattern goes: <i>All men are mortal. Socrates is a man. Therefore Socrates is mortal.</i> If the first two lines are true, the third is not just likely — it is <b>guaranteed</b>, locked, no escape. He called such a pattern a <b>syllogism</b>, and he catalogued which patterns lock and which only <i>look</i> like they lock. It was the first time a human being wrote down the rules of correct reasoning itself.</p>
<p>That word-machine became the skeleton of every mathematical proof, every courtroom argument, every "if this, then that" a computer executes — the logic gates in the device you're reading this on are that idea, cast in silicon. But the machine has a warning label: <b>it only guarantees the conclusion if the ingredients are true AND the pattern is right</b>. Feed it a broken pattern and it produces confident nonsense.</p>""",
            cps=[dict(
                type="mc",
                kicker="Run the machine — carefully",
                q="""Test this argument in Aristotle's machine: <i>"All fish swim. A dolphin swims. Therefore, a dolphin is a fish."</i> Does the machine accept it?""",
                mc=[("No — 'all fish swim' doesn't mean 'everything that swims is a fish.' The rule only runs one way", True),
                    ("Yes — both facts are true, so the conclusion must be true", False),
                    ("Yes — dolphins are fish", False)],
                good="Locked out, exactly right, {name}. The pattern is broken: swimmers include fish, dolphins, ducks, and you. And remember — Aristotle himself proved dolphins aren't fish, at the lagoon. Logic and observation, working as a team.",
                bad="Watch the direction of the rule, {name}. 'All fish swim' puts fish INSIDE the club of swimmers — it doesn't make every swimmer a fish. (Aristotle himself showed dolphins breathe air and make milk!)",
            )],
        ),
        dict(
            kicker="Chapter Seven · The next 2,000 years",
            title="The Spell of Authority",
            html="""
<p>Aristotle also got things wrong — hugely, spectacularly wrong. He taught that heavy objects fall <b>faster</b> than light ones (drop a boulder and a pebble: <i>obviously</i>, right?). He taught that the heavens are made of a perfect, changeless fifth element, moving in perfect circles — an idea he'd absorbed, ironically, from Plato's love of perfect Forms. He never carefully <i>tested</i> the falling idea. The great apostle of looking… didn't look hard enough.</p>
<p>Here's the strange part: the mistakes aren't the tragedy. The tragedy is what happened next. His books were so brilliant, so complete — logic, biology, physics, astronomy, and more — that later generations stopped treating them as <i>a</i> mind's best attempt and started treating them as <b>the final answer</b>. For centuries in Europe, "<i>Aristotle says so</i>" ended arguments the way a measurement should. The man who said truth outranks any teacher became the teacher no one dared out-truth.</p>
<p>The spell held until people finally re-ran his checks. Two thousand years after Aristotle, an Italian named Galileo tested the falling rule with a thought experiment worthy of Plato. Take a heavy stone and a light stone, chain them together, and <b>drop them from up high</b>. If heavy things really fall faster, then the slow light stone should drag on the chain and make the pair fall <i>slower</i> than the heavy stone alone. But wait — chained together, the two stones are one object <i>heavier</i> than the heavy stone, so the pair should fall <i>faster</i> than it. Slower and faster, at the same time, from one rule: Aristotle's rule fights itself. Then Galileo rolled balls down ramps and timed the truth — everything falls alike. And in those same years, stargazers watching the "changeless" heavens caught them changing: new stars flaring out where no change was allowed, comets sailing clean through the supposedly perfect sky, planets refusing to run in perfect circles. Every one of those discoveries was made the same way, and it is the only way a spell like this ever breaks: <b>somebody checks</b>.</p>
<div class="bigidea">🌟 <b>Big Idea #2:</b> "Plato is my friend — but truth is a better friend." Aristotle said it about his teacher; science had to learn to say it about Aristotle himself. No authority, however great, outranks a careful check. The mark of respect a scientist pays a great mind is to <b>test it</b>.</div>""",
            cps=[dict(
                type="num",
                kicker="How long can an unchecked 'obviously' survive?",
                q="""Aristotle died in <b>322 BC</b>. Galileo timed falling bodies and broke the "heavy falls faster" rule around <b>1600 AD</b>. Add across the BC/AD line: about how many years did the mistake go unchecked?""",
                answers=[1922, 1921, 1900], unit="years",
                hint="Crossing the line, you add: 322 + 1600. (About nineteen centuries!)",
            )],
        ),
    ],
)
