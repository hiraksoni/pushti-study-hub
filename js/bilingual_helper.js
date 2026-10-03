/**
 * Pushti Study Hub - Bilingual English & Hindi Learning Assistant
 * Provides:
 * 1. Interactive hover / tap tooltips for key vocabulary & grammar concepts
 * 2. Instant double-click / text selection lookup popup with audio & Google Translate
 * 3. Floating Quick Bilingual Search Drawer (EN <-> HI)
 * 4. Header toggle for inline English hints (EN: ON / OFF)
 */

(function () {
  // Master Comprehensive Bilingual Lexicon (Literature + Grammar)
  const MASTER_LEXICON = {
    // Literature Key Terms
    "विजय": { en: "Victory / Triumph", desc: "जीत" },
    "दम": { en: "Firm resolve / Determination", desc: "हठ या संकल्प" },
    "बदी": { en: "Evil / Wickedness", desc: "बुराई" },
    "भेदभाव": { en: "Discrimination / Distinction", desc: "अंतर या असमानता" },
    "हौसला": { en: "Courage / Confidence", desc: "साहस" },
    "धर्म": { en: "Righteousness / Good deeds", desc: "सत्कर्म" },
    "पुनरागमन": { en: "Return / Coming back", desc: "वापस आना" },
    "आर्तनाद": { en: "Cry of distress / Wailing", desc: "दुख भरी चीख" },
    "सब्जबाग": { en: "False promises / Mirage", desc: "झूठे सपने दिखाना" },
    "रक्षागार": { en: "Safe haven / Refuge", desc: "सुरक्षित स्थान" },
    "विचेष्टा": { en: "Vain effort / Struggle", desc: "व्यर्थ चेष्टा" },
    "निष्कासित": { en: "Expelled / Driven out", desc: "निकाला हुआ" },
    "विषाद": { en: "Grief / Sorrow / Despair", desc: "उदासी या दुख" },
    "निस्तब्धता": { en: "Dead silence / Stillness", desc: "गहरा सन्नाटा" },
    "उत्कंठा": { en: "Curiosity / Eagerness", desc: "तीव्र उत्सुकता" },
    "लाड़ली": { en: "Beloved daughter / Darling", desc: "दुलारी बच्ची" },
    "काकी": { en: "Aunt / Elderly aunt", desc: "चाची" },
    "उपेक्षा": { en: "Neglect / Disregard", desc: "ध्यान न देना" },
    "संवेदना": { en: "Sensitivity / Empathy", desc: "सहानुभूति" },
    "प्रायश्चित": { en: "Atonement / Repentance", desc: "पछतावा" },
    "संकल्प": { en: "Resolution / Vow", desc: "दृढ़ निश्चय" },
    "अग्नि": { en: "Fire", desc: "आग" },
    "मिसाइल": { en: "Missile / Guided Rocket", desc: "प्रक्षेपास्त्र" },
    "उद्भव": { en: "Origin / Evolution", desc: "उत्पत्ति" },
    "उपहार": { en: "Gift / Present", desc: "भेंट" },
    "विश्वराज्य": { en: "Universal State / World Brotherhood", desc: "वसुधैव कुटुंबकम" },
    "वसुधैव कुटुंबकम": { en: "The entire world is one family", desc: "समस्त पृथ्वी ही एक परिवार है" },
    "पंचतत्व": { en: "Five Cosmic Elements", desc: "पृथ्वी, जल, अग्नि, वायु, आकाश" },
    "लोकतंत्र": { en: "Democracy", desc: "जनता का शासन" },

    // Grammar: G1 - भाषा, लिपि, व्याकरण
    "भाषा": { en: "Language", desc: "विचारों एवं भावों के आदान-प्रदान का माध्यम (Medium of communication)" },
    "मौखिक भाषा": { en: "Oral / Spoken Language", desc: "बोलकर और सुनकर विचारों का विनिमय" },
    "लिखित भाषा": { en: "Written Language", desc: "ध्वनियों को लिखित चिह्नों द्वारा स्थायी रूप देना" },
    "लिपि": { en: "Script / Writing System", desc: "मौखिक ध्वनियों को लिखने हेतु निश्चित किए गए चिह्न" },
    "देवनागरी": { en: "Devanagari Script", desc: "हिंदी, संस्कृत व मराठी की अक्षरात्मक व वैज्ञानिक लिपि" },
    "रोमन": { en: "Roman Script", desc: "अंग्रेज़ी, जर्मन, फ्रेंच की लिपि (Left to Right)" },
    "फ़ारसी": { en: "Persian / Nastaliq Script", desc: "उर्दू व फ़ारसी की लिपि (Right to Left)" },
    "व्याकरण": { en: "Grammar", desc: "भाषा के शुद्ध नियमों का शास्त्र" },
    "वर्ण विचार": { en: "Phonology / Orthography", desc: "वर्णों के आकार, उच्चारण, भेद एवं संधि का अध्ययन" },
    "शब्द विचार": { en: "Morphology / Etymology", desc: "शब्दों के स्रोत, भेद, रूप व व्युत्पत्ति का अध्ययन" },
    "पद विचार": { en: "Morphosyntax (Pad Vichar)", desc: "वाक्य में प्रयुक्त पदों का व्याकरणिक परिचय" },
    "वाक्य विचार": { en: "Syntax", desc: "वाक्यों की संरचना, भेद एवं विराम चिह्नों का अध्ययन" },
    "बोली": { en: "Dialect", desc: "भाषा का सीमित व स्थानीय रूप (५-१० किमी में बदलता है)" },
    "उपभाषा": { en: "Sublanguage / Regional Variety", desc: "विस्तृत क्षेत्र की बोली जिसमें प्रचुर साहित्य रचा जाता है" },
    "राजभाषा": { en: "Official Language", desc: "सरकारी व प्रशासनिक कार्यों की निश्चित भाषा (अनुच्छेद ३४३)" },
    "राष्ट्रभाषा": { en: "National Language", desc: "समस्त राष्ट्र द्वारा स्वीकृत व मान्य भाषा" },
    "मानक भाषा": { en: "Standard Language", desc: "शिष्ट व शिक्षित समाज द्वारा स्वीकृत व्याकरण-सम्मत रूप" },
    "साहित्य": { en: "Literature", desc: "किसी भाषा में संचित व सुरक्षित ज्ञान का कोश" },
    "पश्चिमी हिंदी": { en: "Western Hindi", desc: "ब्रजभाषा, खड़ी बोली, बाँगरू, बुंदेली, कन्नौजी" },
    "पूर्वी हिंदी": { en: "Eastern Hindi", desc: "अवधी, बघेली, छत्तीसगढ़ी" },
    "बिहारी हिंदी": { en: "Bihari Hindi", desc: "भोजपुरी, मगही, मैथिली" },
    "पहाड़ी हिंदी": { en: "Pahari Hindi", desc: "गढ़वाली, कुमाऊँनी, हिमाचली" },
    "राजस्थानी हिंदी": { en: "Rajasthani Hindi", desc: "मारवाड़ी, मेवाती, जयपुरी, मालवी" },
    "भारत-यूरोपीय": { en: "Indo-European Family", desc: "हिंदी, गुजराती, मराठी, पंजाबी, बांग्ला आदि" },
    "द्रविड़ परिवार": { en: "Dravidian Family", desc: "तमिल, तेलुगु, कन्नड़, मलयालम" },

    // Grammar: G2 - वर्ण विचार
    "वर्ण": { en: "Letter / Phoneme", desc: "भाषा की लघुतम अखंड मूल ध्वनि (अविभाज्य इकाई)" },
    "वर्णमाला": { en: "Alphabet", desc: "वर्णों का निश्चित, क्रमबद्ध व व्यवस्थित समूह (४४ मानक वर्ण)" },
    "स्वर": { en: "Vowel", desc: "स्वतंत्र रूप से उच्चरित ध्वनियाँ (११ स्वर)" },
    "ह्रस्व स्वर": { en: "Short Vowel", desc: "उच्चारण में १ मात्रा (न्यूनतम समय): अ, इ, उ, ऋ" },
    "दीर्घ स्वर": { en: "Long Vowel", desc: "ह्रस्व से दुगुना समय (२ मात्राएँ): आ, ई, ऊ, ए, ऐ, ओ, औ" },
    "प्लुत स्वर": { en: "Prolonged Vowel", desc: "ह्रस्व से तिगुना समय (३ मात्राएँ): ओ३म्" },
    "व्यंजन": { en: "Consonant", desc: "स्वरों की सहायता से बोले जाने वाले वर्ण (३३ मानक व्यंजन)" },
    "स्पर्श व्यंजन": { en: "Stop / Plosive Consonants", desc: "क से म तक २५ व्यंजन जो वाग्यंत्रों के स्पर्श से उत्पन्न होते हैं" },
    "अंतःस्थ व्यंजन": { en: "Semi-vowels / Approximants", desc: "य, र, ल, व (स्वर व व्यंजन के मध्यवर्ती)" },
    "ऊष्म व्यंजन": { en: "Fricatives / Sibilants", desc: "श, ष, स, ह (वायु के घर्षण से ऊष्मा उत्पन्न करने वाले)" },
    "संयुक्त व्यंजन": { en: "Conjunct Consonants", desc: "दो भिन्न व्यंजनों का मेल: क्ष, त्र, ज्ञ, श्र" },
    "द्वित्व व्यंजन": { en: "Geminate / Doubled Consonants", desc: "एक ही व्यंजन का लगातार दो बार मेल (बच्चा, पक्का)" },
    "व्यंजन-गुच्छ": { en: "Consonant Cluster", desc: "दो या अधिक विभिन्न व्यंजनों का एक साथ मेल (क्यारी, पुस्तक)" },
    "अयोगवाह": { en: "Ayogavaha", desc: "न पूर्ण स्वर, न व्यंजन: अं (अनुस्वार) और अः (विसर्ग)" },
    "अनुस्वार": { en: "Anusvara (ं)", desc: "केवल नाक से उच्चरित ध्वनि (कंठ/तालु/दंत स्पर्श)" },
    "अनुनासिक": { en: "Anunasika / Candrabindu (ँ)", desc: "मुख और नासिका दोनों से उच्चरित ध्वनि (चाँद, आँख)" },
    "विसर्ग": { en: "Visarga (ः)", desc: "'ह' के समान उच्चरित ध्वनि (प्रातः, अतः)" },
    "नुक़्ता": { en: "Nuqta (.)", desc: "अरबी-फ़ारसी अक्षरों के नीचे लगने वाला बिंदु (क़, ख़, ग़, ज़, फ़)" },
    "आगत ध्वनियाँ": { en: "Borrowed Sounds", desc: "विदेशी भाषाओं से हिंदी में आई ध्वनियाँ ('ऑ', 'ज़', 'फ़')" },
    "वर्ण-विच्छेद": { en: "Phonetic Segmentation", desc: "शब्द के प्रत्येक स्वर व व्यंजन को पृथक-पृथक करके लिखना" },
    "रेफ़": { en: "Ref (र्)", desc: "स्वर-रहित 'र्' जो अगले वर्ण के ऊपर लगता है (कर्म, धर्म)" },
    "पदेन": { en: "Paden (्र, ्र)", desc: "स्वर-युक्त 'र' जो व्यंजन के नीचे लगता है (क्रम, ट्रक)" },
    "उच्चारण स्थान": { en: "Place of Articulation", desc: "कंठ्य, तालव्य, मूर्धन्य, दंत्य, ओष्ठ्य, नासिक्य" },

    // Grammar: G3 - शब्द विचार
    "शब्द": { en: "Word", desc: "वर्णों के सार्थक मेल से बनी स्वतंत्र भाषिक इकाई" },
    "विकारी": { en: "Declinable (Changeable)", desc: "लिंग, वचन, कारक, काल से रूप बदलने वाले शब्द (संज्ञा, सर्वनाम, विशेषण, क्रिया)" },
    "अविकारी": { en: "Indeclinable (Unchangeable / Avyaya)", desc: "किसी भी परिस्थिति में रूप न बदलने वाले (क्रियाविशेषण, समुच्चयबोधक आदि)" },
    "तत्सम": { en: "Tatsama (Sanskrit Loanword)", desc: "संस्कृत के मूल शब्द जो बिना परिवर्तन के हिंदी में प्रयुक्त होते हैं" },
    "तद्भव": { en: "Tadbhava (Derived Word)", desc: "संस्कृत के शब्द जो रूप बदलकर हिंदी भाषा में शामिल हुए हैं" },
    "देशज": { en: "Deshaj (Indigenous / Dialect Word)", desc: "क्षेत्रीय बोलियों व स्थानीय जनभाषा से अपनाए गए शब्द (लोटा, पगड़ी, खिचड़ी)" },
    "विदेशज": { en: "Videshaj (Foreign Loanword)", desc: "विदेशी भाषाओं (अरबी, फ़ारसी, अंग्रेज़ी, पुर्तगाली आदि) से आए शब्द" },
    "संकर": { en: "Hybrid / Compound Word", desc: "दो भिन्न भाषाओं के शब्दों के मेल से बने शब्द (उदा. रेलगाड़ी, वर्षगांठ)" },
    "रूढ़ शब्द": { en: "Root / Primitive Word", desc: "जिनके सार्थक टुकड़े नहीं किए जा सकते (घर, जल, पुस्तक)" },
    "यौगिक शब्द": { en: "Compound / Derivative Word", desc: "दो या अधिक सार्थक शब्दों के योग से बने शब्द (विद्यालय, राजपुत्र)" },
    "योगरूढ़ शब्द": { en: "Specialized Compound Word", desc: "जो विशेष पारंपरिक अर्थ में रूढ़ हो गए हैं (पंकज, दशानन)" }
  };

  // Inject CSS Styles for Bilingual Features
  function injectBilingualStyles() {
    if (document.getElementById("bilingual-assistant-styles")) return;
    const style = document.createElement("style");
    style.id = "bilingual-assistant-styles";
    style.textContent = `
      /* English Translation Hints Styling */
      .en-hint {
        display: none;
        font-family: 'Outfit', sans-serif;
        font-size: 0.72rem;
        font-weight: 600;
        color: #93c5fd;
        background: rgba(59, 130, 246, 0.14);
        border: 1px solid rgba(59, 130, 246, 0.28);
        padding: 1px 6px;
        border-radius: 4px;
        margin-left: 5px;
        vertical-align: middle;
        letter-spacing: 0.3px;
        user-select: none;
      }
      html.light .en-hint {
        color: #1d4ed8;
        background: rgba(37, 99, 235, 0.1);
        border-color: rgba(37, 99, 235, 0.25);
      }
      body.show-en-hints .en-hint {
        display: inline-block !important;
      }

      /* Term Gloss Dotted Underline */
      .term-gloss {
        border-bottom: 1.5px dotted #38bdf8;
        cursor: help;
        transition: all 0.2s ease;
      }
      .term-gloss:hover {
        color: #38bdf8;
        background: rgba(56, 189, 248, 0.12);
        border-radius: 3px;
      }
    `;
    document.head.appendChild(style);
  }

  // Inject DOM Elements: Tooltip, Selection Pill, Drawer Button & Drawer
  function injectBilingualDOM() {
    if (document.getElementById("gloss-tooltip")) return;

    // 1. Floating Tooltip
    const tooltip = document.createElement("div");
    tooltip.id = "gloss-tooltip";
    tooltip.className = "fixed hidden z-[9999] max-w-xs sm:max-w-sm p-4 rounded-2xl bg-slate-900/95 backdrop-blur-xl border border-blue-500/40 shadow-2xl text-xs transition-opacity duration-200 pointer-events-auto text-slate-100";
    tooltip.innerHTML = `
      <div class="flex items-center justify-between gap-2 pb-2 mb-2 border-b border-slate-800">
        <div class="flex items-center gap-2 min-w-0">
          <span class="w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
          <h5 id="gloss-tt-term" class="font-bold text-white text-sm truncate font-heading"></h5>
        </div>
        <button id="gloss-tt-audio" class="p-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs transition-colors cursor-pointer" title="उच्चारण सुनें">
          <i class="fas fa-volume-up"></i>
        </button>
      </div>
      <div class="mb-2">
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 block mb-0.5">English Meaning</span>
        <span id="gloss-tt-en" class="font-bold text-amber-300 text-xs font-mono"></span>
      </div>
      <div>
        <span class="text-[10px] uppercase font-mono tracking-wider text-slate-400 block mb-0.5">सरल व्याख्या / अर्थ</span>
        <p id="gloss-tt-desc" class="text-slate-200 text-xs leading-relaxed"></p>
      </div>
    `;
    document.body.appendChild(tooltip);

    // Audio button in tooltip
    tooltip.querySelector("#gloss-tt-audio").addEventListener("click", () => {
      const term = document.getElementById("gloss-tt-term").innerText;
      speakHindi(term);
    });

    // 2. Selection Lookup Pill
    const pill = document.createElement("div");
    pill.id = "selection-lookup-pill";
    pill.className = "fixed hidden z-[9999] p-2 rounded-2xl bg-slate-900/95 backdrop-blur-xl border border-amber-500/40 shadow-2xl text-xs flex items-center gap-2 transition-all text-slate-100";
    pill.innerHTML = `
      <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-xs flex-shrink-0">
        🔤
      </span>
      <div class="min-w-0 pr-1">
        <div id="sel-word-title" class="font-bold text-white truncate text-[11px]"></div>
        <div id="sel-word-meaning" class="text-amber-300 text-[11px] truncate font-mono"></div>
      </div>
      <div class="flex items-center gap-1 border-l border-slate-800 pl-1.5 flex-shrink-0">
        <button id="sel-btn-audio" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white transition-all text-xs cursor-pointer" title="सुनें">
          <i class="fas fa-volume-up"></i>
        </button>
        <a id="sel-btn-trans" target="_blank" rel="noopener noreferrer" class="p-1.5 rounded-lg bg-blue-600/80 hover:bg-blue-600 text-white transition-all text-xs flex items-center gap-1 cursor-pointer" title="Google Translate">
          <i class="fab fa-google text-[10px]"></i>
        </a>
      </div>
    `;
    document.body.appendChild(pill);

    // 3. Floating Drawer Button
    const drawerBtn = document.createElement("button");
    drawerBtn.id = "btn-vocab-drawer";
    drawerBtn.className = "fixed bottom-6 right-6 z-40 px-3.5 py-2.5 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold text-xs shadow-2xl backdrop-blur-md flex items-center gap-2 border border-blue-400/40 transition-all hover:scale-105 cursor-pointer";
    drawerBtn.innerHTML = `<i class="fas fa-language text-base text-amber-300"></i> <span>🔤 EN &harr; HI शब्दकोश</span>`;
    drawerBtn.onclick = toggleVocabDrawer;
    document.body.appendChild(drawerBtn);

    // 4. Slide-Out Drawer & Backdrop
    const backdrop = document.createElement("div");
    backdrop.id = "bilingual-drawer-backdrop";
    backdrop.className = "fixed inset-0 bg-black/60 backdrop-blur-sm z-[9990] hidden transition-opacity";
    backdrop.onclick = toggleVocabDrawer;
    document.body.appendChild(backdrop);

    const drawer = document.createElement("aside");
    drawer.id = "bilingual-drawer";
    drawer.className = "fixed top-0 right-0 h-full w-full sm:w-96 bg-slate-900/95 backdrop-blur-2xl border-l border-slate-800 z-[9995] shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col text-slate-100";
    drawer.innerHTML = `
      <div class="p-5 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-sm font-bold">
            🔤
          </div>
          <div>
            <h4 class="text-sm font-bold text-white font-heading">त्वरित द्विभाषी शब्दकोश</h4>
            <span class="text-[11px] text-slate-400 font-mono">English &harr; Hindi Quick Lexicon</span>
          </div>
        </div>
        <button onclick="window.toggleVocabDrawer()" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-all cursor-pointer">
          <i class="fas fa-times"></i>
        </button>
      </div>

      <div class="p-4 border-b border-slate-800/80 bg-slate-950/40">
        <div class="relative">
          <input type="text" id="drawer-search-input" placeholder="अंग्रेज़ी या हिंदी में खोजें (e.g. victory, भाषा)..." class="w-full pl-9 pr-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 font-sans">
          <i class="fas fa-search absolute left-3 top-2.5 text-xs text-slate-500"></i>
        </div>
      </div>

      <div id="drawer-items-list" class="flex-1 overflow-y-auto p-4 space-y-2.5"></div>

      <div class="p-4 border-t border-slate-800 bg-slate-950/60 text-center text-[11px] text-slate-500 font-sans">
        पुष्टि की अध्ययन सुविधा हेतु &bull; Pushti Study Hub
      </div>
    `;
    document.body.appendChild(drawer);

    drawer.querySelector("#drawer-search-input").addEventListener("keyup", (e) => {
      filterDrawerWords(e.target.value);
    });

    renderDrawerItems();
  }

  // Speak helper
  function speakHindi(text) {
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "hi-IN";
    const voices = window.speechSynthesis.getVoices();
    const hiVoice = voices.find(v => v.lang.startsWith("hi"));
    if (hiVoice) u.voice = hiVoice;
    window.speechSynthesis.speak(u);
  }

  // Tooltip Logic
  function setupGlossaryTooltips() {
    const tt = document.getElementById("gloss-tooltip");
    if (!tt) return;
    let hideTimeout = null;

    document.querySelectorAll(".term-gloss").forEach((el) => {
      el.addEventListener("mouseenter", () => {
        clearTimeout(hideTimeout);
        showTooltip(el);
      });
      el.addEventListener("mouseleave", () => {
        hideTimeout = setTimeout(() => tt.classList.add("hidden"), 300);
      });
      el.addEventListener("click", (e) => {
        e.stopPropagation();
        showTooltip(el);
      });
    });

    tt.addEventListener("mouseenter", () => clearTimeout(hideTimeout));
    tt.addEventListener("mouseleave", () => tt.classList.add("hidden"));

    document.addEventListener("click", (e) => {
      if (!tt.contains(e.target) && !e.target.classList.contains("term-gloss")) {
        tt.classList.add("hidden");
      }
    });
  }

  function showTooltip(el) {
    const tt = document.getElementById("gloss-tooltip");
    const term = el.getAttribute("data-term") || el.innerText.trim();
    const en = el.getAttribute("data-en") || (MASTER_LEXICON[term] ? MASTER_LEXICON[term].en : "");
    const desc = el.getAttribute("data-desc") || (MASTER_LEXICON[term] ? MASTER_LEXICON[term].desc : "");

    document.getElementById("gloss-tt-term").innerText = term;
    document.getElementById("gloss-tt-en").innerText = en ? en : "Vocabulary Word";
    document.getElementById("gloss-tt-desc").innerText = desc ? desc : "पाठ्यपुस्तक प्रामाणिक पद।";

    tt.classList.remove("hidden");

    const rect = el.getBoundingClientRect();
    const ttWidth = 280;
    let left = rect.left + window.scrollX;
    let top = rect.bottom + window.scrollY + 8;

    if (left + ttWidth > window.innerWidth) left = window.innerWidth - ttWidth - 20;
    if (left < 10) left = 10;

    tt.style.left = `${left}px`;
    tt.style.top = `${top}px`;
  }

  // Selection Lookup Engine
  function setupSelectionLookup() {
    const pill = document.getElementById("selection-lookup-pill");
    if (!pill) return;

    document.addEventListener("selectionchange", () => {
      const sel = window.getSelection();
      const selectedText = sel.toString().trim();

      if (!selectedText || selectedText.length < 2 || selectedText.length > 30) {
        pill.classList.add("hidden");
        return;
      }

      if (sel.anchorNode && sel.anchorNode.parentElement &&
        ["INPUT", "TEXTAREA", "BUTTON"].includes(sel.anchorNode.parentElement.tagName)) {
        pill.classList.add("hidden");
        return;
      }

      let matchEn = "";
      if (MASTER_LEXICON[selectedText]) {
        matchEn = MASTER_LEXICON[selectedText].en;
      } else {
        const found = Object.keys(MASTER_LEXICON).find(k => k === selectedText || selectedText.includes(k));
        if (found) matchEn = MASTER_LEXICON[found].en;
      }

      document.getElementById("sel-word-title").innerText = selectedText;
      document.getElementById("sel-word-meaning").innerText = matchEn ? `🇬🇧 ${matchEn}` : "🌐 Google Translate";

      document.getElementById("sel-btn-audio").onclick = (e) => {
        e.stopPropagation();
        speakHindi(selectedText);
      };
      document.getElementById("sel-btn-trans").href = `https://translate.google.com/?sl=hi&tl=en&text=${encodeURIComponent(selectedText)}&op=translate`;

      try {
        const range = sel.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        let top = rect.top + window.scrollY - 48;
        let left = rect.left + window.scrollX;

        if (top < 10) top = rect.bottom + window.scrollY + 8;
        if (left + 220 > window.innerWidth) left = window.innerWidth - 230;
        if (left < 10) left = 10;

        pill.style.top = `${top}px`;
        pill.style.left = `${left}px`;
        pill.classList.remove("hidden");
      } catch (err) {
        pill.classList.add("hidden");
      }
    });

    document.addEventListener("mousedown", (e) => {
      if (!pill.contains(e.target)) {
        pill.classList.add("hidden");
      }
    });
  }

  // Drawer functions
  window.toggleVocabDrawer = function () {
    const drawer = document.getElementById("bilingual-drawer");
    const backdrop = document.getElementById("bilingual-drawer-backdrop");
    if (!drawer) return;
    const isClosed = drawer.classList.contains("translate-x-full");

    if (isClosed) {
      drawer.classList.remove("translate-x-full");
      backdrop.classList.remove("hidden");
      document.getElementById("drawer-search-input").focus();
    } else {
      drawer.classList.add("translate-x-full");
      backdrop.classList.add("hidden");
    }
  };

  function renderDrawerItems() {
    const list = document.getElementById("drawer-items-list");
    if (!list) return;

    let itemsHtml = "";
    for (const [term, data] of Object.entries(MASTER_LEXICON)) {
      itemsHtml += `
        <div class="drawer-item p-3 rounded-2xl bg-slate-800/80 border border-slate-700/80 hover:border-blue-500/50 transition-all flex items-start justify-between gap-3 group" data-term="${term.toLowerCase()}" data-en="${data.en.toLowerCase()}">
          <div class="min-w-0">
            <div class="flex items-center gap-2 mb-1 flex-wrap">
              <span class="font-bold text-white text-sm font-heading">${term}</span>
              <span class="text-xs font-mono font-semibold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">${data.en}</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">${data.desc}</p>
          </div>
          <button onclick="window.speakHindiWordFromDrawer('${term}')" class="p-2 rounded-xl bg-slate-900 group-hover:bg-blue-600 text-slate-400 group-hover:text-white transition-all text-xs flex-shrink-0 cursor-pointer" title="सुनें">
            <i class="fas fa-volume-up"></i>
          </button>
        </div>`;
    }
    list.innerHTML = itemsHtml;
  }

  window.speakHindiWordFromDrawer = function(term) {
    speakHindi(term);
  };

  function filterDrawerWords(query) {
    const q = query.toLowerCase().trim();
    document.querySelectorAll("#drawer-items-list .drawer-item").forEach((item) => {
      const term = item.getAttribute("data-term") || "";
      const en = item.getAttribute("data-en") || "";
      const desc = item.innerText.toLowerCase();
      if (term.includes(q) || en.includes(q) || desc.includes(q)) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
  }

  // Header Toggle Logic
  window.toggleEnglishHints = function () {
    const body = document.body;
    const label = document.getElementById("en-toggle-label");
    const btn = document.getElementById("btn-en-toggle");
    body.classList.toggle("show-en-hints");

    const isShowing = body.classList.contains("show-en-hints");
    if (isShowing) {
      if (label) label.innerText = "EN: ON";
      if (btn) {
        btn.classList.add("bg-blue-600/30", "text-white", "border-blue-400");
        btn.classList.remove("text-amber-400");
      }
      localStorage.setItem("hub_en_hints", "true");
    } else {
      if (label) label.innerText = "EN: OFF";
      if (btn) {
        btn.classList.remove("bg-blue-600/30", "text-white", "border-blue-400");
        btn.classList.add("text-amber-400");
      }
      localStorage.setItem("hub_en_hints", "false");
    }
  };

  // Auto-annotate text across paragraphs if not already marked
  function autoAnnotateKeyWords() {
    const targets = document.querySelectorAll("p, .theory-body, .qa-content");
    const sortedTerms = Object.keys(MASTER_LEXICON).filter(k => k.length >= 3).sort((a, b) => b.length - a.length);

    targets.forEach(container => {
      if (container.querySelector(".term-gloss")) return; // already annotated
      let content = container.innerHTML;
      let count = 0;

      for (const term of sortedTerms) {
        if (count >= 3) break;
        if (content.includes(term) && !content.includes(`data-term="${term}"`)) {
          const en = MASTER_LEXICON[term].en;
          const desc = MASTER_LEXICON[term].desc;
          const rep = `<span class="term-gloss font-semibold cursor-help" data-term="${term}" data-en="${en}" data-desc="${desc}">${term}</span><span class="en-hint font-sans">(${en})</span>`;
          // Replace only first occurrence
          content = content.replace(term, rep);
          count++;
        }
      }
      container.innerHTML = content;
    });
  }

  // Init everything on DOM ready
  document.addEventListener("DOMContentLoaded", () => {
    injectBilingualStyles();
    injectBilingualDOM();
    autoAnnotateKeyWords();
    setupGlossaryTooltips();
    setupSelectionLookup();

    // Check saved state
    if (localStorage.getItem("hub_en_hints") === "true") {
      document.body.classList.add("show-en-hints");
      const label = document.getElementById("en-toggle-label");
      const btn = document.getElementById("btn-en-toggle");
      if (label) label.innerText = "EN: ON";
      if (btn) {
        btn.classList.add("bg-blue-600/30", "text-white", "border-blue-400");
        btn.classList.remove("text-amber-400");
      }
    }
  });
})();
