# -*- coding: utf-8 -*-
"""
Authoritative Tab generator functions for Biology Chapter 4: "Life Processes in Plants".
All questions, theory, drills, match arenas, traps, and video hubs.
"""
import re
import json

def esc(text):
    if text is None:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def check_mcq_correct(ans, opt, idx):
    opt_letter = chr(65 + idx)
    ans_str = str(ans).strip().lower()
    opt_str = str(opt).strip().lower()
    
    if ans_str == opt_str:
        return True
    if ans_str == opt_letter.lower():
        return True
    if ans_str == f'({opt_letter.lower()})':
        return True
    if ans_str.startswith(f'({opt_letter.lower()})') or ans_str.startswith(f'{opt_letter.lower()}.') or ans_str.startswith(f'{opt_letter.lower()})'):
        return True
    clean_ans = re.sub(r'^\([a-dA-D]\)\s*|^[a-dA-D][\.\)]\s*', '', str(ans)).strip().lower()
    clean_opt = re.sub(r'^\([a-dA-D]\)\s*|^[a-dA-D][\.\)]\s*', '', str(opt)).strip().lower()
    if clean_ans and clean_ans == clean_opt:
        return True
    return False

def clean_option_text(opt):
    return re.sub(r'^\([a-dA-D]\)\s*|^[a-dA-D][\.\)]\s*', '', str(opt)).strip()

def build_tab_primer():
    return """<!-- ========================================== -->
<!-- 1. LAUNCHPAD PRIMER (tabPrimer)            -->
<!-- ========================================== -->
<div id="tabPrimer" class="tab-pane active space-y-8 animate-fadeIn">
  <!-- Hero Banner -->
  <div class="relative overflow-hidden p-6 md:p-10 rounded-3xl bg-gradient-to-br from-emerald-950/80 via-slate-900 to-teal-950/80 border border-emerald-500/30 shadow-2xl">
    <div class="absolute -top-24 -right-24 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
    <div class="relative z-10 space-y-4">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-semibold uppercase tracking-wider">
        <i class="fas fa-leaf"></i> Plant Physiology • Science Biology
      </div>
      <h1 class="text-3xl md:text-5xl font-black text-white tracking-tight font-heading">
        Life Processes in Plants
      </h1>
      <p class="text-slate-300 text-sm md:text-base leading-relaxed max-w-3xl">
        The master biological blueprint of terrestrial flora: vegetative and reproductive phases of growth, 
        solar energy conversion through autotrophic photosynthesis, chloroplast ultrastructure &amp; stomatal guard cell mechanics, 
        limiting factor kinetics, unidirectional xylem sap ascent vs. bidirectional phloem translocation, 
        and plant cellular respiration across organs and diurnal day/night cycles.
      </p>

      <!-- Key Metrics Strip -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-slate-800/80">
        <div class="p-3.5 rounded-2xl bg-slate-950/60 border border-slate-800 text-center">
          <div class="text-xs uppercase text-slate-400 font-bold">Photosynthesis</div>
          <div class="text-xl md:text-2xl font-black text-emerald-400 font-mono mt-0.5">6CO₂ + 12H₂O</div>
          <div class="text-[10px] text-slate-500 font-mono">Hexose Sugar + O₂ Yield</div>
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-950/60 border border-slate-800 text-center">
          <div class="text-xs uppercase text-slate-400 font-bold">Transport System</div>
          <div class="text-xl md:text-2xl font-black text-teal-400 font-mono mt-0.5">Xylem &amp; Phloem</div>
          <div class="text-[10px] text-slate-500 font-mono">Unidirectional vs Bidirectional</div>
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-950/60 border border-slate-800 text-center">
          <div class="text-xs uppercase text-slate-400 font-bold">Plant Respiration</div>
          <div class="text-xl md:text-2xl font-black text-cyan-400 font-mono mt-0.5">24 Hours / Day</div>
          <div class="text-[10px] text-slate-500 font-mono">Stomata, Lenticels, Roots</div>
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-950/60 border border-slate-800 text-center">
          <div class="text-xs uppercase text-slate-400 font-bold">Authoritative Bank</div>
          <div class="text-xl md:text-2xl font-black text-amber-400 font-mono mt-0.5">191 Items</div>
          <div class="text-[10px] text-slate-500 font-mono">100% Solved &amp; Verified</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Foundational Roadmap Grid -->
  <div class="space-y-4">
    <div class="flex items-center gap-2 text-white font-bold text-lg">
      <i class="fas fa-compass text-emerald-400"></i>
      <h3>Foundational Learning Roadmap</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div onclick="switchTab('tabGrowth')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-emerald-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-seedling"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-emerald-300 transition-colors">1. Plant Growth &amp; Ancient Insights</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Vegetative vs reproductive phases, Pots A/B/C sunlight &amp; moisture proofs, and ancient <em>Vrikshayurveda</em> herbal taxonomy.
        </p>
      </div>

      <div onclick="switchTab('tabNutrition')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-teal-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-teal-500/20 text-teal-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-sun"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-teal-300 transition-colors">2. Nutrition &amp; Solar Spectrum</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Autotrophic vs heterotrophic modes, Sun as ultimate energy origin, and chlorophyll blue/red absorption vs green reflection.
        </p>
      </div>

      <div onclick="switchTab('tabPhotosynthesis')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-cyan-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-microscope"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-cyan-300 transition-colors">3. Photosynthesis &amp; Stomata</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Balanced biochemical equation, chloroplast double membrane &amp; thylakoids, and guard cell turgor swelling mechanics.
        </p>
      </div>

      <div onclick="switchTab('tabFactors')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-amber-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-flask"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-amber-300 transition-colors">4. Limiting Factors &amp; Starch Assay</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Light, temperature bell-curve, CO₂ saturation, Moll's half-leaf KOH experiment, and variegated <em>Coleus</em> masked pigments.
        </p>
      </div>

      <div onclick="switchTab('tabTransport')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-blue-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-water"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-blue-300 transition-colors">5. Vascular Transport Architecture</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Unidirectional xylem ascent of sap, transpirational suction pull, and bidirectional phloem sucrose translocation.
        </p>
      </div>

      <div onclick="switchTab('tabRespiration')" class="p-5 rounded-2xl bg-slate-900/80 border border-slate-800 hover:border-purple-500/50 hover:bg-slate-800/50 transition-all cursor-pointer group space-y-2">
        <div class="w-10 h-10 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center text-lg group-hover:scale-110 transition-transform">
          <i class="fas fa-wind"></i>
        </div>
        <div class="text-base font-bold text-white group-hover:text-purple-300 transition-colors">6. Cellular Respiration &amp; Day/Night</div>
        <p class="text-xs text-slate-400 leading-relaxed">
          Stomatal, lenticellar, and pneumatophore gas exchange, diurnal balance, and the dawn/dusk Compensation Point.
        </p>
      </div>
    </div>
  </div>
</div>
"""

def build_tab_growth():
    return """<!-- ========================================== -->
<!-- 2. PLANT GROWTH & ANCIENT INSIGHTS (tabGrowth) -->
<!-- ========================================== -->
<div id="tabGrowth" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-lg">
      <i class="fas fa-seedling"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Plant Growth Dynamics &amp; Ancient Botanical Insights</h2>
      <p class="text-xs text-slate-400">Vegetative versus reproductive phases, Pots A/B/C abiotic proofs, and Vrikshayurveda heritage</p>
    </div>
  </div>

  <!-- Dynamics of Plant Growth -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-emerald-500/30 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Physiological Transitions</span>
      <h3 class="text-xl font-bold text-white font-heading">The Dual Phases of Plant Development</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      <div class="p-5 rounded-2xl bg-slate-950/80 border border-emerald-900/40 space-y-3">
        <div class="flex items-center gap-2 text-emerald-400 font-bold text-base">
          <i class="fas fa-leaf"></i> 1. Vegetative Growth Phase
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Initiates at seed germination when the radical anchors into soil and plumule breaks through the surface. 
          Marked by rapid stem elongation, node and internode differentiation, vigorous leaf expansion, and lateral branching. 
          In woody perennials, secondary meristems (vascular cambium) divide continuously, increasing trunk girth with annual growth rings.
        </p>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
          <strong class="text-white">Primary Focus:</strong> Building cellular infrastructure, expanding photosynthetic leaf area, and accumulating energy stores.
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-950/80 border border-teal-900/40 space-y-3">
        <div class="flex items-center gap-2 text-teal-400 font-bold text-base">
          <i class="fas fa-flower"></i> 2. Reproductive Growth Phase
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Triggered by photoperiodic signals and hormonal shifts (florigen). Apical meristems transition into floral buds. 
          Encompasses flower opening (anthesis), pollen transfer (pollination), ovule fertilization, embryo packaging into seeds, 
          and ovarian tissue ripening into protective nutrient-rich fruits.
        </p>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
          <strong class="text-white">Primary Focus:</strong> Species genetic preservation, seed dispersal adaptations, and lineage propagation.
        </div>
      </div>
    </div>
  </div>

  <!-- Pots A, B, C Empirical Proof -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-1 rounded-xl bg-amber-500/20 text-amber-300 font-mono text-xs font-bold">Empirical Verification</span>
        <h3 class="text-xl font-bold text-white font-heading">The Three-Pot Abiotic Factor Experiment (Pots A, B, C)</h3>
      </div>
      <span class="text-xs font-mono text-slate-400">Investigation Duration: 14 Days</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <!-- Pot A -->
      <div class="p-5 rounded-2xl bg-emerald-950/30 border border-emerald-500/40 space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-emerald-500/20 text-emerald-300 font-mono">POT A</span>
          <span class="text-emerald-400 text-xs font-semibold"><i class="fas fa-check-circle"></i> Optimal Growth</span>
        </div>
        <div class="text-xs text-slate-300 space-y-1.5">
          <div><strong class="text-slate-400">Conditions:</strong> Direct Sunlight + Adequate Moisture</div>
          <div><strong class="text-slate-400">Height:</strong> 30 cm → 38 cm (+8 cm)</div>
          <div><strong class="text-slate-400">Foliage Count:</strong> 9 leaves → 13 leaves</div>
          <div><strong class="text-slate-400">Leaf Condition:</strong> Vibrant, turgid, lush dark green</div>
        </div>
        <p class="text-[11px] text-emerald-300 bg-emerald-950/60 p-2.5 rounded-xl border border-emerald-800/40 leading-relaxed">
          <strong>Conclusion:</strong> Synergistic presence of solar energy and water drives full rate of photosynthesis and cell division.
        </p>
      </div>

      <!-- Pot B -->
      <div class="p-5 rounded-2xl bg-rose-950/30 border border-rose-500/40 space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-rose-500/20 text-rose-300 font-mono">POT B</span>
          <span class="text-rose-400 text-xs font-semibold"><i class="fas fa-times-circle"></i> Water Deprived</span>
        </div>
        <div class="text-xs text-slate-300 space-y-1.5">
          <div><strong class="text-slate-400">Conditions:</strong> Direct Sunlight + Zero Water</div>
          <div><strong class="text-slate-400">Height:</strong> 28 cm → 25 cm (-3 cm wilting)</div>
          <div><strong class="text-slate-400">Foliage Count:</strong> 8 leaves → 3 leaves</div>
          <div><strong class="text-slate-400">Leaf Condition:</strong> Flaccid, shrivelled, dry yellow</div>
        </div>
        <p class="text-[11px] text-rose-300 bg-rose-950/60 p-2.5 rounded-xl border border-rose-800/40 leading-relaxed">
          <strong>Conclusion:</strong> Without water, cells lose turgor pressure, stomata close, and tissue dehydrates into permanent wilting.
        </p>
      </div>

      <!-- Pot C -->
      <div class="p-5 rounded-2xl bg-amber-950/30 border border-amber-500/40 space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2 py-0.5 rounded text-xs font-bold bg-amber-500/20 text-amber-300 font-mono">POT C</span>
          <span class="text-amber-400 text-xs font-semibold"><i class="fas fa-exclamation-triangle"></i> Light Deprived</span>
        </div>
        <div class="text-xs text-slate-300 space-y-1.5">
          <div><strong class="text-slate-400">Conditions:</strong> Dark Room + Adequate Moisture</div>
          <div><strong class="text-slate-400">Height:</strong> 31 cm → 30 cm (Stagnant)</div>
          <div><strong class="text-slate-400">Foliage Count:</strong> 10 leaves → 7 leaves</div>
          <div><strong class="text-slate-400">Leaf Condition:</strong> Pale greenish-yellow (Etiolation)</div>
        </div>
        <p class="text-[11px] text-amber-300 bg-amber-950/60 p-2.5 rounded-xl border border-amber-800/40 leading-relaxed">
          <strong>Conclusion:</strong> Chlorophyll biosynthesis strictly requires light. In darkness, photosynthesis halts, leading to chlorosis.
        </p>
      </div>
    </div>
  </div>

  <!-- Ancient Botanical Insights -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-mono text-xs font-bold">Indian Scientific Heritage</span>
      <h3 class="text-xl font-bold text-white font-heading">Vrikshayurveda &amp; Ancient Botanical Wisdom</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-purple-300 text-sm">Surapala's Vrikshayurveda (~10th Century CE):</strong>
        <p class="text-slate-300 leading-relaxed">
          One of ancient India's foundational treatises dedicated exclusively to arbori-horticulture. 
          Surapala systematically codified seed preservation techniques, soil selection by smell and texture, 
          grafting methods, organic fertilizers (*Kunapajala* concoctions), and plant disease diagnosis based on foliar discoloration.
        </p>
      </div>
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-cyan-300 text-sm">Sage Parashara's Vrikshashastra:</strong>
        <p class="text-slate-300 leading-relaxed">
          Pre-Christian era classification of plants based on morphology into 4 major divisions:
          <strong>Vanaspati</strong> (Trees bearing fruits without visible flowers like Fig/Banyan),
          <strong>Vanaspatya</strong> (Trees bearing both distinct flowers and fruits like Mango),
          <strong>Oshadhi</strong> (Annual herbs that wither away after bearing seeds), and
          <strong>Virudh</strong> (Climbers, creepers, and spreading twinning shrubs).
        </p>
      </div>
    </div>
  </div>
</div>
"""

def build_tab_nutrition():
    return """<!-- ========================================== -->
<!-- 3. MODES OF NUTRITION & SOLAR SPECTRUM     -->
<!-- ========================================== -->
<div id="tabNutrition" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-teal-500/20 text-teal-400 flex items-center justify-center text-lg">
      <i class="fas fa-sun"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Modes of Nutrition &amp; The Sun as Ultimate Energy Source</h2>
      <p class="text-xs text-slate-400">Autotrophs versus heterotrophs, solar spectrum energetics, and chlorophyll absorption kinetics</p>
    </div>
  </div>

  <!-- Nutrition Modes Comparison -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-teal-500/30 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-teal-500/20 text-teal-300 font-mono text-xs font-bold">Nutritional Taxonomy</span>
      <h3 class="text-xl font-bold text-white font-heading">Autotrophic vs Heterotrophic Nutrition</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm">
      <div class="p-5 rounded-2xl bg-slate-950 border border-emerald-900/40 space-y-3">
        <div class="text-emerald-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-leaf"></i> Autotrophic Nutrition (Auto = Self; Trophos = Feeding)
        </div>
        <p class="text-slate-300 leading-relaxed">
          Mode of nutrition where organisms synthesize high-energy organic macromolecules (carbohydrates) 
          directly from simple inorganic raw materials (CO₂ and H₂O) utilizing light energy. 
          Green plants, algae, phytoplankton, and cyanobacteria are autotrophs. Because they fabricate all biological energy on earth, they are designated as <strong>producers</strong>.
        </p>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-emerald-300 font-mono">
          Energy Conversion: Radiant Solar Energy → Chemical Bond Energy (Glucose)
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-950 border border-amber-900/40 space-y-3">
        <div class="text-amber-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-utensils"></i> Heterotrophic Nutrition (Heteros = Other; Trophos = Feeding)
        </div>
        <p class="text-slate-300 leading-relaxed">
          Mode of nutrition where organisms cannot synthesize their own food and must consume pre-formed organic matter. 
          Encompasses herbivores, carnivores, omnivores, saprophytes (fungi), and parasites (*Cuscuta* / Dodder). 
          All animals, fungi, and non-green plants are heterotrophs, serving as primary, secondary, or tertiary <strong>consumers</strong>.
        </p>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-amber-300 font-mono">
          Dependence: Directly (Herbivores) or Indirectly (Carnivores) on Producers
        </div>
      </div>
    </div>
  </div>

  <!-- The Sun as the Ultimate Energy Origin -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-amber-500/20 text-amber-300 font-mono text-xs font-bold">Cosmic Bioenergetics</span>
      <h3 class="text-xl font-bold text-white font-heading">Why The Sun is the Ultimate Source of Energy for All Life</h3>
    </div>
    <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 text-xs md:text-sm text-slate-300 leading-relaxed space-y-3">
      <p>
        Nuclear fusion in the core of the Sun releases electromagnetic radiation across wide spectra. 
        Only green plants and other photosynthetic autotrophs possess the biochemical machinery (chlorophyll pigments) 
        capable of capturing this electromagnetic radiation and storing it in covalent carbon-carbon chemical bonds of hexose sugars.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
          <strong class="text-amber-400">1. Herbivore Sustenance:</strong>
          <p class="text-slate-400 text-xs mt-1">Cows, deer, and caterpillars consume plant biomass directly to obtain glucose and amino acids.</p>
        </div>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
          <strong class="text-rose-400">2. Carnivore Energy:</strong>
          <p class="text-slate-400 text-xs mt-1">Lions and hawks consume herbivores; the energy inside their prey originates 100% from solar-driven plant photosynthesis.</p>
        </div>
        <div class="p-3 rounded-xl bg-slate-900 border border-slate-800">
          <strong class="text-cyan-400">3. Fossil Fuels:</strong>
          <p class="text-slate-400 text-xs mt-1">Coal, petroleum, and natural gas are ancient plant and plankton remains buried millions of years ago—stored ancient solar energy!</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Absorption Spectrum of Chlorophyll -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-sky-500/20 text-sky-300 font-mono text-xs font-bold">Spectroscopy</span>
      <h3 class="text-xl font-bold text-white font-heading">Chlorophyll Absorption Spectrum &amp; Why Leaves Look Green</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-sky-300 text-sm">Wavelength Selective Absorption:</strong>
        <p class="text-slate-300 leading-relaxed">
          Visible solar light spans 400 nm to 700 nm. Chlorophyll <em>a</em> and <em>b</em> absorb light maximally in two distinct regions:
          <br>• <strong>Blue-Violet Region (~430–450 nm):</strong> High energy absorption.
          <br>• <strong>Red Region (~650–680 nm):</strong> Highly efficient photochemical absorption.
          <br>Photosynthetic activity reaches its peak in these two spectrum windows.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-emerald-400 text-sm">The Green Reflection Principle:</strong>
        <p class="text-slate-300 leading-relaxed">
          Chlorophyll molecules have virtually zero absorption in the <strong>green-yellow spectrum (~500–550 nm)</strong>. 
          Green wavelengths are neither absorbed nor utilized; instead, they are <strong>transmitted and reflected back</strong> to our eyes. 
          Consequently, healthy foliage appears bright vibrant green to human observers!
        </p>
      </div>
    </div>
  </div>
</div>
"""

def build_tab_photosynthesis():
    return """<!-- ========================================== -->
<!-- 4. PHOTOSYNTHESIS, CHLOROPLASTS & STOMATA   -->
<!-- ========================================== -->
<div id="tabPhotosynthesis" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-lg">
      <i class="fas fa-microscope"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Photosynthesis: Biochemical Mechanics, Organelles &amp; Stomatal Dynamics</h2>
      <p class="text-xs text-slate-400">Balanced chemical equation, chloroplast ultrastructure, and stomatal turgor opening/closing</p>
    </div>
  </div>

  <!-- Balanced Equation Card -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-cyan-500/30 shadow-xl space-y-4">
    <div class="flex items-center justify-between">
      <span class="px-2.5 py-1 rounded-xl bg-cyan-500/20 text-cyan-300 font-mono text-xs font-bold">Biochemical Core</span>
      <span class="text-xs text-slate-400 font-mono">Endothermic Redox Process</span>
    </div>
    <div class="p-4 rounded-2xl bg-slate-950 border border-cyan-900/40 text-center space-y-2">
      <div class="text-xs uppercase text-slate-400 font-bold tracking-wider">The Balanced Photosynthesis Reaction</div>
      <div class="text-lg md:text-2xl font-black text-cyan-300 font-mono tracking-wide">
        6CO₂ + 12H₂O 
        <span class="text-xs text-slate-400 inline-block px-2">──[ Sunlight / Chlorophyll ]──▶</span> 
        C₆H₁₂O₆ + 6O₂↑ + 6H₂O
      </div>
      <div class="text-xs text-slate-400 max-w-2xl mx-auto pt-1 leading-relaxed">
        Carbon dioxide is reduced into glucose carbohydrate, while water is photolyzed (split by light energy), releasing molecular oxygen gas into the atmosphere as a vital byproduct.
      </div>
    </div>
  </div>

  <!-- Chloroplast Ultrastructure -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Organelle Architecture</span>
      <h3 class="text-xl font-bold text-white font-heading">The Chloroplast: Photosynthetic Kitchen of the Plant Cell</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-emerald-400 text-sm">1. Double Membrane Envelope:</strong>
        <p class="text-slate-300 leading-relaxed">
          Composed of an outer permeable membrane and an inner selectively permeable membrane enclosing the intermembrane space. Shields internal enzymatic machinery.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-teal-400 text-sm">2. Thylakoid Discs:</strong>
        <p class="text-slate-300 leading-relaxed">
          Flattened, microscopic membranous sacs whose phospholipid bilayers embed photosystem pigments (chlorophyll <em>a</em>, <em>b</em>, carotenoids). Site of the Light Reactions.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-cyan-400 text-sm">3. Grana &amp; Lamellae:</strong>
        <p class="text-slate-300 leading-relaxed">
          Thylakoids stacked neatly like piles of coins form <strong>Grana</strong> (singular: Granum). Grana stacks are interconnected by membranous channels called <strong>Stroma Lamellae</strong> (frets).
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-amber-400 text-sm">4. Hydrophilic Stroma:</strong>
        <p class="text-slate-300 leading-relaxed">
          The protein-rich aqueous matrix bathing the grana. Contains carbon-fixing enzymes (RuBisCO), circular chloroplast DNA (cpDNA), and 70S ribosomes. Site of Dark Reactions (Calvin cycle).
        </p>
      </div>
    </div>
  </div>

  <!-- Stomatal Guard Cell Mechanics -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-mono text-xs font-bold">Physiological Valve</span>
      <h3 class="text-xl font-bold text-white font-heading">Stomatal Anatomy &amp; Turgor Regulation</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm">
      <div class="p-5 rounded-2xl bg-slate-950 border border-emerald-900/40 space-y-3">
        <div class="text-emerald-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-expand-alt"></i> Stoma Open (Daytime / Turgid State)
        </div>
        <p class="text-slate-300 leading-relaxed">
          During daylight, active potassium ion (K⁺) uptake increases solute concentration inside guard cells. 
          Water enters guard cells from surrounding epidermal cells via <strong>endosmosis</strong>. 
          Guard cells swell and become <strong>turgid</strong>. 
          Because their inner cell walls facing the pore are thick and inelastic, while outer walls are thin and elastic, 
          the swelling causes guard cells to curve outward like two bowed crescents, pulling the <strong>stomatal aperture open</strong>!
        </p>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-emerald-300 font-mono">
          Result: CO₂ diffuses in freely for photosynthesis; transpiration occurs.
        </div>
      </div>

      <div class="p-5 rounded-2xl bg-slate-950 border border-rose-900/40 space-y-3">
        <div class="text-rose-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-compress-alt"></i> Stoma Closed (Night / Flaccid State)
        </div>
        <p class="text-slate-300 leading-relaxed">
          At night or during severe drought, K⁺ ions exit guard cells. 
          Water exits guard cells into adjacent subsidiary cells via <strong>exosmosis</strong>. 
          Guard cells lose internal turgor pressure and become <strong>flaccid</strong> (limp). 
          Their elastic outer walls relax and recoil, causing the inner thick walls to straighten and touch, 
          completely <strong>sealing the stomatal aperture</strong>!
        </p>
        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-rose-300 font-mono">
          Result: Conserves water; prevents excessive transpirational dehydration.
        </div>
      </div>
    </div>
  </div>

  <!-- Scientist Spotlight -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-sky-500/20 text-sky-300 font-mono text-xs font-bold">Scientist Spotlight</span>
      <h3 class="text-xl font-bold text-white font-heading">Rustom Hormusji Dastur (1896–1961)</h3>
    </div>
    <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
      Eminent Indian plant physiologist and founder of modern botanical physiology in India. 
      Professor Dastur conducted pioneering investigations into the relationship between water content, 
      foliar energy absorption, and the photochemical efficiency of chlorophyll pigments in tropical crops (cotton and rice). 
      His rigorous empirical methodologies placed Indian plant physiology on the international scientific map.
    </p>
  </div>
</div>
"""

def build_tab_factors():
    return """<!-- ========================================== -->
<!-- 5. LIMITING FACTORS & STARCH DIAGNOSTICS   -->
<!-- ========================================== -->
<div id="tabFactors" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-lg">
      <i class="fas fa-flask"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Limiting Factors, Ecological Adaptations &amp; Starch Diagnostics</h2>
      <p class="text-xs text-slate-400">Blackman's Law, masked foliar pigments in Coleus, iodine starch assay, and Moll's half-leaf proof</p>
    </div>
  </div>

  <!-- Four Limiting Factors -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-amber-500/30 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-amber-500/20 text-amber-300 font-mono text-xs font-bold">Environmental Kinetics</span>
      <h3 class="text-xl font-bold text-white font-heading">Four Primary Factors Governing Photosynthesis Rate</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-amber-400">1. Light Intensity &amp; Quality:</strong>
        <p class="text-slate-300 leading-relaxed">
          Rate increases linearly with intensity up to light saturation point. Extreme scorching sunlight causes <strong>photo-oxidation</strong> (solarization), bleaching chlorophyll. Photochemically active in blue and red; zero in green.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-rose-400">2. Temperature &amp; Enzyme Denaturation:</strong>
        <p class="text-slate-300 leading-relaxed">
          Follows an inverted bell-curve. Optimum temperature is <strong>25°C to 35°C</strong>. Below 10°C, enzymes become sluggish. Above 40°C–45°C, heat permanently <strong>denatures catalytic enzymes</strong> (RuBisCO), crashing the rate to zero.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-cyan-400">3. Carbon Dioxide Concentration:</strong>
        <p class="text-slate-300 leading-relaxed">
          Atmospheric CO₂ is ~0.04% (400 ppm). Increasing CO₂ up to 0.05% accelerates photosynthesis substantially (utilized in commercial greenhouse farming). Beyond 0.1%, stomata constrict, becoming toxic.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-blue-400">4. Water Availability:</strong>
        <p class="text-slate-300 leading-relaxed">
          Serves as electron donor in photolysis. Water stress induces guard cell flaccidity, triggering stomatal closure, choking CO₂ intake, and causing leaf wilting that reduces photosynthetic surface area.
        </p>
      </div>
    </div>
  </div>

  <!-- Masked Foliar Pigments in Coleus -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-rose-500/20 text-rose-300 font-mono text-xs font-bold">Foliar Variation</span>
      <h3 class="text-xl font-bold text-white font-heading">Masked Foliar Pigments in Variegated Leaves (Coleus &amp; Croton)</h3>
    </div>
    <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 text-xs md:text-sm text-slate-300 leading-relaxed space-y-2">
      <p>
        Students frequently assume that red, purple, or dark brown leaves (e.g., <em>Coleus</em>, ornamental <em>Croton</em>, or red amaranth) cannot perform photosynthesis because they do not appear green. 
        <strong>This is a classic exam trap!</strong>
      </p>
      <div class="p-3.5 rounded-xl bg-slate-900 border border-rose-900/40 text-xs text-rose-300 space-y-1">
        <strong>The Scientific Fact:</strong> Green chlorophyll pigments ARE present in large quantities inside these leaves. However, they are visually masked and overshadowed by dense concentrations of accessory pigments—such as red/purple <strong>anthocyanins</strong> and yellow/orange <strong>carotenoids</strong>. When subjected to the iodine test, these leaves readily turn blue-black, proving active starch synthesis!
      </div>
    </div>
  </div>

  <!-- Ecological Adaptations -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Morphological Adaptations</span>
      <h3 class="text-xl font-bold text-white font-heading">Photosynthetic Adaptations in Desert &amp; Aquatic Taxa</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-amber-400">Xerophytes (Cactus / Opuntia):</strong>
        <p class="text-slate-300 leading-relaxed">
          Leaves modified into sharp non-transpiring <strong>spines</strong> to eliminate water loss and deter herbivores. 
          The stem becomes flattened, fleshy, succulent, and rich in chlorophyll (<strong>phylloclade</strong>), taking over 100% of photosynthetic food synthesis.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
        <strong class="text-cyan-400">Submerged Hydrophytes (Hydrilla / Vallisneria):</strong>
        <p class="text-slate-300 leading-relaxed">
          Possess thin, flexible ribbon-like leaves devoid of stomata and waxy cuticles. 
          Gases (dissolved CO₂ and O₂) diffuse directly across thin epidermal cell membranes throughout the entire submerged surface.
        </p>
      </div>
    </div>
  </div>
</div>
"""

def build_tab_transport():
    return """<!-- ========================================== -->
<!-- 6. VASCULAR TRANSPORT ARCHITECTURE         -->
<!-- ========================================== -->
<div id="tabTransport" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-lg">
      <i class="fas fa-water"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Vascular Transport Architecture: Xylem Ascent vs Phloem Translocation</h2>
      <p class="text-xs text-slate-400">Complex conducting tissues, transpirational pull, source-to-sink sucrose translocation, and Balsam twig test</p>
    </div>
  </div>

  <!-- Master Comparison: Xylem vs Phloem -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-blue-500/30 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-blue-500/20 text-blue-300 font-mono text-xs font-bold">Conducting Pipeline</span>
      <h3 class="text-xl font-bold text-white font-heading">The Dual Conducting Channels: Xylem vs Phloem</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm">
      <!-- Xylem -->
      <div class="p-5 rounded-2xl bg-slate-950 border border-blue-900/40 space-y-3">
        <div class="text-blue-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-arrow-up"></i> Xylem (Water &amp; Mineral Conduction)
        </div>
        <p class="text-slate-300 leading-relaxed">
          Composed primarily of non-living, hollow, thick-walled lignified tubular elements: <strong>Xylem Vessels</strong> and <strong>Tracheids</strong> (along with xylem fibres and living xylem parenchyma).
        </p>
        <div class="space-y-1.5 text-xs">
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-blue-300">Substances Transported:</strong> Water and dissolved mineral nitrates, phosphates, sulfates.
          </div>
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-blue-300">Direction of Flow:</strong> Strictly <strong>UNIDIRECTIONAL (Upward only)</strong>, from root hairs up the stem to foliar petioles.
          </div>
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-blue-300">Driving Physical Force:</strong> <strong>Transpirational Pull</strong> (suction force created by water evaporation from stomata) coupled with cohesive-adhesive water properties.
          </div>
        </div>
      </div>

      <!-- Phloem -->
      <div class="p-5 rounded-2xl bg-slate-950 border border-emerald-900/40 space-y-3">
        <div class="text-emerald-400 font-bold text-base flex items-center gap-2">
          <i class="fas fa-arrows-alt-v"></i> Phloem (Organic Nutrient Translocation)
        </div>
        <p class="text-slate-300 leading-relaxed">
          Composed of living conducting conduits: <strong>Sieve Tubes</strong> (perforated sieve plates) intimately supported by nucleated <strong>Companion Cells</strong> (along with phloem parenchyma and fibres).
        </p>
        <div class="space-y-1.5 text-xs">
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-emerald-300">Substances Transported:</strong> Soluble organic photoassimilates (mainly <strong>sucrose sugar</strong>) and amino acids.
          </div>
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-emerald-300">Direction of Flow:</strong> Highly <strong>BIDIRECTIONAL (Multi-directional)</strong>, moving from Source (mature leaves) to Sinks (growing roots, fruits, tubers, floral buds).
          </div>
          <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
            <strong class="text-emerald-300">Driving Mechanism:</strong> Active hydrostatic pressure gradients requiring metabolic ATP energy.
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Balsam Twig Demonstration -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-rose-500/20 text-rose-300 font-mono text-xs font-bold">Laboratory Demonstration</span>
      <h3 class="text-xl font-bold text-white font-heading">Empirical Proof: Balsam Twig in Red Dye Solution</h3>
    </div>
    <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 text-xs md:text-sm text-slate-300 leading-relaxed space-y-3">
      <p>
        A young tender Balsam/Petunia shoot with white flowers is immersed in a beaker of water tinted red with <strong>eosin dye</strong> for 2–3 hours in bright sunlight.
      </p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-1">
        <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
          <strong class="text-amber-400">Macroscopic Observation:</strong>
          <p class="text-slate-400 text-xs">Red colored streaks visibly travel up the translucent stem, branch into leaf veins, and tint white floral petals pale pink!</p>
        </div>
        <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
          <strong class="text-emerald-400">Microscopic Transverse Section:</strong>
          <p class="text-slate-400 text-xs">A razor-thin cross-section of the stem reveals that ONLY the inner <strong>xylem vascular bundles</strong> are stained vibrant red, while phloem and cortex remain completely unstained!</p>
        </div>
      </div>
    </div>
  </div>
</div>
"""

def build_tab_respiration():
    return """<!-- ========================================== -->
<!-- 7. CELLULAR RESPIRATION & DIURNAL CYCLES   -->
<!-- ========================================== -->
<div id="tabRespiration" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-purple-500/20 text-purple-400 flex items-center justify-center text-lg">
      <i class="fas fa-wind"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Cellular Respiration in Plants &amp; Diurnal Gas Exchange</h2>
      <p class="text-xs text-slate-400">Continuous 24-hour bioenergetics, organ-specific respiratory channels, and the dawn/dusk Compensation Point</p>
    </div>
  </div>

  <!-- Respiration Biochemical Core -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-purple-500/30 shadow-xl space-y-4">
    <div class="flex items-center justify-between">
      <span class="px-2.5 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-mono text-xs font-bold">Continuous Bioenergetics</span>
      <span class="text-xs text-slate-400 font-mono">Exothermic Catabolic Breakdown</span>
    </div>
    <div class="p-4 rounded-2xl bg-slate-950 border border-purple-900/40 text-center space-y-2">
      <div class="text-xs uppercase text-slate-400 font-bold tracking-wider">Aerobic Respiration in Plant Cells (Occurs 24 Hours/Day)</div>
      <div class="text-lg md:text-2xl font-black text-purple-300 font-mono tracking-wide">
        C₆H₁₂O₆ + 6O₂ 
        <span class="text-xs text-slate-400 inline-block px-2">──[ Mitochondria / Enzymes ]──▶</span> 
        6CO₂↑ + 6H₂O + Energy (38 ATP)
      </div>
      <div class="text-xs text-slate-400 max-w-2xl mx-auto pt-1 leading-relaxed">
        Plants require continuous chemical energy (ATP) for nutrient uptake, phloem active loading, cell division, and protoplasmic repair.
      </div>
    </div>
  </div>

  <!-- Specialized Respiratory Organs -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Aeration Anatomy</span>
      <h3 class="text-xl font-bold text-white font-heading">Plant Respiratory Exchange Across Specialized Organs</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-emerald-400 text-sm">1. Foliar Stomata:</strong>
        <p class="text-slate-300 leading-relaxed">
          Abundant on leaf undersides. Gaseous oxygen diffuses directly into intercellular air spaces of spongy mesophyll and into cells.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-teal-400 text-sm">2. Stem Lenticels:</strong>
        <p class="text-slate-300 leading-relaxed">
          Permanent, loosely packed, non-closing cellular pores rupturing through the impermeable cork/bark of mature woody trees for aeration.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-amber-400 text-sm">3. Root Hairs &amp; Aeration:</strong>
        <p class="text-slate-300 leading-relaxed">
          Root epidermal extensions absorb dissolved oxygen trapped between soil micro-particles. Overwatering suffocates roots, causing anaerobic rot.
        </p>
      </div>

      <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-1.5">
        <strong class="text-rose-400 text-sm">4. Mangrove Pneumatophores:</strong>
        <p class="text-slate-300 leading-relaxed">
          In oxygen-depleted saline coastal swamps (*Rhizophora*), specialized breathing roots grow vertically upward above water with lenticels for aeration.
        </p>
      </div>
    </div>
  </div>

  <!-- Diurnal Cycle & The Compensation Point -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-5">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-cyan-500/20 text-cyan-300 font-mono text-xs font-bold">Diurnal Dynamics</span>
      <h3 class="text-xl font-bold text-white font-heading">Day vs Night Gaseous Balance &amp; The Compensation Point</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs md:text-sm">
      <div class="p-5 rounded-2xl bg-slate-950 border border-amber-900/40 space-y-2">
        <strong class="text-amber-300 font-bold flex items-center gap-2">
          <i class="fas fa-sun"></i> 1. Bright Daytime
        </strong>
        <p class="text-slate-300 text-xs leading-relaxed">
          Photosynthesis rate exceeds respiration rate by 10 to 20 times! 
          All CO₂ produced by respiration is consumed internally by chloroplasts, and excess CO₂ is drawn from the air. 
          Massive excess O₂ is released into the biosphere.
        </p>
      </div>

      <div class="p-5 rounded-2xl bg-slate-950 border border-blue-900/40 space-y-2">
        <strong class="text-blue-300 font-bold flex items-center gap-2">
          <i class="fas fa-moon"></i> 2. Complete Night
        </strong>
        <p class="text-slate-300 text-xs leading-relaxed">
          Without sunlight, photosynthesis ceases completely. Respiration continues 24/7. 
          The plant absorbs atmospheric O₂ and releases CO₂ gas into its surroundings. 
          (Explains ancient advice against sleeping under dense trees at night!)
        </p>
      </div>

      <div class="p-5 rounded-2xl bg-slate-950 border border-emerald-900/40 space-y-2">
        <strong class="text-emerald-300 font-bold flex items-center gap-2">
          <i class="fas fa-balance-scale"></i> 3. Dawn &amp; Dusk (Compensation Point)
        </strong>
        <p class="text-slate-300 text-xs leading-relaxed">
          Under low twilight light, the rate of photosynthetic CO₂ absorption <strong>EXACTLY EQUALS</strong> the rate of respiratory CO₂ emission! 
          The volume of O₂ consumed equals O₂ produced. <strong>Net gaseous exchange with the atmosphere is ZERO!</strong>
        </p>
      </div>
    </div>
  </div>

  <!-- Master Comparison Table -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-mono text-xs font-bold">Comparative Matrix</span>
      <h3 class="text-xl font-bold text-white font-heading">Photosynthesis vs Cellular Respiration</h3>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-xs md:text-sm text-slate-300 border-collapse">
        <thead>
          <tr class="border-b border-slate-800 text-slate-400 font-mono text-[11px] uppercase bg-slate-950/80">
            <th class="p-3">Feature</th>
            <th class="p-3 text-emerald-400">Photosynthesis</th>
            <th class="p-3 text-purple-400">Cellular Respiration</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800/60">
          <tr>
            <td class="p-3 font-bold text-white">Metabolic Nature</td>
            <td class="p-3">Anabolic (Constructive synthesis of glucose)</td>
            <td class="p-3">Catabolic (Oxidative breakdown of glucose)</td>
          </tr>
          <tr>
            <td class="p-3 font-bold text-white">Cellular Site</td>
            <td class="p-3">Chloroplasts (Contains chlorophyll)</td>
            <td class="p-3">Cytoplasm &amp; Mitochondria</td>
          </tr>
          <tr>
            <td class="p-3 font-bold text-white">Time of Occurrence</td>
            <td class="p-3">Exclusively during daylight / illumination</td>
            <td class="p-3">Continuously 24 hours a day (Day and Night)</td>
          </tr>
          <tr>
            <td class="p-3 font-bold text-white">Raw Materials</td>
            <td class="p-3">Carbon dioxide (CO₂) and Water (H₂O)</td>
            <td class="p-3">Glucose (C₆H₁₂O₆) and Oxygen (O₂)</td>
          </tr>
          <tr>
            <td class="p-3 font-bold text-white">End Products</td>
            <td class="p-3">Glucose (C₆H₁₂O₆) and Oxygen (O₂↑)</td>
            <td class="p-3">Carbon dioxide (CO₂↑), Water (H₂O), and 38 ATP</td>
          </tr>
          <tr>
            <td class="p-3 font-bold text-white">Energy Conversion</td>
            <td class="p-3">Radiant solar energy trapped into chemical bonds</td>
            <td class="p-3">Chemical energy released as kinetic/thermal ATP</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

def build_tab_activities():
    return """<!-- ========================================== -->
<!-- 8. NCERT LAB ACTIVITIES & EXPERIMENTS       -->
<!-- ========================================== -->
<div id="tabActivities" class="tab-pane hidden space-y-8 animate-fadeIn">
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-lg">
      <i class="fas fa-vial"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Laboratory Demonstrations &amp; NCERT Experiments</h2>
      <p class="text-xs text-slate-400">Step-by-step empirical protocols, controls, and diagnostic chemical reagents</p>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs md:text-sm">
    <!-- Activity 1: Hydrilla O2 Bubble Experiment -->
    <div class="p-6 rounded-3xl bg-slate-900/90 border border-emerald-500/30 space-y-3">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-emerald-500/20 text-emerald-300 font-bold">Experiment 1</span>
        <span class="text-xs text-slate-400 font-mono">Oxygen Evolution</span>
      </div>
      <h4 class="text-base font-bold text-white">Demonstrating Oxygen Evolution in Hydrilla</h4>
      <p class="text-slate-300 leading-relaxed text-xs">
        Place fresh <em>Hydrilla</em> sprigs in a water beaker under an inverted glass funnel. 
        Invert a water-filled test tube over the funnel stem and place in bright sunlight.
      </p>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-emerald-300 space-y-1">
        <strong>Observation &amp; Proof:</strong> Continuous streams of gas bubbles rise and displace water at the top of the test tube. 
        When a glowing incense splint is brought near the mouth of the tube, it <strong>bursts vigorously into flame</strong>, conclusively proving the evolved gas is pure Oxygen!
      </div>
    </div>

    <!-- Activity 2: Starch Iodine Test in Leaves -->
    <div class="p-6 rounded-3xl bg-slate-900/90 border border-teal-500/30 space-y-3">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-teal-500/20 text-teal-300 font-bold">Experiment 2</span>
        <span class="text-xs text-slate-400 font-mono">Starch Assay</span>
      </div>
      <h4 class="text-base font-bold text-white">Testing a Green Leaf for Starch with Iodine</h4>
      <p class="text-slate-300 leading-relaxed text-xs">
        Pluck a green leaf exposed to sunlight. Boil it in water for 2 minutes to soften cell walls and kill protoplasm. 
        Transfer leaf into a test tube of methylated alcohol placed inside a boiling water bath (never over naked flame!) to extract chlorophyll.
      </p>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-teal-300 space-y-1">
        <strong>Observation &amp; Proof:</strong> The decolored pale white leaf is rinsed in warm water and treated with dilute iodine solution. 
        The leaf instantly turns <strong>intense blue-black</strong>, demonstrating active photosynthesis and starch formation!
      </div>
    </div>

    <!-- Activity 3: Moll's Half-Leaf CO2 Proof -->
    <div class="p-6 rounded-3xl bg-slate-900/90 border border-amber-500/30 space-y-3">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-amber-500/20 text-amber-300 font-bold">Experiment 3</span>
        <span class="text-xs text-slate-400 font-mono">CO₂ Essentiality</span>
      </div>
      <h4 class="text-base font-bold text-white">Moll's Half-Leaf Experiment for Carbon Dioxide</h4>
      <p class="text-slate-300 leading-relaxed text-xs">
        De-starch a potted plant in dark for 48 hours. Insert half of an intact leaf through a split cork into a glass bottle containing <strong>potassium hydroxide (KOH) solution</strong> (which completely absorbs all internal CO₂). Keep other half exposed to outside air.
      </p>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-amber-300 space-y-1">
        <strong>Observation &amp; Proof:</strong> After 4 hours of illumination, test leaf with iodine. 
        The exposed outer half turns blue-black (photosynthesis occurred); the inner half starved of CO₂ remains brown, proving CO₂ is essential!
      </div>
    </div>

    <!-- Activity 4: Germinating Seeds Limewater Test -->
    <div class="p-6 rounded-3xl bg-slate-900/90 border border-purple-500/30 space-y-3">
      <div class="flex items-center justify-between border-b border-slate-800 pb-2">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-purple-500/20 text-purple-300 font-bold">Experiment 4</span>
        <span class="text-xs text-slate-400 font-mono">Seed Respiration</span>
      </div>
      <h4 class="text-base font-bold text-white">Carbon Dioxide Evolution by Germinating Seeds</h4>
      <p class="text-slate-300 leading-relaxed text-xs">
        Place actively germinating gram/pea seeds in a sealed conical flask with moist cotton. 
        Suspend a small test tube containing freshly prepared clear <strong>limewater (Ca(OH)₂)</strong> inside the flask with a thread.
      </p>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-purple-300 space-y-1">
        <strong>Observation &amp; Proof:</strong> Within a few hours, the clear limewater turns distinctly <strong>milky (turbid white)</strong> due to insoluble calcium carbonate precipitation (Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O), proving germinating seeds respire actively!
      </div>
    </div>
  </div>
</div>
"""

def build_tab_textbook(subj_questions):
    html = []
    html.append(f"""<!-- ========================================== -->
<!-- 9. COMPREHENSIVE SOLVED REPOSITORY (tabTextbook) -->
<!-- ========================================== -->
<div id="tabTextbook" class="tab-pane hidden space-y-8 animate-fadeIn">
  <!-- Header Title -->
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-5">
    <div>
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-semibold uppercase tracking-wider mb-2">
        <i class="fas fa-book-reader"></i> Comprehensive Solved Repository
      </div>
      <h2 class="text-3xl font-extrabold text-white font-heading">Universal Solved Q&amp;A Bank (All {len(subj_questions)} Subjective Questions)</h2>
      <p class="text-sm text-slate-400 mt-1">Complete textbook, exemplar, and competitive short answer, long answer, and HOTS solutions with physiological and anatomical precision.</p>
    </div>
  </div>

  <!-- Sticky Search & Filter Controls -->
  <div class="sticky top-[54px] z-30 p-4 md:p-5 rounded-2xl bg-slate-900/95 backdrop-blur-md border border-slate-800/80 shadow-xl space-y-3">
    <div class="flex flex-col md:flex-row gap-3">
      <div class="relative flex-1">
        <i class="fas fa-search absolute left-4 top-1/2 -translate-y-1/2 text-slate-500 text-sm"></i>
        <input type="text" id="subjSearchInput" oninput="filterSubjectiveCards()" placeholder="Search questions by keyword (e.g., Photosynthesis, Xylem, Phloem, Stomata, Respiration, Starch, Pots, Guard cells, Transpiration)..." class="w-full pl-11 pr-4 py-2.5 rounded-xl bg-slate-950 border border-slate-800 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 transition-colors">
      </div>
      <div class="flex flex-wrap gap-2" id="subjFilterPills">
        <button onclick="filterSubjCat('all')" id="scat-all" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-emerald-600 text-white cursor-pointer transition-all shadow-md shadow-emerald-600/20">All ({len(subj_questions)})</button>
        <button onclick="filterSubjCat('growth')" id="scat-growth" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Plant Growth &amp; Nutrition</button>
        <button onclick="filterSubjCat('photo')" id="scat-photo" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Photosynthesis &amp; Chloroplasts</button>
        <button onclick="filterSubjCat('factors')" id="scat-factors" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Limiting Factors &amp; Starch</button>
        <button onclick="filterSubjCat('transport')" id="scat-transport" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Vascular Transport</button>
        <button onclick="filterSubjCat('respiration')" id="scat-respiration" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Plant Respiration</button>
      </div>
    </div>
    <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
      <span id="subjCounter">Showing all {len(subj_questions)} solved questions</span>
      <button onclick="toggleAllSubjAnswers()" id="toggleAllSubjBtn" class="text-emerald-400 hover:text-emerald-300 font-semibold cursor-pointer">
        Expand All Solutions
      </button>
    </div>
  </div>

  <!-- Cards Container -->
  <div class="space-y-4" id="subjCardsContainer">
""")

    for idx, q in enumerate(subj_questions, 1):
        qid = q.get('id', f'sq_{idx}')
        raw_type = q.get('type', 'sa')
        qtype = 'Very Short Answer' if raw_type == 'vsa' else ('Long Answer' if raw_type == 'la' else 'Short Answer')
        topic = q.get('topic', 'Plant Physiology')
        marks = q.get('marks', 1 if raw_type == 'vsa' else (5 if raw_type == 'la' else 3))
        difficulty = q.get('difficulty', 'medium')
        diff_badge = 'bg-emerald-500/20 text-emerald-300' if difficulty == 'easy' else ('bg-amber-500/20 text-amber-300' if difficulty == 'medium' else 'bg-rose-500/20 text-rose-300')
        
        # FIXED: Look up 'question', 'question_text', or 'text'
        q_raw = q.get('question') or q.get('question_text') or q.get('text') or ''
        qtext = esc(q_raw)

        # Categorize for pills
        topic_lower = (topic + " " + q_raw).lower()
        cat = 'general'
        if any(k in topic_lower for k in ['growth', 'pot a', 'pot b', 'pot c', 'vrikshayurveda', 'parashara', 'vegetative', 'reproductive', 'nutrition', 'autotroph', 'heterotroph']):
            cat = 'growth'
        elif any(k in topic_lower for k in ['photosynthesis', 'chloroplast', 'grana', 'thylakoid', 'stroma', 'guard cell', 'stomata', 'turgor']):
            cat = 'photo'
        elif any(k in topic_lower for k in ['factor', 'light', 'temperature', 'denatur', 'co2', 'carbon dioxide', 'coleus', 'croton', 'pigment', 'iodine', 'starch', 'moll', 'half-leaf']):
            cat = 'factors'
        elif any(k in topic_lower for k in ['xylem', 'phloem', 'translocation', 'sap', 'transpiration', 'balsam', 'vessel', 'tracheid', 'sieve']):
            cat = 'transport'
        elif any(k in topic_lower for k in ['respiration', 'lenticel', 'root hair', 'aeration', 'pneumatophore', 'compensation point', 'day', 'night', 'atp']):
            cat = 'respiration'

        answer = esc(q.get('answer') or q.get('model_answer') or '')
        reasoning = esc(q.get('explanation') or q.get('scientific_reasoning') or '')
        rubric = q.get('marking_rubric')

        diagram_slot = q.get('diagram_slot')
        diagram_html = ""
        if diagram_slot:
            diagram_html = f"""<div class="p-4 rounded-2xl bg-slate-950/80 border border-emerald-500/30 flex flex-col md:flex-row items-center gap-4 my-3">
  <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xl shrink-0">
    <i class="fas fa-camera-retro"></i>
  </div>
  <div class="flex-1 space-y-1 text-left">
    <div class="flex items-center gap-2">
      <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/20 text-amber-300 uppercase tracking-wide">Diagram Slot (Pending Admin Asset)</span>
      <span class="text-xs text-slate-400 font-mono">{esc(diagram_slot.get('source_hint', ''))}</span>
    </div>
    <p class="text-xs text-slate-300 leading-relaxed">{esc(diagram_slot.get('description', ''))}</p>
  </div>
</div>"""

        rubric_html = ""
        if rubric:
            rubric_html = f"""<div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-xs text-slate-400 mt-2">
  <strong class="text-slate-300"><i class="fas fa-clipboard-check text-emerald-400 mr-1"></i>Marking Breakdown:</strong>
  <span class="ml-1 text-slate-400">{esc(str(rubric))}</span>
</div>"""

        reasoning_html = ""
        if reasoning:
            reasoning_html = f"""<div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/40 text-xs text-emerald-300 mt-2">
  <strong><i class="fas fa-lightbulb text-amber-400 mr-1"></i>Scientific Reasoning:</strong> {reasoning}
</div>"""

        html.append(f"""    <div class="subj-card p-6 rounded-3xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all space-y-4" data-cat="{cat}">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Q{idx} • {qtype}</span>
          <span class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 text-[11px] font-medium">{esc(topic)}</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="px-2 py-0.5 rounded-md {diff_badge} text-[10px] font-semibold">{esc(difficulty)}</span>
          <span class="px-2 py-0.5 rounded-md bg-slate-800 text-amber-300 text-[10px] font-mono font-bold">{marks} Marks</span>
        </div>
      </div>

      <div class="text-sm md:text-base font-semibold text-white leading-relaxed">
        {qtext.replace(chr(10), '<br>')}
      </div>

      {diagram_html}

      <div class="pt-1">
        <button onclick="toggleAnswer('ans-{qid}')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-400 text-xs font-semibold transition-colors flex items-center gap-2 cursor-pointer">
          <i class="fas fa-chevron-down text-xs transition-transform duration-200"></i>
          <span>Show Verified Solution</span>
        </button>
        <div id="ans-{qid}" class="answer-box hidden mt-4 p-5 rounded-2xl bg-slate-950 border border-emerald-900/40 text-slate-200 text-xs md:text-sm leading-relaxed space-y-3">
          <div class="text-white font-medium">
            {answer.replace(chr(10), '<br>')}
          </div>
          {reasoning_html}
          {rubric_html}
        </div>
      </div>
    </div>""")

    html.append("  </div>\n</div>")
    return "\n".join(html)

def build_match_arena_html(arena_id, title, desc, pairs_dict, left_items, right_items):
    pairs_json = esc(json.dumps(pairs_dict))
    
    left_html = []
    for k, text in left_items:
        left_html.append(f"""        <div class="match-bubble-left group relative p-3 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-emerald-500/50 transition-all cursor-pointer flex items-center justify-between gap-3 select-none"
             id="match-left-{arena_id}-{k}"
             data-key="{k}"
             draggable="true"
             ondragstart="handleMatchDragStart(event, {arena_id}, '{k}')"
             onclick="handleMatchItemClick({arena_id}, 'left', '{k}')">
          <div class="flex items-center gap-2.5 min-w-0">
            <span class="w-7 h-7 rounded-xl bg-slate-800 text-emerald-400 font-mono font-bold text-xs flex items-center justify-center shrink-0 border border-slate-700">{k}</span>
            <span class="text-xs text-slate-200 font-medium leading-snug">{esc(text)}</span>
          </div>
          <div class="match-conn-badge hidden shrink-0 px-2 py-0.5 rounded-md bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-[11px] font-mono font-bold flex items-center gap-1">
            <span class="target-label"></span>
          </div>
        </div>""")
        
    right_html = []
    for k, text in right_items:
        right_html.append(f"""        <div class="match-socket-right group relative p-3 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-teal-500/50 transition-all cursor-pointer flex items-center justify-between gap-3 select-none"
             id="match-right-{arena_id}-{k}"
             data-key="{k}"
             ondragover="handleMatchDragOver(event)"
             ondragleave="handleMatchDragLeave(event)"
             ondrop="handleMatchDrop(event, {arena_id}, '{k}')"
             onclick="handleMatchItemClick({arena_id}, 'right', '{k}')">
          <div class="flex items-center gap-2.5 min-w-0">
            <span class="w-7 h-7 rounded-xl bg-slate-800 text-teal-400 font-mono font-bold text-xs flex items-center justify-center shrink-0 border border-slate-700">{k}</span>
            <span class="text-xs text-slate-200 font-medium leading-snug">{esc(text)}</span>
          </div>
          <div class="match-socket-badge hidden shrink-0 px-2 py-0.5 rounded-md bg-teal-500/20 border border-teal-500/40 text-teal-300 text-[11px] font-mono font-bold flex items-center gap-1">
            <span class="source-label"></span>
          </div>
        </div>""")

    return f"""    <div class="drill-card p-6 rounded-3xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all space-y-4" data-type="match">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-mono text-xs font-bold">Interactive Arena #{arena_id}</span>
          <span class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 text-[11px] font-medium">{esc(title)}</span>
        </div>
        <div class="flex items-center gap-2">
          <span id="match-status-{arena_id}" class="font-mono font-bold text-amber-400 bg-amber-950/60 border border-amber-800/50 px-2.5 py-0.5 rounded-full text-[11px]">0/{len(left_items)} Paired</span>
          <span class="px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 text-[10px] font-semibold">Match Columns (Drag or Click)</span>
        </div>
      </div>

      <div class="text-xs md:text-sm text-slate-300 leading-relaxed">
        {esc(desc)}
      </div>

      <div class="match-arena grid grid-cols-1 md:grid-cols-2 gap-4 relative" id="match-arena-{arena_id}" data-idx="{arena_id}" data-pairs="{pairs_json}" data-total="{len(left_items)}">
        <div class="space-y-2" id="match-left-col-{arena_id}">
          <div class="text-[11px] font-mono uppercase text-emerald-400 font-bold px-1 mb-1">Column A (Structures / Concepts)</div>
{chr(10).join(left_html)}
        </div>
        <div class="space-y-2" id="match-right-col-{arena_id}">
          <div class="text-[11px] font-mono uppercase text-teal-400 font-bold px-1 mb-1">Column B (Functions / Roles)</div>
{chr(10).join(right_html)}
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-3 pt-2 border-t border-slate-800/60">
        <div class="match-feedback text-xs font-mono font-semibold text-slate-400" id="match-feedback-{arena_id}">
          Pair each item from Column A with Column B
        </div>
        <div class="flex items-center gap-2">
          <button onclick="checkMatchDrill({arena_id})" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-colors cursor-pointer flex items-center gap-1.5 shadow-md shadow-emerald-600/20">
            <i class="fas fa-check"></i> Check Pairs
          </button>
          <button onclick="resetMatchDrill({arena_id})" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition-colors cursor-pointer flex items-center gap-1.5">
            <i class="fas fa-redo"></i> Reset
          </button>
        </div>
      </div>
    </div>"""

def build_tab_drills(obj_questions):
    html = []
    total_drills = len(obj_questions) + 4
    count_mcq = sum(1 for q in obj_questions if q.get('type') in ['mcq'])
    count_tf = sum(1 for q in obj_questions if q.get('type') in ['tf', 'true_false'])
    count_fib = sum(1 for q in obj_questions if q.get('type') in ['fib', 'fill_in_the_blank'])
    count_ar = sum(1 for q in obj_questions if q.get('type') in ['assertion_reason'])
    count_match = 4

    html.append(f"""<!-- ========================================== -->
<!-- 10. INTERACTIVE DRILLS (tabDrills)         -->
<!-- ========================================== -->
<div id="tabDrills" class="tab-pane hidden space-y-8 animate-fadeIn">
  <!-- Interactive Header with Live Score Dashboard -->
  <div class="p-6 md:p-8 rounded-3xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-cyan-950/60 border border-emerald-800/40 shadow-xl space-y-4">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-semibold uppercase tracking-wider mb-2">
          <i class="fas fa-check-circle"></i> Adaptive Testing Suite
        </div>
        <h2 class="text-3xl font-extrabold text-white font-heading">Interactive Objective Assessment ({total_drills} Drills)</h2>
        <p class="text-sm text-slate-400 mt-1">Multi-tier MCQs, Case-Based Questions with Anatomical Diagrams, Assertion &amp; Reason, True/False, FIBs, and Interactive Match Arenas.</p>
      </div>

      <!-- Live Score Counter -->
      <div class="flex items-center gap-4 bg-slate-950/80 p-4 rounded-2xl border border-slate-800 self-start md:self-auto shadow-inner">
        <div class="text-center">
          <div class="text-2xl font-black text-amber-400 font-mono" id="drillScore">0</div>
          <div class="text-[10px] uppercase font-bold text-slate-400">Score</div>
        </div>
        <div class="w-px h-8 bg-slate-800"></div>
        <div class="text-center">
          <div class="text-2xl font-black text-emerald-400 font-mono" id="drillAnswered">0</div>
          <div class="text-[10px] uppercase font-bold text-slate-400">Answered</div>
        </div>
        <div class="w-px h-8 bg-slate-800"></div>
        <div class="text-center">
          <div class="text-2xl font-black text-sky-400 font-mono" id="drillTotal">{total_drills}</div>
          <div class="text-[10px] uppercase font-bold text-slate-400">Total</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Sticky Drills Filter Bar with Score Badges -->
  <div class="sticky top-[54px] z-30 py-3 px-4 rounded-2xl bg-slate-900/95 backdrop-blur-md border border-slate-800/80 shadow-xl flex flex-wrap items-center justify-between gap-3">
    <!-- Filter Buttons -->
    <div class="flex flex-wrap items-center gap-2">
      <button onclick="filterDrills('all')" id="df-all" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 text-white cursor-pointer transition-all shadow-md">All ({total_drills})</button>
      <button onclick="filterDrills('mcq')" id="df-mcq" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">MCQs ({count_mcq})</button>
      <button onclick="filterDrills('tf')" id="df-tf" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">True / False ({count_tf})</button>
      <button onclick="filterDrills('fib')" id="df-fib" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Fill in Blanks ({count_fib})</button>
      <button onclick="filterDrills('assertion_reason')" id="df-assertion_reason" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Assertion &amp; Reason ({count_ar})</button>
      <button onclick="filterDrills('match')" id="df-match" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all">Match Arenas ({count_match})</button>
    </div>

    <!-- Live Sticky Score Monitor -->
    <div class="flex items-center gap-3 bg-slate-950/90 py-1.5 px-3 rounded-xl border border-slate-800 text-xs font-mono ml-auto">
      <span class="text-slate-400">Score: <strong class="text-amber-400 font-bold" id="drillScoreSticky">0</strong></span>
      <span class="text-slate-700">|</span>
      <span class="text-slate-400">Answered: <strong class="text-emerald-400 font-bold" id="drillAnsweredSticky">0</strong>/<span id="drillTotalSticky">{total_drills}</span></span>
    </div>
  </div>

  <!-- Drills Grid Container -->
  <div class="space-y-4" id="drillsCardsContainer">
""")

    # 4 Match Arenas
    arenas = [
        (1, "Plant Cell Organelles & Cellular Roles", "Match each organelle/structure with its precise biochemical or physiological role in plant cells.",
         {"I": "C", "II": "A", "III": "D", "IV": "B", "V": "E"},
         [("I", "Grana Thylakoids"), ("II", "Chloroplast Stroma"), ("III", "Guard Cells"), ("IV", "Xylem Vessels"), ("V", "Phloem Sieve Tubes")],
         [("A", "Hydrophilic matrix site of Calvin cycle dark reactions"), ("B", "Lignified hollow conduits conducting unidirectional ascent of sap"), ("C", "Membranous pigment stacks hosting photochemical light reactions"), ("D", "Turgor-driven valves regulating stomatal pore opening"), ("E", "Living perforated conduits translocating organic sucrose")]),
        
        (2, "Transport & Translocation Dynamics", "Match each conducting mechanism with its corresponding anatomical feature or physical force.",
         {"I": "D", "II": "A", "III": "B", "IV": "C", "V": "E"},
         [("I", "Transpiration Pull"), ("II", "Root Pressure"), ("III", "Companion Cells"), ("IV", "Eosin Dye"), ("V", "Source Tissue")],
         [("A", "Hydrostatic pressure pushing sap upward short distances"), ("B", "Nucleated cells actively loading sucrose into sieve tubes"), ("C", "Chemical reagent staining xylem bundles red in Balsam shoot"), ("D", "Cohesion-tension suction force pulling water columns to canopy"), ("E", "Mature foliar mesophyll cells synthesizing photoassimilates")]),

        (3, "Limiting Factors & Diagnostic Reagents", "Match each diagnostic chemical or physical factor with its biological significance.",
         {"I": "C", "II": "A", "III": "D", "IV": "B", "V": "E"},
         [("I", "Potassium Hydroxide (KOH)"), ("II", "Iodine Solution"), ("III", "Alcohol Water Bath"), ("IV", "25°C to 35°C"), ("V", "Above 40°C–45°C")],
         [("A", "Reagent testing positive for starch by turning intense blue-black"), ("B", "Optimum physiological temperature window for photosynthesis"), ("C", "Alkaline absorbent removing CO₂ in Moll's half-leaf test"), ("D", "Safely extracts green chlorophyll without flammable naked fire risk"), ("E", "Thermal energy causes irreversible catalytic enzyme denaturation")]),

        (4, "Specialized Plant Respiratory Adaptations", "Match each plant respiratory adaptation with its corresponding ecological taxon or organ.",
         {"I": "B", "II": "D", "III": "A", "IV": "E", "V": "C"},
         [("I", "Foliar Stomata"), ("II", "Stem Lenticels"), ("III", "Pneumatophores"), ("IV", "Root Hairs"), ("V", "Compensation Point")],
         [("A", "Negatively geotropic breathing roots of mangrove trees in saline mud"), ("B", "Epidermal pores providing primary gaseous exchange in foliage"), ("C", "Twilight light level where photosynthesis rate equals respiration rate"), ("D", "Loosely packed aerating cellular pores rupturing mature woody bark"), ("E", "Epidermal extensions absorbing oxygen trapped between soil particles")])
    ]

    for a_id, a_title, a_desc, a_pairs, a_left, a_right in arenas:
        html.append(build_match_arena_html(a_id, a_title, a_desc, a_pairs, a_left, a_right))

    # All objective questions
    for idx, q in enumerate(obj_questions, 5):
        qid = q.get('id', f'oq_{idx}')
        raw_type = q.get('type', 'mcq')
        qtype = 'tf' if raw_type in ['tf', 'true_false'] else ('fib' if raw_type in ['fib', 'fill_in_the_blank'] else ('assertion_reason' if raw_type == 'assertion_reason' else 'mcq'))
        topic = q.get('topic', 'Plant Physiology')
        diff = q.get('difficulty', 'medium')
        diff_badge = 'bg-emerald-500/20 text-emerald-300' if diff == 'easy' else ('bg-amber-500/20 text-amber-300' if diff == 'medium' else 'bg-rose-500/20 text-rose-300')
        
        # FIXED: Look up 'question', 'question_text', or 'text'
        q_raw = q.get('question') or q.get('question_text') or q.get('text') or ''
        qtext = esc(q_raw)

        options = q.get('options', [])
        answer = q.get('answer', '')
        explanation = esc(q.get('explanation') or q.get('scientific_reasoning') or f"The correct answer is {answer}.")

        diagram_slot = q.get('diagram_slot')
        diagram_html = ""
        if diagram_slot:
            diagram_html = f"""<div class="p-3.5 rounded-2xl bg-slate-950/80 border border-emerald-500/30 flex items-center gap-3 my-2.5">
  <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-lg shrink-0">
    <i class="fas fa-camera-retro"></i>
  </div>
  <div class="text-xs space-y-0.5">
    <div class="font-bold text-amber-300 uppercase tracking-wide text-[10px]">Visual Diagram Slot</div>
    <p class="text-slate-300 leading-snug">{esc(diagram_slot.get('description', ''))}</p>
  </div>
</div>"""

        opts_html = []
        if qtype == 'mcq' or qtype == 'assertion_reason':
            for opt_idx, opt in enumerate(options):
                opt_letter = chr(65 + opt_idx)
                opt_clean = clean_option_text(opt)
                is_correct = "true" if check_mcq_correct(answer, opt, opt_idx) else "false"
                opts_html.append(f"""          <button onclick="handleDrillClick(this, {is_correct}, '{explanation}')" class="w-full text-left p-3.5 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-emerald-500/50 hover:bg-slate-800/60 transition-all flex items-start gap-3 cursor-pointer group select-none">
            <span class="w-7 h-7 rounded-xl bg-slate-900 group-hover:bg-emerald-500/20 text-slate-400 group-hover:text-emerald-300 font-mono font-bold text-xs flex items-center justify-center shrink-0 border border-slate-800 transition-colors">{opt_letter}</span>
            <span class="text-xs md:text-sm text-slate-300 group-hover:text-white transition-colors leading-relaxed pt-0.5">{esc(opt_clean)}</span>
          </button>""")
        elif qtype == 'tf':
            for opt in ['True', 'False']:
                is_correct = "true" if (str(answer).strip().lower() == opt.lower()) else "false"
                opts_html.append(f"""          <button onclick="handleDrillClick(this, {is_correct}, '{explanation}')" class="flex-1 text-center p-3.5 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-emerald-500/50 hover:bg-slate-800/60 transition-all cursor-pointer font-bold text-xs md:text-sm text-slate-300 hover:text-white select-none">
            {opt}
          </button>""")
        elif qtype == 'fib':
            opts_html.append(f"""          <div class="flex items-center gap-2">
            <input type="text" placeholder="Type answer here..." class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs md:text-sm text-white focus:outline-none focus:border-emerald-500">
            <button onclick="handleDrillClick(this, true, 'Correct Answer: <strong>{esc(str(answer))}</strong><br>{explanation}')" class="px-4 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition-colors cursor-pointer shrink-0">
              Check Answer
            </button>
          </div>""")

        opts_container = f'<div class="grid grid-cols-1 gap-2 pt-1">\n' + '\n'.join(opts_html) + '\n</div>' if qtype != 'tf' else f'<div class="flex gap-3 pt-1">\n' + '\n'.join(opts_html) + '\n</div>'

        html.append(f"""    <div class="drill-card p-6 rounded-3xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all space-y-4" data-type="{qtype}">
      <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-mono text-xs font-bold">Q{idx} • {qtype.upper()}</span>
          <span class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 text-[11px] font-medium">{esc(topic)}</span>
        </div>
        <span class="px-2 py-0.5 rounded-md {diff_badge} text-[10px] font-semibold">{esc(diff)}</span>
      </div>

      <div class="text-sm md:text-base font-semibold text-white leading-relaxed">
        {qtext.replace(chr(10), '<br>')}
      </div>

      {diagram_html}

      {opts_container}

      <div class="drill-feedback hidden p-4 rounded-2xl text-xs leading-relaxed space-y-1"></div>
    </div>""")

    html.append("  </div>\n</div>")
    return "\n".join(html)

def build_tab_traps():
    return """<!-- ========================================== -->
<!-- 11. EXAM TRAPS & 3D FLASHCARDS (tabTraps)   -->
<!-- ========================================== -->
<div id="tabTraps" class="tab-pane hidden space-y-8 animate-fadeIn">
  <!-- Section Title -->
  <div class="flex items-center gap-3 border-b border-slate-800 pb-4">
    <div class="w-10 h-10 rounded-2xl bg-rose-500/20 text-rose-400 flex items-center justify-center text-lg">
      <i class="fas fa-skull-crossbones"></i>
    </div>
    <div>
      <h2 class="text-2xl font-bold text-white font-heading">Exam Traps, Pitfalls &amp; 3D Flashcards</h2>
      <p class="text-xs text-slate-400">8 High-Yield Board Exam Pitfalls &amp; 16 Interactive 3D Revision Flashcards</p>
    </div>
  </div>

  <!-- 8 Fatal Exam Traps & Misconceptions -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-6">
    <div class="flex items-center gap-2">
      <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-pulse"></span>
      <h3 class="text-lg font-bold text-white font-heading">8 Fatal Board Exam Traps &amp; Common Student Misconceptions</h3>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs md:text-sm">
      <!-- Trap 1 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 1: Plants Respire 24 Hours a Day (Day AND Night)
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Writing that plants perform photosynthesis by day and respire only at night.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Cellular respiration occurs <strong>continuously 24 hours a day</strong> across every living plant cell! What changes is photosynthesis: it runs only during daylight and ceases completely in darkness.
        </p>
      </div>

      <!-- Trap 2 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 2: Photosynthesis DOES NOT Occur at Night
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Thinking that moonlight or starlight drives photosynthesis.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Photosynthesis has an absolute requirement for solar radiant energy. At night, photosynthesis completely stops; plants only consume oxygen and release carbon dioxide via aerobic respiration.
        </p>
      </div>

      <!-- Trap 3 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 3: Temperature Kinetics: Photosynthesis Crashes Above 40°C
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Assuming that higher temperatures always increase the rate of photosynthesis indefinitely.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Photosynthetic dark reactions are catalyzed by complex enzymes (like RuBisCO). Above 40°C to 45°C, high thermal kinetic energy <strong>denatures these proteins</strong>, permanently collapsing photosynthetic activity!
        </p>
      </div>

      <!-- Trap 4 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 4: Green Light is REFLECTED, Not Absorbed!
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Stating that plants absorb green light because their leaves are green.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Chlorophyll absorbs photons primarily in the <strong>Blue (~430 nm) and Red (~660 nm)</strong> spectral bands. Green light (~500–550 nm) is completely <strong>reflected</strong>, which is precisely why foliage appears green to our eyes!
        </p>
      </div>

      <!-- Trap 5 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 5: Alcohol Boiling Must Be in a Water Bath (Never Naked Flame!)
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Boiling a leaf in methylated alcohol directly over a Bunsen burner flame.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Alcohol and ethanol are <strong>violently flammable</strong>. The leaf in alcohol must ALWAYS be heated inside a <strong>water bath</strong> (beaker of boiling water) to safely dissolve chlorophyll pigments without fire hazard!
        </p>
      </div>

      <!-- Trap 6 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 6: Xylem is UNIDIRECTIONAL; Phloem is BIDIRECTIONAL
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Writing that xylem water conduction travels up and down.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Xylem conduction of sap is strictly <strong>unidirectional (upward only)</strong>, driven by transpirational pull from roots to leaves. Phloem translocation of sucrose is <strong>bidirectional</strong>, moving from source to sink.
        </p>
      </div>

      <!-- Trap 7 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 7: Guard Cells Swell to OPEN, Shrink to CLOSE
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Confusing the turgor state of guard cells during stomatal pore opening.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> When guard cells absorb water and become <strong>turgid (swollen)</strong>, their elastic outer walls curve outward, pulling the pore <strong>OPEN</strong>! When they lose water and become <strong>flaccid (limp)</strong>, the pore <strong>CLOSES</strong>.
        </p>
      </div>

      <!-- Trap 8 -->
      <div class="p-4 rounded-2xl bg-slate-950/70 border border-rose-900/40 space-y-2">
        <div class="text-rose-400 font-bold flex items-center gap-2">
          <i class="fas fa-exclamation-triangle"></i> Trap 8: Compensation Point is ZERO NET EXCHANGE, Not Zero Activity
        </div>
        <p class="text-slate-300 text-xs leading-relaxed">
          <strong class="text-rose-300">Fatal Mistake:</strong> Stating that both photosynthesis and respiration stop at the compensation point.<br>
          <span class="text-emerald-400 font-semibold">The Scientific Truth:</span> Both processes run simultaneously! At dawn and dusk, the rate of photosynthetic CO₂ absorption <strong>exactly equals</strong> the rate of respiratory CO₂ evolution. Net gaseous exchange with ambient air is zero!
        </p>
      </div>
    </div>
  </div>

  <!-- 16 Interactive 3D Revision Flashcards -->
  <div class="p-6 md:p-8 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-6">
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <h3 class="text-lg font-bold text-white font-heading">16 Interactive 3D Revision Flashcards</h3>
      </div>
      <span class="text-xs text-slate-500 font-mono">Tap any card to flip 180°</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
""" + build_flashcards_html() + """
    </div>
  </div>
</div>
"""

def build_flashcards_html():
    flashcards_data = [
        ("Photosynthesis Balanced Reaction", "What is the complete balanced equation for photosynthesis with state symbols?",
         "6CO₂ + 12H₂O ──[Light/Chlorophyll]──▶ C₆H₁₂O₆ + 6O₂↑ + 6H₂O. 6 molecules of carbon dioxide reduce with 12 water molecules to produce 1 glucose, 6 oxygen, and 6 water molecules."),
        
        ("Chloroplast Structure", "What are the four main anatomical components of a plant chloroplast?",
         "(1) Outer and inner double-membrane envelope, (2) Hydrophilic proteinaceous Stroma (Dark reaction site), (3) Stacked Thylakoid Grana (Light reaction site), and (4) Connecting Stroma Lamellae."),
        
        ("Stomatal Valve Dynamics", "How do guard cells mechanically open the stomatal aperture during the day?",
         "Active K⁺ uptake causes water influx via endosmosis. Guard cells swell (become turgid). Their thick inner walls resist stretching while elastic outer walls bulge outward, pulling the pore wide open!"),
        
        ("Xylem Transport", "What are the two dead conducting elements of xylem and what direction do they transport?",
         "Xylem Vessels and Tracheids. They transport water and dissolved mineral ions strictly in a UNIDIRECTIONAL upward path from roots to leaves, driven by transpirational pull."),
        
        ("Phloem Translocation", "What are the conducting cells of phloem and what direction does translocation occur?",
         "Sieve Tubes supported by Companion Cells. They translocate soluble organic photoassimilates (sucrose) in a BIDIRECTIONAL (multi-directional) manner from Source to Sink tissues."),
        
        ("Limiting Factors", "What is Blackman's Law of Limiting Factors in plant photosynthesis?",
         "When a physiological process is conditioned as to its rapidity by several separate factors, its rate is limited by the pace of the factor that is nearest to its minimal value (most scarce)."),
        
        ("Masked Pigments in Coleus", "Why can non-green variegated leaves (e.g. Coleus) perform active photosynthesis?",
         "They contain normal quantities of green chlorophyll! The green pigment is simply masked and hidden from view by heavy concentrations of red/purple anthocyanins and yellow carotenoids."),
        
        ("Starch Iodine Test", "What chemical changes occur when iodine solution touches active photosynthetic leaf tissue?",
         "Iodine interacts with the helical coils of amylose starch molecules, forming a characteristic dark BLUE-BLACK polyiodide complex. Tissues devoid of starch remain pale brown/yellow."),
        
        ("Moll's Half-Leaf Experiment", "What is the specific scientific role of Potassium Hydroxide (KOH) in Moll's experiment?",
         "KOH vigorously absorbs and binds gaseous carbon dioxide (2KOH + CO₂ → K₂CO₃ + H₂O), completely starving the enclosed leaf half of CO₂ to prove its indispensability for photosynthesis."),
        
        ("Hydrilla Experiment", "Why is Hydrilla sprig ideal for demonstrating oxygen evolution in laboratory tests?",
         "Hydrilla is a submerged aquatic hydrophyte. Gaseous oxygen released during photosynthesis cannot escape invisibly into air; instead, it bubbles continuously through water for collection."),
        
        ("Plant Respiration Organs", "Name four distinct anatomical structures plants utilize for cellular aeration.",
         "(1) Foliar Stomata (Leaves), (2) Woody Stem Lenticels (Bark), (3) Root Hairs (Soil air spaces), and (4) Mangrove Pneumatophores (Breathing roots in salt marshes)."),
        
        ("The Compensation Point", "Define the botanical Compensation Point observed during dawn and twilight.",
         "The exact light intensity where the rate of Photosynthesis precisely equals the rate of Cellular Respiration. Volume of O₂ produced equals O₂ consumed; net atmospheric gas exchange is zero!"),
        
        ("Transpirational Pull", "What physical forces generate the continuous ascent of sap in tall forest trees?",
         "Water evaporation from leaf stomata generates negative hydrostatic suction (Transpirational Pull). Cohesion between water molecules and adhesion to xylem walls maintains an unbroken column."),
        
        ("Ancient Vrikshayurveda", "Who authored the 10th-century Indian treatise Vrikshayurveda and what did it cover?",
         "Authored by Surapala. It systematically codified arbori-horticulture: seed germination treatments, soil diagnosis, organic bio-fertilizers (*Kunapajala*), and foliar pest treatments."),
        
        ("Rustom Hormusji Dastur", "What was Professor Rustom H. Dastur's primary contribution to Indian botanical science?",
         "Pioneer of Indian Plant Physiology. Conducted landmark empirical research on chlorophyll photochemical energy absorption, cotton foliar physiology, and plant water-relations in India."),
        
        ("Xerophytic Spines", "Why are cactus leaves modified into spines and what organ takes over photosynthesis?",
         "Leaves are modified into sharp spines to eliminate transpirational water loss and deter grazers. The succulent green flattened stem (phylloclade) contains chlorophyll and manufactures all food.")
    ]

    cards_html = []
    for idx, (title, front, back) in enumerate(flashcards_data, 1):
        card = f"""      <div class="flashcard-3d h-56 cursor-pointer select-none" onclick="this.classList.toggle('flipped'); flipFlashcard(this)">
        <div class="flashcard-inner relative w-full h-full transition-transform duration-500 transform-gpu">
          <!-- Front -->
          <div class="flashcard-front absolute inset-0 p-5 rounded-2xl bg-slate-950 border border-slate-800 hover:border-emerald-500/50 flex flex-col justify-between transition-colors shadow-lg">
            <div class="flex items-center justify-between">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300">CARD #{idx}</span>
              <i class="fas fa-sync text-xs text-slate-500"></i>
            </div>
            <div>
              <div class="text-[11px] font-mono text-emerald-400 uppercase font-semibold">{esc(title)}</div>
              <p class="text-xs md:text-sm font-bold text-white mt-1 leading-snug">{esc(front)}</p>
            </div>
            <div class="text-[10px] text-slate-500 font-mono flex items-center gap-1">
              <i class="fas fa-hand-pointer text-[9px]"></i> Tap to flip for verified answer
            </div>
          </div>
          <!-- Back -->
          <div class="flashcard-back absolute inset-0 p-5 rounded-2xl bg-emerald-950/90 border border-emerald-500/50 flex flex-col justify-between transition-colors shadow-lg">
            <div class="flex items-center justify-between">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-400 text-slate-950">VERIFIED ANSWER</span>
              <i class="fas fa-check-circle text-xs text-emerald-400"></i>
            </div>
            <p class="text-xs text-emerald-100 leading-relaxed overflow-y-auto max-h-36 pr-1">{esc(back)}</p>
            <div class="text-[10px] text-emerald-300/80 font-mono">Tap again to flip back</div>
          </div>
        </div>
      </div>"""
        cards_html.append(card)
    return "\n".join(cards_html)

def build_tab_googlehub():
    modules = [
        {"num": 1, "domain": "PLANT GROWTH", "color": "emerald", "icon": "fas fa-seedling",
         "title": "Vegetative vs Reproductive Growth & Ancient Wisdom",
         "desc": "Morphological milestones, Pots A/B/C empirical abiotic factor investigation, and Vrikshayurveda heritage.",
         "anchors": ["Vegetative internode extension", "Reproductive floral anthesis", "Pots A/B/C sunlight & water controls", "Surapala's Vrikshayurveda arboriculture"],
         "yt_query": "Class+7+Science+Plant+Growth+Dynamics+Pots+Experiment",
         "google_query": "Life+Processes+in+Plants+growth+phases+Vrikshayurveda"},

        {"num": 2, "domain": "BIOENERGETICS", "color": "amber", "icon": "fas fa-sun",
         "title": "Autotrophic Nutrition & The Solar Spectrum",
         "desc": "Photosynthetic producers, cosmic energy conversion, and chlorophyll blue/red absorption spectra.",
         "anchors": ["Autotrophic vs heterotrophic modes", "Producers at trophic pyramid base", "Sun as cosmic ultimate energy origin", "Blue-red absorption & green reflection"],
         "yt_query": "Class+7+Biology+Modes+of+Nutrition+Autotrophic+Heterotrophic",
         "google_query": "Autotrophic+nutrition+producers+chlorophyll+absorption+spectrum"},

        {"num": 3, "domain": "BIOCHEMISTRY", "color": "cyan", "icon": "fas fa-microscope",
         "title": "Photosynthesis Balanced Reaction & Chloroplast Anatomy",
         "desc": "Balanced biochemical equation, photolysis of water, and chloroplast double membrane thylakoids.",
         "anchors": ["6CO2 + 12H2O balanced reaction", "Hexose glucose carbohydrate synthesis", "Thylakoid grana & hydrophilic stroma", "Hydrilla O2 evolution demonstration"],
         "yt_query": "Class+7+Science+Photosynthesis+Balanced+Chemical+Equation",
         "google_query": "Photosynthesis+balanced+equation+chloroplast+ultrastructure"},

        {"num": 4, "domain": "PHYSIOLOGY", "color": "purple", "icon": "fas fa-expand-alt",
         "title": "Stomatal Guard Cell Turgor Mechanics",
         "desc": "Potassium ion fluxes, endosmosis/exosmosis, and crescent guard cell opening/closing.",
         "anchors": ["Active K+ ion accumulation", "Turgid swelling pulls aperture open", "Flaccid limp recoil seals stomatal pore", "Transpiration vs CO2 intake regulation"],
         "yt_query": "Class+7+Science+How+Stomata+Open+and+Close+Animation",
         "google_query": "Stomatal+opening+and+closing+guard+cells+turgor+pressure"},

        {"num": 5, "domain": "ECOLOGICAL KINETICS", "color": "teal", "icon": "fas fa-flask",
         "title": "Limiting Factors & Masked Foliar Pigments",
         "desc": "Blackman's Law, temperature enzyme denaturation, Moll's half-leaf proof, and variegated Coleus.",
         "anchors": ["Light & CO2 concentration limits", "Thermal denaturation above 40C", "Variegated Coleus masked chlorophyll", "Molls half-leaf KOH CO2 essentiality"],
         "yt_query": "Class+7+Science+Factors+Affecting+Photosynthesis+Experiments",
         "google_query": "Limiting+factors+photosynthesis+Moll+half+leaf+experiment+Coleus"},

        {"num": 6, "domain": "VASCULAR TRANSPORT", "color": "blue", "icon": "fas fa-water",
         "title": "Xylem Ascent of Sap & Transpirational Suction",
         "desc": "Non-living vessels and tracheids, cohesion-tension transpirational pull, and Balsam twig eosin test.",
         "anchors": ["Unidirectional root-to-leaf conduction", "Transpirational pull suction dynamics", "Cohesion & adhesion in xylem vessels", "Balsam twig red dye transverse section"],
         "yt_query": "Class+7+Science+Transportation+in+Plants+Xylem+and+Phloem",
         "google_query": "Xylem+ascent+of+sap+transpirational+pull+Balsam+twig+experiment"},

        {"num": 7, "domain": "TRANSLOCATION", "color": "indigo", "icon": "fas fa-arrows-alt-v",
         "title": "Phloem Organic Translocation & Source-Sink Dynamics",
         "desc": "Living sieve tubes and companion cells, bidirectional sucrose translocation, and metabolic loading.",
         "anchors": ["Living sieve tubes & perforated plates", "Nucleated companion cell active loading", "Bidirectional flow from source to sink", "Sucrose transport to roots & fruits"],
         "yt_query": "Class+7+Science+Phloem+Translocation+of+Food+Animation",
         "google_query": "Phloem+translocation+sieve+tubes+companion+cells+source+sink"},

        {"num": 8, "domain": "RESPIRATION", "color": "rose", "icon": "fas fa-wind",
         "title": "Plant Cellular Respiration & Diurnal Balance",
         "desc": "Continuous 24-hour aerobic bioenergetics, lenticels, root hairs, pneumatophores, and Compensation Point.",
         "anchors": ["24-hour aerobic ATP production", "Lenticels & mangrove pneumatophores", "Day vs night gaseous exchange balance", "Dawn & dusk Compensation Point"],
         "yt_query": "Class+7+Science+Respiration+in+Plants+Day+and+Night",
         "google_query": "Respiration+in+plants+stomata+lenticels+pneumatophores+compensation+point"}
    ]

    cards_html = []
    color_map = {
        "emerald": ("bg-emerald-500/20 text-emerald-300", "text-emerald-400"),
        "amber": ("bg-amber-500/20 text-amber-300", "text-amber-400"),
        "cyan": ("bg-cyan-500/20 text-cyan-300", "text-cyan-400"),
        "purple": ("bg-purple-500/20 text-purple-300", "text-purple-400"),
        "teal": ("bg-teal-500/20 text-teal-300", "text-teal-400"),
        "blue": ("bg-blue-500/20 text-blue-300", "text-blue-400"),
        "indigo": ("bg-indigo-500/20 text-indigo-300", "text-indigo-400"),
        "rose": ("bg-rose-500/20 text-rose-300", "text-rose-400"),
    }

    for m in modules:
        badge_cls, icon_cls = color_map.get(m["color"], ("bg-cyan-500/20 text-cyan-300", "text-cyan-400"))
        anchors_li = "".join([
            f"""<li class="flex items-start gap-2 text-slate-300 text-xs"><i class="fas fa-check-circle text-emerald-400 mt-0.5 shrink-0"></i><span>{a}</span></li>"""
            for a in m["anchors"]
        ])
        card = f"""    <div class="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 hover:border-slate-700 transition-all space-y-4 flex flex-col justify-between">
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono {badge_cls} font-bold">{m["domain"]}</span>
          <span class="text-xs text-slate-500 font-mono">Module #{m["num"]}</span>
        </div>
        <div class="flex items-start gap-3 pt-1">
          <div class="w-10 h-10 rounded-2xl bg-slate-800 {icon_cls} flex items-center justify-center text-lg shrink-0">
            <i class="{m["icon"]}"></i>
          </div>
          <div>
            <h4 class="text-base font-bold text-white leading-snug">{m["title"]}</h4>
            <p class="text-xs text-slate-400 mt-1 leading-relaxed">{m["desc"]}</p>
          </div>
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-2">
          <div class="text-[10px] font-mono uppercase text-slate-400 font-bold">Key Conceptual Anchors</div>
          <ul class="space-y-1.5">
            {anchors_li}
          </ul>
        </div>
      </div>

      <div class="flex items-center gap-2 pt-3 border-t border-slate-800/80">
        <a href="https://www.youtube.com/results?search_query={m["yt_query"]}" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-3 rounded-xl bg-red-600/20 hover:bg-red-600 text-red-300 hover:text-white text-xs font-semibold text-center transition-all flex items-center justify-center gap-1.5">
          <i class="fab fa-youtube"></i> Video Lectures
        </a>
        <a href="https://www.google.com/search?q={m["google_query"]}" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 px-3 rounded-xl bg-sky-600/20 hover:bg-sky-600 text-sky-300 hover:text-white text-xs font-semibold text-center transition-all flex items-center justify-center gap-1.5">
          <i class="fab fa-google"></i> Web Research
        </a>
      </div>
    </div>"""
        cards_html.append(card)

    all_cards = "\n\n".join(cards_html)
    return f"""<!-- ========================================== -->
<!-- 12. RESEARCH & VIDEO HUB (tabGoogleHub)    -->
<!-- ========================================== -->
<div id="tabGoogleHub" class="tab-pane hidden space-y-8 animate-fadeIn">
  <!-- Header Title -->
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-5">
    <div>
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/20 text-cyan-300 text-xs font-semibold uppercase tracking-wider mb-2">
        <i class="fab fa-google"></i> Multimodal Research &amp; Video Hub
      </div>
      <h2 class="text-3xl font-extrabold text-white font-heading">Curated Video Lectures &amp; Knowledge Vault (8 Topics)</h2>
      <p class="text-sm text-slate-400 mt-1">Zero-rot verified search routes, visual lectures, laboratory demonstrations, and conceptual deep-dives across Life Processes in Plants.</p>
    </div>
  </div>

  <!-- Topics Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
{all_cards}
  </div>
</div>
"""
