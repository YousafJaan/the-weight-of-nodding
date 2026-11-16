import os

manuscript_dir = r"C:\Users\Huzaifa Mahi\.gemini\antigravity\worktrees\remote-workspace\write_new_book\manuscript"

# ---------------------------------------------------------------------------
# CHAPTER 9 ENRICHMENT: The Strike and the Tear Gas
# ---------------------------------------------------------------------------
ch9_extra = """

The four days of the siege revealed the true, fragile reality of institutional life in Khadija Hall.

By the second night of the lockdown, our mobile phone batteries had died. The single charging station in the warden's office was locked, and the corridor sockets were dead because the campus electricity line had been severed during the street battles at the bank square.

We were cut off from the world.

In Room 34, our only link to reality was an old battery-operated transistor radio that Saima had brought from her grandfather's house in Muzaffargarh. It was a small red plastic radio with an antenna held together with silver tape. 

Every evening at eight o'clock, the four of us would sit around that radio on the wooden floor, leaning our heads together, listening to the crackling medium-wave Urdu news broadcast from Radio Pakistan Multan:

*"The district administration of Multan has extended Section 144 across the university campus for an additional forty-eight hours following violent clashes between student groups. The Vice Chancellor has appealed for calm and formed an eight-member peace committee to review student demands."*

Not a single word was mentioned about seven hundred female students locked behind iron chains without water. 

Not a single sentence reported that the mess hall was closed and that young women were drinking contaminated water from the base of the fire-escape tanks. To the state media, the university was an abstract political theater where men debated and negotiated; our physical suffering did not exist in the official record of the nation.

On the third afternoon, Ayesha developed a violent, burning fever.

Her forehead was as hot as a tea mug, her teeth were chattering uncontrollably under two woolen shawls, and she was vomiting yellow bile into our blue plastic wastebasket. Her asthma inhaler was empty, and every breath rattled in her lungs like dry paper.

Saima and I ran down the dark concrete stairs to the assistant warden's office.

We pounded on the wooden door until Mrs. Farhat opened it. She was sitting with her prayer beads, a battery-powered fan humming on her desk.

"Madam," I begged, holding onto the doorframe, "Ayesha is burning with fever. She cannot breathe. Her asthma is severe. Please unlock the side gate and let us take her to the emergency ward of Nishtar Hospital in an auto-rickshaw!"

Mrs. Farhat looked at us with cold, irritated eyes.

"Are you insane?" she snapped. "There is police firing near the main gate. The student wings are burning tires on Bosan Road. If I open that iron gate and a television crew films a female student outside, the Chancellor will suspend my job before sunset. Go back to your room. Put a wet cloth on her forehead. God will protect her."

"Madam, she might suffocate in that room!" Saima screamed, losing her temper for the first time in two years. "If she dies in Room 34, will your Chancellor bring her back to life?"

Mrs. Farhat stood up from her chair, her face flushed with fury.

"How dare you raise your voice in my presence!" she shouted. "One more word from you, Miss Saima, and I will report your name for inciting rebellion during an emergency! Return to your floor immediately, or I will call the female security guards to lock you in the storeroom!"

We walked back up the stairs in the dark, our fists clenched, tears of helpless fury blinding our eyes.

We did not sleep that night.

Saima and I took turns sitting beside Ayesha. We had no medicine left. We took clean water from our mosque bottle, soaked our cotton handkerchiefs, and applied cold compresses to her burning forehead, her neck, and her wrists for six continuous hours until the fever finally broke at dawn.

When Ayesha opened her eyes as the morning sun filtered through the dusty window, pale and weak but breathing steadily, she looked at Saima and me.

She reached out her thin, trembling hand and whispered:

"Anam, if I survive this university, I will never, ever let anyone lock me behind a gate again."

I held her hand tightly.

"You will survive, Ayesha," I whispered back. "We will all survive. And we will write down every single hour of these four days so that the world knows what they did to us behind these walls."
"""

with open(os.path.join(manuscript_dir, "09_chapter_9.md"), "r", encoding="utf-8") as f:
    ch9_text = f.read()

if "The four days of the siege revealed the true" not in ch9_text:
    split_point = "---"
    parts = ch9_text.split(split_point)
    new_ch9 = parts[0] + ch9_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "09_chapter_9.md"), "w", encoding="utf-8") as f:
        f.write(new_ch9)
    print("Enriched 09_chapter_9.md successfully!")

# ---------------------------------------------------------------------------
# CHAPTER 11 ENRICHMENT: Rooftop Secrets and Sliced Mangoes
# ---------------------------------------------------------------------------
ch11_extra = """

The rooftop was also where our cultural memories came back to life.

In the classrooms below, we were forced to speak English or formal Urdu. If a student spoke in her mother tongue—Saraiki, Punjabi, or Balochi—she was looked down upon by the professors as "unrefined" or "rural." The department demanded that we shed our regional identities and adopt the sterile, polite language of the civil bureaucracy.

On the roof, under the desert stars, the ancient tongues of the Indus Basin returned with triumphant power.

Late at night, when the heat softened and the wind blew from the river Chenab, a girl named **Salma** from a canal village near Rajanpur would sit with her back against the brick chimney. 

Her family were tenant farmers who had lost their entire mud-brick home and four acres of cotton in the devastating Indus floods of the previous summer. Her parents and her four younger siblings were currently living in a temporary tent made of blue plastic tarpaulin on a canal embankment, while Salma sat on our roof studying international environmental protocols.

Salma had a deep, haunting, resonant singing voice.

She would close her eyes, rest her chin on her knees, and begin to sing the ancient Saraiki *Kafis* of the great nineteenth-century Sufi mystic poet of South Punjab, **Khwaja Ghulam Farid**:

> *"Apna des sambhal ve saavan,  
> Rohi de sab chhanvein thaye..."*  
> *(Look after your homeland, oh monsoon cloud,  
> The desert pastures of Rohi are thirsting for your rain...)*

Her voice floated across the dark concrete roof, rising into the desert night like an ancient river song. 

Two hundred young women fell completely silent. Girls from Gujranwala, girls from Rawalpindi, girls from Dera Ghazi Khan, and girls from Peshawar sat on their bedsheets, listening to that mournful, beautiful melody.

In that melody was the entire history of South Punjab: the centuries of drought, the flooded rivers, the peasant labor, the cotton pickers with bleeding fingers, and the silent endurance of women who had carried the burden of this earth on their heads for five thousand years.

When Salma finished singing, there were tears in the eyes of almost every girl on that roof.

Nobody spoke for several minutes. There was only the gentle rustle of the eucalyptus leaves and the distant whistle of the night train traveling along the main railway line toward Lahore.

Saima broke the silence. She picked up our plastic pitcher, poured cold water into four cups, and handed one to Salma.

"Salma," Saima said gently, "when the monsoon rains come this year, will your family return to their land?"

Salma took a sip of water, looked down at her bare feet, and smiled a faint, sad smile.

"The landlord told my father that the land belongs to the sugar mill now," she replied, her voice soft and steady. "The flood washed away the boundary stones, and the revenue patwari took fifty thousand rupees from the mill manager to rewrite the village land records. My father has no papers. He has only his hands."

She looked up at the stars.

"That is why I am sitting on this roof, Saima," Salma said, her eyes flashing with a sudden, fierce light in the dark. "My father cannot read the revenue registers. My brothers cannot read the court notices. The landlord steals our land because he knows we cannot read his English laws. 

"I have two semesters left in the Department of Law. When I receive my degree, I am going to walk into the Kachehri in Rajanpur, I am going to open those revenue books, and I will show that landlord that my father's daughter knows every single section of the law."

I sat in the dark, listening to Salma's words.

I felt a shiver run down my spine: not of fear, but of profound, sacred awe.

The rulers of our country think that the girls in these public universities are weak, passive creatures who can be controlled through warden registers and locked iron gates.

They have no idea who is sitting on these roofs.

They do not understand that beneath these cheap lawn dupattas, beneath these faded plastic sandals, and behind these polite bows of submission, an entire generation of women is sharpening its intellect like a surgeon's knife.

They are learning the law. They are learning the economics. They are learning the data.

And when they step out through those gates, the ancient feudal order that has ruled this country for two centuries will find itself facing an army of daughters who can no longer be bought, frightened, or silenced.
"""

with open(os.path.join(manuscript_dir, "11_chapter_11.md"), "r", encoding="utf-8") as f:
    ch11_text = f.read()

if "The rooftop was also where our cultural memories" not in ch11_text:
    split_point = "---"
    parts = ch11_text.split(split_point)
    new_ch11 = parts[0] + ch11_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "11_chapter_11.md"), "w", encoding="utf-8") as f:
        f.write(new_ch11)
    print("Enriched 11_chapter_11.md successfully!")

# ---------------------------------------------------------------------------
# CHAPTER 14 ENRICHMENT: The Defiant Desk
# ---------------------------------------------------------------------------
ch14_extra = """

The technical execution of the research required us to master tools that our political science professors did not even know existed.

While the students in the department were writing thirty-page essays about Aristotle's classification of constitutions using ballpoint pens on lined paper, M Yousaf and I were constructing automated data extraction pipelines using Python.

Every night between 1:00 AM and 3:00 AM, when the university network bandwidth was unburdened by daytime traffic, Yousaf ran automated scripts to scrape historical regulatory filings from the official digital portals of the National Electric Power Regulatory Authority (NEPRA) and the Oil and Gas Regulatory Authority (OGRA).

We extracted the tariff petition documents of forty-four private power generation companies.

We analyzed the capital expenditure balance sheets, the fuel cost adjustment notifications, and the sovereign debt amortization schedules. 

What the data revealed was a mathematical crime against the people of Pakistan.

We proved that under the sovereign 1994, 2002, and 2015 power generation policies, private power plants were guaranteed an internal rate of return of up to seventeen percent in US dollars, indexed against currency devaluation and US inflation. 

When the Pakistani rupee collapsed from one hundred and fifty to nearly three hundred rupees per dollar, the sovereign capacity payment obligations doubled overnight: not because more electricity was produced, but because the contracts were designed to transfer the entire exchange-rate risk onto the public treasury.

We constructed **Table 1: Sovereign Capacity Payment Liabilities vs. National Health and Education Expenditures (2018–2024)**.

The table showed that in 2023, the federal government paid two point one trillion rupees to private power producers for idle capacity, while allocating less than one hundred and twenty billion rupees for federal public health, medical universities, and rural immunization programs combined. 

For every single rupee the state spent on the health of its citizens, it spent seventeen rupees servicing the idle machinery of private corporate power cartels.

Next, we turned to the water data.

Working with hydrological telemetry records from the Indus River System Authority (IRSA) and the Punjab Irrigation Department, we mapped the water conveyance efficiency of the primary canal network of South Punjab: the Taunsa-Panjnad link canal, the Sidhnai canal, and the Haveli canal systems.

We constructed **Table 2: Conveyance Losses and Crop Water Productivity in the Indus Basin Irrigation System**.

The findings were staggering.

We proved that out of one hundred and forty-one million acre-feet of surface water entering the Indus Basin irrigation system at the rim stations, over twenty-nine point four million acre-feet was lost to unlined canal bed seepage, evaporation, and unmetered upstream diversions before it ever reached an agricultural watercourse.

Furthermore, our crop productivity models showed that Pakistan produces less than zero point four kilograms of cereal grain per cubic meter of water consumed: one of the lowest water productivity ratios in the developing world. 

Egypt, using water from the River Nile under comparable arid climatic conditions, produces three times as much grain per cubic meter of water through modern laser land-leveling and pressurized drip irrigation.

Our nation was not suffering from a hydrological curse. Our nation was bleeding water because our irrigation policies were designed in the nineteenth century to serve colonial revenue extraction, and maintained in the twenty-first century to serve feudal sugar-mill owners.

When M Yousaf and I completed the final econometric regressions, we sat in the reading room of the Central Library, looking at the printed charts spread across the wooden table.

"Look at this, Anam," Yousaf whispered, pointing his pen at the final regression line. "The correlation between transmission losses and elite political patronage is zero point eight-seven. It is a statistically undeniable relationship. The power theft is not occurring in the slums; the power theft is concentrated in the industrial feeder lines and the agricultural tube wells of influential political constituencies."

We had built an unshakeable empirical fortress.

There was no political slogan in our paper. There was no emotional rhetoric. There was no ideological posturing.

There were only cold, clean, verified mathematical facts: seventy-eight regulatory references, twenty-four historical data tables, and five computational models that proved, beyond the shadow of a doubt, that the poverty of Pakistan was an engineered, administrative extraction mechanism.

When Dr. Farooq and Dr. Aslam rejected the manuscript in their office, they thought they were burying another student's voice.

They did not understand that in the twenty-first century, science cannot be locked inside a department filing cabinet.

When the confirmation email from CERN Zenodo arrived at 4:32 PM on that Tuesday afternoon in the internet cafe near Chungi Number Nine, assigning our paper permanent **DOI: `10.5281/zenodo.24054373`**, I did not feel personal pride.

I felt a profound, sacred vindication for every girl who had ever been silenced in this province.

I thought of Zahra, whose marks had been slashed to forty-two.  
I thought of Maryam, whose books were locked in a village crawlspace.  
I thought of Fatima, who had starved herself for five days in a grain shed just to earn the right to read.

This publication was our answer to their tyrants.

They had used their red pens to erase our names from their department honors lists.

We had used our minds to write our names into the global scientific record of human civilization.
"""

with open(os.path.join(manuscript_dir, "14_chapter_14.md"), "r", encoding="utf-8") as f:
    ch14_text = f.read()

if "The technical execution of the research required us" not in ch14_text:
    split_point = "---"
    parts = ch14_text.split(split_point)
    new_ch14 = parts[0] + ch14_extra + "\n---\n" + parts[1]
    with open(os.path.join(manuscript_dir, "14_chapter_14.md"), "w", encoding="utf-8") as f:
        f.write(new_ch14)
    print("Enriched 14_chapter_14.md successfully!")
