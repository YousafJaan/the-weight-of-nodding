# -*- coding: utf-8 -*-
import os
import re

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

with open("manuscript/FULL_MANUSCRIPT.md", "r", encoding="utf-8") as f:
    full_text = f.read()

sections = re.split(r'\n(?=# Chapter|\n# Prologue)', full_text)

# Chapter 4 is index 5
ch4 = sections[5]
ch4 = ch4.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")

ch4_stories = """
The corridors of Amna Hall did not merely hold academic notes and examination panic; they held the secret, dangerous emotional entanglements of girls who were experiencing psychological freedom for the very first time in their lives.

Two of those entanglements shook our wing to its foundations.

The first was the story of **Aqsa and Ammar**.

Aqsa had arrived in Multan from a conservative, mud-brick basti on the agricultural periphery of Muzaffargarh. She was an extraordinarily beautiful girl, with large, sorrowful eyes, a gentle voice, and a deep, village-bred piety that made her stand apart from the urban students. Before she set foot on the campus bus, she had placed her hand on her father's shoulder and sworn a sacred oath: she would wear her black abaya every single day, she would keep her eyes fixed on the pavement, she would not engage in modern campus frivolity, and she would never, under any circumstance, allow a man to enter her heart.

For her first two semesters, Aqsa was an untouchable fortress of modesty. She walked straight from Amna Hall to the Political Science lecture halls, attended her classes with downcast eyes, and returned immediately to the hostel library.

Then came Ammar.

Ammar was a third-year classmate from a prominent family in Khanewal: confident, articulate, wearing tailored kurtas and driving a red motorcycle that he parked ostentatiously near the department veranda. For seven relentless months, Ammar pursued Aqsa with the single-minded focus of a hunter. He sent study guides through third parties. He sat two rows behind her in every seminar. He left polite notes in her library books. For seven months, Aqsa repelled every advance with stony, freezing silence, refusing even to look in his direction.

Then came the day of the public explosion.

During a crowded departmental symposium in the main auditorium, before sixty students and three junior lecturers, Ammar lost his patience with her silence. He stood up in the middle of the lecture hall, walked down the aisle, and staged a dramatic, impassioned declaration of his love. He declared to the entire department that Aqsa was his destined wife, that no other male student should dare look in her direction, and that his intentions were honorable and pure.

The hall was stunned into breathless silence. For a girl from a traditional Muzaffargarh basti, where a girl's name mentioned in public with a boy meant an instant family jirga, disownment, and immediate forced marriage, Ammar's public stunt was not romantic. It was a terrifying public humiliation.

Aqsa rose from her wooden chair like an enraged queen. With a voice that rang through the rafters like a whip, she tore Ammar's dignity to shreds before the entire faculty. She called him a cowardly, dishonorable boy who possessed neither the manners of a gentleman nor the fear of God. She demanded that the department disciplinary committee take notice of his harassment, packed her books with trembling hands, and walked out of the auditorium with her head held high.

Yet human psychology is a dark, contradictory labyrinth.

That public confrontation broke the emotional wall between them. Over the following weeks, Ammar sent desperate, tearful apologies through mutual acquaintances, swearing that his outburst had been driven by overwhelming devotion rather than disrespect. Slowly, insidiously, Aqsa's righteous fury turned into curiosity, and that curiosity softened into conversation. Within three months, the girl who had sworn never to look at a man had fallen deeply, completely, and helplessly in love with Ammar.

And that was when the trap snapped shut.

The moment Aqsa gave her heart, the power dynamic inverted completely. Ammar, having achieved his conquest, began to retreat. He became cold, distant, and erratic. When Aqsa, terrified of discovery and longing for legitimate honor, pleaded with him to send his mother with a formal marriage proposal to her father, Ammar laughed, calling her naive and claiming that they needed years to understand each other before discussing marriage.

Every ignored message, every cold dismissal plunged Aqsa into a vortex of acute physical panic, culminating in the midnight episodes where she would burst into Room 42, turn off our cooling fans in forty-degree heat, and weep in our laps until dawn.

The second entanglement was even more bizarre and tragic: **The Loyalty Test of Saba and Anza**.

Saba, who lived in the gallery adjacent to Room 42, had a close departmental classmate from Vehari. This classmate had been secretly dating a charismatic student politics activist, but she was plagued by constant doubts regarding his fidelity. Suspecting that her boyfriend was flirting with other girls on WhatsApp, the classmate hatched a clandestine surveillance plot and enlisted Saba's help.

Saba brought the boy's mobile number into Room 42 and handed it to Anza.

"Anza," Saba had whispered conspiratorially, closing our wooden door. "My friend needs a girl who is clever, witty, and completely immune to male charms to test her boyfriend. You text him from a new SIM card. Flirt with him slightly. See if he bites the bait or if he stays loyal to her. If he tries to arrange a secret meeting, we will take screenshots and hand them to my friend."

Anza, who considered herself an untouchable cynic regarding campus romances, accepted the assignment with theatrical confidence. She bought a new SIM card, created a fictional persona, and sent the boy an enigmatic, teasing greeting.

The boy took the bait within three minutes.

For the first forty-eight hours, it was a hilarious covert game inside Room 42. Anza would draft witty, sarcastic messages while Sara and I watched, documenting how eagerly the boy abandoned his declared loyalty to Saba's friend. But then, as the text conversations deepened over late nights, something catastrophic occurred.

The boy was genuinely brilliant, sharp-tongued, and possessing a dark, poetic charisma that pierced straight through Anza's intellectual defenses. Within ten days, the fake surveillance chat had transformed into a raw, intense, authentic emotional connection.

Anza, who had set out to catch a traitor, was caught in the trap herself.

She stopped showing us the messages. She began staying awake until three in the morning, her face illuminated by the pale blue light of her phone screen, smiling with an expression of tender, secret intoxication that terrified me. When she finally confessed the truth to me on our cot, she was shaking with violent, uncontrollable guilt.

"Anam, main kya karoon?" Anza had sobbed, burying her face into my chest while the rain poured down onto the tin roof outside. "Mera dil baahar nikalne lag gaya hai! I was supposed to expose him for my friend, and now I cannot breathe if he does not text me for an hour! I feel like a disgusting traitor, but I love him. Main kya karoon?"

In Room 42, I found myself sitting between two shattered worlds: on one cot sat Aqsa, sobbing because a boy was pulling away; on the other cot sat Anza, sobbing because she had fallen for a boy she was supposed to destroy.

And in the middle of them stood I: nodding, consoling, offering water, absorbing their hysteria, carrying the crushing, silent weight of their secrets while my own spine burned with unaddressed fever.
"""

ch4 = ch4.replace("# Chapter 4: The Currency of Sifarish (Allotment)\n", "# Chapter 4: The Currency of Sifarish (Allotment)\n\n" + ch4_stories + "\n\n")
ch4 = clean(ch4)
assert_no_dashes(ch4, "04_chapter_4.md")
with open("manuscript/04_chapter_4.md", "w", encoding="utf-8") as f:
    f.write(ch4)
print(f"Updated Chapter 4: {len(ch4.split())} words")

# Chapter 5 is index 6
ch5 = sections[6]
ch5 = ch5.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")

ch5_stories = """
By the winter of 2024, the sisterhood of Room 42 had become an emergency ward for female distress, and the greatest crisis of all was **The Engagement Crisis of Saba**.

Saba was the most sensible, intellectually grounded girl in our entire wing. Her family in Vehari had arranged her engagement two years prior to an honorable, educated cousin who worked as a civil engineer in Islamabad. The match was an ideal traditional union: approved by both families, respectable, and promising a stable, peaceful future. Saba had always worn her silver engagement ring with quiet, unpretentious pride.

Yet in the middle of our third year, the psychological pressure cooker of university life produced a dangerous fracture in Saba's composure.

A dashing young lecturer from another department had begun paying extraordinary personal attention to Saba during joint academic seminars. He praised her intellect, lent her rare academic volumes with personal inscriptions, and engaged her in long, philosophic conversations on the library lawn. To an intelligent young woman from an orthodox southern family, who had never experienced intellectual validation from an attractive male, the attention was intoxicating.

The lecturer began dropping subtle, devastating hints: that an arranged marriage was a prison for a brilliant woman, that her cousin was a provincial engineer who would never appreciate her mind, and that true intellectual peers should choose their own destiny.

Saba was on the verge of emotional suicide.

She stopped wearing her silver ring, hiding it inside a brass cold-cream container under her pillow. She began speaking of breaking her engagement, defying her father, and declaring her autonomy. She did not realize that the lecturer was a serial campus predator who used philosophic flattery to manipulate young female students every semester, discarding them the moment their family honor was compromised.

It was on a freezing Thursday night in December that the confrontation occurred inside Room 42.

Saba came into our room with a handwritten letter in her hand, her eyes rimmed with red. She was preparing to call her elder brother in Vehari the following morning to declare that she would refuse the wedding.

I locked the wooden door of Room 42. I made Anza sit on the window cot, and I sat Saba down directly across from me at our scarred study table. I placed a hot cup of tea between her cold hands.

"Saba," I said, looking straight into her eyes, keeping my voice stripped of all anger, steady and piercing. "Listen to me as a sister who loves you enough to tell you the raw, unvarnished truth. You are about to throw your entire family into social disgrace and destroy your own future for a mirage made of borrowed English vocabulary."

For the next three hours, I did not preach traditional morality. I spoke to Saba in the cold, empirical language of political and economic reality that we studied every day.

I mapped out the landscape for her: the lecturer had three previous complaints quietly buried by the dean's office; he lived in a university bungalow protected by tenure; he would never bring a formal marriage proposal to her father in Vehari; the moment her brother disowned her, the lecturer would disavow all connection with her, and she would be left isolated, ruined, and socially executed in South Punjab.

"Look at your cousin," I urged her, holding her cold fingers. "He respected your father. He agreed that you should complete your master's degree before the wedding. He sends you books without demanding secret phone calls. That is real honor, Saba. Do not confuse the cheap glamour of an academic flirtation with the lifelong loyalty of a man who respects your roots."

Saba broke down, weeping into my shoulder, trembling as the romantic illusion shattered inside her chest.

That night, we took the brass cold-cream container. Saba took out her silver engagement ring. She cleaned it with the edge of her shawl and slipped it back onto her left finger. I helped her draft a polite, formal text message to the lecturer, terminating all private communication outside the seminar room.

Today, Saba is happily, peacefully married to that honorable cousin. She lives with dignity and security, and whenever we speak on the phone, she reminds me that my midnight intervention in Room 42 was the anchor that saved her life.

And then came the departure that permanently altered our circle: **The Wedding of Sara**.

At the beginning of our seventh semester, Sara, who had shared Room 42 with Anza and me since our very first day, reached the end of her hostel journey. Her wedding had been finalized during the winter break.

The week before her departure was an emotional tempest inside Amna Hall. We packed her iron trunks with her lab coats, her chemistry textbooks, and her embroidered bridal shawls. On her final night in Room 42, all of us gathered on our floor: Anam, Anza, Sara, Aqsa, Saba, and Palwasha. We cooked a huge pot of spiced rice on our illegal electric coil, ate from a shared metal platter, and laughed until our tears flowed into the food.

When Sara walked through the green iron gates of Amna Hall for the last time, wearing her bridal bangles and waving back at us from the car window, an era ended.

After Sara left, our circle settled into its permanent, legendary core: **Anam, Anza, Aqsa, and Saba**, with Palwasha remaining our sweet, devoted companion down the hall. We were no longer merely roommates or neighbors; we were battle-tested comrades who had seen each other stripped of every pretense, holding each other's secrets, and refusing to let each other fall.
"""

ch5 = ch5.replace("# Chapter 5: The Circle of Seven (Room 34 Secrets)\n", "# Chapter 5: The Circle of Seven (Room 34 Secrets)\n\n" + ch5_stories + "\n\n")
ch5 = clean(ch5)
assert_no_dashes(ch5, "05_chapter_5.md")
with open("manuscript/05_chapter_5.md", "w", encoding="utf-8") as f:
    f.write(ch5)
print(f"Updated Chapter 5: {len(ch5.split())} words")

# Chapter 6 is index 7
ch6 = sections[7]
ch6 = ch6.replace("Khadija Hall", "Amna Hall").replace("Room 34", "Room 42")

evening_walks = """
Yet the memory that outshone all the hardships of Amna Hall was our sacred evening ritual: **The Walk to the BZU Main Gate**.

Every evening around seven o'clock, as the fierce Multan sun finally dipped behind the western mango orchards and the asphalt began to cool, the stifling rooms of Amna Hall became uninhabitable. The air inside smelled of dust and warm brick, and our minds were numb from academic theory.

That was when Palwasha would appear in our doorway, clapping her hands with childish glee: "Chalo larkiyo! Utho! The sun has set, the breeze is coming from the orchards, and the samosa vendor at the main gate is frying fresh batches!"

Within five minutes, the four of us, Anam, Anza, Aqsa, and Saba, accompanied by Palwasha, would emerge from Amna Hall.

The walk from Amna Hall to the BZU Main Gate on Bosan Road was nearly a mile and a half along the wide, tree-lined university avenue. The path was shaded by ancient eucalyptus and neem trees, whose leaves rustled gently in the southern twilight. On both sides lay the sprawling green lawns of the university, where the evening shadows stretched long and cool.

Those walks were our only sanctuary of pure, unadulterated freedom.

On that road, we were not daughters under surveillance or students under administrative threat. We walked five abreast, our arms linked together, laughing until our stomachs ached. Anza would mimic the pompous accents of visiting Islamabad professors, making us double over with laughter. Aqsa, relaxed beneath her black abaya, would tell hilarious stories about village jinj weddings in Muzaffargarh. Saba would share practical gossip about department scholarships, and Palwasha would skip ahead, picking fallen jasmine flowers to tuck behind our ears.

At the Main Gate, where the bustling traffic of Bosan Road roared past, we would gather around the street carts. We bought roasted corn rubbed with lemon and black salt, spicy potato samosas dripping with mint chutney, and chilled bottles of lemon soda that hissed when opened. We stood on the footpath, eating from brown paper bags, watching the colorful city buses speed toward Multan Cantt, feeling the immense, untamed pulse of the world outside.

We walked slowly back under the starlit sky, timing our arrival to eight-forty-five, just fifteen minutes before the heavy iron gates of Amna Hall were locked with chains for the nine o'clock curfew.

Those evening walks were our life support. They reminded us that despite the poverty of our institutions, despite our aching bodies, and despite the endless compromises demanded of us by society, our youth was alive, vibrant, and fiercely beautiful.
"""

ch6 = ch6.replace("# Chapter 6: Khara Paani (The Saline Water)\n", "# Chapter 6: Khara Paani (The Saline Water)\n\n" + evening_walks + "\n\n")
ch6 = clean(ch6)
assert_no_dashes(ch6, "06_chapter_6.md")
with open("manuscript/06_chapter_6.md", "w", encoding="utf-8") as f:
    f.write(ch6)
print(f"Updated Chapter 6: {len(ch6.split())} words")
