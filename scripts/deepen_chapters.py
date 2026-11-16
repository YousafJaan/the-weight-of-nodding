import os

manuscript_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\manuscript"

# ---------------------------------------------------------------------------
# CHAPTER 4 ENRICHMENT: Khara Paani
# ---------------------------------------------------------------------------
ch4_extra = """

The physical toll of this water was not distributed equally.

The daughters of the wealthy families who lived on the ground floor or in the new executive hostel never touched the tap water. They had twenty-liter mineral water dispensers delivered to their rooms twice a week by private delivery vans from the city cantonment. They washed their hair with bottled water poured from plastic jugs, their complexions remained clear, and their clothes smelled of imported floral fabric conditioners.

For the rest of us on the second and third floors, the saline water was an everyday humiliation that marked our bodies.

I remember watching my roommate Zoya sit on the edge of her wooden cot every Sunday afternoon, using an old horn comb to gently work through her tangled hair. Her hair had been thick, black, and heavy when she arrived from Dera Ghazi Khan. By our second winter, her scalp was covered in dry, flaky white patches of dermatitis caused by the high sulfate concentration in the groundwater. 

She would sit with her knees pulled up, looking at the small pile of broken hair on her bedsheet, and whisper verses from Surah Al-Rahman under her breath to keep from crying.

"My mother told me to look after my hair," Zoya whispered one evening, her eyes moist with tears. "She said that in our tribe, when relatives come to inspect a girl for marriage, the first thing the women look at is the thickness of her braid. If my aunt sees that my hair has become thin and dry like corn silk, she will tell my father that the city air has made me sick, and they will arrange my wedding before the year ends."

I sat beside her, took the horn comb from her trembling fingers, and began gently parting her hair, applying warm mustard oil drop by drop to her irritated scalp.

We became each other's doctors, each other's beauticians, and each other's keepers.

We learned the folk remedies of South Punjab: mixing gram flour (*besan*) with curd to wash our faces instead of drying commercial soaps, boiling dried neem leaves in a steel pot on our illegal immersion rod to make an antiseptic wash for skin rashes, and soaking fenugreek seeds overnight in a glass of water to drink on an empty stomach to soothe the burning acid reflux caused by drinking hard water.

In the washroom, the concrete washing platform was our communal agora.

Every Saturday morning, thirty girls would gather around the low brass taps, their shalwars rolled up to their knees, their arms bare to the elbows, scrubbing their clothes against the rough gray stone. 

The rhythm of the washing was hypnotic: the wet *slap-slap-slap* of cotton shirts beaten against the concrete slabs, the frothy gray water swirling down the open floor gutters, the sharp scent of yellow laundry soap bars mixing with the humid steam of the morning sun.

As our hands worked until our knuckles were raw, the conversations flowed freely:

"Did you hear that the chemistry department failed twelve girls in the practical examination because the lab assistant lost their record notebooks?"

"My brother called from Layyah yesterday. The wheat crop was ruined by hail, and my father does not know how he will pay my second-semester examination fee."

"The pump was supposed to run until seven o'clock, but Chacha Ramzan turned it off twenty minutes early because he wanted to go to the mosque for his morning tea. Someone should report him to the registrar."

"Report him to whom? The registrar is Chacha Ramzan's second cousin from Lodhran. If you report him, he will turn off the pump at six o'clock tomorrow, and we will all brush our teeth with mud."

We laughed, but it was the bitter, defensive laughter of people who understood that in this country, accountability is a private joke told by the powerful at the expense of the weak.

We scrubbed our clothes. We wrung the heavy, waterlogged cotton with our aching wrists until the veins stood out on our forearms. We carried our dripping plastic buckets back to our rooms, hung our dupattas and shirts along the balcony railings, and pinned them with wooden clothespins to prevent the desert wind from blowing them into the muddy courtyard.

And as I stood on that second-floor balcony, watching our colorful cotton clothes flutter in the dry Multan wind like flags of defiance, I realized that our struggle with the saline water was not an accident.

It was a daily lesson in structural subjugation.

If you want to keep a population from questioning the state budget, from investigating sovereign foreign debt, and from organizing democratic resistance, you do not need to deploy tanks in the streets.

You simply make the water bitter.

You make the water scarce, you make the water salty, and you force the young to spend three hours every morning carrying plastic buckets on their shoulders. By the time they finish carrying the water, they are too tired to carry the revolution.

I wiped my wet hands on my apron. I looked down at the white salt crust on my fingers.

I told myself: *Let the salt burn my skin today. Tomorrow, I will use my pen to show this nation where its water truly goes.*
"""

# Let's append this rich section to Chapter 4 if not already present
with open(os.path.join(manuscript_dir, "04_chapter_4.md"), "r", encoding="utf-8") as f:
    ch4_text = f.read()

if "The physical toll of this water was not distributed equally" not in ch4_text:
    # insert before Baji's Advice
    split_point = "---"
    parts = ch4_text.split(split_point)
    new_ch4 = parts[0] + ch4_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "04_chapter_4.md"), "w", encoding="utf-8") as f:
        f.write(new_ch4)
    print("Enriched 04_chapter_4.md successfully!")

# ---------------------------------------------------------------------------
# CHAPTER 5 ENRICHMENT: The Mess Token and the Cold Roti
# ---------------------------------------------------------------------------
ch5_extra = """

The physical hunger in the middle of the night was something nobody prepared us for.

In a traditional Pakistani household, even in the poorest village, a mother will always find a piece of dry bread, a bowl of curd, or a cup of warm sweetened milk for her child before bed. In Khadija Hall, the kitchen doors were slammed shut and padlocked with heavy brass chains at 8:45 PM. 

If you had a headache at nine o'clock and could not stomach the watery daal with pebbles, you had no alternative. You went to bed with an empty stomach that gnawed at your ribs like a sharp claw.

By eleven at night, the entire second floor was hungry.

Sometimes, when we could no longer bear the physical ache of empty stomachs during exam season, Saima and I would pull together our crumpled ten-rupee notes. We would collect forty or fifty rupees from under our mattresses, walk quietly down the dark staircase, and approach the back perimeter wall of the hostel near the laundry shed.

There was a small section of the brick wall where three iron spikes had been bent outward by previous generations of students, leaving a gap between the bricks and the concertina razor wire.

Through that narrow gap, we conducted our midnight trade.

Across the dirt lane outside the wall sat a small, unpaved tea kiosk operated by an elderly Pashtun man named **Chacha Gul Khan**. 

Chacha Gul Khan was a kind, white-bearded man who wore a traditional woolen Chitrali cap and kept a massive black iron frying pan bubbling with dark, used vegetable oil on a portable kerosene burner. He sold hot potato samosas filled with mashed yellow lentils, crushed coriander seeds, and fiery green chilies for fifteen rupees each.

We would stand on our tiptoes in the darkness behind the brick wall and make a quiet clucking sound with our tongues.

From across the ditch, Chacha Gul Khan’s twelve-year-old grandson, a quick boy named Ahmad, would appear in the shadows. He would hold a newspaper package containing four steaming, golden-brown samosas, their corners crisp and blistered from the boiling oil, smelling intensely of cumin and hot pastry.

Through the gap in the wire, we would slide our crumpled fifty-rupee note. 

Ahmad would slide the hot newspaper package through the razor wire into our waiting hands, whispering: *"Garam hai, baji! Sambhal ke pakro!"* (They are hot, sister! Hold them carefully!).

We would run back up the concrete stairs like thieves, our hearts pounding with adrenaline, holding the warm parcel beneath our woolen shawls.

In Room 34, we would spread an old Urdu newspaper on the floor between our beds. 

The four of us would sit around that newspaper, breaking the hot samosas with our fingers, the fragrant steam rising into the cold room air. The pastry was greasy, the oil had probably been used thirty times, but to our starving bodies, that fifty-rupee snack was a feast fit for an emperor.

We would eat every single crumb, lick the salt from our fingers, and drink a glass of water from our mosque bottle.

"One day," Ayesha said one night, wiping her eyes after a spicy mouthful of green chili, "when I pass the CSS examination and become an Assistant Commissioner, the first thing I will do is inspect the university mess halls. I will take the contractor, Haji Bashir, and I will force him to sit on a wooden bench for three hours, and I will make him eat his own yellow daal with a spoon. I will make him chew every single stone."

We laughed until the wooden cots shook, but behind our laughter was a profound, lingering grief.

Why should a twenty-year-old girl, studying to be an officer of the state, have to buy samosas through razor wire like a common criminal just to keep her stomach from cramping in the night?

In the male dormitories on the other side of campus, when the food was substandard, the young men had options. 

They could walk out onto Bosan Road at midnight. They could sit at the open-air dhabas under the fluorescent lights, eating hot chicken karahi, freshly baked naan, and fried river fish, drinking sweet Kashmiri chai from glass tumblers until two in the morning. They had mobility, they had freedom, and they had the power of collective threat.

We had the locked green gate. We had the Black Register. And we had the unbending administrative demand that we starve in silence to preserve our moral reputation.

I looked at the grease stains on the Urdu newspaper on our floor.

The newspaper had an article about the federal budget, announcing that forty billion rupees had been allocated for executive subsidies and official VIP protocol in Islamabad.

Beneath that headline, four university students were dividing a fifteen-rupee potato samosa in the dark.

I picked up my pen. I wrote down the date, the time, and the price of the samosa.

I knew that this was the real political science of Pakistan: a predatory ruling class that feasts on sovereign loans, while the educated youth of the nation scavenges for crumbs behind razor wire.
"""

with open(os.path.join(manuscript_dir, "05_chapter_5.md"), "r", encoding="utf-8") as f:
    ch5_text = f.read()

if "The physical hunger in the middle of the night" not in ch5_text:
    split_point = "---"
    parts = ch5_text.split(split_point)
    new_ch5 = parts[0] + ch5_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "05_chapter_5.md"), "w", encoding="utf-8") as f:
        f.write(new_ch5)
    print("Enriched 05_chapter_5.md successfully!")

# ---------------------------------------------------------------------------
# CHAPTER 8 ENRICHMENT: The Photostat Shop
# ---------------------------------------------------------------------------
ch8_extra = """

The underground geography of Chacha Asghar’s photostat shop was an education in itself.

In the back corner of that concrete basement, behind the giant stacks of paper and the drums of black powdered toner, sat a low wooden bench. It was covered in a faded floral cushion that had lost all its cotton stuffing, and on the plaster wall above it hung three hand-painted signs:

1. **NO CREDIT (UDHAAR) ALLOWED TO ANY STUDENT UNDER ANY CIRCUMSTANCES.**
2. **CHECK YOUR COPIES BEFORE LEAVING THE COUNTER.**
3. **DO NOT ASK FOR BANNED OR SENSITIVE MATERIALS.**

Chacha Asghar was more than a copyist; he was the chronicler of the university's intellectual decay.

While his two young assistants, boys of fourteen named Bilal and Tariq, fed paper into the roaring machines with rapid, practiced movements, Chacha Asghar would sit on his wooden stool, cleaning his bifocals with a corner of his white cotton vest, and talk about the history of the department.

"Baji," he told me one rainy afternoon while I waited for forty pages of constitutional law notes, "I have stood behind this counter since 1991. In those days, professors like Dr. Hasan Askari Rizvi and Dr. Inayatullah used to bring original research manuscripts from international conferences. They would sit on that bench, drink tea from an earthen cup, and discuss whether Pakistan's federal structure could survive the tensions between the center and the provinces. 

"Now? The new professors do not read books. They download slides from the internet on their mobile phones, send their departmental peon to my shop to print twenty copies on departmental account, and dictate the same three definitions every semester. The students do not want knowledge; they want twenty pages of guess papers that will give them sixty marks on the final paper. The university has stopped being an academy, baji. It is a paper mill."

He tapped the wooden counter with his plastic ruler.

"And do you know who suffers the most?" he asked, lowering his voice so his assistants could not hear. "The poor students. The girls from the tehsils who arrive here thinking that this is a temple of wisdom. When they realize that the professors are merchants selling degrees for obedience, their hearts break into small pieces."

I remembered Chacha Asghar’s words on the afternoon Zahra had her confrontation with Dr. Aslam.

After Dr. Aslam had shouted at her and walked out of Lecture Hall 2, Zahra did not go to the cafeteria. She did not go to the student union lawn.

She walked down the dark concrete stairs into the basement, stepped into the communal washroom behind the photostat shop, and locked the wooden latch.

I followed her down the stairs. I stood outside that washroom door in the dim, yellow basement light.

From inside the cubicle came the sound of a human being breaking down. 

It was not gentle weeping. It was the deep, shuddering, suffocating grief of a young woman who had poured every drop of her youth, every hour of her sleep, and every sacrifice of her poor family into an academic dream, only to watch an arrogant man in a safari suit destroy it in ninety seconds with a red pen.

"Zahra," I whispered, resting my palm against the rough wooden door. "Zahra, open the door. It is Anam."

For five minutes, there was only the sound of running water from the brass tap and her ragged, gasping breaths.

Finally, the latch clicked. The door opened.

Zahra stood there in the doorway. Her wire-rimmed spectacles were crooked on her nose, her eyes were swollen and red, and her white cotton dupatta was wet where she had buried her face to muffle her screams. Her hands were trembling violently.

"Why did he do that, Anam?" she whispered, her voice cracked and raw. "What did I do wrong? I read the book. I stayed awake until three in the morning to understand the constitutional clauses. I only asked why our parliament cannot enforce its laws. Is asking an honest question a crime in this country?"

I put my arms around her narrow, trembling shoulders. I pulled her close, feeling her tears soak through the lawn fabric of my shirt.

"No, Zahra," I whispered into her hair. "Asking a question is not a crime. Your intellect is not a crime. But you made a mistake: you treated this university as if it were an institution of truth. It is not. It is a colonial court, and Dr. Aslam is a courtier who protects the throne."

She pulled back, looking at my face with hollow, despairing eyes.

"My father sold his bicycle to pay my semester fee, Anam," she said, her voice dropping to a whisper that broke my heart. "He told everyone in our village: *My daughter is studying political science at BZU; she will write books; she will advise the government.* What will I tell him when he sees my mark sheet? How can I tell him that my marks were slashed because I asked a question?"

We stood in that damp basement corridor, beside the hum of Chacha Asghar’s photocopiers, holding each other like sisters on a sinking ship.

In that moment, I hated the red brick colonnades of the department. I hated the bronze bust of Allama Iqbal. I hated the portraits of John Locke and Jean-Jacques Rousseau hanging in the library.

Those portraits were masks. They were decorative lies painted on the walls of a prison to make the prisoners believe they were free.

I walked Zahra back to the bus stop on Bosan Road. I paid the twenty rupees for her ticket, helped her climb into the crowded passenger van back to Vehari, and watched the vehicle disappear into the golden afternoon dust.

When I returned to Khadija Hall that evening, I sat at my wooden study table in Room 34.

I opened my spiral notebook. I picked up my black ballpoint pen.

I wrote:

> *They can punish Zahra today because she stood alone in their lecture hall.*  
> *They can slash her marks because they control the grading register.*  
> *But one day, the truth of what happens in these classrooms will be written down.*  
> *It will not be printed on Chacha Asghar's twenty-page guess packets.*  
> *It will be published as an indictment of every cowardly master who traded truth for a pension.*

That afternoon in the basement was the moment I ceased to be an ordinary student.

I was no longer studying political science to pass their examinations or earn their plastic gold medals. 

I was studying political science to understand how to dismantle the intellectual tyranny that broke the spirits of the brightest daughters of my country.
"""

with open(os.path.join(manuscript_dir, "08_chapter_8.md"), "r", encoding="utf-8") as f:
    ch8_text = f.read()

if "The underground geography of Chacha Asghar" not in ch8_text:
    split_point = "---"
    parts = ch8_text.split(split_point)
    new_ch8 = parts[0] + ch8_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "08_chapter_8.md"), "w", encoding="utf-8") as f:
        f.write(new_ch8)
    print("Enriched 08_chapter_8.md successfully!")
