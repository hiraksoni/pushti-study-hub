
    // 1. Session Timer
    let sessionSeconds = 0;
    setInterval(() => {
      sessionSeconds++;
      const mins = String(Math.floor(sessionSeconds / 60)).padStart(2, '0');
      const secs = String(sessionSeconds % 60).padStart(2, '0');
      const el = document.getElementById('sessionTimerDisplay');
      if (el) el.textContent = `${mins}:${secs}`;
    }, 1000);

    // 2. Theme Switcher
    function toggleTheme() {
      const htmlEl = document.documentElement;
      const isDark = htmlEl.classList.toggle('dark');
      htmlEl.setAttribute('data-theme', isDark ? 'dark' : 'light');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      updateThemeIcon(isDark);
    }

    function updateThemeIcon(isDark) {
      const icon = document.getElementById('themeToggleIcon');
      if (icon) {
        icon.className = isDark ? 'fas fa-moon text-sm' : 'fas fa-sun text-sm text-amber-400';
      }
    }

    if (localStorage.getItem('theme') === 'light') {
      document.documentElement.classList.remove('dark');
      document.documentElement.setAttribute('data-theme', 'light');
      updateThemeIcon(false);
    }

    // 3. Sidebar Pinning Controller
    function updatePinButtonUI(isPinned) {
      const btn = document.getElementById('pinToggleBtn');
      const icon = document.getElementById('pinToggleIcon') || document.getElementById('pinIcon');
      const dot = document.getElementById('pinStatusDot');
      const label = document.getElementById('pinStatusText');
      const hint = document.getElementById('pinActionHint');
      
      if (btn) {
        btn.setAttribute('aria-pressed', isPinned ? 'true' : 'false');
        if (isPinned) {
          btn.className = 'w-full h-10 px-2 rounded-xl border transition-all flex items-center justify-center gap-2 cursor-pointer relative overflow-hidden bg-cyan-500/20 border-cyan-500/50 text-cyan-300 ring-1 ring-cyan-500/30 shadow-[0_0_12px_rgba(6,182,212,0.25)]';
          btn.title = 'Sidebar: Pinned (Locked Open - tap to collapse to compact dock)';
        } else {
          btn.className = 'w-full h-10 px-2 rounded-xl border transition-all flex items-center justify-center gap-2 cursor-pointer relative overflow-hidden bg-slate-800/80 border-slate-700/60 text-slate-400 hover:text-slate-200 hover:bg-slate-700/80';
          btn.title = 'Sidebar: Unpinned (Compact Dock - tap to lock open)';
        }
      }
      
      if (icon) {
        if (isPinned) {
          icon.className = 'fas fa-thumbtack text-xs transition-transform duration-300 rotate-0 text-cyan-400 font-bold scale-110';
        } else {
          icon.className = 'fas fa-thumbtack text-xs transition-transform duration-300 -rotate-45 text-slate-400';
        }
      }
      
      if (dot) {
        if (isPinned) {
          dot.className = 'w-2 h-2 rounded-full bg-cyan-400 shadow-[0_0_8px_rgba(6,182,212,0.9)] animate-pulse absolute top-1.5 right-1.5 transition-colors';
        } else {
          dot.className = 'w-1.5 h-1.5 rounded-full bg-slate-600 absolute top-1.5 right-1.5 transition-colors';
        }
      }
      
      if (label) {
        label.textContent = isPinned ? 'Pinned (Locked)' : 'Compact Dock';
        label.className = isPinned ? 'text-xs font-bold tracking-wide uppercase text-cyan-300' : 'text-xs font-semibold tracking-wide uppercase text-slate-400';
      }
      
      if (hint) {
        hint.textContent = isPinned ? 'Tap to collapse' : 'Tap to lock';
        hint.className = isPinned ? 'text-[10px] font-mono text-cyan-400/80' : 'text-[10px] font-mono text-slate-500';
      }
    }

    function toggleSidebarPin() {
      const dock = document.getElementById('sidebarDock');
      if (!dock) return;
      const isPinned = dock.classList.toggle('pinned');
      document.body.classList.toggle('dock-pinned', isPinned);
      localStorage.setItem('bio4_dock_pinned', isPinned ? 'true' : 'false');
      updatePinButtonUI(isPinned);
    }
    window.toggleDockPin = toggleSidebarPin;
    window.toggleSidebarPin = toggleSidebarPin;

    if (localStorage.getItem('bio4_dock_pinned') === 'true') {
      toggleSidebarPin();
    }

    // 4. Tab Switching Controller
    function switchTab(tabId, btn) {
      if (!tabId) return;
      document.querySelectorAll('.tab-pane, .tab-content').forEach(p => {
        p.classList.remove('active');
        p.classList.add('hidden');
        p.style.display = 'none';
      });
      
      let target = document.getElementById(tabId);
      if (!target) {
        target = Array.from(document.querySelectorAll('.tab-pane, .tab-content')).find(
          el => el.id && el.id.toLowerCase() === (tabId || '').toLowerCase()
        );
      }
      
      if (target) {
        target.classList.remove('hidden');
        target.classList.add('active');
        target.style.display = 'block';
      }

      document.querySelectorAll('.nav-tab-btn').forEach(b => {
        b.classList.remove('active');
        const dot = b.querySelector('.animate-pulse');
        if (dot) dot.remove();
      });

      const activeBtn = btn || document.getElementById('navBtn-' + tabId) || (target ? document.getElementById('navBtn-' + target.id) : null);
      if (activeBtn) {
        activeBtn.classList.add('active');
        const iconWrap = activeBtn.querySelector('div:nth-child(2)');
        if (iconWrap && !iconWrap.querySelector('.animate-pulse')) {
          const pulseDot = document.createElement('span');
          pulseDot.className = 'w-2 h-2 rounded-full bg-emerald-400 absolute top-0.5 right-0.5 ring-2 ring-slate-900 animate-pulse';
          iconWrap.appendChild(pulseDot);
        }
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
      try {
        history.replaceState(null, null, '#' + (target ? target.id : tabId));
      } catch (e) {
        window.location.hash = target ? target.id : tabId;
      }
    }
    window.switchTab = switchTab;
    window.switchMainTab = switchTab;

    // Initial Hash Loader
    window.addEventListener('DOMContentLoaded', () => {
      let hash = window.location.hash ? window.location.hash.substring(1) : '';
      if (hash && document.getElementById(hash)) {
        switchTab(hash);
      }
    });
    window.addEventListener('hashchange', () => {
      let hash = window.location.hash ? window.location.hash.substring(1) : '';
      if (hash && document.getElementById(hash)) {
        switchTab(hash);
      }
    });

    // 5. Flashcards Controller
    function flipFlashcard(target) {
      let card = null;
      if (typeof target === 'string') {
        card = document.getElementById(target);
      } else if (target && target.nodeType) {
        card = target.classList.contains('flashcard-3d') ? target : target.closest('.flashcard-3d');
      }
      if (card) {
        card.classList.toggle('flipped');
      }
    }
    window.flipFlashcard = flipFlashcard;

    function toggleFlipAll() {
      document.querySelectorAll('.flashcard-3d').forEach(c => c.classList.toggle('flipped'));
    }
    window.toggleFlipAll = toggleFlipAll;

    // 6. Solved Questions Answer Toggler
    function toggleAnswer(arg) {
      let box = null;
      let btn = null;
      if (typeof arg === 'string') {
        box = document.getElementById(arg);
        if (box) {
          const prev = box.previousElementSibling;
          if (prev) btn = prev.querySelector('button') || prev;
        }
      } else if (arg && arg.nodeType) {
        btn = arg;
        const parent = arg.parentElement;
        if (parent) {
          box = parent.querySelector('.answer-box');
        }
        if (!box) box = arg.nextElementSibling;
      }
      
      if (box) {
        box.classList.toggle('hidden');
        if (btn) {
          const isHidden = box.classList.contains('hidden');
          const span = btn.querySelector('span');
          const icon = btn.querySelector('i');
          if (span) span.textContent = isHidden ? 'Show Verified Solution' : 'Hide Solution';
          if (icon) {
            icon.className = isHidden 
              ? 'fas fa-chevron-down text-xs transition-transform duration-200' 
              : 'fas fa-chevron-up text-xs transition-transform duration-200';
          }
        }
      }
    }
    window.toggleAnswer = toggleAnswer;

    let allSubjExpanded = false;
    function toggleAllSubjAnswers() {
      allSubjExpanded = !allSubjExpanded;
      const btn = document.getElementById('toggleAllSubjBtn');
      if (btn) btn.textContent = allSubjExpanded ? 'Collapse All Solutions' : 'Expand All Solutions';
      document.querySelectorAll('.answer-box').forEach(box => {
        if (allSubjExpanded) {
          box.classList.remove('hidden');
        } else {
          box.classList.add('hidden');
        }
        const b = box.parentElement ? box.parentElement.querySelector('button') : null;
        if (b) {
          const span = b.querySelector('span');
          const icon = b.querySelector('i');
          if (span) span.textContent = allSubjExpanded ? 'Hide Solution' : 'Show Verified Solution';
          if (icon) {
            icon.className = allSubjExpanded
              ? 'fas fa-chevron-up text-xs transition-transform duration-200'
              : 'fas fa-chevron-down text-xs transition-transform duration-200';
          }
        }
      });
    }
    window.toggleAllSubjAnswers = toggleAllSubjAnswers;

    // 7. Subjective Filters & Search
    function filterSubjectiveCards() {
      const q = (document.getElementById('subjSearchInput')?.value || '').toLowerCase().trim();
      let visible = 0;
      document.querySelectorAll('.subj-card').forEach(card => {
        const text = card.textContent.toLowerCase();
        const matchesSearch = !q || text.includes(q);
        const matchesCat = card.dataset.activeCat !== 'false';
        if (matchesSearch && matchesCat) {
          card.classList.remove('hidden');
          visible++;
        } else {
          card.classList.add('hidden');
        }
      });
      const counter = document.getElementById('subjCounter');
      if (counter) counter.textContent = `Showing ${visible} solved questions`;
    }
    window.filterSubjectiveCards = filterSubjectiveCards;

    function filterSubjCat(cat) {
      document.querySelectorAll('#subjFilterPills button').forEach(b => {
        b.className = 'px-3.5 py-2 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all';
      });
      const act = document.getElementById('scat-' + cat);
      if (act) {
        act.className = 'px-3.5 py-2 rounded-xl text-xs font-semibold bg-emerald-600 text-white cursor-pointer transition-all shadow-md shadow-emerald-600/20';
      }

      document.querySelectorAll('.subj-card').forEach(card => {
        if (cat === 'all' || card.dataset.cat === cat) {
          card.dataset.activeCat = 'true';
        } else {
          card.dataset.activeCat = 'false';
        }
      });
      filterSubjectiveCards();
    }
    window.filterSubjCat = filterSubjCat;

    // 8. Interactive Drills Scoring Engine
    let userDrillScore = 0;
    let userDrillAnswered = 0;
    const answeredDrills = new Set();

    function handleDrillClick(btn, isCorrect, explanation) {
      const card = btn.closest('.drill-card');
      if (!card) return;
      const qid = card.querySelector('.font-mono')?.textContent || Math.random();

      // Disable other buttons in this card
      card.querySelectorAll('button').forEach(b => {
        b.disabled = true;
        b.classList.add('cursor-not-allowed', 'opacity-75');
      });

      if (isCorrect) {
        btn.classList.remove('bg-slate-950/80', 'border-slate-800');
        btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200', 'ring-1', 'ring-emerald-500/40');
      } else {
        btn.classList.remove('bg-slate-950/80', 'border-slate-800');
        btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200', 'ring-1', 'ring-rose-500/40');
      }

      if (!answeredDrills.has(qid)) {
        answeredDrills.add(qid);
        userDrillAnswered++;
        if (isCorrect) userDrillScore++;

        const scoreEl = document.getElementById('drillScore');
        const ansEl = document.getElementById('drillAnswered');
        if (scoreEl) scoreEl.textContent = userDrillScore;
        if (ansEl) ansEl.textContent = userDrillAnswered;

        const scoreElSticky = document.getElementById('drillScoreSticky');
        const ansElSticky = document.getElementById('drillAnsweredSticky');
        if (scoreElSticky) scoreElSticky.textContent = userDrillScore;
        if (ansElSticky) ansElSticky.textContent = userDrillAnswered;
      }

      const fb = card.querySelector('.drill-feedback');
      if (fb) {
        fb.classList.remove('hidden');
        if (isCorrect) {
          fb.className = 'drill-feedback p-4 rounded-2xl text-xs leading-relaxed space-y-1 bg-emerald-950/70 border border-emerald-500/40 text-emerald-200';
          fb.innerHTML = `<strong><i class="fas fa-check-circle text-emerald-400 mr-1"></i>Correct!</strong><br>${explanation}`;
        } else {
          fb.className = 'drill-feedback p-4 rounded-2xl text-xs leading-relaxed space-y-1 bg-rose-950/70 border border-rose-500/40 text-rose-200';
          fb.innerHTML = `<strong><i class="fas fa-times-circle text-rose-400 mr-1"></i>Incorrect.</strong><br>${explanation}`;
        }
      }
    }
    window.handleDrillClick = handleDrillClick;

    function filterDrills(type) {
      document.querySelectorAll('#df-all, #df-mcq, #df-tf, #df-fib, #df-assertion_reason, #df-match').forEach(b => {
        b.className = 'px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 cursor-pointer transition-all';
      });
      const act = document.getElementById('df-' + type);
      if (act) {
        act.className = 'px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 text-white cursor-pointer transition-all shadow-md';
      }

      document.querySelectorAll('.drill-card').forEach(c => {
        if (type === 'all' || c.dataset.type === type) {
          c.classList.remove('hidden');
        } else {
          c.classList.add('hidden');
        }
      });
    }
    window.filterDrills = filterDrills;

    // 9. Match Columns Interactive Arena Engine (Option 3)
    const matchState = {};

    function initMatchDrill(idx) {
      if (!matchState[idx]) {
        matchState[idx] = {
          pairs: {},
          selectedLeft: null,
          checked: false
        };
      }
      return matchState[idx];
    }

    function handleMatchItemClick(idx, side, key) {
      const state = initMatchDrill(idx);
      const arena = document.getElementById(`match-arena-${idx}`);
      if (!arena) return;

      if (state.checked) {
        clearMatchValidation(idx);
      }

      if (side === 'left') {
        if (state.selectedLeft === key) {
          state.selectedLeft = null;
        } else {
          state.selectedLeft = key;
        }
      } else if (side === 'right') {
        if (state.selectedLeft) {
          const leftKey = state.selectedLeft;
          const rightKey = key;

          for (const lk in state.pairs) {
            if (state.pairs[lk] === rightKey) {
              delete state.pairs[lk];
            }
          }
          state.pairs[leftKey] = rightKey;
          state.selectedLeft = null;
        } else {
          for (const lk in state.pairs) {
            if (state.pairs[lk] === key) {
              delete state.pairs[lk];
              break;
            }
          }
        }
      }

      updateMatchUI(idx);
    }
    window.handleMatchItemClick = handleMatchItemClick;

    function handleMatchDragStart(e, idx, key) {
      const state = initMatchDrill(idx);
      state.selectedLeft = key;
      e.dataTransfer.setData('text/plain', JSON.stringify({ idx, key }));
      e.dataTransfer.effectAllowed = 'copyMove';
      updateMatchUI(idx);
    }
    window.handleMatchDragStart = handleMatchDragStart;

    function handleMatchDragOver(e) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      const el = e.currentTarget;
      if (el) el.classList.add('is-dragover');
    }
    window.handleMatchDragOver = handleMatchDragOver;

    function handleMatchDragLeave(e) {
      const el = e.currentTarget;
      if (el) el.classList.remove('is-dragover');
    }
    window.handleMatchDragLeave = handleMatchDragLeave;

    function handleMatchDrop(e, idx, rightKey) {
      e.preventDefault();
      const el = e.currentTarget;
      if (el) el.classList.remove('is-dragover');

      try {
        const data = JSON.parse(e.dataTransfer.getData('text/plain'));
        if (data && data.idx === idx && data.key) {
          const state = initMatchDrill(idx);
          const leftKey = data.key;

          for (const lk in state.pairs) {
            if (state.pairs[lk] === rightKey) {
              delete state.pairs[lk];
            }
          }
          state.pairs[leftKey] = rightKey;
          state.selectedLeft = null;
          updateMatchUI(idx);
        }
      } catch (err) {
        console.error(err);
      }
    }
    window.handleMatchDrop = handleMatchDrop;

    function updateMatchUI(idx) {
      const state = initMatchDrill(idx);
      const arena = document.getElementById(`match-arena-${idx}`);
      if (!arena) return;

      const totalItems = parseInt(arena.dataset.total || '5', 10);
      const pairedCount = Object.keys(state.pairs).length;

      const statusBadge = document.getElementById(`match-status-${idx}`);
      if (statusBadge) {
        statusBadge.textContent = `${pairedCount}/${totalItems} Paired`;
        if (pairedCount === totalItems) {
          statusBadge.className = 'font-mono font-bold text-emerald-400 bg-emerald-950/60 border border-emerald-700/60 px-2.5 py-0.5 rounded-full text-[11px] animate-pulse';
        } else {
          statusBadge.className = 'font-mono font-bold text-amber-400 bg-amber-950/60 border border-amber-800/50 px-2.5 py-0.5 rounded-full text-[11px]';
        }
      }

      arena.querySelectorAll('.match-bubble-left').forEach(el => {
        const k = el.dataset.key;
        const badge = el.querySelector('.match-conn-badge');
        const targetLbl = badge ? badge.querySelector('.target-label') : null;

        el.classList.remove('is-selected', 'is-paired');
        if (state.selectedLeft === k) {
          el.classList.add('is-selected');
        }

        if (state.pairs[k]) {
          el.classList.add('is-paired');
          if (badge) {
            badge.classList.remove('hidden');
            if (targetLbl) targetLbl.textContent = `➔ (${state.pairs[k]})`;
          }
        } else {
          if (badge) badge.classList.add('hidden');
        }
      });

      const rightToLeft = {};
      for (const lk in state.pairs) {
        rightToLeft[state.pairs[lk]] = lk;
      }

      arena.querySelectorAll('.match-socket-right').forEach(el => {
        const rk = el.dataset.key;
        const badge = el.querySelector('.match-socket-badge');
        const srcLbl = badge ? badge.querySelector('.source-label') : null;

        el.classList.remove('is-paired');
        if (rightToLeft[rk]) {
          el.classList.add('is-paired');
          if (badge) {
            badge.classList.remove('hidden');
            if (srcLbl) srcLbl.textContent = `⮌ [${rightToLeft[rk]}]`;
          }
        } else {
          if (badge) badge.classList.add('hidden');
        }
      });
    }

    function clearMatchValidation(idx) {
      const arena = document.getElementById(`match-arena-${idx}`);
      if (!arena) return;

      arena.querySelectorAll('.match-bubble-left, .match-socket-right').forEach(el => {
        el.classList.remove('match-item-correct', 'match-item-wrong');
      });

      const feedback = document.getElementById(`match-feedback-${idx}`);
      if (feedback) {
        feedback.className = 'match-feedback text-xs font-mono font-semibold text-slate-400';
        feedback.innerHTML = 'Pair each item from Column A with Column B';
      }
    }

    function checkMatchDrill(idx) {
      const state = initMatchDrill(idx);
      const arena = document.getElementById(`match-arena-${idx}`);
      if (!arena) return;

      const pairsExpected = JSON.parse(arena.dataset.pairs || '{}');
      const totalItems = parseInt(arena.dataset.total || '5', 10);
      const pairedCount = Object.keys(state.pairs).length;

      const feedback = document.getElementById(`match-feedback-${idx}`);
      if (!feedback) return;

      if (pairedCount === 0) {
        feedback.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-950/80 border border-amber-600/70 text-amber-200 flex items-center gap-1.5';
        feedback.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Please match at least one pair before checking.';
        return;
      }

      state.checked = true;
      let correctCount = 0;

      for (const lk in pairsExpected) {
        const userRk = state.pairs[lk];
        const leftEl = arena.querySelector(`.match-bubble-left[data-key="${lk}"]`);
        const rightEl = userRk ? arena.querySelector(`.match-socket-right[data-key="${userRk}"]`) : null;

        if (userRk === pairsExpected[lk]) {
          correctCount++;
          if (leftEl) leftEl.classList.add('match-item-correct');
          if (rightEl) rightEl.classList.add('match-item-correct');
        } else if (userRk) {
          if (leftEl) leftEl.classList.add('match-item-wrong');
          if (rightEl) rightEl.classList.add('match-item-wrong');
        }
      }

      if (correctCount === totalItems) {
        feedback.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-950/90 border border-emerald-500/70 text-emerald-200 flex items-center gap-1.5';
        feedback.innerHTML = `<i class="fas fa-check-circle"></i> Perfect Score! All ${totalItems}/${totalItems} Pairs Correctly Matched! (+1 Score)`;

        if (!answeredDrills.has('match_' + idx)) {
          answeredDrills.add('match_' + idx);
          userDrillAnswered++;
          userDrillScore++;

          const scoreEl = document.getElementById('drillScore');
          const ansEl = document.getElementById('drillAnswered');
          if (scoreEl) scoreEl.textContent = userDrillScore;
          if (ansEl) ansEl.textContent = userDrillAnswered;

          const scoreElSticky = document.getElementById('drillScoreSticky');
          const ansElSticky = document.getElementById('drillAnsweredSticky');
          if (scoreElSticky) scoreElSticky.textContent = userDrillScore;
          if (ansElSticky) ansElSticky.textContent = userDrillAnswered;
        }
      } else {
        feedback.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-950/90 border border-rose-500/70 text-rose-200 flex items-center gap-1.5';
        feedback.innerHTML = `<i class="fas fa-times-circle"></i> ${correctCount}/${totalItems} Correct. Adjust the mismatched pairs or tap Reset to try again!`;
      }
    }
    window.checkMatchDrill = checkMatchDrill;

    function resetMatchDrill(idx) {
      const state = initMatchDrill(idx);
      state.pairs = {};
      state.selectedLeft = null;
      state.checked = false;
      clearMatchValidation(idx);
      updateMatchUI(idx);
    }
    window.resetMatchDrill = resetMatchDrill;
