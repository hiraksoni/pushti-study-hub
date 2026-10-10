# -*- coding: utf-8 -*-
"""
Authoritative Generator for Silver Bells Public School Mid-Term Science Exam 2026-27
Produces:
1. chapters/science/test_silver_bells_midterm_science.html
2. KB Files/science/school_exam/midterm_2026_silver_bells/sci_school_midterm_2026_silver_bells.json
3. KB Files/science/school_exam/midterm_2026_silver_bells/sci_school_midterm_2026_silver_bells.md
4. knowledge_base/science/school_exam/midterm_2026_silver_bells/sci_school_midterm_2026_silver_bells.json
5. knowledge_base/science/school_exam/midterm_2026_silver_bells/sci_school_midterm_2026_silver_bells.md
"""

import os
import json

base_dir = r"d:\Users\expor\Downloads\Codes"
kb_dir_1 = os.path.join(base_dir, "KB Files", "science", "school_exam", "midterm_2026_silver_bells")
kb_dir_2 = os.path.join(base_dir, "knowledge_base", "science", "school_exam", "midterm_2026_silver_bells")
html_path = os.path.join(base_dir, "chapters", "science", "test_silver_bells_midterm_science.html")

os.makedirs(kb_dir_1, exist_ok=True)
os.makedirs(kb_dir_2, exist_ok=True)
os.makedirs(os.path.dirname(html_path), exist_ok=True)

# -------------------------------------------------------------
# 1. QUESTION DATA DICTIONARY
# -------------------------------------------------------------
questions_data = [
    # SECTION A: BIOLOGY (30 MARKS)
    # Part I: Q1 - Q9 (1M each)
    {
        "q_num": 1,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Which endocrine gland secretes hormones that regulate and stimulate other endocrine glands, earning it the title of the \"master gland\"?",
        "options": {
            "a": "Thyroid gland",
            "b": "Pituitary gland",
            "c": "Adrenal gland",
            "d": "Pancreas"
        },
        "correct": "b",
        "explanation": "The pituitary gland, located at the base of the brain, secretes stimulating and trophic hormones (e.g., TSH, ACTH, FSH, LH, and growth hormone) that regulate the hormonal output of other endocrine glands such as the thyroid, adrenal cortex, and gonads. Therefore, it is termed the 'master gland'.",
        "concept": "Endocrine System & Hormonal Control",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    {
        "q_num": 2,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "In human digestion, the finger-like projections called villi that maximize nutrient absorption are located in the inner lining of the:",
        "options": {
            "a": "Stomach",
            "b": "Large intestine",
            "c": "Small intestine",
            "d": "Esophagus"
        },
        "correct": "c",
        "explanation": "Villi are microscopic, millions of finger-like projections found exclusively on the inner mucosa of the small intestine (jejunum and ileum). They drastically increase the effective surface area for the absorption of digested nutrients into blood capillaries and lymphatic lacteals.",
        "concept": "Digestive Anatomy & Nutrient Absorption",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 3,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "The protruding growth of the voice box visible in adolescent boys during puberty is termed:",
        "options": {
            "a": "Thyroid cartilage",
            "b": "Larynx node",
            "c": "Adam's apple",
            "d": "Epiglottis"
        },
        "correct": "c",
        "explanation": "Under the stimulation of testosterone during male puberty, the larynx (voice box) expands significantly, causing the prominent thyroid cartilage protrusion at the anterior of the throat known as the Adam's apple, resulting in a deeper male voice.",
        "concept": "Secondary Sexual Characteristics & Voice Change",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    {
        "q_num": 4,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "The oxygen-carrying red pigment present inside red blood cells (RBCs) is:",
        "options": {
            "a": "Hemoglobin",
            "b": "Chlorophyll",
            "c": "Plasma",
            "d": "Platelet factor"
        },
        "correct": "a",
        "explanation": "Hemoglobin is an iron-containing respiratory protein present in red blood cells (erythrocytes). It binds reversibly with inhaled oxygen in the lungs to form oxyhemoglobin, transporting oxygen throughout bodily tissues.",
        "concept": "Circulatory & Respiratory Pigments",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 5,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "During intense physical exercise, cramps develop in human leg muscles primarily due to the accumulation of:",
        "options": {
            "a": "Carbon dioxide",
            "b": "Alcohol",
            "c": "Lactic acid",
            "d": "Hydrochloric acid"
        },
        "correct": "c",
        "explanation": "During strenuous exercise, muscle cells consume oxygen faster than the blood can deliver it. Under these anaerobic conditions, pyruvate is converted into lactic acid (Glucose -> Lactic acid + Energy). The local accumulation of lactic acid causes muscle fatigue and painful cramps.",
        "concept": "Anaerobic Respiration in Skeletal Muscles",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 6,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Bile juice plays a vital role in digestion by breaking down large fat droplets into smaller globules. It is produced by the ________ and stored in the ________.",
        "options": {
            "a": "Pancreas; Stomach",
            "b": "Liver; Gallbladder",
            "c": "Gallbladder; Liver",
            "d": "Liver; Pancreas"
        },
        "correct": "b",
        "explanation": "Bile juice is synthesized and secreted by the liver (the largest gland in the body) and stored and concentrated in the sac-like gallbladder until signaled to discharge into the duodenum for fat emulsification.",
        "concept": "Liver & Gallbladder Digestive Physiology",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 7,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Why do adolescent teenagers often develop acne and pimples on their face?",
        "options": {
            "a": "Excessive secretion of thyroxine",
            "b": "Increased activity of sweat and sebaceous (oil) glands",
            "c": "Deficiency of dietary proteins",
            "d": "Underproduction of insulin"
        },
        "correct": "b",
        "explanation": "During puberty, surges in sex hormones stimulate the sweat glands and sebaceous (oil) glands in the skin, increasing oil (sebum) production. Blocked pores and bacterial colonization trigger inflammatory acne and facial pimples.",
        "concept": "Pubertal Glandular Hyperactivity",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    {
        "q_num": 8,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "ar",
        "marks": 1,
        "question": "Assertion (A): Oesophagus transfers food from the mouth to the stomach.<br>Reason (R): Windpipe assists the Oesophagus to transfer food from mouth to the stomach.",
        "options": {
            "a": "Both A and R are true, and R is the correct explanation of A.",
            "b": "Both A and R are true, but R is not the correct explanation of A.",
            "c": "A is true, but R is false.",
            "d": "A is false, but R is true."
        },
        "correct": "c",
        "explanation": "Assertion (A) is TRUE: The oesophagus conveys food downwards through wave-like muscular contractions known as peristalsis. Reason (R) is FALSE: The windpipe (trachea) conducts air into the respiratory system and does not aid food transport. In fact, the flap-like epiglottis covers the trachea during swallowing to stop food entry.",
        "concept": "Alimentary Peristalsis vs Respiratory Tract",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 9,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "ar",
        "marks": 1,
        "question": "Assertion (A): Adolescents require a higher proportion of iron-rich foods like greens and jaggery in their diet.<br>Reason (R): Iron is indispensable for hemoglobin synthesis, supporting rapid growth and increased blood volume.",
        "options": {
            "a": "Both A and R are true, and R is the correct explanation of A.",
            "b": "Both A and R are true, but R is not the correct explanation of A.",
            "c": "A is true, but R is false.",
            "d": "A is false, but R is true."
        },
        "correct": "a",
        "explanation": "Both Assertion (A) and Reason (R) are TRUE, and Reason (R) is the exact scientific explanation. The adolescent growth spurt involves rapid muscle and skeletal expansion, leading to increased total blood volume. In adolescent girls, menstruation begins, causing periodic blood loss. Dietary iron is essential to synthesize hemoglobin; inadequate iron intake causes anemia.",
        "concept": "Adolescent Nutrition & Hemoglobin Synthesis",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    # Part II: Q10 - Q12 (2M each)
    {
        "q_num": 10,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part II: Very Short Answer Questions",
        "type": "vsa",
        "marks": 2,
        "question": "State any two secondary sexual characteristics that develop in human males and two that develop in human females during puberty. [2 Marks]",
        "model_answer": """<strong>In Human Males (Any two):</strong>
<ol>
  <li><strong>Facial and Body Hair:</strong> Appearance of mustache, beard, and hair in armpits and pubic region.</li>
  <li><strong>Voice Deepening:</strong> Enlargement of the larynx (prominent Adam's apple) causing the voice to crack and deepen.</li>
  <li><strong>Musculoskeletal Growth:</strong> Broadening of shoulders and increased muscular mass development.</li>
</ol>
<strong>In Human Females (Any two):</strong>
<ol>
  <li><strong>Breast Development:</strong> Enlargement of mammary glands (breasts).</li>
  <li><strong>Pelvic Broadening:</strong> Widening of hips and pelvic region to facilitate future childbearing.</li>
  <li><strong>Menarche:</strong> Initiation of the menstrual cycle and development of high-pitched voice.</li>
</ol>""",
        "marking_scheme": "1 Mark for two valid male secondary sexual characteristics (0.5M each) + 1 Mark for two valid female secondary sexual characteristics (0.5M each). Total = 2 Marks.",
        "concept": "Pubertal Secondary Sexual Characteristics",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    {
        "q_num": 11,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part II: Very Short Answer Questions",
        "type": "vsa",
        "marks": 2,
        "question": "Differentiate between arteries and veins based on: (a) Direction of blood flow relative to the heart, and (b) Presence of internal valves. [2 Marks]<br><em>(Teacher Annotated Internal Choice: OR Explain functions of the small intestine)</em>",
        "model_answer": """<strong>Comparison Table: Arteries vs. Veins</strong>
<table class="exam-table">
  <thead>
    <tr>
      <th>Distinguishing Feature</th>
      <th>Arteries</th>
      <th>Veins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>(a) Direction of Blood Flow</strong></td>
      <td>Carry blood <strong>away from the heart</strong> to various body tissues and organs (Exception: Pulmonary artery carries deoxygenated blood to lungs).</td>
      <td>Carry blood <strong>towards the heart</strong> collected from various body organs (Exception: Pulmonary vein carries oxygenated blood from lungs).</td>
    </tr>
    <tr>
      <td><strong>(b) Presence of Internal Valves</strong></td>
      <td>Internal semilunar valves are <strong>absent</strong> (blood flows at high, pulsing pressure from heart ventricular contractions).</td>
      <td>Internal semilunar valves are <strong>present</strong> along their length to prevent backflow of blood flowing under low pressure.</td>
    </tr>
  </tbody>
</table>

<div class="or-box">
  <div class="or-badge">OR OPTION: FUNCTIONS OF SMALL INTESTINE</div>
  <ol>
    <li><strong>Final & Complete Chemical Digestion:</strong> Enzymes from intestinal juice (maltase, sucrase, peptidase) and pancreatic juice (amylase, trypsin, lipase) break down complex carbohydrates into glucose, proteins into amino acids, and fats into fatty acids and glycerol.</li>
    <li><strong>Maximum Nutrient Absorption:</strong> Millions of microscopic, vascularized villi and microvilli absorb digested nutrients directly into blood capillaries and lymphatic lacteals.</li>
  </ol>
</div>""",
        "marking_scheme": "1 Mark for differentiating direction of blood flow (0.5M arteries + 0.5M veins) + 1 Mark for differentiating presence of valves (0.5M arteries + 0.5M veins). OR: 1 Mark for complete chemical digestion + 1 Mark for villi nutrient absorption. Total = 2 Marks.",
        "concept": "Circulatory Vessels / Small Intestinal Digestion",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 12,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part II: Very Short Answer Questions",
        "type": "vsa",
        "marks": 2,
        "question": "Why does the breathing rate of a person increase sharply after running a 100-meter sprint race? [2 Marks]",
        "model_answer": """<ol>
  <li><strong>Surge in Muscle Energy Demand:</strong> Running a rapid 100-meter sprint demands a tremendous amount of instantaneous energy (ATP) in leg skeletal muscles.</li>
  <li><strong>Anaerobic Respiration & Oxygen Debt:</strong> Since the circulating blood cannot supply oxygen fast enough to meet this intense aerobic demand, muscle cells respire anaerobically, accumulating <em>lactic acid</em> and incurring an <strong>oxygen debt</strong>.</li>
  <li><strong>Clearing Oxygen Debt:</strong> After stopping, the breathing rate remains elevated to inhale excess oxygen rapidly. This surplus oxygen oxidizes accumulated lactic acid back into carbon dioxide and water, relieving muscle fatigue and restoring homeostasis.</li>
</ol>""",
        "marking_scheme": "1 Mark for identifying rapid muscular ATP demand leading to anaerobic respiration and lactic acid/oxygen debt accumulation + 1 Mark for explaining that rapid breathing supplies extra oxygen to break down lactic acid. Total = 2 Marks.",
        "concept": "Cellular Respiration, Anaerobic Metabolism & Oxygen Debt",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    # Part III: Q13 - Q14 (3M each)
    {
        "q_num": 13,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "Describe the mechanism of inhalation and exhalation in humans with specific reference to the movement of the ribs and diaphragm. [3 Marks]",
        "model_answer": """<strong>1. Inhalation (Breathing In):</strong>
<ul>
  <li><strong>Ribs Movement:</strong> The external intercostal muscles contract, causing the ribs to move <strong>upwards and outwards</strong>.</li>
  <li><strong>Diaphragm Movement:</strong> The dome-shaped muscular diaphragm contracts and <strong>flattens downwards</strong>.</li>
  <li><strong>Thoracic Volume & Air Pressure:</strong> The combined movements expand thoracic cavity volume. This expansion lowers pressure inside the lungs below atmospheric pressure, causing atmospheric oxygen-rich air to rush into the alveoli.</li>
</ul>

<strong>2. Exhalation (Breathing Out):</strong>
<ul>
  <li><strong>Ribs Movement:</strong> The intercostal muscles relax, allowing the ribs to move <strong>downwards and inwards</strong>.</li>
  <li><strong>Diaphragm Movement:</strong> The diaphragm relaxes and curves upwards, returning to its original <strong>dome-like resting shape</strong>.</li>
  <li><strong>Thoracic Volume & Air Pressure:</strong> The thoracic cavity volume shrinks, increasing internal pulmonary pressure above atmospheric levels, forcing carbon dioxide-laden air out of the lungs.</li>
</ul>""",
        "marking_scheme": "1.5 Marks for inhalation (0.5M ribs upwards/outwards, 0.5M diaphragm flattens, 0.5M volume expands and air rushes in) + 1.5 Marks for exhalation (0.5M ribs downwards/inwards, 0.5M diaphragm relaxes to dome shape, 0.5M volume decreases and air expelled). Total = 3 Marks.",
        "concept": "Pulmonary Ventilation Dynamics",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    {
        "q_num": 14,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "(a) What is emulsification of fats, and which digestive secretion aids this process? (1.5 Marks)<br>(b) What physiological role does the large intestine perform on undigested food waste? (1.5 Marks) [3 Marks]",
        "model_answer": """<strong>(a) Emulsification of Fats:</strong>
<ul>
  <li><strong>Definition:</strong> Emulsification is the physical breakdown of large, insoluble dietary fat globules into microscopic droplets. This substantially increases the surface area exposed to water-soluble lipases for efficient enzymatic breakdown into fatty acids and glycerol.</li>
  <li><strong>Digestive Secretion:</strong> <strong>Bile juice</strong> (specifically bile salts like sodium glycocholate and sodium taurocholate), synthesized by the liver and stored in the gallbladder, performs fat emulsification. (Bile contains no enzymes but creates an alkaline pH essential for lipase action).</li>
</ul>

<strong>(b) Physiological Role of the Large Intestine:</strong>
<ul>
  <li><strong>Water and Mineral Absorption:</strong> The large intestine reabsorbs the majority of unabsorbed water, salts, and electrolytes from the liquid chyme entering from the ileum, preventing dehydration.</li>
  <li><strong>Fecal Compaction & Elimination:</strong> It compacts the remaining non-digestible fibrous residue into semi-solid feces, which passes into the rectum for temporary storage until egestion through the anus.</li>
</ul>""",
        "marking_scheme": "(a) 1 Mark for defining fat emulsification + 0.5 Mark for naming bile juice. (b) 1 Mark for water and mineral salt reabsorption + 0.5 Mark for compaction of undigested waste/egestion. Total = 3 Marks.",
        "concept": "Lipid Digestion & Large Intestinal Absorption",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },
    # Part IV: Q15 (4M Case Study)
    {
        "q_num": 15,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part IV: Case Study Based Question",
        "type": "case_study",
        "marks": 4,
        "case_text": """<strong>CASE STUDY: ADOLESCENT PHYSIOLOGY AND HORMONAL DYNAMICS</strong><br>
During an interactive classroom seminar on adolescent health, the school counselor discussed how the body undergoes profound emotional, psychological, and physiological transformations between ages 11 and 19. Hormones like testosterone and estrogen trigger sudden growth spurts, bodily changes, and emotional mood swings. The counselor emphasized the importance of balanced personal nutrition, regular physical activity, and stress management, warning students against succumbing to peer pressure and substance abuse.""",
        "question": "(a) Define the term \"hormone.\" [1 Mark]<br>(b) Name the male and female sex hormones responsible for secondary sexual characteristics. [1 Mark]<br>(c) Why are adolescents especially vulnerable to nutritional deficiencies if they depend heavily on fast food (junk food)? Suggest two nutritional corrections. [2 Marks]",
        "model_answer": """<strong>(a) Definition of Hormone:</strong><br>
A <strong>hormone</strong> is a chemical messenger synthesized in minute trace quantities by ductless endocrine glands and released directly into the bloodstream to reach distant target tissues or organs to coordinate physiological growth, development, and metabolism.

<br><br><strong>(b) Male and Female Sex Hormones:</strong>
<ul>
  <li><strong>Male Sex Hormone:</strong> <em>Testosterone</em> (secreted by the testes).</li>
  <li><strong>Female Sex Hormone:</strong> <em>Estrogen</em> (and progesterone, secreted by the ovaries).</li>
</ul>

<strong>(c) Nutritional Vulnerability & Corrections:</strong>
<ul>
  <li><strong>Why Vulnerable:</strong> Adolescence involves an intense growth spurt, bone elongation, and expansion of blood volume. Fast foods (junk foods) are calorie-dense but nutrient-poor (high in refined sugars, sodium, and saturated fats, while devoid of proteins, dietary iron, calcium, and vitamins). Relying on junk food causes iron-deficiency anemia, brittle bones, lethargy, and stunted growth.</li>
  <li><strong>Two Nutritional Corrections:</strong>
    <ol>
      <li><strong>Iron and Calcium Fortification:</strong> Consume iron-rich foods (green leafy vegetables, jaggery, beetroot) to support hemoglobin synthesis, and calcium sources (milk, curd) for skeletal growth.</li>
      <li><strong>Protein & Fresh Produce:</strong> Incorporate high-protein sources (pulses, sprouts, paneer, eggs) along with fresh fruits and salads for optimal tissue repair and immunity.</li>
    </ol>
  </li>
</ul>""",
        "marking_scheme": "(a) 1 Mark for precise definition of hormone as a chemical messenger from ductless glands. (b) 0.5 Mark for testosterone + 0.5 Mark for estrogen. (c) 1 Mark for explaining why adolescents suffer deficiencies from junk food + 1 Mark for two valid nutritional corrections (0.5M each). Total = 4 Marks.",
        "concept": "Endocrine Physiology, Sex Steroids & Adolescent Nutrition",
        "ncert_ref": "Chapter 2: Adolescence"
    },
    # Part V: Q16 (5M LA with OR)
    {
        "q_num": 16,
        "section": "bio",
        "section_name": "Section A: Biology",
        "part": "Part V: Long Answer Question",
        "type": "la",
        "marks": 5,
        "question": "(a) Trace the complete path of food through the human alimentary canal from the mouth to the anus. (2 Marks)<br>(b) Explain the chemical digestion of carbohydrates, proteins, and fats inside the small intestine, mentioning the enzymes involved. (3 Marks)<br><div style='text-align:center; font-weight:700; margin:8px 0;'>OR</div>Mention 5-6 functions of the stomach. [5 Marks]",
        "model_answer": """<strong>(a) Complete Path of Food in Human Alimentary Canal:</strong><br>
<div class="flowchart-box">
  Mouth / Buccal Cavity &rarr; Pharynx &rarr; Oesophagus (Food Pipe) &rarr; Stomach &rarr; Small Intestine (Duodenum &rarr; Jejunum &rarr; Ileum) &rarr; Large Intestine (Caecum &rarr; Colon &rarr; Rectum) &rarr; Anus
</div>

<br><strong>(b) Chemical Digestion in the Small Intestine:</strong><br>
The small intestine is the site of complete chemical digestion where intestinal juice, alkaline pancreatic juice, and bile juice act together:
<ol>
  <li><strong>Carbohydrates:</strong> Pancreatic amylase hydrolyzes remaining starches into maltose. Intestinal enzymes (maltase, sucrase, lactase) break down disaccharides into simple absorbable <strong>glucose</strong>.<br>
  <em>Starch / Complex Sugars &rarr; Glucose</em></li>
  <li><strong>Proteins:</strong> Pancreatic trypsin and chymotrypsin (activated in alkaline medium) along with intestinal peptidases cleave peptones and polypeptides into individual <strong>amino acids</strong>.<br>
  <em>Proteins & Peptones &rarr; Amino Acids</em></li>
  <li><strong>Fats (Lipids):</strong> After bile salts emulsify fat droplets, pancreatic and intestinal <strong>lipases</strong> digest emulsified fats into absorbable <strong>fatty acids and glycerol</strong>.<br>
  <em>Emulsified Fats &rarr; Fatty Acids + Glycerol</em></li>
</ol>

<div class="or-box">
  <div class="or-badge">OR OPTION: 5-6 FUNCTIONS OF THE HUMAN STOMACH</div>
  <ol>
    <li><strong>Mechanical Food Reservoir:</strong> Temporarily stores ingested food for 3 to 5 hours, regulating slow passage into the duodenum.</li>
    <li><strong>Mechanical Churning:</strong> Coordinated rhythmic peristaltic contractions of its muscular walls churn, liquefy, and blend food with gastric secretions into an acidic semi-fluid called <strong>chyme</strong>.</li>
    <li><strong>Pathogen Destruction via HCl:</strong> Gastric parietal cells secrete Hydrochloric Acid (HCl, pH ~ 1.5 - 2.5), which kills food-borne bacteria and microorganisms.</li>
    <li><strong>Enzyme Activation:</strong> The acidic environment of HCl activates the inactive pro-enzyme <em>pepsinogen</em> into active <strong>pepsin</strong>.</li>
    <li><strong>Protein Digestion:</strong> Active pepsin initiates the chemical cleavage of complex dietary proteins into soluble peptones and proteoses.</li>
    <li><strong>Gastric Mucosal Protection:</strong> Mucus neck cells produce a continuous coating of bicarbonate-rich alkaline mucus that guards the stomach wall against corrosive self-digestion by HCl and pepsin.</li>
    <li><strong>Intrinsic Factor Secretion:</strong> Secretes Castle's intrinsic factor, essential for the subsequent absorption of Vitamin B12 in the terminal ileum.</li>
  </ol>
</div>""",
        "marking_scheme": "(a) 2 Marks for correct chronological sequence of the alimentary canal. (b) 1 Mark each for digestion of carbohydrates, proteins, and fats with correct enzymes (3 Marks). OR: 1 Mark each for any 5 clearly articulated functions of the stomach (5 Marks). Total = 5 Marks.",
        "concept": "Gastrointestinal Physiology, Enzymatic Digestion & Gastric Functions",
        "ncert_ref": "Chapter 3: Life Processes in Animals"
    },

    # SECTION B: CHEMISTRY (25 MARKS)
    # Part I: Q17 - Q24 (1M each)
    {
        "q_num": 17,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Which of the following organic acids is naturally present in curd (sour milk)?",
        "options": {
            "a": "Citric acid",
            "b": "Lactic acid",
            "c": "Tartaric acid",
            "d": "Formic acid"
        },
        "correct": "b",
        "explanation": "Lactic acid is produced during milk fermentation when <em>Lactobacillus</em> bacteria convert lactose sugar into lactic acid, causing curdling of milk proteins and imparting a sour taste.",
        "concept": "Naturally Occurring Organic Acids",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    {
        "q_num": 18,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "When phenolphthalein indicator is added to a dilute sodium hydroxide solution, the color turns:",
        "options": {
            "a": "Blue",
            "b": "Pink",
            "c": "Colorless",
            "d": "Bright yellow"
        },
        "correct": "b",
        "explanation": "Phenolphthalein is a synthetic indicator that remains completely colorless in acidic or neutral solutions, but turns vibrant deep pink in basic (alkaline) solutions such as sodium hydroxide (NaOH).",
        "concept": "Acid-Base Synthetic Indicators",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    {
        "q_num": 19,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Which metal exists as a liquid at standard room temperature?",
        "options": {
            "a": "Sodium",
            "b": "Mercury",
            "c": "Bromine",
            "d": "Magnesium"
        },
        "correct": "b",
        "explanation": "Mercury (Hg) is the only metallic element that exists in liquid form under ambient room temperature and pressure (melting point -38.83 °C). (Note: Bromine is also liquid at room temp, but it is a non-metal).",
        "concept": "Physical States of Metals & Exceptions",
        "ncert_ref": "Chapter 2: Metals and Non-Metals"
    },
    {
        "q_num": 20,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "The mechanical property that allows metals to be beaten into thin sheets without shattering is known as:",
        "options": {
            "a": "Ductility",
            "b": "Malleability",
            "c": "Sonority",
            "d": "Tensile strength"
        },
        "correct": "b",
        "explanation": "Malleability is the physical property of metals that allows them to deform under compressive stress, enabling them to be hammered or rolled into ultra-thin sheets (such as aluminium and gold foil) without fracturing.",
        "concept": "Mechanical Properties of Metals",
        "ncert_ref": "Chapter 2: Metals and Non-Metals"
    },
    {
        "q_num": 21,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "An ant sting injects formic acid under the skin. The burning irritation can be neutralised and relieved by rubbing:",
        "options": {
            "a": "Vinegar",
            "b": "Lemon juice",
            "c": "Moist baking soda (sodium hydrogen carbonate)",
            "d": "Dilute hydrochloric acid"
        },
        "correct": "c",
        "explanation": "An ant sting injects formic acid (methanoic acid). Applying a mild basic substance like moist baking soda (sodium hydrogen carbonate, NaHCO3) or calamine lotion (zinc carbonate) neutralizes the acid and soothes the inflammation.",
        "concept": "Practical Neutralization in Daily Life",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    {
        "q_num": 22,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "mcq",
        "marks": 1,
        "question": "Which of the following non-metals is an exceptional conductor of electricity?",
        "options": {
            "a": "Sulphur",
            "b": "Graphite",
            "c": "Phosphorus",
            "d": "Iodine"
        },
        "correct": "b",
        "explanation": "Graphite is an allotrope of carbon with a layered hexagonal lattice. Each carbon atom is bonded to three others, leaving one delocalized valence electron free to move within the sheets, enabling graphite to conduct electricity.",
        "concept": "Conductivity Exceptions in Non-Metals",
        "ncert_ref": "Chapter 2: Metals and Non-Metals"
    },
    {
        "q_num": 23,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "ar",
        "marks": 1,
        "question": "Assertion (A): Copper metal cannot displace Zinc from an aqueous Zinc sulphate solution.<br>Reason (R): Copper is less reactive than zinc according to the metal reactivity series.",
        "options": {
            "a": "Both A and R are true, and R is the correct explanation of A.",
            "b": "Both A and R are true, but R is not the correct explanation of A.",
            "c": "A is true, but R is false.",
            "d": "A is false, but R is true."
        },
        "correct": "a",
        "explanation": "Both Assertion (A) and Reason (R) are TRUE, and R is the correct scientific explanation. In the electrochemical reactivity series: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu. Because zinc is higher than copper in reactivity, copper cannot reduce or displace zinc ions from zinc sulphate solution.",
        "concept": "Metal Reactivity Series & Displacement Reactions",
        "ncert_ref": "Chapter 2: Metals and Non-Metals"
    },
    {
        "q_num": 24,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part I: MCQs & Assertion-Reason",
        "type": "ar",
        "marks": 1,
        "question": "Assertion (A): Distilled water turns red litmus paper blue.<br>Reason (R): Pure distilled water is neutral, having neither acidic nor basic characteristics.",
        "options": {
            "a": "Both A and R are true, and R is the correct explanation of A.",
            "b": "Both A and R are true, but R is not the correct explanation of A.",
            "c": "A is true, but R is false.",
            "d": "A is false, but R is true."
        },
        "correct": "d",
        "explanation": "Assertion (A) is FALSE: Pure distilled water is chemically neutral (pH = 7) and does not alter the color of either red or blue litmus paper. Reason (R) is TRUE: Distilled water contains equal concentrations of H+ and OH- ions, showing neither acidic nor basic properties. Thus, A is false but R is true.",
        "concept": "Neutral Substances & Litmus Indicator Behavior",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    # Part II: Q25 (2M VSA)
    {
        "q_num": 25,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part II: Very Short Answer Question",
        "type": "vsa",
        "marks": 2,
        "question": "State what visible change occurs when blue litmus paper and red litmus paper are dipped separately into: (a) Lime water, (b) Amla juice. [2 Marks]",
        "model_answer": """<strong>(a) Lime Water [Calcium hydroxide, Ca(OH)<sub>2</sub> - Basic in Nature]:</strong>
<ul>
  <li><strong>Blue Litmus Paper:</strong> Remains <strong>Blue</strong> (no color change).</li>
  <li><strong>Red Litmus Paper:</strong> Turns <strong>Blue</strong> (confirms presence of a base).</li>
</ul>

<strong>(b) Amla Juice [Rich in Ascorbic Acid / Citric Acid - Acidic in Nature]:</strong>
<ul>
  <li><strong>Blue Litmus Paper:</strong> Turns <strong>Red</strong> (confirms presence of an acid).</li>
  <li><strong>Red Litmus Paper:</strong> Remains <strong>Red</strong> (no color change).</li>
</ul>""",
        "marking_scheme": "1 Mark for lime water (0.5M blue litmus remains blue + 0.5M red litmus turns blue) + 1 Mark for amla juice (0.5M blue litmus turns red + 0.5M red litmus remains red). Total = 2 Marks.",
        "concept": "Litmus Color Transitions in Acids and Bases",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    # Part III: Q26 - Q27 (3M each SA)
    {
        "q_num": 26,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "What is a neutralization reaction? Write the word equation for the reaction between hydrochloric acid and sodium hydroxide, and name the salt and secondary product formed. [3 Marks]<br><div style='text-align:center; font-weight:700; margin:8px 0;'>OR</div>Identify the scientific name and give their uses: 1. Calamine 2. Blue vitriol 3. Vinegar. [3 Marks]",
        "model_answer": """<strong>1. Neutralization Reaction:</strong><br>
A <strong>neutralization reaction</strong> is a chemical reaction in which an acid and a base react together quantitatively in equivalent proportions to form a salt and water, accompanied by the evolution of heat.<br>
<em>General Equation: Acid + Base &rarr; Salt + Water + Heat</em>

<br><br><strong>2. Word Equation:</strong><br>
<div class="formula-box">
  Hydrochloric acid + Sodium hydroxide &rarr; Sodium chloride + Water (+ Heat)<br>
  <em>(HCl + NaOH &rarr; NaCl + H<sub>2</sub>O)</em>
</div>

<br><strong>3. Products Identified:</strong>
<ul>
  <li><strong>Salt Formed:</strong> Sodium chloride (NaCl, common edible table salt).</li>
  <li><strong>Secondary Product:</strong> Water (H<sub>2</sub>O).</li>
</ul>

<div class="or-box">
  <div class="or-badge">OR OPTION: SCIENTIFIC NAMES & USES</div>
  <ol>
    <li><strong>Calamine:</strong>
      <ul>
        <li><em>Scientific Chemical Name:</em> <strong>Zinc carbonate</strong> (ZnCO<sub>3</sub>).</li>
        <li><em>Primary Use:</em> Applied as a soothing topical calamine lotion to neutralize acidic ant stings and relieve insect bite itchiness and skin rashes.</li>
      </ul>
    </li>
    <li><strong>Blue Vitriol:</strong>
      <ul>
        <li><em>Scientific Chemical Name:</em> <strong>Copper(II) sulphate pentahydrate</strong> (CuSO<sub>4</sub>&bull;5H<sub>2</sub>O).</li>
        <li><em>Primary Use:</em> Formulated into Bordeaux mixture as an agricultural fungicide/algaecide, and used in copper electroplating and crystal growth demonstrations.</li>
      </ul>
    </li>
    <li><strong>Vinegar:</strong>
      <ul>
        <li><em>Scientific Chemical Name:</em> <strong>Dilute Acetic acid / Ethanoic acid</strong> (CH<sub>3</sub>COOH, 5-8% aqueous solution).</li>
        <li><em>Primary Use:</em> Acts as a natural food preservative in pickles and condiments by inhibiting bacterial growth; also used as a household cleaning and descaling agent.</li>
      </ul>
    </li>
  </ol>
</div>""",
        "marking_scheme": "1 Mark for clear scientific definition of neutralization + 1 Mark for accurate word equation + 1 Mark for correctly naming the salt (sodium chloride) and secondary product (water). OR: 1 Mark each for compound (0.5M scientific name + 0.5M practical use x 3 = 3 Marks). Total = 3 Marks.",
        "concept": "Acid-Base Neutralization & Common Chemical Formulations",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    {
        "q_num": 27,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "Provide scientific justifications for each observation:<br>(a) Sodium and potassium metals are preserved immersed under kerosene oil. (1 Mark)<br>(b) High-voltage electric transmission cables use copper core with PVC cladding. (1 Mark)<br>(c) School acoustic bells are manufactured from bronze/brass instead of seasoned wood. (1 Mark) [3 Marks]",
        "model_answer": """<strong>(a) Preservation of Sodium and Potassium under Kerosene Oil:</strong><br>
Sodium (Na) and potassium (K) are highly electropositive alkali metals situated at the very top of the reactivity series. They react vigorously and exothermically with atmospheric oxygen and moisture even at ambient room temperature, liberating flammable hydrogen gas that catches fire spontaneously. Immersing them under chemically inert kerosene oil cuts off all contact with atmospheric oxygen and moisture.

<br><br><strong>(b) Copper Core with PVC Cladding in Electric Cables:</strong><br>
Copper has extremely low electrical resistivity and high conductivity, allowing high-voltage currents to transmit with minimal Joule resistive heating loss. Polyvinyl chloride (PVC) is an outstanding, flexible electrical insulator that forms a secure barrier, preventing electric current leakage, accidental short-circuits, and protecting people from electric shocks.

<br><br><strong>(c) School Bells Made of Bronze/Brass instead of Wood:</strong><br>
Metals and metal alloys like bronze (copper-tin) and brass (copper-zinc) are <strong>sonorous</strong>. When struck, their metallic crystal structure resonates with minimal internal damping, producing a clear, loud, sustained ringing acoustic tone that propagates across long distances. Seasoned wood is non-sonorous; it rapidly damps vibrational energy and emits only a dull, muffled thud.""",
        "marking_scheme": "1 Mark for explaining alkali reactivity with air/water and protective barrier of kerosene + 1 Mark for copper high conductivity and PVC insulation safety + 1 Mark for metallic sonority vs non-sonorous damping in wood. Total = 3 Marks.",
        "concept": "Chemical Reactivity & Physical Material Justifications",
        "ncert_ref": "Chapter 2: Metals and Non-Metals"
    },
    # Part IV: Q28 (4M Case Study)
    {
        "q_num": 28,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part IV: Case Study Based Question",
        "type": "case_study",
        "marks": 4,
        "case_text": """<strong>CASE STUDY: SOIL CHEMISTRY & AGRICULTURAL PRODUCTIVITY</strong><br>
Farmers in a village noticed that crop yields had dropped significantly over two consecutive seasons. An agricultural scientist tested soil samples and discovered that prolonged overuse of synthetic chemical fertilizers had rendered the fields excessively acidic. She advised the farmers to treat the soil with slaked lime [calcium hydroxide] or powdered quicklime [calcium oxide] prior to the next sowing season. She added that should the soil ever become excessively alkaline, decaying organic compost must be added instead.""",
        "question": "(a) Why does overly acidic soil hamper healthy root development and crop yield? [1 Mark]<br>(b) Name the chemical treatment prescribed to rectify soil acidity, and classify the reaction type. [1.5 Marks]<br>(c) How does decaying organic compost counteract excess alkalinity in basic soil? [1.5 Marks]",
        "model_answer": """<strong>(a) Impact of Overly Acidic Soil on Roots and Yield:</strong><br>
Overly acidic soil (pH < 5.5) locks up essential macronutrients (phosphorus, calcium, and potassium) into insoluble compounds, making them inaccessible for root absorption. Furthermore, high acidity leaches toxic aluminium and manganese ions into soil water, which stunt root cell elongation, kill beneficial nitrogen-fixing soil bacteria, and cause poor crop yields.

<br><br><strong>(b) Prescribed Chemical Treatment and Reaction Classification:</strong>
<ul>
  <li><strong>Prescribed Chemical Bases:</strong> Treatment with powdered <strong>quicklime</strong> [Calcium oxide, CaO] or <strong>slaked lime</strong> [Calcium hydroxide, Ca(OH)<sub>2</sub>], or chalk [Calcium carbonate, CaCO<sub>3</sub>].</li>
  <li><strong>Reaction Classification:</strong> <strong>Neutralization reaction</strong>. The basic metal oxides/hydroxides react with excess hydrogen ions (acids) in the soil, forming neutral salts and water and elevating soil pH to an optimal neutral range (6.5 to 7.5).</li>
</ul>

<strong>(c) How Organic Compost Counteracts Excess Alkalinity:</strong><br>
Decaying organic matter (compost/humus) is decomposed by soil microbes, releasing natural <strong>organic acids</strong> (such as humic and fulvic acids). These mild acids neutralize excess alkaline bases present in basic soil, reducing the high pH back to a neutral, fertile balance while simultaneously improving soil moisture retention.""",
        "marking_scheme": "(a) 1 Mark for explaining nutrient locking / root toxicity. (b) 1 Mark for identifying quicklime/slaked lime + 0.5 Mark for classifying it as a neutralization reaction. (c) 1 Mark for explaining release of microbial organic acids from compost + 0.5 Mark for neutralizing basic soil. Total = 4 Marks.",
        "concept": "Soil pH Chemistry, Agricultural Neutralization & Organic Compost",
        "ncert_ref": "Chapter 1: Acids, Bases and Neutral Substances"
    },
    # Part V: Q29 (5M LA with OR)
    {
        "q_num": 29,
        "section": "chem",
        "section_name": "Section B: Chemistry",
        "part": "Part V: Long Answer Question",
        "type": "la",
        "marks": 5,
        "question": "(a) Differentiate between metals and non-metals based on physical properties. (3 Marks)<br>(b) Describe an experiment to demonstrate that burning magnesium ribbon produces a basic oxide. Write the word equation involved. (2 Marks)<br><div style='text-align:center; font-weight:700; margin:8px 0;'>OR</div>(a) You are provided with three unlabelled test tubes containing dilute hydrochloric acid, sodium hydroxide solution, and distilled water. Using only turmeric paper indicator, outline the step-by-step procedure to identify each liquid. (3 Marks)<br>(b) How can we prevent rusting? (2 Marks) [5 Marks]",
        "model_answer": """<strong>(a) Differentiation Between Metals and Non-Metals:</strong>
<table class="exam-table">
  <thead>
    <tr>
      <th>Physical Property</th>
      <th>Metals</th>
      <th>Non-Metals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Physical State</strong></td>
      <td>Solids at room temperature (Exception: Mercury is liquid).</td>
      <td>Exist as solids, liquids (Bromine), or gases.</td>
    </tr>
    <tr>
      <td><strong>Malleability & Ductility</strong></td>
      <td>Highly malleable (beaten into foils) and ductile (drawn into wires).</td>
      <td>Brittle when solid; shatter upon hammering; non-ductile.</td>
    </tr>
    <tr>
      <td><strong>Electrical & Thermal Conductivity</strong></td>
      <td>Good conductors of heat and electricity (e.g., Cu, Al, Ag).</td>
      <td>Poor conductors / insulators (Exception: Graphite conducts electricity).</td>
    </tr>
    <tr>
      <td><strong>Lustre & Sonority</strong></td>
      <td>Exhibit metallic lustre (shiny surface) and are sonorous (ring when struck).</td>
      <td>Non-lustrous and dull (Exception: Iodine is shiny); non-sonorous.</td>
    </tr>
  </tbody>
</table>

<br><strong>(b) Magnesium Oxide Basicity Experiment:</strong>
<ol>
  <li><strong>Burning Ribbon:</strong> Clean a strip of magnesium ribbon with sandpaper and ignite it using a burner while holding with tongs. It burns with an intense, dazzling white flame, forming white magnesium oxide ash.</li>
  <li><strong>Dissolving in Water:</strong> Collect the white ash in a test tube, add distilled water, and shake thoroughly to form magnesium hydroxide solution.</li>
  <li><strong>Testing with Litmus:</strong> Dip red and blue litmus papers into the solution. Red litmus turns <strong>blue</strong>, while blue litmus remains unchanged.</li>
  <li><strong>Conclusion:</strong> Turning red litmus blue confirms that magnesium oxide forms a basic solution in water, proving metallic oxides are basic.</li>
</ol>
<div class="formula-box">
  Word Equations:<br>
  Magnesium + Oxygen &rarr; Magnesium oxide<br>
  Magnesium oxide + Water &rarr; Magnesium hydroxide [Basic]
</div>

<div class="or-box">
  <div class="or-badge">OR OPTION: TURMERIC IDENTIFICATION & RUST PREVENTION</div>
  <strong>(a) Step-by-Step Identification Using Only Turmeric Paper:</strong><br>
  <em>Principle: Turmeric indicator remains yellow in neutral and acidic solutions, but turns deep reddish-brown in basic solutions.</em>
  <ol>
    <li><strong>Step 1 (Identify Sodium Hydroxide):</strong> Place a drop from each test tube onto separate strips of yellow turmeric paper. The test tube whose drop turns yellow turmeric paper <strong>reddish-brown</strong> contains the base: <strong>Sodium hydroxide (NaOH)</strong>.</li>
    <li><strong>Step 2 (Distinguish HCl and Distilled Water):</strong> Take the turmeric strip that turned reddish-brown from NaOH. Divide it into two pieces. Add a drop from the second tube to one piece and a drop from the third tube to the other:
      <ul>
        <li>The liquid that <strong>reverses the reddish-brown color back to bright yellow</strong> is the acid: <strong>Dilute Hydrochloric acid (HCl)</strong>, because it neutralizes the base.</li>
        <li>The liquid that <strong>causes no color change</strong> (paper remains reddish-brown) is <strong>Distilled water</strong> (neutral).</li>
      </ul>
    </li>
  </ol>

  <br><strong>(b) Methods to Prevent Rusting (Any 2-3 methods):</strong>
  <ol>
    <li><strong>Barrier Coating (Painting / Oiling / Greasing):</strong> Applying a coat of paint, enamel, or grease prevents iron from contacting atmospheric oxygen and moisture.</li>
    <li><strong>Galvanization:</strong> Coating iron and steel articles with a protective thin layer of molten zinc metal. Even if scratched, zinc preferentially oxidizes, protecting the underlying iron.</li>
    <li><strong>Alloying:</strong> Melting iron with carbon, chromium, and nickel produces stainless steel, which is completely resistant to rust.</li>
  </ol>
</div>""",
        "marking_scheme": "(a) 3 Marks for 3 distinct comparison criteria between metals and non-metals. (b) 1.5 Marks for experiment steps and litmus observation + 0.5 Mark for word equations. OR: (a) 1 Mark for identifying NaOH + 2 Marks for distinguishing HCl and water using the neutralized mixture. (b) 2 Marks for two clear methods of rust prevention (1M each). Total = 5 Marks.",
        "concept": "Metal Properties, Oxide Basicity, Turmeric pH Identification & Rust Prevention",
        "ncert_ref": "Chapter 2: Metals and Non-Metals & Chapter 1: Acids and Bases"
    },

    # SECTION C: PHYSICS (25 MARKS)
    # Part I: Q30 - Q32 (1M each MCQ)
    {
        "q_num": 30,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part I: Multiple Choice Questions",
        "type": "mcq",
        "marks": 1,
        "question": "The heating element of an electrical appliance such as an electric room heater or iron is made of:",
        "options": {
            "a": "Pure copper",
            "b": "Nichrome alloy",
            "c": "Pure silver",
            "d": "Soft lead"
        },
        "correct": "b",
        "explanation": "Nichrome (an alloy of nickel, chromium, and iron) has very high electrical resistance and an exceptionally high melting point (~1400 °C). It does not oxidize (burn) even when glowing red-hot, making it the ideal heating element according to Joule's law (H = I²Rt).",
        "concept": "Heating Effect of Current & Heating Elements",
        "ncert_ref": "Chapter 1: Electricity: Circuits and their Components"
    },
    {
        "q_num": 31,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part I: Multiple Choice Questions",
        "type": "mcq",
        "marks": 1,
        "question": "Heat transfer through fluid mediums (liquids and gases) via actual mass displacement of heated particles is called:",
        "options": {
            "a": "Conduction",
            "b": "Convection",
            "c": "Thermal Radiation",
            "d": "Insulation"
        },
        "correct": "b",
        "explanation": "Convection is the mode of heat transfer in fluids where warmer, less dense fluid expands and rises while cooler, denser fluid descends, establishing circulatory convection currents that transfer thermal energy via bulk particle displacement.",
        "concept": "Modes of Heat Transfer: Convection",
        "ncert_ref": "Chapter 2: Heat Transfer and Temperature"
    },
    {
        "q_num": 32,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part I: Multiple Choice Questions",
        "type": "mcq",
        "marks": 1,
        "question": "If a simple pendulum takes 36 seconds to complete 20 full oscillations, its time period is:",
        "options": {
            "a": "0.55 s",
            "b": "1.8 s",
            "c": "72 s",
            "d": "18.0 s"
        },
        "correct": "b",
        "explanation": "The time period (T) is the time required to execute one complete oscillation: Time Period T = Total Time / Number of Oscillations = 36 s / 20 = 1.8 seconds.",
        "concept": "Simple Pendulum Kinematics & Periodicity",
        "ncert_ref": "Chapter 3: Measurement of Time and Motion"
    },
    # Part II: Q33 - Q34 (2M each VSA)
    {
        "q_num": 33,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part II: Very Short Answer Questions",
        "type": "vsa",
        "marks": 2,
        "question": "Draw the standard electrical circuit diagram symbols for: (a) An electric cell, (b) An open switch (OFF position), (c) An electric bulb, and (d) A battery of two cells. [2 Marks]",
        "model_answer": """<strong>Standard Electrical Schematic Symbols:</strong>
<div class="symbols-grid">
  <div class="sym-card">
    <div class="sym-name">(a) Electric Cell</div>
    <div class="sym-visual">
      <svg width="140" height="60" viewBox="0 0 140 60">
        <line x1="20" y1="30" x2="60" y2="30" stroke="#38BDF8" stroke-width="3"/>
        <line x1="60" y1="12" x2="60" y2="48" stroke="#34D399" stroke-width="4"/>
        <line x1="80" y1="20" x2="80" y2="40" stroke="#EF4444" stroke-width="6"/>
        <line x1="80" y1="30" x2="120" y2="30" stroke="#38BDF8" stroke-width="3"/>
        <text x="56" y="10" fill="#34D399" font-size="11" font-weight="bold">+</text>
        <text x="77" y="15" fill="#EF4444" font-size="11" font-weight="bold">-</text>
      </svg>
    </div>
    <div class="sym-desc">Long thin line = Positive (+); Short thick line = Negative (-)</div>
  </div>

  <div class="sym-card">
    <div class="sym-name">(b) Open Switch (OFF)</div>
    <div class="sym-visual">
      <svg width="140" height="60" viewBox="0 0 140 60">
        <line x1="15" y1="30" x2="45" y2="30" stroke="#38BDF8" stroke-width="3"/>
        <circle cx="48" cy="30" r="4" fill="none" stroke="#F59E0B" stroke-width="2.5"/>
        <line x1="48" y1="30" x2="88" y2="12" stroke="#F59E0B" stroke-width="3"/>
        <circle cx="92" cy="30" r="4" fill="none" stroke="#F59E0B" stroke-width="2.5"/>
        <line x1="95" y1="30" x2="125" y2="30" stroke="#38BDF8" stroke-width="3"/>
      </svg>
    </div>
    <div class="sym-desc">Break / gap in line indicates an open, broken circuit</div>
  </div>

  <div class="sym-card">
    <div class="sym-name">(c) Electric Bulb</div>
    <div class="sym-visual">
      <svg width="140" height="60" viewBox="0 0 140 60">
        <line x1="15" y1="30" x2="50" y2="30" stroke="#38BDF8" stroke-width="3"/>
        <circle cx="70" cy="30" r="18" fill="none" stroke="#C084FC" stroke-width="2.5"/>
        <path d="M 58 30 Q 70 14 70 30 Q 70 14 82 30" fill="none" stroke="#F59E0B" stroke-width="2.5"/>
        <line x1="90" y1="30" x2="125" y2="30" stroke="#38BDF8" stroke-width="3"/>
      </svg>
    </div>
    <div class="sym-desc">Filament loop enclosed within an outer circular envelope</div>
  </div>

  <div class="sym-card">
    <div class="sym-name">(d) Battery of 2 Cells</div>
    <div class="sym-visual">
      <svg width="140" height="60" viewBox="0 0 140 60">
        <line x1="15" y1="30" x2="40" y2="30" stroke="#38BDF8" stroke-width="3"/>
        <!-- Cell 1 -->
        <line x1="40" y1="14" x2="40" y2="46" stroke="#34D399" stroke-width="3"/>
        <line x1="55" y1="20" x2="55" y2="40" stroke="#EF4444" stroke-width="5"/>
        <line x1="55" y1="30" x2="75" y2="30" stroke="#38BDF8" stroke-width="2"/>
        <!-- Cell 2 -->
        <line x1="75" y1="14" x2="75" y2="46" stroke="#34D399" stroke-width="3"/>
        <line x1="90" y1="20" x2="90" y2="40" stroke="#EF4444" stroke-width="5"/>
        <line x1="90" y1="30" x2="125" y2="30" stroke="#38BDF8" stroke-width="3"/>
      </svg>
    </div>
    <div class="sym-desc">Two cells connected in series: positive of one to negative of next</div>
  </div>
</div>""",
        "marking_scheme": "0.5 Mark for each correctly labeled and neat standard circuit symbol (4 x 0.5M = 2 Marks).",
        "concept": "Electrical Circuit Schematics & Standard Components",
        "ncert_ref": "Chapter 1: Electricity: Circuits and their Components"
    },
    {
        "q_num": 34,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part II: Very Short Answer Questions",
        "type": "vsa",
        "marks": 2,
        "question": "Why are frying pans and saucepans often manufactured with copper bases while their handles are wrapped in Bakelite or hard wood? [2 Marks]",
        "model_answer": """<ol>
  <li><strong>Copper Base (Thermal Conduction):</strong> Copper has very high thermal conductivity. A copper base transfers heat from the cooking flame quickly and distributes it evenly across the bottom surface, preventing hot spots and cooking food faster and uniformly.</li>
  <li><strong>Bakelite or Hard Wood Handles (Thermal Insulation):</strong> Bakelite (a thermosetting polymer) and wood are poor thermal conductors (insulators). They prevent heat from conducting from the hot cookware body into the cook's hand, allowing safe handling without accidental burns.</li>
</ol>""",
        "marking_scheme": "1 Mark for copper high thermal conductivity & uniform heat distribution + 1 Mark for Bakelite/wood thermal insulation preventing burns. Total = 2 Marks.",
        "concept": "Thermal Conductivity in Utensil Engineering",
        "ncert_ref": "Chapter 2: Heat Transfer and Temperature"
    },
    # Part III: Q35 - Q37 (3M each SA)
    {
        "q_num": 35,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "(a) What is an electromagnet? Mention two methods to increase its magnetic field strength. (2 Marks)<br>(b) State one everyday practical industrial application of an electromagnet. (1 Mark) [3 Marks]",
        "model_answer": """<strong>(a) Electromagnet & Methods to Increase Strength:</strong>
<ul>
  <li><strong>Definition:</strong> An electromagnet is a temporary magnet consisting of a coil of insulated wire wrapped around a soft iron core that behaves as a magnet only when an electric current flows through the coil.</li>
  <li><strong>Two Methods to Increase Magnetic Field Strength:</strong>
    <ol>
      <li><strong>Increasing Current Magnitude:</strong> Increasing the electric current (I) flowing through the solenoid by adding more cells in the circuit.</li>
      <li><strong>Increasing Number of Turns:</strong> Increasing the total number of turns (N) of the insulated wire coil around the iron core.</li>
      <li><em>(Alternative valid factor: Using high-permeability soft iron rather than steel).</em></li>
    </ol>
  </li>
</ul>

<strong>(b) Practical Industrial Application:</strong>
<ul>
  <li><strong>Heavy Scrap Cranes:</strong> Giant electromagnets mounted on salvage cranes are used to lift, transport, and release tons of heavy iron and steel scrap, railway tracks, and machinery. Turning the electric current on attracts magnetic metals; switching it off drops them cleanly in designated locations.</li>
  <li><em>(Other accepted examples: Electric bells, Maglev trains, MRI scanners, electromagnetic relays).</em></li>
</ul>""",
        "marking_scheme": "(a) 1 Mark for defining electromagnet as temporary current-dependent magnet + 1 Mark for two methods to increase field strength (0.5M each). (b) 1 Mark for industrial application with functional reason. Total = 3 Marks.",
        "concept": "Electromagnetism, Magnetic Field Determinants & Industrial Cranes",
        "ncert_ref": "Chapter 1: Electricity: Circuits and their Components"
    },
    {
        "q_num": 36,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "Differentiate between uniform motion and non-uniform motion with one example each. Draw a neat representative distance-time graph for a body traveling at uniform speed. [3 Marks]",
        "model_answer": """<strong>1. Differentiation Between Uniform and Non-Uniform Motion:</strong>
<table class="exam-table">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Uniform Motion</th>
      <th>Non-Uniform Motion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Definition</strong></td>
      <td>An object covers <strong>equal distances in equal intervals of time</strong> along a straight path, regardless of how small the time intervals are.</td>
      <td>An object covers <strong>unequal distances in equal intervals of time</strong>, meaning its speed changes continuously.</td>
    </tr>
    <tr>
      <td><strong>Speed Character</strong></td>
      <td>Speed remains constant throughout the motion.</td>
      <td>Speed varies (body undergoes acceleration or deceleration).</td>
    </tr>
    <tr>
      <td><strong>Example</strong></td>
      <td>A vehicle running on a deserted straight expressway with cruise control locked at 60 km/h; tip of a clock's second hand.</td>
      <td>A city bus moving through heavy urban traffic, frequently speeding up, braking, and stopping at traffic lights.</td>
    </tr>
  </tbody>
</table>

<br><strong>2. Distance-Time Graph for Uniform Motion:</strong>
<div class="graph-visual-container">
  <svg width="280" height="200" viewBox="0 0 280 200">
    <!-- Axes -->
    <line x1="40" y1="160" x2="250" y2="160" stroke="#94A3B8" stroke-width="2"/>
    <line x1="40" y1="160" x2="40" y2="30" stroke="#94A3B8" stroke-width="2"/>
    <!-- Arrows -->
    <polygon points="250,157 257,160 250,163" fill="#94A3B8"/>
    <polygon points="37,30 40,23 43,30" fill="#94A3B8"/>
    <!-- Slope Line -->
    <line x1="40" y1="160" x2="230" y2="40" stroke="#10B981" stroke-width="3.5"/>
    <!-- Points -->
    <circle cx="40" cy="160" r="4" fill="#34D399"/>
    <circle cx="103" cy="120" r="4" fill="#34D399"/>
    <circle cx="166" cy="80" r="4" fill="#34D399"/>
    <circle cx="230" cy="40" r="4" fill="#34D399"/>
    <!-- Labels -->
    <text x="110" y="185" fill="#94A3B8" font-size="12" font-family="'Space Mono', monospace">Time (t) &rarr;</text>
    <text x="10" y="95" fill="#94A3B8" font-size="12" font-family="'Space Mono', monospace" transform="rotate(-90 10 95)">Distance (s) &rarr;</text>
    <text x="130" y="70" fill="#10B981" font-size="11" font-weight="bold">Straight Line Slope = Constant Speed</text>
    <text x="25" y="172" fill="#94A3B8" font-size="11">O (0,0)</text>
  </svg>
  <div style="font-size:0.85rem; color:var(--text-muted); margin-top:6px;">Representative Distance-Time graph: A straight line passing through origin indicates uniform speed.</div>
</div>""",
        "marking_scheme": "1 Mark for uniform motion definition and example + 1 Mark for non-uniform motion definition and example + 1 Mark for neat straight-line distance-time graph with labeled axes. Total = 3 Marks.",
        "concept": "Kinematics: Uniform vs Non-Uniform Motion & Graphical Analysis",
        "ncert_ref": "Chapter 3: Measurement of Time and Motion"
    },
    {
        "q_num": 37,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part III: Short Answer Questions",
        "type": "sa",
        "marks": 3,
        "question": "Explain the scientific mechanism responsible for sea breezes during daytime and land breezes at night in coastal environments with reference to modes of heat transfer. [3 Marks]",
        "model_answer": """<strong>Mode of Heat Transfer:</strong> Thermal Convection in air driven by differential rates of heating and cooling of land and water (due to water's higher specific heat capacity).

<br><br><strong>(a) Sea Breeze (During Daytime):</strong>
<ol>
  <li>During daylight, land heats up significantly faster than seawater under solar radiation.</li>
  <li>The air above the warm land becomes hot, expands, decreases in density, and rises, creating a low-pressure zone.</li>
  <li>The cooler, denser, high-pressure air over the sea moves inland toward the shore to take its place.</li>
  <li>This cool breeze blowing <strong>from the sea towards the land during the daytime</strong> is termed a <strong>sea breeze</strong>.</li>
</ol>

<strong>(b) Land Breeze (During Nighttime):</strong>
<ol>
  <li>At night, solar heating stops. Land cools down much faster than seawater, which retains thermal energy much longer.</li>
  <li>The warmer air situated over the sea expands and rises.</li>
  <li>The cooler, denser air from the land flows seaward to replace the rising air over the water.</li>
  <li>This breeze blowing <strong>from the land towards the sea at night</strong> is termed a <strong>land breeze</strong>.</li>
</ol>""",
        "marking_scheme": "0.5 Mark for identifying thermal convection and differential heating capacity of land/sea + 1.25 Marks for detailed sea breeze daytime mechanism + 1.25 Marks for detailed land breeze nighttime mechanism. Total = 3 Marks.",
        "concept": "Atmospheric Convection Currents: Sea and Land Breezes",
        "ncert_ref": "Chapter 2: Heat Transfer and Temperature"
    },
    # Part IV: Q38 (4M Case Study)
    {
        "q_num": 38,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part IV: Case Study Based Question",
        "type": "case_study",
        "marks": 4,
        "case_text": """<strong>CASE STUDY: EXPRESSWAY TRAVEL & SPEED KINEMATICS</strong><br>
Sunita and her father set out on an expressway journey from City A to City B. Before departing at 8:00 AM, Sunita noted that the car's odometer read 12,450 km. At 10:30 AM, they arrived at City B, and the odometer displayed 12,630 km. During the trip, Sunita checked the speedometer periodically and noted that it hovered around 80 km/h, though it dropped to zero at two toll gates.""",
        "question": "(a) Differentiate between the measurement functions of an odometer and a speedometer. [1 Mark]<br>(b) Calculate the total distance traveled and the total elapsed travel time in hours. [1 Mark]<br>(c) Calculate the average speed of the vehicle in km/h for the entire trip, and convert this value into m/s. [2 Marks]",
        "model_answer": """<strong>(a) Measurement Functions of Odometer vs Speedometer:</strong>
<ul>
  <li><strong>Odometer:</strong> Measures and records the <strong>cumulative total distance</strong> traversed by the vehicle, expressed in kilometers (km).</li>
  <li><strong>Speedometer:</strong> Measures and displays the <strong>instantaneous speed</strong> of the vehicle at any particular moment in time, expressed in kilometers per hour (km/h).</li>
</ul>

<strong>(b) Calculation of Distance and Time:</strong>
<ul>
  <li><strong>Total Distance Traveled (d):</strong><br>
  Final Odometer Reading - Initial Odometer Reading<br>
  = 12,630 km - 12,450 km = <strong>180 km</strong></li>
  <li><strong>Total Elapsed Time (t):</strong><br>
  From 8:00 AM to 10:30 AM = 2 hours and 30 minutes<br>
  = 2 + (30 / 60) = <strong>2.5 hours</strong></li>
</ul>

<strong>(c) Average Speed in km/h and Conversion to m/s:</strong>
<div class="formula-box">
  <strong>1. Average Speed (v<sub>av</sub>):</strong><br>
  Average Speed = Total Distance Traveled / Total Time Taken<br>
  v<sub>av</sub> = 180 km / 2.5 h = <strong>72 km/h</strong><br><br>
  <strong>2. Conversion into m/s:</strong><br>
  To convert km/h to m/s, multiply by 5/18 (since 1000 m / 3600 s = 5/18):<br>
  v<sub>av</sub> = 72 &times; (5 / 18) = 4 &times; 5 = <strong>20 m/s</strong>
</div>""",
        "marking_scheme": "(a) 1 Mark for distinguishing odometer (distance) and speedometer (instant speed). (b) 0.5 Mark for distance (180 km) + 0.5 Mark for time (2.5 h). (c) 1 Mark for average speed formula and 72 km/h + 1 Mark for unit conversion and 20 m/s. Total = 4 Marks.",
        "concept": "Kinematics Telemetry, Average Speed & Dimensional Unit Conversion",
        "ncert_ref": "Chapter 3: Measurement of Time and Motion"
    },
    # Part V: Q39 (5M LA with OR)
    {
        "q_num": 39,
        "section": "phy",
        "section_name": "Section C: Physics",
        "part": "Part V: Long Answer Question",
        "type": "la",
        "marks": 5,
        "question": "(a) What is an electric fuse? On which scientific effect of electric current does it function? (2 Marks)<br>(b) Why are Miniature Circuit Breakers (MCBs) increasingly replacing traditional rewirable wire fuses in modern electrical switchboards? (1.5 Marks)<br>(c) Why is substituting an ordinary thick copper wire in place of an authentic rated fuse wire an extremely dangerous hazard? (1.5 Marks) [Evaluating]<br><div style='text-align:center; font-weight:700; margin:8px 0;'>OR</div>(a) Describe a controlled experiment using two tin cans (one painted dull black, one polished shiny white) to prove that dark surfaces absorb and emit thermal radiation more effectively. (3 Marks)<br>(b) Why do we wear light-colored cotton garments in peak summers and dark woolen attire during winter? Explain using heat transfer principles. (2 Marks) [5 Marks]",
        "model_answer": """<strong>(a) Electric Fuse & Working Principle:</strong>
<ul>
  <li><strong>Definition:</strong> An electric fuse is an essential electrical safety device connected in series with the live wire of a circuit to protect household wiring and appliances from damage caused by short-circuits and electrical overloads.</li>
  <li><strong>Scientific Effect:</strong> It operates strictly on the <strong>heating effect of electric current (Joule heating, H = I²Rt)</strong>. The fuse wire is manufactured from a low-melting-point alloy (such as lead-tin). When an excessive current flows, Joule heating quickly melts the wire, breaking the circuit instantly.</li>
</ul>

<strong>(b) Why MCBs are Replacing Traditional Wire Fuses:</strong>
<ol>
  <li><strong>Automatic and Rapid Tripping:</strong> An MCB automatically switches off within milliseconds via electromagnetic sensing whenever an overcurrent or short circuit occurs, offering superior sensitivity.</li>
  <li><strong>Quick Reset without Rewiring:</strong> When a wire fuse blows, the melted wire must be manually rethreaded, posing risks of wrong wire thickness. An MCB simply trips its switch, which can be flipped back up into the 'ON' position once the fault is cleared.</li>
  <li><strong>Safety:</strong> Eliminates the risk of electrical contact shocks during fuse wire replacement.</li>
</ol>

<strong>(c) Severe Hazard of Using Thick Copper Wire as Fuse:</strong>
<ul>
  <li>An authentic fuse wire is engineered with a strictly calculated low melting point to melt before domestic copper wires overheat.</li>
  <li>A thick copper wire has very low electrical resistance and an extremely high melting point (~1085 °C).</li>
  <li>If an overcurrent surge occurs, the thick copper wire will <strong>not melt</strong>. As a result, massive current will continue flowing through domestic wiring, causing wall wires to overheat, melt their PVC insulation, damage valuable appliances, and ignite devastating electrical fires.</li>
</ul>

<div class="or-box">
  <div class="or-badge">OR OPTION: RADIATION EXPERIMENT & SEASONAL CLOTHING</div>
  <strong>(a) Controlled Tin Can Radiation Experiment:</strong>
  <ol>
    <li><strong>Setup:</strong> Take two identical tin cans of equal volume. Paint the exterior of Can A with matte black paint, and paint Can B with polished reflective white paint.</li>
    <li><strong>Absorption Phase:</strong> Pour equal quantities of cold water (at 20 °C) into both cans. Insert a laboratory thermometer through a lid into each can. Place both cans side-by-side in direct bright sunlight for 1 hour.
      <ul>
        <li><em>Observation:</em> Water temperature in the Black Can A rises significantly higher than in the White Can B, proving that dull black surfaces absorb radiant heat much more effectively.</li>
      </ul>
    </li>
    <li><strong>Emission Phase:</strong> Now fill both cans with equal volumes of hot water at 70 °C and place them in a shaded, cool room for 15 minutes.
      <ul>
        <li><em>Observation:</em> The temperature in Black Can A falls significantly faster than in White Can B, proving that dark surfaces are also superior heat emitters.</li>
      </ul>
    </li>
  </ol>

  <br><strong>(b) Seasonal Garments and Heat Transfer Principles:</strong>
  <ul>
    <li><strong>Summer Attire (Light Cotton):</strong> Light/white clothes reflect the vast majority of incident solar radiant heat rather than absorbing it. Cotton is porous and breathable; it readily absorbs body sweat and exposes it to air, causing continuous evaporative cooling.</li>
    <li><strong>Winter Attire (Dark Woolens):</strong> Dark clothes absorb maximum radiant heat from surroundings. Wool is a poor conductor of heat, and its crimped fibers trap a large amount of stationary air (air is an excellent thermal insulator), preventing metabolic body heat from escaping into the cold environment.</li>
  </ul>
</div>""",
        "marking_scheme": "(a) 1 Mark for fuse definition + 1 Mark for heating effect (Joule's law). (b) 1.5 Marks for MCB advantages (automatic tripping, easy reset, safety). (c) 1.5 Marks for thick copper wire high melting point hazard and fire risk. OR: (a) 1.5 Marks for absorption experiment + 1.5 Marks for emission experiment with clear observations. (b) 1 Mark for light cotton summer reflection & perspiration evaporation + 1 Mark for dark wool winter absorption & trapped air insulation. Total = 5 Marks.",
        "concept": "Electrical Protection, Circuit Breakers vs Fuses & Radiation Principles",
        "ncert_ref": "Chapter 1: Electricity & Chapter 2: Heat Transfer and Temperature"
    }
]

print(f"Total questions loaded: {len(questions_data)}")

# -------------------------------------------------------------
# 2. GENERATE JSON KNOWLEDGE BASE
# -------------------------------------------------------------
kb_json = {
    "subject": "Science",
    "curriculum_source": "school_exam_paper",
    "source_display": "Silver Bells Public School, Bhavnagar — Mid Term Assessment 2026-27",
    "standard": "Std VII (Alpha 7)",
    "exam_date": "09 October 2026",
    "time_allowed": "3 Hours",
    "total_marks": 80,
    "total_questions": 39,
    "created_at": "10 October 2026, 18:30 IST",
    "last_modified": "10 October 2026, 18:30 IST",
    "section_marks": {
        "Section A: Biology": 30,
        "Section B: Chemistry": 25,
        "Section C: Physics": 25
    },
    "blueprint": {
        "Section A (Biology - 30M)": "Q1-Q9: 9 MCQs/AR (9M), Q10-Q12: 3 VSA (6M), Q13-Q14: 2 SA (6M), Q15: 1 Case Study (4M), Q16: 1 LA (5M)",
        "Section B (Chemistry - 25M)": "Q17-Q24: 8 MCQs/AR (8M), Q25: 1 VSA (2M), Q26-Q27: 2 SA (6M), Q28: 1 Case Study (4M), Q29: 1 LA (5M)",
        "Section C (Physics - 25M)": "Q30-Q32: 3 MCQs (3M), Q33-Q34: 2 VSA (4M), Q35-Q37: 3 SA (9M), Q38: 1 Case Study (4M), Q39: 1 LA (5M)"
    },
    "questions": questions_data
}

# Write JSON to both destinations
json_file_1 = os.path.join(kb_dir_1, "sci_school_midterm_2026_silver_bells.json")
json_file_2 = os.path.join(kb_dir_2, "sci_school_midterm_2026_silver_bells.json")

with open(json_file_1, "w", encoding="utf-8") as f:
    json.dump(kb_json, f, indent=2, ensure_ascii=False)

with open(json_file_2, "w", encoding="utf-8") as f:
    json.dump(kb_json, f, indent=2, ensure_ascii=False)

print(f"JSON Knowledge Base saved to:\n  - {json_file_1}\n  - {json_file_2}")

# -------------------------------------------------------------
# 3. GENERATE MARKDOWN STUDY GUIDE
# -------------------------------------------------------------
md_lines = [
    "# Silver Bells Public School, Bhavnagar — Mid-Term Assessment 2026–27",
    "## Subject: Science | Std: Alpha 7 | Total Marks: 80 | Time: 3 Hours",
    "**Date of Exam:** 09/10/2026  ",
    "**Official Model Answers, Marking Schemes, and Rubrics**",
    "",
    "---",
    "",
    "## Blueprint Summary",
    "| Section | Discipline | Marks | Question Range | Typologies |",
    "| :--- | :--- | :--- | :--- | :--- |",
    "| **Section A** | Biology | 30 Marks | Q1 – Q16 | 9 MCQs/AR (9M), 3 VSA (6M), 2 SA (6M), 1 Case Study (4M), 1 LA (5M) |",
    "| **Section B** | Chemistry | 25 Marks | Q17 – Q29 | 8 MCQs/AR (8M), 1 VSA (2M), 2 SA (6M), 1 Case Study (4M), 1 LA (5M) |",
    "| **Section C** | Physics | 25 Marks | Q30 – Q39 | 3 MCQs (3M), 2 VSA (4M), 3 SA (9M), 1 Case Study (4M), 1 LA (5M) |",
    "| **Total** | **Science** | **80 Marks** | **39 Questions** | **Full NCERT / CBSE Aligned Blueprint** |",
    "",
    "---",
    ""
]

current_sec = ""
for q in questions_data:
    if q["section_name"] != current_sec:
        current_sec = q["section_name"]
        md_lines.append(f"\n# {current_sec.upper()}\n")

    md_lines.append(f"### Q{q['q_num']}. [{q['marks']} Mark{'s' if q['marks']>1 else ''}] — {q['part']}")
    md_lines.append(f"**Concept:** {q['concept']} | **NCERT:** {q['ncert_ref']}\n")
    if "case_text" in q:
        md_lines.append(f"> {q['case_text'].replace('<br>', '\n> ')}\n")
    md_lines.append(f"**Question:**\n{q['question'].replace('<br>', '\n')}\n")

    if q["type"] in ["mcq", "ar"]:
        md_lines.append("**Options:**")
        for opt_key, opt_val in q["options"].items():
            check = " *(Correct)*" if opt_key == q["correct"] else ""
            md_lines.append(f"- ({opt_key}) {opt_val}{check}")
        md_lines.append(f"\n**Correct Answer:** `({q['correct']}) {q['options'][q['correct']]}`")
        md_lines.append(f"\n**Explanation:**\n{q['explanation']}\n")
    else:
        clean_model = q["model_answer"].replace("<br>", "\n").replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
        md_lines.append(f"**Model Solution:**\n{clean_model}\n")
        md_lines.append(f"**Marking Scheme & Rubric:**\n*{q['marking_scheme']}*\n")
    md_lines.append("---\n")

md_content = "\n".join(md_lines)

md_file_1 = os.path.join(kb_dir_1, "sci_school_midterm_2026_silver_bells.md")
md_file_2 = os.path.join(kb_dir_2, "sci_school_midterm_2026_silver_bells.md")

with open(md_file_1, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(md_file_2, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Markdown Study Guide saved to:\n  - {md_file_1}\n  - {md_file_2}")

# -------------------------------------------------------------
# 4. GENERATE INTERACTIVE HTML TEST PAGE
# -------------------------------------------------------------

def render_mcq_html(q):
    options_html = ""
    for opt_key, opt_val in q["options"].items():
        is_cor = "true" if opt_key == q["correct"] else "false"
        options_html += f"""
        <div class="opt-btn" data-opt="{opt_key}" data-correct="{is_cor}" onclick="handleOptClick(this, '{opt_key}', '{q['correct']}')">
          <span class="opt-label">{opt_key.upper()}</span>
          <span class="opt-text">{opt_val}</span>
        </div>"""

    return f"""
    <div class="q-card" data-section="{q['section']}" data-type="{q['type']}" data-qnum="{q['q_num']}">
      <div class="q-header">
        <div class="q-badge-group">
          <span class="q-num-pill">Q{q['q_num']}</span>
          <span class="q-badge badge-{q['section']}">{q['section_name'].split(':')[1].strip()}</span>
          <span class="q-badge badge-type">{ 'Assertion-Reason' if q['type'] == 'ar' else 'MCQ' }</span>
          <span class="q-marks-pill">{q['marks']} Mark</span>
        </div>
        <div class="q-meta-concept"><i class="fas fa-bookmark"></i> {q['concept']}</div>
      </div>
      <div class="q-prompt">{q['question']}</div>
      <div class="options-container">
        {options_html}
      </div>
      <div class="explanation-box" id="exp-{q['q_num']}">
        <div class="exp-header"><i class="fas fa-lightbulb"></i> <strong>Scientific Rationale & Key Concept:</strong></div>
        <div class="exp-body">
          <p><strong>Correct Answer:</strong> <span class="badge-cor">Option ({q['correct'].upper()}): {q['options'][q['correct']]}</span></p>
          <p>{q['explanation']}</p>
        </div>
      </div>
    </div>"""

def render_subjective_html(q):
    case_block = ""
    if "case_text" in q:
        case_block = f"""
        <div class="case-study-box">
          <div class="case-header"><i class="fas fa-newspaper"></i> CASE STUDY TEXT</div>
          <div class="case-body">{q['case_text']}</div>
        </div>"""

    type_name = "Very Short Answer" if q['type'] == 'vsa' else ("Short Answer" if q['type'] == 'sa' else ("Case Study" if q['type'] == 'case_study' else "Long Answer"))

    return f"""
    <div class="q-card" data-section="{q['section']}" data-type="{q['type']}" data-qnum="{q['q_num']}">
      <div class="q-header">
        <div class="q-badge-group">
          <span class="q-num-pill">Q{q['q_num']}</span>
          <span class="q-badge badge-{q['section']}">{q['section_name'].split(':')[1].strip()}</span>
          <span class="q-badge badge-type">{type_name}</span>
          <span class="q-marks-pill">{q['marks']} Marks</span>
        </div>
        <div class="q-meta-concept"><i class="fas fa-bookmark"></i> {q['concept']}</div>
      </div>
      {case_block}
      <div class="q-prompt">{q['question']}</div>
      
      <div class="solution-toggle-bar">
        <button type="button" class="btn-toggle-sol" onclick="toggleSolution({q['q_num']})">
          <i class="fas fa-eye" id="eye-icon-{q['q_num']}"></i> <span id="btn-text-{q['q_num']}">Reveal Model Solution & Marking Scheme</span>
        </button>
      </div>

      <div class="solution-pane" id="sol-{q['q_num']}">
        <div class="sol-inner">
          <div class="sol-header">
            <span class="sol-title"><i class="fas fa-certificate"></i> CBSE / NCERT Model Solution</span>
            <span class="sol-ncert-badge"><i class="fas fa-book-open"></i> {q['ncert_ref']}</span>
          </div>
          <div class="sol-content">
            {q['model_answer']}
          </div>
          <div class="marking-scheme-box">
            <div class="ms-title"><i class="fas fa-check-double"></i> Step-by-Step Marking Scheme & Rubric:</div>
            <div class="ms-body">{q['marking_scheme']}</div>
          </div>
        </div>
      </div>
    </div>"""

cards_html = ""
for q in questions_data:
    if q["type"] in ["mcq", "ar"]:
        cards_html += render_mcq_html(q)
    else:
        cards_html += render_subjective_html(q)

html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Science Mid-Term Assessment 2026–27 (Official 80M Paper & Model Solutions) | Silver Bells Public School</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {{
      --primary: #10b981;
      --primary-glow: #34d399;
      --primary-subtle: rgba(16, 185, 129, 0.15);
      --primary-deep: rgba(16, 185, 129, 0.08);

      --bio-color: #10b981;
      --bio-subtle: rgba(16, 185, 129, 0.15);
      --bio-border: rgba(16, 185, 129, 0.35);

      --chem-color: #8b5cf6;
      --chem-subtle: rgba(139, 92, 246, 0.15);
      --chem-border: rgba(139, 92, 246, 0.35);

      --phy-color: #06b6d4;
      --phy-subtle: rgba(6, 182, 212, 0.15);
      --phy-border: rgba(6, 182, 212, 0.35);

      --bg-main: #0a0e1a;
      --bg-card: rgba(15, 23, 42, 0.90);
      --surface: #131d31;
      --surface-hover: #1c2a44;
      --surface-glass: rgba(19, 29, 49, 0.95);

      --text-main: #e2e8f0;
      --text-muted: #94a3b8;
      --text-title: #ffffff;
      --text-dim: #64748b;

      --border: rgba(255, 255, 255, 0.09);
      --border-hover: rgba(16, 185, 129, 0.45);

      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --cyan: #06b6d4;

      --font-body: 'Inter', sans-serif;
      --font-head: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --font-space: 'Space Mono', monospace;

      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.35);
      --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.45);
      --shadow-lg: 0 8px 36px rgba(0, 0, 0, 0.60);
    }}

    [data-theme="light"] {{
      --bg-main: #f8fafc;
      --bg-card: #ffffff;
      --surface: #f1f5f9;
      --surface-hover: #e2e8f0;
      --surface-glass: rgba(241, 245, 249, 0.97);

      --primary: #059669;
      --primary-glow: #10b981;
      --primary-subtle: #d1fae5;
      --primary-deep: #ecfdf5;

      --bio-color: #059669;
      --bio-subtle: #d1fae5;
      --bio-border: #a7f3d0;

      --chem-color: #7c3aed;
      --chem-subtle: #ede9fe;
      --chem-border: #ddd6fe;

      --phy-color: #0891b2;
      --phy-subtle: #cffafe;
      --phy-border: #a5f3fc;

      --text-main: #1e293b;
      --text-muted: #64748b;
      --text-title: #0f172a;
      --text-dim: #94a3b8;

      --border: rgba(0, 0, 0, 0.09);
      --border-hover: rgba(16, 185, 129, 0.4);

      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.10);
      --shadow-lg: 0 8px 36px rgba(0, 0, 0, 0.15);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: var(--font-body);
      background: var(--bg-main);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Header Bar */
    .site-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      height: 58px;
      background: var(--surface-glass);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
    }}
    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.9rem;
    }}
    .header-left a {{
      color: var(--text-muted);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .header-left a:hover {{ color: var(--primary); }}
    .crumb-sep {{ color: var(--text-dim); font-size: 0.75rem; }}
    .crumb-active {{ color: var(--text-title); font-weight: 700; }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-tool {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-tool:hover {{
      background: var(--surface-hover);
      border-color: var(--primary);
      color: var(--text-title);
    }}
    .btn-primary-tool {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}
    .btn-primary-tool:hover {{
      background: var(--primary-glow);
    }}

    /* Main Container */
    .main-wrapper {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 24px 20px 80px;
      width: 100%;
    }}

    /* Exam Paper Hero Banner */
    .exam-hero {{
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(139, 92, 246, 0.08) 50%, rgba(6, 182, 212, 0.1) 100%);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      position: relative;
      overflow: hidden;
    }}
    .exam-hero::before {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 4px;
      background: linear-gradient(90deg, #10b981, #8b5cf6, #06b6d4, #f59e0b);
    }}
    .hero-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .school-title {{
      font-family: var(--font-head);
      font-size: 1.55rem;
      font-weight: 800;
      color: var(--text-title);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .assessment-sub {{
      font-size: 1rem;
      color: var(--primary);
      font-weight: 700;
      margin-top: 4px;
    }}
    .meta-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .meta-pill {{
      background: var(--surface-glass);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-family: var(--font-space);
      font-weight: 600;
      color: var(--text-main);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .hero-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 12px;
    }}
    .hero-stat-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .stat-icon {{
      width: 42px;
      height: 42px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }}
    .stat-bio {{ background: var(--bio-subtle); color: var(--bio-color); }}
    .stat-chem {{ background: var(--chem-subtle); color: var(--chem-color); }}
    .stat-phy {{ background: var(--phy-subtle); color: var(--phy-color); }}
    .stat-total {{ background: rgba(245, 158, 11, 0.15); color: #f59e0b; }}
    .stat-info-title {{ font-size: 0.76rem; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-space); }}
    .stat-info-val {{ font-size: 1.05rem; font-weight: 700; color: var(--text-title); font-family: var(--font-head); }}

    /* Sticky Control Toolbar */
    .controls-bar {{
      position: sticky;
      top: 58px;
      z-index: 900;
      background: var(--surface-glass);
      backdrop-filter: blur(14px);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      box-shadow: var(--shadow-sm);
    }}
    .section-nav-pills {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .nav-pill {{
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text-muted);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .nav-pill:hover {{
      color: var(--text-title);
      border-color: var(--primary);
    }}
    .nav-pill.active {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);
    }}

    .type-filter-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .filter-select {{
      padding: 6px 12px;
      border-radius: 8px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-main);
      font-size: 0.82rem;
      font-weight: 500;
      cursor: pointer;
    }}

    /* Score Bar for Student Mode */
    .score-summary-bar {{
      background: var(--primary-deep);
      border: 1px dashed var(--primary);
      border-radius: 10px;
      padding: 10px 16px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.88rem;
    }}

    /* Question Cards */
    .q-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 22px;
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
      position: relative;
    }}
    .q-card:hover {{
      border-color: var(--border-hover);
      box-shadow: var(--shadow-md);
    }}
    .q-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .q-badge-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .q-num-pill {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--primary);
      font-family: var(--font-space);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    .q-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      font-family: var(--font-mono);
    }}
    .badge-bio {{ background: var(--bio-subtle); color: var(--bio-color); border: 1px solid var(--bio-border); }}
    .badge-chem {{ background: var(--chem-subtle); color: var(--chem-color); border: 1px solid var(--chem-border); }}
    .badge-phy {{ background: var(--phy-subtle); color: var(--phy-color); border: 1px solid var(--phy-border); }}
    .badge-type {{ background: var(--surface); color: var(--text-muted); border: 1px solid var(--border); }}
    .q-marks-pill {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: #fbbf24;
      font-family: var(--font-space);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
    }}
    .q-meta-concept {{
      font-size: 0.78rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .q-prompt {{
      font-size: 1.02rem;
      font-weight: 600;
      color: var(--text-title);
      margin-bottom: 16px;
      line-height: 1.65;
    }}

    /* Options Container for MCQs */
    .options-container {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
      margin-bottom: 14px;
    }}
    .opt-btn {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 14px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      cursor: pointer;
      transition: all 0.2s;
      font-size: 0.92rem;
    }}
    .opt-btn:hover {{
      background: var(--surface-hover);
      border-color: var(--primary);
    }}
    .opt-label {{
      background: var(--bg-main);
      border: 1px solid var(--border);
      color: var(--text-muted);
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.78rem;
      font-weight: 700;
      flex-shrink: 0;
      font-family: var(--font-mono);
    }}
    .opt-text {{
      flex: 1;
      padding-top: 2px;
    }}

    .opt-btn.opt-correct {{
      background: rgba(16, 185, 129, 0.15) !important;
      border-color: #10b981 !important;
      color: #34d399 !important;
    }}
    .opt-btn.opt-correct .opt-label {{
      background: #10b981;
      color: #fff;
      border-color: #10b981;
    }}

    .opt-btn.opt-wrong {{
      background: rgba(239, 68, 68, 0.15) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }}
    .opt-btn.opt-wrong .opt-label {{
      background: #ef4444;
      color: #fff;
      border-color: #ef4444;
    }}

    /* Explanation Box */
    .explanation-box {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-left: 4px solid var(--primary);
      border-radius: 8px;
      padding: 12px 16px;
      margin-top: 12px;
      display: none;
      animation: fadeIn 0.3s ease;
    }}
    .exp-header {{
      color: var(--primary-glow);
      font-size: 0.88rem;
      margin-bottom: 6px;
    }}
    .exp-body {{
      font-size: 0.88rem;
      color: var(--text-main);
      line-height: 1.6;
    }}
    .badge-cor {{
      color: #34d399;
      font-weight: 700;
    }}

    /* Subjective Toggle and Pane */
    .solution-toggle-bar {{
      margin-top: 12px;
    }}
    .btn-toggle-sol {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--primary);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }}
    .btn-toggle-sol:hover {{
      background: var(--primary-subtle);
      border-color: var(--primary);
      color: var(--text-title);
    }}

    .solution-pane {{
      margin-top: 14px;
      display: none;
      animation: fadeIn 0.35s ease;
    }}
    .sol-inner {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--primary);
      border-radius: 10px;
      padding: 18px 20px;
    }}
    .sol-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px dashed var(--border);
    }}
    .sol-title {{
      font-family: var(--font-head);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-glow);
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .sol-ncert-badge {{
      font-size: 0.76rem;
      font-family: var(--font-space);
      color: var(--text-muted);
    }}
    .sol-content {{
      font-size: 0.92rem;
      color: var(--text-main);
      line-height: 1.7;
    }}
    .sol-content ol, .sol-content ul {{
      margin-left: 20px;
      margin-top: 8px;
      margin-bottom: 8px;
    }}
    .sol-content li {{
      margin-bottom: 6px;
    }}

    /* Marking Scheme Box */
    .marking-scheme-box {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 8px;
      padding: 10px 14px;
      margin-top: 14px;
      font-size: 0.84rem;
    }}
    .ms-title {{
      color: #fbbf24;
      font-weight: 700;
      font-size: 0.82rem;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .ms-body {{
      color: var(--text-muted);
      font-style: italic;
    }}

    /* Case Study Box */
    .case-study-box {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 18px;
      margin-bottom: 16px;
    }}
    .case-header {{
      color: var(--phy-color);
      font-family: var(--font-space);
      font-weight: 700;
      font-size: 0.8rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .case-body {{
      font-size: 0.92rem;
      color: var(--text-main);
      line-height: 1.65;
    }}

    /* OR Option Box */
    .or-box {{
      background: rgba(139, 92, 246, 0.08);
      border: 1px solid rgba(139, 92, 246, 0.25);
      border-radius: 8px;
      padding: 14px 16px;
      margin-top: 16px;
    }}
    .or-badge {{
      display: inline-block;
      background: var(--chem-color);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      font-family: var(--font-mono);
      margin-bottom: 8px;
    }}

    /* Formulas & Flowcharts */
    .formula-box {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 10px 0;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: var(--primary-glow);
    }}
    .flowchart-box {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 14px;
      margin: 10px 0;
      font-family: var(--font-space);
      font-size: 0.85rem;
      color: var(--cyan);
      word-break: break-word;
    }}

    /* Tables */
    .exam-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      font-size: 0.88rem;
    }}
    .exam-table th, .exam-table td {{
      border: 1px solid var(--border);
      padding: 8px 12px;
      text-align: left;
    }}
    .exam-table th {{
      background: var(--surface-hover);
      color: var(--primary);
      font-family: var(--font-head);
    }}

    /* Schematic Symbols Grid */
    .symbols-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin: 12px 0;
    }}
    .sym-card {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
    }}
    .sym-name {{
      font-weight: 700;
      font-size: 0.82rem;
      color: var(--primary-glow);
      margin-bottom: 6px;
    }}
    .sym-visual {{
      background: var(--bg-main);
      border-radius: 6px;
      padding: 6px;
      margin-bottom: 6px;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .sym-desc {{
      font-size: 0.72rem;
      color: var(--text-muted);
    }}

    /* Graph Visual Container */
    .graph-visual-container {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      margin: 12px 0;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    /* Global Teacher Mode */
    body.teacher-mode .solution-pane {{
      display: block !important;
    }}
    body.teacher-mode .explanation-box {{
      display: block !important;
    }}
    body.teacher-mode .btn-toggle-sol {{
      display: none !important;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Print Stylesheet */
    @media print {{
      .site-header, .controls-bar, .score-summary-bar, .solution-toggle-bar {{
        display: none !important;
      }}
      body {{
        background: #fff !important;
        color: #000 !important;
        font-size: 10pt;
      }}
      .main-wrapper {{
        max-width: 100% !important;
        padding: 0 !important;
      }}
      .exam-hero {{
        border: 2px solid #000 !important;
        box-shadow: none !important;
        background: none !important;
      }}
      .q-card {{
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        background: #fff !important;
        break-inside: avoid;
        page-break-inside: avoid;
      }}
      .solution-pane, .explanation-box {{
        display: block !important;
        background: #fdfdfd !important;
        border: 1px solid #999 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Site Sticky Header -->
  <header class="site-header">
    <div class="header-left">
      <a href="../../science_index.html"><i class="fas fa-atom"></i> Science Hub</a>
      <span class="crumb-sep">/</span>
      <a href="../../science_index.html#sec-tests"><i class="fas fa-file-signature"></i> Test Bank</a>
      <span class="crumb-sep">/</span>
      <span class="crumb-active">Silver Bells Mid-Term 2026-27</span>
    </div>
    <div class="header-right">
      <button type="button" class="btn-tool" id="btn-toggle-mode" onclick="toggleTeacherMode()">
        <i class="fas fa-chalkboard-teacher"></i> <span id="mode-label">Teacher / Solution Mode</span>
      </button>
      <button type="button" class="btn-tool" onclick="window.print()">
        <i class="fas fa-print"></i> Print Paper
      </button>
      <button type="button" class="btn-tool" id="btn-theme-toggle" onclick="toggleTheme()">
        <i class="fas fa-moon" id="theme-icon"></i>
      </button>
    </div>
  </header>

  <main class="main-wrapper">

    <!-- Exam Hero Banner -->
    <div class="exam-hero">
      <div class="hero-top">
        <div>
          <h1 class="school-title">
            <i class="fas fa-school" style="color:var(--primary);"></i>
            Silver Bells Public School, Bhavnagar
          </h1>
          <div class="assessment-sub">
            Mid-term Assessment 2026–27 &bull; Subject: Science &bull; Std: Alpha 7
          </div>
        </div>
        <div class="meta-pills">
          <div class="meta-pill"><i class="fas fa-calendar-day" style="color:var(--primary)"></i> 09/10/2026</div>
          <div class="meta-pill"><i class="fas fa-clock" style="color:#f59e0b"></i> 3 Hours</div>
          <div class="meta-pill"><i class="fas fa-award" style="color:#38bdf8"></i> 80 Marks</div>
          <div class="meta-pill"><i class="fas fa-list-ol" style="color:#c084fc"></i> 39 Questions</div>
        </div>
      </div>

      <div class="hero-grid">
        <div class="hero-stat-card">
          <div class="stat-icon stat-bio"><i class="fas fa-dna"></i></div>
          <div>
            <div class="stat-info-title">Section A &bull; Biology</div>
            <div class="stat-info-val">30 Marks (Q1 – Q16)</div>
          </div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon stat-chem"><i class="fas fa-flask"></i></div>
          <div>
            <div class="stat-info-title">Section B &bull; Chemistry</div>
            <div class="stat-info-val">25 Marks (Q17 – Q29)</div>
          </div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon stat-phy"><i class="fas fa-bolt"></i></div>
          <div>
            <div class="stat-info-title">Section C &bull; Physics</div>
            <div class="stat-info-val">25 Marks (Q30 – Q39)</div>
          </div>
        </div>
        <div class="hero-stat-card">
          <div class="stat-icon stat-total"><i class="fas fa-check-circle"></i></div>
          <div>
            <div class="stat-info-title">Model Solutions</div>
            <div class="stat-info-val">100% Solved + Rubrics</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Controls Toolbar -->
    <div class="controls-bar">
      <div class="section-nav-pills">
        <button type="button" class="nav-pill active" onclick="filterSection('all', this)">
          <i class="fas fa-layer-group"></i> All Sections (39 Qs)
        </button>
        <button type="button" class="nav-pill" onclick="filterSection('bio', this)">
          <i class="fas fa-leaf" style="color:var(--bio-color);"></i> Sec A: Biology (30M)
        </button>
        <button type="button" class="nav-pill" onclick="filterSection('chem', this)">
          <i class="fas fa-vial" style="color:var(--chem-color);"></i> Sec B: Chemistry (25M)
        </button>
        <button type="button" class="nav-pill" onclick="filterSection('phy', this)">
          <i class="fas fa-bolt" style="color:var(--phy-color);"></i> Sec C: Physics (25M)
        </button>
      </div>

      <div class="type-filter-group">
        <label for="type-select" style="font-size:0.8rem; color:var(--text-muted); font-weight:600;">Filter Typology:</label>
        <select id="type-select" class="filter-select" onchange="filterType(this.value)">
          <option value="all">All Typologies</option>
          <option value="mcq">MCQs & Assertion-Reason (20 Qs)</option>
          <option value="vsa">Very Short Answer (6 Qs)</option>
          <option value="sa">Short Answer (7 Qs)</option>
          <option value="case_study">Case Study Based (3 Qs)</option>
          <option value="la">Long Answer (3 Qs)</option>
        </select>
      </div>
    </div>

    <!-- Student Score Tracker Bar -->
    <div class="score-summary-bar" id="score-bar">
      <div>
        <i class="fas fa-tasks" style="color:var(--primary);"></i>
        <strong>Interactive Objective Drills:</strong> Attempt MCQs below for instant evaluation.
      </div>
      <div>
        <strong>MCQ Score:</strong> <span id="mcq-score" style="color:var(--primary); font-weight:700; font-family:var(--font-mono);">0 / 20</span>
      </div>
    </div>

    <!-- Questions Container -->
    <div id="questions-container">
      {cards_html}
    </div>

  </main>

  <script>
    let currentSectionFilter = 'all';
    let currentTypeFilter = 'all';
    let correctCount = 0;
    let answeredQNums = new Set();
    const totalMCQs = 20;

    // Filter by Section
    function filterSection(section, btn) {{
      currentSectionFilter = section;
      document.querySelectorAll('.nav-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      applyFilters();
    }}

    // Filter by Question Typology
    function filterType(type) {{
      currentTypeFilter = type;
      applyFilters();
    }}

    function applyFilters() {{
      const cards = document.querySelectorAll('.q-card');
      cards.forEach(card => {{
        const cardSection = card.getAttribute('data-section');
        const cardType = card.getAttribute('data-type');
        
        let matchSection = (currentSectionFilter === 'all' || cardSection === currentSectionFilter);
        let matchType = (currentTypeFilter === 'all' || 
          (currentTypeFilter === 'mcq' && (cardType === 'mcq' || cardType === 'ar')) ||
          cardType === currentTypeFilter);

        if (matchSection && matchType) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Handle Option Click
    function handleOptClick(btn, selectedOpt, correctOpt) {{
      const card = btn.closest('.q-card');
      const qNum = card.getAttribute('data-qnum');
      const expBox = document.getElementById('exp-' + qNum);
      const isAlreadyAnswered = answeredQNums.has(qNum);

      // Disable sibling clicks
      const allOpts = card.querySelectorAll('.opt-btn');
      allOpts.forEach(b => b.style.pointerEvents = 'none');

      if (selectedOpt === correctOpt) {{
        btn.classList.add('opt-correct');
        if (!isAlreadyAnswered) {{
          correctCount++;
          answeredQNums.add(qNum);
        }}
      }} else {{
        btn.classList.add('opt-wrong');
        // Highlight correct
        allOpts.forEach(b => {{
          if (b.getAttribute('data-opt') === correctOpt) {{
            b.classList.add('opt-correct');
          }}
        }});
        answeredQNums.add(qNum);
      }}

      // Show explanation
      if (expBox) {{
        expBox.style.display = 'block';
      }}

      // Update Score
      const scoreElem = document.getElementById('mcq-score');
      if (scoreElem) {{
        scoreElem.innerText = correctCount + ' / ' + totalMCQs;
      }}
    }}

    // Toggle Individual Solution
    function toggleSolution(qNum) {{
      const pane = document.getElementById('sol-' + qNum);
      const icon = document.getElementById('eye-icon-' + qNum);
      const text = document.getElementById('btn-text-' + qNum);
      if (!pane) return;

      if (pane.style.display === 'block') {{
        pane.style.display = 'none';
        icon.className = 'fas fa-eye';
        text.innerText = 'Reveal Model Solution & Marking Scheme';
      }} else {{
        pane.style.display = 'block';
        icon.className = 'fas fa-eye-slash';
        text.innerText = 'Hide Model Solution';
      }}
    }}

    // Toggle Teacher Mode (Reveals all solutions instantly)
    function toggleTeacherMode() {{
      const isTeacher = document.body.classList.toggle('teacher-mode');
      const label = document.getElementById('mode-label');
      if (isTeacher) {{
        label.innerText = 'Switch to Student Mode';
      }} else {{
        label.innerText = 'Teacher / Solution Mode';
      }}
    }}

    // Theme Toggle
    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', target);
      localStorage.setItem('studyhub-theme', target);
      updateThemeIcon(target);
    }}

    function updateThemeIcon(theme) {{
      const icon = document.getElementById('theme-icon');
      if (icon) {{
        icon.className = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
      }}
    }}

    // Init Theme from localStorage
    document.addEventListener('DOMContentLoaded', () => {{
      const savedTheme = localStorage.getItem('studyhub-theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);
    }});
  </script>
</body>
</html>"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Interactive HTML Test page saved to:\n  - {html_path}")
print("All artifacts successfully created and synchronized!")
