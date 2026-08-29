/**
 * Pushti Study Hub - Main Application JavaScript
 * 
 * A comprehensive vanilla JavaScript application for a static HTML study hub.
 * Handles interactivity, theme management, navigation, search, media, and more.
 */

(function () {
  'use strict';

  // ==========================================
  // CONFIGURATION & GLOBALS
  // ==========================================
  const CONFIG = {
    DEBOUNCE_MS: 300,
    ANIMATION_MS: 300,
    SCROLL_THRESHOLD: 300,
    SEARCH_MIN_CHARS: 2,
    THEME_KEY: 'pushti-theme',
    TAB_KEY: 'pushti-active-tab',
    DEBUG: false // Set to true to enable debug logs
  };

  /**
   * Utility functions
   */
  const Utils = {
    /**
     * Logger that respects the DEBUG flag
     */
    log: (...args) => {
      if (CONFIG.DEBUG) {
        console.log('[PushtiHub]', ...args);
      }
    },
    
    /**
     * Debounce function to limit how often a function can run
     */
    debounce: (func, wait) => {
      let timeout;
      return function executedFunction(...args) {
        const later = () => {
          clearTimeout(timeout);
          func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
      };
    },

    /**
     * Check if an element exists
     */
    exists: (selector) => document.querySelector(selector) !== null
  };


  // ==========================================
  // 1. THEME MANAGEMENT
  // ==========================================
  class ThemeManager {
    constructor() {
      this.toggleBtn = document.querySelector('.theme-toggle');
      this.body = document.body;
      this.init();
    }

    init() {
      Utils.log('Initializing ThemeManager');
      
      // Determine initial theme
      const savedTheme = localStorage.getItem(CONFIG.THEME_KEY);
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      
      let initialTheme = 'light';
      if (savedTheme) {
        initialTheme = savedTheme;
      } else if (prefersDark) {
        initialTheme = 'dark';
      }

      this.setTheme(initialTheme);

      // Listen for theme change messages from parent frame
      window.addEventListener('message', (event) => {
        if (event.data && event.data.theme) {
          this.setTheme(event.data.theme);
        }
      });
      
      // Add event listener if toggle button exists
      if (this.toggleBtn) {
        this.toggleBtn.addEventListener('click', () => this.toggleTheme());
      }
    }

    setTheme(theme) {
      this.body.setAttribute('data-theme', theme);
      localStorage.setItem(CONFIG.THEME_KEY, theme);
      this.updateIcon(theme);
      Utils.log(`Theme set to ${theme}`);
    }

    toggleTheme() {
      const currentTheme = this.body.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      this.setTheme(newTheme);
    }

    updateIcon(theme) {
      if (!this.toggleBtn) return;
      const icon = this.toggleBtn.querySelector('i');
      if (icon) {
        icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
      }
    }
  }


  // ==========================================
  // 2. TAB NAVIGATION (CHAPTER TABS)
  // ==========================================
  class TabManager {
    constructor() {
      this.tabButtons = document.querySelectorAll('button.tab[data-tab]');
      this.tabPanes = document.querySelectorAll('section.tab-pane[id]');
      if (this.tabButtons.length > 0 && this.tabPanes.length > 0) {
        this.init();
      }
    }

    init() {
      Utils.log('Initializing TabManager');

      // Click events
      const tabList = document.querySelector('.tab-list') || document.body;
      tabList.addEventListener('click', (e) => {
        const btn = e.target.closest('button.tab[data-tab]');
        if (btn) {
          this.switchTab(btn.dataset.tab);
        }
      });

      // Keyboard navigation
      tabList.addEventListener('keydown', (e) => this.handleKeydown(e));

      // Handle URL hash on load
      this.handleHashChange();
      window.addEventListener('hashchange', () => this.handleHashChange());
    }

    switchTab(tabId) {
      Utils.log(`Switching to tab: ${tabId}`);
      let targetPane = document.getElementById(tabId);
      
      if (!targetPane) return;

      // Update Buttons
      this.tabButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.tab === tabId);
        btn.setAttribute('aria-selected', btn.dataset.tab === tabId);
      });

      // Update Panes
      this.tabPanes.forEach(pane => {
        pane.classList.remove('active', 'fade-in');
      });

      targetPane.classList.add('active');
      // Force reflow for animation
      void targetPane.offsetWidth;
      targetPane.classList.add('fade-in');

      // Update URL hash
      history.replaceState(null, null, `#${tabId}`);
    }

    handleHashChange() {
      const hash = window.location.hash.replace('#', '');
      if (hash && document.getElementById(hash) && document.querySelector(`button.tab[data-tab="${hash}"]`)) {
        this.switchTab(hash);
      } else if (this.tabButtons.length > 0) {
        // Default to first tab
        this.switchTab(this.tabButtons[0].dataset.tab);
      }
    }

    handleKeydown(e) {
      const activeBtn = document.activeElement;
      if (!activeBtn.classList.contains('tab')) return;

      const tabsArray = Array.from(this.tabButtons);
      let index = tabsArray.indexOf(activeBtn);
      
      if (e.key === 'ArrowRight') {
        index = (index + 1) % tabsArray.length;
        tabsArray[index].focus();
        this.switchTab(tabsArray[index].dataset.tab);
      } else if (e.key === 'ArrowLeft') {
        index = (index - 1 + tabsArray.length) % tabsArray.length;
        tabsArray[index].focus();
        this.switchTab(tabsArray[index].dataset.tab);
      }
    }
  }


  // ==========================================
  // 3. TOPIC NAVIGATION (WITHIN NOTES)
  // ==========================================
  class TopicManager {
    constructor() {
      this.topicButtons = document.querySelectorAll('button.topic-tab[data-topic]');
      this.topicPanes = document.querySelectorAll('.topic-pane[data-topic-id]');
      if (this.topicButtons.length > 0 && this.topicPanes.length > 0) {
        this.init();
      }
    }

    init() {
      Utils.log('Initializing TopicManager');

      const sidebar = document.querySelector('.topic-sidebar') || document.body;
      sidebar.addEventListener('click', (e) => {
        const btn = e.target.closest('button.topic-tab[data-topic]');
        if (btn) {
          this.switchTopic(btn.dataset.topic);
        }
      });
    }

    switchTopic(topicId) {
      Utils.log(`Switching topic to: ${topicId}`);
      
      let foundPane = false;

      // Update Buttons
      this.topicButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.topic === topicId);
      });

      // Update Panes
      this.topicPanes.forEach(pane => {
        if (pane.dataset.topicId === topicId) {
          pane.classList.add('active', 'fade-in');
          foundPane = true;
        } else {
          pane.classList.remove('active', 'fade-in');
        }
      });

      if (foundPane) {
        // Smooth scroll to top of content
        const contentContainer = document.querySelector('.notes-content');
        if (contentContainer) {
          contentContainer.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    }
  }


  // ==========================================
  // 4. SEARCH FUNCTIONALITY
  // ==========================================
  class SearchManager {
    constructor() {
      this.searchInput = document.querySelector('.search-input');
      this.searchResults = document.querySelector('.search-results');
      if (this.searchInput && this.searchResults) {
        this.fuse = null;
        this.searchData = [];
        this.init();
      }
    }

    init() {
      Utils.log('Initializing SearchManager');
      this.buildSearchData();
      
      if (window.Fuse) {
        this.fuse = new window.Fuse(this.searchData, {
          keys: ['title', 'content', 'tags'],
          includeScore: true,
          includeMatches: true,
          threshold: 0.3
        });
        Utils.log('Fuse.js initialized successfully.');
      } else {
        Utils.log('Fuse.js not found, falling back to simple search.');
      }

      const handleInput = Utils.debounce((e) => this.performSearch(e.target.value), CONFIG.DEBOUNCE_MS);
      this.searchInput.addEventListener('input', handleInput);
      
      // Close on escape
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && this.searchResults.classList.contains('show')) {
          this.closeResults();
        }
      });

      // Close on click outside
      document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container')) {
          this.closeResults();
        }
      });
    }

    buildSearchData() {
      // Gather data from the page for search
      // Assuming sections with data-search-title and text content
      const searchElements = document.querySelectorAll('[data-search-title]');
      searchElements.forEach((el, index) => {
        this.searchData.push({
          id: index,
          title: el.getAttribute('data-search-title') || 'Section',
          content: el.textContent.replace(/\s+/g, ' ').trim(),
          tags: el.getAttribute('data-search-tags') || '',
          elementId: el.id,
          tabId: el.closest('.tab-pane') ? el.closest('.tab-pane').id : null
        });
      });
    }

    performSearch(query) {
      if (query.length < CONFIG.SEARCH_MIN_CHARS) {
        this.closeResults();
        return;
      }

      let results = [];
      if (this.fuse) {
        results = this.fuse.search(query).map(result => result.item);
      } else {
        // Fallback simple search
        const lowerQuery = query.toLowerCase();
        results = this.searchData.filter(item => 
          item.title.toLowerCase().includes(lowerQuery) || 
          item.content.toLowerCase().includes(lowerQuery)
        );
      }

      this.renderResults(results, query);
    }

    renderResults(results, query) {
      this.searchResults.innerHTML = '';
      
      if (results.length === 0) {
        this.searchResults.innerHTML = '<div class="no-results">No results found</div>';
      } else {
        // Limit to top 5
        results.slice(0, 5).forEach(item => {
          const div = document.createElement('div');
          div.className = 'search-result-item';
          
          // Generate simple snippet
          let snippet = item.content.substring(0, 80) + '...';
          
          div.innerHTML = `
            <h4>${item.title}</h4>
            <p>${snippet}</p>
          `;
          
          div.addEventListener('click', () => {
            this.navigateToResult(item);
            this.closeResults();
          });
          
          this.searchResults.appendChild(div);
        });
      }
      
      this.searchResults.classList.add('show');
    }

    navigateToResult(item) {
      // If it belongs to a tab, switch tab first
      if (item.tabId) {
        const btn = document.querySelector(`button.tab[data-tab="${item.tabId}"]`);
        if (btn) btn.click();
      }
      
      // Scroll to element
      if (item.elementId) {
        const el = document.getElementById(item.elementId);
        if (el) {
          setTimeout(() => {
            el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            // Add highlight class briefly
            el.classList.add('highlight-search');
            setTimeout(() => el.classList.remove('highlight-search'), 2000);
          }, 300);
        }
      }
    }

    closeResults() {
      this.searchResults.classList.remove('show');
    }
  }


  // ==========================================
  // 5. VIDEO PLAYER ENHANCEMENT
  // ==========================================
  class VideoManager {
    constructor() {
      this.videoThumbnails = document.querySelectorAll('.video-thumbnail[data-video-id]');
      if (this.videoThumbnails.length > 0) {
        this.init();
      }
    }

    init() {
      Utils.log('Initializing VideoManager');
      
      this.videoThumbnails.forEach(thumb => {
        const videoId = thumb.dataset.videoId;
        if (!videoId) return;

        // Click to load iframe
        thumb.addEventListener('click', () => this.loadVideo(thumb, videoId));
      });
    }

    loadVideo(thumb, videoId) {
      Utils.log(`Loading video: ${videoId}`);
      
      // If already loaded, do nothing
      if (thumb.querySelector('iframe')) return;

      // Pause other videos — reset them back to thumbnails
      this.videoThumbnails.forEach(otherThumb => {
        if (otherThumb !== thumb && otherThumb.querySelector('iframe')) {
          const otherId = otherThumb.dataset.videoId;
          otherThumb.innerHTML = `
            <img src="https://img.youtube.com/vi/${otherId}/hqdefault.jpg" alt="Video thumbnail" loading="lazy">
            <div class="play-button"><i class="fas fa-play"></i></div>
          `;
        }
      });

      // Replace thumbnail with iframe
      thumb.innerHTML = `
        <iframe 
          src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
      `;
    }
  }


  // ==========================================
  // 6. IMAGE GALLERY / LIGHTBOX
  // ==========================================
  class GalleryManager {
    constructor() {
      this.galleryItems = document.querySelectorAll('.gallery-item img');
      if (this.galleryItems.length > 0) {
        this.currentIndex = 0;
        this.init();
      }
    }

    init() {
      Utils.log('Initializing GalleryManager');
      this.createLightbox();

      this.galleryItems.forEach((img, index) => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', () => this.openLightbox(index));
      });
    }

    createLightbox() {
      this.lightbox = document.createElement('div');
      this.lightbox.className = 'lightbox-overlay';
      this.lightbox.innerHTML = `
        <div class="lightbox-content">
          <button class="lightbox-close">&times;</button>
          <button class="lightbox-prev">&#10094;</button>
          <img class="lightbox-img" src="" alt="Gallery Image">
          <div class="lightbox-caption"></div>
          <button class="lightbox-next">&#10095;</button>
        </div>
      `;
      document.body.appendChild(this.lightbox);

      // Event listeners for lightbox
      this.lightbox.querySelector('.lightbox-close').addEventListener('click', () => this.closeLightbox());
      this.lightbox.querySelector('.lightbox-prev').addEventListener('click', (e) => { e.stopPropagation(); this.navigate(-1); });
      this.lightbox.querySelector('.lightbox-next').addEventListener('click', (e) => { e.stopPropagation(); this.navigate(1); });
      this.lightbox.addEventListener('click', (e) => {
        if (e.target === this.lightbox) this.closeLightbox();
      });

      document.addEventListener('keydown', (e) => {
        if (!this.lightbox.classList.contains('active')) return;
        if (e.key === 'Escape') this.closeLightbox();
        if (e.key === 'ArrowLeft') this.navigate(-1);
        if (e.key === 'ArrowRight') this.navigate(1);
      });
    }

    openLightbox(index) {
      this.currentIndex = index;
      this.updateLightboxContent();
      this.lightbox.classList.add('active');
      document.body.style.overflow = 'hidden'; // Prevent scrolling
    }

    closeLightbox() {
      this.lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }

    navigate(direction) {
      this.currentIndex += direction;
      if (this.currentIndex < 0) this.currentIndex = this.galleryItems.length - 1;
      if (this.currentIndex >= this.galleryItems.length) this.currentIndex = 0;
      this.updateLightboxContent();
    }

    updateLightboxContent() {
      const imgEl = this.galleryItems[this.currentIndex];
      const lightboxImg = this.lightbox.querySelector('.lightbox-img');
      const caption = this.lightbox.querySelector('.lightbox-caption');
      
      lightboxImg.src = imgEl.src;
      caption.textContent = imgEl.alt || imgEl.getAttribute('data-caption') || '';
      
      // Preload next image
      const nextIndex = (this.currentIndex + 1) % this.galleryItems.length;
      const preloader = new Image();
      preloader.src = this.galleryItems[nextIndex].src;
    }
  }


  // ==========================================
  // 7. FLASHCARD FLIP
  // ==========================================
  class FlashcardManager {
    constructor() {
      this.flashcards = document.querySelectorAll('.flashcard');
      this.shuffleBtn = document.querySelector('#shuffle-flashcards');
      if (this.flashcards.length > 0) {
        this.init();
      }
    }

    init() {
      Utils.log('Initializing FlashcardManager');
      
      this.flashcards.forEach(card => {
        card.addEventListener('click', () => {
          card.classList.toggle('flipped');
        });
        
        // Keyboard accessibility
        card.setAttribute('tabindex', '0');
        card.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            card.classList.toggle('flipped');
          }
        });
      });

      if (this.shuffleBtn) {
        this.shuffleBtn.addEventListener('click', () => this.shuffleCards());
      }
    }

    shuffleCards() {
      const container = this.flashcards[0].parentNode;
      const cardsArray = Array.from(this.flashcards);
      
      // Fisher-Yates shuffle
      for (let i = cardsArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cardsArray[i], cardsArray[j]] = [cardsArray[j], cardsArray[i]];
      }
      
      // Re-append in new order and unflipp
      cardsArray.forEach(card => {
        card.classList.remove('flipped');
        container.appendChild(card);
      });
    }
  }


  // ==========================================
  // 8. READING PROGRESS
  // ==========================================
  class ProgressManager {
    constructor() {
      // Only initialize on pages that make sense (e.g. chapter reading)
      const contentArea = document.querySelector('.main-content, .notes-content');
      if (contentArea) {
        this.contentArea = contentArea;
        this.init();
      }
    }

    init() {
      Utils.log('Initializing ProgressManager');
      
      // Create progress bar element
      this.progressBar = document.createElement('div');
      this.progressBar.className = 'reading-progress-bar';
      document.body.appendChild(this.progressBar);

      // Listen to scroll events (debounce or requestAnimationFrame for performance)
      window.addEventListener('scroll', () => this.updateProgress(), { passive: true });
      // If content area has its own scrollbar
      if (this.contentArea !== document.body) {
        this.contentArea.addEventListener('scroll', () => this.updateProgress(true), { passive: true });
      }
    }

    updateProgress(isContainer = false) {
      let scrollPos, docHeight, winHeight;

      if (isContainer) {
        scrollPos = this.contentArea.scrollTop;
        docHeight = this.contentArea.scrollHeight;
        winHeight = this.contentArea.clientHeight;
      } else {
        scrollPos = window.scrollY;
        docHeight = document.body.scrollHeight;
        winHeight = window.innerHeight;
      }

      const totalScroll = docHeight - winHeight;
      const percentage = totalScroll > 0 ? (scrollPos / totalScroll) * 100 : 0;
      
      this.progressBar.style.width = `${percentage}%`;
    }
  }


  // ==========================================
  // 9. SMOOTH SCROLL & BACK TO TOP
  // ==========================================
  class ScrollManager {
    constructor() {
      this.backToTopBtn = document.querySelector('.back-to-top');
      this.init();
    }

    init() {
      Utils.log('Initializing ScrollManager');

      // Smooth scroll for internal links
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
          const targetId = this.getAttribute('href');
          if (targetId === '#') return;
          
          const target = document.querySelector(targetId);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({
              behavior: 'smooth'
            });
          }
        });
      });

      // Back to top button logic
      if (this.backToTopBtn) {
        window.addEventListener('scroll', () => {
          if (window.scrollY > CONFIG.SCROLL_THRESHOLD) {
            this.backToTopBtn.classList.add('show');
          } else {
            this.backToTopBtn.classList.remove('show');
          }
        }, { passive: true });

        this.backToTopBtn.addEventListener('click', () => {
          window.scrollTo({
            top: 0,
            behavior: 'smooth'
          });
        });
      }
    }
  }


  // ==========================================
  // 10. PAGE INITIALIZATION
  // ==========================================
  document.addEventListener('DOMContentLoaded', () => {
    Utils.log('DOM fully loaded and parsed. Initializing Pushti Study Hub.');

    // Initialize all managers
    const themeManager = new ThemeManager();
    const tabManager = new TabManager();
    const topicManager = new TopicManager();
    const searchManager = new SearchManager();
    const videoManager = new VideoManager();
    const galleryManager = new GalleryManager();
    const flashcardManager = new FlashcardManager();
    const progressManager = new ProgressManager();
    const scrollManager = new ScrollManager();

    // Mark as loaded
    document.body.classList.add('js-loaded');
  });

})();
