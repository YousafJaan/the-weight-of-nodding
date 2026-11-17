# -*- coding: utf-8 -*-
"""
Generate Season 1 of the Epic Novel in English (Episodes 01 to 10)
Novel: 'Rija: A Daughter's True Memoir'
Season 1: The Sanctuary and the Iron Gate (Bosan Road & Room 42)
Strict Plain Writing: ZERO em-dashes (\u2014) or en-dashes (\u2013).
Protagonist: Rija (Anam)
"""

import os
import json

base_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book"
out_dir = os.path.join(base_dir, "english_novel")
os.makedirs(out_dir, exist_ok=True)

def sanitize(text):
    return text.replace("\u2014", " : ").replace("\u2013", " : ").replace("  ", " ")

S1_EN_EPISODES = []

# Episode 1
S1_EN_EPISODES.append({
    "id": 1,
    "season": 1,
    "season_name": "Season 1: The Sanctuary and the Iron Gate",
    "title": "The Threshold of Bosan Road",
    "subtitle": "The Homestead Courtyard, The Battered Iron Trunk, and The Scorching Sun of Multan",
    "synopsis": "Stepping out from the safe, suffocating boundaries of the ancestral village to stand before Aisha Hall at Bahauddin Zakariya University Multan, bearing a father's severe burden of family honor.",
    "scenes": [
        """When the crowded passenger wagon finally slammed its screeching brakes on the burning asphalt of Bosan Road, a gust of scorching desert air laden with gritty yellow dust struck my face like an open flame. It was a suffocating September noon in Southern Punjab, where the sky had surrendered its azure blue to a heavy, chalky haze that seemed to press down upon every living creature. Before me, the imposing iron gates of Bahauddin Zakariya University stood like the portal of an ancient fortress. Beyond that threshold stretched a wide, tree-lined avenue, an asphalt highway carrying the whispered hopes of thousands of daughters who had journeyed out from the narrow mud courtyards of their villages to seek the skies.
 
From the luggage carrier fastened to the wagon's sun-baked roof, the conductor hauled down our battered tin trunk and two heavy canvas travel bags. My father, Sajjad, stepped down into the dust and exhaled a long, trembling breath. The stiff collar of his white cotton kurta was already dark with sweat, and the deep, weathered furrows across his forehead mirrored the unspoken dread he had carried inside his chest for the last three days.
 
He placed a calloused palm upon the rusted corner of the trunk, surveyed the strange, bustling crowds of students and university buses, and then turned his gaze directly toward me. When he spoke, there was a noticeable tremor in his deep voice, that instinctive, terrifying tremor that seizes an Eastern patriarch when he prepares to entrust his hereditary turban to the unpredictable winds of an unfamiliar city.
 
"Rija, listen to me with open ears," Father said, his voice quiet yet carrying the weight of iron. "In our entire ancestry, not a single daughter has ever crossed the threshold of a hostel. For three weeks now, inside the drawing rooms of your uncles and cousins, venomous whispers have circulated that Sajjad has surrendered his honor by letting his girl wander into the open air of Multan. Remember this well : honor is like a fragile glass cup placed upon the home's high shelf. Inside the house, it catches the morning light and glistens, but if it takes a single stumble out here on the road, it shatters into fine powder, and not a single soul in this world will stoop down to help gather its broken splinters. If your foot hesitates or slips here for even an instant, your father's head will be buried in the mud forever."
 
His words formed a sharp, hot thorn that lodged deep within my throat. I lowered my eyes instantly, clutching the frayed hem of my black cotton dupatta tightly inside my fist. Every fiber of my being wanted to cry out : 'Father, I do not love my books more than I revere your dignity. Why must you measure my existence only through the lens of potential disgrace? Why can you not trust the blood that runs through my veins?' But in our traditional Eastern households, daughters are never given the language of defense; they are granted only the habit of bowing their heads in silence.""",
 
        """Aisha Hall was a sprawling, red-brick labyrinth that sprawled beneath the relentless midday sun. Stepping into the main corridor, my nostrils were immediately attacked by the overwhelming odor of cheap hospital-grade phenyl, stale mustard hair oil, and the trapped dampness of hundred-year-old masonry. In the vast breezeways, scores of young women scurried back and forth : some balancing plastic laundry buckets on their hips, others huddled in weeping clusters over payphones talking to anxious mothers in remote towns, while senior girls strolled toward the communal mess with indifferent, worldly glances.
 
A sluggish queue wound through the central registration hall. When my turn finally arrived, I slid my admission papers and paid bank challan across the worn wooden counter. The registrar, an elderly woman in oversized plastic spectacles, scrutinized me from head to toe. Her eyes possessed that glazed, bureaucratic indifference that forms after decades of witnessing thousands of frightened, provincial faces cycle through the halls.
 
"Rija Sajjad? Department of Political Science?" she asked in a dry, monotonous tone.
"Yes, Madam," I managed to whisper, my hands moist with perspiration.
"Room 42, Block B, third floor. Here is your hostel regulation booklet. Be present every single evening at seven sharp for the mandatory roll call. If you are absent without a stamped medical slip from the university clinic, you face a five-hundred rupee fine and a disciplinary letter dispatched directly to your village address."
 
Father lifted the iron trunk by its wire handle, and together we began climbing the concrete stairwell. By the time we reached the third landing, his breath was coming in ragged, shallow gasps, his sixty-year-old knees groaning beneath the physical exertion. When we arrived outside Room 42, the warped wooden door screeched upon its rusted hinges as he pushed it open.
 
Inside, four crude iron cots were wedged into the corners, their thin mattresses covered in mismatched cotton sheets. Two rickety study desks sat near the window, their varnished tops scarred by decades of blue ink stains and carved initials of forgotten occupants. Above us, an antique ceiling fan spun with agonizing slowness, squeaking rhythmically with every revolution, stirring the suffocating heat rather than relieving it.
 
Father placed the trunk against the peeling wall. He reached deep inside the inner pocket of his waistcoat, pulled out three crumpled five-hundred-rupee notes that remained after paying the admission challan, and pressed them into my open palm.
 
"This must carry you through the entire month," he said, avoiding my eyes. "If you waste a single coin on frivolity, you will face starvation in this hall. And remember my command : you are here only to attend your lectures and return straight to this room. Do not speak with strangers."
 
He paused for a long, agonizing second. I saw his right hand twitch slightly, as if an ancient paternal instinct urged him to place his palm upon my head or draw me into a protective embrace. But the rigid, unyielding armor of patriarchal pride checked his motion. Without another syllable, he turned sharply and hurried down the dim hallway. I leaned against the rusted window mesh, watching his solitary white silhouette walk across the blazing tarmac below until he dissolved into the shimmering heat waves of Bosan Road.""",
 
        """When night finally fell over Multan and the blackness of the Punjab plains swallowed the horizon, the terrifying reality of complete isolation tightened its grip around my chest like an iron band. Sitting upon the coarse mattress of that stranger's cot, I slowly unlatched my small cloth suitcase. Tucked beneath my spare cotton clothes lay the familiar things my mother had secretly packed the night before : her worn velvet prayer rug, a tiny tin of green cardamom pods, and a container of homemade gram-flour sweets.
 
Mother had undoubtedly wept over those sweets while kneading the dough over the clay stove in our courtyard. Her parting whisper, delivered into my ear during our frantic dawn farewell, resonated through the silence of the room : "Rija, my precious child! Your father is a stern man, but his heart is eaten away by the terror that this cruel world will devour his daughter's innocence. Whenever the walls of this strange city close in upon you and every earthly door is bolted shut, spread this rug and recite Surah An-Nur. Your Lord will become your living fortress."
 
I unfolded the prayer rug and spread it across the cold, dusty floor of Room 42. In that forgotten corner of Aisha Hall, completely severed from everything familiar, I performed the first prostration of my adult life where no earthly mediator stood between my soul and its Creator. Beyond the closed door, the laughter of unfamiliar girls and the harsh whistle of the night warden echoed through the hallways. But against that coarse fabric, with my forehead pressed against the floor, a profound stillness washed over my heart. This was the threshold where a daughter's long, agonizing battle for truth, honor, and destiny had officially begun."""
    ]
})

# Episode 2
S1_EN_EPISODES.append({
    "id": 2,
    "season": 1,
    "season_name": "Season 1: The Sanctuary and the Iron Gate",
    "title": "The Republic of Room 42",
    "subtitle": "Four Iron Cots, Stifled Dreams, and The Warden's Midnight Whistle",
    "synopsis": "The turbulent coexistence of four girls from radically contrasting social classes inside Room 42, their clashing worldviews, and the suffocating discipline enforced by hostel warden Miss Nazia.",
    "scenes": [
        """Room 42 was never merely a residential chamber : it was a volatile, high-pressure microcosm of Southern Punjab's profound socio-economic fractures, an accidental sanctuary where four deeply wounded young women were crammed into eighteen square yards of peeling lime plaster. The four iron cots anchored to the corners were four distinct continents, each carrying its own unspoken tragedy.
 
My cot rested beside the barred window, overlooking an ancient, scorched neem tree and the back entrance of the student canteen. Directly opposite me slept Saba, an eighteen-year-old girl from a remote, drought-stricken agrarian hamlet near Layyah, enrolled in the Urdu Literature department. Saba possessed the perpetual, wide-eyed terror of a caged sparrow. Her father, a small-scale tenant farmer, had granted her permission to attend university on a single, terrifying condition : she was strictly forbidden from participating in any public debate, speaking in any seminar, or allowing her photograph to be taken, under threat of immediate withdrawal and forced marriage to an illiterate village cousin.
 
Near the doorway stood the cot of Sara, a political science major hailing from a wealthy yet deeply fractured feudal estate in Bahawalpur. Sara was the complete antithesis of Saba : tall, sharp-tongued, harboring a permanent sneer of cynical defiance. She kept a small box of matches tucked inside her pillowcase, spent hours blowing smoke rings through the door crack after midnight, and treated every administrative regulation with theatrical contempt.
 
The fourth cot belonged to Anza, a quiet, bespectacled scholar from the rural outskirts of Multan enrolled in the Philosophy department. Anza lived entirely in a fortress of thick, yellowed paperbacks. She sat cross-legged from dawn until the late hours of the night, sipping lukewarm black tea from an enamel mug, feverishly annotating treatises by Allama Iqbal, Nietzsche, and Bertrand Russell.
 
At precisely six-thirty in the evening, a piercing brass whistle shattered the humid air of the corridor, vibrating through the concrete floor like an electric shock. Saba leapt up from her cot with such violent panic that her notebook tumbled to the floor.
 
"Quickly, Rija! Pull your chador over your shoulders!" Saba gasped, her hands trembling as she fumbled with her plastic slippers. "Miss Nazia has entered the block! If we are not standing in line beside the doorframe before her whistle sounds for the second count, she will cut off the room's electricity for the entire night!"
 
I scrambled to my feet, adjusting my coarse black shawl, feeling the suffocating absurdity of being treated like a convict in a maximum-security penitentiary.""",
 
        """We stood in rigid, silent attention along the whitewashed corridor alongside forty other girls from Block B. Warden Miss Nazia, who had governed Aisha Hall with an iron fist for nearly two decades, marched down the gallery holding a thick cardboard dossier beneath her arm. She was a woman in her late forties, her hair tightly pulled back into an austere bun, her countenance set in an expression of perpetual, bitter hostility : that unmistakable bitterness that often festers inside souls who have sacrificed their own youth to enforce the joyless rules of a patriarchal institution.
 
She paused before each student, her hawk-like eyes scanning collars, hems, hairpins, and fingernails, making sharp pencil notations upon her register. When she arrived directly before Room 42, her gaze locked onto me with clinical intensity.
 
"You are the new arrival?" she asked, her voice flat and cold as chilled marble.
"Yes, Madam. Rija Sajjad, Department of Political Science," I answered, keeping my gaze respectfully lowered to the tops of her polished black oxfords.
"You may appear decent and modest on the surface, young lady," Miss Nazia remarked, stepping closer until the sharp scent of medicated soap enveloped me. "But remember where you are. This is a university hostel. Out here, girls sprout rebellious wings overnight. Mark my words : after seven in the evening, no resident steps past the courtyard gate. Telephone calls are strictly prohibited past ten at night. And if I hear a single burst of loud laughter emerging from this doorway after dark, I will suspend this entire room for a week. Do you comprehend?"
 
"Yes, Madam," I whispered, swallowing the bitter bile of humiliation.
 
The moment the warden's footsteps faded around the staircase corner, Sara let out a theatrical, mocking sigh and leaned against the doorpost. "The Führer's granddaughter has completed her daily inspection," Sara murmured with venomous amusement. "That woman genuinely believes that every female born east of the Indus is inherently sinful until she produces a stamped affidavit of her own misery."
 
That night, an unscheduled regional blackout plunged Multan into utter darkness. Within minutes, Room 42 transformed into an unventilated furnace, the brick walls radiating the day's trapped heat like an oven. The four of us sat cross-legged upon old newspapers spread across the bare floor tiles, taking turns waving a piece of cardboard to stir the motionless, suffocating air.
 
"Why did you really come to Multan, Rija?" Sara asked into the darkness, the brief flare of her match illuminating her sharp cheekbones as she lit an incense stick to ward off the swarming mosquitoes.
 
"I came to conduct research, Sara," I answered truthfully, wiping beads of sweat from my temple. "I came to prove to my father that his trust was not an error. I want to earn my degree and stand on my own feet."
 
Sara burst into a sharp, dry laugh that sounded like dry leaves scraping across concrete. "Earn your father's approval? Oh, you poor, naive village girl! Eastern fathers do not celebrate their daughter's intellect. They only draw a breath of relief when that daughter's palanquin is safely unloaded into some stranger's courtyard where her screams will remain muffled behind four walls. None of us came here to be educated, Rija. We are all simply serving out our sentences before the executioner arrives."
 
Sara's chilling words hung in the suffocating heat of Room 42 like an executioner's noose. Through the open window, the dry wind rattled the leaves of the old neem tree. I looked up at the patch of dusty sky visible through the iron bars and silently resolved that no matter how dark the road became, I would never allow my spirit to surrender to Sara's fatalism."""
    ]
})

# Episode 3
S1_EN_EPISODES.append({
    "id": 3,
    "season": 1,
    "season_name": "Season 1: The Sanctuary and the Iron Gate",
    "title": "The Warden's Whistle and The Electric Kettle",
    "subtitle": "Winter Fog, Contraband Coils, and The Gate-Pass Tribunal",
    "synopsis": "As winter descends on Multan, the residents of Room 42 navigate freezing conditions and arbitrary hostel bans, building a clandestine survival system while facing administrative humiliation at the main gate.",
    "scenes": [
        """By mid-December, the blistering heat of Southern Punjab had evaporated, replaced by a dense, bone-chilling winter fog that rolled across the sugarcane fields and swallowed Bosan Road in a white, blinding shroud. The temperature plummeted into the single digits, and the aged red-brick walls of Aisha Hall, designed to dissipate heat, now transformed the interior into an unheated stone crypt.
 
The hostel taps yielded water so frigid that washing one's face felt like plunging flesh into crushed ice. Yet, by decree of the Chief Warden's office, all high-voltage electrical heating appliances : immersion rods, electric heaters, and kettles : were strictly outlawed under threat of a three-thousand-rupee fine and immediate eviction. The official rationale was 'fire safety', but every student knew the truth : the administration refused to pay the winter electricity surcharge to the utility company.
 
Inside Room 42, we were shivering uncontrollably. Saba's fingers had swollen with painful, purplish chilblains, making it nearly impossible for her to grip her pen during morning lectures.
 
"We cannot survive January like this," Sara declared one evening, pulling an oversized woolen shawl over her shoulders. "Tomorrow, Rija and I are going to the electronic bazaar in Hussain Agahi."
 
The expedition required smuggling a five-hundred-watt brass immersion rod past the security post at the main portal. Sara wrapped the metal coil in three layers of old newspaper and concealed it inside the hollow lining of my winter coat. My heart pounded furiously against my ribs as we approached the security desk, but the aging guard was busy slurping hot soup from an aluminum bowl and barely glanced at our student identity cards.
 
Back inside Room 42, behind bolted doors and with heavy blankets draped over the windows to block any light leak, we inaugurated our clandestine heating station. We wedged an empty metal powdered-milk tin into the narrow alcove behind the wooden wardrobe, filled it with water, and plugged the immersion coil into an illicit wall socket whose safety plate Sara had bypassed with a butter knife.
 
When the water began to bubble with a soft, comforting hiss, the four of us clustered around that tiny tin can like travelers around an oasis fire. When Anza dropped four teabags and a pinch of crushed cardamom into the boiling water, the fragrant steam that rose into the icy room felt like an act of triumphant rebellion. That hot brew, shared in chipped ceramic mugs in the dead of winter, was not merely tea; it was life itself.""",
 
        """Yet, the hostel's administrative machinery found endless ways to strip away a young woman's dignity. The most humiliating daily gauntlet was the infamous 'Gate-Pass System'.
 
To step beyond the university gates for even two hours : whether to purchase prescribed textbooks, visit a medical laboratory, or submit photocopies : required an ordeal that resembled an interrogation before a military tribunal. One chilly Tuesday afternoon, I needed to visit the Central Post Office to mail my handwritten case notes to a research journal.
 
I stood before Miss Nazia's mahogany desk in the administrative wing. The warden was scrutinizing my printed pass application through her spectacles as if hunting for hidden treason.
 
"The Central Post Office?" she asked, raising a skeptical eyebrow. "Why can you not use the student post box inside the campus student center?"
"Madam, the campus box is only cleared once a fortnight, and my research submission deadline expires on Thursday," I explained with quiet dignity.
 
"Who is this supervisor you are corresponding with? Is he a male professor?" Her questions carried that toxic, unstated insinuation that perpetually haunted every female movement in Southern Punjab. "Girls from respectable rural families do not wander around the city's commercial centers on a weekday afternoon. Bring me a written authorization letter signed by your department head, or this slip remains unsigned."
 
A surge of burning anger rose from my stomach to my throat. I stood there in my worn black shoes, looking at this woman whose sole authority derived from policing the physical boundaries of young women who had never committed a crime.
 
"Madam," I said, looking directly into her eyes without lowering my gaze for the first time. "My department head, Dr. Masood, appointed me as a student researcher precisely because he values my intellectual capacity. If you suspect that a scientific paper on constitutional law is a cover for immoral behavior, I invite you to read the sixty pages currently in my bag."
 
Miss Nazia's face flushed with sudden irritation at my composure. She signed the slip with a violent stroke of her red pen and slammed the stamp onto the carbon paper.
 
"Take it!" she snapped. "And if you are not back inside this gate by four-thirty sharp, do not bother returning. Sleep on the pavement of Bosan Road!"
 
I took the stamped pass, turned on my heel, and walked out into the chilly winter air. As I passed through the iron gates and stepped onto the public road, I drew in a deep breath of the misty wind. The city outside was harsh, indifferent, and dangerous, but inside the hostel, the walls were suffocating the very soul. I knew then that every step toward freedom would require tearing through layers of suspicion and spite."""
    ]
})

# Episode 4
S1_EN_EPISODES.append({
    "id": 4,
    "season": 1,
    "season_name": "Season 1: The Sanctuary and the Iron Gate",
    "title": "Two A.M. at Nishtar Emergency",
    "subtitle": "A Midnight Collapse, The Refusal of Care, and The Wards of Despair",
    "synopsis": "When roommate Saba collapses in the dead of night with acute appendicitis, Rija and Sara must battle indifferent hostel administrators and navigate the chaotic, harrowing wards of Nishtar Hospital without a male guardian.",
    "scenes": [
        """The emergency struck at twenty minutes past one in the morning, when Aisha Hall was submerged in dead silence and the winter frost clung to the window panes. A sickening, choked cry sliced through the stillness of Room 42, followed by the violent crash of an aluminum water jug hitting the floor tiles.
 
I bolted upright from my cot, my heart racing. In the dim amber glow of the corridor lamp leaking through the transom, I saw Saba crumpled upon the concrete floor, clutching her lower right abdomen, her knees drawn tightly toward her chest. Her skin was deathly pale, covered in a cold, clammy sweat, and her lips were trembling violently.
 
"Saba! What is happening?" I cried, dropping to my knees beside her. Her forehead was burning like a furnace, yet her entire frame shuddered with severe chills.
 
"Rija... it feels like... a knife inside my stomach," she gasped, her voice breaking into an agonized whimper. "I cannot breathe... please... help me..."
 
Sara leapt from her bed, instantly assessing the situation. "Her appendix is rupturing," Sara said, her voice unusually stripped of its trademark cynicism. "We have to get her to Nishtar Hospital immediately."
 
Leaving Anza to hold Saba's convulsing frame, Sara and I sprinted down three flights of concrete stairs in our bare feet, banging with both fists against the heavy teak door of the superintendent's residence on the ground floor.
 
When the night supervisor finally cracked open the door, wearing an oversized woolen cardigan and a scowl of deep annoyance, her response was a masterclass in bureaucratic callousness : "An ambulance? For an ordinary stomach ache? Do you think university vehicles are taxis for hysterical girls? Give her two paracetamol tablets and let her rest until the morning clinic opens at nine."
 
"Madam, she is vomiting blood and cannot stand!" I screamed, grabbing the doorframe before she could shut it. "If her appendix bursts inside this building tonight, you will answer for her murder to the police and her family in Layyah!"
 
The word 'police' punctured the supervisor's smug indifference. Five minutes later, she reluctantly scribbled an emergency gate exit slip, but flatly refused to summon the university driver. "Find your own transport on the road," she sneered, locking her door behind us.""",
 
        """Sara and I practically carried Saba across the dark, frozen campus grounds, supporting her limp arms over our shoulders, her feet dragging helplessly through the winter weeds. Outside the main gate, after ten terrifying minutes in the pitch-black mist, we managed to hail a battered auto-rickshaw whose driver agreed to transport us only after Sara pressed a five-hundred-rupee note into his palm.
 
The emergency department of Nishtar Hospital at two in the morning was an unfiltered descent into Dante's Inferno. The reception hall reeked of coagulated blood, cheap carbolic acid, and human despair. Exhausted orderlies pushed squeaking iron stretchers through crowded corridors lined with groaning road accident victims, screaming children, and destitute families huddled upon the filthy terrazzo floor.
 
"Where is the male guardian?" the triage clerk demanded aggressively, pushing our admission slip back across the blood-splattered counter. "We cannot admit a female patient for surgical evaluation without the presence and signature of her father, brother, or husband."
 
"Her father is a tenant farmer stranded five hours away in a remote village near Layyah!" I shouted, slamming both palms onto the counter, heedless of the shocked stares around us. "She is dying right in front of you! Here are our university identity cards. I will sign whatever document is required, but if you do not call a surgeon to this stretcher right now, I will walk straight into the Medical Superintendent's office upstairs!"
 
Something in my furious, uncompromising gaze broke through the clerk's obstinacy. Within twenty minutes, a young, bleary-eyed surgical resident examined Saba, confirmed an acute, gangrenous appendicitis, and wheeled her directly into the pre-operative theater.
 
For the next four hours, Sara and I sat side by side upon a rusted metal bench in the freezing hospital corridor. The fluorescent tubes above us flickered and hummed with a monotonous, maddening buzz. Around us, weeping relatives prayed on small handkerchiefs, while police constables escorted handcuffed criminals through the swinging doors.
 
At six in the morning, the surgeon emerged, pulling off his bloodstained latex gloves. "She was twenty minutes away from septic peritonitis," he said, wiping his exhausted brow. "The appendix was completely perforated. But she will survive. You two saved her life."
 
When they wheeled Saba into the recovery ward, pale and groggy from the general anesthesia, she opened her heavy eyelids and feebly grasped my hand. Her voice was barely a whisper : "Rija... did my father... find out?"
 
Even at the literal edge of death, the supreme terror of a daughter in our society was not the scalpel or the grave; it was the terrifying specter of paternal wrath. I squeezed her cold fingers, hot tears finally spilling down my cheeks. "No, Saba," I whispered. "Your father knows nothing. You are safe now."
 
Sitting beside that squeaking hospital cot as the grey dawn light filtered through the cracked window, I realized how horrifyingly fragile a woman's existence was when severed from home, and how we, the daughters of this unforgiving land, had no choice but to become each other's shield."""
    ]
})

# Episode 5
S1_EN_EPISODES.append({
    "id": 5,
    "season": 1,
    "season_name": "Season 1: The Sanctuary and the Iron Gate",
    "title": "The HEC Research Merit",
    "subtitle": "The Notice Board, The Feudal Heiress, and The Battle for the Assistantship",
    "synopsis": "Facing severe financial hardship, Rija competes for a prestigious Higher Education Commission research position, triggering the bitter, vindictive wrath of Umme Rubab, a powerful and privileged senior student.",
    "scenes": [
        """By the onset of my third semester, the meager financial reserves Father had provided were completely exhausted. The cost of photocopied syllabi, research monographs, and daily necessities had devoured every rupee. When I called home from the public telephone booth near the university bank, Father's response was curt and devastating : "Crop yields this season have failed, Rija. Cotton prices have collapsed. If you cannot manage your expenses, pack your trunk and return home. A daughter's education cannot take precedence over feeding the household."
 
The threat of eviction hung over my head like an executioner's blade. It was precisely at this desperate juncture that a white, stamped official circular appeared upon the glass-encased notice board outside the Department of Political Science.
 
The Higher Education Commission, in partnership with an international development consortium, was funding a high-profile empirical research initiative entitled : *'Tribal Customary Panchayats and the Denial of Statutory Inheritance Rights to Rural Women in Southern Punjab.'*
 
The project had a single opening for a 'Junior Research Assistant', carrying a monthly stipend of thirty-five thousand rupees : an astronomical sum that represented not merely financial survival, but total liberation from the humiliating necessity of begging Father for pocket money. It was the key to my academic sovereignty.
 
However, across the corridors of Aisha Hall, the position was already considered the exclusive, pre-ordained property of Umme Rubab.
 
Umme Rubab was a senior graduate student whose family owned sprawling agricultural lands along the Chenab river and maintained powerful political connections in Lahore. She arrived at the department every morning in a gleaming red sedan, wore imported designer lawn suits that trailed expensive French perfume through the dusty corridors, and maintained an entourage of sycophantic junior girls who carried her files. Her paternal uncle was a personal confidant of the University Vice-Chancellor.
 
Two days before the scheduled interviews, Umme Rubab cornered me outside the departmental seminar library. Her painted lips curled into a patronizing, razor-sharp smile.
 
"Listen to me, Rija," she said, tapping her manicured red nails against her leather folder. "You are embarrassing yourself by submitting an application for this assistantship. Dr. Arshad has been a house guest at our Multan residence for a decade. Positions of this caliber are designed for candidates with social pedigree and global polish, not for provincial hostelites who buy second-hand shoes from the bazaar. Go back to your dorm and prepare for your regular coursework."
 
The raw, casual arrogance in her voice was breathtaking. It was the generational entitlement of the landed gentry who believe that intellectual merit, like river canal water, can be diverted into their private estates through bribery and political coercion.
 
I tightened my grip on the strap of my frayed shoulder bag and looked directly into her dark, mascara-rimmed eyes.
 
"Umme Rubab," I replied evenly, keeping my voice low and steady. "Knowledge and sustenance are not inherited family jagirs. If my Lord has written this research appointment in my destiny, all the political uncles of Multan cannot tear it from my hands. We will let the selection board decide on Friday."
 
She recoiled slightly, her eyes narrowing into cold slits of hatred. "You will regret this insolence, village girl," she hissed, turning on her designer heels and marching away.""",
 
        """On Friday morning, the air inside the Dean's Conference Room was thick with academic tension. The selection panel was formidable : the Head of Department Dr. Arshad, an external constitutional expert from Punjab University, and a senior British project representative named Dr. Julian Evans.
 
When my name was summoned, I entered wearing my plain white cotton suit and a modest black headscarf. I had spent the preceding two weeks staying awake until four in the morning, compiling fifty pages of primary field interviews conducted in the rural outposts of Muzaffargarh and Rajanpur, detailing the clandestine practice of *Haq Bakhshwana* : the coerced ritual where young rural women are forced to swear an oath upon the Holy Quran renouncing their inheritance rights in favor of their brothers.
 
Dr. Arshad opened the interview with a barrage of skeptical, aggressive inquiries, attempting to trip me up on statistical modeling and theoretical paradigms. But when I presented my primary field documentation : complete with court case citations, village revenue settlement maps, and translated testimonies of disinherited sisters : Dr. Evans took off his reading glasses and leaned forward over the mahogany conference table.
 
"Remarkable," Dr. Evans remarked, examining my handwritten charts. "Miss Rija, this is not mere theoretical regurgitation. You have captured the living, bleeding reality of Southern Punjab's agrarian patriarchy. This is precisely the empirical rigor this international consortium requires."
 
The interview lasted forty-five minutes. When I emerged into the courtyard, the afternoon sun felt warm and benevolent upon my face.
 
At eleven the following morning, the official results were posted on the department board beneath the university seal. A dense crowd of students pressed against the glass. At the very summit of the list, printed in bold black typography, appeared the verdict :
 
**Selected Candidate : Rija Sajjad (Merit Score : 94 / 100)**  
**Waiting List Alternate : Umme Rubab (Merit Score : 71 / 100)**
 
The news detonated through Aisha Hall like an earthquake. Saba and Sara wrapped their arms around me, weeping with uninhibited joy. For the first time in my life, I felt the intoxicating power of pure, uncompromised intellectual merit.
 
Yet, in an Eastern society, a poor woman's victory over the privileged is never forgiven.
 
That evening, as I walked toward the hostel dining hall, Umme Rubab was waiting in the central corridor surrounded by her cabal of wealthy sycophants. Her face was chalky white, distorted by uncontrollable humiliation and venom.
 
"Congratulations, Rija Bibi!" she announced loudly, her shrill voice echoing off the brick walls so that doors flew open across Block B. "We had no idea your research talents were so exceptional! Tell us, how many late-night sessions did you spend inside Dr. Arshad's private office to earn those ninety-four marks? A destitute village girl does not secure an international salary through textbooks alone. You must have provided some very specialized private services!"
 
The filthy accusation struck my ears like boiling lead. Around us, dozens of girls looked on, their faces twisting into perverse, gleeful smirks. My blood turned to ice. I felt an overwhelming urge to tear her lying throat apart, but the terrifying memory of Father's warning and the absolute vulnerability of my position paralyzed my hands. I spun on my heel, fled into Room 42, threw the bolt, and collapsed onto my cot.
 
When a woman's intellectual excellence is answered by smearing her moral character, it is not merely an insult : it is a calculated attempt to assassinate her soul."""
    ]
})

print(f"Season 1 Episodes 1 to 5 generated in English. Generating 6 to 10...")
