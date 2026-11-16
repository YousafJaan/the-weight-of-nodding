# -*- coding: utf-8 -*-
"""
author_batch_1.py
Authors Chapters 00 to 04 of 'The Weight of Nodding' (Expanded Edition).
Zero em-dashes or en-dashes. Plain writing. High emotional and literary depth.
"""
import os
import re

def clean_dashes(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

chapters = {}

# ---------------------------------------------------------------------------
# 00_prologue.md
# ---------------------------------------------------------------------------
chapters['00_prologue.md'] = """# Prologue: The Cost of the Reflex

The small seminar room on the third floor of the Department of Political Science at Bahauddin Zakariya University had three ceiling fans. Two of them turned with a rhythmic, metal scrape that sounded like an old pair of garden shears cutting through wire. The third fan did not turn at all. It hung motionless from the damp ceiling, its iron blades coated in the thick grey dust that settles over Multan every summer.

It was eleven in the morning in mid-August. Outside, the heat on Bosan Road was already touching forty-five degrees Celsius. Inside Seminar Room 4, thirty-eight students sat on wooden benches designed for twenty-five. The air was heavy with the smell of sweat, damp notebooks, and the cheap black hair oil that the boys bought from the general store outside Chungi No. 9.

At the wooden podium stood Dr. Qureshi. He was a man of sixty-two with yellowed teeth, an untrimmed white beard, and a grey safari suit that he wore regardless of the weather. For forty minutes, he had been explaining the concept of social contract theory. He did not use books. He used a bundle of dog-eared, yellowing foolscap sheets that had clearly been photocopied twenty years earlier from a textbook long out of print.

"In an ordered society," Dr. Qureshi said, tapping his chalk against the edge of the wood, "the individual surrenders their unruly personal judgment to the sovereign. Order requires compliance. When the citizen questions the ruler without sanction, the moral fabric unravels. Does everyone understand this fundamental truth?"

He stopped. His eyes swept across the crowded benches.

Every single head in the room moved in unison.

Up, then down. A smooth, rhythmic, collective dip of thirty-eight chins.

I felt the movement before I even consciously registered the thought. My chin dropped toward my chest, my neck bent, and my face arranged itself into that universal Pakistani expression of docile comprehension. A polite smile. A soft, deferential nod.

*Yes, sir. Of course, sir. We agree, sir.*

Sitting next to me on the wooden bench was Aqsa. Her knuckles were white against her plastic pencil box. She knew, and I knew, that the syllabus we had been reading for the past three weeks contradicted every single sentence Dr. Qureshi had just uttered. John Locke had argued the exact opposite. Jean-Jacques Rousseau had argued that sovereignty belongs to the people, and when authority breaches trust, obedience is void. In our own country, the uncritical surrender of citizens to arbitrary rulers had produced decades of constitutional disasters, unbridled monopolies, and institutional decay.

Aqsa's lips parted. She leaned forward half an inch. She was going to speak.

Under the wooden bench, my hand reached out and gripped her wrist. I squeezed hard.

"Do not," I whispered, barely moving my lips, keeping my eyes glued to my open notebook. "Do not do it, Aqsa. Just nod."

She turned her head to look at me. Her brown eyes were furious, bright with that dangerous, burning clarity that gets young girls thrown out of university departments. But she felt the pressure of my fingers on her pulse. She looked at Dr. Qureshi, whose chalk was poised like a dagger over his attendance register. If he wrote a red cross next to a student's name, their internal assessment marks would vanish. If he decided a student was insolent, no sifarish from the Dean could restore their grade.

Aqsa swallowed. Her shoulder dropped. Slowly, reluctantly, her chin tilted downward.

She nodded.

Dr. Qureshi smiled, a satisfied, benevolent curl of his dry lips. "Good," he said, turning back to the blackboard. "At least this batch has basic manners."

Under the bench, I let go of Aqsa's wrist. My palm was damp with cold sweat.

My neck ached. It was not a physical cramp from sitting on a hard bench. It was an ache deeper down, inside the tendon, in the small hinge where the base of the skull meets the spine.

That hinge is where women in Pakistan are trained to carry the weight of survival.

From the day a girl is born in our cities and towns, she is taught that agreement is the highest female virtue. When your father decides which college you will attend, you nod. When your mother tells you to lower your voice because your uncle has walked into the veranda, you nod. When your brother takes the larger piece of chicken and the cooler room near the fan, you nod. When your cousins lecture you on modesty while staring at your collarbone, you pull your chadar tighter around your shoulders, you look down at your slippers, and you nod.

You are told that nodding keeps you safe. You are told that nodding proves your tarbiyat, your family honor, your sweet nature.

They do not tell you the truth.

The truth is that nodding is a slow, silent poison. Every time you bow your head to a statement you know is a lie, a small piece of your intellect rots. Every time you agree to a rule designed to demean your dignity, you sign an invisible contract that makes you smaller, quieter, and more convenient for the people who profit from your silence.

For two long years inside the walls of Khadija Hall at Bahauddin Zakariya University, I nodded. I nodded to corrupt wardens who stole our food budget. I nodded to arrogant professors who threatened our marks if we asked for primary data. I nodded to doctors who told me that my agonizing, undiagnosed nerve pain was just female nervousness. I nodded to distant relatives who whispered that a girl from a respectable family should finish her degree quickly, pack her tin trunk, and go to her husband's house without opening her mouth.

I nodded until my body collapsed. I nodded until my nervous system broke down. I nodded until I lost an entire academic year to an illness that no hospital in Multan could name, an illness born entirely from the violent friction between what my soul knew and what my mouth was forbidden to say.

This book is the record of what happened when the nodding stopped.

It is not an academic paper, though it contains data that powerful people in our university tried very hard to bury. It is not a polite memoir, because politeness is the velvet glove that institutional bullies wear when they choke you.

It is a field guide for every Pakistani girl who has ever felt that suffocating knot in her throat while sitting on a wooden bench, watching someone with authority tell her that black is white, that corruption is culture, and that obedience is her only duty.

You do not owe them your agreement. You never did.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 1: The Rule of the Three-Second Pause

1. **Break the Muscle Memory of Agreement:** The human neck has a reflex. When confronted with authority, most young women nod within half a second to relieve social tension. From this day forward, introduce a three-second freeze. When a professor, family elder, or supervisor makes an assertion, do not move your chin. Keep your eyes steady, your spine straight, and count three silent seconds in your chest. That small delay dismantles the expectation of immediate submission.
2. **Distinguish Civility from Agreement:** You can be exceptionally polite without agreeing to a falsehood. A neutral, quiet statement like, "I hear your perspective, sir," commits you to nothing. It leaves your intellectual dignity intact while giving the bully no pretext to accuse you of disrespect.
3. **Audit Your Concessions:** Every night, ask yourself one question: What lie did I endorse today simply because I was afraid of the awkwardness of silence? When you identify it, write it down in a private notebook. What is named can be resisted.
"""

# ---------------------------------------------------------------------------
# 01_chapter_1.md
# ---------------------------------------------------------------------------
chapters['01_chapter_1.md'] = """# Chapter 1: The February Midnight (Room 34)

The cold in Multan during February does not behave like the cold in northern towns. It does not come with snow or clean, crisp mountain breezes. It comes as a thick, yellow-grey fog that rolls off the agricultural fields around Bosan Road, saturating the ancient brickwork with damp chill.

It was two in the morning on the tenth of February.

Inside Room 34 of Khadija Hall, the concrete walls felt like the inside of a cold storage locker. The university had turned off the main gas line at eleven at night, claiming fuel conservation, though everyone knew the hostel superintendent's bungalow across the lawn had gas heaters burning until dawn.

I was sitting on the edge of my iron cot, wrapped in three layers of clothing: a thick woolen sweater my mother had knitted five years earlier, an oversized fleece jacket, and a brown handloom shawl pulled tight over my ears. My feet were shoved into double wool socks, yet my toes were completely numb.

On the floor between my cot and Sidra's bed sat a plastic bucket. Inside the bucket, a contraband immersion rod hummed softly.

The copper coil was black with years of built-up mineral scale from Multan's saline bore water. It hissed as it heated three inches of water in a dented steel mug. We were not allowed to have immersion rods. If the hostel supervisor caught you with an electrical element, the fine was five thousand rupees on your semester voucher, plus a mandatory disciplinary notice sent to your father.

Yet without that red-hot copper coil, we would have frozen.

I reached out and touched the steel mug with the back of my fingernail. It was warm. I dropped in a spoonful of cheap Danedar tea dust, half a packet of powdered milk, and a lump of unrefined brown sugar that Iqra had smuggled from her home in Lodhran.

The steam rose in a thin, fragrant curl into the freezing air. It was the only warmth in the entire room.

Sidra was asleep on the cot next to mine, breathing with that shallow, exhausted rhythm of someone whose dreams are troubled. Her face was half-hidden under a heavy cotton quilt. Next to her pillow lay a folded white letter from her village near Khanewal. Her paternal uncle had set a wedding date for June, to a cousin twelve years older than her who ran a fertilizer depot. She had cried until her eyes were swollen shut at nine in the evening, and then she had fallen into a heavy, defeated sleep.

Across the narrow room, on the upper bunk, Saba was reading by the glow of a rechargeable torch. She held the plastic tube between her teeth, turning the pages of an Indian edition of international political economy with gloved fingers. Her breath made small white clouds in the darkness.

I turned back to my wooden study table.

The surface of the table was scarred with old pen marks, ring stains from tea cups, and names carved by girls who had lived in Room 34 ten years before us. In the corner of the desk lay my medical file from Nishtar Hospital.

It was three inches thick. Inside were dozens of blood tests, thyroid panels, brain CT scans, and nerve conduction reports. Every single test carried the same printed conclusion at the bottom: *Within Normal Limits.*

Yet for twelve months, I had been unable to lift my arms without blinding, electric pain shooting down my cervical spine. My fingers had developed involuntary tremors that made my tea spill onto my notes. Some mornings, I would step onto the cold concrete floor and my legs would simply buckle, dropping me to my knees in front of my iron trunk.

The chief physician at Nishtar Hospital, a heavy man with gold cufflinks and an impatient scowl, had looked at my clean blood reports, adjusted his spectacles, and said to my father:

"The girl has nothing physical. It is functional tension. Female hysteria from academic pressure. Give her multivitamins and marry her off. A domestic routine will settle her mind."

My father had sat there, his weathered hands clutching his prayer beads, nodding respectfully to the big doctor. And I, sitting on the steel examination stool, had lowered my eyes and nodded too.

*Yes, doctor. Of course, doctor.*

That nod had cost me an entire year of my life.

I had been forced to freeze my academic session. A one-year drop. In Pakistan, when a male student takes an extra year, people say he is preparing for competitive exams or building a business. When a female student drops a year, the neighborhood talks in hushed, suspicious whispers. Did she have a scandal? Is she mentally unstable? Is she damaged goods?

I had spent eight months locked inside my family's house, staring at the ceiling, listening to the ceiling fan cut through the silence. My body was broken, but it was not broken by a virus or a bacterial infection.

It was broken by two decades of silence.

Every unsaid truth, every forced smile, every swallowed insult from corrupt administrators and entitled relatives had turned inward, becoming an autoimmune fury that attacked my own nerves. The human body is not built to carry the weight of continuous lying. When your mind refuses to scream, your nerves scream for you.

It was on that freezing February night in Room 34, watching the steam rise from that dented steel mug, that something inside me hardened into stone.

I opened a fresh, unlined spiral notebook that I had bought from the stationery shop near the department for two hundred rupees. The paper was rough, off-white, and smelled faintly of wood pulp.

My hands were shaking, partly from the cold, partly from the tremor in my wrists.

I picked up a blue ballpoint pen. I rested my forearm on the cold wooden desk.

I wrote the first sentence:

*I have nodded my life away, and the bill has arrived in my bones.*

I stared at the words for five minutes. The ink looked dark and permanent against the white sheet.

Saba turned a page in her book on the upper bunk. The paper rustled.

"Anam?" she whispered, taking the torch from her mouth. "Why are you still awake? The temperature is dropping. Come under the quilt."

"I am writing, Saba," I said softly.

"Writing what? The notes for Comparative Government?"

"No," I replied, looking down at the notebook. "A record. A record of everything they told us to swallow, and what it costs to digest it."

Saba was quiet for a long moment. Then she pulled her blanket tighter around her shoulders and rested her chin on the wooden guardrail of the bunk.

"Be careful what you write down, Anam," she said, her voice barely louder than the hum of the immersion rod. "Paper has ears in this hostel. If the warden finds out you are keeping a journal about what happens behind these gates, she will confiscate it before you can write the final chapter."

"Let her try," I whispered, dipping my fingers near the hot mug to warm them. "A warden can seize a cell phone. She can lock an iron gate. But she cannot seize what a woman writes when she has already lost an entire year of her life."

That night, between two and five in the morning, while the fog pressed against the windowpanes and the cold crept through the cracks in the wooden frame, I wrote fifteen pages.

I did not write with polite academic detachment. I did not use the passive voice that professors love because it hides human responsibility. I wrote names. I wrote dates. I wrote about the saline bore water that made our scalps bleed. I wrote about the five-hundred-rupee bribes demanded for clean gate passes. I wrote about the girl from Muzaffargarh who was expelled because someone saw her talking to her male cousin outside the Metro station.

By the time the call to prayer drifted across Bosan Road from the university central mosque, my steel mug was cold. The immersion rod sat silent in the empty bucket.

My fingers were stiff, but the tremor in my right wrist had stopped.

For the first time in eighteen months, the pain in my neck was gone.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 2: The Threshold Manifesto (Writing as Self-Preservation)

1. **Document the Attrition Before You Forget:** When an institution degrades you, it relies on your exhaustion to erase the record. You tell yourself, "I will deal with this after exams," or "It is not worth the headache." That is how abuses become normal. Keep an uncompromised, physical ledger hidden from casual view. Write the date, the exact quote, and the names of the witnesses. Documentation transforms subjective trauma into objective evidence.
2. **Recognize Somatic Resistance:** If you are experiencing mysterious fatigue, unexplainable digestive collapses, hair thinning, or muscle tremors that medical scans cannot explain, do not let patriarchal doctors dismiss you as neurotic. Examine your compromises. Where are you currently pretending to agree with something that disgusts you? Your body often rebels long before your conscious mind admits you are living in an unbearable compromise.
3. **The Power of the Private Notebook:** Never use institutional cloud drives or shared university devices to store your personal reflections or investigative logs. Buy a cheap, bound notebook. Keep it in your personal possession. In a world where digital surveillance is cheap and pervasive, ink on paper remains the ultimate secure perimeter.
"""

# ---------------------------------------------------------------------------
# 02_chapter_2.md
# ---------------------------------------------------------------------------
chapters['02_chapter_2.md'] = """# Chapter 2: The Red Line on Bosan Road

If you stand on the pedestrian footbridge outside the main gate of Bahauddin Zakariya University at eight in the morning, you see two different centuries colliding in the red dust.

Down below, on the cracked asphalt of Bosan Road, motorcycle rickshaws rattle past, spewing blue two-stroke smoke that smells of cheap kerosene. Donkey carts loaded with green sugarcane stalks move slowly along the dirt shoulder, their wooden wheels squeaking against the dry axle grease. Vendors push wooden barrows piled high with Kinnow oranges from Khanewal, shouting prices into the morning haze.

Rising directly above this chaos, supported by massive cylindrical concrete pillars of raw grey cement, is the elevated track of the Multan Metro Bus system.

The glass-and-steel stations at Chungi No. 9 and the BZU terminal look like spaceships that made an emergency landing in an ancient southern Punjab desert. Their red and green glass panels reflect the harsh sunlight, gleaming clean and antiseptic against the brick kilns and mango orchards that stretch toward the horizon.

Every five minutes, a long red-and-green articulated Metro bus hums quietly along the elevated concrete track. It glides smoothly past the traffic jams below, air-conditioned, orderly, and indifferent to the dust.

For a girl from a conservative middle-class home, that elevated red line is not just public transit.

It is a lifeline. It is the only corridor in the entire city where a woman can travel without an uncle, a brother, or an apologetic excuse.

I remember the morning I arrived for my first semester.

My father had accompanied me on the intercity bus from our district. He was a retired junior government clerk whose pension voucher arrived two weeks late every single month. He wore his good grey shalwar kameez, freshly pressed with a heavy coal iron, and black leather shoes whose heels had been replaced three times by the cobbler near the bus terminal.

Between us on the concrete platform of the BZU Metro terminal sat my tin trunk.

It was painted dark green, with brass latches that had turned brown with age. On the lid, my father had neatly stenciled my name in white oil paint: *ANAM SAJJAD, ROLL NO. 412, DEPT OF POLITICAL SCIENCE.*

That trunk had belonged to my mother when she married in 1994. It had held her wedding dupattas, her matriculation certificate, and two silver bangles that were sold when my elder brother needed kidney treatment. Now it held my life: three sets of stitched lawn suits, two woolen cardigans, a plastic bottle of mustard oil, four notebooks, and a pocket copy of the Holy Quran wrapped in green silk.

My father stood near the stainless steel turnstile, clutching his leather wallet inside his pocket. He looked around the modern glass station with that specific, anxious tension common to village elders when confronted by automated ticket barriers.

"Anam," he said, adjusting the strap of his shoulder bag. His voice was quiet, hushed by the sheer size of the university campus spreading out beyond the station windows. "You are the first girl from our family to cross the threshold of a university hostel. You must remember why you are here."

"I know, Baba," I replied, keeping my eyes fixed on the green trunk.

"You are here to study, pass your examinations with respect, and come home," he said. His fingers tapped against his knuckles. "Do not get involved in student politics. Do not sit in the cafeteria with girls from wealthy families who have no fear of social shame. If a professor speaks harshly to you, bow your head and say ji-achha. If the hostel administration makes a difficult rule, comply without argument. A girl's reputation in Multan is like a white sheet. Once it catches grease, no river can wash it clean."

He was not being cruel. He was giving me the only survival manual he knew.

In the world my father inhabited, safety was achieved through invisibility. If you did not make a sound, if you paid your electricity bills on time, if you agreed with every clerk who held your pension paperwork, you were allowed to survive unmolested. He genuinely believed that if I made myself quiet enough, the university would treat me with fatherly benevolence.

He did not know that institutions do not possess fatherly benevolence. Institutions are cold, bureaucratic machines designed to maximize revenue and minimize resistance. When an institution encounters an invisible, compliant person, it does not reward them with dignity.

It crushes them because it knows they will not scream.

The automated glass doors of the Metro station hissed open. A wave of students poured out: boys with plastic folders tucked under their arms, girls in dark abayas adjusting their hijabs, junior lecturers carrying leather briefcases stuffed with unread exam scripts.

My father picked up one handle of the green trunk. I picked up the other.

The trunk was heavy. The iron handle bit into the flesh of my fingers, leaving a deep red indentation. Together, we walked down the concrete steps of the elevated pedestrian bridge, descending from the cool glass of the Metro station into the blinding, dusty heat of Bosan Road.

The main university gate loomed before us: two massive brick pylons flanking an iron archway that bore the motto of the university in faded green Urdu calligraphy: *Knowledge is Light.*

At the security barrier, four guards in khaki uniforms sat on plastic chairs, smoking filterless cigarettes and drinking tea from small glass cups. They did not check the identity cards of the young men who roared through the gate on heavy motorcycles without mufflers. But when they saw my father and me carrying the green trunk, one of the guards stood up slowly, tapping a wooden baton against his shin.

"Where are you going?" he barked, blocking our path.

My father immediately stopped. He reached into his breast pocket with trembling fingers, pulling out my admission slip, my national identity card, his own pension card, and three passport-sized photographs stapled to a bank challan.

"Hostel allotment, officer," my father said, bowing slightly from the waist. His voice carried that familiar, humble tremor that broke my heart every time I heard it. "My daughter has secured admission in the Department of Political Science on open merit. Khadija Hall."

The guard took the papers. He did not look at the merit marks. He looked at my face, staring for three long seconds under the brim of his peaked cap, checking whether my eyes would drop.

I looked at his third shirt button, where a thread was coming loose. My chin dropped half an inch.

The guard grunted. He handed the papers back to my father without looking at him.

"Go straight down the main boulevard. Turn left after the library. Do not wander toward the boys' hostels. Visitors must leave before sunset."

"Ji-achha, sir. Thank you, sir," my father said, carefully tucking the papers back into his pocket.

We walked along the cracked asphalt of the campus boulevard. On either side, eucalyptus trees stood tall and grey, their leaves motionless in the suffocating heat. The smell of burning dry grass drifted from the university nursery.

Every twenty steps, we had to put the trunk down to rest our hands.

My father's forehead was covered in sweat. His breath came fast and ragged.

"Baba, let me carry it alone," I said, reaching for his handle.

"No," he said sharply, waving my hand away. "While I am alive, you do not carry your burdens alone on a public road."

He smiled, a tired, brave smile that made the deep lines around his eyes crinkle. He wiped his brow with the corner of his handkerchief.

Looking at him standing there in the middle of Bosan Road, with his worn-out leather shoes and his fierce, protective love, I felt a terrible weight settle onto my chest.

He had spent his entire life savings to pay my first semester admission fee: forty-two thousand rupees deposited into the university bank branch on a torn pink slip. He had borrowed seven thousand rupees from his brother to buy the mattress, the plastic bucket, and the wooden study lamp.

He believed that my education would buy our family freedom from the indignities of the clerk's office.

He did not know that inside the gates of Khadija Hall, a new set of clerks was already waiting, ready to teach me that the price of an education in Pakistan is your soul.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 3: Strategic Detachment (Separating Love from Submission)

1. **Love the Parent, Reject the Conditioning:** Our parents teach us docility not out of malice, but out of terror. They grew up in a country where speaking truth to power resulted in lost jobs, police beatings, or social exile. When your father tells you to bow your head, honor the love that birthed the advice, but discard the advice itself. Inherited fear is not a family heirloom; you are under no moral obligation to carry it into the next generation.
2. **The Logistics of Physical Autonomy:** Never rely on family members or male peers for basic daily transit if public alternatives exist. The elevated Metro bus, public shuttles, and predictable transit routes are tools of sovereignty. When you master your own mobility, you eliminate the primary leverage controlling individuals use to restrict female ambition: the threat of stranded isolation.
3. **The Silent Audit of Burdens:** Notice who carries the weight. When authority figures perform symbolic acts of protection while demanding your absolute obedience, calculate the trade-off. True protection empowers your independence; fake protection infantilizes you so that you remain dependent on the protector's whims.
"""

# ---------------------------------------------------------------------------
# 03_chapter_3.md
# ---------------------------------------------------------------------------
chapters['03_chapter_3.md'] = """# Chapter 3: Behind the Green Iron Gates

Khadija Hall did not look like a place of higher learning. It looked like a medium-security correctional facility built by people who deeply distrusted the concept of female literacy.

The boundary wall was twelve feet high, constructed from rough red bricks capped with two feet of rusted concertina razor wire. At the top of the wall, shards of broken brown glass bottles had been embedded into wet cement forty years ago, their jagged edges pointing toward the sky to deter anyone foolish enough to attempt an escape.

The main entrance was a massive double gate made of heavy sheet iron, painted a sickly shade of dark green that had blistered and peeled under decades of southern Punjab sun.

Set into the right side of the massive iron gate was a smaller, narrow wicket door, barely four feet high and eighteen inches wide. To enter Khadija Hall, every resident had to bend their spine, lower their head, and step sideways over a sharp steel sill while dragging their belongings behind them.

The architecture itself forced you to bow before you took a single step into the compound.

Inside the wicket door sat Maasi Sakina.

She was an institution older than the university itself. A woman of indeterminate age, somewhere between fifty-five and seventy, with skin like dried leather, missing molars, and a permanent wad of chewing tobacco tucked into her lower lip. She sat on a low wooden charpai covered in a faded ralli quilt, positioned so that her gaze intercepted every single person who crossed the threshold.

Next to her charpai was a heavy wooden table on which rested the Master Register: a massive, canvas-bound ledger with water-stained blue paper.

"Stop right there," Maasi Sakina rasped, spitting a stream of dark red tobacco juice into a rusted tin can behind her bed. "Father stays outside. No males past the green door. Not your father, not your brother, not your grandfather. Leave the trunk on the gravel."

My father stood outside the wicket door, peering nervously through the iron bars.

"Maasi ji," he said politely, holding out my allotment paper. "She is new. Room 34. Can I carry her trunk to the veranda? It is very heavy."

"Rules are rules, babu," she replied without looking up from her ledger. "If I let your feet touch this gravel, the warden will deduct five hundred rupees from my salary at the end of the month. The girl has two arms. Let her pull it."

My father looked at me, his eyes full of that helpless, aching apology that poor men give their daughters when they hit the brick wall of petty authority.

"It is alright, Baba," I said, forcing a steady voice. "I can pull it. You go back to the Metro station before the heat gets worse. Go home."

He hesitated. He reached into his pocket and pulled out a crumpled five-hundred-rupee note, folded into a tiny triangle. He pressed it into my palm, closing my fingers over it.

"Keep it inside your Quran," he whispered. "Do not show it to anyone. Call me from the PCO booth on Sunday afternoon. Recite Ayat-ul-Kursi before you sleep."

He turned and walked away down the dusty asphalt path, his shoulders hunched, his worn leather shoes kicking up small puffs of red dust. I stood at the threshold, watching his grey figure shrink until he disappeared behind the eucalyptus trees near the central library.

I turned back to the wicket door.

The green trunk weighed thirty kilograms. The gravel path was rough, filled with broken brick chips and sharp stones. I gripped the iron handle with both hands, bent my knees, and hauled it across the concrete sill. The metal bottom scraped against the stone with a terrible, screeching sound that echoed through the courtyard.

Maasi Sakina watched me with cold, indifferent eyes.

"Name?" she asked, dipping a rusted steel nib into an inkpot.

"Anam Sajjad."

"Department?"

"Political Science."

She wrote slowly, her gnarled fingers gripping the wooden penholder like an iron wrench.

"Room 34. East Wing. Third floor. Top of the stairs, turn left, last door on the right. You will share with five girls. If you lose your room key, the duplicate costs two hundred rupees. Curfew is five-thirty in the evening. At five-thirty-one, the iron bar falls across this gate. If you are outside when the bar falls, you sleep on the concrete outside until the morning warden arrives at eight."

"What if our afternoon lecture finishes at five in the department?" I asked.

She stopped writing. Slowly, deliberately, she lifted her head. Her yellowed eyes narrowed as she looked at me, as if an ant had suddenly spoken in fluent Urdu.

"Listen to me, girl," she said, her voice dropping to a harsh whisper. "You have just entered through that door. Do not bring your mouth in with you. In Khadija Hall, the clock belongs to the warden, not to your department. If your professor keeps you until five-fifteen, you run. If you cannot run, you drop the lecture. But if that iron bar falls while you are on Bosan Road, your name goes into the Red Book. Three entries in the Red Book, and your father receives a registered letter stating that his daughter is wandering the streets of Multan after dark. Do you want that letter to reach your village?"

My stomach turned to ice.

A letter like that in my village was not an administrative notice. It was a social death sentence. It was the kind of piece of paper that caused uncles to demand that a girl be locked inside the house and married off to the nearest available cousin before the family honor was stained.

"No, Maasi," I said softly.

"Then pull your trunk and climb the stairs," she said, spitting into her tin can again.

I dragged the trunk across the gravel.

The courtyard of Khadija Hall was a vast, bleak square of hard-packed earth where nothing grew except three stunted neem trees covered in white chemical dust from the nearby construction work. The four-story hostel building surrounded the square like the walls of a fortress. Every window on the first three floors was barred with thick criss-cross iron grates. On the fourth floor, the balconies were covered in corrugated fiberglass sheets that trapped the rising heat and turned the corridors into ovens.

Lines of cheap, faded plastic clotheslines criss-crossed the space between the pillars, sagging under the weight of wet dupattas, patched shalwars, and grey towels that smelled of borewell sulfur.

As I dragged my trunk toward the dark stairwell of the East Wing, I heard the sounds of two hundred female lives compressed into concrete boxes:

The hiss of illegal immersion rods boiling water in plastic mugs.

The rhythmic, dull thumping of wooden washing paddles beating wet clothes against concrete slabs in the communal washrooms.

A transistor radio playing an old Nusrat Fateh Ali Khan qawwali from a second-floor window, its batteries dying, the voice warping in the heavy heat.

And from somewhere down the corridor, the quiet, muffled sound of a young girl crying into her pillow, so soft that if you were not listening for it, you would think it was just the wind whistling through the razor wire on the roof.

I reached the bottom of the concrete staircase.

There were sixty-four steps to the third floor. The edges of the concrete steps were chipped and broken, exposing rusted iron reinforcement rods that stuck out like broken teeth.

I stood there, looking up into the dark stairwell. My hands were already blistered. My back throbbed with a dull, sickening ache.

I had thought that getting into the university on open merit, scoring ninety-two percent in my intermediate examinations, was the battle. I had thought that intellectual excellence was the coin that purchased your dignity in an institution of higher learning.

Standing at the bottom of those sixty-four concrete steps, looking up into the suffocating gloom of Khadija Hall, I understood my first political science lesson:

Excellence means nothing inside an empire of petty gatekeepers. Here, the only currency was endurance, and the only shield was the secret alliance of the women who lived behind the wire.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 4: Decoding Institutional Panopticons (Operating Under Surveillance)

1. **Map the Informal Hierarchy Immediately:** In every closed institution, the real power rarely resides in the person with the official title. The hostel superintendent signs the forms, but the gatekeeper, the sweeper, and the mess accountant control your daily reality. Identify who holds the keys, who logs the hours, and who handles the petty paperwork. Never fight a battle with a low-level enforcer; neutralize them through predictable compliance in public while building your independence in private.
2. **The Weaponization of Moral Terror:** Notice how administrative control in conservative societies is almost always framed as "moral protection." When an institution threatens your reputation rather than your academic standing, recognize it as an asymmetric intimidation tactic. Protect your flank: ensure all your official communications, gate passes, and lecture timetables are stamped, photographed, and filed before you leave any department.
3. **Physical Territory and Mental Sanity:** In high-density, shared institutional spaces, claim a physical perimeter immediately. Even if it is only a single wooden shelf or the space under your iron cot, establish absolute order over that space. Psychological sovereignty begins with the neatness of your immediate physical boundary.
"""

# ---------------------------------------------------------------------------
# 04_chapter_4.md
# ---------------------------------------------------------------------------
chapters['04_chapter_4.md'] = """# Chapter 4: The Currency of Sifarish (Allotment)

Room 34 measured fourteen feet by twelve feet.

The room had originally been built in 1982 to house two senior research scholars. It had two built-in brick alcoves for books, two narrow wooden wardrobes without locks, and one double casement window that looked out onto the boundary wall and the razor wire.

By 2024, through the magical arithmetic of university hostel administrations, Room 34 had been allotted to six girls.

When I pushed open the warped wooden door, the room was already full.

Four iron cots had been pushed together in pairs to create two massive communal sleeping platforms. In the narrow space between the two platforms, barely two feet wide, sat six tin trunks stacked three high like metal shipping containers. The air smelled of damp linen, Pond's talcum powder, and the sharp, sulfurous stink of bore water that had seeped through the washroom wall.

Sitting on the lower bunk nearest the window was a tall girl with fair skin, dark circles under her eyes, and a blue chiffon dupatta pinned tightly around her head with three steel safety pins.

She was unpacking a cardboard carton of books. When she saw me standing in the doorway with my green trunk, she stopped.

"You must be the sixth," she said. Her voice was flat, neither welcoming nor hostile, just the tired voice of someone who has seen an eviction notice arrive in the mail.

"Anam," I said, catching my breath. "Anam Sajjad. Political Science."

"Aqsa," she replied, wiping dust from a thick copy of Mazhar-ul-Haq's political theory textbook. "English Literature. Third semester. That is your corner."

She pointed with her chin toward the upper bunk on the left.

The upper cot was made of rusted angle iron with a sagging base of interwoven steel strips. On top of the steel strips lay a two-inch mattress made of recycled cotton waste that smelled faintly of kerosene. There was no pillow. There was no ladder. To get onto the cot, you had to place your foot on the lid of a tin trunk, grab the iron rail of the window, and haul yourself upward by your upper arms.

"Who are the other four?" I asked, sliding my trunk into the remaining six inches of floor space near the door.

"You will meet them when the sun goes down," Aqsa said, sitting cross-legged on her mattress. "Anza is at the library. Saba is at the administrative block trying to get her fee concession approved for the fourth time. Sidra is at the dispensary trying to get Panadol for her toothache. And Momina is somewhere in the art department avoiding the warden."

She looked at my green trunk, then at my face.

"Did your father pay a bribe for this allotment?"

The question was so blunt that it felt like a slap.

"No," I stammered, my cheeks burning. "I got this room on merit. First list. Ninety-two percent in intermediate."

Aqsa let out a short, dry laugh that sounded like dry leaves scraping across a brick floor.

"Merit," she said, shaking her head. "Girl, do you know why you are on the third floor in Room 34? Look out that window."

I walked over to the casement window and looked down.

Directly below us, twenty feet from the hostel wall, was the main drainage ditch for the northern campus. It was an open, concrete-lined nullah six feet wide, filled with black, sluggish sludge that smelled of rotten eggs and sewage. Swarms of black mosquitoes hovered over the water in clouds so thick they looked like smoke.

"The ground floor and first floor rooms facing the lawn are reserved for the daughters of section officers, deputy commissioners, and the nieces of senior professors," Aqsa said, leaning against the brick alcove. "They have two girls to a room. They have functional ceiling fans. Some of them have smuggled split air conditioners with private electricity lines tapped directly into the department transformer. But if you arrive here on pure merit, with a father who carries a clerk's pension card, you get Room 34 over the open sewer."

She leaned forward, her dark eyes fixing mine with an intensity that made me want to step back.

"Do you know who lived in this bed before you?"

"No," I whispered.

"A girl named Rabia. Economics department. From Bahawalnagar. Brilliant girl. Wrote research papers in Urdu and English. Her father died in her second year. When the fee hike came last autumn, her semester voucher went from twenty-eight thousand to forty-six thousand rupees. She went to the Warden's office every morning for three weeks with an application for the Student Welfare Fund."

Aqsa paused. The ceiling fan overhead gave a violent, metallic shudder, wobbling on its iron hook before settling back into its droning scrape.

"What happened to her?" I asked.

"The Warden told her that the welfare fund was exhausted," Aqsa said quietly. "Then the Assistant Warden told her that if she was truly needy, she should visit the home of a certain member of the university syndicate in Cantt on Sunday evening to have her application personally attested."

My hands went cold.

"Rabia did not go," Aqsa continued. "She sat on that very cot where your mattress is lying. She packed her tin trunk. She walked out through that green iron gate, took the Metro bus to the terminal, and went back to Bahawalnagar. She is married now to a cousin who runs a tire repair shop. She doesn't read books anymore."

Aqsa picked up her textbook and opened it to page one hundred and forty.

"That is what merit means inside these walls, Anam. Merit is what they make you believe in so you work sixteen hours a day to keep the university's ranking alive. But when the vouchers are printed, the only language this administration speaks is sifarish, money, or silence."

I sat down on the edge of my green trunk.

My hands rested on my knees. I looked up at the rusted angle iron of the bunk bed above me.

In my village, my uncles and neighbors had congratulated my father with garlands of yellow marigolds when the admission list was pinned to the board. They had said, *Sajjad sahib, your daughter is going to the university. She will become an officer. She will sit in an air-conditioned room with files.*

They did not know that the university was not an ivory tower. It was a market stall where the weak were traded for political peace, where every privilege had a price tag, and where a girl without a patron was expected to pay with her silence or her future.

I reached out and touched the cold iron rail of the bunk.

*Rabia gave up her bed,* I thought to myself. *She packed her trunk and she went back to the tire shop.*

I looked at Aqsa, who was marking a paragraph with a yellow highlighter.

"Aqsa?"

"What?"

"I am not packing my trunk."

Aqsa stopped her highlighter. She looked up over the rim of her reading glasses. For a second, just a fraction of a second, the hard, cynical armor around her eyes softened.

"Good," she said, her voice dropping to a low, steady pitch. "Because if you pack your trunk, they win without even throwing a punch. But if you stay, you need to understand one thing: the six of us in this room are not roommates. We are a garrison. We share the salt, we share the tea, and when one of us is under fire, we all hold the line. Do you understand?"

"I understand," I said.

And for the first time since my father had left me at the wicket gate, I did not nod.

I looked her straight in the eyes, kept my neck straight, and let the word stand on its own.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 5: The Asymmetry of Discretion (How to Maneuver Without Sifarish)

1. **Never Rely on Unwritten Promises:** When an administrator tells you, "Do not worry, beta, submit the paper and I will handle your fee concession later," they are neutralizing your immediate resistance with an unwritten promise they have no intention of keeping. In Pakistani institutions, verbal sympathy is the cheapest sedative available. Demand everything in writing: diary numbers, receipt stamps, and photocopied acknowledgments.
2. **The Defense of the Collective Unit:** When you lack individual political leverage, your only defense is horizontal solidarity. Corrupt administrations thrive by isolating dissenters, convincing each girl that she is alone in her struggle. Form an unbreakable information pact with your immediate circle. Share every administrative encounter, every subtle threat, and every fee irregularity immediately. When five women speak the exact same truth at the same time, the cost of silencing them multiplies exponentially.
3. **Refuse the Victim Mindset:** Recognizing that the system is rigged is not an excuse to despair; it is the prerequisite for strategic victory. Do not spend your emotional energy mourning the death of meritocracy. Accept the battlefield as it exists, master the regulations better than the clerks who enforce them, and operate with cold, disciplined precision.
"""

# Write batch 1 files
output_dir = 'manuscript'
os.makedirs(output_dir, exist_ok=True)

for fname, content in chapters.items():
    cleaned = clean_dashes(content)
    path = os.path.join(output_dir, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    words = len(cleaned.split())
    dashes = cleaned.count('\u2014') + cleaned.count('\u2013')
    print(f"Authored {fname}: {words} words, {dashes} dashes")

