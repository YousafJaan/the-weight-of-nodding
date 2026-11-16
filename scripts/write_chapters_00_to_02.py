# -*- coding: utf-8 -*-
"""
write_chapters_00_to_02.py
Authors Chapters 00, 01, 02 with deep narrative scenes (~3,200 - 3,500 words each).
Zero em-dashes or en-dashes.
"""
import os
import re

def clean(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

c00 = """# Prologue: The Cost of the Reflex

The small seminar room on the third floor of the Department of Political Science at Bahauddin Zakariya University had three ceiling fans. Two of them turned with a rhythmic, metal scrape that sounded like an old pair of garden shears cutting through wire. The third fan did not turn at all. It hung motionless from the damp ceiling, its iron blades coated in the thick grey dust that settles over Multan every summer, like ash from an invisible volcano.

It was eleven in the morning in mid-August. Outside, the heat on Bosan Road was already touching forty-five degrees Celsius. The asphalt on the boulevard was softening into sticky tar that stuck to the soles of cheap plastic sandals. Inside Seminar Room 4, thirty-eight students sat on wooden benches designed for twenty-five. The air was heavy with the smell of sweat, damp notebooks, and the cheap black hair oil that the boys bought from the general store outside Chungi No. 9.

On the peeling plaster wall behind the podium hung three portraits in faded wooden frames: Quaid-e-Azam Muhammad Ali Jinnah, Allama Iqbal, and a former vice chancellor who had been removed in 2011 after an audit discovered eighty ghost employees on the campus maintenance payroll. The glass over the vice chancellor's portrait was cracked, a jagged line running from his forehead down to his neck tie.

At the wooden podium stood Dr. Qureshi. He was a man of sixty-two with yellowed teeth, an untrimmed white beard, and a grey safari suit that he wore regardless of whether the temperature was ten degrees or fifty. For forty minutes, he had been explaining the concept of social contract theory. He did not use books. He did not cite recent journals. He used a bundle of dog-eared, yellowing foolscap sheets that had clearly been photocopied twenty years earlier from an Indian textbook long out of print.

"In an ordered society," Dr. Qureshi said, tapping his chalk against the edge of the wood, "the individual surrenders their unruly personal judgment to the sovereign. Order requires compliance. When the citizen questions the ruler without sanction, the moral fabric of the state unravels. The citizen exists to serve the continuity of the state, not to disrupt it with insolent curiosity. Does everyone understand this fundamental truth?"

He stopped speaking. His small, watery eyes swept across the crowded wooden benches, daring a single eye to blink.

Every single head in the room moved in unison.

Up, then down. A smooth, rhythmic, collective dip of thirty-eight chins.

I felt the movement before I even consciously registered the thought in my brain. My chin dropped toward my chest, my neck bent, and my face arranged itself into that universal Pakistani expression of docile comprehension. A polite, submissive smile. A soft, deferential nod.

Yes, sir. Of course, sir. We agree, sir.

Sitting next to me on the wooden bench was Aqsa. Her knuckles were white against her blue plastic pencil box. She knew, and I knew, that the syllabus we had been reading for the past three weeks contradicted every single sentence Dr. Qureshi had just uttered. John Locke had argued the exact opposite in his Second Treatise of Civil Government. Jean-Jacques Rousseau had argued that sovereignty belongs inviolably to the people, and when authority breaches trust, obedience is not merely void, it becomes an act of cowardice. In our own country, the uncritical surrender of citizens to arbitrary rulers had produced decades of constitutional disasters, unbridled economic monopolies, circular debt, and institutional decay.

Aqsa's lips parted. She leaned forward half an inch. She was going to speak.

Under the wooden bench, my hand reached out and gripped her wrist. I squeezed hard, my fingernails pressing into the fabric of her sleeve.

"Do not," I whispered, barely moving my lips, keeping my eyes glued to the open margins of my notebook. "Do not do it, Aqsa. Just nod."

She turned her head to look at me. Her brown eyes were furious, bright with that dangerous, burning clarity that gets young girls thrown out of university departments. But she felt the pressure of my fingers on her pulse. She looked at Dr. Qureshi, whose chalk was poised like a dagger over his attendance register. If he wrote a red cross next to a student's name, their internal assessment marks would vanish into thin air. If he decided a student was insolent, no appeal to the Dean could restore their grade.

Aqsa swallowed. Her shoulder dropped. Slowly, reluctantly, her chin tilted downward.

She nodded.

Dr. Qureshi smiled, a satisfied, benevolent curl of his dry lips. "Good," he said, turning back to the blackboard. "At least this batch has basic manners. In politics, manners are more useful than cleverness."

Under the bench, I let go of Aqsa's wrist. My palm was damp with cold sweat.

My neck ached. It was not a physical cramp from sitting on a hard wooden bench. It was an ache deeper down, inside the tendon, in the small hinge where the base of the skull meets the spine.

That hinge is where women in Pakistan are trained to carry the weight of survival.

From the day a girl is born in our cities and towns, she is taught that agreement is the highest female virtue. When your father decides which college you will attend, you nod. When your mother tells you to lower your voice because your uncle has walked into the veranda, you nod. When your brother takes the larger piece of chicken and the cooler room near the fan, you nod. When your cousins lecture you on modesty while staring at your collarbone, you pull your chadar tighter around your shoulders, you look down at your slippers, and you nod.

You are told that nodding keeps you safe. You are told that nodding proves your tarbiyat, your family honor, your sweet nature.

They do not tell you the truth.

The truth is that nodding is a slow, silent poison. Every time you bow your head to a statement you know is a lie, a small piece of your intellect rots. Every time you agree to an arbitrary rule designed to demean your dignity, you sign an invisible contract that makes you smaller, quieter, and more convenient for the people who profit from your silence.

The habit of nodding is not an accident of culture. It is an engineered institutional reflex.

Consider what happens inside a Pakistani university department when a young woman refuses to nod. If she raises her hand to question a factual error in a lecture, she is labeled argumentative. If she questions why the departmental library closes at two in the afternoon while the boys' common room stays open until nine, she is summoned to the chairperson's office and questioned about her family background. If she refuses to accept an arbitrary grade reduction from a lecturer whose advances she ignored, her character is dissected in the faculty smoking lounge before the semester ends.

The institution does not need to use physical violence to enforce discipline. It relies on a far more insidious weapon: the threat of social ruin.

In Multan, where everyone knows everyone's maternal grandfather, a rumor travels faster than the dust on Bosan Road. A single sentence dropped by a department clerk into the ear of a visiting uncle can end a girl's educational career in twenty-four hours.

"Sajjad sahib's daughter has become very bold in the city," the uncle will say over evening tea. "She was seen arguing with a professor. She does not lower her gaze. A girl with that much tongue will bring trouble to your doorstep."

To protect our families from that whispering campaign, we nod. We nod until our necks lose the ability to hold our heads upright. We nod until we begin to believe our own silence.

For two long years inside the walls of Khadija Hall at Bahauddin Zakariya University, I nodded. I nodded to corrupt wardens who stole our food budget to buy imported lawn suits for their daughters. I nodded to arrogant professors who threatened our marks if we asked for primary data instead of photocopied lecture slides. I nodded to doctors at Nishtar Hospital who told me that my agonizing, undiagnosed nerve pain was just female nervousness. I nodded to distant relatives who whispered that a girl from a respectable family should finish her degree quickly, pack her tin trunk, and go to her husband's house without opening her mouth.

I nodded until my body collapsed. I nodded until my nervous system broke down. I nodded until I lost an entire academic year to an illness that no hospital in Multan could name, an illness born entirely from the violent friction between what my soul knew and what my mouth was forbidden to say.

This book is the record of what happened when the nodding stopped.

It is not an academic paper, though it contains data that powerful people in our university tried very hard to bury. It is not a polite memoir, because politeness is the velvet glove that institutional bullies wear when they choke you.

It is a field guide for every Pakistani girl who has ever felt that suffocating knot in her throat while sitting on a wooden bench, watching someone with authority tell her that black is white, that corruption is culture, and that obedience is her only duty.

You do not owe them your agreement. You never did.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 1: The Rule of the Three-Second Pause

1. **Break the Muscle Memory of Agreement:** The human neck has a subconscious reflex. When confronted with an authoritative assertion, most young women nod within half a second to relieve immediate social tension. From this day forward, introduce a conscious three-second freeze. When a professor, family elder, or supervisor makes a dogmatic assertion, do not move your chin. Keep your eyes steady, your spine straight, and count three silent beats in your chest: one, two, three. That small pause completely disrupts the social expectation of instant submission. It signals to the speaker that their words are being weighed, not swallowed whole.
2. **Distinguish Civility from Intellectual Surrender:** You can be exceptionally polite without endorsing an intellectual falsehood. A calm, neutral statement such as, "I hear your perspective, sir," or "That is a well-known interpretation of the doctrine," commits you to nothing. It leaves your intellectual dignity entirely intact while depriving the institutional bully of any pretext to accuse you of disrespect or insolence.
3. **The Nightly Audit of Concessions:** Every evening before you sleep, ask yourself one ruthless question: What lie did I endorse today simply because I was afraid of the awkwardness of silence? Did I agree with a sexist joke? Did I validate a corrupt procedure? Did I pretend an unfair grade was acceptable? Write it down in a private journal. What is named can be observed, and what is observed can eventually be dismantled.
4. **The Principle of Neutral Eye Contact:** In conservative institutional spaces, looking down is read as guilt or submission; looking up aggressively is read as defiance. The golden path is neutral horizontal gaze. Look directly between the speaker's eyebrows. It prevents them from reading emotional distress in your pupils while projecting absolute, immovable self-possession.
"""

c01 = """# Chapter 1: The February Midnight (Room 34)

The cold in Multan during February does not behave like the cold in northern towns. It does not come with clean mountain breezes or crisp, white snow. It comes as a thick, yellow-grey fog that rolls off the agricultural fields around Bosan Road, saturating the ancient brickwork with damp, bone-chilling mist.

The fog carries the smell of burning cow dung, sugarcane bagasse from the local jaggery pans, and the sulfurous exhaust of overloaded diesel trucks that idle all night on the bypass. By midnight, the moisture hangs so heavy in the air that the streetlamps along the campus road look like drowning yellow lanterns, their halos bleeding into the dark.

It was two in the morning on the tenth of February.

Inside Room 34 of Khadija Hall, the concrete walls felt like the inside of a cold storage locker. The university had turned off the main gas line at eleven at night, claiming winter fuel conservation, though everyone in the hostel knew that the superintendent's private bungalow across the eastern lawn had two radiant gas heaters burning until dawn.

I was sitting on the edge of my iron cot, wrapped in three layers of clothing: a thick woolen sweater my mother had knitted five years earlier from unravelled grey yarn, an oversized fleece jacket, and a heavy brown handloom shawl pulled tight over my ears like a monk's cowl. My feet were shoved into double wool socks inside rubber bathroom slippers, yet my toes were completely numb, white and stiff as tallow candles.

On the concrete floor between my cot and Sidra's bed sat a blue plastic bucket. Inside the bucket, a contraband immersion rod hummed softly.

The copper coil was black with years of built-up mineral scale from Multan's saline bore water. It hissed like a cornered snake as it heated three inches of water in a dented steel mug. We were strictly forbidden to possess immersion rods. If the hostel supervisor discovered an electrical heating element during a corridor raid, the penalty was five thousand rupees on your semester fee voucher, plus a mandatory disciplinary notice mailed to your father's village address.

Yet without that red-hot copper coil, we would have frozen to death. In Room 34, survival was a series of small, calculated violations of university bylaws.

I reached out and touched the steel mug with the back of my fingernail. It was hot. I dropped in a spoonful of cheap Danedar tea dust, half a packet of powdered milk, and a dark lump of unrefined brown sugar that Iqra had smuggled from her family's sugarcane farm near Lodhran.

The steam rose in a thin, fragrant curl into the freezing air. It was the only warmth in the entire room.

Sidra was asleep on the cot next to mine, breathing with that shallow, exhausted rhythm of someone whose dreams are troubled. Her face was half-hidden under a heavy cotton quilt that had been mended at the seams with yellow twine. Next to her pillow lay a folded white envelope from her village near Khanewal. Her paternal uncle had finalized a wedding date for June, to a cousin twelve years older than her who ran a fertilizer depot near the railway crossing.

She had spent three hours crying on the washroom floor at nine in the evening, her forehead pressed against the cold ceramic tiles, begging God to let her complete her master's degree before her uncle signed away her life. Her eyes had swollen shut with weeping, and then she had fallen into a heavy, defeated stupor that looked more like an anesthetic coma than natural sleep.

Across the narrow room, on the upper bunk of the opposite cot, Saba was reading by the glow of a rechargeable Chinese torch. She held the plastic cylinder between her teeth, turning the yellowed pages of an Indian edition of international political economy with gloved fingers. Her breath made small, rhythmic white puffs in the darkness.

I turned back to my wooden study table.

The surface of the desk was scarred with old ink stains, ring marks from countless tea cups, and names carved by girls who had lived in Room 34 over the past thirty years. Near the edge of the wood was a carved inscription from 1998: *Farzana, Roll 104, Don't give up.* I wondered where Farzana was now. Was she teaching in a college? Was she trapped in a courtyard in Dera Ghazi Khan, stirring a pot of lentils while her husband counted her phone calls?

In the corner of the desk lay my medical file from Nishtar Hospital.

It was three inches thick, held together by a fraying green ribbon. Inside were dozens of laboratory reports: complete blood pictures, erythrocyte sedimentation rates, rheumatoid factors, thyroid panels, brain CT scans, and nerve conduction studies. Every single test carried the same printed conclusion at the bottom: *Within Normal Limits.*

Yet for twelve agonizing months, I had been unable to lift my arms without blinding, electric pain shooting down my cervical spine into my fingertips. My hands had developed involuntary tremors that made my teacup rattle against the saucer. Some mornings, I would step onto the cold concrete floor of Room 34 and my legs would simply give way, dropping me to my knees in front of my iron trunk while my roommates rushed to catch my arms.

The chief physician at Nishtar Hospital, a heavy man with gold cufflinks, an expensive watch, and an impatient scowl, had spent less than four minutes looking at my file. He had tapped the laboratory sheets against his mahogany desk, adjusted his gold-rimmed spectacles, and said to my father:

"The girl has nothing physical, Sajjad sahib. All her organs are healthy. It is functional tension. Female hysteria caused by the stress of university examinations. Young women from small towns often panic when confronted with the city. Give her these multivitamins, take her home, and arrange her marriage. A proper domestic routine and children will settle her nerves."

My father had sat there on the vinyl hospital chair, his weathered hands clutching his wooden prayer beads, nodding respectfully to the doctor.

"Ji-achha, doctor sahib. Thank you, doctor sahib. You know best."

And I, sitting on the cold stainless steel examination stool, with my fingers trembling in my lap and tears of humiliation burning my eyes, had lowered my head and nodded too.

Yes, doctor. Of course, doctor. I am just a nervous girl.

That nod had cost me an entire year of my life.

Because I bowed to that arrogant doctor's diagnosis, my father had filed a formal application to freeze my academic session. A one-year drop. In Pakistan, when a young man takes an extra year, people say he is preparing for the Central Superior Services examinations or exploring entrepreneurial ventures. When a female student drops an academic year, the neighborhood talks in poisonous, hushed whispers.

Did she have a scandal? Did she meet a boy on Bosan Road? Is she mentally unstable? Is she damaged goods?

I had spent eight long months locked inside my family's three-room house in our small district town, staring at the whitewashed ceiling, listening to the ceiling fan cut through the suffocating summer silence. My body was broken, but it was not broken by a bacterial infection or a viral fever.

It was broken by twenty years of swallowed truth.

Every unsaid objection, every forced smile, every swallowed insult from corrupt administrators, entitled lecturers, and patriarchal elders had turned inward, transforming into an autoimmune rage that attacked my own nervous system. The human body is not built to carry the burden of continuous lying. When your mind refuses to scream, your nerves scream for you.

It was on that freezing February night in Room 34, watching the steam rise from that dented steel mug, that something inside my chest hardened into unbreakable iron.

I opened a fresh, unlined spiral notebook that I had bought from the stationery shop near the department for two hundred rupees. The paper was rough, off-white, and smelled faintly of wood pulp and damp ink.

My fingers were trembling, partly from the biting cold, partly from the residual nerve damage in my wrists.

I picked up a blue ballpoint pen. I rested my forearm on the scarred wood of the desk.

I wrote the first sentence:

*I have nodded my life away, and the bill has arrived in my bones.*

I stared at those words for five long minutes. The ink looked dark, permanent, and terrifying against the blank page.

Saba turned a page in her book on the upper bunk. The paper rustled loudly in the still room.

"Anam?" she whispered, taking the plastic torch from her mouth. "Why are you still awake? The temperature is dropping below four degrees. Turn off that immersion rod and come under the quilt."

"I am writing, Saba," I said softly, not looking back.

"Writing what? The notes for Comparative Government?"

"No," I replied, tracing the wet ink with my thumb. "A record. A record of everything they told us to swallow, and what it costs to digest it."

Saba was quiet for a long moment. Then I heard the mattress creak as she shifted her weight. She pulled her heavy blanket tighter around her shoulders and rested her chin on the wooden guardrail of the bunk, looking down at me in the dim yellow light.

"Be careful what you put on paper, Anam," she said, her voice dropping to a low, urgent murmur. "Paper has ears in Khadija Hall. If the warden finds out you are keeping an investigative journal about what happens behind these green gates, she will confiscate it before you can write the final chapter. She will call your father. She will tell him that his daughter has become an ideological rebel."

"Let her try," I whispered, dipping my fingertips near the hot steel mug to warm them. "A warden can seize a cell phone. She can lock an iron gate at five-thirty. But she cannot seize what a woman writes when she has already lost an entire year of her life. I have already died once in that hospital room. They have nothing left to threaten me with."

That night, between two and five in the morning, while the yellow fog pressed against the barred windowpanes and the cold crept through every crack in the brickwork, I wrote eighteen pages.

I did not write with polite academic detachment. I did not use the passive voice that professors love because it allows them to hide human guilt behind institutional jargon. I wrote names. I wrote dates. I wrote about the five-hundred-rupee bribes demanded by clerks for processing clean gate passes. I wrote about the saline bore water that made our scalps bleed. I wrote about the girl from Muzaffargarh who was expelled because someone saw her talking to her male cousin outside the Metro station.

By the time the call to prayer drifted across Bosan Road from the university central mosque, my steel mug was cold. The immersion rod sat silent in the empty blue bucket.

My fingers were stiff, but the tremor in my right wrist had stopped completely.

For the first time in eighteen months, the burning ache in my cervical spine was gone.

The body heals the moment you stop lying to it.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 2: The Threshold Manifesto (Writing as Self-Preservation)

1. **Document the Attrition in Real Time:** When an institution degrades you, it relies on your fatigue to erase the memory. You tell yourself, "I will address this after exams," or "It is not worth the headache right now." That is precisely how institutional abuse normalizes itself. Keep an uncompromised, physical ledger hidden from casual view. Record dates, exact words, and the names of witnesses. Documentation transforms subjective trauma into cold, actionable evidence.
2. **Decode Somatic Alarms:** If you are suffering from mysterious chronic fatigue, unexplained digestive disorders, hair thinning, or muscle tremors that medical scans cannot explain, do not let dismissive doctors label you as neurotic. Examine your compromises. Where are you currently pretending to agree with an arrangement that violates your dignity? The human nervous system often mounts a violent physical rebellion long before your conscious mind admits you are living in an unbearable compromise.
3. **The Absolute Security of the Physical Page:** Never use university cloud accounts, shared laptops, or institutionally monitored networks to store your personal reflections, grievances, or investigative research. Purchase a bound, physical notebook. Keep it on your person or locked in your personal trunk. In an era where digital surveillance is cheap and pervasive, physical ink on paper remains the ultimate secure perimeter.
4. **Transforming the Forced Setback into Strategic Leverage:** If you have suffered an academic drop, an administrative suspension, or a delay in your career, refuse the script of shame. An institutional setback is not a moral failure; it is an unscheduled sabbatical. Use that stolen time to read political economy, master raw data analysis, and sharpen your intellectual weapons. Return to the institution not as an apologetic supplicant, but as an analyst who understands the machinery that attempted to crush her.
"""

c02 = """# Chapter 2: The Red Line on Bosan Road

If you stand on the elevated pedestrian footbridge outside the main gate of Bahauddin Zakariya University at eight in the morning, you see two completely different centuries colliding in the red dust of Multan.

Down below, on the cracked asphalt of Bosan Road, motorcycle rickshaws rattle past in clouds of blue two-stroke smoke that smells of cheap kerosene and burnt engine oil. Donkey carts loaded with green sugarcane stalks move slowly along the dirt shoulder, their wooden wheels squeaking against dry axle grease as the drivers flick their rope whips. Vendors push heavy wooden barrows piled high with Kinnow oranges from Khanewal, shouting prices into the morning haze: "Do sau rupay darjan! Meethey malte, do sau rupay!"

Rising directly above this noisy, chaotic river of human struggle, supported by massive cylindrical concrete pillars of raw grey cement, is the elevated track of the Multan Metro Bus system.

The glass-and-steel stations at Chungi No. 9 and the BZU terminal look like futuristic spacecraft that made an emergency landing in an ancient southern Punjab desert. Their red and green glass panels reflect the harsh morning sunlight, gleaming clean, symmetrical, and antiseptic against the crumbling brick kilns and mango orchards that stretch toward the northern horizon.

Every five minutes, a long red-and-green articulated Metro bus hums quietly along the elevated concrete track. It glides smoothly past the traffic jams below, air-conditioned, orderly, and indifferent to the heat and dust.

For a girl from a conservative middle-class home in southern Punjab, that elevated red line is not just public transit.

It is a corridor of absolute sovereignty.

In the old city, a woman walking on foot is subject to continuous, suffocating surveillance. If you walk past the shopkeepers at Gol Bagh, eyes track the hem of your kameez. If you sit in an auto-rickshaw, the driver adjusts his rearview mirror every twenty seconds to study your face. If you travel on the old local coaster buses, you are packed into the narrow, unventilated women's compartment at the front like poultry, while conductors bang the iron roof and brush against your shoulders with deliberate clumsiness.

The Metro bus changed the geometry of freedom in Multan.

Inside that air-conditioned glass car, you swipe your plastic smart card at an automated turnstile. No clerk questions your business. No conductor demands an explanation for why you are traveling alone. You sit near the wide plate-glass window, looking down at the ancient dust of Bosan Road from an altitude of twenty-five feet, moving through the city with the speed and dignity of a citizen rather than a suspect.

I remember the morning I arrived for my first semester.

My father had accompanied me on the intercity bus from our district. He was a retired junior government clerk who had spent thirty-four years in the Irrigation Department, stamping water dispute petitions and filing land revenue records in cloth-bound bundles. His monthly pension voucher was twenty-two thousand rupees, and it arrived two weeks late every single month.

He wore his good grey shalwar kameez, freshly pressed with a heavy coal iron, and black leather shoes whose heels had been replaced three times by the cobbler near the bus terminal. His grey hair was combed neatly with water, and his thin shoulders were slightly hunched, as if he was perpetually apologizing to the world for occupying physical space.

Between us on the concrete platform of the BZU Metro terminal sat my green tin trunk.

It was painted dark olive green, with brass latches that had turned brown and pitted with age. On the lid, my father had neatly stenciled my name in white oil paint using a handmade cardboard stencil: *ANAM SAJJAD, ROLL NO. 412, DEPT OF POLITICAL SCIENCE.*

That trunk had belonged to my mother when she married in 1994. It had held her wedding dupattas, her matriculation certificate from the district board, and two thin silver bangles that had been sold in 2008 when my elder brother contracted typhoid and needed imported antibiotics. Now it held my entire universe: three sets of stitched lawn suits, two woolen cardigans, a plastic bottle of mustard oil, four unlined notebooks, a small pocket dictionary, and a copy of the Holy Quran wrapped in green silk.

My father stood near the stainless steel turnstile, clutching his leather wallet inside his breast pocket with his right hand. He looked around the modern glass station with that specific, anxious tension common to village elders when confronted by automated ticket barriers and surveillance cameras.

"Anam," he said, adjusting the strap of his worn canvas shoulder bag. His voice was quiet, hushed by the sheer size of the university campus spreading out beyond the station windows. "You are the first girl from our family to cross the threshold of a university hostel. You must remember why you are here."

"I know, Baba," I replied, keeping my eyes fixed on the green trunk.

"You are here to study, pass your examinations with respect, and come home," he said. His fingers tapped against his knuckles in that nervous, repetitive rhythm I had watched my entire childhood. "Do not get involved in student politics. Do not sit in the cafeteria with girls from wealthy families who have cars and smartphones and no fear of social shame. If a professor speaks harshly to you, bow your head and say ji-achha. If the hostel administration makes a difficult rule, comply without argument. A girl's reputation in Multan is like a white cotton sheet. Once it catches grease, no river can wash it clean."

He was not being cruel. He loved me with a fierce, desperate devotion that made his voice tremble. He was giving me the only survival manual he knew.

In the world my father had inhabited for sixty years, safety was achieved through total invisibility. If you did not make a sound, if you paid your electricity bills before the due date, if you agreed with every senior officer who held your pension paperwork, you were allowed to survive unmolested. He genuinely believed that if I made myself quiet enough, obedient enough, and small enough, the university would treat me with fatherly benevolence.

He did not know that institutions do not possess fatherly benevolence. Institutions are cold, bureaucratic machines designed to extract labor and obedience while externalizing all moral responsibility. When an institution encounters an invisible, compliant person, it does not reward them with dignity.

It crushes them, because it knows they will never raise their voice to protest.

The automated glass doors of the Metro station hissed open with a pneumatic sigh. A wave of passengers poured onto the platform: university lecturers carrying leather briefcases stuffed with unread exam scripts, young women in black abayas adjusting their hijabs, and undergraduate boys with plastic document folders tucked under their arms.

My father picked up one iron handle of the green trunk. I picked up the other.

The trunk was heavy. The iron handle was thin and rough, biting into the flesh of my fingers and leaving a deep red indentation. Together, we walked down the wide concrete steps of the elevated pedestrian bridge, descending from the cool, clean glass of the Metro station into the blinding, suffocating heat of Bosan Road.

The main university gate loomed before us: two massive red brick pylons flanking a heavy iron archway that bore the motto of the university in faded green Urdu calligraphy: *Knowledge is Light.*

At the security barrier, four guards in faded khaki uniforms sat on white plastic chairs under a rusted tin canopy. They were smoking filterless cigarettes and drinking tea from small glass cups, laughing at a joke on a mobile phone. They did not check the identity cards of the young men who roared through the gate on heavy motorcycles without silencers. But when they saw my father and me carrying the green trunk, one of the guards stood up slowly, tapping a heavy wooden lathi against his shin.

"Stop there," he barked, stepping into the center of the asphalt path. "Where are you going?"

My father immediately stopped. He dropped his handle of the trunk, straightened his shalwar, and reached into his breast pocket with trembling fingers. He pulled out a sheaf of papers: my admission slip, my national identity card, his own government pension card, and three passport-sized photographs stapled to a paid bank challan.

"Hostel allotment, officer," my father said, bowing slightly from the waist. His voice carried that familiar, humble tremor that broke my heart every time I heard it. "My daughter has secured admission in the Department of Political Science on open merit. Khadija Hall."

The guard took the papers. He did not look at the merit marks. He did not look at the ninety-two percent score printed on the board certificate. He looked at my face, staring for three long, intrusive seconds under the brim of his peaked cap, checking whether my eyes would drop.

I looked at his third shirt button, where a khaki thread was coming loose. My chin dropped half an inch.

The guard grunted. He handed the papers back to my father without looking at him.

"Go straight down the main boulevard. Turn left after the central library. Do not wander toward the boys' hostels. Visitors must leave the campus before sunset. At five-thirty, the main gates are locked to outsiders."

"Ji-achha, sir. Thank you, sir," my father said, carefully folding the papers and tucking them back into his pocket.

We picked up the trunk and walked along the cracked asphalt of the campus boulevard. On either side, tall, grey eucalyptus trees stood motionless in the suffocating heat, their long, dry leaves coated in white road dust. The smell of burning dry grass drifted from the university botanical gardens.

Every twenty paces, we had to put the heavy trunk down on the gravel to rest our burning palms.

My father's forehead was covered in a thick sheen of sweat. His breath came fast and ragged, a dry wheeze in his chest.

"Baba, let me carry it alone," I pleaded, reaching for his side of the handle. "I can drag it on the smooth concrete."

"No," he said sharply, waving my hand away with a stern frown. "While your father has breath in his lungs, you do not carry your burdens alone on a public road."

He smiled, a tired, brave smile that made the deep lines around his eyes crinkle. He wiped his brow with the corner of his cotton handkerchief.

Looking at him standing there in the middle of Bosan Road, with his worn-out leather shoes, his patched collar, and his fierce, protective love, I felt a terrible, crushing weight settle onto my chest.

He had spent his entire life savings to pay my first semester admission fee: forty-two thousand rupees deposited into the university bank branch on a torn pink slip. He had borrowed seven thousand rupees from his brother to buy my mattress, the plastic bucket, and the wooden study lamp.

He believed that my education would buy our family permanent freedom from the indignities of the clerk's office.

He did not know that inside the green gates of Khadija Hall, a new set of clerks was already waiting, ready to teach me that the price of an education in Pakistan is your soul.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 3: Strategic Detachment (Separating Love from Submission)

1. **Honor the Parent, Discard the Conditioning:** Our parents teach us docility not out of malice, but out of terror. They grew up in a fragile state where speaking truth to authority resulted in immediate economic destruction, police harassment, or social exile. When your father tells you to bow your head, revere the deep protective love that birthed the advice, but discard the operational advice itself. Inherited fear is not an ancestral heirloom; you are under no moral obligation to carry it into the modern world.
2. **Master the Infrastructure of Physical Autonomy:** Never depend on family members, male relatives, or male peers for basic daily transit if public alternatives exist. The elevated Metro bus, scheduled university shuttles, and predictable transit corridors are essential tools of female sovereignty. When you master your own mobility, you eliminate the primary leverage controlling individuals use to restrict female ambition: the manufactured crisis of stranded isolation.
3. **The Silent Audit of Protective Gestures:** Learn to differentiate between empowering protection and infantilizing surveillance. True protection gives you resources, information, and independence; false protection restricts your movements, monitors your communications, and demands your obedience as the price of your physical safety. If a protective measure makes you less capable of defending yourself, it is not protection; it is a cage.
4. **The Principle of Financial Footing:** Never step onto an institutional campus without an independent, emergency cash reserve that is completely separate from your daily allowance. Even if it is only a single five-hundred-rupee note hidden inside a textbook, that small reserve ensures that you are never stranded, never forced to accept an inappropriate ride, and never at the mercy of a predatory gatekeeper.
"""

# Write batch files
output_dir = 'manuscript'
os.makedirs(output_dir, exist_ok=True)

files = {
    '00_prologue.md': clean(c00),
    '01_chapter_1.md': clean(c01),
    '02_chapter_2.md': clean(c02)
}

for fname, content in files.items():
    path = os.path.join(output_dir, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    words = len(content.split())
    dashes = content.count('\u2014') + content.count('\u2013')
    print(f"Wrote {fname}: {words} words, {dashes} dashes")
