"""
Vector SVG Diagram Engine for Olympiad Web Applications
Provides clean, scalable, theme-aware SVGs for question setups (stimuli),
ensuring question cards contain the problem figure rather than answer keys.
"""

def get_question_svg(paper_key, q_num):
    pk = paper_key.lower().replace("_set_", "_")

    # -------------------------------------------------------------
    # 1. NSO 2022-23 SET-A
    # -------------------------------------------------------------
    if pk in ["nso_2022_23_a", "nso_2022_23_set_a"]:
        if q_num == 4:
            # Water Image Problem Setup: Given Figure + 4 Candidate Options (A, B, C, D)
            return """
            <svg width="440" height="260" viewBox="0 0 440 260" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.18); border-radius:12px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Given Object Box -->
                <g transform="translate(180, 10)">
                    <text x="40" y="-2" text-anchor="middle" fill="#94A3B8" font-size="10" font-weight="bold">Given Figure</text>
                    <rect x="0" y="5" width="80" height="75" fill="rgba(255,255,255,0.03)" stroke="#38BDF8" stroke-width="1.8" rx="6" />
                    <!-- Stick figure -->
                    <circle cx="40" cy="24" r="11" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="36" cy="22" r="1.3" fill="#E2E8F0" /><circle cx="44" cy="22" r="1.3" fill="#E2E8F0" />
                    <line x1="40" y1="35" x2="40" y2="60" stroke="#E2E8F0" stroke-width="1.8" />
                    <!-- Left arm with arrow pointing down -->
                    <path d="M 40 45 L 24 45 L 24 58" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <polygon points="21,56 24,62 27,56" fill="#E2E8F0" />
                    <!-- Right arm with dot pointing down -->
                    <path d="M 40 45 L 56 45 L 56 56" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="56" cy="58" r="2.8" fill="#E2E8F0" />
                </g>
                
                <!-- Water Surface Boundary -->
                <line x1="20" y1="102" x2="420" y2="102" stroke="#38BDF8" stroke-width="2" stroke-dasharray="6,4" />
                <text x="220" y="116" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="700" letter-spacing="1">WATER SURFACE (REFLECTION)</text>
                
                <!-- Candidate Options Row: (A), (B), (C), (D) -->
                <!-- Option A: Laterally Inverted (Left-Right swapped) -->
                <g transform="translate(25, 130)">
                    <rect x="0" y="0" width="75" height="75" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" rx="6" />
                    <line x1="37" y1="18" x2="37" y2="43" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="37" cy="54" r="11" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <!-- Dot on left, arrow on right (swapped) -->
                    <path d="M 37 32 L 21 32 L 21 21" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="21" cy="19" r="2.8" fill="#E2E8F0" />
                    <path d="M 37 32 L 53 32 L 53 19" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <polygon points="50,21 53,15 56,21" fill="#E2E8F0" />
                    <text x="37" y="93" text-anchor="middle" fill="#94A3B8" font-size="11" font-weight="bold">(A)</text>
                </g>

                <!-- Option B: Upright (Not Inverted Vertically) -->
                <g transform="translate(130, 130)">
                    <rect x="0" y="0" width="75" height="75" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" rx="6" />
                    <circle cx="37" cy="24" r="11" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <line x1="37" y1="35" x2="37" y2="60" stroke="#E2E8F0" stroke-width="1.8" />
                    <path d="M 37 45 L 21 45 L 21 58" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <polygon points="18,56 21,62 24,56" fill="#E2E8F0" />
                    <path d="M 37 45 L 53 45 L 53 56" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="53" cy="58" r="2.8" fill="#E2E8F0" />
                    <text x="37" y="93" text-anchor="middle" fill="#94A3B8" font-size="11" font-weight="bold">(B)</text>
                </g>

                <!-- Option C: Inverted head but arms pointing DOWN -->
                <g transform="translate(235, 130)">
                    <rect x="0" y="0" width="75" height="75" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" rx="6" />
                    <line x1="37" y1="18" x2="37" y2="43" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="37" cy="54" r="11" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <path d="M 37 32 L 21 32 L 21 45" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <polygon points="18,43 21,49 24,43" fill="#E2E8F0" />
                    <path d="M 37 32 L 53 32 L 53 43" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="53" cy="45" r="2.8" fill="#E2E8F0" />
                    <text x="37" y="93" text-anchor="middle" fill="#94A3B8" font-size="11" font-weight="bold">(C)</text>
                </g>

                <!-- Option D -->
                <g transform="translate(340, 130)">
                    <rect x="0" y="0" width="75" height="75" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" rx="6" />
                    <!-- Torso at top -->
                    <line x1="37" y1="18" x2="37" y2="43" stroke="#E2E8F0" stroke-width="1.8" />
                    <!-- Head at bottom -->
                    <circle cx="37" cy="54" r="11" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="33" cy="56" r="1.3" fill="#E2E8F0" /><circle cx="41" cy="56" r="1.3" fill="#E2E8F0" />
                    <!-- Left arm with arrow pointing UP -->
                    <path d="M 37 32 L 21 32 L 21 19" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <polygon points="18,21 21,15 24,21" fill="#E2E8F0" />
                    <!-- Right arm with dot pointing UP -->
                    <path d="M 37 32 L 53 32 L 53 21" fill="none" stroke="#E2E8F0" stroke-width="1.8" />
                    <circle cx="53" cy="19" r="2.8" fill="#E2E8F0" />
                    <text x="37" y="93" text-anchor="middle" fill="#94A3B8" font-size="11" font-weight="bold">(D)</text>
                </g>
            </svg>
            """

        elif q_num == 6:
            # Overlapping Venn Diagram
            return """
            <svg width="280" height="190" viewBox="0 0 280 190" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Circle -->
                <circle cx="110" cy="95" r="55" fill="rgba(99, 102, 241, 0.15)" stroke="#6366F1" stroke-width="2" />
                <!-- Triangle -->
                <polygon points="140,25 80,145 200,145" fill="rgba(16, 185, 129, 0.15)" stroke="#10B981" stroke-width="2" />
                <!-- Rectangle -->
                <rect x="100" y="65" width="110" height="70" fill="rgba(245, 158, 11, 0.15)" stroke="#F59E0B" stroke-width="2" rx="4" />
                
                <!-- Region Numbers -->
                <text x="80" y="80" fill="#E2E8F0" font-size="12" font-weight="bold">5</text>
                <text x="140" y="55" fill="#E2E8F0" font-size="12" font-weight="bold">1</text>
                <text x="185" y="115" fill="#E2E8F0" font-size="12" font-weight="bold">6</text>
                <text x="105" y="125" fill="#E2E8F0" font-size="12" font-weight="bold">4</text>
                <text x="160" y="125" fill="#E2E8F0" font-size="12" font-weight="bold">2</text>
                <text x="145" y="85" fill="#E2E8F0" font-size="12" font-weight="bold">7</text>
                <!-- Common to All Three -->
                <text x="130" y="109" text-anchor="middle" fill="#E2E8F0" font-size="12" font-weight="bold">3</text>
            </svg>
            """

        elif q_num == 9:
            # Unfolded Dice Net
            return """
            <svg width="240" height="180" viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <g transform="translate(60, 15)">
                    <!-- Face 1 (Top) -->
                    <rect x="40" y="0" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <circle cx="60" cy="20" r="5" fill="#E2E8F0" />
                    
                    <!-- Face 2 (Branch Left) -->
                    <rect x="0" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="20" y="66" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="bold">©</text>
                    
                    <!-- Face 3 (Center) -->
                    <rect x="40" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="66" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="bold">@</text>
                    
                    <!-- Face 4 (Branch Right) -->
                    <rect x="80" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="100" y="66" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="bold">#</text>
                    
                    <!-- Face 5 (Below Center) -->
                    <rect x="40" y="80" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="106" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="bold">★</text>
                    
                    <!-- Face 6 (Bottom) -->
                    <rect x="40" y="120" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="146" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="bold">%</text>
                </g>
            </svg>
            """

        elif q_num == 13:
            # Electric Circuit with Compass
            return """
            <svg width="280" height="170" viewBox="0 0 280 170" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Circuit Loop -->
                <rect x="40" y="30" width="200" height="110" fill="none" stroke="#64748B" stroke-width="2.5" rx="8" />
                
                <!-- Batteries on Top Wire -->
                <rect x="90" y="22" width="100" height="18" fill="var(--surface)" />
                <!-- Cell 1 (+ -) -->
                <line x1="100" y1="20" x2="100" y2="40" stroke="#E2E8F0" stroke-width="3" />
                <line x1="110" y1="25" x2="110" y2="35" stroke="#E2E8F0" stroke-width="1.5" />
                <!-- Cell 2 (- +) -->
                <line x1="140" y1="25" x2="140" y2="35" stroke="#E2E8F0" stroke-width="1.5" />
                <line x1="150" y1="20" x2="150" y2="40" stroke="#E2E8F0" stroke-width="3" />
                <text x="125" y="16" text-anchor="middle" fill="#94A3B8" font-size="9" font-weight="bold">Cells 1 &amp; 2</text>
                
                <!-- Bulb on Right -->
                <circle cx="240" cy="85" r="14" fill="rgba(255,255,255,0.05)" stroke="#F59E0B" stroke-width="2" />
                <path d="M 233 80 Q 240 73 247 80 Q 240 92 233 80" fill="none" stroke="#F59E0B" stroke-width="1.5" />
                
                <!-- Magnetic Compass on Bottom Wire -->
                <circle cx="140" cy="140" r="16" fill="rgba(0,0,0,0.4)" stroke="#38BDF8" stroke-width="2" />
                <line x1="130" y1="140" x2="150" y2="140" stroke="#EF4444" stroke-width="2.5" />
                <text x="140" y="166" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">Compass</text>
            </svg>
            """

        elif q_num == 15:
            # Light Ray Reflection: Plane mirror, 4 identical objects P, Q, R, S and observer eye
            return """
            <svg width="270" height="160" viewBox="0 0 270 160" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Mirror Surface at Top -->
                <line x1="30" y1="30" x2="240" y2="30" stroke="#38BDF8" stroke-width="3" />
                <!-- Hatching on Back of Mirror -->
                <g stroke="#64748B" stroke-width="1">
                    <line x1="40" y1="25" x2="50" y2="30" /><line x1="70" y1="25" x2="80" y2="30" />
                    <line x1="100" y1="25" x2="110" y2="30" /><line x1="130" y1="25" x2="140" y2="30" />
                    <line x1="160" y1="25" x2="170" y2="30" /><line x1="190" y1="25" x2="200" y2="30" />
                    <line x1="220" y1="25" x2="230" y2="30" />
                </g>
                <text x="135" y="20" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="bold">Plane Mirror</text>
                
                <!-- Pins / Objects: All identically styled to prevent pre-answer leak -->
                <circle cx="50" cy="120" r="5" fill="#38BDF8" /><text x="50" y="136" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">P</text>
                <circle cx="90" cy="120" r="5" fill="#38BDF8" /><text x="90" y="136" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Q</text>
                <circle cx="130" cy="120" r="5" fill="#38BDF8" /><text x="130" y="136" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">R</text>
                <circle cx="170" cy="120" r="5" fill="#38BDF8" /><text x="170" y="136" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">S</text>
                
                <!-- Observer Eye Position -->
                <g transform="translate(220, 110)">
                    <path d="M 0 10 Q 15 0 30 10 Q 15 20 0 10 Z" fill="rgba(255,255,255,0.1)" stroke="#10B981" stroke-width="1.5" />
                    <circle cx="15" cy="10" r="4" fill="#10B981" />
                    <text x="15" y="26" text-anchor="middle" fill="#10B981" font-size="9" font-weight="bold">Eye</text>
                </g>
            </svg>
            """

        elif q_num == 16:
            # Reflection Angle (30 deg with mirror surface)
            return """
            <svg width="270" height="150" viewBox="0 0 270 150" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Mirror Surface at Bottom -->
                <line x1="20" y1="120" x2="250" y2="120" stroke="#38BDF8" stroke-width="3" />
                <line x1="135" y1="30" x2="135" y2="120" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4" />
                <text x="135" y="22" text-anchor="middle" fill="#94A3B8" font-size="10">Normal</text>
                
                <!-- Incident Ray -->
                <line x1="45" y1="65" x2="135" y2="120" stroke="#F59E0B" stroke-width="2.5" />
                <!-- 30 deg arc with surface -->
                <path d="M 80 120 A 55 55 0 0 0 95 95" fill="none" stroke="#F59E0B" stroke-width="1.5" />
                <text x="65" y="112" fill="#F59E0B" font-size="11" font-weight="bold">30°</text>
                
                <!-- Question: Angle of reflection -->
                <text x="160" y="80" fill="#38BDF8" font-size="12" font-weight="bold">∠r = ?</text>
            </svg>
            """

        elif q_num == 17:
            # Parallel Displacement-Time Graph
            return """
            <svg width="260" height="170" viewBox="0 0 260 170" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Axes -->
                <line x1="40" y1="20" x2="40" y2="135" stroke="#94A3B8" stroke-width="2" />
                <line x1="40" y1="135" x2="240" y2="135" stroke="#94A3B8" stroke-width="2" />
                <text x="140" y="155" text-anchor="middle" fill="#94A3B8" font-size="10">Time (t) →</text>
                <text x="16" y="75" text-anchor="middle" fill="#94A3B8" font-size="10" transform="rotate(-90 16 75)">Displacement (m) →</text>
                
                <!-- Object Q Line (Starts at 20m) -->
                <text x="25" y="88" fill="#38BDF8" font-size="10" font-weight="bold">20</text>
                <line x1="40" y1="85" x2="210" y2="35" stroke="#38BDF8" stroke-width="2.5" />
                <text x="220" y="38" fill="#38BDF8" font-size="11" font-weight="bold">Q</text>
                
                <!-- Object P Line (Starts at 0m, Parallel) -->
                <text x="28" y="138" fill="#10B981" font-size="10" font-weight="bold">0</text>
                <line x1="40" y1="135" x2="210" y2="85" stroke="#10B981" stroke-width="2.5" />
                <text x="220" y="88" fill="#10B981" font-size="11" font-weight="bold">P</text>
            </svg>
            """

        elif q_num == 18:
            # Convex Lens Ray Problem Setup: Incident ray parallel to axis; asks which point ray passes through
            return """
            <svg width="270" height="140" viewBox="0 0 270 140" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Principal Axis -->
                <line x1="20" y1="70" x2="250" y2="70" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4" />
                
                <!-- Convex Lens -->
                <path d="M 130 15 Q 145 70 130 125 Q 115 70 130 15 Z" fill="rgba(56, 189, 248, 0.2)" stroke="#38BDF8" stroke-width="2" />
                <circle cx="130" cy="70" r="3" fill="#94A3B8" />
                <text x="130" y="86" text-anchor="middle" fill="#94A3B8" font-size="9">O</text>
                <circle cx="180" cy="70" r="3" fill="#E2E8F0" />
                <text x="180" y="86" text-anchor="middle" fill="#E2E8F0" font-size="10" font-weight="bold">F</text>
                <circle cx="230" cy="70" r="3" fill="#E2E8F0" />
                <text x="230" y="86" text-anchor="middle" fill="#E2E8F0" font-size="10" font-weight="bold">2F</text>
                
                <!-- Incident Parallel Ray -->
                <line x1="25" y1="35" x2="130" y2="35" stroke="#F59E0B" stroke-width="2.5" />
                <!-- Prompt arrow indicating question -->
                <text x="175" y="42" fill="#38BDF8" font-size="10" font-weight="bold">After Refraction: ?</text>
            </svg>
            """

        elif q_num == 19:
            # Bar Magnet Magnetic Field Lines Problem Setup (Two opposing magnets, identical neutral test points)
            return """
            <svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <!-- Magnet 1 (Left: N top, S bottom) -->
                <rect x="75" y="40" width="40" height="70" fill="#1E293B" stroke="#64748B" stroke-width="1.8" rx="4" />
                <rect x="75" y="40" width="40" height="35" fill="rgba(239, 68, 68, 0.25)" />
                <text x="95" y="62" text-anchor="middle" fill="#EF4444" font-size="12" font-weight="bold">N</text>
                <rect x="75" y="75" width="40" height="35" fill="rgba(56, 189, 248, 0.25)" />
                <text x="95" y="97" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="bold">S</text>
                
                <!-- Magnet 2 (Right: S top, N bottom) -->
                <rect x="185" y="40" width="40" height="70" fill="#1E293B" stroke="#64748B" stroke-width="1.8" rx="4" />
                <rect x="185" y="40" width="40" height="35" fill="rgba(56, 189, 248, 0.25)" />
                <text x="205" y="62" text-anchor="middle" fill="#38BDF8" font-size="12" font-weight="bold">S</text>
                <rect x="185" y="75" width="40" height="35" fill="rgba(239, 68, 68, 0.25)" />
                <text x="205" y="97" text-anchor="middle" fill="#EF4444" font-size="12" font-weight="bold">N</text>
                
                <!-- Field Line Curves -->
                <path d="M 95 40 C 140 15, 160 15, 205 40" fill="none" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3" />
                <path d="M 95 110 C 140 135, 160 135, 205 110" fill="none" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,3" />
                
                <!-- Identically Colored Test Points (P, Q, R) to prevent pre-answer leak -->
                <circle cx="35" cy="75" r="5" fill="#38BDF8" /><text x="35" y="92" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">P</text>
                <circle cx="150" cy="75" r="5" fill="#38BDF8" /><text x="150" y="92" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Q</text>
                <circle cx="265" cy="75" r="5" fill="#38BDF8" /><text x="265" y="92" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">R</text>
            </svg>
            """

    # -------------------------------------------------------------
    # 2. IMO 2023-24 SET-B
    # -------------------------------------------------------------
    elif pk in ["imo_2023_24_b", "imo_2023_24_set_b"]:
        if q_num == 1:
            # Cube Net L, M, N, P, Q, R
            return """
            <svg width="240" height="180" viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.15); border-radius:10px; border:1px solid rgba(255,255,255,0.08);">
                <g transform="translate(60, 15)">
                    <!-- Face L -->
                    <rect x="40" y="0" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="26" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">L</text>
                    <!-- Face Q -->
                    <rect x="0" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="20" y="66" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">Q</text>
                    <!-- Face M -->
                    <rect x="40" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="66" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">M</text>
                    <!-- Face R -->
                    <rect x="80" y="40" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="100" y="66" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">R</text>
                    <!-- Face P -->
                    <rect x="40" y="80" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="106" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">P</text>
                    <!-- Face N -->
                    <rect x="40" y="120" width="40" height="40" fill="rgba(255,255,255,0.04)" stroke="#6366F1" stroke-width="1.5" />
                    <text x="60" y="146" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="bold">N</text>
                </g>
            </svg>
            """

        elif q_num in [29, 30]:
            # Shared Grouped Bar Chart for Brands P, Q, R, S, T
            return """
            <svg width="480" height="260" viewBox="0 0 480 260" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.18); border-radius:12px; border:1px solid rgba(255,255,255,0.1);">
                <!-- Chart Title & Legend -->
                <text x="240" y="24" text-anchor="middle" fill="#E2E8F0" font-size="13" font-weight="bold" font-family="'Outfit', sans-serif">Beverage Brand Preference Survey by Gender</text>
                <g transform="translate(320, 38)">
                    <rect x="0" y="0" width="14" height="10" fill="#38BDF8" rx="2" />
                    <text x="20" y="9" fill="#94A3B8" font-size="10">Males</text>
                    <rect x="65" y="0" width="14" height="10" fill="#EC4899" rx="2" />
                    <text x="85" y="9" fill="#94A3B8" font-size="10">Females</text>
                </g>
                
                <!-- Y-Axis Gridlines & Values -->
                <g stroke="rgba(255,255,255,0.07)" stroke-width="1" font-size="9" fill="#94A3B8" text-anchor="end">
                    <line x1="50" y1="210" x2="450" y2="210" /><text x="44" y="213">0</text>
                    <line x1="50" y1="175" x2="450" y2="175" /><text x="44" y="178">50</text>
                    <line x1="50" y1="140" x2="450" y2="140" /><text x="44" y="143">100</text>
                    <line x1="50" y1="105" x2="450" y2="105" /><text x="44" y="108">150</text>
                    <line x1="50" y1="70" x2="450" y2="70" /><text x="44" y="73">200</text>
                </g>
                <line x1="50" y1="50" x2="50" y2="210" stroke="#64748B" stroke-width="1.5" />
                <line x1="50" y1="210" x2="450" y2="210" stroke="#64748B" stroke-width="1.5" />
                
                <!-- Group P: Male 110, Female 130 -->
                <rect x="75" y="133" width="22" height="77" fill="#38BDF8" rx="2" /><text x="86" y="127" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">110</text>
                <rect x="100" y="119" width="22" height="91" fill="#EC4899" rx="2" /><text x="111" y="113" text-anchor="middle" fill="#EC4899" font-size="9" font-weight="bold">130</text>
                <text x="98" y="226" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Brand P</text>
                
                <!-- Group Q: Male 90, Female 150 -->
                <rect x="150" y="147" width="22" height="63" fill="#38BDF8" rx="2" /><text x="161" y="141" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">90</text>
                <rect x="175" y="105" width="22" height="105" fill="#EC4899" rx="2" /><text x="186" y="99" text-anchor="middle" fill="#EC4899" font-size="9" font-weight="bold">150</text>
                <text x="173" y="226" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Brand Q</text>
                
                <!-- Group R: Male 120, Female 110 -->
                <rect x="225" y="126" width="22" height="84" fill="#38BDF8" rx="2" /><text x="236" y="120" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">120</text>
                <rect x="250" y="133" width="22" height="77" fill="#EC4899" rx="2" /><text x="261" y="127" text-anchor="middle" fill="#EC4899" font-size="9" font-weight="bold">110</text>
                <text x="248" y="226" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Brand R</text>
                
                <!-- Group S: Male 180, Female 200 -->
                <rect x="300" y="84" width="22" height="126" fill="#38BDF8" rx="2" /><text x="311" y="78" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">180</text>
                <rect x="325" y="70" width="22" height="140" fill="#EC4899" rx="2" /><text x="336" y="64" text-anchor="middle" fill="#EC4899" font-size="9" font-weight="bold">200</text>
                <text x="323" y="226" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Brand S</text>
                
                <!-- Group T: Male 140, Female 140 -->
                <rect x="375" y="112" width="22" height="98" fill="#38BDF8" rx="2" /><text x="386" y="106" text-anchor="middle" fill="#38BDF8" font-size="9" font-weight="bold">140</text>
                <rect x="400" y="112" width="22" height="98" fill="#EC4899" rx="2" /><text x="411" y="106" text-anchor="middle" fill="#EC4899" font-size="9" font-weight="bold">140</text>
                <text x="398" y="226" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="bold">Brand T</text>
            </svg>
            """

    return None


def get_solution_svg(paper_key, q_num):
    """
    Returns authentic step-by-step vector diagrams for the solution/explanation section.
    """
    pk = paper_key.lower().replace("_set_", "_")

    if pk in ["nso_2022_23_a", "nso_2022_23_set_a"]:
        if q_num == 2:
            # Geometrically correct Direction Path Derivation:
            # 1. Start at House (Top-Right)
            # 2. Walks 7 km South (Downwards)
            # 3. Facing South -> Right hand points WEST (Leftwards on map). Walks 3 km West.
            # 4. Facing West -> Left hand points SOUTH (Downwards on map). Walks 10 km South.
            # 5. Final Facing: SOUTH
            return """
            <svg width="340" height="240" viewBox="0 0 340 240" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.2); border-radius:12px; border:1px solid rgba(255,255,255,0.1);">
                <defs>
                    <marker id="sol-arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 9 5 L 0 9 z" fill="#10B981" />
                    </marker>
                    <marker id="sol-arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 9 5 L 0 9 z" fill="#38BDF8" />
                    </marker>
                    <marker id="sol-arrow-gold" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 9 5 L 0 9 z" fill="#F59E0B" />
                    </marker>
                </defs>
                
                <!-- Compass Rose Reference (Top-Left) -->
                <g transform="translate(50, 50)">
                    <circle cx="0" cy="0" r="26" fill="rgba(255,255,255,0.02)" stroke="rgba(255,255,255,0.15)" stroke-width="1.2" />
                    <line x1="0" y1="-24" x2="0" y2="24" stroke="#94A3B8" stroke-width="1.2" />
                    <line x1="-24" y1="0" x2="24" y2="0" stroke="#94A3B8" stroke-width="1.2" />
                    <polygon points="0,-20 3.5,-3 0,0 -3.5,-3" fill="#EF4444" />
                    <polygon points="0,20 3.5,3 0,0 -3.5,3" fill="#94A3B8" />
                    <text x="0" y="-27" text-anchor="middle" fill="#EF4444" font-size="10" font-weight="bold">N</text>
                    <text x="0" y="34" text-anchor="middle" fill="#94A3B8" font-size="10" font-weight="bold">S</text>
                    <text x="31" y="3.5" text-anchor="middle" fill="#94A3B8" font-size="10" font-weight="bold">E</text>
                    <text x="-31" y="3.5" text-anchor="middle" fill="#94A3B8" font-size="10" font-weight="bold">W</text>
                </g>

                <!-- Step 1: Starting Point (House) at Top-Right -->
                <circle cx="230" cy="30" r="6" fill="#10B981" />
                <text x="242" y="34" fill="#E2E8F0" font-size="11" font-weight="bold">Starting Point (House)</text>

                <!-- Step 1: Walks 7 km South (Downwards) -->
                <line x1="230" y1="36" x2="230" y2="90" stroke="#10B981" stroke-width="3" marker-end="url(#sol-arrow-green)" />
                <text x="238" y="68" fill="#10B981" font-size="11" font-weight="600">7 km South</text>

                <!-- Step 2: Facing South, Turns to Rohan's Right -> WEST (Leftwards) -->
                <line x1="230" y1="90" x2="140" y2="90" stroke="#38BDF8" stroke-width="3" marker-end="url(#sol-arrow-blue)" />
                <text x="185" y="82" text-anchor="middle" fill="#38BDF8" font-size="10" font-weight="bold">Turns Right (West, 3 km)</text>

                <!-- Step 3: Facing West, Turns to Rohan's Left -> SOUTH (Downwards) -->
                <line x1="140" y1="90" x2="140" y2="180" stroke="#F59E0B" stroke-width="3" marker-end="url(#sol-arrow-gold)" />
                <text x="148" y="140" fill="#F59E0B" font-size="11" font-weight="600">Turns Left (10 km)</text>

                <!-- Final Position and Facing Indicator -->
                <circle cx="140" cy="186" r="6" fill="#EF4444" />
                <polygon points="140,202 135,192 145,192" fill="#EF4444" />
                <text x="140" y="218" text-anchor="middle" fill="#EF4444" font-size="12" font-weight="bold">Facing Direction: SOUTH ↓</text>
            </svg>
            """

        elif q_num == 4:
            # Water Image Solution SVG
            return """
            <svg width="280" height="180" viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.2); border-radius:12px; border:1px solid rgba(16,185,129,0.3);">
                <!-- Problem Stick Figure Top -->
                <g transform="translate(40, 15)">
                    <rect x="0" y="0" width="60" height="60" fill="rgba(255,255,255,0.02)" stroke="#94A3B8" stroke-width="1.2" rx="4" />
                    <circle cx="30" cy="18" r="9" fill="none" stroke="#E2E8F0" stroke-width="1.5" />
                    <line x1="30" y1="27" x2="30" y2="48" stroke="#E2E8F0" stroke-width="1.5" />
                    <path d="M 30 35 L 18 35 L 18 46" fill="none" stroke="#E2E8F0" stroke-width="1.5" />
                    <polygon points="15,44 18,49 21,44" fill="#E2E8F0" />
                    <path d="M 30 35 L 42 35 L 42 44" fill="none" stroke="#E2E8F0" stroke-width="1.5" />
                    <circle cx="42" cy="46" r="2.5" fill="#E2E8F0" />
                    <text x="30" y="-4" text-anchor="middle" fill="#94A3B8" font-size="9">Original</text>
                </g>

                <text x="140" y="50" text-anchor="middle" fill="#10B981" font-size="18">→</text>
                <text x="140" y="68" text-anchor="middle" fill="#10B981" font-size="10" font-weight="bold">Vertical Flip</text>

                <!-- Solution Figure (D) Bottom -->
                <g transform="translate(180, 15)">
                    <rect x="0" y="0" width="60" height="60" fill="rgba(16,185,129,0.08)" stroke="#10B981" stroke-width="1.8" rx="4" />
                    <line x1="30" y1="12" x2="30" y2="33" stroke="#10B981" stroke-width="1.5" />
                    <circle cx="30" cy="42" r="9" fill="none" stroke="#10B981" stroke-width="1.5" />
                    <path d="M 30 23 L 18 23 L 18 12" fill="none" stroke="#10B981" stroke-width="1.5" />
                    <polygon points="15,14 18,9 21,14" fill="#10B981" />
                    <path d="M 30 23 L 42 23 L 42 14" fill="none" stroke="#10B981" stroke-width="1.5" />
                    <circle cx="42" cy="12" r="2.5" fill="#10B981" />
                    <text x="30" y="-4" text-anchor="middle" fill="#10B981" font-size="9" font-weight="bold">Correct: (D)</text>
                </g>
                <text x="140" y="105" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="600">Water reflection inverts vertically only.</text>
                <text x="140" y="125" text-anchor="middle" fill="#94A3B8" font-size="10">Left and right lateral positions remain identical.</text>
            </svg>
            """

        elif q_num == 18:
            # Convex Lens Solution SVG showing ray through Focus F
            return """
            <svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.2); border-radius:12px; border:1px solid rgba(16,185,129,0.3);">
                <line x1="20" y1="75" x2="280" y2="75" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4" />
                <path d="M 140 20 Q 155 75 140 130 Q 125 75 140 20 Z" fill="rgba(56, 189, 248, 0.2)" stroke="#38BDF8" stroke-width="2" />
                <circle cx="140" cy="75" r="3" fill="#94A3B8" /><text x="140" y="92" text-anchor="middle" fill="#94A3B8" font-size="9">O</text>
                <circle cx="195" cy="75" r="4" fill="#10B981" /><text x="195" y="94" text-anchor="middle" fill="#10B981" font-size="11" font-weight="bold">F</text>
                <circle cx="250" cy="75" r="3" fill="#E2E8F0" /><text x="250" y="92" text-anchor="middle" fill="#E2E8F0" font-size="10">2F</text>
                
                <!-- Incident Ray -->
                <line x1="30" y1="40" x2="140" y2="40" stroke="#F59E0B" stroke-width="2.5" />
                <!-- Refracted Ray passing through Focus F -->
                <line x1="140" y1="40" x2="250" y2="110" stroke="#10B981" stroke-width="2.5" />
                <text x="195" y="32" text-anchor="middle" fill="#10B981" font-size="10" font-weight="bold">Ray passes through Principal Focus (F)</text>
            </svg>
            """

        elif q_num == 19:
            # Bar Magnet Neutral Point Solution SVG
            return """
            <svg width="320" height="150" viewBox="0 0 320 150" xmlns="http://www.w3.org/2000/svg" style="background:rgba(0,0,0,0.2); border-radius:12px; border:1px solid rgba(16,185,129,0.3);">
                <!-- Magnet 1 -->
                <rect x="70" y="35" width="36" height="65" fill="#1E293B" stroke="#64748B" stroke-width="1.8" rx="4" />
                <rect x="70" y="35" width="36" height="32.5" fill="rgba(239, 68, 68, 0.25)" /><text x="88" y="56" text-anchor="middle" fill="#EF4444" font-size="11" font-weight="bold">N</text>
                <rect x="70" y="67.5" width="36" height="32.5" fill="rgba(56, 189, 248, 0.25)" /><text x="88" y="88" text-anchor="middle" fill="#38BDF8" font-size="11" font-weight="bold">S</text>
                
                <!-- Magnet 2 -->
                <rect x="195" y="35" width="36" height="65" fill="#1E293B" stroke="#64748B" stroke-width="1.8" rx="4" />
                <rect x="195" y="35" width="36" height="32.5" fill="rgba(56, 189, 248, 0.25)" /><text x="213" y="56" text-anchor="middle" fill="#38BDF8" font-size="11" font-weight="bold">S</text>
                <rect x="195" y="67.5" width="36" height="32.5" fill="rgba(239, 68, 68, 0.25)" /><text x="213" y="88" text-anchor="middle" fill="#EF4444" font-size="11" font-weight="bold">N</text>
                
                <!-- Midpoint Q with canceling vectors -->
                <circle cx="150" cy="67.5" r="6" fill="#10B981" />
                <text x="150" y="86" text-anchor="middle" fill="#10B981" font-size="12" font-weight="bold">Q (B_net = 0)</text>
                <text x="150" y="125" text-anchor="middle" fill="#E2E8F0" font-size="11" font-weight="600">Neutral Point: Opposing magnetic fields cancel out at Q</text>
            </svg>
            """

    return None

