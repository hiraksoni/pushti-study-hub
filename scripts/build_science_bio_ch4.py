# -*- coding: utf-8 -*-
"""
Master Build Script for Class 7 Science (Biology) Chapter 4: "Life Processes in Plants"
Assembles: chapters/science/science_bio_ch4.html
Updates: science_index.html
"""

import os
import sys
import json
import re

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))

from generate_bio4_tabs import (
    build_tab_primer,
    build_tab_growth,
    build_tab_nutrition,
    build_tab_photosynthesis,
    build_tab_factors,
    build_tab_transport,
    build_tab_respiration,
    build_tab_activities,
    build_tab_textbook,
    build_tab_drills,
    build_tab_traps,
    build_tab_googlehub
)

sys.stdout.reconfigure(encoding='utf-8')

print("Starting master compilation for Biology Chapter 4...")

# Load Authoritative KB
kb_path = 'KB Files/biology/ch4_life_processes_plants/bio_ch4_life_processes_plants.json'
with open(kb_path, 'r', encoding='utf-8') as f:
    kb_data = json.load(f)

questions = kb_data['assessment_items']
theory_modules = kb_data['theory_summary']

obj_types = ['mcq', 'tf', 'true_false', 'fib', 'fill_in_the_blank', 'assertion_reason', 'match', 'matching']
obj_questions = [q for q in questions if q.get('type') in obj_types]
subj_questions = [q for q in questions if q.get('type') not in obj_types]

print(f"Loaded {len(questions)} items ({len(obj_questions)} objective, {len(subj_questions)} subjective).")

# Load CSS and JavaScript
with open('scripts/bio3_style.css', 'r', encoding='utf-8') as f:
    bio_styles = f.read()

with open('scripts/bio_common_app.js', 'r', encoding='utf-8') as f:
    bio_common_js = f.read()

# Replace any legacy keys
bio_common_js = bio_common_js.replace("bio3_dock_pinned", "bio4_dock_pinned")

with open('scripts/bio_jump_to_top.js', 'r', encoding='utf-8') as f:
    bio_jump_js = f.read()

# Build all 12 Tab Panes
tab1 = build_tab_primer()
tab2 = build_tab_growth()
tab3 = build_tab_nutrition()
tab4 = build_tab_photosynthesis()
tab5 = build_tab_factors()
tab6 = build_tab_transport()
tab7 = build_tab_respiration()
tab8 = build_tab_activities()
tab9 = build_tab_textbook(subj_questions)
tab10 = build_tab_drills(obj_questions)
tab11 = build_tab_traps()
tab12 = build_tab_googlehub()

# Assemble Main Document
html_document = f"""<!DOCTYPE html>
<html lang="en" class="dark" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Life Processes in Plants — Science Biology | Pushti Study Hub</title>
  
  <!-- Inter, Outfit & Space Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
            heading: ['Outfit', 'sans-serif'],
            mono: ['Space Mono', 'monospace'],
          }},
          colors: {{
            bio: {{
              50: '#f0fdf4', 100: '#dcfce7', 200: '#bbf7d0', 300: '#86efac', 400: '#4ade80',
              500: '#22c55e', 600: '#16a34a', 700: '#15803d', 800: '#166534', 900: '#14532d',
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- FontAwesome 6.4.0 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
{bio_styles}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 antialiased min-h-screen flex flex-col font-sans selection:bg-emerald-500/30 selection:text-emerald-200 transition-colors duration-300">

  <!-- ==================== TOP SITE HEADER (54px) ==================== -->
  <header class="sticky top-0 z-50 bg-slate-900/95 dark:bg-slate-950/95 backdrop-blur-md border-b border-slate-800 px-4 lg:px-8 py-2.5 h-[54px] flex items-center justify-between transition-colors duration-300">
    <!-- Left: Breadcrumbs -->
    <nav class="flex items-center gap-2 text-sm text-slate-400 overflow-x-auto whitespace-nowrap">
      <a href="../../index.html" class="flex items-center gap-1.5 hover:text-emerald-400 transition-colors font-medium text-slate-300">
        <i class="fas fa-home text-xs"></i>
        <span>Home</span>
      </a>
      <span class="text-slate-600">/</span>
      <a href="../../science_index.html" class="hover:text-emerald-400 transition-colors font-medium text-slate-300">
        Science
      </a>
      <span class="text-slate-600">/</span>
      <span class="text-emerald-400 font-semibold truncate">Biology Ch.4: Life Processes in Plants</span>
    </nav>

    <!-- Right: Header Controls -->
    <div class="flex items-center gap-3">
      <!-- Session Timer Badge -->
      <div class="hidden sm:flex items-center gap-1.5 px-3 py-1 rounded-xl bg-slate-800/80 border border-slate-700/60 text-xs font-mono text-emerald-400">
        <i class="fas fa-clock text-[10px]"></i>
        <span id="sessionTimerDisplay">00:00</span>
      </div>
      <!-- Quick Jump to Mid-Term / Test Hub -->
      <a href="test_silver_bells_midterm_science.html" class="hidden md:inline-flex items-center gap-1.5 px-3 py-1 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold transition-all">
        <i class="fas fa-file-signature text-xs"></i>
        <span>Mid-Term Exam</span>
      </a>
      <!-- Theme Toggle -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors cursor-pointer" title="Toggle Light/Dark Theme">
        <i id="themeToggleIcon" class="fas fa-moon text-sm"></i>
      </button>
    </div>
  </header>

  <!-- ==================== MAIN SHELL (SIDEBAR DOCK + CONTENT) ==================== -->
  <div class="flex flex-1 relative">

    <!-- ==================== COLLAPSIBLE VERTICAL DOCK RAIL ==================== -->
    <aside id="sidebarDock" class="sidebar-dock group" aria-label="Chapter Navigation">
      <div class="flex flex-col gap-1.5 p-2">
        
        <!-- Tab 1: Primer -->
        <button id="navBtn-tabPrimer" onclick="switchTab('tabPrimer', this)" class="nav-tab-btn active flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="1. Launchpad Primer">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-emerald-400">
            <i class="fas fa-leaf text-base"></i>
            <span class="w-2 h-2 rounded-full bg-emerald-400 absolute top-0.5 right-0.5 ring-2 ring-slate-900 animate-pulse"></span>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-emerald-400">Launchpad</span>
            <span class="font-medium text-sm text-slate-200">Primer &amp; Roadmap</span>
          </div>
        </button>

        <!-- Tab 2: Growth Dynamics -->
        <button id="navBtn-tabGrowth" onclick="switchTab('tabGrowth', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="2. Growth &amp; Ancient Insights">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-emerald-400">
            <i class="fas fa-seedling text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-emerald-400">Plant Growth</span>
            <span class="font-medium text-sm text-slate-200">Dynamics &amp; Pots</span>
          </div>
        </button>

        <!-- Tab 3: Modes of Nutrition -->
        <button id="navBtn-tabNutrition" onclick="switchTab('tabNutrition', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="3. Nutrition &amp; Solar Spectrum">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-teal-400">
            <i class="fas fa-sun text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-teal-400">Nutrition</span>
            <span class="font-medium text-sm text-slate-200">Modes &amp; The Sun</span>
          </div>
        </button>

        <!-- Tab 4: Photosynthesis & Stomata -->
        <button id="navBtn-tabPhotosynthesis" onclick="switchTab('tabPhotosynthesis', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="4. Photosynthesis &amp; Stomata">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-cyan-400">
            <i class="fas fa-microscope text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-cyan-400">Photosynthesis</span>
            <span class="font-medium text-sm text-slate-200">Chloroplasts &amp; Stomata</span>
          </div>
        </button>

        <!-- Tab 5: Limiting Factors -->
        <button id="navBtn-tabFactors" onclick="switchTab('tabFactors', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="5. Limiting Factors &amp; Starch">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-amber-400">
            <i class="fas fa-flask text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-amber-400">Limiting Factors</span>
            <span class="font-medium text-sm text-slate-200">Factors &amp; Starch</span>
          </div>
        </button>

        <!-- Tab 6: Vascular Transport -->
        <button id="navBtn-tabTransport" onclick="switchTab('tabTransport', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="6. Vascular Conduction">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-blue-400">
            <i class="fas fa-water text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-blue-400">Vascular Conduction</span>
            <span class="font-medium text-sm text-slate-200">Xylem &amp; Phloem</span>
          </div>
        </button>

        <!-- Tab 7: Plant Respiration -->
        <button id="navBtn-tabRespiration" onclick="switchTab('tabRespiration', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="7. Plant Respiration &amp; Day/Night">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-purple-400">
            <i class="fas fa-wind text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-purple-400">Respiration</span>
            <span class="font-medium text-sm text-slate-200">24h Bioenergetics</span>
          </div>
        </button>

        <!-- Tab 8: NCERT Lab Activities -->
        <button id="navBtn-tabActivities" onclick="switchTab('tabActivities', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="8. NCERT Lab Activities">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-emerald-400">
            <i class="fas fa-vial text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-emerald-400">Laboratories</span>
            <span class="font-medium text-sm text-slate-200">NCERT Activities</span>
          </div>
        </button>

        <!-- Tab 9: Solved Textbook Q&A -->
        <button id="navBtn-tabTextbook" onclick="switchTab('tabTextbook', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="9. Solved Textbook Q&amp;A (69 Qs)">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-emerald-400">
            <i class="fas fa-book-open text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-emerald-400">Textbook Solved</span>
            <span class="font-medium text-sm text-slate-200">Q&amp;A Repository (69)</span>
          </div>
        </button>

        <!-- Tab 10: Interactive Drills -->
        <button id="navBtn-tabDrills" onclick="switchTab('tabDrills', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="10. Interactive Drills (126 Qs)">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-amber-400">
            <i class="fas fa-check-circle text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-amber-400">Adaptive Drills</span>
            <span class="font-medium text-sm text-slate-200">OMR Test Bank (126)</span>
          </div>
        </button>

        <!-- Tab 11: Exam Traps & Flashcards -->
        <button id="navBtn-tabTraps" onclick="switchTab('tabTraps', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="11. Exam Traps &amp; Flashcards">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-rose-400">
            <i class="fas fa-skull-crossbones text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-rose-400">Exam Traps</span>
            <span class="font-medium text-sm text-slate-200">Pitfalls &amp; 3D Cards</span>
          </div>
        </button>

        <!-- Tab 12: Multimodal Google Hub -->
        <button id="navBtn-tabGoogleHub" onclick="switchTab('tabGoogleHub', this)" class="nav-tab-btn flex items-center w-full h-11 px-2.5 rounded-xl border border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition-all text-left relative overflow-hidden cursor-pointer" title="12. Research &amp; Video Hub">
          <div class="tab-indicator-pill"></div>
          <div class="w-9 min-w-[36px] max-w-[36px] h-9 flex items-center justify-center relative flex-shrink-0 text-cyan-400">
            <i class="fab fa-google text-base"></i>
          </div>
          <div class="tab-label-group">
            <span class="font-semibold text-xs tracking-wide uppercase text-cyan-400">Research &amp; Videos</span>
            <span class="font-medium text-sm text-slate-200">Google Hub (8 Topics)</span>
          </div>
        </button>

      </div>

      <!-- Dock Footer: Theme Switcher & Pin Sidebar -->
      <div class="sidebar-footer p-2 border-t border-slate-800/80 space-y-2">
        <button id="pinToggleBtn" onclick="toggleSidebarPin()" class="w-full h-10 px-2 rounded-xl border transition-all flex items-center justify-center gap-2 cursor-pointer relative overflow-hidden bg-slate-800/80 border-slate-700/60 text-slate-400 hover:text-slate-200 hover:bg-slate-700/80" title="Sidebar: Unpinned (Compact Dock - tap to lock open)" aria-label="Pin Sidebar Navigation" aria-pressed="false">
          <i id="pinToggleIcon" class="fas fa-thumbtack text-xs -rotate-45 transition-transform duration-300"></i>
          <span id="pinStatusDot" class="w-1.5 h-1.5 rounded-full bg-slate-600 absolute top-1.5 right-1.5 transition-colors"></span>
          <div class="tab-label-group">
            <span id="pinStatusText" class="text-xs font-semibold tracking-wide uppercase text-slate-400">Compact Dock</span>
            <span id="pinActionHint" class="text-[10px] font-mono text-slate-500">Tap to lock</span>
          </div>
        </button>
      </div>
    </aside>

    <!-- ==================== MAIN APPLICATION CONTENT ==================== -->
    <main class="main-app-content flex-1 max-w-7xl mx-auto p-4 sm:p-6 lg:p-8 space-y-8 min-w-0 transition-all duration-300">
{tab1}

{tab2}

{tab3}

{tab4}

{tab5}

{tab6}

{tab7}

{tab8}

{tab9}

{tab10}

{tab11}

{tab12}
    </main>

  </div>

  <!-- Universal Jump to Top Floating Button -->
  <button id="pushti-jump-to-top" class="pushti-jump-to-top" title="Jump to Top" aria-label="Jump to Top">
    <svg viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
  </button>

  <!-- ==================== SCRIPTS ==================== -->
  <script>
{bio_common_js}
  </script>

  <script>
{bio_jump_js}
  </script>
</body>
</html>
"""

output_path = 'chapters/science/science_bio_ch4.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_document)

print(f"Successfully generated {output_path} ({len(html_document)} bytes, {len(html_document.splitlines())} lines).")
