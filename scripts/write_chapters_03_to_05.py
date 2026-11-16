# -*- coding: utf-8 -*-
"""
write_chapters_03_to_05.py
Authors Chapters 03, 04, 05 with deep narrative scenes (~2,500 - 3,500 words each).
Zero em-dashes or en-dashes.
"""
import os
import re

def clean(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

c03 = """# Chapter 3: Behind the Green Iron Gates

Khadija Hall did not look like a place of higher learning. It looked like a medium-security correctional facility built by people who deeply distrusted the concept of female literacy.

The boundary wall was twelve feet high, constructed from rough red bricks capped with two feet of rusted concertina razor wire. At the top of the wall, shards of broken brown glass bottles had been embedded into wet cement forty years ago, their jagged edges pointing toward the sky to deter anyone foolish enough to attempt an escape. The red brick was stained with black mold along the water pipes and covered in faded chalk slogans from previous student union campaigns: *Haq-o-Insaaf, Inqilab, Talba Rabita Council.*

The main entrance was a massive double gate made of heavy sheet iron, painted a sickly shade of dark green that had blistered and peeled under decades of southern Punjab sun.

Set into the right side of the massive iron gate was a smaller, narrow wicket door, barely four feet high and eighteen inches wide. To enter Khadija Hall, every resident had to bend their spine, lower their head, and step sideways over a sharp steel sill while dragging their belongings behind them.

The architecture itself forced you to bow before you took a single step into the compound. It was a physical rehearsal for the psychological obedience demanded inside.

Inside the wicket door sat Maasi Sakina.

She was an institution older than the university itself. A woman of indeterminate age, somewhere between fifty-five and seventy, with skin like dried leather, missing molars, and a permanent wad of chewing tobacco tucked into her lower lip. She sat on a low wooden charpai covered in a faded ralli quilt, positioned so that her gaze intercepted every single person who crossed the threshold. Her bare feet were cracked at the heels, grey with brick dust, and she wore a silver amulet wrapped in black thread around her withered ankle.

Next to her charpai was a heavy wooden table on which rested the Master Register: a massive, canvas-bound ledger with water-stained blue paper.

"Stop right there," Maasi Sakina rasped, spitting a stream of dark red tobacco juice into a rusted tin can behind her bed. "Father stays outside. No males past the green door. Not your father, not your brother, not your grandfather. Leave the trunk on the gravel."

My father stood outside the wicket door, peering nervously through the iron bars like a man visiting an inmate.

"Maasi ji," he said politely, holding out my allotment paper with both hands. "She is new. Room 34. Can I carry her trunk to the veranda? It is very heavy. Her hands will blister."

"Rules are rules, babu," she replied without looking up from her ledger. "If I let your feet touch this gravel, the warden will deduct five hundred rupees from my salary at the end of the month. The girl has two arms. Let her pull it. If she cannot pull her own trunk, she should stay home and stir the lentil pot."

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
2. **The Weaponization of Moral Terror:** Notice how administrative control in conservative societies is almost always framed as moral protection. When an institution threatens your reputation rather than your academic standing, recognize it as an asymmetric intimidation tactic. Protect your flank: ensure all your official communications, gate passes, and lecture timetables are stamped, photographed, and filed before you leave any department.
3. **Physical Territory and Mental Sanity:** In high-density, shared institutional spaces, claim a physical perimeter immediately. Even if it is only a single wooden shelf or the space under your iron cot, establish absolute order over that space. Psychological sovereignty begins with the neatness of your immediate physical boundary.
4. **The Principle of Silent Passage:** When entering or leaving an enclosure governed by petty gatekeepers, minimize all emotional display. Do not appear anxious; do not appear arrogant. Move with smooth, neutral efficiency. When you become memorable to an enforcer, you invite scrutiny; when you become routine, you gain operational invisibility.
"""

c04 = """# Chapter 4: The Currency of Sifarish (Allotment)

Room 34 measured fourteen feet by twelve feet.

The room had originally been built in 1982 to house two senior research scholars in botany. It had two built-in brick alcoves for reference books, two narrow wooden wardrobes without functional locks, and one double casement window that looked out onto the boundary wall and the razor wire.

By 2024, through the magical arithmetic of university hostel administrations, Room 34 had been allotted to six girls.

When I pushed open the warped wooden door, the room was already full.

Four iron cots had been pushed together in pairs to create two massive communal sleeping platforms. In the narrow space between the two platforms, barely two feet wide, sat six tin trunks stacked three high like metal shipping containers. The air smelled of damp linen, cheap rose talcum powder, and the sharp, sulfurous stink of saline bore water that had seeped through the washroom wall.

Sitting on the lower bunk nearest the window was a tall girl with fair skin, sharp features, dark circles under her eyes, and a blue chiffon dupatta pinned tightly around her head with three steel safety pins.

She was unpacking a cardboard carton of books. When she saw me standing in the doorway with my green trunk, she stopped her work.

"You must be the sixth," she said. Her voice was flat, neither welcoming nor hostile, just the tired voice of someone who has seen an eviction notice arrive in the mail.

"Anam," I said, catching my breath and wiping sweat from my forehead. "Anam Sajjad. Political Science."

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

Directly below us, twenty feet from the hostel wall, was the main drainage ditch for the northern campus. It was an open, concrete-lined nullah six feet wide, filled with black, sluggish sludge that smelled of rotten eggs and sewage. Swarms of black mosquitoes hovered over the water in clouds so thick they looked like smoke rising from a wet fire.

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

Rabia gave up her bed, I thought to myself. She packed her trunk and she went back to the tire shop.

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

1. **Never Rely on Unwritten Administrative Promises:** When an administrator tells you, "Do not worry, beta, submit the paper and I will handle your fee concession later," they are neutralizing your immediate resistance with an unwritten promise they have no intention of keeping. In Pakistani institutions, verbal sympathy is the cheapest sedative available. Demand everything in writing: diary numbers, receipt stamps, and photocopied acknowledgments. If they refuse a stamp, follow up with a registered postal letter. A postal receipt cannot be deleted from a ledger.
2. **The Defense of the Collective Unit:** When you lack individual political leverage, your only defense is horizontal solidarity. Corrupt administrations thrive by isolating dissenters, convincing each girl that she is alone in her struggle. Form an unbreakable information pact with your immediate circle. Share every administrative encounter, every subtle threat, and every fee irregularity immediately. When five women speak the exact same truth at the same time, the cost of silencing them multiplies exponentially.
3. **Refuse the Victim Mindset:** Recognizing that the system is rigged is not an excuse to despair; it is the prerequisite for strategic victory. Do not spend your emotional energy mourning the death of meritocracy. Accept the battlefield as it exists, master the regulations better than the clerks who enforce them, and operate with cold, disciplined precision.
4. **The Audit of Exploitative Conditions:** Document the material conditions of your allotment. If basic services (ventilation, clean water, structural safety) are denied based on socioeconomic discrimination, build an objective photographic and written record. Institutional exploiters fear external audits more than moral arguments.
"""

c05 = """# Chapter 5: The Circle of Seven (Room 34 Secrets)

By nine in the evening, the heavy heat inside Room 34 had settled into a dense, humid swamp.

Outside, the crickets in the eucalyptus trees screamed in a deafening, continuous pitch that sounded like high-voltage electric wires short-circuiting. The yellow bulb in the center of the ceiling flickered every time the compressor of the water cooler in the corridor kicked on, dimming to an orange wire before flaring back to life.

Room 34 was designed for four, stretched to six, and on most nights, functioned as the secret sanctuary for seven.

We called ourselves the Circle of Seven.

We came from seven different corners of Pakistan, from districts where girls were rarely allowed to see the inside of a high school, let alone an ancient university on Bosan Road. Each of us carried a public persona: the quiet student, the diligent notetaker, the obedient daughter who lowered her gaze in the seminar hall.

And each of us carried a secret that could have destroyed our lives if it reached the warden's desk.

First was **Aqsa**.

To the faculty of the English Department, Aqsa was a sharp, unsmiling student who wrote essays on postcolonial resistance and sat in the front row. To the hostel administration, she was a troublemaker who questioned water bills.

Her secret was hidden inside the hollow plastic tube of a broken desk lamp in the corner of Room 34. Inside that tube was a micro-SD card containing six issues of *The Red Gate*: an anonymous, photocopied two-page newsletter that appeared under hostel doors every three months. *The Red Gate* documented the exact figures of the hostel mess budget, the names of contractors who paid kickbacks to the assistant registrar, and the unreported cases of harassment by laboratory attendants. Aqsa wrote every word using an old offline tablet, printed the pages on an inkjet printer in Chungi No. 9 at midnight, and slid them under the doors while the wardens were asleep.

If she was caught, it would not be a hostel fine. She would be expelled under the university's anti-sedition bylaws and blacklisted from civil service examinations forever.

Second was **Anza**.

Anza was from a small village near Bahawalpur, studying sociology. She was the quietest girl in the room, with large, sorrowful eyes and a voice so gentle you had to lean close to hear her speak. She never complained about the watery daal in the mess. She never asked for tea.

Her secret was tucked inside a tin biscuit box beneath her iron cot. In 2023, her father's small cloth printing shop in the bazaar had gone bankrupt when the textile mill cancelled their credit. Her family was living on dry bread and borrowed flour. To pay her semester fee and send five thousand rupees home every month for her younger sister's school books, Anza stayed awake from midnight until four in the morning, sewing intricate shadow-work embroidery onto designer lawn shirts for the wives of senior professors.

She earned two hundred rupees per shirt. Her fingers were criss-crossed with tiny needle punctures that had turned blue under the skin. If the hostel warden discovered she was running an unauthorized tailoring trade inside Khadija Hall, she would be evicted within an hour for running a commercial enterprise on campus.

Third was **Saba**.

Saba was a third-year economics major from Vehari. She was an academic machine. While other girls chatted in the corridor, Saba sat on her cot with three highlighters in her hand, memorizing statistical formulas until her lips moved without sound.

Her secret was a stolen spiral notebook locked inside her suitcase. It was a handwritten grading ledger from the Department of Economics that she had found left behind on a lecturer's desk during exam evaluation. The ledger proved, with mathematical certainty, that female students were systematically given lower internal assessment scores than male students, regardless of their test performance, to ensure that the gold medals and university teaching assistantships went to male graduates who were expected to become breadwinners. Saba was quietly building a statistical correlation model using five years of department records, waiting for the exact moment to drop the file onto the Higher Education Commission's portal.

Fourth was **Momina**.

Momina was from Sahiwal, studying fine arts. She had wild, curly hair that escaped from her dupatta, ink stains on her thumbs, and a laugh that made the hostel guards outside the window grumble about female modesty.

Momina's secret was stitched directly into the underside of her cotton mattress. If you turned the mattress over and sliced a three-inch section of the yellow seam, you found thirty-five brilliant, satirical charcoal caricatures of the university administration: the Vice Chancellor sitting on a throne of broken water coolers, the Chief Warden counting bribes with three hands, and Dr. Qureshi lecturing to a lecture hall populated entirely by bowing sheep. They were masterpieces of political satire, drawn on heavy cartridge paper. In an authoritarian institution, political satire is considered treason.

Fifth was **Sidra**.

Sidra was from a conservative landed family near Khanewal, studying Urdu literature. She was gentle, deeply religious, and observant of every social propriety.

Her secret was the white envelope with the red seal that she kept beneath her pillow. Her paternal uncle, who controlled her deceased father's agricultural land, had finalized her engagement to a man eighteen years older than her, a cousin with two previous marriages and a reputation for drunken violence in the village. The wedding was scheduled for the end of the semester. Sidra had secretly made contact with an independent legal aid shelter in Lahore through a junior female lawyer in Multan. She was preparing to file a petition of legal autonomy the day her final exam paper was submitted, knowing that it meant she could never return to her village, never see her mother again, and would have to enter a state of total social exile to save her life.

Sixth was **Iqra**.

Iqra was a master of logistics from Lodhran, studying public administration. She was short, sharp-witted, and possessed a network of contacts that rivaled the university intelligence bureau.

Her secret was the hollow wooden base of the common study desk. Inside that cavity, wrapped in plastic medicine pouches, was an underground pharmacy and supply depot: ventolin inhalers, antibiotics, sanitary pads, emergency painkillers, and duplicate gate passes with forged hostel stamps. In Khadija Hall, where the dispensary closed at three in the afternoon and sick girls were left to shiver with typhoid on concrete floors, Iqra's underground pharmacy was the only reason three dozen girls had survived the winter without hospitalization. She charged nothing; she traded medicine for library books, fruit, and silence.

And seventh was **Palwasha**.

Palwasha was not formally allotted to Room 34. She lived down the hall in Room 41, but spent almost every evening sitting on our floor with her back pressed against my green trunk. She was from the tribal belt near Dera Ismail Khan, studying international relations on a provincial quota scholarship. She was tall, with high cheekbones, green eyes that looked straight through you, and a blunt directness that terrified the soft, polite girls from the Punjab plains.

Her secret was the burden of an ancestral blood feud that had claimed her father and two elder brothers when she was ten years old. Her family had sent her to Multan not just for an education, but to keep the last educated child alive. Palwasha carried an iron nail file sharpened to a razor point inside the lining of her boot, and she slept with her door unbolted because she believed that locked doors only trap you when the hunters arrive.

These were the seven women who sat in Room 34 on that humid night in late August.

We were not a random collection of roommates. We were an underground resistance cell operating inside the belly of a patriarchal machine.

Around ten at night, Iqra stood up from the floor, clicked the bolt of the room door into place, and hung a dark dupatta over the frosted glass transom so no light would leak into the corridor.

From under her cot, Anza pulled out a small plastic container filled with dry tea leaves, half a cup of sugar, and two green cardamoms. From under my bed, I pulled the contraband immersion rod and the dented steel mug.

Aqsa plugged the extension cord into the single wall socket behind the wardrobe, her eyes fixed on the door handle.

The immersion rod hummed. Within four minutes, the water was boiling, filling the cramped, airless room with the rich, clean aroma of cardamoms and black tea.

Palwasha took seven small plastic medicine cups from Iqra's supply box and poured three sips of hot tea into each one.

We sat in a tight circle on the floor, our knees touching, our shoulders pressed together in the narrow aisle between the iron cots.

Sidra held her hot plastic cup between both palms, staring down at the dark amber liquid.

"My uncle called my brother today," she whispered. Her voice was trembling. "He told him that he has already purchased the bridal tent. He said that if I do not arrive in Khanewal by the fifteenth of June, he will send four men in a pickup truck to the main gate of BZU to take me home."

The room went completely silent. The only sound was the droning scrape of the ceiling fan and the crickets outside the barred window.

Aqsa looked up from her tea. Her jaw was tight, her eyes cold as flint.

"Let him send the pickup truck," Aqsa said, her voice steady and sharp as a scalpel. "The fifteenth of June is four days after the final political theory exam. You are not going to Khanewal, Sidra. You are taking the eight-thirty morning Metro bus from BZU to Chungi No. 9. From there, Iqra has arranged a ride to the Daewoo terminal. You will be on the motorway to Lahore before your uncle's pickup truck even crosses the Chenab bridge."

"And what happens when he files a police abduction report against my brother?" Sidra asked, tears slipping down her cheeks.

"He cannot file an abduction report for a twenty-three-year-old woman with a national identity card and a registered affidavit of independent consent," Palwasha said, her green eyes fixed on Sidra. "My cousin in Lahore works with the women's legal collective. The affidavit is already drafted. The day you arrive, the High Court issues a protection order. In my homeland, we fight with rifles. In this city, you fight with affidavits and bus tickets. But you do not surrender. You never surrender to a man who treats your life like a sack of wheat."

Sidra swallowed. She looked at Palwasha, then at Aqsa, then at me.

She wiped her tears with the corner of her sleeve. Slowly, she took a sip of the hot tea.

"You really think I can do it?" she whispered.

"You have already done it," I told her, resting my hand on her knee. "The moment you refused to pack your trunk in your mind, you crossed the river. Now we just have to move your body."

In that tiny, suffocating room, surrounded by razor wire, open sewage, and the constant threat of administrative ruin, we drank our three sips of tea.

We had no political patrons. We had no money. We had no sifarish from senior bureaucrats.

All we had was the iron circle of our loyalty, the secrets we guarded for each other, and the unshakeable certainty that none of us would ever nod alone again.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 6: The Sisterhood Defense (Building Non-Compromised Alliances)

1. **Vetting for Horizontal Loyalty:** In a high-surveillance environment, never form alliances based on casual friendship or shared superficial interests. True institutional allies are vetted through shared adversity and discretion. Look for individuals who do not gossip about others' vulnerabilities, who do not boast about administrative connections, and who demonstrate the capacity to hold silence under pressure.
2. **Decentralized Resource Networks:** Do not depend on a single individual for your operational survival. In our circle, each woman owned a specific operational vertical: legal aid, medical logistics, editorial publishing, financial emergency reserves, and tactical evasion. When resources are decentralized, the elimination or compromise of one member cannot destroy the collective network.
3. **The Absolute Protection of Vulnerabilities:** A friend's secret is an unexploded ordnance. Never use a sister's vulnerability as conversational currency, even among trusted mutual acquaintances. The moment an institutional adversary detects a fracture in your circle, they will insert a wedge of fear or privilege to extract betrayal. Absolute, unbreachable secrecy is the only armor that holds against systemic pressure.
4. **The Law of Mutual Extraction:** When an ally faces an existential crisis (such as forced marriage, academic sabotage, or physical threat), formulate an extraction plan before the crisis reaches its climax. Panic during a crisis produces catastrophic mistakes; a pre-planned operational protocol executed with cold precision creates safety where none seemed possible.
"""

# Write batch files
output_dir = 'manuscript'
os.makedirs(output_dir, exist_ok=True)

files = {
    '03_chapter_3.md': clean(c03),
    '04_chapter_4.md': clean(c04),
    '05_chapter_5.md': clean(c05)
}

for fname, content in files.items():
    path = os.path.join(output_dir, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    words = len(content.split())
    dashes = content.count('\u2014') + content.count('\u2013')
    print(f"Wrote {fname}: {words} words, {dashes} dashes")
