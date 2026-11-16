# -*- coding: utf-8 -*-
import os

def clean(text):
    text = text.replace("—", ", ").replace("–", ", ")
    while "--" in text:
        text = text.replace("--", ", ")
    return text

def assert_no_dashes(text, filename):
    for dash in ["—", "–"]:
        if dash in text:
            raise ValueError(f"Found forbidden dash '{dash}' in {filename}!")
    if "--" in text:
        raise ValueError(f"Found forbidden double-dash in {filename}!")

# Chapter 1
ch1_content = clean("""# Chapter 1: The February Midnight (Amna Hall, Room 42)

Inside Room 42 of Amna Hall, the concrete walls felt like the inside of a cold storage locker. The university administration had turned off the main gas line at eleven at night, claiming winter fuel conservation, though everyone in the hostel knew that the superintendent's private bungalow across the eastern lawn had two radiant gas heaters burning brightly until dawn.

I sat at the narrow wooden table near the corner window, wrapping a faded wool shawl tightly around my shoulders. My fingers were stiff from the cold, but my ballpoint pen moved steadily across the unlined pages of my notebook. The date was February 14, 2024. Outside, the night fog hung heavy over the eucalyptus trees of Bahauddin Zakariya University, blanketing Bosan Road in a white, soundless mist that swallowed the headlights of occasional long-distance freight trucks heading toward Khanewal.

Behind me, in the dim glow of our small emergency lamp, my two roommates lay asleep under heavy floral quilts. On the left cot was Anza, her face turned toward the bare wall, breathing with the quiet, delicate rhythm of someone who treated the entire world as an intrusion. On the right cot slept Sara, our senior roommate, exhausted after ten hours in the university chemistry laboratory. Their presence was a steady, rhythmic comfort in the silence.

Room 42 was our small, contested fortress inside Amna Hall. Amna Hall was universally acknowledged among the girls as the most cherished and beautiful hall on the BZU campus, with its wide central courtyard, arched brick corridors, and the sprawling rose bushes that bloomed fiercely every February. Yet beauty in a public university hostel never softened the harshness of institutional life. The hostel was built to house two hundred girls; by 2024, more than five hundred of us were crammed into its three residential wings.

On my desk sat a glass of lukewarm tap water and a rusted single-coil electric stove plugged into an illegal extension board beneath my cot. Heating water on an exposed heating coil was strictly forbidden by hostel bylaws. Every Tuesday morning, the sub-warden made her inspection rounds, swinging her heavy brass key ring and threatening to confiscate appliances and impose five-thousand-rupee fines on anyone caught using unauthorized coils. Yet without that red-hot copper wire, winter in South Punjab was an endurance test that broke your body. In Room 42, survival was an art of calculated, silent defiance.

I was twenty-two years old, an honors student in the Department of Political Science, and I was quietly falling apart.

For over a year, an undiagnosed medical storm had been raging through my body. It had begun in the middle of my second year as a dull, constant ache along my neck and cervical spine, before branching into sharp electric shocks that shot down my arms into my fingertips. Some mornings, my hands shook so violently that my teacup clattered against its saucer. Other days, when I stepped out of bed onto the freezing concrete floor, my knees would buckle without warning, dropping me onto the dusty rug before Anza or Sara could jump up to catch my elbows.

We had visited the government clinics in Multan. We had sat on the peeling green benches of Nishtar Hospital while junior medical officers glanced at my blood charts for twenty seconds, scribbled prescriptions for cheap multivitamins and pain relievers, and told my father that female university students suffered from psychological hysteria brought on by examination stress. They dismissed my pain because I looked quiet, because I did not scream, because when the physician pressed his cold thumb into my inflamed cervical joints, I merely bit my lower lip and nodded.

That silent nodding was the real disease.

Growing up as a daughter in a traditional family from South Punjab, nodding was the first and most fundamental discipline taught to a girl. You nodded when your relatives dictated which degree was respectable for a young woman. You nodded when the transport committee cancelled the women's university shuttle because the fuel budget was diverted to executive staff cars. You nodded when a male department chairman made inappropriate comments about your attendance before signing your scholarship voucher. You nodded to preserve peace, to avoid scandal, to protect your father from shame, and to prove that education had not made you insolent or rebellious.

Every nod was supposed to be a virtue. In our culture, a girl who nods is called virtuous, sabir, and well-raised. But no one tells you the true physiological arithmetic of compliance. When you swallow your voice to keep the room calm, that swallowed protest does not disappear. It calcifies into poison inside your tissue. It settles into your joints, inflames your vertebrae, and tightens around your throat like a wet leather strap.

On that freezing February night in Room 42, watching the yellow bulb flicker against the damp wall, I realized a terrifying truth: if I kept nodding, this institution would slowly consume my youth and bury my intellect without ever acknowledging what it had taken.

I dipped my pen into the blue ink. Across the top of the crisp white page, I wrote seven words that felt like a quiet declaration of war against my own upbringing:

*The Weight of Nodding.*

I did not begin this chronicle to produce literature. I began it as an autopsy of survival. I wanted to record, with the rigorous empirical discipline of a political scientist, exactly what happens to a woman when she agrees to endure institutional injustice in exchange for the permission to study. I wanted to document the hidden life of Amna Hall, the secret heartbreaks of my circle of friends, the economic fractures of Pakistan that our leaders cover with patriotic slogans, and the quiet courage of young women who fight daily battles inside corridors that were designed to silence them.

The yellow bulb gave a sudden pop, plunging Room 42 into absolute darkness.

Across the room, Anza stirred beneath her floral quilt, coughing softly against the cold night air. I did not move. I sat in the darkness, listening to the midnight wind sweep through the eucalyptus branches outside on Bosan Road. My hands were freezing, my neck burned with pain, but my mind was completely awake.

The book had begun.

***

### The Strategist's Margin: Tactical Protocols for Daring Women

1. **Audit the Real Cost of Your Agreement:** Whenever you feel compelled to say yes to an unjust demand, pause for sixty seconds. Ask yourself plainly: what part of my health, dignity, or future am I paying to keep this peace? Compliance is never free; it is merely billed to your future self at compounded interest.
2. **Transform Pain into Primary Documentation:** When an institution denies your suffering, stop arguing with its functionaries. Begin recording dates, names, budgets, and specific violations in an unalterable notebook. Personal agony becomes political leverage only when it is transformed into rigorous empirical evidence.
3. **The Shield of Controlled Silence:** Do not confuse strategic silence with passive surrender. True silence is an observation post, not a white flag. Watch the room, analyze the incentives of the men who hold administrative power, and conserve your energy until you hold the documentary leverage to strike decisively.
""")

assert_no_dashes(ch1_content, "01_chapter_1.md")
with open("manuscript/01_chapter_1.md", "w", encoding="utf-8") as f:
    f.write(ch1_content)
print(f"Updated Chapter 1: {len(ch1_content.split())} words")

# Chapter 2
ch2_content = clean("""# Chapter 2: The Red Line on Bosan Road (Amna Hall & The Allergy Protocol)

The morning alarm in Room 42 of Amna Hall did not ring from a phone. It began at five-fifteen with the sound of metal buckets clattering against the concrete floor of the communal washrooms down the western corridor.

By five-thirty, sixty girls were standing in the chilly gallery, clutching plastic mugs and bars of cheap soap, waiting for their turn under the three functional water taps. In the winter months, the university boiler was an ornamental myth; the water that gushed from the rusted iron pipes was freezing cold, drawn directly from the subsoil pumps of Multan. To wash your face was to feel needles of ice piercing your forehead.

I returned to Room 42 with a plastic jug of cold water and placed it on the floor next to our wooden tea table.

On the cot nearest the window, Anza was already awake, sitting cross-legged under her floral quilt. She was wrapped in three woolen sweaters, with a woolen cap pulled down to her eyebrows. Her dark eyes were scanning the floor with sharp, suspicious intensity.

"Anam," Anza announced before I could even hang my damp towel on the iron drying rack. "There is dust near the trunk. If anyone moves that broom, I will have an asthma attack before the first lecture."

I could not help but smile. In Amna Hall, every resident had an operational specialty, and Anza's specialty was her legendary, immovable Allergy Protocol.

Anza was one of the dearest, most loyal friends I would ever have in my life, but living in a twelve-by-fourteen room with her was an exercise in continuous domestic negotiation. She possessed a phobia of hostel dust that bordered on performance art. Whenever it was her turn to sweep the floor or wipe down the ceiling fan blades, she would immediately clutch her throat, produce a dry, theatrical cough, and declare that the fine Multani silt was triggering her chronic respiratory allergies.

"Mujhe allergy hoti hai," she would say with wide, innocent eyes, tucking her hands securely inside her sleeves. "If I touch that broom, my hands will break out in red rashes and my throat will swell shut. You sweep, Anam. I will supervise and inspect the corners."

Sara, who was ironing her laboratory coat on a towel spread over her cot, burst out laughing.

"Anza, you have an allergy to sweeping, you have an allergy to washing the tea cups, and you have an allergy to carrying the laundry bucket down the stairs," Sara teased, pressing the hot iron onto her white collar. "The only thing in South Punjab you are not allergic to is sitting on that bed and drinking four cups of cardamoms tea while Anam cleans the room!"

"Sara baji, you do not understand medical science," Anza replied with total seriousness, refusing to break character. "Multani dust contains micro-particles from the brick kilns. A sensitive girl cannot expose her lungs to such trauma."

That was Anza: charming, stubborn, effortlessly critical of every tiny irregularity in our environment, yet fiercely defensive of us whenever any outsider threatened our room. If a sub-warden tried to harass us about our curfew signatures, Anza would transform from a frail allergic invalid into an aggressive advocate, quoting university regulations with such rapid-fire ferocity that the wardens would back out of our doorway in confusion.

Just as I finished sweeping the dust toward the door, the wooden screen rattled, and two heads peeked inside.

It was **Aqsa** and **Saba**, our neighbors from the adjoining gallery.

Amna Hall was divided into interconnected wings, and our Room 42 was connected via a short covered corridor to the eastern portion where Aqsa and Saba lived. Although they technically resided in the adjacent portion, they spent eighty percent of their waking hours inside our room, crowded around our tea kettle or sitting on our rugs.

Aqsa stepped inside first, slipping off her black sandals at the door.

She was from a conservative rural basti on the outskirts of Muzaffargarh, across the Chenab River. Aqsa was striking in her simplicity: fair-complexioned, with soft, innocent features and large, gentle eyes that held the wide, untamed trust of village life. She was deeply religious, modest, and carried herself with an earnest, unpretentious sweetness.

Before arriving at Bahauddin Zakariya University, Aqsa had made a sacred pact with her family and with herself. She had promised her father that university life would not corrupt her rural values. She wore a strict, flowing black abaya that covered her from shoulders to feet, accompanied by a modest dark scarf pinned tightly beneath her chin.

"University is only for my degree," Aqsa had declared to all of us during our very first week in Amna Hall. "I will never wear modern clothes. I will never do fashion. I will keep my gaze lowered on the footpath. I will never look at any boy, and I will certainly never, ever fall in love. Love is a trap that destroys an honorable girl."

We had all nodded solemnly in agreement, admiring her resolve. None of us knew that within six months, Aqsa's heart would become the epicenter of the most turbulent emotional earthquake Amna Hall had ever witnessed.

Behind Aqsa came Saba.

Saba was from Vehari, sharp-featured, practical, and carrying an air of quiet maturity that made her seem older than the rest of us. Saba was already formally engaged back home to a respectable cousin, a match arranged by her parents with full family approval. She wore a thin silver ring on her left finger, which she polished compulsively with the corner of her dupatta whenever she was nervous.

"Anam, is the kettle boiling?" Saba asked, closing the door behind her and sitting down on the edge of Anza's cot. "The corridor is freezing. If I do not get tea, I will fall asleep during Constitutional Law."

Before I could answer, the door opened again, and in walked **Palwasha**, carrying a metal plate piled high with warm, freshly fried parathas wrapped in newspaper.

Palwasha was an absolute darling. She lived down the hall, but she was an inseparable part of our circle. Tall, cheerful, with a natural, blooming sweetness that instantly disarmed everyone she met, Palwasha had the rare gift of bringing pure warmth into the grimmest situations. While the rest of us analyzed problems and dissected university politics, Palwasha focused on making sure everyone was fed, warm, and smiling.

"Hot parathas from the canteen gate," Palwasha announced proudly, setting the plate on our tea table. "I fought with the canteen boy for fifteen minutes to get them fresh off the tawa before the seniors grabbed the entire batch."

For the next twenty minutes, Room 42 was transformed into a paradise of female laughter and shared food. We tore pieces of hot parathas, dipped them into spicy mango pickle, and sipped steaming black tea from chipped ceramic mugs. In that small room, listening to Anza complain about the draught under the door, watching Palwasha laugh until her cheeks turned red, and listening to Aqsa recite an Urdu couplet about rural dignity, the weight of the institution vanished.

Here, behind the peeling paint of Amna Hall, we were not poor girls from struggling southern districts begging for an education. We were an autonomous, brilliant sisterhood of young women who understood each other without explanations.

Yet outside that door, Bosan Road was waiting.

Bosan Road was the six-lane asphalt artery that connected the ancient, crowded city of Multan to the sprawling university campus. To a casual visitor driving past in an air-conditioned car, Bosan Road was merely a wide university avenue lined with mango groves, housing societies, and private colleges.

To the female students of BZU, Bosan Road was a militarized frontier of public scrutiny.

From the moment you stepped through the green iron gates of Amna Hall onto the main campus road, you ceased to be an individual human being. You became a subject under public surveillance. Every motor rickshaw driver, every motorcycle boy revving his engine at the corner, every male student loitering near the cafeteria benches, and every security guard leaning against his rusted rifle watched your footsteps with evaluating eyes.

They watched how fast you walked. They watched whether your dupatta covered your chest or drifted near your shoulders. They watched whether you looked straight ahead or allowed your eyes to glance sideways. If you walked too fast, you were deemed bold and brazen. If you walked too slow, you were accused of lingering to attract attention.

The men of our society believed that the public square belonged exclusively to them by divine right. When a woman walked on Bosan Road, she was an trespasser in their territory. Her only permitted defense was to shrink herself, to lower her eyes, to pull her shawl tight, and to move like a ghost between the library and the hostel gate.

"Anam, we have to leave," Sara said, checking her wrist watch. "Dr. Qureshi locks the department seminar room at eight-fifteen sharp. If we are late by two minutes, he marks us absent for the week."

I swallowed the last sip of tea, picked up my heavy canvas bag filled with notebooks on comparative political systems, and stood up. My cervical spine sent a familiar, dull throbbing pain down into my left shoulder blade, but I straightened my back and adjusted my dupatta.

"Anza, are you coming?" I asked.

"Of course I am coming," Anza sighed, dramatically dusting her woolen coat with the back of her wrist. "Though if Dr. Qureshi's classroom has not been swept this morning, I am sitting next to the window. I refuse to sacrifice my lungs for comparative government."

Aqsa adjusted her black abaya, ensuring not a single strand of hair escaped from her scarf. Saba adjusted her silver ring. Palwasha gave my hand a warm, reassuring squeeze.

Together, the five of us opened the wooden door of Room 42 and walked out into the morning mist of Amna Hall, ready to face the world.

***

### The Strategist's Margin: Tactical Protocols for Daring Women

1. **Build Your Sanctuary Before the Storm Hits:** A woman surviving inside an unyielding institution cannot fight alone. Cultivate a tight, trustworthy inner circle of women who share your ethical frequency. Your room, your shared meals, and your shared humor are your primary defensive shields against systemic exhaustion.
2. **Humor as a Weapon of Resilience:** Do not allow the grimness of your circumstances to strip away your ability to laugh. Institutional oppression thrives when its victims become solemn, terrified, and isolated. Shared satire, affectionate teasing, and communal joy are active forms of political resistance.
3. **Master the Public Domain with Controlled Presence:** When walking through hostile or scrutinizing environments, do not look down in shame, nor look around in anxious hesitation. Keep your chin level, your gaze fixed fifty paces ahead, and your pace measured and deliberate. You do not owe the spectators of the street an apology for occupying space.
""")

assert_no_dashes(ch2_content, "02_chapter_2.md")
with open("manuscript/02_chapter_2.md", "w", encoding="utf-8") as f:
    f.write(ch2_content)
print(f"Updated Chapter 2: {len(ch2_content.split())} words")

# Chapter 3
ch3_content = clean("""# Chapter 3: Behind the Green Iron Gates (The Summer of 47 Degrees & The Fan Shut-Off)

By the middle of May, the city of Multan ceases to be a normal geographical city. It transforms into a white-hot furnace of dust, sun, and suffocating silence.

The temperature on the asphalt of Bosan Road routinely crossed forty-seven degrees Celsius in the shade. The air did not circulate; it hung over the campus like a thick, boiling sheet of invisible oil. The leaves of the ancient shisham and eucalyptus trees turned brown and brittle, coated in a fine layer of chalky dust that blew in from the surrounding cotton fields. By noon, even the stray dogs had abandoned the shaded verandas of the library, crawling under the concrete steps of the administrative block to pant in the darkness.

Inside Amna Hall, the heat was an inescapable physical punishment.

The hostel building had been designed in the late 1970s with thick brick walls, high ceilings, and small, barred windows that looked out into the courtyard. In winter, those thick walls trapped the damp cold. In summer, they absorbed the relentless solar radiation from sunrise until seven in the evening, storing the heat deep inside the masonry and radiating it back into our rooms like kiln ovens throughout the night.

In Room 42, we possessed two instruments of survival: a rusted ceiling fan that wobbled dangerously on its iron hook at speed five, and a rectangular galvanized-iron desert cooler mounted in our exterior window frame.

The desert cooler was a monstrous, deafening contraption. Its water pump rattled like a tractor engine, and its straw-padded sides dripped lukewarm, brackish water into an iron tray that smelled permanently of wet hay and copper rust. But when the temperature inside the room hovered at forty-two degrees at midnight, that noisy cooler was our lifeline. Its loud, churning roar drowned out the cries of the night crickets and provided the only cool, humid breeze that allowed us to sleep.

And it was during the peak of that suffocating summer that the legendary Fan and Cooler Shut-Off Protocol was born.

The drama had begun in early June, during the final preparation week for our annual semester examinations.

Across the corridor in the eastern portion, Aqsa's emotional world had collapsed into absolute chaos. The boy from her department, Ammar, who had pursued her relentlessly for seven months, had suddenly turned distant and erratic. After staging public scenes of devotion that had shattered Aqsa's strict resolutions and drawn her into an intense, overwhelming romance, Ammar had begun pulling away. He ignored her calls for days. He gave evasive, cold replies to her messages. When Aqsa, terrified of dishonor and desperate for family legitimacy, demanded that he send a formal marriage proposal to her father in Muzaffargarh, Ammar mocked her urgency, claiming that an educated modern girl should not think like an illiterate village elder.

For a girl who had staked her entire moral identity on that love, his withdrawal was not merely a romantic disappointment. It felt like a public execution.

It was two-thirty in the morning on a Tuesday. The outside air was completely still, stifling, and humid. In Room 42, Anza and I were fast asleep. Our ceiling fan was spinning at full throttle, humming its high-pitched metallic whine, and the desert cooler was churning out its steady, cool roar of damp air.

Suddenly, the wooden door of Room 42 was kicked open with a loud, violent bang.

I bolted upright on my cot, my heart racing, thinking that the hostel roof had collapsed or that an electrical fire had broken out in the corridor. Anza gasped, pulling her sheet up to her nose, blinking in terror in the dim green glow of our mosquito repellent light.

Standing in the doorway was Aqsa.

She looked like a ghost escaped from a fever dream. Her black dupatta was twisted around her neck like a noose. Her face was drenched in sweat and tears, her cheeks blotched with red, and her chest was heaving with rapid, shallow gasps as if she had just sprinted five miles across the desert.

"Anam! Utho!" Aqsa screamed, her voice cracking with hysterical panic. "Utho! Tumhein pata hai meri kya halat ho rahi hai aur tum log sukoon se so rahi ho! Utho meri baat suno!"

"Aqsa? Kya hua?" I scrambled out from under my sheet, stepping barefoot onto the warm concrete floor. "Is someone hurt? Did someone break into the hall?"

"Mera dil baahar nikalne lag gaya hai!" Aqsa cried, pressing both hands against her sternum, rocking back and forth on her heels. "Main mar rahi hoon! My chest is exploding! Ammar has not replied to my message since nine o'clock! He was online three minutes ago and he did not open my chat! Main mar jaungi, Anam! My life is over!"

Before Anza or I could say a single word of comfort, Aqsa did something that left both of us paralyzed in absolute shock.

She marched across Room 42 straight to the plastic switchboard mounted near the door.

With two swift, violent flicks of her index finger, she hit the rocker switches.

CLACK. CLACK.

The desert cooler's motor sputtered and died. The rattling roar of water vanished.

Above our heads, the ceiling fan's electric hum died into silence. The three metal blades slowed down, spinning with diminishing momentum, until they hung completely motionless in the dark.

In less than ten seconds, the temperature inside Room 42 began to skyrocket. The room became an airtight concrete tomb. The heavy, damp, forty-degree heat closed in on us like a wet wool blanket, sticking our clothes to our skin and making every breath feel like inhaling steam from a boiling kettle.

"Aqsa! Are you insane?" Anza shrieked from her cot, throwing her hands in the air. "Turn the fan back on! It is forty-five degrees in this room! We will suffocate to death!"

"No!" Aqsa yelled back, her eyes flashing with wild, desperate tears. "No cooler! No fan! Bas koi shor na ho! Na cooler ka shor, na pankhe ka shor! I cannot hear my own thoughts with that noise! You have to listen to me! I am dying, and all you care about is your fan! Sit down and listen to my heart! I need courage, I need someone to tell me what to do!"

I stood in the center of the stifling room, sweat already trickling down the back of my neck into my collar.

Any rational person would have pushed Aqsa aside, flicked the switches back on, and told her to go cry in her own room. But looking at Aqsa in the faint amber light from the courtyard lamp, I saw the raw, terrifying agony in her eyes. She was a village girl who had crossed the red line of her upbringing, who had trusted a smooth-talking campus boy, and who now felt the cold, bottomless abyss of abandonment opening beneath her feet.

"Anza, stay quiet," I whispered gently.

I pulled two cardboard examination clipboards from the study table. I handed one to Anza and kept one for myself. Sitting down cross-legged on the floor rug in front of Aqsa, I began waving the cardboard back and forth, fanning the heavy, suffocating air toward her tear-stained face.

"Sit down, Aqsa," I said softly, keeping my voice as calm as still water. "We are listening. Tell us everything from the beginning."

Aqsa collapsed onto the floor between our cots. And there, in the suffocating Multan heat, without a breath of breeze, in a room that felt like a furnace, she poured out her heart.

She told us about the text messages. She told us about how Ammar had sworn on the Quran that he would speak to his mother after the third semester, and how he was now making excuses about family debts and distant aunts. She told us how he had walked past her in the library corridor that afternoon with three junior girls, laughing and ignoring her presence as if she did not exist.

Every few minutes, Aqsa would break down, sobbing into her dupatta: "Main kya karoon, Anam? If my father finds out that I spoke to a boy, he will take me out of the university and lock me in the village courtyard forever. My degree will be cancelled. My life will be finished."

And while she cried, Anza and I sat there, waving our cardboard clipboards until our wrists ached with cramps, our clothes soaked through with perspiration, our hair plastered to our foreheads. Whenever Anza reached toward the switchboard to turn the fan on low, Aqsa would scream: "Don't touch it! The whirring sound drives me crazy! Let there be silence!"

We sat in that sweltering silence until four-fifteen in the morning.

We sat until the first light of dawn turned the eastern sky from indigo to a pale, milky gray. We sat until the call to prayer began echoing from the campus mosque, its deep, resonant cadence floating across the eucalyptus trees. Only when the morning breeze finally began to stir the dusty rose bushes in the courtyard did Aqsa's tears subside, her breathing slowing as exhaustion claimed her body.

"Are you feeling better?" I asked gently, offering her a glass of lukewarm water.

Aqsa took a slow sip, wiped her eyes with the sleeve of her abaya, and nodded.

"Yes," she whispered, looking down at her trembling hands. "Thank you, Anam. You saved my life tonight."

She stood up, slipped out of Room 42, and walked quietly back to her bed in the eastern gallery.

The moment the door closed behind her, Anza sprang from her cot like an enraged leopard. She lunged at the switchboard, hitting both switches with a resounding slap.

CLACK. CLACK.

The cooler roared to life, showering the room with cool, damp air. The ceiling fan whipped into a furious blur. Anza stood directly beneath the spinning blades, lifting her face toward the wind, gasping for breath as if she had just survived a deep-sea shipwreck.

"That girl is a terrorist!" Anza declared passionately, wiping sweat from her eyebrows. "She has no mercy! Na khud sukoon karti hai, na humein karne deti hai! If she ever turns off our cooler again during an emotional emergency, Anam, I swear to God I will lock this door from the inside and let her cry in the corridor until morning!"

I fell back onto my cot, laughing until my chest hurt.

My back ached, my shirt was drenched, and I had lost four hours of study before a major examination. But as the cool air washed over my exhausted face, I felt a deep, strange sense of gratitude.

This was the hidden reality of Amna Hall. Behind the political speeches, behind the administrative cruelty, behind the cold red brick walls of the university, we were keeping each other alive. In an environment designed to isolate and break us, our willingness to sit in the suffocating heat and bear each other's burdens was the only genuine grace we possessed.

***

### The Strategist's Margin: Tactical Protocols for Daring Women

1. **Recognize the Anatomy of Emotional Sabotage:** When a person experiences internal panic, their first instinct is often to control their external environment, even if it harms those who love them. Learn to identify when someone's dramatic demands are rooted in genuine trauma rather than malice, and respond with firm, boundaries-backed composure.
2. **Never Suffer Without Clear Tactical Limits:** Empathy is a virtue, but unregulated empathy is self-immolation. While you must support your sisters in crisis, you must also establish clear operational limits. A strategist comforts the wounded without allowing their panic to destroy the team's operational capacity.
3. **The Power of the Non-Judgmental Witness:** Most emotional crises in young women do not require immediate technical solutions; they require witnessing. When a friend feels that her secret pain is acknowledged without judgment or gossip, eighty percent of the panic dissipates. Be the steady anchor in the room that does not sway with the storm.
""")

assert_no_dashes(ch3_content, "03_chapter_3.md")
with open("manuscript/03_chapter_3.md", "w", encoding="utf-8") as f:
    f.write(ch3_content)
print(f"Updated Chapter 3: {len(ch3_content.split())} words")
