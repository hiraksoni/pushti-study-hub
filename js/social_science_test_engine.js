/**
 * Pushti Study Hub - Social Science Random Test Generator Engine
 * 50 Questions · 50 Marks · 1 Hour (60:00) Countdown
 * Subjects: History, Geography, Civics (Individual or Joint)
 * Types: MCQ, FIB, TF, MTF (1 Mark each)
 * Answers locked until submission or 1-hour timer expiry.
 * Automatic persistent archive to localStorage.
 */

(function() {
  'use strict';

  // --- STATE ---
  let activeExam = null;
  let examTimerInterval = null;

  // --- LOCAL STORAGE KEY ---
  const ARCHIVE_KEY = 'pushti_social_solved_tests';

  function getArchive() {
    try {
      const data = localStorage.getItem(ARCHIVE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error("Error reading test archive:", e);
      return [];
    }
  }

  function saveToArchive(testResult) {
    try {
      const archive = getArchive();
      archive.unshift(testResult); // most recent first
      localStorage.setItem(ARCHIVE_KEY, JSON.stringify(archive));
      renderArchiveList();
    } catch (e) {
      console.error("Error saving test result:", e);
    }
  }

  function deleteFromArchive(testId) {
    if (!confirm("Are you sure you want to delete this solved test from your archive?")) return;
    try {
      let archive = getArchive();
      archive = archive.filter(t => t.testId !== testId);
      localStorage.setItem(ARCHIVE_KEY, JSON.stringify(archive));
      renderArchiveList();
    } catch (e) {
      console.error("Error deleting test:", e);
    }
  }

  function clearAllArchive() {
    if (!confirm("Are you sure you want to clear all solved tests from your archive?")) return;
    localStorage.removeItem(ARCHIVE_KEY);
    renderArchiveList();
  }

  // --- FORMAT TIME ---
  function formatSeconds(secs) {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function formatTimeTaken(secs) {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    if (m === 0) return `${s}s`;
    return `${m}m ${s}s`;
  }

  // --- SHUFFLE HELPER (Fisher-Yates) ---
  function shuffleArray(arr) {
    const copy = [...arr];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  // --- GENERATE 50-MARK TEST ---
  function generateTest(selectedSubjects) {
    const bank = window.SOCIAL_SCIENCE_QUESTION_BANK;
    if (!bank) {
      alert("Question bank is still loading. Please try again in a few moments.");
      return null;
    }

    if (!selectedSubjects || selectedSubjects.length === 0) {
      alert("Please select at least one section: History, Geography, or Civics.");
      return null;
    }

    // Determine quotas per subject
    const numSubj = selectedSubjects.length;
    let quotas = {};
    if (numSubj === 1) {
      quotas[selectedSubjects[0]] = 50;
    } else if (numSubj === 2) {
      quotas[selectedSubjects[0]] = 25;
      quotas[selectedSubjects[1]] = 25;
    } else if (numSubj === 3) {
      quotas['geography'] = 17;
      quotas['history'] = 17;
      quotas['civics'] = 16;
    }

    let selectedQuestions = [];

    selectedSubjects.forEach(s => {
      const pool = bank[s] || [];
      const quota = quotas[s] || 0;
      if (pool.length === 0) return;

      // Group by type for balanced sampling
      const mcqs = pool.filter(q => q.type === 'mcq');
      const fibs = pool.filter(q => q.type === 'fib');
      const tfs = pool.filter(q => q.type === 'tf');
      const mtfs = pool.filter(q => q.type === 'mtf');

      // Target type proportions: ~40% MCQ, ~20% FIB, ~20% TF, ~20% MTF
      const mcqQuota = Math.round(quota * 0.40);
      const fibQuota = Math.round(quota * 0.20);
      const tfQuota = Math.round(quota * 0.20);
      const mtfQuota = quota - (mcqQuota + fibQuota + tfQuota);

      const sampled = [
        ...shuffleArray(mcqs).slice(0, mcqQuota),
        ...shuffleArray(fibs).slice(0, fibQuota),
        ...shuffleArray(tfs).slice(0, tfQuota),
        ...shuffleArray(mtfs).slice(0, mtfQuota)
      ];

      // If we fall short of quota due to category limits, fill from remaining pool
      if (sampled.length < quota) {
        const remaining = pool.filter(q => !sampled.some(sq => sq.id === q.id));
        sampled.push(...shuffleArray(remaining).slice(0, quota - sampled.length));
      }

      selectedQuestions.push(...sampled);
    });

    // Final shuffle so questions from different subjects are interwoven
    const final50 = shuffleArray(selectedQuestions).slice(0, 50);

    // Human-friendly title
    let titleParts = [];
    if (selectedSubjects.includes('history')) titleParts.push('History');
    if (selectedSubjects.includes('geography')) titleParts.push('Geography');
    if (selectedSubjects.includes('civics')) titleParts.push('Civics');
    const labelTitle = titleParts.length === 3 ? 'Full Social Science' : titleParts.join(' & ');

    return {
      testId: 'test_' + Date.now(),
      label: `Random Generated Test - ${labelTitle}`,
      selectedSubjects: selectedSubjects,
      subjectLabel: labelTitle,
      questions: final50,
      currentIndex: 0,
      userAnswers: {},
      flagged: new Set(),
      timeRemaining: 3600, // 60 minutes = 3600 seconds
      startTime: Date.now(),
      endTime: null,
      isSubmitted: false
    };
  }

  // --- LAUNCH EXAM ---
  function startExam(selectedSubjects) {
    const test = generateTest(selectedSubjects);
    if (!test) return;

    activeExam = test;
    renderExamModal();
    startTimer();
  }

  // --- TIMER ---
  function startTimer() {
    if (examTimerInterval) clearInterval(examTimerInterval);

    examTimerInterval = setInterval(() => {
      if (!activeExam || activeExam.isSubmitted) {
        clearInterval(examTimerInterval);
        return;
      }

      activeExam.timeRemaining--;

      // Update timer UI
      const timerEl = document.getElementById('examTimerDisplay');
      if (timerEl) {
        timerEl.textContent = formatSeconds(activeExam.timeRemaining);
        if (activeExam.timeRemaining <= 300) {
          timerEl.classList.add('text-red-400', 'animate-pulse');
        } else if (activeExam.timeRemaining <= 900) {
          timerEl.classList.add('text-amber-400');
        }
      }

      // Time expired! Auto-submit
      if (activeExam.timeRemaining <= 0) {
        clearInterval(examTimerInterval);
        alert("⏱️ Time is up! Your 1-hour exam period has concluded. Submitting test to reveal solutions and performance telemetry.");
        submitExam();
      }
    }, 1000);
  }

  // --- SUBMIT EXAM ---
  function submitExam() {
    if (!activeExam || activeExam.isSubmitted) return;

    if (examTimerInterval) clearInterval(examTimerInterval);
    activeExam.isSubmitted = true;
    activeExam.endTime = Date.now();
    activeExam.timeTakenSeconds = Math.max(1, 3600 - activeExam.timeRemaining);

    // Evaluate answers
    let totalScore = 0;
    let subjectScores = { geography: { score: 0, total: 0 }, history: { score: 0, total: 0 }, civics: { score: 0, total: 0 } };
    let typeScores = { mcq: { score: 0, total: 0 }, fib: { score: 0, total: 0 }, tf: { score: 0, total: 0 }, mtf: { score: 0, total: 0 } };

    activeExam.questions.forEach((q, idx) => {
      const userAns = activeExam.userAnswers[idx];
      let isCorrect = false;

      // Update subject & type totals
      const s = q.subject || 'geography';
      const t = q.type || 'mcq';
      if (!subjectScores[s]) subjectScores[s] = { score: 0, total: 0 };
      if (!typeScores[t]) typeScores[t] = { score: 0, total: 0 };
      subjectScores[s].total++;
      typeScores[t].total++;

      if (t === 'mcq') {
        if (userAns !== undefined && userAns !== null) {
          // Compare answer option strings or letters
          const cleanUser = String(userAns).trim().toLowerCase();
          const cleanAns = String(q.answer).trim().toLowerCase();
          
          // Match by exact string or letter prefix like '(a)' or 'a'
          if (cleanUser === cleanAns) {
            isCorrect = true;
          } else {
            const letterUser = cleanUser.match(/^\(?([a-d])\)?/);
            const letterAns = cleanAns.match(/^\(?([a-d])\)?/);
            if (letterUser && letterAns && letterUser[1] === letterAns[1]) {
              isCorrect = true;
            }
          }
        }
      } else if (t === 'tf') {
        if (userAns !== undefined && userAns !== null) {
          const expectedBool = Boolean(q.answer);
          isCorrect = (Boolean(userAns) === expectedBool);
        }
      } else if (t === 'fib') {
        if (userAns && String(userAns).trim().length > 0) {
          const userClean = String(userAns).trim().toLowerCase();
          const ansClean = String(q.answer).trim().toLowerCase();
          
          // Check exact match or comma/slash separated synonyms
          const acceptedParts = ansClean.split(/[,/]/).map(p => p.trim());
          if (userClean === ansClean || acceptedParts.includes(userClean)) {
            isCorrect = true;
          } else {
            // Check if key words match
            const allKeywordsMatch = acceptedParts.every(part => userClean.includes(part));
            if (allKeywordsMatch) isCorrect = true;
          }
        }
      } else if (t === 'mtf') {
        if (userAns && typeof userAns === 'object') {
          // Check if all pairs match
          const correctMatches = q.correctMatches || {};
          let allMatched = true;
          const keys = Object.keys(correctMatches);
          if (keys.length > 0) {
            for (let k of keys) {
              if (parseInt(userAns[k]) !== parseInt(correctMatches[k])) {
                allMatched = false;
                break;
              }
            }
            isCorrect = allMatched;
          }
        }
      }

      q.userAnswer = userAns !== undefined ? userAns : null;
      q.isCorrect = isCorrect;

      if (isCorrect) {
        totalScore++;
        subjectScores[s].score++;
        typeScores[t].score++;
      }
    });

    activeExam.score = totalScore;
    activeExam.subjectScores = subjectScores;
    activeExam.typeScores = typeScores;
    activeExam.percentage = Math.round((totalScore / 50) * 100);
    activeExam.date = new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' });

    // Save to Persistent Archive
    saveToArchive({
      testId: activeExam.testId,
      label: activeExam.label,
      subjectLabel: activeExam.subjectLabel,
      date: activeExam.date,
      score: totalScore,
      totalMarks: 50,
      percentage: activeExam.percentage,
      timeTakenSeconds: activeExam.timeTakenSeconds,
      selectedSubjects: activeExam.selectedSubjects,
      subjectScores: activeExam.subjectScores,
      typeScores: activeExam.typeScores,
      questions: activeExam.questions
    });

    // Render Review Solutions View
    renderReviewModal(activeExam);
  }

  // --- RENDER EXAM MODAL ---
  function renderExamModal() {
    let modal = document.getElementById('socialExamModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'socialExamModal';
      modal.className = 'fixed inset-0 z-[2000] bg-slate-950/95 backdrop-blur-md flex flex-col overflow-hidden text-slate-100 font-sans';
      document.body.appendChild(modal);
    }
    modal.classList.remove('hidden');

    const q = activeExam.questions[activeExam.currentIndex];
    const answeredCount = Object.keys(activeExam.userAnswers).length;

    modal.innerHTML = `
      <!-- TOP NAV BAR -->
      <div class="h-16 px-4 md:px-8 border-b border-slate-800 bg-slate-900/90 flex items-center justify-between shrink-0 shadow-lg">
        <div class="flex items-center gap-3">
          <button onclick="window.confirmExitExam()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-semibold flex items-center gap-1.5 transition-all cursor-pointer">
            <i class="fas fa-times"></i> Exit
          </button>
          <div>
            <h2 class="text-sm md:text-base font-bold text-white flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
              ${activeExam.label}
            </h2>
            <span class="text-[11px] text-slate-400 font-mono">50 Questions · 50 Marks · 1-Hour Timed Mode</span>
          </div>
        </div>

        <div class="flex items-center gap-3 md:gap-6">
          <!-- Live Timer -->
          <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-950 border border-slate-700/80 font-mono font-bold text-sm shadow-inner">
            <i class="fas fa-stopwatch text-indigo-400 text-xs"></i>
            <span id="examTimerDisplay">${formatSeconds(activeExam.timeRemaining)}</span>
          </div>

          <!-- Answered Counter -->
          <div class="hidden sm:flex items-center gap-1.5 text-xs text-slate-300 font-medium">
            <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold">${answeredCount} / 50</span>
            <span class="text-slate-400">Answered</span>
          </div>

          <!-- Finish Button -->
          <button onclick="window.confirmSubmitExam()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs md:text-sm shadow-lg shadow-emerald-900/30 transition-all flex items-center gap-2 cursor-pointer">
            <i class="fas fa-check-circle"></i>
            <span>Submit Test</span>
          </button>
        </div>
      </div>

      <!-- MAIN EXAM WORKSPACE -->
      <div class="flex-1 flex overflow-hidden">
        <!-- LEFT: QUESTION PALETTE (Desktop) -->
        <aside class="w-64 border-r border-slate-800 bg-slate-900/40 p-4 hidden md:flex flex-col shrink-0">
          <div class="flex items-center justify-between mb-3 text-xs text-slate-400 font-bold uppercase tracking-wider">
            <span>Question Palette</span>
            <span class="text-indigo-400 font-mono">${activeExam.currentIndex + 1} / 50</span>
          </div>
          
          <div class="grid grid-cols-5 gap-2 overflow-y-auto pr-1 flex-1">
            ${activeExam.questions.map((ques, i) => {
              const isAnswered = activeExam.userAnswers[i] !== undefined;
              const isCurrent = activeExam.currentIndex === i;
              const isFlagged = activeExam.flagged.has(i);
              
              let bg = "bg-slate-800/80 text-slate-400 border-slate-700";
              if (isAnswered) bg = "bg-emerald-600 text-white border-emerald-500 font-bold";
              if (isFlagged) bg = "bg-amber-500 text-slate-950 border-amber-400 font-bold";
              if (isCurrent) bg += " ring-2 ring-indigo-400 ring-offset-2 ring-offset-slate-900 scale-105";

              return `<button onclick="window.jumpToQuestion(${i})" class="w-10 h-10 rounded-lg text-xs font-mono border flex items-center justify-center transition-all cursor-pointer ${bg}">${i + 1}</button>`;
            }).join('')}
          </div>

          <div class="mt-4 pt-3 border-t border-slate-800 text-[11px] text-slate-400 space-y-1.5">
            <div class="flex items-center gap-2"><span class="w-3 h-3 rounded bg-emerald-600"></span> Answered</div>
            <div class="flex items-center gap-2"><span class="w-3 h-3 rounded bg-amber-500"></span> Flagged for Review</div>
            <div class="flex items-center gap-2"><span class="w-3 h-3 rounded bg-slate-800 border border-slate-700"></span> Unanswered</div>
          </div>
        </aside>

        <!-- RIGHT: QUESTION DISPLAY & INPUT AREA -->
        <main class="flex-1 overflow-y-auto p-4 md:p-8 flex flex-col justify-between max-w-4xl mx-auto w-full">
          <div>
            <!-- Question Metadata Bar -->
            <div class="flex flex-wrap items-center justify-between gap-2 pb-4 mb-6 border-b border-slate-800">
              <div class="flex items-center gap-2 flex-wrap">
                <span class="px-3 py-1 rounded-lg bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 text-xs font-mono font-bold">
                  Q${activeExam.currentIndex + 1} of 50
                </span>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold uppercase tracking-wider ${
                  q.subject === 'geography' ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30' :
                  q.subject === 'history' ? 'bg-amber-500/10 text-amber-400 border border-amber-500/30' :
                  'bg-blue-500/10 text-blue-400 border border-blue-500/30'
                }">
                  ${q.subject}
                </span>
                <span class="text-xs text-slate-400 font-medium">Ch ${q.chapterNum}: ${q.chapterTitle}</span>
              </div>

              <div class="flex items-center gap-2">
                <span class="px-2.5 py-0.5 rounded bg-slate-800 text-slate-300 text-xs font-mono">1 Mark</span>
                <span class="px-2.5 py-0.5 rounded bg-purple-500/10 text-purple-300 border border-purple-500/30 text-xs font-mono uppercase font-bold">
                  ${q.type.toUpperCase()}
                </span>
              </div>
            </div>

            <!-- Question Stem -->
            <div class="text-base md:text-lg font-medium text-slate-100 leading-relaxed mb-6">
              ${q.question}
            </div>

            <!-- Interactive Answer Controls (Strictly NO answers revealed!) -->
            <div class="space-y-4 my-6">
              ${renderQuestionInput(q, activeExam.currentIndex)}
            </div>
          </div>

          <!-- BOTTOM ACTION FOOTER -->
          <div class="pt-6 border-t border-slate-800 flex items-center justify-between gap-3 mt-8">
            <button onclick="window.prevQuestion()" ${activeExam.currentIndex === 0 ? 'disabled' : ''} class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 disabled:opacity-40 text-slate-200 text-xs md:text-sm font-semibold flex items-center gap-2 transition-all cursor-pointer">
              <i class="fas fa-chevron-left"></i> Previous
            </button>

            <button onclick="window.toggleFlagCurrent()" class="px-4 py-2 rounded-xl border ${
              activeExam.flagged.has(activeExam.currentIndex) ? 'bg-amber-500/20 border-amber-400 text-amber-300' : 'border-slate-700 bg-slate-800/60 text-slate-300'
            } text-xs md:text-sm font-semibold flex items-center gap-2 transition-all cursor-pointer">
              <i class="fas fa-flag"></i>
              <span>${activeExam.flagged.has(activeExam.currentIndex) ? 'Flagged' : 'Mark for Review'}</span>
            </button>

            ${activeExam.currentIndex < 49 ? `
              <button onclick="window.nextQuestion()" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs md:text-sm font-bold flex items-center gap-2 transition-all cursor-pointer">
                <span>Next</span> <i class="fas fa-chevron-right"></i>
              </button>
            ` : `
              <button onclick="window.confirmSubmitExam()" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs md:text-sm font-bold flex items-center gap-2 transition-all cursor-pointer">
                <i class="fas fa-check-circle"></i> <span>Submit Exam</span>
              </button>
            `}
          </div>
        </main>
      </div>
    `;
  }

  // --- RENDER QUESTION INPUT ACCORDING TO TYPE ---
  function renderQuestionInput(q, idx) {
    const currentAns = activeExam.userAnswers[idx];

    if (q.type === 'mcq') {
      return (q.options || []).map((opt, optIdx) => {
        const isSelected = currentAns === opt;
        return `
          <label onclick="window.selectMcqAnswer(${idx}, '${opt.replace(/'/g, "\\'")}')" class="flex items-center gap-3.5 p-3.5 md:p-4 rounded-xl border transition-all cursor-pointer ${
            isSelected ? 'bg-indigo-600/20 border-indigo-500 text-white shadow-md shadow-indigo-900/20' : 'bg-slate-900/70 border-slate-800 text-slate-300 hover:bg-slate-800/60 hover:border-slate-700'
          }">
            <div class="w-5 h-5 rounded-full border-2 flex items-center justify-center shrink-0 ${
              isSelected ? 'border-indigo-400 bg-indigo-500' : 'border-slate-600'
            }">
              ${isSelected ? '<div class="w-2 h-2 rounded-full bg-white"></div>' : ''}
            </div>
            <span class="text-sm md:text-base leading-relaxed">${opt}</span>
          </label>
        `;
      }).join('');
    }

    if (q.type === 'tf') {
      return `
        <div class="grid grid-cols-2 gap-4 max-w-md">
          <button onclick="window.selectTfAnswer(${idx}, true)" class="py-4 px-6 rounded-2xl border text-sm md:text-base font-bold flex items-center justify-center gap-2 transition-all cursor-pointer ${
            currentAns === true ? 'bg-emerald-600 border-emerald-400 text-white shadow-lg shadow-emerald-900/40 ring-2 ring-emerald-400' : 'bg-slate-900/80 border-slate-700 text-slate-300 hover:bg-slate-800'
          }">
            <i class="fas fa-check-circle text-lg"></i> True
          </button>
          <button onclick="window.selectTfAnswer(${idx}, false)" class="py-4 px-6 rounded-2xl border text-sm md:text-base font-bold flex items-center justify-center gap-2 transition-all cursor-pointer ${
            currentAns === false ? 'bg-rose-600 border-rose-400 text-white shadow-lg shadow-rose-900/40 ring-2 ring-rose-400' : 'bg-slate-900/80 border-slate-700 text-slate-300 hover:bg-slate-800'
          }">
            <i class="fas fa-times-circle text-lg"></i> False
          </button>
        </div>
      `;
    }

    if (q.type === 'fib') {
      return `
        <div class="space-y-2">
          <label class="text-xs text-slate-400 font-mono">Type your missing word / term:</label>
          <input type="text" value="${currentAns || ''}" oninput="window.setFibAnswer(${idx}, this.value)" placeholder="Enter the exact answer here..." class="w-full max-w-lg px-4 py-3 rounded-xl bg-slate-950 border border-slate-700 text-white text-base focus:outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20 transition-all font-medium">
          <span class="text-[11px] text-slate-500 block">Answers are evaluated case-insensitively.</span>
        </div>
      `;
    }

    if (q.type === 'mtf') {
      const colA = q.columnA || [];
      const colB = q.columnB || [];
      const userMatches = currentAns || {};

      return `
        <div class="bg-slate-950/80 rounded-2xl border border-slate-800 p-4 space-y-4">
          <div class="text-xs text-indigo-400 font-mono font-bold uppercase tracking-wider mb-2">
            Match Column A with Column B:
          </div>
          <div class="space-y-3">
            ${colA.map((itemA, rowIdx) => {
              const selectedB = userMatches[rowIdx];
              return `
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-3 rounded-xl bg-slate-900 border border-slate-800">
                  <div class="font-medium text-sm text-slate-200 flex-1">
                    ${itemA}
                  </div>
                  <div class="sm:w-72 shrink-0">
                    <select onchange="window.setMtfMatch(${idx}, ${rowIdx}, this.value)" class="w-full px-3 py-2 rounded-lg bg-slate-950 border border-slate-700 text-xs text-indigo-300 focus:outline-none focus:border-indigo-500 cursor-pointer">
                      <option value="">-- Select Match from Column B --</option>
                      ${colB.map((itemB, bIdx) => `
                        <option value="${bIdx}" ${selectedB == bIdx ? 'selected' : ''}>${itemB}</option>
                      `).join('')}
                    </select>
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
    }

    return `<div class="text-slate-500 italic">No input configuration required.</div>`;
  }

  // --- REVIEW SOLUTIONS MODAL ---
  function renderReviewModal(testData) {
    const modal = document.getElementById('socialExamModal');
    if (!modal) return;

    modal.innerHTML = `
      <!-- TOP NAV -->
      <div class="h-16 px-4 md:px-8 border-b border-slate-800 bg-slate-900/90 flex items-center justify-between shrink-0 shadow-lg">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm">
            <i class="fas fa-award"></i>
          </div>
          <div>
            <h2 class="text-sm md:text-base font-bold text-white">${testData.label} · Official Solutions</h2>
            <span class="text-[11px] text-slate-400 font-mono">${testData.date} · Time Taken: ${formatTimeTaken(testData.timeTakenSeconds)}</span>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <button onclick="window.closeExamModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs md:text-sm font-semibold transition-all cursor-pointer">
            <i class="fas fa-times"></i> Close Review
          </button>
        </div>
      </div>

      <!-- SOLUTIONS BODY -->
      <div class="flex-1 overflow-y-auto p-4 md:p-8 max-w-5xl mx-auto w-full space-y-8">
        
        <!-- SCORECARD HERO BANNER -->
        <div class="p-6 md:p-8 rounded-3xl bg-gradient-to-br from-slate-900 via-slate-900 to-slate-950 border border-indigo-500/30 shadow-2xl relative overflow-hidden">
          <div class="flex flex-col md:flex-row items-center justify-between gap-6 relative z-10">
            <div class="flex items-center gap-5">
              <div class="w-24 h-24 rounded-2xl bg-indigo-500/10 border-2 border-indigo-500/40 flex flex-col items-center justify-center text-center shadow-lg">
                <span class="text-3xl font-extrabold text-white font-mono leading-none">${testData.score}</span>
                <span class="text-xs text-indigo-400 font-mono mt-1">/ 50 Marks</span>
              </div>
              <div>
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider mb-2 ${
                  testData.percentage >= 80 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' :
                  testData.percentage >= 60 ? 'bg-amber-500/20 text-amber-400 border border-amber-500/40' :
                  'bg-rose-500/20 text-rose-400 border border-rose-500/40'
                }">
                  ${testData.percentage >= 80 ? '🌟 Superior Rigor Mastered' : testData.percentage >= 60 ? '⚡ Solid Prep · Notes Review Advised' : '⚠️ Intensive Revision Required'}
                </div>
                <h3 class="text-xl md:text-2xl font-bold text-white font-heading">
                  Diagnostic Performance: ${testData.percentage}%
                </h3>
                <p class="text-slate-400 text-xs md:text-sm mt-1 max-w-xl">
                  Above-average difficulty drill completed. Review every solution below and study the cited notes references to address any gaps before the actual exam.
                </p>
              </div>
            </div>

            <div class="flex flex-col gap-2 w-full md:w-auto">
              <button onclick="window.launchNewTestFromModal()" class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs md:text-sm shadow-lg shadow-indigo-900/30 transition-all flex items-center justify-center gap-2 cursor-pointer">
                <i class="fas fa-redo"></i> Generate Another Test
              </button>
            </div>
          </div>

          <!-- Subject & Type Telemetry Badges -->
          <div class="mt-6 pt-6 border-t border-slate-800 grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
              <span class="text-slate-400 block text-[10px] uppercase font-bold">Time Spent</span>
              <span class="text-white font-mono text-sm font-bold">${formatTimeTaken(testData.timeTakenSeconds)}</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
              <span class="text-slate-400 block text-[10px] uppercase font-bold">MCQs Accuracy</span>
              <span class="text-white font-mono text-sm font-bold">${testData.typeScores.mcq.score} / ${testData.typeScores.mcq.total}</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
              <span class="text-slate-400 block text-[10px] uppercase font-bold">FIB & T/F</span>
              <span class="text-white font-mono text-sm font-bold">${testData.typeScores.fib.score + testData.typeScores.tf.score} / ${testData.typeScores.fib.total + testData.typeScores.tf.total}</span>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800">
              <span class="text-slate-400 block text-[10px] uppercase font-bold">Match Following</span>
              <span class="text-white font-mono text-sm font-bold">${testData.typeScores.mtf.score} / ${testData.typeScores.mtf.total}</span>
            </div>
          </div>
        </div>

        <!-- FILTER CHIPS -->
        <div class="flex items-center gap-2 overflow-x-auto pb-2 border-b border-slate-800">
          <button onclick="window.filterReviewQuestions('all')" class="review-filter-btn active px-3.5 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white cursor-pointer" data-filter="all">All (50)</button>
          <button onclick="window.filterReviewQuestions('incorrect')" class="review-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-rose-400 cursor-pointer" data-filter="incorrect">Incorrect (${50 - testData.score})</button>
          <button onclick="window.filterReviewQuestions('correct')" class="review-filter-btn px-3.5 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-emerald-400 cursor-pointer" data-filter="correct">Correct (${testData.score})</button>
        </div>

        <!-- 50 QUESTION SOLUTION CARDS -->
        <div class="space-y-6" id="reviewQuestionsList">
          ${testData.questions.map((q, idx) => {
            const isCorrect = q.isCorrect;
            const isUnanswered = q.userAnswer === null || q.userAnswer === undefined;
            
            let statusBadge = '';
            let cardBorder = 'border-slate-800';
            if (isCorrect) {
              statusBadge = '<span class="px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-bold flex items-center gap-1"><i class="fas fa-check"></i> Correct (+1)</span>';
              cardBorder = 'border-emerald-500/30';
            } else if (isUnanswered) {
              statusBadge = '<span class="px-2.5 py-0.5 rounded-full bg-slate-700 text-slate-300 text-xs font-bold flex items-center gap-1"><i class="fas fa-minus"></i> Unanswered (0)</span>';
            } else {
              statusBadge = '<span class="px-2.5 py-0.5 rounded-full bg-rose-500/20 text-rose-400 border border-rose-500/30 text-xs font-bold flex items-center gap-1"><i class="fas fa-times"></i> Incorrect (0)</span>';
              cardBorder = 'border-rose-500/30';
            }

            return `
              <div class="review-q-card p-5 md:p-6 rounded-2xl bg-slate-900/90 border ${cardBorder} space-y-4" data-status="${isCorrect ? 'correct' : (isUnanswered ? 'unanswered' : 'incorrect')}">
                <div class="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-800">
                  <div class="flex items-center gap-2">
                    <span class="font-mono font-bold text-sm text-indigo-400">Q${idx + 1}.</span>
                    <span class="px-2 py-0.5 rounded bg-slate-800 text-[11px] font-semibold uppercase ${
                      q.subject === 'geography' ? 'text-emerald-400' : q.subject === 'history' ? 'text-amber-400' : 'text-blue-400'
                    }">${q.subject}</span>
                    <span class="text-xs text-slate-400">Ch ${q.chapterNum}: ${q.chapterTitle}</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="px-2 py-0.5 rounded bg-slate-800 text-xs font-mono uppercase text-slate-400">${q.type}</span>
                    ${statusBadge}
                  </div>
                </div>

                <!-- Question Prompt -->
                <div class="text-base text-slate-100 font-medium leading-relaxed">
                  ${q.question}
                </div>

                <!-- Answer Review Block -->
                <div class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs md:text-sm space-y-2">
                  <div class="flex items-start gap-2">
                    <span class="font-bold text-slate-400 w-28 shrink-0">Your Answer:</span>
                    <span class="${isCorrect ? 'text-emerald-400 font-bold' : (isUnanswered ? 'text-slate-500 italic' : 'text-rose-400 font-bold')}">
                      ${formatUserAnswerDisplay(q)}
                    </span>
                  </div>
                  <div class="flex items-start gap-2">
                    <span class="font-bold text-slate-400 w-28 shrink-0">Correct Answer:</span>
                    <span class="text-emerald-400 font-bold font-mono">
                      ${formatCorrectAnswerDisplay(q)}
                    </span>
                  </div>
                </div>

                <!-- Pedagogical In-Depth Explanation -->
                <div class="p-3.5 rounded-xl bg-indigo-950/20 border border-indigo-500/20 text-xs md:text-sm text-slate-300 leading-relaxed">
                  <strong class="text-indigo-400 block mb-1 font-semibold flex items-center gap-1.5">
                    <i class="fas fa-lightbulb"></i> Conceptual Explanation:
                  </strong>
                  ${q.explanation}
                </div>

                <!-- Notes Reference (encourages reading notes rather than being overconfident) -->
                <div class="flex items-center gap-2 text-xs text-amber-400 font-mono bg-amber-500/10 px-3 py-1.5 rounded-lg border border-amber-500/20">
                  <i class="fas fa-book-open"></i>
                  <span><strong>Refer to Notes:</strong> ${q.notesRef}</span>
                </div>
              </div>
            `;
          }).join('')}
        </div>

      </div>
    `;
  }

  function formatUserAnswerDisplay(q) {
    if (q.userAnswer === null || q.userAnswer === undefined) return 'Not Attempted';
    if (q.type === 'tf') return q.userAnswer ? 'True' : 'False';
    if (q.type === 'mtf') {
      const userMatches = q.userAnswer || {};
      const colA = q.columnA || [];
      const colB = q.columnB || [];
      return Object.keys(userMatches).map(k => {
        const itemA = colA[k] || `Item ${parseInt(k)+1}`;
        const itemB = colB[userMatches[k]] || 'None';
        return `[${itemA} ➔ ${itemB}]`;
      }).join(', ');
    }
    return String(q.userAnswer);
  }

  function formatCorrectAnswerDisplay(q) {
    if (q.type === 'tf') return q.answer ? 'True' : 'False';
    if (q.type === 'mtf') {
      const correctMatches = q.correctMatches || {};
      const colA = q.columnA || [];
      const colB = q.columnB || [];
      return Object.keys(correctMatches).map(k => {
        const itemA = colA[k] || `Item ${parseInt(k)+1}`;
        const itemB = colB[correctMatches[k]] || '';
        return `[${itemA} ➔ ${itemB}]`;
      }).join(', ');
    }
    return String(q.answer);
  }

  // --- RENDER SOLVED TESTS ARCHIVE LIST IN THE TAB ---
  function renderArchiveList() {
    const container = document.getElementById('solvedTestsArchiveContainer');
    if (!container) return;

    const archive = getArchive();
    if (archive.length === 0) {
      container.innerHTML = `
        <div class="text-center py-8 px-4 rounded-2xl bg-slate-900/40 border border-slate-800 text-slate-400">
          <i class="fas fa-clipboard-list text-3xl mb-2 text-slate-600 block"></i>
          <p class="font-medium text-sm">No solved tests yet.</p>
          <span class="text-xs text-slate-500">Configure your sections above and launch a 50-mark test to build your archive!</span>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div class="flex items-center justify-between mb-4">
        <span class="text-xs font-mono text-slate-400 font-bold uppercase tracking-wider">
          ${archive.length} Test${archive.length > 1 ? 's' : ''} Solved & Archived
        </span>
        <button onclick="window.clearAllArchive()" class="text-xs text-rose-400 hover:text-rose-300 flex items-center gap-1 cursor-pointer">
          <i class="fas fa-trash-alt"></i> Clear Archive
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${archive.map(test => `
          <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 hover:border-slate-700 transition-all flex flex-col justify-between gap-4 shadow-lg">
            <div class="space-y-2">
              <div class="flex items-center justify-between gap-2">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider ${
                  test.percentage >= 80 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' :
                  test.percentage >= 60 ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
                  'bg-rose-500/20 text-rose-400 border border-rose-500/30'
                }">
                  Score: ${test.score} / 50 (${test.percentage}%)
                </span>
                <span class="text-[11px] text-slate-500 font-mono">${test.date}</span>
              </div>
              <h4 class="font-bold text-white text-base leading-snug">
                ${test.label}
              </h4>
              <div class="flex items-center gap-3 text-xs text-slate-400 font-mono">
                <span><i class="fas fa-stopwatch text-indigo-400"></i> ${formatTimeTaken(test.timeTakenSeconds)}</span>
                <span>•</span>
                <span>50 Questions Evaluated</span>
              </div>
            </div>

            <div class="pt-3 border-t border-slate-800 flex items-center justify-between gap-2">
              <button onclick="window.viewArchivedTestSolutions('${test.testId}')" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold flex items-center gap-1.5 transition-all cursor-pointer">
                <i class="fas fa-book-open"></i> Review Solutions & Notes
              </button>
              <button onclick="window.deleteArchivedTest('${test.testId}')" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-slate-400 hover:text-rose-400 flex items-center justify-center transition-all cursor-pointer" title="Delete this test">
                <i class="fas fa-trash text-xs"></i>
              </button>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  // --- WINDOW GLOBAL CONTROLS ---
  window.launchSocialTest = function() {
    const selected = [];
    if (document.getElementById('chkSubjGeo')?.checked) selected.push('geography');
    if (document.getElementById('chkSubjHist')?.checked) selected.push('history');
    if (document.getElementById('chkSubjCiv')?.checked) selected.push('civics');

    startExam(selected);
  };

  window.selectSubjectPreset = function(preset) {
    const g = document.getElementById('chkSubjGeo');
    const h = document.getElementById('chkSubjHist');
    const c = document.getElementById('chkSubjCiv');
    if (!g || !h || !c) return;

    if (preset === 'all') {
      g.checked = true; h.checked = true; c.checked = true;
    } else if (preset === 'geo') {
      g.checked = true; h.checked = false; c.checked = false;
    } else if (preset === 'hist') {
      g.checked = false; h.checked = true; c.checked = false;
    } else if (preset === 'civ') {
      g.checked = false; h.checked = false; c.checked = true;
    }
  };

  window.jumpToQuestion = function(idx) {
    if (!activeExam || idx < 0 || idx >= 50) return;
    activeExam.currentIndex = idx;
    renderExamModal();
  };

  window.nextQuestion = function() {
    if (!activeExam || activeExam.currentIndex >= 49) return;
    activeExam.currentIndex++;
    renderExamModal();
  };

  window.prevQuestion = function() {
    if (!activeExam || activeExam.currentIndex <= 0) return;
    activeExam.currentIndex--;
    renderExamModal();
  };

  window.toggleFlagCurrent = function() {
    if (!activeExam) return;
    const cur = activeExam.currentIndex;
    if (activeExam.flagged.has(cur)) {
      activeExam.flagged.delete(cur);
    } else {
      activeExam.flagged.add(cur);
    }
    renderExamModal();
  };

  window.selectMcqAnswer = function(qIdx, val) {
    if (!activeExam) return;
    activeExam.userAnswers[qIdx] = val;
    renderExamModal();
  };

  window.selectTfAnswer = function(qIdx, val) {
    if (!activeExam) return;
    activeExam.userAnswers[qIdx] = val;
    renderExamModal();
  };

  window.setFibAnswer = function(qIdx, val) {
    if (!activeExam) return;
    activeExam.userAnswers[qIdx] = val;
  };

  window.setMtfMatch = function(qIdx, rowIdx, bIdx) {
    if (!activeExam) return;
    if (!activeExam.userAnswers[qIdx]) activeExam.userAnswers[qIdx] = {};
    activeExam.userAnswers[qIdx][rowIdx] = parseInt(bIdx);
  };

  window.confirmSubmitExam = function() {
    if (!activeExam) return;
    const answeredCount = Object.keys(activeExam.userAnswers).length;
    const unanswered = 50 - answeredCount;

    let msg = `Are you ready to submit your exam and reveal the solutions?\n\n` +
              `• Answered: ${answeredCount} / 50\n` +
              `• Unanswered: ${unanswered}\n` +
              `• Time Remaining: ${formatSeconds(activeExam.timeRemaining)}`;

    if (unanswered > 0) {
      msg += `\n\n⚠️ Note: You still have ${unanswered} unanswered questions!`;
    }

    if (confirm(msg)) {
      submitExam();
    }
  };

  window.confirmExitExam = function() {
    if (!activeExam) return;
    if (confirm("Are you sure you want to exit? Your active exam progress will be lost.")) {
      if (examTimerInterval) clearInterval(examTimerInterval);
      activeExam = null;
      const modal = document.getElementById('socialExamModal');
      if (modal) modal.classList.add('hidden');
    }
  };

  window.closeExamModal = function() {
    const modal = document.getElementById('socialExamModal');
    if (modal) modal.classList.add('hidden');
    activeExam = null;
    renderArchiveList();
  };

  window.launchNewTestFromModal = function() {
    window.closeExamModal();
    window.launchSocialTest();
  };

  window.viewArchivedTestSolutions = function(testId) {
    const archive = getArchive();
    const test = archive.find(t => t.testId === testId);
    if (!test) return;

    let modal = document.getElementById('socialExamModal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'socialExamModal';
      modal.className = 'fixed inset-0 z-[2000] bg-slate-950/95 backdrop-blur-md flex flex-col overflow-hidden text-slate-100 font-sans';
      document.body.appendChild(modal);
    }
    modal.classList.remove('hidden');

    renderReviewModal(test);
  };

  window.deleteArchivedTest = function(testId) {
    deleteFromArchive(testId);
  };

  window.clearAllArchive = function() {
    clearAllArchive();
  };

  window.filterReviewQuestions = function(filter) {
    document.querySelectorAll('.review-filter-btn').forEach(b => {
      b.classList.remove('bg-indigo-600', 'text-white');
      b.classList.add('bg-slate-800', 'text-slate-300');
      if (b.getAttribute('data-filter') === filter) {
        b.classList.remove('bg-slate-800', 'text-slate-300');
        b.classList.add('bg-indigo-600', 'text-white');
      }
    });

    document.querySelectorAll('.review-q-card').forEach(card => {
      const status = card.getAttribute('data-status');
      if (filter === 'all') {
        card.style.display = '';
      } else if (filter === 'correct' && status === 'correct') {
        card.style.display = '';
      } else if (filter === 'incorrect' && (status === 'incorrect' || status === 'unanswered')) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  };

  // Auto-init archive rendering on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    renderArchiveList();
  });

  // Also expose init function
  window.initSocialTestArchive = renderArchiveList;

})();
