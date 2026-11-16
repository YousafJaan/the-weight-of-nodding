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

# Read the original rich texts from FULL_MANUSCRIPT.md
with open("manuscript/FULL_MANUSCRIPT.md", "r", encoding="utf-8") as f:
    full_text = f.read()

import re
sections = re.split(r'\n(?=# Chapter|\n# Prologue)', full_text)

# Prologue is index 1
prologue = sections[1]
prologue = prologue.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")
prologue = clean(prologue)
assert_no_dashes(prologue, "00_prologue.md")
with open("manuscript/00_prologue.md", "w", encoding="utf-8") as f:
    f.write(prologue)
print(f"Updated Prologue: {len(prologue.split())} words")

# Chapter 1 is index 2
ch1 = sections[2]
ch1 = ch1.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")
# Ensure Anza and Sara are prominently established as the roommates in Room 42
ch1 = ch1.replace("my roommates lay asleep", "my two roommates, Anza and Sara, lay asleep")
ch1 = clean(ch1)
assert_no_dashes(ch1, "01_chapter_1.md")
with open("manuscript/01_chapter_1.md", "w", encoding="utf-8") as f:
    f.write(ch1)
print(f"Updated Chapter 1: {len(ch1.split())} words")

# Chapter 2 is index 3
ch2 = sections[3]
ch2 = ch2.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")
# Add the vivid Allergy Protocol narrative of Anza and the morning dynamic
allergy_scene = """
The morning routine in Room 42 was governed by an unspoken domestic treaty, and at the center of that treaty was Anza's legendary Allergy Protocol.

Anza was one of the dearest, most fiercely loyal friends I would ever have in my life, but sharing a twelve-by-fourteen room with her was an ongoing masterclass in human negotiation. She was a girl of delicate sensibilities, sharp humor, and an immovable aversion to manual cleaning chores. Whenever it was her scheduled turn to sweep the concrete floor or dust the window ledges, she would immediately wrap her woolen shawl tightly around her throat, produce a series of gentle, theatrical coughs, and look at me with wide, tragic eyes.

"Anam," she would announce with complete medical conviction, sitting cross-legged on her quilt and tucking her hands securely into her sleeves. "There is a fresh layer of dust near the wooden wardrobe. If I touch that broom, the Multani silt will enter my bronchioles, my hands will break out in allergic hives, and my throat will swell shut before the first lecture. Mujhe shadeed dust allergy hoti hai. You sweep, Anam. I will sit here on the cot and supervise the perimeter to ensure no corners are missed."

Sara, who was busy ironing her laboratory coat over an old towel on her cot, would invariably burst into laughter.

"Anza, you have an allergy to the broom, an allergy to washing the teacups, and an allergy to carrying the bucket down to the courtyard," Sara would tease, pressing the iron firmly along the sleeve. "The only phenomenon in the entire province of Punjab you are not allergic to is sitting on that mattress, eating roasted pistachios, and drinking five cups of black tea while Anam cleans the room!"

"Sara baji, you mock what you do not understand," Anza would reply without breaking character for a fraction of a second. "Multani dust contains alkaline kiln particles. A girl of sensitive respiratory constitution must protect her health for the sake of her future education."

And while Anza inspected the room with aristocratic detachment, criticizing every speck of lint on the rug while refusing to touch the broom, she was also the first person to jump between us and any administrative threat. If a hostel supervisor entered our corridor to bully us about late entry slips, Anza would rise from her cot like an advocate before the High Court, her allergies completely forgotten, dismantling the supervisor's arguments with such blistering legal fluency that the official would retreat down the stairs in silence.
"""

# Insert the allergy scene smoothly into Chapter 2 before the walk
if "The morning routine" in ch2:
    ch2 = ch2.replace("The morning routine", allergy_scene + "\n\nThe morning routine")
else:
    ch2 = ch2.replace("# Chapter 2: The Red Line on Bosan Road\n", "# Chapter 2: The Red Line on Bosan Road\n\n" + allergy_scene + "\n\n")

ch2 = clean(ch2)
assert_no_dashes(ch2, "02_chapter_2.md")
with open("manuscript/02_chapter_2.md", "w", encoding="utf-8") as f:
    f.write(ch2)
print(f"Updated Chapter 2: {len(ch2.split())} words")

# Chapter 3 is index 4
ch3 = sections[4]
ch3 = ch3.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")

fan_scene = """
Yet no account of summer inside Amna Hall would be complete without documenting the legendary Fan and Cooler Shut-Off Protocol, an event that became etched forever into the emotional folklore of Room 42.

It occurred during the searing heat of early June, when the outside temperature lingered at forty-two degrees even at two in the morning. The masonry of the hostel was radiating heat like a bread oven. Inside Room 42, our ceiling fan was spinning at maximum velocity, and our window-mounted desert cooler was roaring at full throttle, pumping out a precious, damp stream of cool air that made sleep barely possible. Anza and I were fast asleep under thin cotton sheets, exhausted after hours of memorizing international relations treaties.

At exactly two-forty in the morning, the heavy wooden door of Room 42 was kicked open with a terrifying crash.

I bolted upright, gasping for air, thinking that a water pipe had burst or that an electrical fire had broken out in the corridor. Anza sat up on her cot, screaming in panic, clutching her quilt to her collarbone.

Standing in the doorway, framed against the amber courtyard lamp, was Aqsa.

She looked entirely unhinged by grief. Her black dupatta was twisted violently around her neck, her hair was damp with perspiration, her eyes were swollen and bloodshot, and her chest was heaving with rapid, desperate sobs. She had spent the entire evening across the corridor in the eastern portion, engaged in a tortuous text-message confrontation with Ammar, the classmate who had pursued her for seven months and was now growing cold and distant.

"Utho!" Aqsa screamed, her voice trembling with hysteria as tears streamed down her cheeks. "Utho! Tumhein pata hai meri kya halat ho rahi hai aur tum log sukoon se so rahi ho! Utho meri baat suno!"

"Aqsa? What happened? Are you hurt?" I asked, scrambling out of bed and hurrying toward her.

"Mera dil baahar nikalne lag gaya hai!" she cried, clutching her chest with both hands as if her ribs were cracking. "Main mar rahi hoon! Ammar has not replied to my message for four hours! He read my text and went offline! My heart is bursting, Anam! Main mar jaungi!"

Before Anza or I could offer a single soothing word, Aqsa charged across the room directly to the plastic switchboard near our wardrobe.

CLACK. CLACK.

With two furious flicks of her fingers, she switched off the desert cooler. She switched off the ceiling fan.

The cooling roar vanished instantly. Above our heads, the three heavy metal blades slowed to a lazy crawl and stopped. Within thirty seconds, the damp, suffocating, forty-degree heat collapsed onto Room 42 like a sodden wool carpet. The air became motionless and stifling, making it difficult to draw a full breath.

"Aqsa! Have you lost your mind?" Anza shrieked, springing up on her mattress, her hands in her hair. "Turn the fan back on! It is forty-five degrees in here! We will suffocate to death in five minutes!"

"No!" Aqsa shouted back, her eyes blazing through her tears. "No cooler! No fan! Bas koi shor na ho! Na cooler ka shor, na pankhe ka shor! I cannot hear my own soul with that roaring motor! You must listen to me! I am dying, and all you care about is cold air! Sit down and listen to my heart! Mujhe hosla do, meri baat samjho!"

I looked at Anza, who was staring at Aqsa with absolute, murderous disbelief. Then I looked at Aqsa, who was trembling so violently that her knees were knocking together. She was a village girl from a conservative basti near Muzaffargarh who had dared to give her heart to a smooth-talking university boy, and who now felt her entire world disintegrating into shame and abandonment.

"Anza, be patient," I whispered.

I grabbed two cardboard exam clipboards from the desk. I handed one to Anza and sat down on the floor rug, gently pulling Aqsa down beside me. For the next two hours, in the pitch-black, airless furnace of Room 42, Anza and I waved those cardboard clipboards with aching wrists, fanning the heavy air toward Aqsa while she wept, recited Ammar's broken promises, and sought our reassurance.

Whenever Anza quietly reached her foot out toward the wall switch to turn the fan on low, Aqsa would scream: "Don't touch it! The whirring sound drives me crazy! Let there be silence!"

We sat in that suffocating heat until four in the morning, listening to her pour out her terror of dishonor and heartbreak, fanning her until our clothes were drenched with sweat. Only when the first call to prayer echoed across Bosan Road did Aqsa finally calm down, drink a glass of water, and return quietly to her room.

The second the door clicked shut behind her, Anza leapt across the room and slammed both switches down with the fury of a storm.

CLACK. CLACK.

The cooler roared. The fan whipped the air into a frenzy. Anza stood directly beneath the spinning blades, lifting her dripping face to the wind, panting like an athlete at the end of a marathon.

"That girl is an emotional terrorist!" Anza declared with venomous passion, wiping sweat from her chin. "She has no mercy in her soul! Na khud sukoon karti hai, na humein karne deti hai! If she ever turns off our fan again in forty-degree heat, Anam, I swear I will bolt this door from the inside and let her weep in the hallway until the sun comes up!"

I fell back onto my cot, laughing despite my exhaustion and aching back. In Amna Hall, survival was not just about enduring the university administration; it was about absorbing the collateral emotional damage of our sisters' shattered hearts.
"""

# Insert into Chapter 3
ch3 = ch3.replace("# Chapter 3: Behind the Green Iron Gates\n", "# Chapter 3: Behind the Green Iron Gates\n\n" + fan_scene + "\n\n")
ch3 = clean(ch3)
assert_no_dashes(ch3, "03_chapter_3.md")
with open("manuscript/03_chapter_3.md", "w", encoding="utf-8") as f:
    f.write(ch3)
print(f"Updated Chapter 3: {len(ch3.split())} words")
