# -*- coding: utf-8 -*-
"""
Compiler script for Class 7 Science (Biology) Chapter 4: Life Processes in Plants.
Dual-store output:
- KB Files/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.json
- KB Files/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.md
- knowledge_base/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.json
- knowledge_base/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.md

Strict adherence:
- Dual-schema parity: questions == assessment_items
- Diagram Slot Protocol for visual/experimental questions
- Pure Unicode text (CO₂, O₂, H₂O, C₆H₁₂O₆, Ca(OH)₂, CaCO₃, NaHCO₃, KOH, 25°C–40°C, →, ↓, ↑)
- Complete 100% ingestion of all text from user request (191 assessment items + 7 comprehensive theory modules)
"""

import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure directories exist
os.makedirs("KB Files/biology/ch4_life_processes_plants", exist_ok=True)
os.makedirs("knowledge_base/biology/ch4_life_processes_plants", exist_ok=True)

kb_metadata = {
    "subject": "Science",
    "discipline": "Biology",
    "chapter_num": 4,
    "chapter_title": "Life Processes in Plants",
    "kb_version": "1.0",
    "curriculum": "CBSE / NCERT / National Curriculum Framework (Class 7)",
    "book_page_range": "Chapter 4",
    "source_pdf": "source_materials/science/Bio_ch4_life_processes_in_plants.pdf",
    "summary": "Authoritative, zero-loss, curriculum-aligned knowledge base on plant life processes covering plant growth phases, autotrophic nutrition, photosynthesis biochemical mechanics and limiting factors, chloroplast ultrastructure, stomatal guard cell physiology, vascular transport (xylem ascent of sap vs phloem translocation), and plant cellular respiration across organs and diurnal cycles.",
    "learning_outcomes": [
        "Explain how plants grow through vegetative and reproductive phases driven by sunlight, water, and vital nutrients.",
        "Differentiate between autotrophic and heterotrophic nutrition, establishing why the Sun is the ultimate source of energy.",
        "Formulate and balance the chemical equation for photosynthesis and analyze the roles of chlorophyll, water, carbon dioxide, and sunlight.",
        "Examine the ultrastructure of chloroplasts (thylakoids, grana, stroma, stroma lamellae) and stomatal regulation via guard cells.",
        "Analyze factors governing the rate of photosynthesis: light intensity and quality (blue/red vs green), temperature (enzyme denaturation), CO₂ levels, and water.",
        "Explain vascular transport in plants: unidirectional xylem conduction of water and minerals vs bidirectional phloem translocation of organic sugars.",
        "Analyze plant cellular respiration across leaves (stomata), woody stems (lenticels), roots (root hairs), and mangrove swamps (pneumatophores).",
        "Compare photosynthesis and respiration during day and night, resolving diurnal gaseous exchange and the concept of compensation point."
    ]
}

theory_modules = [
    {
        "module_id": "bio_ch4_mod_01",
        "title": "Plant Growth Dynamics, Experimental Proofs & Ancient Insights",
        "content": """### 1. Dynamics of Plant Growth
Green plants are the true **"power plants"** of our planet. They capture solar energy and use it along with water and carbon dioxide to create organic molecules. This extraordinary ability to convert solar energy into food makes green plants and other autotrophs (such as algae, phytoplankton, and certain photosynthetic bacteria) **producers**.

As plants develop over time, they exhibit characteristic morphological and physiological transitions:
* **Vegetative Phase:** Marked by seed germination, emergence of the shoot from the soil, formation and expansion of new foliage, elongation of stem internodes, and development of lateral branches. In woody perennials, the stem accumulates secondary tissues, thickening its girth and becoming woody over time.
* **Reproductive Phase:** Transition from vegetative meristems to reproductive structures, characterized by flower initiation, pollination, fertilization, fruit development, and seed maturation.
* **Underlying Driving Life Processes:** Plant growth and morphogenesis are strictly powered by coordinated life processes including photosynthesis (carbon assimilation), cellular respiration (ATP production), vascular transport (water, mineral, and photoassimilate translocation), and transpiration (temperature regulation and transpirational pull).

---

### 2. Experimental Verification: Effect of Sunlight and Water on Plant Growth
An empirical investigation using three pots (A, B, and C) with chilli/tomato saplings over a 2-week period proves the fundamental necessity of abiotic factors:
* **Pot A (Direct sunlight + adequate moisture):** Height increased from 30 cm to 38 cm; leaves increased from 9 to 13; foliage remained healthy vibrant green.
* **Pot B (Direct sunlight + no water):** Height dropped from 28 cm to 25 cm due to loss of turgor; leaves dropped from 8 to 3; foliage turned dry yellow.
* **Pot C (Dark room + moist soil):** Height remained almost stagnant (31 cm to 30 cm); leaves decreased from 10 to 7; foliage turned etiolar greenish-yellow due to failure of chlorophyll biosynthesis.
* **Conclusion:** Maximum growth requires synergistic presence of both sunlight (energy source for photosynthesis) and water (turgor pressure, nutrient medium, and electron donor). Deprivation of either arrests growth and causes chlorosis and wilting.

---

### 3. Ancient Indian Insight: Vrikshayurveda
*Vrikshayurveda*, an ancient Indian classical treatise on arbori-horticulture and plant science, documents advanced empirical observations on plant physiology, soil classification, seed selection, crop rotation, and organic fertilization:
* Details traditional formulations of fermented organic manures (e.g., *Kunapajala*) prepared by infusing water, barley, and various pulses/legume seeds (green gram, black gram, horse gram).
* Emphasizes sustainable, chemical-free agricultural foundations, establishing that the future of ecological human nutrition is rooted in the principles of *Vrikshayurveda*."""
    },
    {
        "module_id": "bio_ch4_mod_02",
        "title": "Modes of Nutrition & The Sun as the Ultimate Energy Source",
        "content": """### 1. Classification of Nutrition Modes
Living organisms are classified based on their nutritional sourcing into two primary categories:

1. **Autotrophic Nutrition (*auto* = self; *trophos* = nourishment):**
   * Mode of nutrition in which organisms synthesize high-energy organic compounds (carbohydrates) from simple, low-energy inorganic raw materials (carbon dioxide and water) using radiant solar or chemical energy.
   * Organisms: Green plants, photosynthetic algae, cyanobacteria, and chemosynthetic bacteria.
   * Role in Ecosystem: Function as **primary producers**, generating the entire biospheric biomass.

2. **Heterotrophic Nutrition (*heteros* = other; *trophos* = nourishment):**
   * Mode of nutrition in which organisms cannot manufacture their own food and must obtain preformed organic nutrients by consuming other living beings or organic detritus.
   * Organisms: All animals, non-green parasitic plants (e.g., *Cuscuta* / dodder), fungi, and the vast majority of bacteria.
   * Role in Ecosystem: Function as **consumers** (herbivores, carnivores, omnivores) and **decomposers** (saprotrophs).

---

### 2. The Sun as the Ultimate Source of Biospheric Energy
* Green plants absorb only a tiny fraction of incoming solar radiation to drive the light reactions of photosynthesis.
* Solar photons are transduced into chemical bond energy stored in glucose and starch.
* Herbivores ingest autotrophic plant matter to extract this stored energy; carnivores subsequently feed on herbivores.
* Decomposers recycle energy and minerals from dead tissues across all trophic tiers.
* Thus, directly or indirectly, every biological metabolic flux and food web on Earth relies entirely on solar energy captured by autotrophs."""
    },
    {
        "module_id": "bio_ch4_mod_03",
        "title": "Photosynthesis: Biochemical Mechanics, Organelles & Stomatal Dynamics",
        "content": """### 1. Definition and Balanced Chemical Equation
Photosynthesis (*photo* = light; *synthesis* = putting together) is the physicochemical process by which green plant tissues synthesize hexose carbohydrates from carbon dioxide and water in the presence of sunlight captured by chlorophyll pigments, releasing molecular oxygen as a vital by-product.

$$\\text{6CO}_2 + \\text{12H}_2\\text{O} \\xrightarrow[\\text{Chlorophyll}]{\\text{Sunlight}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + \\text{6O}_2 + \\text{6H}_2\\text{O}$$

$$\\text{Carbon dioxide (from air)} + \\text{Water (from soil)} \\xrightarrow[\\text{Chlorophyll}]{\\text{Sunlight}} \\text{Glucose (Carbohydrate)} + \\text{Oxygen (Released to air)}$$

* **Immediate vs Storage Form:** The immediate primary monosaccharide formed is **glucose** ($\\text{C}_6\\text{H}_{12}\\text{O}_6$). For vascular transport, it is converted into soluble disaccharide **sucrose**. For long-term non-osmotic storage, it is polymerized into insoluble polysaccharide **starch**.
* **Food Factories of the Plant:** Leaves are the principal **food factories** or **kitchens** due to their broad surface area and dense concentration of chloroplast-rich mesophyll cells. Green stems and sepals also contribute to photosynthetic assimilation.

---

### 2. Experimental Proof of Oxygen Evolution (*Hydrilla* Experiment)
* An inverted glass funnel containing water plant twigs (*Hydrilla*, *Elodea*, or *Spirogyra*) submerged in a beaker of water is capped with a water-filled inverted test tube under bright illumination.
* Effervescent gas bubbles accumulate at the top by downward displacement of water.
* Introducing a glowing wooden splinter into the collected gas causes it to burst into flame, confirming the gas is concentrated **molecular oxygen** ($\\text{O}_2$).

---

### 3. Historical Pioneer: Rustom Hormusji Dastur (1896–1961)
* Distinguished Indian plant physiologist and Head of Botany at the Royal Institute of Science, Bombay (1921–1935).
* Conducted foundational research on the interplay of water availability, ambient temperature, and light spectral wavelengths on the kinetics of photosynthesis in tropical crops.

---

### 4. Chloroplast Ultrastructure (Competition Window)
Chloroplasts are specialized biconvex, semi-autonomous double-membrane-bound green plastids:
* **Double Membrane Envelope:** Outer and inner membranes enclosing an aqueous, proteinaceous matrix called the **stroma**.
* **Thylakoids & Grana:** The stroma contains organised disc-shaped flattened membranous sacs termed **thylakoids**, stacked like columns of coins into units called **grana** (singular: *granum*).
* **Stroma Lamellae:** Intergranal flat tubular membranes interconnecting thylakoid discs of adjacent grana.
* **Pigment Localization:** Green chlorophyll pigments and accessory carotenoids are embedded within the thylakoid lipid bilayer membranes (site of light-dependent photolysis and ATP/NADPH generation).
* **Stroma Enzymes & Autonomy:** The stroma harbors Rubisco and Calvin cycle enzymes for carbon fixation, along with 70S ribosomes and circular double-stranded chloroplast DNA (cpDNA).

---

### 5. Stomatal Architecture and Guard Cell Mechanics
* Leaves possess thousands of microscopic epidermal pores called **stomata** (singular: *stoma*), concentrated predominantly on the lower abaxial epidermis to reduce transpirational water loss.
* **Guard Cells:** Each stoma is flanked by two specialized, kidney/bean-shaped epidermal cells containing chloroplasts and differentially thickened cell walls (inner wall facing pore is thick and rigid; outer wall is thin and elastic).
* **Turgor Mechanism:**
  * In the presence of light and adequate water, guard cells absorb water by endosmosis, become turgid, and bow outward, pulling the stomatal aperture **open** to admit $\\text{CO}_2$.
  * In darkness or severe water deficit, guard cells lose water by exosmosis, become flaccid, and collapse inward, closing the stomatal pore to conserve moisture."""
    },
    {
        "module_id": "bio_ch4_mod_04",
        "title": "Limiting Factors, Ecological Adaptations & Starch Diagnostics",
        "content": """### 1. Environmental Factors Governing Photosynthetic Rate
1. **Light:**
   * *Intensity:* Photosynthetic rate increases linearly with increasing light intensity up to a light saturation point; extreme solar radiation bleaches and photo-oxidizes chlorophyll molecules, depressing the rate.
   * *Quality (Wavelength):* Chlorophyll absorbs photons maximally in the **blue** (430–450 nm) and **red** (640–660 nm) spectral regions. Photosynthetic rate is lowest or nil in **green light** (500–550 nm), which is reflected/transmitted.
2. **Temperature:**
   * Possesses a classic bell-shaped response curve with an optimum between **25°C and 40°C**.
   * Low temperatures (<10°C) reduce molecular kinetic energy and slow down enzymatic turnover; temperatures above 40°C cause thermal denaturation and inactivation of photosynthetic enzymes.
3. **Carbon Dioxide Concentration:**
   * $\\text{CO}_2$ is the chief substrate for carbohydrate synthesis. Ambient concentration (~0.04% or 400 ppm) is sub-saturating; elevating $\\text{CO}_2$ enhances assimilation up to an optimum, beyond which stomatal closure or cellular acidosis inhibits metabolism.
4. **Water:**
   * Less than 1% of water absorbed by roots is chemically split in photolysis; however, water status governs stomatal aperture. Water deficit triggers synthesis of abscisic acid, closing stomata, cutting off $\\text{CO}_2$ diffusion, and causing leaf wilting.

---

### 2. Anatomical Concepts & Adaptations
* **Phyllotaxy:** The geometric arrangement of leaves along a stem or branch (alternate, opposite, whorled) evolved to minimize mutual shading and optimize photon interception.
* **Coloured Foliage (*Coleus*, Crotons):** Foliage displaying red, purple, or brown colours contains abundant chlorophyll; the green colour is masked by dense accessory anthocyanin and carotenoid pigments.
* **Xerophytes (e.g., Cacti):** Foliage is reduced to protective spines to eliminate transpiration; green succulent stems assume photosynthetic functions (**phylloclade**).
* **Algal Colonies:** Microscopic and macroscopic aquatic algae contain chlorophyll within thylakoids and carry out substantial autotrophic carbon fixation in aquatic biomes.

---

### 3. Diagnostic Chemical Assays
* **Iodine Starch Test:**
  1. Boil leaf in water for 5–10 min: Inactivates all metabolic enzymes, terminates life processes, and permeabilizes plasma membranes.
  2. Boil leaf in ethanol over a water bath: Decolorizes the leaf by dissolving and extracting chlorophyll into ethanol (ethanol is volatile/flammable; never heated directly).
  3. Rinse in warm water: Softens the brittle bleached leaf tissue.
  4. Flood with iodine solution: Starch binds iodine to produce an intense **blue-black** polyiodide complex. Absence of starch yields a pale **yellow-brown** hue.
* **Moll’s Half-Leaf Experiment (Proving $\\text{CO}_2$ is Essential):**
  * Destarched leaf is split so that one half is sealed in a flask containing caustic soda / potassium hydroxide ($\\text{KOH}$), which absorbs all ambient $\\text{CO}_2$.
  * The exposed half outside receives natural atmospheric $\\text{CO}_2$.
  * Following solar exposure and iodine testing, only the exposed portion turns blue-black; the enclosed portion remains yellow-brown, conclusively proving that $\\text{CO}_2$ is indispensable for photosynthesis."""
    },
    {
        "module_id": "bio_ch4_mod_05",
        "title": "Vascular Transport Architecture: Xylem Ascent vs Phloem Translocation",
        "content": """### 1. The Plant Vascular Network
Higher plants possess a dedicated internal conducting network called the **vascular system**, organized into specialized complex permanent tissues:

1. **Xylem (Water and Mineral Conducting Tissue):**
   * **Function:** Transports water and dissolved mineral ions absorbed by root epidermal hairs upward through roots and stems to photosynthetic leaves (**ascent of sap**).
   * **Directionality:** Exclusively **unidirectional** (upward from roots $\\rightarrow$ aerial organs).
   * **Constituent Cell Types:**
     * *Tracheids:* Elongated, lignified, tapering dead cells with pitted walls.
     * *Xylem Vessels:* Long continuous cylindrical conduits formed of dead, perforated tube-like vessel elements joined end-to-end.
     * *Xylem Fibres:* Highly thickened, lignified dead sclerenchyma cells providing mechanical rigidity.
     * *Xylem Parenchyma:* The only **living** component; stores starch and facilitates radial water conduction.
   * **Driving Forces:** Driven by capillary action, root osmotic pressure, and predominantly transpirational negative tension (pull) created by stomatal evaporation.

2. **Phloem (Photoassimilate Translocating Tissue):**
   * **Function:** Transports soluble organic photosynthates (sucrose, amino acids) synthesized in leaves to all non-photosynthetic sink organs (roots, growing shoot apices, fruits, tubers) via **translocation**.
   * **Directionality:** **Bidirectional** (upward to developing shoot buds, flowers, and fruits; downward to root systems and underground storage tubers).
   * **Constituent Cell Types:**
     * *Sieve Tubes:* Long, slender conducting tubes composed of living, enucleated sieve tube elements with porous end walls called sieve plates.
     * *Companion Cells:* Specialized parenchymatous living sister cells packed with mitochondria and nuclei that regulate sieve tube metabolic transport.
     * *Phloem Parenchyma:* Living cells involved in food storage and lateral diffusion.
     * *Phloem Fibres (Bast fibres):* Dead sclerenchymatous elements providing mechanical support (e.g., jute, flax).

---

### 2. Experimental Verification of Xylem Transport (Balsam Twig Assay)
* A tender herbaceous leafy shoot (e.g., balsam) is placed in a tumbler containing water stained with red eosin dye or red ink and kept in sunlight.
* Within hours, leaf venation, petioles, and flower petals develop distinct red lines.
* Microscopic examination of stem transverse cross-sections reveals that only the lumen and lignified secondary walls of xylem vessels are stained red, verifying that xylem serves as the conduit for water and mineral ascent."""
    },
    {
        "module_id": "bio_ch4_mod_06",
        "title": "Cellular Respiration in Plants & Diurnal Gas Exchange",
        "content": """### 1. Biochemical Nature of Plant Respiration
Plants undergo **aerobic cellular respiration** continuously (24 hours a day, day and night) across every living tissue:
$$\\text{C}_6\\text{H}_{12}\\text{O}_6 + \\text{6O}_2 \\rightarrow \\text{6CO}_2 + \\text{6H}_2\\text{O} + \\text{Energy (38 ATP)}$$
In pure Unicode notation:
C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy (38 ATP)

* Respiration is a **catabolic** process that breaks down stored hexose sugars to synthesize ATP needed for active ion uptake, protein synthesis, cell division, and protoplasmic maintenance.

---

### 2. Specialized Plant Respiratory Organs
Unlike animals, plants lack a centralized circulatory or respiratory pump; each organ takes care of its own gaseous exchange requirements via short-distance diffusion:
* **Foliage (Leaves):** Oxygen diffuses in and CO₂ diffuses out through stomatal pores into extensive spongy mesophyll intercellular air spaces.
* **Woody Stems and Branches:** Impermeable dead bark contains raised, lens-shaped porous loose cell openings called **lenticels** that facilitate gas exchange between internal tissues and the atmosphere.
* **Root Systems:** Thin-walled epidermal root hairs absorb oxygen dissolved within capillary soil air pockets.
  * *Hazard of Waterlogging:* Overwatering submerges soil, expelling air pockets. Roots suffocate from hypoxia, fail to generate ATP, and rot due to anaerobic decay.
* **Halophytic Mangroves:** Growing in saline, oxygen-deficient, waterlogged tidal marshes, mangrove species (e.g., *Rhizophora*) produce specialized negative-geotropic upright aerial breathing roots termed **pneumatophores** studded with lenticels.
* **Germinating Seeds:** Exhibit massive metabolic activation, rapidly consuming oxygen to oxidize endosperm reserves and generate thermal and biochemical energy.

---

### 3. Diurnal Comparison: Photosynthesis vs Respiration
* **During Daytime (Light):**
  * Both photosynthesis and respiration occur simultaneously.
  * The rate of photosynthesis is 10 to 20 times faster than the rate of respiration.
  * All respiratory CO₂ is immediately consumed internally by chloroplasts, and surplus O₂ is evolved into the atmosphere. Net gaseous output: **Oxygen release**.
* **During Nighttime (Darkness):**
  * Photosynthesis ceases completely due to absence of light.
  * Aerobic respiration continues unabated.
  * Plants absorb O₂ from ambient air and release CO₂.
  * *Health Implication:* Sleeping directly under dense tree canopies at night exposes individuals to a locally elevated CO₂ and reduced O₂ microenvironment.
* **Compensation Point:** The specific light intensity (typically at dawn and dusk) where the rate of photosynthetic CO₂ uptake exactly equals the rate of respiratory CO₂ release, resulting in zero net gas exchange."""
    },
    {
        "module_id": "bio_ch4_mod_07",
        "title": "Comprehensive Contrast: Photosynthesis vs Respiration",
        "content": """### Structural and Functional Comparison

| Feature | Photosynthesis | Cellular Respiration |
| :--- | :--- | :--- |
| **Metabolic Nature** | Anabolic (constructive synthesis of complex organic matter) | Catabolic (destructive oxidative breakdown of organic molecules) |
| **Cellular Site** | Confined to chloroplasts of chlorophyllous green cells | Occurs in cytoplasm and mitochondria of all living cells |
| **Light Dependency** | Strictly light-dependent; active only in the presence of photons | Light-independent; operates continuously 24/7 (day and night) |
| **Raw Materials** | Inorganic CO₂ and H₂O | Organic Glucose (C₆H₁₂O₆) and Oxygen (O₂) |
| **End Products** | Glucose (C₆H₁₂O₆), Oxygen (O₂), and water | Carbon dioxide (CO₂), Water (H₂O), and ATP energy |
| **Energy Transformation** | Traps radiant solar energy → converts to chemical bond energy | Releases chemical bond energy → converts to metabolic ATP and heat |
| **Biomass Impact** | Increases total dry weight of the plant | Decreases total dry weight of the plant |
| **Gas Exchange** | Net uptake of CO₂ and net release of O₂ | Net uptake of O₂ and net release of CO₂ |
| **Ecological Balance** | Purifies air; provides global base food supply and atmospheric O₂ | Recycles carbon into atmosphere; powers vital cell maintenance |"""
    }
]

# Import the 191 assessment items
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from build_biology_ch4_items import assessment_items

# Assemble dual-schema complete KB
full_kb = {
    **kb_metadata,
    "theory_summary": theory_modules,
    "questions": assessment_items,
    "assessment_items": assessment_items
}

# Generate Markdown Document
def generate_markdown(kb):
    md = []
    md.append(f"# {kb['subject']}: {kb['discipline']} - Chapter {kb['chapter_num']}: {kb['chapter_title']}\n")
    md.append(f"**Curriculum:** {kb['curriculum']} | **Version:** {kb['kb_version']} | **Source PDF:** `{kb['source_pdf']}`\n")
    md.append("## Executive Chapter Summary\n")
    md.append(f"{kb['summary']}\n")
    
    md.append("## Learning Outcomes\n")
    for lo in kb['learning_outcomes']:
        md.append(f"* {lo}")
    md.append("\n---\n")
    
    md.append("## Comprehensive Theory Frameworks\n")
    for mod in kb['theory_summary']:
        md.append(f"### {mod['title']}\n")
        md.append(f"{mod['content']}\n\n---\n")
        
    md.append("## Authoritative Question Repository & Assessment Items\n")
    md.append(f"Total Authoritative Assessment Items: **{len(kb['assessment_items'])}**\n")
    
    # Group items by source/type
    categories = [
        ("Textbook Illustrations", lambda x: x["source"] == "textbook_illustration"),
        ("Solved Examples", lambda x: x["source"] == "solved_example"),
        ("NCERT Section Exercises", lambda x: x["source"] == "ncert_exercise"),
        ("Level 1 Multiple Choice Questions", lambda x: x["source"] == "textbook_mcq_l1"),
        ("Level 2 Multiple Choice Questions", lambda x: x["source"] == "textbook_mcq_l2"),
        ("Level 3 HOTS & Competency MCQs", lambda x: x["source"] == "textbook_mcq_l3"),
        ("Fill in the Blanks", lambda x: x["source"] == "fill_in_the_blanks"),
        ("True or False", lambda x: x["source"] == "true_false"),
        ("Assertion & Reason", lambda x: x["source"] == "assertion_reason"),
        ("Very Short Answer Questions", lambda x: x["source"] == "very_short_answer"),
        ("Short Answer Questions", lambda x: x["source"] == "short_answer"),
        ("Long Answer Questions", lambda x: x["source"] == "long_answer"),
        ("Case-Based Comprehensive Problems", lambda x: x["source"] == "case_based")
    ]
    
    for cat_name, pred in categories:
        cat_items = [it for it in kb['assessment_items'] if pred(it)]
        if not cat_items:
            continue
        md.append(f"\n### {cat_name} ({len(cat_items)} Items)\n")
        for it in cat_items:
            md.append(f"#### Item ID: `{it['id']}` | Topic: {it['topic']} | Marks: {it['marks']}M | Difficulty: {it['difficulty'].capitalize()}")
            md.append(f"**Question:**\n{it['question']}\n")
            if "options" in it and it["options"]:
                md.append("**Options:**")
                for opt in it["options"]:
                    md.append(f"- {opt}")
                md.append("")
            md.append(f"**Answer:**\n{it['answer']}\n")
            md.append(f"**Pedagogical Explanation:**\n{it['explanation']}\n")
            if "diagram_slot" in it and it["diagram_slot"]:
                slot = it["diagram_slot"]
                md.append(f"> **Diagram Slot [Status: {slot['status']}]:** *{slot['source_hint']}* — {slot['description']}\n")
            md.append("---\n")
            
    return "\n".join(md)

# File Paths
kb_json_path = "KB Files/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.json"
kb_md_path = "KB Files/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.md"
prod_json_path = "knowledge_base/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.json"
prod_md_path = "knowledge_base/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.md"

# Serialize JSON
json_content = json.dumps(full_kb, indent=4, ensure_ascii=False)
with open(kb_json_path, "w", encoding="utf-8") as f:
    f.write(json_content)
with open(prod_json_path, "w", encoding="utf-8") as f:
    f.write(json_content)

# Serialize Markdown
md_content = generate_markdown(full_kb)
with open(kb_md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
with open(prod_md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"[SUCCESS] Wrote JSON to {kb_json_path} ({os.path.getsize(kb_json_path):,} bytes)")
print(f"[SUCCESS] Wrote MD to {kb_md_path} ({os.path.getsize(kb_md_path):,} bytes)")
print(f"[SUCCESS] Mirrored JSON to {prod_json_path} ({os.path.getsize(prod_json_path):,} bytes)")
print(f"[SUCCESS] Mirrored MD to {prod_md_path} ({os.path.getsize(prod_md_path):,} bytes)")
print(f"Successfully compiled Class 7 Biology Chapter 4 KB with {len(assessment_items)} items!")
