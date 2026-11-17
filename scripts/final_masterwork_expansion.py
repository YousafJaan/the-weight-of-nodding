# -*- coding: utf-8 -*-
"""
final_masterwork_expansion.py
Final polishing and expansion pass bringing Chapters 06 to 17 to ~3,350 words each.
Total chapter words will reach ~59,500 words (matching full 236-page print standard).
Strictly 0 em-dashes and 0 en-dashes.
"""
import os
import re

def clean_text(t):
    t = t.replace('\u2014', ', ')
    t = t.replace('\u2013', ', ')
    t = re.sub(r' +', ' ', t)
    return t

def enrich_chapter(fname, text_to_insert):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fpath = os.path.join(root, "manuscript", fname)
    with open(fpath, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    marker = "### The Strategist's Margin: Tactical Protocols for Daring Women"
    if marker in content:
        parts = content.split(marker, 1)
        new_content = parts[0].strip() + "\n\n" + text_to_insert.strip() + "\n\n" + marker + parts[1]
    else:
        new_content = content.strip() + "\n\n" + text_to_insert.strip() + "\n"
    
    cleaned = clean_text(new_content)
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(cleaned)
    words = len(cleaned.split())
    dashes = cleaned.count('—') + cleaned.count('–')
    print(f"Final Enriched {fname}: {words:,} words | {dashes} dashes")

final_expansions = {
    "06_chapter_6.md": """
### The Jurisprudential History of Environmental Litigation

The legal battle over the potable water of Amna Hall must be situated within the broader evolution of South Asian public interest environmental litigation.

In the 1980s and 1990s, the Supreme Court of India under Justice P.N. Bhagwati and the Supreme Court of Pakistan under Chief Justice Nasim Hasan Shah pioneered the concept of epistemic standing in environmental law. In traditional common law, an individual could only sue if they had suffered direct, personal financial damage. Under the revolutionary doctrine of public interest environmental litigation, any citizen, researcher, or collective gained the legal right to approach the superior courts directly under original constitutional jurisdiction to enforce environmental and biological protection on behalf of vulnerable populations.

When our circle prepared the water quality petition, we utilized this specific legal architecture.

We did not frame the issue as a private administrative grievance between students and a university warden. We framed it as a violation of the Public Trust Doctrine: an ancient legal principle dating back to Roman Emperor Justinian, codified in common law, which holds that certain natural resources, including clean air, running water, and navigable rivers, are held by the state in sovereign trust for the free, unpolluted use of the entire public.

When a university administration allows an underground sewage line to contaminate a student drinking aquifer, it is not merely committing an administrative oversight; it is committing a criminal breach of public trust.

By citing the Public Trust Doctrine and presenting calibrated spectrophotometric measurements, Sara and I demonstrated to the university legal advisors that their institutional shield was entirely porous. We showed them that if this dossier was placed before the Green Bench of the Lahore High Court, the court would not merely issue an administrative reprimand; it would issue a writ of mandamus, appoint an independent judicial commission, and hold senior university engineers personally liable for criminal environmental negligence.

It was this legal mastery that transformed our laboratory data into an irresistible administrative lever, forcing the allocation of capital for the deep tubewell.
""",

    "07_chapter_7.md": """
### The Political Theory of Famine and Extraction: Amartya Sen

In his 1981 foundational economic masterpiece *Poverty and Famines: An Essay on Entitlement and Deprivation*, Nobel laureate Amartya Sen established a revolutionary thesis: famines and acute nutritional crises are rarely caused by a physical decline in food availability. Instead, they are caused by catastrophic failures in food entitlement systems: the legal, economic, and institutional mechanisms through which individuals command food in a society.

Sen proved that in authoritarian systems lacking democratic feedback and free press mechanisms, ruling elites can allow captive populations to starve or suffer malnutrition in plain sight, because the sufferers possess zero institutional leverage to penalize the rulers.

The dining hall of Amna Hall was a micro-scale manifestation of Sen's entitlement failure.

Food was physically abundant in Multan. The grain markets of Galla Mandi, located three miles south of the campus, were overflowing with high-grade wheat, basmati rice, and fresh vegetables from the fertile irrigated districts of southern Punjab. The university possessed an operating budget sufficient to procure premium nutritional rations for its residential scholars.

Yet, inside the dining hall, six hundred adult women were subjected to chronic nutritional degradation.

Why? Because Haji Manzoor and the university administration had disenfranchised the students' economic entitlement. By making the monthly coupon subscription mandatory, banning independent external food delivery, and criminalizing cooking inside dormitory rooms, the administration severed the student's right to command food through market choice.

Our clandestine kitchen in Room 42 was an act of entitlement reclamation.

We broke Sen's entitlement failure by re-establishing direct market relations with independent agricultural producers outside the campus gates. And by organizing the escrow payment strike, we demonstrated that when a captive population regains its economic agency and withholds its financial tokens, the artificial scarcity created by the extraction cartel collapses into dust.
""",

    "08_chapter_8.md": """
### The Operational Velocity of Quick Services and Workx

The operational philosophy that Yousaf brought to our collaboration was grounded in the principles of Lean Manufacturing, the Theory of Constraints formulated by Eliyahu Goldratt, and the high-velocity execution methodologies of Silicon Valley enterprise engineering.

Through his enterprise venture Quick Services, Yousaf had pioneered a radical transformation in regional corporate logistics.

In traditional logistics networks across southern Punjab, freight operations were paralyzed by multi-tier manual paperwork, arbitrary police extortion checkpoints, and unpredictable driver scheduling that resulted in forty percent asset idle time. Quick Services eliminated this waste by implementing real-time telematics, automated dispatch algorithms, and transparent performance metrics that increased fleet velocity by sixty percent while reducing operational overhead.

Through his platform Workx, Yousaf applied these same operational engineering principles to human capital.

He recognized that thousands of exceptionally talented university graduates in cities like Multan, Faisalabad, and Bahawalpur were condemned to economic underemployment because traditional local employers operated as feudal patronage networks. Workx bridged this gap by creating direct, meritocratic pipelines connecting regional technical and analytical talent with high-growth international technology enterprises, providing remote workers with global market compensation and operational training.

In our collaborative research, Yousaf demonstrated that these enterprise methodologies could be applied directly to public sector governance.

"Anam," Yousaf would point out, sketching process flowcharts on the whiteboard in his office, "look at the journey of an administrative file inside BZU. It requires fourteen distinct manual signatures to approve an eight-hundred-rupee chemical reagent for a student laboratory, taking an average of forty-two days. Meanwhile, an administrative requisition for the vice chancellor's official guest tea is approved in four minutes. This is not an administrative procedure; it is an engineered bottleneck designed to extract bribes at every desk."

By applying Goldratt's Theory of Constraints to the university's procurement and administrative workflows, our paper demonstrated that ninety percent of institutional delays could be eliminated through automated digital approvals and decentralized fiscal authority.

Our collaboration proved that when the critical analytical rigor of political science is joined with the relentless operational velocity of enterprise engineering, there is no public sector failure that cannot be diagnosed, audited, and permanently solved.
""",

    "09_chapter_9.md": """
### The Jurisprudence of Habeas Corpus and Adult Female Autonomy

The legal confrontation that liberated Sidra from administrative custody at BZU was grounded in one of the most ancient and sacred legal instruments in Anglo-American and post-colonial constitutional law: the writ of Habeas Corpus.

Codified in Article 199 of the Constitution of the Islamic Republic of Pakistan, the writ of habeas corpus empowers the High Court to require that a person detained within its jurisdiction be brought before the court so that the court may satisfy itself that the person is not being held without lawful authority or in an unlawful manner.

In the conservative social landscape of Pakistan, patriarchal families and complicit educational institutions have historically operated on the false assumption that an unmarried daughter is the domestic property of her father, and that confining her against her will does not constitute unlawful detention.

The superior judiciary has repeatedly, unequivocally dismantled this feudal myth.

In dozens of landmark rulings, including the historic judgments *Mst. Humaira Mehmood v. State* (PLD 1999 Lahore 494) and *Mst. Saima Waheed v. State* (PLD 1997 Lahore 301), the Lahore High Court firmly established that:
1. An adult female of eighteen years or older is an autonomous legal citizen possessing full constitutional agency.
2. No father, brother, husband, or institutional authority possesses the lawful right to restrain her physical liberty, confiscate her identity documents, or compel her into marriage against her explicit consent.
3. Any institution or individual that facilitates the unlawful detention or forced marriage of an adult female is guilty of criminal kidnapping, wrongful confinement, and statutory human rights violations.

When our legal counsel stepped into the office of the Director of Student Affairs, she was armed with these exact constitutional precedents.

We did not make an emotional plea for mercy; we laid the law on the table like a loaded weapon. We showed the Director that if he attempted to hand Sidra's academic transcripts to her father, a habeas corpus bailiff would arrive at the university gates within eighteen hours, accompanied by criminal warrants naming him personally.

The law, so frequently abused to contain women, was deployed as our ultimate instrument of liberation. We proved that an educated woman who masters the legal statutes of her nation can walk out of the strongest feudal trap with her head held high.
""",

    "10_chapter_10.md": """
### The Micro-Sociology of the Photocopy Line: Spatial Subjugation

To fully appreciate the epistemic revolution executed by our Horizon Archive, one must understand the micro-sociological dynamics of the physical photocopy line outside Chacha Asghar's shop.

In his 1973 sociological study *The Presentation of Self in Everyday Life*, Erving Goffman analyzed how spatial arrangements and social rituals enforce status hierarchies between dominant and subordinate groups. Goffman observed that spatial exclusion is maintained through subtle, informal micro-behaviors that signal to the subordinate group that they do not belong in public territory.

The unpaved alleyway behind the Central Canteen was a textbook arena of spatial subjugation.

Male student union activists occupied the wooden benches outside the shop, their postures open, relaxed, and expansive: legs crossed, arms slung casually over the backs of chairs, cigarettes smoking, conversing in loud, authoritative voices that claimed the entire acoustic space of the alley.

When a female student entered this corridor to photocopy an academic syllabus, the social temperature shifted instantly.

The conversations would cease, replaced by an oppressive, predatory silence. Male eyes would track her physical progress along the path, performing what sociologist Carol Brooks Gardner defines as "public harassment": intrusive staring, calculated spatial blocking, and audible, evaluative comments regarding her clothing, posture, and appearance disguised as casual conversation.

To survive this gauntlet, female scholars were forced to adopt what Goffman called "the defensive self": eyes fixed on the gravel, shoulders hunched inward to minimize physical volume, moving rapidly, accepting delays and overcharges at the counter without protest, and exiting the space as quickly as possible.

This spatial humiliation was not an accident; it was an informal gatekeeping mechanism designed to increase the psychological cost of female academic diligence.

When Room 42 built the Horizon Archive and broadcast thousands of digitized textbooks directly into student rooms via local Wi-Fi, we did not merely provide free books.

We dismantled the spatial trap of the alleyway.

A female scholar was no longer required to run the predatory gauntlet of male stares to access the knowledge required for her degree. She could study in the dignified, unmonitored sanctuary of her own quarters, out-reading and out-thinking her male competitors in peace. We proved that technological democratization is the ultimate weapon against spatial subjugation.
""",

    "11_chapter_11.md": """
### Elias Canetti, Gustave Le Bon, and the Pathology of the Crowd

The violent student strike that paralyzed Bosan Road in autumn 2024 offers a chilling demonstration of the classical theories of crowd psychology formulated by French sociologist Gustave Le Bon and Nobel laureate Elias Canetti.

In his 1895 classic *The Crowd: A Study of the Popular Mind*, Le Bon argued that when individuals merge into an unorganized, emotional crowd, their conscious intellectual personality dissolves. The collective mind is governed entirely by contagion, emotional impulsivity, and the illusion of omnipotence. The individual in a crowd performs acts of destruction and violence that they would find unthinkable in their private, rational life.

In *Crowds and Power*, Canetti expanded this insight, explaining that crowds seek a discharge: a moment of sudden, explosive collective release where all social hierarchies and institutional boundaries are obliterated through destructive physical force.

The student unions on Bosan Road were caught in the exact grip of Canetti's discharge.

Fueled by political speeches, national economic frustration, and masculine group contagion, the crowd sought catharsis through destruction: smashing the automated turnstiles of the Metrobus, burning tires, and throwing rocks at police vans. In that moment of collective intoxication, the students believed they were exercising sovereign power.

In institutional reality, they were walking directly into the state's strategic trap.

As political scientist Gene Sharp demonstrated in his masterwork *The Politics of Nonviolent Action*, an authoritarian state is organized and equipped to conquer on the terrain of physical violence. When a dissident movement adopts violent tactics, it chooses to fight the state on the single battlefield where the state possesses overwhelming, asymmetric superiority: batons, tear gas, armored vehicles, and legal statutes of terrorism.

By resorting to disorganized violence, the student movement legitimized the state's deployment of anti-riot forces and alienated the broader civilian population.

Inside Room 42, we rejected the pathology of the crowd with absolute discipline.

We recognized that true, transformative power does not reside in the chaotic emotional contagion of the street; it resides in the cold, disciplined, and unyielding execution of strategic non-violence, legal counter-leverage, and superior institutional engineering.
""",

    "12_chapter_12.md": """
### The Thermal Physiology of Human Resilience

The extreme forty-eight-degree Multani summer was an empirical trial of the biological limits of the human nervous system.

In the medical literature on environmental physiology, thermal stress is recognized as a profound neurological disrupter. When core temperature rises above 38.5 degrees Celsius, the human body enters a state of systemic hyperthermia: cellular heat shock proteins (HSPs) are up-regulated, the permeability of the blood-brain barrier increases, and neurochemical neurotransmission across cortical synapses is severely compromised.

In Amna Hall, where uninsulated brick walls transformed rooms into thermal ovens and the electrical grid collapsed for fourteen hours a day, female scholars were subjected to this physiological assault on a daily basis.

Yet, human resilience is an extraordinary biological phenomenon.

Drawing upon the thermodynamic adaptations of ancient desert populations, our collective in Room 42 developed a comprehensive thermal survival doctrine:
- We adjusted our biological hydration protocols, adding precise quantities of mineral salts, potassium, and raw lemon to our water supplies to prevent hyponatremia and preserve electrolyte conductivity across muscle and nerve membranes.
- We turned our unpolished terrazzo floor into a continuous heat exchange sink, flooding the stone tiles with thin sheets of water that evaporated rapidly into the dry air, cooling the room's lower atmospheric stratum by seven degrees Celsius.
- We utilized our flat roof as a nocturnal sanctuary, breathing the cooler upper air, allowing our core body temperatures to reset beneath the desert stars.

We proved that human beings, when united by fierce collective solidarity and grounded in scientific understanding, can endure extreme physical adversity without surrendering their intellectual clarity.

The heat of Multan did not destroy our ambition; it burned away our superficial anxieties, leaving our minds as sharp, resilient, and enduring as ancient desert stone.
""",

    "13_chapter_13.md": """
### Bessel van der Kolk and Somatic Memory

The physical collapse I suffered in Seminar Room 4, and my subsequent hospitalization in Nishtar Wards, must be understood through the lens of modern trauma neuroscience, formulated by Dr. Bessel van der Kolk in *The Body Keeps the Score*.

Van der Kolk demonstrated that chronic psychological stress, interpersonal subjugation, and the systematic denial of authentic self-expression are not merely mental events; they leave deep, permanent imprints upon the physical neurobiology of the organism. The body stores the emotional trauma in altered autonomic nervous system wiring, chronic muscle tension, dysregulated endocrine cortisol curves, and systemic autoimmune inflammation.

For four years, I had treated my physical body as an irrelevant vehicle for my intellect.

Whenever I swallowed an objection to an authoritarian professor, whenever I forced my chin to nod while my soul burned with rage, my autonomic nervous system registered a threat signal that could neither fight nor flee. Under continuous societal conditioning, the natural physiological urge to push back or speak out was forcibly suppressed by my prefrontal cortex.

The result was what neuroscientists term **Somatic Conversion**: the unresolved psychological stress, finding no verbal or physical release, converts into chronic biological pathology.

My cardiac arrhythmias, my collapsed blood pressure, and my gastrointestinal paralysis were the physical symptoms of an organism that had reached its absolute biological threshold of compliance.

My healing in Room 42, nurtured by the unconditional love of Sara, Anza, Aqsa, Saba, and Palwasha, was not merely a physical recovery; it was an act of profound neuro-somatic de-conditioning.

I learned to listen to the whisper of my body before it was forced to scream. I unlearned the toxic habit of sacrificing my biological baseline for institutional deadlines. And I recognized that the greatest act of defiance an autonomous woman can commit is to keep her physical body healthy, rested, and whole in a world that seeks to consume her labor for free.
""",

    "14_chapter_14.md": """
### The Strategic Geometry of Sun Tzu's Strategic Retreat

The decision to freeze my academic degree and take a one-year medical hiatus is a direct validation of Chapter 3 of Sun Tzu's *The Art of War*: Attack by Stratagem.

Sun Tzu formulated five essential rules for military victory, the first of which is: *He will win who knows when to fight and when not to fight.* Sun Tzu observed that mediocre commanders, blinded by false pride and the fear of losing face, press forward into unfavorable terrain, exhausting their troops and courting total annihilation, while the master strategist yields ground without hesitation to preserve their core forces for the decisive counter-stroke.

In the conservative culture of South Asia, female persistence is frequently romanticized as continuous, unyielding endurance (*bardasht*).

A woman is expected to endure sickness, endure institutional abuse, and endure domestic humiliation without ever pausing or stepping back. Society celebrates her exhaustion as proof of her devotion, never recognizing that this romanticized endurance is a trap designed to run her into an early grave.

My one-year hiatus was an uncompromising rejection of the cult of endurance.

I refused to die for a master's degree. I recognized that my physical body was my only non-renewable strategic asset, and that to continue fighting on the hostile, corrupted terrain of Seminar Room 4 while my biology was collapsing was an act of profound tactical idiocy.

I yielded the terrain. I withdrew into rural solitude, allowing the academic cartels and the family gossips to celebrate their premature victory.

And in that solitude, I executed what military theorists call **Asymmetric Regeneration**:
- I restored my physical nervous system through clean nutrition, deep sleep, and natural movement.
- I deepened my intellectual weaponry, mastering econometric modeling, systems engineering, and advanced political philosophy.
- I forged my enterprise partnership with Yousaf, grounding my academic critique in the operational reality of Quick Services and Workx.

When I returned to BZU in 2025, I did not return as an exhausted student pleading for accommodation. I returned as a fully armed institutional strategist who understood precisely how to out-think, out-maneuver, and permanently defeat the academic gatekeepers of the university.
""",

    "15_chapter_15.md": """
### Thomas Kuhn and the Structure of Academic Revolutions

The intellectual warfare surrounding my thesis defense must be viewed through the philosophical framework of Thomas Kuhn's 1962 masterwork *The Structure of Scientific Revolutions*. Kuhn demonstrated that scientific disciplines do not evolve through smooth, continuous accumulation of knowledge; they advance through catastrophic **Paradigm Shifts**.

Entrenched academic elites operate within what Kuhn called "Normal Science": a stagnant intellectual regime where researchers solve minor puzzles defined by existing theoretical dogmas, never questioning the foundational assumptions of the paradigm. When anomalous empirical data emerges that threatens the established paradigm, the old guard responds not with scientific curiosity, but with violent defensive suppression.

The Department of Political Science at BZU was locked in a dead, decaying paradigm of Normal Science.

Dr. Qureshi and the senior faculty had spent thirty years teaching that the state is an unassailable sovereign monolith, that bureaucratic authority is synonymous with public welfare, and that student obedience is the highest civic duty.

My thesis was an empirical paradigm shift.

By presenting hard, quantitative data on procurement kickbacks, transport bottlenecks, and the macroeconomic cost of gendered curfews, I introduced anomalous reality that the old paradigm could neither explain nor absorb.

The faculty attempted to crush the paper because they recognized that if my methodology was legitimized, their own thirty-year careers of writing sycophantic, un-empirical essays would be exposed as intellectually worthless.

My victory was achieved by applying Kuhn's ultimate insight: a paradigm shift cannot be negotiated with the old guard; it must be authenticated by the broader, international scientific community.

By securing independent blind reviews from European university chairs and depositing the research on CERN Zenodo, I bypassed the dying paradigm of the local department, and forced the local gatekeepers to surrender before the unassailable light of modern empirical science.
""",

    "16_chapter_16.md": """
### The Policy Legacy of Pakistan Is Not Poor, It Is Poorly Managed

The publication of *Pakistan Is Not Poor, It Is Poorly Managed* (CERN Zenodo DOI: 10.5281/zenodo.24054373) established a new public policy benchmark for economic and institutional reform in southern Punjab and across Pakistan.

The monograph did not stop at theoretical critique; it provided an executable national reform roadmap across three critical frontiers:

1. **The Modernization of Agrarian Logistics:** We provided detailed engineering blueprints for decentralized, solar-powered cold-storage hubs along the National Highway and motorway corridors, demonstrating that an investment of twenty billion rupees in post-harvest preservation would prevent sixty billion rupees in annual food losses, stabilizing food inflation for working-class urban consumers.
2. **The Digitization of Public Sector Procurement:** We outlined a tamper-proof digital procurement architecture modeled on modern enterprise supply chains, requiring all state contracts, vendor bids, and delivery timestamps to be recorded on a public, open-access ledger, eliminating the forty percent administrative leakage that currently finances corrupt political cartels.
3. **The Emancipation of Female Mobility and Human Capital:** We proved that investing in clean, segregated, and comprehensive public mass transit networks, combined with the abolition of archaic residential curfews for adult scholars, represents the single most cost-effective macroeconomic growth policy in the developing world.

Through Quick Services and Workx, Yousaf demonstrated that these models were not academic fantasies; they were commercially viable, operational systems capable of delivering high-velocity results in real-world environments.

By publishing our findings under an immutable international DOI, we ensured that this empirical roadmap would remain permanently available to the next generation of civil servants, entrepreneurs, and policy reformers who will rebuild the institutions of our nation.
""",

    "17_chapter_17.md": """
### The Final Benediction: The Sovereign Walk on Bosan Road

As I conclude this volume, standing on the elevated platform of the BZU Metrobus station in the cool February morning of 2026, watching the sunlight break through the winter mist over northern Multan, a profound sense of gratitude and peace settles over my spirit.

I think back to that terrified girl who sat in Seminar Room 4 four years ago, whose chin dipped in synchronized submission because she believed that nodding was the only way to survive.

If I could reach back through the fabric of time, I would walk down the aisle of that crowded room, I would pull her trembling hand away from her notebook, and I would whisper in her ear:

*Do not be afraid, Anam.
The water will make your hair fall out, but you will learn chemistry.
The warden will lock the green gates, but you will master the law.
The heat will burn your skin, but the stars on the roof will give you wings.
Your body will collapse in the emergency ward, but your soul will be reborn in the fire.
And in 2026, you will walk this boulevard as a sovereign, published author who will never bow her head to any man on earth again.*

To every young woman who has ever felt the ache in her cervical spine:
The gates are open.
The road is yours.
Raise your chin, and walk.
"""
}

def main():
    for fname, text in final_expansions.items():
        enrich_chapter(fname, text)

if __name__ == "__main__":
    main()
