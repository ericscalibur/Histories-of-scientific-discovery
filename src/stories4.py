# -*- coding: utf-8 -*-
"""Story data: Plato & Aristotle."""

PLATO_ARISTOTLE = dict(
    title="The School of Athens — Socrates, Plato & Aristotle",
    h1="✦ The School of Athens ✦",
    sub="Socrates, Plato, Aristotle — and the birth of thinking about thinking · Athens, 470–322 BC",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(the cave is a story Plato told on purpose — that's what makes it a thought experiment;<br>Socrates wrote nothing — every word we have of his was written down by his students)",
    praise=["Flawlessly reasoned, {name}!", "The Academy would carve that over the door, {name}!",
            "Exactly right, philosopher!", "{name}, Aristotle would write that down!",
            "Logic accepts your answer, {name}!",
            "Socrates would have had a follow-up question, {name} — and you'd have had the answer!"],
    cert_org="The Agora · The Academy of Athens · The Lyceum",
    cert_of="the tale of Socrates, Plato & Aristotle",
    cert_rank="Philosopher of Nature, First Class",
    finale_title="The Mother of Science",
    finale_html="""
<p>Everything science has done in the twenty-three centuries since — every careful measurement of the sky, every law found hiding in the numbers, every theory forced to face the evidence — have happened inside a workshop that these three men built. <b>Socrates</b> supplied the tool and the nerve to use it: the question that makes a claim show its work, aimed without flinching at the people least happy to have it aimed at them. <b>Plato</b> supplied the faith that the world runs on mathematics, and that patient thinking can climb out of the cave. <b>Aristotle</b> supplied the other half: <i>go and look</i>. Collect, compare, classify, and reason by rules that anyone can check. Science wasn't born yet — but its family was assembled: the one who asked, the one who reasoned, and the one who went and looked.</p>
<p>For centuries, what we call science was simply named <b>natural philosophy</b> — philosophy aimed at nature. When Newton published the greatest science book ever written, he titled it <i>Mathematical Principles of Natural Philosophy</i>. The word "scientist" wasn't even invented until 1833. So what's the difference? A <b>philosopher</b> asks the deepest questions and reasons carefully about them. A <b>scientist</b> does that too — and then makes nature answer, with experiments and measurements that anyone can repeat. A philosopher can argue forever. A measurement ends the argument.</p>
<p>And the thought experiment — the laboratory that runs inside your head, which Plato's cave opened for business — never closed. Galileo used one to break Aristotle's law of falling. Newton fired an imaginary cannonball into orbit. Einstein chased a beam of light. Every one of them was doing what a barefoot Athenian did first: <i>thinking about thinking, on purpose</i>.</p>
<p>Last of all, remember the boy at Mieza. Alexander took the thinking of Athens to the edge of India, and the empire he built with it lasted barely longer than he did. But the city he left behind on the Nile filled up with books, and with the students of his teacher's students, and in it Euclid wrote down geometry and Eratosthenes measured the Earth. The sword is what everybody remembers. The library is what actually conquered the world.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① <b>Socrates' question:</b> the strongest thing you can say to a confident claim is <i>what exactly do you mean, and how would we know if you were wrong?</i> Knowing that you don't know is where knowing starts.</p>
<p>② <b>Plato's Forms:</b> the perfect circle exists nowhere you can point — yet mathematics lets you reason about it exactly. Math is the ladder out of the cave.</p>
<p>③ <b>Aristotle's move:</b> truth doesn't live behind the world; it lives <i>in</i> it. Go look. Collect. Compare. Classify.</p>
<p>④ <b>Logic:</b> an argument is a machine — if the parts are true and the machine is built right, the conclusion is guaranteed. If not, it's just noise that sounds confident.</p>
<p>⑤ <b>The thought experiment:</b> a laboratory in your head — and the warning that even a genius's untested "obvious" idea can be wrong for 2,000 years.</p>
<p>⑥ <b>The chain:</b> Socrates → Plato → Aristotle → Alexander. The empire broke up within years; the method is still running. Ideas outlast armies.</p>
</div>""",
    quiz=dict(
        title="&#10022; Ten Questions from the Agora to Alexandria &#10022;",
        intro="One attempt per question, the way a jury votes: once. The whole lesson is fair game, from the barefoot man in the market to the boy king in Babylon. Score yourself, then argue with the answers &mdash; Socrates would.",
        verdicts=[
            dict(min=10, title="{score} &mdash; Philosopher of Nature, First Class", text="Not one wobble, {name}. Aristotle would write that down, Plato would carve it over the door, and Socrates would have a follow-up question anyway. Go and ask somebody what they mean."),
            dict(min=7, title="{score} &mdash; The Academy admits you", text="Solid reasoning, {name}. Read the explanations under the ones you missed: every one of them is a place where the obvious answer was a trap, which is the whole point of this lesson."),
            dict(min=4, title="{score} &mdash; Halfway up out of the cave", text="Your eyes are still adjusting to the light, {name}. Wipe the slate, re-read the chapters the missed questions point to, and come back. Plato said learning hurts. He did not say it stops."),
            dict(min=0, title="{score} &mdash; Back to the agora", text="Socrates would say this is the best place to start, {name}: knowing what you don't know yet. Wipe the slate, read again, and this time ask each chapter what it means."),
        ],
        questions=[
            dict(type="mc", kicker="Chapter One &middot; Socrates",
                 q="""Socrates never wrote a book and claimed to know nothing. So what did he actually <i>do</i> all day in the agora?""",
                 mc=[("Asked people to explain what they claimed to know, and kept asking until the claim stood up or fell over", True),
                     ("Gave lectures on the correct answers to the big questions", False),
                     ("Sold written speeches to politicians", False)],
                 why="He sold no answers at all. His tool was the question that makes a claim say exactly what it means, and his method got a name: the elenchus."),
            dict(type="num", kicker="Chapter Two &middot; countdown arithmetic",
                 q="""Plato was <b>28</b> years old when Socrates drank the hemlock in <b>399 BC</b>. In what year was Plato born? (Remember which way BC counts.)""",
                 answers=[427, 428], unit="BC",
                 why="399 + 28 = 427 BC. Going back in time, BC numbers get bigger. Historians say 428 or 427, depending on which month of the Athenian year you trust."),
            dict(type="mc", kicker="Chapter Two &middot; the Academy",
                 q="""Legend says a warning was carved over the door of Plato's Academy. Which one?""",
                 mc=[("Let no one ignorant of geometry enter here", True),
                     ("Plato is my friend, but truth is a better friend", False),
                     ("The unexamined life is not worth living", False)],
                 why="Geometry guarded the door because it was the one subject where the arguing stops: a proof gives no jury a vote. The other two lines belong to Aristotle and to Socrates at his trial."),
            dict(type="num", kicker="Chapter Three &middot; Socrates' trap, again",
                 q="""A square garden is 3 &times; 3 = <b>9</b> square meters. Someone doubles the side to 6 to “double the area.” What area do they actually get?""",
                 answers=[36], unit="square meters",
                 why="6 &times; 6 = 36, which is four times 9, not double. Doubling a side always quadruples the area. Same trap the boy fell into in the Meno, and it works on every square ever drawn."),
            dict(type="num", kicker="Chapter Three &middot; the secret in the solids",
                 q="""On a cube, corners &minus; edges + faces came out to 2. Now try the <b>tetrahedron</b>: it has <b>4</b> corners, <b>6</b> edges and <b>4</b> triangular faces. What do you get?""",
                 answers=[2], unit="",
                 why="4 &minus; 6 + 4 = 2. It comes out 2 for all five Platonic solids, and for any ball-shaped solid at all. Nobody noticed for two thousand years after Plato; Leonhard Euler finally did in the 1700s."),
            dict(type="mc", kicker="Chapter Four &middot; the cave",
                 q="""In Plato's cave, the freed prisoner climbs into the sunlight and then goes back down to tell the others. What happens, and what is Plato pointing at?""",
                 mc=[("They laugh at him, and would kill anyone who tried to unchain them: Plato is describing what Athens did to Socrates", True),
                     ("They follow him out at once: Plato is describing how easy teaching is", False),
                     ("He forgets what he saw: Plato is describing sleep", False)],
                 why="The prisoners' eyes are used to shadows, and the returning man is now bad at the shadow-guessing game. Plato, who watched Athens hand his teacher the poison cup, wrote the prisoners' death threat on purpose."),
            dict(type="mc", kicker="Chapter Five &middot; two hands",
                 q="""In Raphael's painting, Plato points <b>up</b> and Aristotle holds his palm <b>down</b>. Which idea belongs to Aristotle?""",
                 mc=[("Truth lives in the world in front of us: go and look, collect, compare, classify", True),
                     ("Truth lives behind the world, in a realm of perfect Forms, reached by pure reason", False),
                     ("Truth is whatever the crowd votes for", False)],
                 why="Palm down means <i>here</i>. The doctor's son learned what a horse is from horses. The Forms were Plato's road, and the crowd's vote was exactly what both of them had learned not to trust."),
            dict(type="mc", kicker="Chapter Seven &middot; the logic machine",
                 q="""Run this through Aristotle's machine: <i>“All birds have feathers. A penguin has feathers. Therefore a penguin is a bird.”</i> Penguins really are birds. Does the machine accept the argument?""",
                 mc=[("No. The rule runs backwards: having feathers doesn't make a thing a bird by this argument, even though the conclusion happens to be true", True),
                     ("Yes. The conclusion is true, so the argument must be valid", False),
                     ("Yes. Both facts are true, so it locks", False)],
                 why="A true conclusion can fall out of a broken argument by luck. “All birds have feathers” puts birds inside the club of feathered things; it doesn't make every feathered thing a bird. Same broken pattern as the dolphin, with a happier ending."),
            dict(type="num", kicker="Chapter Nine &middot; the pupil becomes king",
                 q="""Alexander was born in <b>356 BC</b>. His father Philip was murdered in <b>336 BC</b> and Alexander took the throne. How old was the new king?""",
                 answers=[20], unit="years old",
                 why="356 &minus; 336 = 20. Two years later he crossed into Asia, and eleven years after that he was dead in Babylon at 32."),
            dict(type="mc", kicker="Chapter Nine &middot; check every quote",
                 q="""The lesson calls two things <i>legends</i>: Alexander shipping animal specimens home to Aristotle, and Aristotle's exit line about Athens “sinning twice against philosophy.” What do the two stories have in common?""",
                 mc=[("Both first appear in books written centuries after the events, so nobody can check them", True),
                     ("Both were made up by Plato to make Aristotle look good", False),
                     ("Both are carved on stone in Athens, so they must be true", False)],
                 why="The specimens come from Pliny, nearly four centuries later; the exit line from Aelian, about five. A good story is not evidence. That rule is the one thing every chapter in this lesson agrees on."),
        ],
    ),
    chapters=[        dict(
            kicker="Chapter One · The agora of Athens · about 430 BC",
            title="The Man Who Knew Nothing",
            html="""
<p>Twenty-four centuries ago there was a man in Athens who never wrote a book. Not one page. He owned almost nothing, went barefoot even in winter, and had a face people teased him about &mdash; snub nose, bulging eyes, more like a garden statue of a satyr than a wise man. He had been a soldier, and a brave one: at the battle of Delium the Athenian army broke and ran, and witnesses said he walked off the field so calmly that the enemy decided to leave him alone. His name was <b>Socrates</b>, and his job &mdash; as far as anyone in Athens could tell &mdash; was <b>asking questions</b>.</p>
<p>It started, the story goes, with an oracle. A friend of his named Chaerephon made the trip to the temple of Apollo at <b>Delphi</b> and asked the priestess a question: is anyone wiser than Socrates? The answer came back: <b>no one</b>. Socrates was baffled. He knew perfectly well that he wasn't wise about anything. So he set out to prove the oracle wrong &mdash; by finding somebody wiser.</p>
<p>He went to the politicians. He went to the poets. He went to the craftsmen. And each time he did the same simple thing: he asked them to explain what they claimed to know. What is justice? What is courage? What makes a thing beautiful? And each time, after a few polite questions, the expert's answer came apart in his hands. Socrates went home with a discovery that stung: those men didn't know either &mdash; but they thought they did. <b>He</b> didn't know, and he knew he didn't know. That tiny gap was the whole of his wisdom.</p>
<div class="funfact">📜 The famous line "I know that I know nothing" is a tidied-up version of what Plato actually wrote down. In the <i>Apology</i>, Socrates says something more careful: <i>"What I do not know, I do not think I know."</i> Check every quote &mdash; especially the good ones.</div>
<p>His method got a name &mdash; the <b>elenchus</b>, or simply the <b>Socratic method</b> &mdash; and it is the most useful tool in this entire lesson. He never lectured. He asked you what you believed. Then he asked what that belief would have to mean if it were true. Then he asked about <i>that</i>, and about that, until either the belief stood up on its own legs or collapsed under its own weight. His mother had been a midwife, and he said he did the same job for ideas: he had none of his own to deliver, so he helped other people give birth to theirs &mdash; and then checked whether the newborn idea was healthy.</p>
<p>Notice how strange that is. Everyone before him who claimed to teach wisdom sold <b>answers</b>. Socrates sold nothing and gave no answers at all. What he gave was a <b>procedure</b> &mdash; a way to find out whether an answer is any good. That is why he stands at the front of this lesson, and at the front of Western thinking: not for what he knew, but for what he did to what everyone else claimed to know.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> A question is a tool. <i>What exactly do you mean? How do you know? How would we find out if you were wrong?</i> Those are the three most powerful sentences in science &mdash; and a barefoot man in a market square was the first to use them on purpose, as a method. Every scientist who has ever tested a famous claim is doing what Socrates did in the agora.</div>
<div class="funfact">🗣️ <b>Five questions Socrates went around asking.</b> They are his, out of the dialogues Plato wrote down, put into plain words. No answers here &mdash; that is the whole point. Pick one and sit with it.<br><br>
① A friend lends you his sword. Later he loses his mind and comes back demanding it. Do you hand it over? Being fair means giving people back what is theirs &mdash; doesn't it? <i>(the Republic)</i><br>
② A soldier holds his ground because he has no idea how much danger he is in. Is he brave? <i>(the Laches)</i><br>
③ Which is worse: doing something wrong to somebody, or having somebody do something wrong to you? <i>(the Gorgias &mdash; Socrates picked an answer, and almost nobody agrees with him)</i><br>
④ Can being <i>good</i> be taught, the way geometry is taught? If it can, who teaches it &mdash; and why are there so few good people? <i>(the Meno &mdash; it is the very first line of the book, fired at Socrates the moment he walks in)</i><br>
⑤ Is a thing right because someone important says it is &mdash; or do they say it because it is right? <i>(Socrates asked this about the gods, in the Euthyphro. It works on any authority, and Chapter Eight is going to need it.)</i><br><br>
Watch what happens when you try to answer one. The <b>second</b> question is always harder than the first, and the third is harder still. That is the machine running.</div>
<p>Athens did not love him for it. He did this in public, in the <b>agora</b> &mdash; the market square &mdash; where anybody could stand and watch a respected general fumble a simple question in front of a laughing crowd. The playwright Aristophanes put him in a comedy called <i>The Clouds</i>, dangling in a basket, teaching young men how to argue their way out of paying their debts. And Athens had just lost a long, ruinous war. A city hunting for someone to blame is a dangerous place to be the man who makes important people look foolish.</p>
<p>In <b>399 BC</b> they charged him with two crimes: not believing in the gods of the city, and <b>corrupting the young</b>. That first charge is not the same as calling him an atheist. He said an inner voice &mdash; he called it his <i>daimonion</i> &mdash; warned him off things he was about to do; he took the oracle at Delphi seriously enough to rebuild his life around it; and his friends saw him make sacrifices like anybody else. The complaint was that he did religion his own way, and asked awkward questions about the rest. In court he pointed out that the charge argued with itself: they were accusing him of believing in <b>no</b> gods and of inventing <b>new</b> ones, in the same sentence. A jury of 501 ordinary Athenians heard the case. Socrates refused to grovel. He told them that if they offered to free him on condition that he stop asking questions, he would refuse &mdash; because <i>"the unexamined life is not worth living."</i> Asked to propose his own punishment, he suggested that the city ought to give him free dinners for life, as a public benefactor. The jury voted for death. He drank a cup of poison hemlock in his cell, surrounded by his friends, still doing philosophy, and &mdash; his students wrote &mdash; perfectly calm.</p>
<div class="funfact">⚖️ The first vote was close: roughly <b>280</b> for guilty against <b>221</b> for innocent. Socrates pointed out himself that if just <b>30</b> jurors had voted the other way he would have walked free. Then his free-dinners answer made the jury angrier, and the second vote &mdash; the death vote &mdash; was far more lopsided than the first. He talked himself into the hemlock on purpose. Being right, he thought, mattered more than staying alive.</div>
<p>Every word we have of his was written down by somebody else. Most of it came from one heartbroken 28-year-old who was sitting in that courtroom, and who spent the rest of his life writing conversations in which Socrates asks questions. His name was <b>Plato</b>. Historians still argue about where the real Socrates stops and Plato's Socrates begins. The man who never wrote a page became the most quoted person in philosophy.</p>""",
            cps=[dict(
                type="num",
                kicker="Counting backwards through a life",
                q="""Socrates was born in Athens about <b>470 BC</b> and drank the hemlock in <b>399 BC</b>. Roughly how old was he? (BC years count <i>backwards</i> &mdash; the numbers shrink as time moves forward.)""",
                answers=[71, 70], unit="years old",
                hint="470 &minus; 399.",
            ), dict(
                type="mc",
                kicker="Spot the Socratic move",
                q="""A boy tells you: <i>"Cheetahs are the fastest animals &mdash; everybody knows that."</i> Which reply is the Socratic method at work?""",
                mc=[('"Fastest at what? Running on land, or moving at all &mdash; what about a diving falcon?"', True),
                    ('"No, you are wrong, and here is the correct answer."', False),
                    ('"If everybody knows it, then it must be true."', False)],
                good="That's the move, {name}. Socrates almost never said \u201cyou're wrong.\u201d He asked what the claim actually meant, and let the claim fall apart on its own. (A diving peregrine falcon passes 300 km/h, so the question was worth asking.)",
                bad="Careful &mdash; Socrates gave no answers and won nothing by shouting. His only tool was a question that forces a claim to say exactly what it means. Which reply does that?",
            )],
        ),
        dict(
            kicker="Chapter Two · Athens · 399–387 BC",
            title="The Student Who Never Forgot",
            html="""
<p>Sitting in that courtroom was a broad-shouldered young wrestler from one of the richest families in Athens. His given name may have been Aristocles; everybody called him <b>Plato</b> &mdash; "Broady," probably for those shoulders. He was twenty-eight years old, he had been raised to help govern his city, and he had just watched his city vote to kill his teacher.</p>
<p>The lesson Plato took from the poison cup shaped everything that came after. A city can vote. A crowd can be completely certain. A jury of 501 free citizens can be loud, and legal, and wrong. <b>Truth is not decided by the crowd.</b> But if truth isn't settled by a show of hands &mdash; then where <i>is</i> it settled? That question is the engine of the whole rest of this lesson.</p>
<p>Plato left Athens and travelled for years &mdash; Egypt, southern Italy, Sicily &mdash; and in Italy he fell in with the followers of <b>Pythagoras</b>, who taught that the universe is secretly built out of numbers and ratios. Then, around <b>387 BC</b>, he came home, bought a grove of olive trees outside the city walls, and founded something the world had never had: a permanent school for pure thinking, named after the grove &mdash; the <b>Academy</b>. Every "academy" since, including the word itself, is that olive grove still echoing. It kept teaching, on and off, for centuries.</p>
<p>Legend says a warning was carved over its door: <i>"Let no one ignorant of geometry enter here."</i> Think about where his teacher's questions had ended up &mdash; in a room full of confident opinions and a death sentence. Plato went hunting for a subject where the arguing <b>stops</b>: where a thing can be proved so completely that no jury, no crowd, and no king gets a vote on it. He believed he had found it in mathematics.</p>
<div class="funfact">📅 Careful &mdash; BC years count <b>backwards</b>: 399 BC came <i>before</i> 387 BC. The number gets smaller as time moves forward, until it hits 1 BC and flips to AD. It's like a rocket countdown before the launch.</div>""",
            cps=[dict(
                type="num",
                kicker="Countdown arithmetic",
                q="""Socrates drank the hemlock in <b>399 BC</b>. Plato founded the Academy in <b>387 BC</b>. How many years passed in between?""",
                answers=[12], unit="years",
                hint="BC counts down: 399 − 387.",
            )],
        ),
        dict(
            kicker="Chapter Three · The Academy · about 387 BC",
            title="The World Behind the World",
            html="""
<p>Here is Plato's big idea — maybe the biggest "what if" ever asked. Take a compass and draw a circle. Look closely: the line wobbles. Zoom in and it's worse — bumpy ink on rough paper. In fact, <b>no one in history has ever seen a perfect circle</b>. Not one exists anywhere on Earth. And yet — you know <i>exactly</i> what a perfect circle is. You can reason about it, calculate with it, prove things about it that are true forever.</p>
<p>So Plato asked: if the perfect circle isn't <i>here</i>… where is it? His answer: there is a world behind the world — a realm of perfect <b>Forms</b> — and everything we see is a rough, wobbly copy of it. Every drawn circle is a shadow of <i>the</i> Circle. Every act of kindness, a shadow of Goodness itself. And mathematics? Mathematics is the <b>ladder</b> — the one human activity that climbs past the wobbly copies and touches the perfect things directly. That's why geometry guarded the Academy's door.</p>
<p>Plato especially loved five shapes — the only five solids whose faces are all identical perfect shapes: the pyramid-like <b>tetrahedron</b> (4 triangle faces), the <b>cube</b> (6 squares), the <b>octahedron</b> (8 triangles), the <b>dodecahedron</b> (12 pentagons), and the <b>icosahedron</b> (20 triangles). We still call them the <b>Platonic solids</b>. (Here's a secret none of them knew, and nobody found for another two thousand years: on a cube, count 8 corners, 12 edges, 6 faces, and work out corners − edges + faces. You get 8 − 12 + 6 = <b>2</b>. Try it on any of the other four. You get 2 every single time.) He matched them to fire, earth, air, water, and the cosmos itself — and two thousand years later, young Johannes Kepler was still so enchanted that he tried to build the solar system out of them.</p>
<p>One warning, though, hidden in a puzzle Plato wrote down — and look who is asking the questions. In Plato's dialogue <i>Meno</i>, <b>Socrates</b> takes a boy who has never studied geometry and, using nothing but questions, walks him to a piece of mathematics the boy did not know he had in him. First, though, Socrates lets him fall into a trap. Take a square, the boy is told, and build a new square with <b>double the area</b>. Easy, says the boy — double the side! The point: the "obvious" answer, unchecked, is a trap. Spring it yourself below.</p>""",
            cps=[dict(
                type="num",
                kicker="Socrates' trap (from Plato's dialogue Meno)",
                q="""A square courtyard is 5 × 5 = <b>25</b> square meters. To double the area to 50, the boy doubles the side to 10. What area does a 10 × 10 square actually have?<svg viewBox="0 0 470 262" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A 5 by 5 square of 25 units beside a 10 by 10 square of 100 units, showing that four of the small square fit inside the big one" style="display:block;margin:16px auto 4px;max-width:100%;height:auto;"><g font-family="Georgia,serif" fill="#eef1fb"><rect x="40" y="120" width="80" height="80" fill="rgba(232,169,12,.22)"/><line x1="56" y1="120" x2="56" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="40" y1="136" x2="120" y2="136" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="72" y1="120" x2="72" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="40" y1="152" x2="120" y2="152" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="88" y1="120" x2="88" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="40" y1="168" x2="120" y2="168" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="104" y1="120" x2="104" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="40" y1="184" x2="120" y2="184" stroke="rgba(238,241,251,.30)" stroke-width="1"/><rect x="40" y="120" width="80" height="80" fill="none" stroke="#e8a90c" stroke-width="2.5"/><rect x="210" y="40" width="80" height="80" fill="rgba(232,169,12,.22)"/><rect x="290" y="40" width="80" height="80" fill="rgba(232,169,12,.10)"/><rect x="210" y="120" width="80" height="80" fill="rgba(232,169,12,.10)"/><rect x="290" y="120" width="80" height="80" fill="rgba(232,169,12,.22)"/><line x1="226" y1="40" x2="226" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="56" x2="370" y2="56" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="242" y1="40" x2="242" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="72" x2="370" y2="72" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="258" y1="40" x2="258" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="88" x2="370" y2="88" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="274" y1="40" x2="274" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="104" x2="370" y2="104" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="290" y1="40" x2="290" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="120" x2="370" y2="120" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="306" y1="40" x2="306" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="136" x2="370" y2="136" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="322" y1="40" x2="322" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="152" x2="370" y2="152" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="338" y1="40" x2="338" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="168" x2="370" y2="168" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="354" y1="40" x2="354" y2="200" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="210" y1="184" x2="370" y2="184" stroke="rgba(238,241,251,.30)" stroke-width="1"/><line x1="290" y1="40" x2="290" y2="200" stroke="#e8a90c" stroke-width="2" opacity=".85"/><line x1="210" y1="120" x2="370" y2="120" stroke="#e8a90c" stroke-width="2" opacity=".85"/><rect x="210" y="40" width="160" height="160" fill="none" stroke="#e8a90c" stroke-width="2.5"/><text x="80" y="167" text-anchor="middle" font-size="19" font-weight="bold" fill="#ffd977">25</text><text x="250" y="86" text-anchor="middle" font-size="17" fill="#ffd977" opacity=".95">25</text><text x="330" y="86" text-anchor="middle" font-size="17" fill="#ffd977" opacity=".95">25</text><text x="250" y="166" text-anchor="middle" font-size="17" fill="#ffd977" opacity=".95">25</text><text x="330" y="166" text-anchor="middle" font-size="17" fill="#ffd977" opacity=".95">25</text><text x="165" y="150" text-anchor="middle" font-size="12.5" fill="#c3cdea">double</text><text x="165" y="165" text-anchor="middle" font-size="12.5" fill="#c3cdea">the side</text><line x1="130" y1="178" x2="196" y2="178" stroke="#c3cdea" stroke-width="2"/><path d="M196 178 l-9 -5 v10 z" fill="#c3cdea"/><text x="80" y="226" text-anchor="middle" font-size="15">5 &#215; 5 = <tspan fill="#ffd977" font-weight="bold">25</tspan></text><text x="290" y="226" text-anchor="middle" font-size="15">10 &#215; 10 = <tspan fill="#ffd977" font-weight="bold">100</tspan></text><text x="235" y="252" text-anchor="middle" font-size="13" fill="#c3cdea" font-style="italic">Doubling the side did not double the area. Count the blocks.</text></g></svg>""",
                answers=[100], unit="square meters",
                hint="10 × 10. Notice: doubling the side didn't double the area — it quadrupled it!",
            ), dict(
                type="mc",
                kicker="Now run Plato's circle argument on a square",
                q="""Zoom in far enough on <b>any</b> square anybody has ever made — a floor tile, a window, a chessboard, this one — and something always goes wrong. The sides bow. The corners round off. The line turns out to be made of atoms with gaps between them. So what is Plato's point?""",
                mc=[("The perfect square isn't in the world — it's the thing all the wobbly ones are copies of, and you can reason about it exactly even though nobody has ever seen one", True),
                    ("With better tools — a sharper pencil, a finer machine — we could finally make a perfect one", False),
                    ("Squares aren't real, so geometry is a waste of time", False)],
                good="That's it exactly, {name}. Better tools get you closer forever and never arrive — the gap isn't a workmanship problem, and no machine will ever close it. Now hold the strange part: a shape that nobody has ever seen, touched, or measured is the thing every real square gets measured against. That is what Plato meant by a Form, and why he thought mathematics was the ladder out of the cave.",
                bad="Careful. Plato is not saying geometry is useless — he thinks it's the most useful thing there is. And test the 'better tools' answer with a thought experiment: sharpen the pencil, and the line is still made of atoms. Sharpen it again. How close do you get, and do you ever actually arrive?",
            )],
        ),
        dict(
            kicker="Chapter Four · A story Plato told · from his book The Republic",
            title="The Cave",
            html="""
<p>To explain what learning <i>feels</i> like, Plato told a story — the most famous story in the history of philosophy. Imagine prisoners chained in a cave since birth, facing a blank wall. Behind them burns a fire, and between the fire and their backs, people carry objects whose <b>shadows</b> fall on the wall. The prisoners have never seen anything else. For them, the shadows aren't <i>like</i> reality — the shadows <b>are</b> reality. They give the shadows names. They hold contests in shadow-guessing, with prizes.</p>
<p>Now one prisoner is unchained. He turns — and the firelight stabs his eyes. Dragged up out of the cave, he's blinded by the sun; it <i>hurts</i>. But slowly his eyes adjust, and he sees trees, water, stars — and finally understands the shadows were only copies of copies. Then comes Plato's cruelest twist: the freed prisoner goes back down to tell the others… and they think he's gone mad. His eyes, ruined by the light, are now bad at the shadow-guessing game. And Plato — who watched Athens hand his teacher the poison cup — has the prisoners say that anyone who tries to unchain them <b>deserves to die</b>. Read that line again, and remember who is writing it: Plato has just told you, in a story, exactly how his teacher died.</p>
<p>Notice what Plato just did. He didn't run an experiment. He built an imaginary world, set the rules, and let it run — to test an idea about <i>knowledge itself</i>. There's a name for that: a <b>thought experiment</b> — a laboratory that runs inside your head. It became one of science's most powerful tools. Galileo will use one to topple a 2,000-year-old law. Newton will fire an imaginary cannonball into orbit. Einstein will chase an imaginary beam of light. All of them are borrowing Plato's cave-shaped laboratory.</p>
<div class="bigidea">🌟 <b>Big Idea #2:</b> Some experiments need no equipment. A thought experiment sets up an imaginary situation with strict rules and asks: <i>what MUST happen?</i> The cave was the first great one — and it's about why learning hurts, and why crowds laugh at people who've seen more.</div>""",
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
            kicker="Chapter Five · The Academy · 367–347 BC",
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
            kicker="Chapter Six · The island of Lesbos · about 345 BC",
            title="The Man Who Looked",
            html="""
<p>After Plato died, Aristotle left Athens and did something no philosopher had ever bothered to do: he went to a lagoon on the island of <b>Lesbos</b>, rolled up his robes, and started pulling things out of the water. For two years he dissected, described, and compared: sea urchins, cuttlefish, sponges, birds, bees. He recorded about <b>500 species</b>. He described how the octopus changes color to vanish against the rocks. He noticed that dolphins breathe air and feed their babies milk — and concluded they belong with the beasts of the land, <b>not with the fish</b>. It took the rest of the world two thousand years to agree.</p>
<p>This was a new kind of thinking: not asking what a perfect animal would be, but cataloguing what animals <i>are</i> — collect, compare, group, and then hunt for the <b>causes</b>. It isn't yet the full scientific method (that needs experiments and measurement — wait for Galileo), but it is its direct ancestor. Every field guide, every museum drawer, every biology class descends from that lagoon.</p>
<p>And when Aristotle aimed that method at the sky, he nailed one of the biggest facts there is: <b>the Earth is a sphere</b>. His proofs still work. Travel south, and new stars climb above the horizon — that only happens on a curved surface. Better: during a lunar eclipse, the Earth's shadow creeps across the Moon, and that shadow is <b>always round, every single time</b>. Educated people have known the Earth is round ever since — Columbus's sailors knew it too, despite what the internet tells you.</p>""",
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
            kicker="Chapter Seven · The Lyceum, Athens · 335 BC",
            title="The Logic Machine",
            html="""
<p>Back in Athens, Aristotle opened his own school, the <b>Lyceum</b>. He liked to teach while strolling the covered walkways, so his students got nicknamed the <i>peripatetics</i> — "the walkers." And there he built his most astonishing invention. Not a machine of bronze or wood — a machine made of <b>words</b>.</p>
<p>He asked: forget <i>what</i> we're arguing about — what makes an argument itself <b>valid</b>? And he found rules. The most famous pattern goes: <i>All men are mortal. Socrates is a man. Therefore Socrates is mortal.</i> If the first two lines are true, the third is not just likely — it is <b>guaranteed</b>, locked, no escape. He called such a pattern a <b>syllogism</b>, and he catalogued which patterns lock and which only <i>look</i> like they lock. It was the first time a human being wrote down the rules of correct reasoning itself.</p>
<p>And notice whose name that famous example uses. Aristotle never met Socrates — Socrates drank the hemlock in 399 BC, fifteen years before Aristotle was born. But the man who spent his life taking arguments apart with questions ended up, through his student's student, as the standard test piece for checking whether an argument holds together. (Textbooks have used that particular three-liner for so long that most people assume Aristotle wrote it; he taught the <i>pattern</i>, usually with letters instead of names. Check every caption — including this one.)</p>
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
            kicker="Chapter Eight · The next 2,000 years",
            title="The Spell of Authority",
            html="""
<p>Aristotle also got things wrong — hugely, spectacularly wrong. He taught that heavy objects fall <b>faster</b> than light ones (drop a boulder and a pebble: <i>obviously</i>, right?). He taught that the heavens are made of a perfect, changeless fifth element, moving in perfect circles — an idea he'd absorbed, ironically, from Plato's love of perfect Forms. He never carefully <i>tested</i> the falling idea. The great apostle of looking… didn't look hard enough.</p>
<p>Here's the strange part: the mistakes aren't the tragedy. The tragedy is what happened next. His books were so brilliant, so complete — logic, biology, physics, astronomy, and more — that later generations stopped treating them as <i>a</i> mind's best attempt and started treating them as <b>the final answer</b>. For centuries in Europe, "<i>Aristotle says so</i>" ended arguments the way a measurement should. The man who said truth outranks any teacher became the teacher no one dared out-truth.</p>
<p>The spell held until people finally re-ran his checks. Two thousand years after Aristotle, an Italian named Galileo tested the falling rule with a thought experiment worthy of Plato. Take a heavy stone and a light stone, chain them together, and <b>drop them from up high</b>. If heavy things really fall faster, then the slow light stone should drag on the chain and make the pair fall <i>slower</i> than the heavy stone alone. But wait — chained together, the two stones are one object <i>heavier</i> than the heavy stone, so the pair should fall <i>faster</i> than it. Slower and faster, at the same time, from one rule: Aristotle's rule fights itself. Then Galileo rolled balls down ramps and timed the truth — everything falls alike. And in those same years, stargazers watching the "changeless" heavens caught them changing: new stars flaring out where no change was allowed, comets sailing clean through the supposedly perfect sky, planets refusing to run in perfect circles. Every one of those discoveries was made the same way, and it is the only way a spell like this ever breaks: <b>somebody checks</b>.</p>
<div class="bigidea">🌟 <b>Big Idea #3:</b> "Plato is my friend — but truth is a better friend." Aristotle said it about his teacher; science had to learn to say it about Aristotle himself. No authority, however great, outranks a careful check. The mark of respect a scientist pays a great mind is to <b>test it</b>.</div>""",
            cps=[dict(
                type="num",
                kicker="How long can an unchecked 'obviously' survive?",
                q="""Aristotle died in <b>322 BC</b>. Galileo timed falling bodies and broke the "heavy falls faster" rule around <b>1600 AD</b>. Add across the BC/AD line: about how many years did the mistake go unchecked?""",
                answers=[1922, 1921, 1900], unit="years",
                hint="Crossing the line, you add: 322 + 1600. (About nineteen centuries!)",
            )],
        ),
        dict(
            kicker="Chapter Nine · Mieza, Babylon & Chalcis · 343–322 BC",
            title="The Student Who Conquered the World",
            html="""
<p>In <b>343 BC</b>, while Aristotle was still hauling sea creatures out of the lagoon at Lesbos, a letter arrived from the north. King <b>Philip of Macedon</b> &mdash; ruler of the rough hill country where the Athenians thought nobody civilised lived &mdash; had a thirteen-year-old son who needed a teacher, and he wanted the best mind alive. Aristotle went. For about <b>three years</b> he taught the prince in a sanctuary at <b>Mieza</b> called the Temple of the Nymphs: a shaded walk, stone benches, a spring, and the boy who would become <b>Alexander the Great</b>.</p>
<p>Nobody knows exactly what Aristotle taught him. Plutarch, writing four hundred years later, says the lessons ran from medicine to poetry, and that Aristotle gave his pupil a copy of Homer's <i>Iliad</i> that he had corrected by hand. Alexander carried that book across Asia for the rest of his life and slept with it under his pillow &mdash; next to a dagger. That pairing is the whole man: the poem and the knife.</p>
<p>In <b>336 BC</b> Philip was murdered, and the twenty-year-old pupil became king. Two years later he marched his army into Asia, and he never came home. He beat the Persian Empire, the largest the world had ever seen, in three great battles. He took Egypt, and in <b>331 BC</b> paced out the streets of a new city at the mouth of the Nile and named it after himself: <b>Alexandria</b>. He crossed the mountains into what is now Afghanistan and Pakistan. In <b>326 BC</b>, at a river in India, his exhausted soldiers finally refused to take one more step east &mdash; the only army that ever beat him was his own. Three years later, in Babylon, he caught a fever and died. Born in July 356 BC, dead in June 323 BC: he was <b>32</b>, a month short of 33. He had been marching for eleven years.</p>
<div class="funfact">📜 One legend says Alexander ordered hunters, fishermen and bird-catchers across his empire to send specimens back to his old teacher, and that Aristotle's animal books were written from them. The story comes from the Roman writer Pliny, nearly four centuries after the fact, and nobody has been able to check it &mdash; so treat it as a good story, not a fact. (Aristotle's own descriptions are almost all of animals from the Aegean, which is a clue.) What <i>is</i> certain is that the friendship cooled: Aristotle's nephew Callisthenes went along as the expedition's historian, spoke his mind once too often, and in 327 BC Alexander had him killed.</div>
<p>Now watch what the pupil did to the teacher, without meaning to. The morning the news of Alexander's death reached Athens, the city rose against everything Macedonian &mdash; and the most famous Macedonian in town was Aristotle. Somebody dug up a charge: <b>impiety</b>. The <i>same</i> charge that had killed Socrates, seventy-six years earlier, in the same city. Aristotle did not stay for the trial. He packed up and left for the island of Euboea, and later writers put a line in his mouth as he went: <i>he would not let Athens sin twice against philosophy.</i> (The line first appears in a book written five hundred years later &mdash; check every quote. But whoever wrote it understood the lesson.) He died there the next year, <b>322 BC</b>, of a stomach illness, aged 62. Socrates stayed and drank. Aristotle looked, compared, and walked away. Two hand gestures, one more time.</p>
<p>And then something strange happened. The empire fell apart almost at once: within a few years Alexander's generals had carved it into kingdoms and were at war with each other. But one of those generals, <b>Ptolemy</b>, who had been a boy at Philip's court with Alexander, took Egypt &mdash; and took Alexandria. There he and his son built a temple to the Muses, a <b>Museum</b>, with the greatest <b>Library</b> the world had ever seen, and the man who advised them on how to set it up was a graduate of Aristotle's Lyceum. Euclid worked there and wrote geometry down as a machine of proofs, the way Plato had dreamed. And not quite a century after Alexander's death the Library's chief, a man named <b>Eratosthenes</b>, measured the size of the Earth from that city with a stick and a shadow &mdash; the very sphere that Aristotle had proved was round by watching eclipses. The conqueror's city outlived the conquest by centuries, and what it produced was not an empire. It was <i>science</i>.</p>
<div class="bigidea">🌟 <b>Big Idea #4:</b> Count the chain. Socrates taught Plato. Plato taught Aristotle. Aristotle taught Alexander. Alexander's empire lasted about as long as he did &mdash; a dozen years and then pieces. The ideas passed down that chain are still running the world. A sword can take a city. A method can take everything after it.</div>""",
            cps=[dict(
                type="num",
                kicker="The whole chain, in one subtraction",
                q="""Socrates was born about <b>470 BC</b>. Alexander, the student of the student of his student, died in <b>323 BC</b>. How many years does the whole four-man chain span, from the first man's birth to the last man's death?""",
                answers=[147], unit="years",
                hint="BC counts down: 470 − 323.",
            ), dict(
                type="mc",
                kicker="Read the exit line like a philosopher",
                q="""Leaving Athens in 323 BC, Aristotle is said to have declared that he would not let the city <i>"sin twice against philosophy."</i> What was the <b>first</b> sin?""",
                mc=[("The hemlock — Athens had already put Socrates to death on the same charge, and Aristotle refused to be the sequel", True),
                    ("Letting Plato found a school outside the city walls", False),
                    ("Teaching geometry to Macedonians", False)],
                good="Exactly, {name}. The lesson closes where it opened: the same city, the same charge of impiety, seventy-six years apart. Socrates stayed and made his point with a cup of poison. Aristotle, the man who looked at the evidence, looked at it and left. Neither of them stopped doing philosophy.",
                bad="Look back at Chapter One, {name}. What did Athens do to a philosopher in 399 BC, and on what charge? Aristotle had just been handed the very same charge.",
            )],
        ),
    ],
)
