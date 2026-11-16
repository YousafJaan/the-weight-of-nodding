# -*- coding: utf-8 -*-
"""
write_chapters_09_to_11.py
Authors Chapters 09, 10, 11 with deep narrative scenes (~2,500 - 3,500 words each).
Zero em-dashes or en-dashes.
"""
import os
import re

def clean(text):
    text = text.replace('\u2014', ', ')
    text = text.replace('\u2013', ', ')
    text = re.sub(r' +', ' ', text)
    return text

c09 = """# Chapter 9: The Curfew Slip and the Father's Honor (Sidra's Crisis)

The most dangerous weapon in Khadija Hall was not a wooden baton or an iron padlock.

It was a small, rectangular slip of pink newsprint paper, four inches wide and three inches tall, known as the Gate Pass.

On that pink slip, in faded purple letterpress ink, was printed the architecture of female confinement:

*KHADIJA HALL (GIRLS HOSTEL)*  
*Gate Pass No: ________*  
*Resident Name: ________________ Roll No: ________*  
*Purpose of Exit: [ ] Medical [ ] Academic [ ] Home Visit*  
*Expected Return Time: ________ Actual Return Time: ________*  
*Warden Signature: ____________ Father's Verification: [ ] Yes [ ] No*

To step beyond the green iron gate after four in the afternoon, a female university student needed that pink slip. To obtain it, you had to stand outside the Assistant Warden's office, submit an application countersigned by your departmental chairperson, and wait while the warden picked up a landline telephone to call your father or designated male guardian.

The telephone call was a ritual of calculated humiliation.

The assistant warden, a bitter, middle-aged woman named Mrs. Farhat who wore thick gold bangles that clinked against her glass desktop, would dial the number slowly with a pencil eraser.

"Hello? Is this Sajjad sahib? This is Khadija Hall warden office. Your daughter Anam has requested permission to visit the university library until six-thirty in the evening for thesis research. Do you permit this? We take no responsibility for what happens beyond the gate after five-thirty. If you give permission, say it clearly so it is recorded in the ledger."

To a poor clerk or a small farmer in a distant district, a telephone call from a university official was terrifying. The immediate assumption in our culture is that if an official calls home about a female student, she has committed a moral transgression.

Fathers would stammer, apologize, and say:

"No, madam. Cancel the pass. Tell her to stay in her room and recite her prayers. She does not need to visit the library after dark."

And with one telephone call, a woman's intellectual mobility was snuffed out for the semester.

In mid-April, the system turned from petty harassment into a weapon of existential destruction.

The crisis began on a Thursday afternoon with **Sidra**.

Sidra had returned from her Urdu literature seminar at three o'clock, her face pale as flour. She did not take off her shoes. She sat on the edge of her cot in Room 34, clutching her plastic file folder to her chest, trembling so violently that the rusted iron frame of the bed began to vibrate against the concrete wall.

"Sidra?" Anza asked, looking up from her embroidery frame. "What happened? Did the department post the mid-term marks?"

Sidra did not answer. She reached into her handbag with shaking fingers, pulled out a folded slip of white notebook paper, and let it drop onto the floor.

Aqsa picked it up. Momina and I leaned over her shoulder to read it.

It was written in the rough, uneven Urdu handwriting of Sidra's younger brother, Tariq. The ink was smudged with thumbprints:

*Baji,*  
*Chacha has sold the tractor. He has paid seventy thousand rupees to the tent contractor and the caterer in the village. The date is set for Sunday, the twenty-first of April. Chacha told Baba that if you do not come home voluntarily on Friday, he will arrive at the BZU main gate with his three brothers and a hired Toyota Hiace van at two in the afternoon to bring you back. He has already told the Assistant Warden that your mother is critically ill with a heart attack and you must be released immediately into your uncle's custody. The warden has already approved the emergency gate pass. If you stay in the hostel, the security guards will escort you to the gate and put you into the van. Run if you can.*

The room went dead silent.

Outside, the afternoon heat was suffocating. Through the open window, the stench of the open sewer drifted into Room 34, heavy and sickening.

"My mother is not sick," Sidra whispered, her voice choking on tears. "My mother is healthy. My uncle lied to the warden. He is using the emergency clause in the hostel manual to have me dragged out by the university's own security guards. If they put me in that Hiace van, my life is finished. He will take me to the village, lock me in the back room, and marry me to his brother-in-law before sunset on Sunday."

She buried her face in her hands. Her weeping was silent, frantic, the weeping of an animal that sees the butcher's knife reflected in the water trough.

In that moment, the entire brutal reality of our society was laid bare before us.

The university, which claimed in its motto to bring *Knowledge and Light*, was functioning as an enforcement arm for rural patriarchy. The warden did not ask for a medical certificate from a hospital to verify the mother's illness. She did not ask Sidra whether she wanted to leave. In the eyes of Khadija Hall, a female student was not an adult citizen with constitutional rights; she was a piece of mobile property entrusted by a male guardian, to be handed back to any male claimant who carried the family surname.

Aqsa did not panic.

She folded the letter, walked to the door of Room 34, turned the brass bolt into place, and hung the dark dupatta over the frosted glass window.

"Sit down, Sidra," Aqsa said, her voice dropping to a low, commanding frequency. "Wipe your face. If you cry, your brain produces cortisol and your tactical reasoning collapses. Look at me."

Sidra looked up, her red eyes pleading.

"You are not getting into any Hiace van," Aqsa said. "And you are not going to Khanewal."

"How?" Sidra sobbed. "The warden has already signed the emergency discharge slip. Tomorrow at two o'clock, the van will be at the gate. If I refuse to leave my room, Maasi Sakina and the female guards will come up these stairs, pack my trunk, and drag me down. They did it to a girl from Dera Ghazi Khan last semester. You know they will do it."

"They will only do it if you are in this room at two o'clock tomorrow," a voice said from the floor.

It was **Palwasha**.

Palwasha was sitting with her back against my green trunk, cleaning the dirt from her fingernails with the tip of her sharpened steel nail file. Her green eyes were completely calm, cold, and predatory.

"Listen to me carefully," Palwasha said, looking around our circle: Aqsa, Anza, Saba, Momina, Sidra, Iqra, and me. "In my homeland, when an uncle attempts to kidnap a daughter, the clan settles it with gunfire. Here, you have no rifles. But you have something better: you have the law, and you have the Metro bus."

She pointed the nail file at Iqra.

"Iqra. Where is your duplicate gate pass stamp?"

Iqra reached under the common desk, slid the false wooden panel aside, and pulled out a small velvet pouch. Inside was a hand-carved rubber stamp that read: *CHIEF MEDICAL OFFICER | BZU HEALTH CENTRE | APPROVED FOR EXTERNAL REFERRAL.*

"Here," Iqra said.

"And you have the blank medical referral forms from Nishtar Hospital?" Palwasha asked.

"Twelve copies," Iqra nodded.

Palwasha turned to Saba. "Saba. What time is the first Metro bus from BZU terminal to Chungi No. 9 tomorrow morning?"

"Six-fifteen," Saba replied instantly from her upper bunk, her econometrics notes resting on her knees. "The gate opens for morning prayers at five-thirty. The first batch of staff enters at six."

Palwasha turned to Momina. "Momina. Can you pack Sidra's essential belongings: her national identity card, her matriculation certificate, her intermediate marksheets, and her degree registration slip, into a flat leather artist portfolio that looks like drawing sheets?"

"Give me ten minutes," Momina said, standing up and reaching under her bed for her heavy black portfolio case.

Palwasha looked at Sidra.

"Tomorrow morning at five-forty, while Maasi Sakina is washing her face for morning prayers, you do not walk through the gate with a tin trunk. If you carry a trunk, they know you are running. You walk out wearing your regular departmental abaya, carrying Momina's drawing portfolio under your arm, holding Iqra's stamped medical referral slip for an emergency dental x-ray at the university medical center. Maasi Sakina will log your name in the medical book."

"And then?" Sidra whispered, her breath trembling.

"You do not go to the university medical center," Palwasha continued, her voice steady and resolute. "You walk straight up the concrete stairs to the elevated Metro station at BZU. You take the six-fifteen Metro bus. You ride the red line all the way to Chungi No. 9. Waiting at Chungi No. 9 will be a private vehicle arranged by my cousin's legal collective in Multan. An advocate of the High Court, Miss Rubina Malik, will be inside."

Palwasha reached into the pocket of her shalwar and pulled out a folded green paper: an official legal vakalatnama and a registered affidavit of constitutional autonomy under Article 9 and Article 25 of the Constitution of Pakistan.

"Miss Rubina has already drafted the petition. By ten o'clock tomorrow morning, while your uncle is driving his Hiace van down the highway from Khanewal, Sidra will be standing inside the chambers of the Senior Civil Judge at Multan Kutchery, recording her voluntary statement under Section 164 of the Criminal Procedure Code, declaring that she is an adult, of sound mind, and that any attempt by her paternal uncle to restrain her liberty is criminal abduction."

Palwasha leaned forward, her gaze locking onto Sidra's soul.

"Once a civil judge records a Section 164 statement, a copy is served on the Senior Superintendent of Police and the Vice Chancellor of BZU by a court bailiff. If your uncle comes within fifty yards of this gate with his Hiace van, the police will arrest him for contempt of court and attempted kidnapping. The warden will not dare touch your trunk. She will have to serve you tea."

Sidra sat frozen. Her mouth was slightly open. She looked at the green paper in Palwasha's hand, then at the rubber stamp in Iqra's fingers, then at Momina neatly sliding her educational certificates into the black artist portfolio.

For her entire life, Sidra had been told that a woman's destiny is written by male hands, that an uncle's signature is law, and that an obedient girl must bow her head until she is led like a sheep to the altar.

She had never known that the law could be picked up like a shield. She had never known that seven girls in a twelve-by-fourteen room could outmaneuver an entire clan of patriarchal enforcers using an artist case, a rubber stamp, and a Metro bus ticket.

"What if the judge refuses to record the statement?" Sidra whispered.

"He cannot refuse," Aqsa said, resting her hand on Sidra's shoulder. "Miss Rubina is accompanied by three female human rights advocates. They will have cameras. In Pakistan, a corrupt judge fears public media exposure more than the wrath of God. You are safe, Sidra. But only if you stop shaking. Fear smells like blood to a wolf. When you walk past Maasi Sakina tomorrow morning at five-forty, you walk with your spine straight, your chin up, and your eyes looking forward. You do not look at her shoes. You look through her."

Sidra took a long, deep breath.

She reached out her trembling hand, took the green affidavit from Palwasha, and tucked it into her breast pocket, over her heart.

She wiped her tears. Her face was pale, but the desperate, terrified glaze in her eyes vanished, replaced by that cold, diamond-hard resolve that women only find when they realize that surrender means death.

"I will not look at her shoes," Sidra said, her voice clear and unbroken.

The next morning, at five-forty-two, I stood at the third-floor corridor window of the East Wing, watching the courtyard below in the grey dawn mist.

The heavy green iron gate stood open a crack.

A lone figure in a dark black abaya, carrying a flat leather drawing portfolio under her left arm, stepped across the gravel.

She reached the wicket gate. Maasi Sakina looked up from her wooden charpai, spitting dark tobacco juice into her rusted tin can.

Sidra handed her the pink slip with Iqra's purple medical stamp.

Maasi Sakina glanced at the stamp, grunted, and made a mark in her canvas ledger.

Sidra did not bow. She did not lower her chin. She did not say ji-achha.

She took back her pass, stepped over the sharp steel sill, and walked out onto Bosan Road with the long, deliberate strides of a free woman walking toward the elevated red line of the Metro station.

She did not look back.

At two o'clock that afternoon, a white Toyota Hiace van with tinted windows and Khanewal registration plates pulled up to the main gate of BZU. Four bearded men in starched white kurtas stepped out, their faces dark with patriarchal entitlement, ready to collect their runaway property.

They never crossed the threshold.

Waiting for them at the security barrier were two uniformed police sub-inspectors, a court bailiff holding a stamped certified copy of the Senior Civil Judge's protection injunction, and Miss Rubina Malik, Advocate High Court, holding a digital video camera.

The uncle screamed. He cursed his niece's soul. He threatened to burn her village home to the ground.

The court bailiff handed him the injunction and said one sentence:

"Cross that white line, and you spend the night in the central jail for contempt of the High Court."

The uncle looked at the police, looked at the camera, spat on the asphalt of Bosan Road, climbed back into his Hiace van, and drove away in a cloud of red dust.

Upstairs in Room 34, seven girls stood around the wooden study desk.

We did not celebrate with shouts. We made a pot of black tea on the illegal immersion rod. We poured it into seven plastic cups.

And when we raised our cups, our heads were held so high that our necks did not ache at all.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 10: Disarming Coercive Moral Panics & Family Extortion

1. **Recognize the False Emergency Mechanism:** Feudal families and predatory guardians almost always engineer a manufactured crisis (a sudden fake heart attack, a family medical emergency, a fabricated land dispute) to lure an independent woman back into their physical perimeter where her legal rights can be extinguished. Never travel into an unverified domestic perimeter based on verbal reports. Demand hospital verification, doctor names, and independent corroboration through neutral third parties.
2. **Preemptive Legal Encampment:** If you anticipate family coercion, forced marriage, or physical extraction, establish your legal perimeter before the perpetrators launch their strike. Execute a voluntary affidavit under Section 164 of the Criminal Procedure Code or an equivalent judicial declaration confirming your adult status, mental competence, and explicit refusal of forced matrimony. Once an affidavit is officially filed in a court of record, any subsequent forced marriage becomes prima facie criminal abduction.
3. **The Protocol of Non-Confrontational Extraction:** When escaping an oppressive enclosure, never signal your intent through emotional arguments, dramatic farewells, or conspicuous luggage. Travel light. Disguise high-value documentation (certificates, passports, identity cards) inside ordinary academic or professional portfolios. Move during scheduled, routine operational hours when gatekeepers are biologically fatigued and procedurally lax.
4. **Deploy External Asymmetric Power:** Local institutional administrators (wardens, chairpersons, registrars) will almost always collude with family patriarchs to preserve conservative social peace. Do not appeal to the moral conscience of university officials; compel their compliance through external legal instruments. A formal judicial injunction, backed by human rights legal collectives and documented with video evidence, paralyzes administrative collusion instantly.
"""

c10 = """# Chapter 10: The Photostat Archives (Chacha Asghar's Den)

Behind the Department of Political Science, tucked beneath the outdoor concrete staircase that led to the faculty air conditioning compressors, was a narrow brick alcove eight feet wide and twelve feet deep.

It smelled of burnt ozone, hot toner powder, cheap machine grease, and stale filterless Gold Flake cigarettes.

This was the intellectual engine of the university.

Above the wooden doorframe hung a rusted tin sign, painted by hand in chipped blue enamel: *AL-MADINA PHOTOSTAT & COMPOSING CENTRE. CHACHA ASGHAR.*

Inside the den, barely illuminated by a single bare sixty-watt bulb hanging from a fraying cloth wire, sat two massive, grey Canon photocopiers from the late 1990s. Their metal casings were dented and scratched, held together in places with silver duct tape. They ran continuously from eight in the morning until six in the evening, humming with a rhythmic, mechanical drone: *shhk-clack, shhk-clack, shhk-clack*, spitting out warm, static-charged sheets of white paper into plastic trays.

Behind the machines stood Chacha Asghar.

He was a man of sixty-five with a snow-white beard stained yellow around his mouth from four decades of smoking, thick cataract spectacles held together with copper wire at the nose bridge, and ink-blackened thumbs that looked like they had been dipped in liquid coal.

Chacha Asghar possessed more real power over the academic fate of five thousand students than the Dean of the Faculty of Arts.

He did not have a degree. He had left school in the fifth grade in a village near Shujabad. But he possessed the Photostat Archives: sixty wooden shelves crammed with cardboard cartons, labeled in blue marker with the names of every course taught at Bahauddin Zakariya University since 1986.

If you wanted to pass Comparative Political Systems without attending a single lecture, you did not go to the library.

You walked down the concrete steps behind the department, pulled aside the faded calico curtain of the photostat den, placed two hundred and fifty rupees on the toner-stained counter, and said:

"Chacha. Professor Qureshi. Five-year guess paper."

Chacha Asghar would not even look up. His blackened hand would reach into the third carton from the left on shelf number four, pull out a twenty-page stapled sheaf of papers, and slap it onto the counter.

Inside that sheaf was the entire examination paper you would face in December.

Not a sample paper. Not a practice test. The exact questions, phrased in the exact same broken English, accompanied by the exact five-point model answers that Dr. Qureshi had written in 2004 and had never updated since.

For thirty-five years, the faculty and the students had maintained an unspoken, corrupt truce mediated by Chacha Asghar's photocopiers:

The professors pretended to teach; the students pretended to learn; Chacha Asghar sold the answers for two hundred and fifty rupees; and the examination branch printed the degrees on thick parchment paper stamped with the university seal.

Everyone passed. Everyone nodded. The university's graduation statistics looked magnificent in the annual report.

And the graduates walked out onto Bosan Road with a Master's degree in Political Science, unable to draft a single professional memorandum, unable to calculate a percentage variance in a public budget, and entirely incapable of critical thought.

It was an industry of manufactured illiteracy.

I spent three hours inside Chacha Asghar's den on a Thursday morning in early May, waiting for him to photocopy eighty pages of historical land reform gazettes that I had borrowed from the provincial archives.

Sitting on a low wooden bench in the corner was a girl from our department named **Zahra**.

Zahra was from a lower-middle-class family in Muzaffargarh. Her father ran a small bicycle repair stall on the bypass. She had arrived at BZU with a fierce, quiet passion for constitutional history, spending her first semester sitting in the front row, taking meticulous notes in four different colored pens, and asking difficult questions about the judicial abrogation of the 1956 Constitution.

By her third semester, the department had broken her spirit.

She was sitting on the wooden bench, her head bowed, clutching a fresh copy of the *Five-Year Solved Guess Papers for International Relations*. Her eyes were red-rimmed, dull with that heavy, vacant exhaustion that comes when an idealist realizes she has been running inside a hamster wheel.

"Are you preparing for the mid-terms, Zahra?" I asked, sitting beside her on the bench.

She looked down at the stapled sheets in her lap. The paper was rough, cheap pulp, and the toner ink was already smudging onto her fingers.

"What is the point of preparing, Anam?" she whispered. Her voice was flat, devoid of anger, which made it far more terrifying than rage. "In the mid-term paper for Political Philosophy last week, I wrote six pages analyzing how Machiavelli's advice in The Prince reflects the modern bureaucratic mechanics of the civil secretariat in Lahore. I cited contemporary administrative data. I spent three nights without sleep drafting the argument."

"And?" I asked.

"Dr. Qureshi gave me nine marks out of twenty," she said, pulling her examination script from her canvas bag and handing it to me.

Across the top of the first page, written in thick, angry red ink, was Dr. Qureshi's scrawl:

*IRRELEVANT PHILOSOPHICAL BABBLE. DO NOT INVENT PRIVATE THEORIES. FOLLOW CHACHA ASGHAR'S MODEL ANSWERS IF YOU WANT TO PASS THIS COURSE.*

I looked at the red marks. My stomach turned with a sickening mixture of rage and grief.

Sitting on the other side of Seminar Room 4 was a boy named Kamran: the son of an influential textile mill manager from Cantt, who never attended a single morning lecture, who spent his afternoons smoking near the cafeteria, and who had memorized Chacha Asghar's five-point model answer word for word the night before the exam.

Kamran had received eighteen marks out of twenty, accompanied by a small note in red ink: *EXCELLENT GRASP OF THE SYLLABUS.*

"I cannot fight them anymore, Anam," Zahra said quietly, folding her guess paper in half. "My father borrows three thousand rupees every month for my bus fare and lunch money. He thinks I am becoming an intellectual. He thinks my mind is growing larger. He doesn't know that to get a degree from this department, you have to lobotomize yourself. You have to take your brain out of your skull, put Chacha Asghar's photocopied sheets in its place, and smile while they hand you an A-grade."

She stood up from the bench, paid Chacha Asghar sixty rupees for the guess paper, and walked out through the calico curtain into the blinding heat of Bosan Road.

Two weeks later, Zahra dropped out of the university.

She did not attend the final examinations. She packed her cardboard cartons, returned to her village near Muzaffargarh, and married a clerk in the municipal committee. The department did not even notice she was gone. On the attendance register, Dr. Qureshi simply drew a red line through her roll number, replaced it with a transfer student, and continued lecturing from his 2004 foolscap sheets.

When my photocopies were finished, Chacha Asghar stacked the warm sheets neatly on the wooden counter, tapping the edges against the glass lid of the copier to align them.

He looked at me over his wire-rimmed spectacles, his cataract-clouded eyes surprisingly shrewd.

"You are Sajjad sahib's daughter from Political Science, aren't you?" he asked, wiping toner dust from his fingers with a grey rag.

"Yes, Chacha," I replied, taking out my money.

"You don't buy the guess papers," he said. It was not a question; it was an observation. "Every girl from your department buys the guess papers. Even the gold medalist from last year bought my solved booklet for Public Administration. Why do you waste your money copying these thick government gazettes?"

"Because the guess papers are full of lies, Chacha," I said, looking him straight in the eyes. "They are thirty years old. The institutions described in those model answers do not exist anymore. If I memorize your booklets, I will pass the exam, but I will be blind."

Chacha Asghar was quiet for a long moment. He pulled a battered pack of Gold Flake cigarettes from his shirt pocket, struck a match against the side of the copier, and took a long, slow drag. The blue smoke curled up toward the bare bulb hanging from the ceiling.

"Beti," he said, his voice low and gravelly, softened by decades of tobacco smoke. "I have stood behind these two machines for thirty-five years. I have copied the exam papers for boys who became ministers, boys who became judges, and boys who became senior superintendents of police. Do you know what they all had in common?"

"What?"

"They never argued with the photocopier," he said, pointing the burning tip of his cigarette at the grey machine. "This university does not want scholars, beti. A scholar is dangerous. A scholar reads the budget, asks where the money went, and causes trouble for the syndicate. This university is a paper mill. It takes raw human beings from the villages, runs them through the rollers, imprints them with standard slogans, and stamps them with a degree so they can go work in government offices without asking questions."

He tapped the stack of my gazette copies with his blackened thumb.

"If you want to read the real numbers, read them. But do it with your eyes wide open. The moment an institution realizes that you are reading the original files instead of the guess papers, they will not praise your diligence. They will treat you like an enemy spy inside their fortress."

I took the stack of photocopies into my arms. The paper was still warm against my chest.

"Thank you, Chacha," I said.

"Do not thank me," he muttered, turning back to the glass platen of the machine as another customer pulled aside the curtain. "Just make sure that when you write your book, you tell them who owned the toner."

I walked out of the photostat den into the midday sun.

The heat on Bosan Road was touching forty-six degrees, but as I walked toward the library with my arms full of raw, unmanipulated government data, I felt cold with absolute clarity.

Zahra had surrendered. Rabia had packed her trunk. A thousand girls before them had memorized Chacha Asghar's five-point model answers, bowed their heads, collected their degrees, and vanished into the silent obscurity of domestic subjugation.

I looked at the stack of papers in my hands.

*I will not memorize their slogans,* I whispered to the dust of Bosan Road. *I will master the arithmetic, I will cite the original ledgers, and I will force this entire paper mill to look at its own reflection.*

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 11: The Anti-Shortcut Doctrine (Building Asymmetric Competence)

1. **Reject the Currency of Intellectual Counterfeiting:** In mediocre institutions, an elaborate ecosystem of shortcuts (guess papers, ready-made thesis mills, past paper memorization) exists to simulate academic competence while evading true learning. While using these materials to decode an examiner's prejudices may have short-term utility, never mistake the simulation for real knowledge. If you rely on institutional shortcuts, you remain intellectually helpless the moment you exit the university gates.
2. **The Monopoly of Primary Data:** The single greatest asymmetric advantage an independent researcher can build is access to unmanipulated primary data. While your peers memorize secondary summaries and outdated textbooks, master the original regulatory filings, gazettes, audit reports, and balance sheets. When you speak with the authority of raw data, no academic charlatan or corporate gatekeeper can intimidate you with theoretical jargon.
3. **The Discipline of Intellectual Sovereignty:** Understand why authoritarian institutions promote rote memorization: an obedient memorizer is predictable and easily governed; an analytical thinker who verifies data independently is uncontrollable. Treat every intellectual shortcut offered by an institution as a disguised bribe designed to purchase your future compliance.
4. **Preserve Your Intellectual Vitality:** When surrounded by peers who have surrendered to academic cynicism, protect your internal standards with absolute ruthlessness. Set your benchmarks not against the low standards of your departmental examination, but against international standards of empirical rigor. Excellence is the only armor that cannot be confiscated by a petty administrator.
"""

c11 = """# Chapter 11: The Strike, The Tear Gas, and The Suspended Metro

The riot began on a scorching Monday morning in late May, during the peak of the university mid-term examination week.

It started at ten o'clock outside the administrative block, where two rival student political organizations: the student wing of the ruling provincial political party and an armed ideological student federation, clashed over the lucrative monopoly on university transport contracts and hostel canteen concessions.

In a Pakistani public university, a student clash is not a civilized campus debate.

It is an armed factional turf war conducted by young men carrying automatic Kalashnikov rifles, steel knuckle-dusters, and iron reinforcement rods stripped from construction sites, operating under the direct patronage of provincial ministers and local criminal syndicates.

Within twenty minutes, the sound of semi-automatic gunfire was echoing across the main campus boulevard, cracking through the heavy summer heat like dry bamboo splitting in a fire.

Inside Khadija Hall, two hundred and fifty female students were trapped like sheep inside a fortified sheepfold.

At ten-fifteen, the heavy green iron gate was slammed shut by six campus security guards wearing steel riot helmets. They dropped three massive horizontal iron bars across the double gates, wrapped a heavy ship's anchor chain through the iron handles, and secured it with two heavy brass padlocks.

Then the security guards took off their helmets, laid their batons on the grass, climbed into an open security jeep, and drove away toward the administrative block, leaving Khadija Hall locked from the outside with no staff, no warden, and no medical personnel inside the compound.

The only person left at the gate was Maasi Sakina, who sat on her wooden charpai with her hands over her head, reciting the verses of Surah Yaseen in a cracked, terrified voice.

At ten-thirty, the wind shifted.

A contingent of Punjab Police anti-riot squads, armed with wooden shields and tear gas launchers, had cornered eighty rioting students on Bosan Road directly outside the university perimeter wall.

The police fired thirty rounds of tear gas canisters into the crowd.

The heavy, acrid canisters, trailing plumes of dense white chemical smoke, arced over the twelve-foot brick boundary wall of Khadija Hall. Two of them landed directly on the hard-packed clay of our inner courtyard, while a third struck the concrete balcony of the second floor, hissing and spitting chemical fire onto the hanging laundry.

Within ninety seconds, Khadija Hall was turned into an outdoor gas chamber.

The chemical agent used by the anti-riot police was not standard crowd-control gas; it was expired CS tear gas from military surplus stocks. It smelled of burnt industrial pepper, rotten cabbage, and chlorine gas.

The moment the white cloud touched your face, your mucous membranes felt as though they had been bathed in boiling battery acid.

Your eyes clamped shut with violent, involuntary spasms. Blind, searing tears flooded your cheeks. Your nasal passages constricted until you could not draw air through your nose, and when you opened your mouth to gasp for oxygen, the chemical smoke entered your throat, triggering uncontrollable, gagging dry heaves that dropped girls to their knees on the concrete corridors.

Two hundred girls began screaming in the dark stairwells.

Doors were banging. Footsteps thundered across the concrete floors as terrified students ran from the suffocating lower corridors toward the upper floors, crying for water, calling for their mothers, convinced that the hostel was being stormed by armed militants.

In Room 34, **Palwasha** took command within three seconds.

While Sidra was choking on her cot and Anza was hyperventilating into her pillow, Palwasha leaped across the room, grabbed our five-liter plastic water container, and dumped it directly over six heavy cotton dupattas that were hanging from the clothesline.

"Do not rub your eyes!" Palwasha roared, her voice cutting through the panic like an artillery shell. "If you rub your eyes, you grind the chemical crystals into your corneas! Tear the wet cloth! Cover your nose and mouth! Press it tight against your face!"

She shoved a soaking wet, cold cotton dupatta into my hands.

I pressed the wet cloth over my nose and mouth. The cold water filtered the worst of the burning gas, allowing me to draw a shallow, painful breath into my burning lungs.

Palwasha grabbed a second wet cloth and tied it firmly around Sidra's head, covering her mouth. She pulled Anza from her cot, forced her down onto the concrete floor where the air was marginally cooler, and shoved a third wet cloth into her face.

Aqsa was already at the casement window.

She had pushed the heavy wooden shutters closed and was stuffing wet socks and old newspaper sheets into the cracks around the window frame to keep the white chemical fog from entering the room.

"They have locked the main gate from the outside!" Aqsa shouted through her wet mask. "I saw the guards drive away! We are padlocked in!"

I crawled on my hands and knees over to the window and peered through a narrow crack in the shutter.

Down in the courtyard, the white tear gas smoke was billowing across the hard-packed earth like thick winter fog. The three stunted neem trees were completely obscured. Near the wicket door, a discarded tear gas canister was still sputtering sparks, charring a hole in a fallen cotton dupatta.

And outside on Bosan Road, visible through the razor wire on the perimeter wall, the city had stopped.

The elevated track of the Multan Metro Bus system was completely deserted. The automated stations at BZU terminal and Chungi No. 9 had their emergency steel shutters pulled down. The red-and-green buses were parked in long, motionless rows along the concrete viaduct, their diesel engines shut off, their glass windows reflecting the black plumes of smoke rising from two burning motorcycle rickshaws on the highway below.

The university administration had declared an indefinite emergency curfew.

The entire city of Multan was locked down.

For four agonizing days and four nights, Khadija Hall remained under total, unbroken siege.

No food arrived. The mess hall in the basement remained padlocked, Haji Manzoor having fled to his bungalow in Cantt the moment the first gunshot was fired.

On the second morning, the municipal power supply to the northern campus was severed when a high-voltage transformer outside the department was destroyed by an arson attack.

The electricity died.

When the electricity died, the electric bore pumps died with it.

By noon on the second day, the taps in the communal washrooms let out a final, choking gasp of air and went bone-dry. Not a single drop of saline water flowed through the iron pipes.

Two hundred and fifty girls were trapped inside a concrete fortress in forty-six-degree summer heat, with no electricity, no running water, no sanitation, and no access to the outside world.

Cell phone signals were jammed by the district administration to prevent student factions from coordinating reinforcement mobs. Every time a girl held her phone to the barred window, the screen read: *No Service.*

It was in those ninety-six hours of total abandonment that the veneer of modern civilization peeled away, revealing the raw, primal reality of institutional neglect.

Girls were drinking the stale, rust-colored water from the bottoms of the communal toilet cisterns. Third-floor residents were fainting from heat exhaustion and dehydration, lying motionless on the concrete corridors with wet cloths over their foreheads.

In Room 34, the Circle of Seven did not faint.

We went onto a military war footing.

Under **Iqra's** logistical direction, we conducted an emergency inventory of our survival assets:

We had eighteen liters of clean drinking water stored in plastic bottles beneath our iron cots.

We had half a sack of dry wheat rusks that Anza had purchased two days before the strike.

We had two jars of peanut butter, three packets of powdered milk, half a kilo of brown sugar, and a dozen packets of oral rehydration salts from Iqra's contraband pharmacy.

We formed a defense perimeter around Room 34.

Palwasha stationed herself near the door with her sharpened steel nail file and a heavy iron reinforcement rod that she had secretly pried loose from a broken balcony railing on the third floor.

Every six hours, under cover of darkness, Aqsa, Momina, and I would leave Room 34 carrying two plastic mugs and a small medical kit.

We moved quietly along the suffocating, pitch-black corridors of the East Wing, checking on the youngest girls: first-semester students from small rural towns who were weeping in their rooms, paralyzed by terror, their lips cracked and bleeding from dehydration.

We administered measured doses of rehydration salts dissolved in three ounces of clean water. We washed the eyes of girls whose corneas had been burned by the tear gas crystals using sterile saline solution from Iqra's stash. We distributed dry rusks, breaking them into quarters so that forty girls could have a single mouthful of solid food before sunrise.

We did not ask for money. We did not ask for merit marks. We did not ask which political party their brothers supported.

In the dark, suffocating heat of that besieged hostel, with the smell of rotting sewage rising from the dried washroom pipes and the silence of the suspended Metro overhead, we kept forty young women alive through pure, disciplined horizontal solidarity.

On the fifth morning, at six o'clock, the roar of diesel engines broke the campus silence.

Three army troop carriers and two armored police vehicles escorted a convoy of private transport buses through the shattered main gates of BZU.

The heavy anchor chain on Khadija Hall's green iron gate was cut with an industrial bolt-cutter. The iron doors swung open with a screech of rusted hinges.

The Chief Warden walked into the courtyard, flanked by four armed police officers and two junior lecturers carrying clipboards. She wore a pristine white lawn suit, oversized sunglasses to protect her eyes from the morning glare, and held a perfumed handkerchief over her nose to block the stench of the open drains.

"Attention, residents!" her voice boomed through a battery-powered megaphone. "Pack your bags immediately! The university is closed indefinitely by order of the Syndicate! You have thirty minutes to vacate the compound and board the evacuation buses to the general bus stand! Any student remaining after seven o'clock will be arrested under Section 144!"

Two hundred girls poured out of the dark stairwells like ghosts, hollow-eyed, trembling, dragging their dented trunks across the gravel path, weeping with relief as they climbed into the evacuation buses.

The Chief Warden stood by the wicket door, checking names off her clipboard, nodding with bureaucratic satisfaction at the efficiency of the evacuation.

When the six of us from Room 34 walked down the concrete stairs carrying our belongings, we did not run.

We walked slowly, shoulder to shoulder, our spines straight, our chins held level with the horizon.

Palwasha carried her leather duffel bag. Iqra carried her medical kit. Anza carried her embroidery frame. Sidra carried her artist portfolio containing her court injunction. Saba carried her econometrics ledger. Momina carried her rolled-up satirical caricatures. And I carried my green tin trunk and my unlined spiral notebook.

We reached the wicket gate.

The Chief Warden looked up from her clipboard. She saw our faces: clean, unbowed, without tears, without the frantic, begging hysteria of the other residents.

"You girls from Room 34," the Warden said, her voice sharp with institutional annoyance. "Why were you not at the gate when the horn sounded? Don't you know there is an emergency?"

Aqsa stopped. She did not lower her chin. She looked at the Warden through the tinted glass of her sunglasses.

"We were busy doing your job, madam," Aqsa said, her voice quiet, steady, and terrifyingly clear. "We were keeping your students alive while you were hiding in your air-conditioned bungalow in Cantt. You do not need to hurry us. We are leaving. But do not ever mistake our departure for your victory."

The Chief Warden's mouth opened in shock. Her face turned crimson under her powder.

"What is your roll number, girl?" she hissed. "I will have you expelled before the sun sets!"

"Write it down, madam," Palwasha said, stepping forward, towering over the Warden with her green eyes blazing like emeralds. "Her roll number is 402. Mine is 418. And if you touch a single hair on her head, fifty files documenting how your mess contractor bought industrial soap fat will be on the desk of the National Accountability Bureau in Lahore before your tea gets cold. Take your clipboard and step aside."

The Warden looked at Palwasha's face. She looked at the seven of us standing in an unbreakable, immovable wall of young womanhood.

She saw no fear. She saw no weakness. She saw no willingness to nod.

Slowly, without saying another word, the Chief Warden of Khadija Hall took one step backward onto the gravel.

We walked through the green iron gate.

We crossed the threshold without bending our spines. We walked out onto Bosan Road, where the morning sun was rising behind the concrete pillars of the Metro station, casting long, golden shadows across the highway.

The red line above us was still silent, but as we walked together toward the dawn, we knew that the real power in Multan was no longer on the elevated tracks or in the air-conditioned syndicate rooms.

The real power was walking on foot, carrying an unlined spiral notebook, ready to write the truth into the history of this country.

---

### The Strategist's Margin: Tactical Protocols for Daring Women

#### Protocol 12: Autonomous Crisis Logistics in Hostile Enclosures

1. **Immediate Pivot to Survival Command:** When an institutional crisis erupts (riots, structural lockdowns, natural disasters), immediately discard standard administrative hierarchies. Authorities who abandon their posts during a crisis forfeit all legitimate command. Form an autonomous, decentralized crisis council within your immediate trusted circle. Assign specific operational roles: water discipline, medical triage, perimeter defense, and counter-panic communication.
2. **The Redundant Hydration and Caloric Buffer:** In any enclosed residential facility, maintain a mandatory four-day survival buffer that is completely independent of institutional utilities. Store a minimum of ten liters of sealed potable water and three thousand calories of non-perishable, nutrient-dense dry rations (nuts, peanut butter, dried fruit, rehydration salts) inside your private perimeter. In a structural collapse, those who possess independent water hold total operational sovereignty.
3. **The Protocol of Non-Compliance During Abandonment:** When an authority figure returns after abandoning you during a life-threatening crisis, reject any attempt to reimpose moral or administrative dominance. Do not offer emotional apologies, do not scramble to appease their demands, and do not validate their manufactured authority. Record their dereliction of duty in verified, timestamped logs. Dereliction of duty during an emergency is the ultimate legal leverage against corrupt management.
4. **Horizontal Solidarity Over Individual Flight:** In a high-risk evacuation or crisis scenario, the instinct of weak individuals is atomized, panic-driven flight, which invariably results in exploitation or injury. Move as a unified, disciplined phalanx. Protect the most vulnerable members of your circle. When an institution encounters an organized, fearless collective of women who refuse to panic, its capacity to intimidate collapses entirely.
"""

# Write batch files
output_dir = 'manuscript'
os.makedirs(output_dir, exist_ok=True)

files = {
    '09_chapter_9.md': clean(c09),
    '10_chapter_10.md': clean(c10),
    '11_chapter_11.md': clean(c11)
}

for fname, content in files.items():
    path = os.path.join(output_dir, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    words = len(content.split())
    dashes = content.count('\u2014') + content.count('\u2013')
    print(f"Wrote {fname}: {words} words, {dashes} dashes")
