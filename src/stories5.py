# -*- coding: utf-8 -*-
"""Story data: Galileo Galilei."""

GALILEO = dict(
    title="The Starry Messenger — Galileo Galilei",
    h1="✦ The Starry Messenger ✦",
    sub="Galileo, the telescope, and the price of looking for yourself · 1564–1642",
    footer="Companion lesson to the Constellation Plotting Worksheets · All events are historical<br>(where a famous story is probably legend, the lesson says so)",
    praise=["Measured like a master, {name}!", "The Medici court would hire you, {name}!",
            "Exactly right, starry messenger!", "{name}, that answer would survive the Inquisition!",
            "Padua would give you a professorship, {name}!"],
    cert_org="The University of Padua · The Medici Court of Tuscany",
    cert_of="the tale of Galileo Galilei",
    cert_rank="Starry Messenger, First Class",
    finale_title="You Can Silence a Man, Not a Fact",
    finale_html="""
<p>Galileo died in January 1642, still under house arrest, still officially a condemned man. Within a year, on a farm in England, <b>Isaac Newton</b> was born — the man who would take Galileo's falling bodies and Kepler's planet laws and weld them into one universal physics. The relay never dropped the baton.</p>
<p>And the machinery of authority ground on, and then ground down. The <i>Dialogue</i> stayed on the church's index of forbidden books until <b>1835</b> — two hundred years of banning a book about a fact. In <b>1992</b>, Pope John Paul II formally acknowledged that the church had been wrong to condemn him. By then, spacecraft had been named after Galileo, and astronauts standing on the Moon had dropped a hammer and a feather side by side — on live television, in a place with no air — and watched them land together, exactly as he said they would.</p>
<p>Galileo's deepest belief was written in his own book <i>The Assayer</i>: the universe "is written in the language of mathematics" — and anyone who learns that language can read it for themselves. Not just priests. Not just professors. That's why he wrote in Italian. That's why he pointed the tube at the sky and then handed it to whoever was next in line. <b>Look for yourself</b> may be the most dangerous sentence ever spoken — and it's the founding sentence of science.</p>""",
    takeaways="""<div class="laws">
<p><b>What you now know that most adults don't:</b></p>
<p>① <b>The pendulum law:</b> a pendulum's timing depends on its length — not on how heavy it is or how wide it swings. Timekeeping was born from a swinging lamp.</p>
<p>② <b>The law of falling:</b> everything falls alike, and distance grows with the square of time — the ramp data goes 1, 3, 5, 7… and the totals are perfect squares.</p>
<p>③ <b>Jupiter's moons</b> proved not everything circles the Earth; <b>the phases of Venus</b> proved Venus circles the Sun. Two observations, one collapsing worldview.</p>
<p>④ Authority can ban a book, silence a man, and win every argument — and the Earth keeps moving anyway. <b>Facts don't need permission.</b></p>
</div>""",
    chapters=[
        dict(
            kicker="Chapter One · Pisa, Italy · 1564",
            title="The Musician's Son",
            html="""
<p>In February 1564, in the leaning-tower town of Pisa, a lute player's wife had a son. Three days later, across the country, the great Michelangelo died — Italy traded its greatest artist of the old age for the man who would drag it into the new one. (William Shakespeare was born that same spring, in England. 1564 was a very good year.)</p>
<p>The lute player mattered. Galileo's father, <b>Vincenzo Galilei</b>, was a musician with a rebellious streak: when the music professors of his day quoted ancient rules about harmony, Vincenzo <b>tested</b> them — hanging weights from lute strings, changing lengths and tensions, writing down what actually sounded right versus what the old books said should. Galileo grew up in a house where you settled arguments with an experiment. Remember that; it's the whole story in miniature.</p>
<p>His father wanted a doctor in the family — doctors got paid. So at seventeen, Galileo was packed off to the University of Pisa to study medicine. He lasted about four years, no degree — because somewhere along the way he wandered into a geometry lecture, and medicine never stood a chance.</p>
<div class="funfact">📅 Timeline check: when Tycho Brahe saw his new star explode into Cassiopeia in 1572, Galileo was a schoolboy in Pisa. The generation that would finish what Tycho started was already alive.</div>""",
            cps=[dict(
                type="num",
                kicker="The timeline",
                q="""Galileo was born in <b>1564</b>. Tycho's new star blazed out in <b>1572</b>. How old was Galileo when the "unchangeable" heavens changed?""",
                answers=[8], unit="years old",
                hint="1572 − 1564.",
            )],
        ),
        dict(
            kicker="Chapter Two · Pisa Cathedral · about 1583",
            title="The Lamp and the Pulse",
            html="""
<p>The most famous story about young Galileo goes like this. He's nineteen, a bored medical student at Mass in the Pisa cathedral. High overhead, a bronze lamp on a long chain is swinging — a caretaker must have pulled it aside to light it and let it go. The swings start wide and slowly die down to small ones. Everyone else sees a lamp. Galileo sees a <b>question</b>: do the wide swings take longer than the narrow ones?</p>
<p>He has no clock — nobody has a clock worth the name; that's the point. But he's a medical student, trained to count a patient's pulse. So he presses his fingers to his wrist and times the lamp with <b>his own heartbeat</b>. Wide swing: so many beats. Medium swing: the same. Tiny swing: <i>the same</i>. The swing shrinks, but the timing doesn't change.</p>
<p>Honesty first, as always: this story was written down by Viviani, Galileo's devoted student, years after his death — and the famous lamp that tour guides point to in Pisa was hung in 1587, <i>after</i> the story takes place. Take the scene as legend polished smooth. But the discovery is no legend: Galileo's own notebooks and letters show him experimenting with pendulums for decades, and the law he found is real. A pendulum's timing depends on the <b>length of its string</b> — not on how heavy the weight is, and (for ordinary swings) not on how wide it swings.</p>
<p>Then he flipped the trick, doctor-style: if a pendulum keeps steadier time than a pulse, use the <b>pendulum</b> to measure the <b>patient</b>. Adjust a little pendulum's length until it matches the heartbeat, read the length, and you've turned a heartbeat into a number. Doctors used pendulum pulse-counters for decades. And as a blind old man, Galileo dictated a design for a full <b>pendulum clock</b> — built in working form by Christiaan Huygens in 1656, it became the most accurate timekeeper on Earth for the next 270 years. Every tick of a grandfather clock is that cathedral lamp, still swinging.</p>""",
            cps=[dict(
                type="num",
                kicker="Think like a clockmaker",
                q="""A pendulum about <b>1 meter</b> long takes almost exactly <b>2 seconds</b> per full swing (over and back) — that's why grandfather clocks are the height they are. If a clock's pendulum makes <b>30</b> full swings, how many seconds have passed?""",
                answers=[60], unit="seconds",
                hint="30 swings × 2 seconds each.",
            )],
        ),
        dict(
            kicker="Chapter Three · Pisa & Padua · 1589–1604",
            title="The Tumbling Stones",
            html="""
<p>Now the young professor picks a fight with a man who'd been dead for 1,900 years. Aristotle taught that heavy objects fall faster than light ones — ten times heavier, ten times faster. For centuries, nobody checked. Galileo checked <i>twice</i>: once in his head, once on a ramp.</p>
<p>First, in his head. Imagine tying a light stone to a heavy stone with a cord and dropping the pair. By Aristotle's rule, the light stone falls slower, so it should drag on the heavy one like a little parachute — the pair falls <b>slower</b> than the heavy stone alone. But wait: tied together, they're one object <i>heavier</i> than the heavy stone — so the pair should fall <b>faster</b> than it. Slower and faster at the same time. The rule contradicts itself, and no experiment was ever needed to see it. (Viviani claimed his teacher also dropped weights from the Leaning Tower of Pisa in front of the assembled professors. Historians suspect that scene is another polished legend — you know the drill by now.)</p>
<p>Second, on the ramp — and this is the part that survives in his own handwriting. Falling is too fast to time, so Galileo <b>diluted gravity</b>: a polished bronze ball rolling down a gentle groove, timed with a water clock (weigh the water that flows while the ball rolls — heavier water, more time). Roll after roll, hundreds of them, he found a pattern of astonishing beauty. Mark off equal ticks of time. In the 1st tick the ball covers 1 unit of distance. In the 2nd tick: 3 units. In the 3rd: 5 units. In the 4th: 7 units — <b>the odd numbers, in order</b>. And the running totals? 1, 4, 9, 16… <b>perfect squares</b>. Distance grows with the square of time — the exact law you used in the Newton lesson, caught raw in the data.</p>
<div class="bigidea">🌟 <b>Big Idea #1:</b> Galileo's real invention wasn't a fact — it was a <b>method</b>. Tame the problem (slow it with a ramp), measure it (even if your clock is water), find the pattern, write it as mathematics. He called mathematics "the language in which the book of nature is written." The measured experiment starts here.</div>""",
            cps=[dict(
                type="mc",
                kicker="Run the thought experiment yourself",
                q="""Two stones, one heavy and one light, tied together with a cord and dropped. Aristotle's rule says the pair must fall <i>slower</i> than the heavy stone alone (the light one drags) AND <i>faster</i> than it (together they're heavier). What does this contradiction prove?""",
                mc=[("Aristotle's rule destroys itself — falling speed can't depend on weight at all", True),
                    ("The cord must break in mid-air", False),
                    ("Heavy and light stones can't be tied together", False)],
                good="Exactly, {name} — if a rule gives two opposite answers to one question, the rule is dead. Everything falls alike; air resistance is the only reason a feather loses to a hammer. Astronauts proved it on the Moon in 1971: hammer and feather, dropped together, landed together.",
                bad="Look at the logic again: one rule, one situation, two contradictory predictions. What does that always mean for the rule?",
            ), dict(
                type="num",
                kicker="Galileo's actual ramp data",
                q="""Equal ticks of time; distances per tick go <b>1, 3, 5, 7</b> — the odd numbers. What is the <b>total</b> distance rolled after 4 ticks? (Check your answer against 4 × 4 — Galileo noticed that too.)""",
                answers=[16], unit="units",
                hint="1 + 3 = 4. Then + 5 = 9. Then + 7 = …  Notice the running totals: 1, 4, 9 — the square numbers!",
            )],
        ),
        dict(
            kicker="Chapter Four · Venice · summer 1609",
            title="The Tube from Holland",
            html="""
<p>In 1609, word reached Venice of a Dutch novelty: a tube with two lenses that made far things look about <b>3 times</b> closer. A toy for sea captains and spies. Galileo — now a 45-year-old mathematics professor at Padua, chronically short of money — heard the rumor and understood two things instantly: how it probably worked, and what it was worth.</p>
<p>Without ever seeing one, he built his own in 24 hours. Then a better one: <b>8 times</b>. He marched the Venetian senators up the bell tower of St. Mark's and let them watch ships two hours before the ships reached harbor — for a navy, two hours' warning is treasure. The senate doubled his salary on the spot. He kept grinding lenses, night after night, until his instruments reached <b>20 and then 30 times</b>.</p>
<p>Here is the part that matters: Galileo did not invent the telescope, and the lesson won't pretend he did. Dozens of people held one before him. His genius was different — he was the first to <b>point it at the sky and understand what he was seeing</b>. A tool is just a tool; the discovery lives in the question you aim it at.</p>""",
            cps=[dict(
                type="num",
                kicker="Grinding lenses",
                q="""The Dutch spyglass magnified about <b>3×</b>. Galileo's best instruments reached about <b>30×</b>. How many times more powerful had he made the "toy"?""",
                answers=[10], unit="times",
                hint="30 ÷ 3.",
            )],
        ),
        dict(
            kicker="Chapter Five · Padua · winter 1609–1610",
            title="Two Months That Changed the Sky",
            html="""
<p>Then he aimed it up, and in about two months found more new things in the sky than humanity had found in two thousand years.</p>
<p><b>The Moon</b>: not a polished crystal globe, but a <i>world</i> — mountains, craters, plains. He watched sunlight catch the peaks while the valleys stayed dark, and — geometry, always geometry — used the shadow lengths to calculate the mountains' height at around four miles. <b>The Milky Way</b>: that faint cloud across the sky dissolved, in the eyepiece, into <b>countless individual stars</b> no eye had ever separated. Then, on <b>January 7, 1610</b>, the shot heard round the universe: three little "stars" in a dead-straight line beside Jupiter. Odd. The next night they had <i>moved</i> — the wrong way. Within a week a fourth appeared, and the truth landed: these weren't stars. They were <b>moons, orbiting Jupiter</b>.</p>
<p>Feel how much broke in that moment. Every version of the old sky agreed on one thing: everything circles the <b>Earth</b>. Yet here were four worlds circling <i>Jupiter</i>, in plain, repeatable view. And a favorite argument against Copernicus — "if the Earth moved, it would leave its Moon behind!" — collapsed on the spot, because Jupiter visibly moves and hauls four moons along without losing one. Months later Galileo added the knockout: through the telescope, <b>Venus shows phases</b> like a little Moon, including a nearly <i>full</i> face — which is geometrically impossible unless Venus goes around the <b>Sun</b>.</p>
<p>He rushed it all into a slim book, <i>Sidereus Nuncius</i> — <b>The Starry Messenger</b> (March 1610). It sold out. He named Jupiter's moons the "Medicean stars" after Tuscany's ruling family, and the flattered Medici made him their court philosopher — no more teaching, all discovery. Some professors, invited to simply <i>look through the tube</i>, refused. They said the instrument couldn't be trusted — some wouldn't put their eye to it at all. Remember them, the men who wouldn't look.</p>""",
            cps=[dict(
                type="num",
                kicker="Keep Galileo's logbook",
                q="""Galileo timed the innermost moon, Io, circling Jupiter in about <b>42 hours</b>. A week is <b>168 hours</b>. How many complete laps does Io make around Jupiter in one week?""",
                answers=[4], unit="orbits",
                hint="168 ÷ 42.",
            ), dict(
                type="mc",
                kicker="The Venus verdict",
                q="""Through the telescope, Venus shows a <b>full set of phases</b> — thin crescent all the way to nearly full, changing size as it goes. Why is the nearly-FULL phase the killer evidence?""",
                mc=[("Venus can only look full when it's on the far side of the Sun from us — so Venus must orbit the Sun", True),
                    ("A full Venus proves Venus makes its own light", False),
                    ("It proves the telescope adds light to faint objects", False)],
                good="Locked, {name}. To show us a fully lit face, Venus has to be across the Sun from Earth — impossible if it circles the Earth, automatic if it circles the Sun. One observation, and the Earth-centered sky lost its best planet.",
                bad="Think about where the Sun, Venus, and Earth must sit for us to see Venus fully lit — like seeing someone's whole sunlit face, sunward of them. What does Venus have to be orbiting for that lineup to happen?",
            )],
        ),
        dict(
            kicker="Chapter Six · Florence & Rome · 1616–1632",
            title="The Warning and the Book",
            html="""
<p>Fame that big casts a shadow. In <b>1616</b>, church authorities formally declared the Sun-centered system "foolish and absurd… and contrary to Holy Scripture," and Galileo was officially warned: you may not hold or defend it. He bit his tongue for years. And Galileo's tongue did not enjoy being bitten.</p>
<p>Then came what looked like a miracle: in 1623 his old friend and admirer Maffeo Barberini — a man who had once written a poem praising Galileo's discoveries — became <b>Pope Urban VIII</b>. Galileo visited Rome, was warmly received, and came away believing he had permission to write about the two rival systems of the world, as long as he treated the question as undecided.</p>
<p>What he wrote instead, in 1632, was the <i>Dialogue Concerning the Two Chief World Systems</i> — and it is one of the great troublemaking books of all time. Three friends debate the cosmos: brilliant <b>Salviati</b> argues for Copernicus, fair-minded <b>Sagredo</b> asks the questions, and the Aristotelian gets stuck defending the old sky with the weakest arguments. Galileo named him <b>Simplicio</b> — officially after an ancient philosopher; in Italian, unmistakably, "the simpleton." Two more provocations: he wrote it in <b>Italian</b>, not scholars' Latin — and worst of all, he put one of the Pope's own favorite arguments into Simplicio's mouth, on the last page. Urban was told he'd been made the fool of the book. The friendship died that day. The book sold out anyway.</p>""",
            cps=[dict(
                type="mc",
                kicker="Why Italian?",
                q="""Serious books were written in Latin, the private language of scholars. Galileo wrote the <i>Dialogue</i> in everyday Italian. Knowing everything this series has taught you about him — why?""",
                mc=[("So ordinary people, not just professors, could read the evidence and judge for themselves", True),
                    ("His Latin was poor", False),
                    ("Latin books were more expensive to print", False)],
                good="Exactly, {name} — same reason he handed senators the telescope. Galileo's whole creed was that nature's book is open to anyone who'll read it. Writing in Italian was 'look for yourself,' in print. (His Latin was excellent — Sidereus Nuncius is in Latin, aimed at scholars across Europe.)",
                bad="Think about who can read Latin in 1632 — and who Galileo kept trying to hand the evidence to, from the senate bell tower on.",
            )],
        ),
        dict(
            kicker="Chapter Seven · Rome · 1633",
            title="The Trial",
            html="""
<p>The summons came from the Inquisition in the autumn of 1632: present yourself in Rome. Galileo was sixty-nine, half-blind, and so ill that three doctors signed a statement that the winter journey might kill him. Rome's answer: come, or be brought in chains. He went.</p>
<p>This chapter tells it plainly, because it happened. He was interrogated four times. He was shown the instruments of torture — a formal step called <i>rigorous examination</i>, a threat the old man was legally required to take seriously. And behind everything stood a memory no one in that room had to say out loud: <b>Giordano Bruno</b>, who had also refused to take back his ideas about the cosmos, and who had been burned at the stake in a Roman market square in 1600, when Galileo was already a professor.</p>
<p>On June 22, 1633, in a Dominican convent, the man who had seen more of the universe than any human being in history knelt in the white shirt of a penitent and read aloud a confession: that he <i>"abjured, cursed, and detested"</i> the opinion that the Earth moves. Legend says he muttered <i>"Eppur si muove"</i> — "and yet it moves" — as he rose. Honesty check: there's no evidence for it; the line first appears a century later. But notice something. Whether or not he whispered it, <b>it was true anyway</b>. The Earth did not pause to hear the verdict. That's the terrifying, wonderful thing about facts: they don't attend trials.</p>
<div class="bigidea">🌟 <b>Big Idea #2:</b> The court won everything that day — the confession, the ban, the sentence. It just couldn't win the actual question. Authority can decide who gets punished; it cannot decide what's true. Tycho's comet didn't ask permission, and neither did Galileo's Earth.</div>""",
            cps=[dict(
                type="num",
                kicker="An old man before the judges",
                q="""Galileo was born in <b>1564</b>; the trial ended in <b>1633</b>, a few months after his birthday. How old was the man kneeling in the penitent's shirt?""",
                answers=[69], unit="years old",
                hint="1633 − 1564.",
            )],
        ),
        dict(
            kicker="Chapter Eight · Arcetri · 1633–1642",
            title="The Smuggled Book",
            html="""
<p>The sentence was prison; it was softened to <b>house arrest for life</b> at his villa in Arcetri, in the hills above Florence — near the convent of his beloved daughter, Sister Maria Celeste, who had secretly helped him through the trial and who died, to his devastation, the very next year. He was forbidden to publish. Forbidden to teach. The most famous eyes in Europe then went dark: by 1638 Galileo was completely blind. He wrote to a friend that the universe he had "enlarged a hundred, a thousand times" had now shrunk "to the narrow confines of my own body."</p>
<p>And then the old prisoner pulled off his greatest escape. Locked in his villa, going blind, he wrote an entire book — not about the forbidden heavens, but about his life's real treasure: motion. The ramps. The pendulums. The odd numbers and the squares. Why structures break. It was, in effect, the founding textbook of physics: <i>Discourses on Two New Sciences</i>. Publishing it in Italy was impossible — so the manuscript was <b>smuggled out</b>, page by page, to Protestant Holland, beyond the Inquisition's reach, and printed in Leiden in 1638. When copies circulated back into Italy, Galileo innocently marveled that he had no idea how the printers got it. The generation that learned physics from that contraband book included the teachers of Isaac Newton.</p>
<p>He died at Arcetri on January 8, 1642, at seventy-seven, with a small circle of students at his side — still, on paper, guilty. The paper took a while to catch up with the sky: the <i>Dialogue</i> stayed banned until 1835, and not until <b>1992</b> did Pope John Paul II formally acknowledge that condemning Galileo had been a mistake.</p>""",
            cps=[dict(
                type="num",
                kicker="How long does an apology take?",
                q="""The trial: <b>1633</b>. The formal acknowledgment that the court was wrong: <b>1992</b>. How many years did the correction take?""",
                answers=[359], unit="years",
                hint="1992 − 1633.",
            )],
        ),
    ],
)
