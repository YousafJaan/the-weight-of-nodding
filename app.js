/* ==========================================================================
   The Weight of Nodding - Interactive Web Reader Engine (Expanded Edition)
   Author: Anam Sajjad · BZU Multan · CERN Zenodo DOI: 10.5281/zenodo.24054373
   ========================================================================== */

(function () {
  'use strict';

  // App State
  const STATE = {
    currentIndex: 0,
    theme: localStorage.getItem('won_theme') || 'sepia',
    font: localStorage.getItem('won_font') || 'serif',
    size: localStorage.getItem('won_size') || 'md',
    bookmarkedChapter: parseInt(localStorage.getItem('won_last_chapter') || '0', 10)
  };

  // DOM Elements
  const body = document.body;
  const progressBar = document.getElementById('progress-bar');
  const headerChapterName = document.getElementById('header-chapter-name');
  const chapterPartLabel = document.getElementById('chapter-part-label');
  const chapterMainTitle = document.getElementById('chapter-main-title');
  const chapterReadTime = document.getElementById('chapter-read-time');
  const chapterWordsCount = document.getElementById('chapter-words-count');
  const chapterBody = document.getElementById('chapter-body');

  const menuBtn = document.getElementById('menu-btn');
  const tocDrawer = document.getElementById('toc-drawer');
  const closeDrawerBtn = document.getElementById('close-drawer-btn');
  const tocList = document.getElementById('toc-list');
  const protocolsList = document.getElementById('protocols-list');
  const backdrop = document.getElementById('backdrop');

  const styleSettingsBtn = document.getElementById('style-settings-btn');
  const settingsPopover = document.getElementById('settings-popover');
  const themeBtn = document.getElementById('theme-btn');

  const searchToggleBtn = document.getElementById('search-toggle-btn');
  const searchModal = document.getElementById('search-modal');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const closeSearchBtn = document.getElementById('close-search-btn');

  const aboutBtn = document.getElementById('about-btn');
  const aboutModal = document.getElementById('about-modal');
  const closeAboutBtn = document.getElementById('close-about-btn');

  const prevBtn = document.getElementById('prev-chapter-btn');
  const nextBtn = document.getElementById('next-chapter-btn');
  const prevBtnTitle = document.getElementById('prev-btn-title');
  const nextBtnTitle = document.getElementById('next-btn-title');

  // Verify Book Data
  if (typeof BOOK_DATA === 'undefined' || !Array.isArray(BOOK_DATA) || BOOK_DATA.length === 0) {
    console.error('Book data not loaded.');
    return;
  }

  // Initialize Application
  function init() {
    applyStyles();
    renderTOC();
    renderProtocolsTab();
    setupEventListeners();

    const initialIdx = (STATE.bookmarkedChapter >= 0 && STATE.bookmarkedChapter < BOOK_DATA.length) 
      ? STATE.bookmarkedChapter 
      : 0;

    loadChapter(initialIdx, false);
  }

  // Apply Theme & Font Styles
  function applyStyles() {
    body.setAttribute('data-theme', STATE.theme);
    body.setAttribute('data-font', STATE.font);
    body.setAttribute('data-size', STATE.size);

    document.querySelectorAll('.theme-opt').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-theme-val') === STATE.theme);
    });
    document.querySelectorAll('.size-opt').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-size-val') === STATE.size);
    });
    document.querySelectorAll('.font-opt').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-font-val') === STATE.font);
    });
  }

  // Render Table of Contents List
  function renderTOC() {
    tocList.innerHTML = '';
    BOOK_DATA.forEach((chapter, idx) => {
      const item = document.createElement('a');
      item.className = 'toc-item';
      item.href = `#${chapter.id}`;
      item.setAttribute('data-idx', idx);

      item.innerHTML = `
        <div class="toc-item-part">${chapter.part}</div>
        <div class="toc-item-title">${chapter.title}</div>
        <div class="toc-item-meta">${chapter.readTime} · ${chapter.words ? chapter.words.toLocaleString() : ''} words</div>
      `;

      item.addEventListener('click', (e) => {
        e.preventDefault();
        loadChapter(idx);
        closeDrawer();
      });

      tocList.appendChild(item);
    });
  }

  // Render Protocols Tab
  function renderProtocolsTab() {
    protocolsList.innerHTML = '';
    BOOK_DATA.forEach((chapter, idx) => {
      const item = document.createElement('a');
      item.className = 'toc-item';
      item.href = `#${chapter.id}`;
      item.setAttribute('data-idx', idx);

      item.innerHTML = `
        <div class="toc-item-part">${chapter.part} Strategy</div>
        <div class="toc-item-title">Protocol: ${chapter.title.split('(')[0].trim()}</div>
        <div class="toc-item-meta">Tactical Rules for Daring Women</div>
      `;

      item.addEventListener('click', (e) => {
        e.preventDefault();
        loadChapter(idx);
        closeDrawer();
        setTimeout(() => {
          const marginBox = document.querySelector('.strategist-margin-box');
          if (marginBox) {
            marginBox.scrollIntoView({ behavior: 'smooth' });
          }
        }, 150);
      });

      protocolsList.appendChild(item);
    });
  }

  // Load Chapter by Index
  function loadChapter(index, scroll = true) {
    if (index < 0 || index >= BOOK_DATA.length) return;

    STATE.currentIndex = index;
    localStorage.setItem('won_last_chapter', index);

    const chapter = BOOK_DATA[index];

    // Update DOM
    headerChapterName.textContent = `${chapter.part}: ${chapter.title}`;
    chapterPartLabel.textContent = chapter.part.toUpperCase();
    chapterMainTitle.textContent = chapter.title;
    chapterReadTime.textContent = chapter.readTime;
    if (chapterWordsCount) {
      chapterWordsCount.textContent = `${chapter.words ? chapter.words.toLocaleString() : ''} words`;
    }

    chapterBody.innerHTML = chapter.contentHtml;

    // Update TOC Active State
    document.querySelectorAll('.toc-item').forEach(el => {
      const elIdx = parseInt(el.getAttribute('data-idx'), 10);
      el.classList.toggle('active', elIdx === index);
    });

    // Update Navigation Buttons
    if (index > 0) {
      prevBtn.style.visibility = 'visible';
      prevBtnTitle.textContent = BOOK_DATA[index - 1].part + ': ' + BOOK_DATA[index - 1].title;
    } else {
      prevBtn.style.visibility = 'hidden';
    }

    if (index < BOOK_DATA.length - 1) {
      nextBtn.style.visibility = 'visible';
      nextBtnTitle.textContent = BOOK_DATA[index + 1].part + ': ' + BOOK_DATA[index + 1].title;
    } else {
      nextBtn.style.visibility = 'hidden';
    }

    if (scroll) {
      window.scrollTo({ top: 0, behavior: 'instant' });
    }

    updateProgress();
  }

  // Update Reading Progress Bar
  function updateProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = Math.min(100, Math.max(0, scrollPercent)) + '%';
  }

  // Search Engine
  function performSearch(query) {
    if (!query || query.trim().length < 2) {
      searchResults.innerHTML = '<p class="search-empty">Type at least 2 characters to search across the entire book...</p>';
      return;
    }

    const cleanQuery = query.trim().toLowerCase();
    const matches = [];

    BOOK_DATA.forEach((chapter, chIdx) => {
      // Strip HTML to search plain text
      const tmp = document.createElement('div');
      tmp.innerHTML = chapter.contentHtml;
      const paragraphs = Array.from(tmp.querySelectorAll('p, li, h3, h4'));

      paragraphs.forEach(p => {
        const text = p.textContent;
        const lower = text.toLowerCase();
        const foundPos = lower.indexOf(cleanQuery);
        if (foundPos !== -1) {
          const start = Math.max(0, foundPos - 45);
          const end = Math.min(text.length, foundPos + cleanQuery.length + 55);
          let snippet = text.substring(start, end);
          if (start > 0) snippet = '...' + snippet;
          if (end < text.length) snippet = snippet + '...';

          const regex = new RegExp(`(${cleanQuery})`, 'gi');
          const highlighted = snippet.replace(regex, '<mark>$1</mark>');

          matches.push({
            chIdx: chIdx,
            part: chapter.part,
            title: chapter.title,
            snippet: highlighted
          });
        }
      });
    });

    if (matches.length === 0) {
      searchResults.innerHTML = `<p class="search-empty">No results found for "${query}".</p>`;
      return;
    }

    searchResults.innerHTML = '';
    const limited = matches.slice(0, 30);
    limited.forEach(m => {
      const resItem = document.createElement('div');
      resItem.className = 'search-result-item';
      resItem.innerHTML = `
        <div class="search-res-part">${m.part}</div>
        <div class="search-res-title">${m.title}</div>
        <div class="search-res-snippet">${m.snippet}</div>
      `;
      resItem.addEventListener('click', () => {
        searchModal.classList.add('hidden');
        loadChapter(m.chIdx);
      });
      searchResults.appendChild(resItem);
    });
  }

  // Setup Event Listeners
  function setupEventListeners() {
    window.addEventListener('scroll', updateProgress, { passive: true });

    // Menu Drawer
    menuBtn.addEventListener('click', openDrawer);
    closeDrawerBtn.addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', () => {
      closeDrawer();
      settingsPopover.classList.add('hidden');
      aboutModal.classList.add('hidden');
      searchModal.classList.add('hidden');
      backdrop.classList.remove('active');
    });

    // Drawer Tabs
    document.querySelectorAll('.drawer-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        document.querySelectorAll('.drawer-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const targetTab = tab.getAttribute('data-tab');
        if (targetTab === 'chapters') {
          tocList.classList.remove('hidden');
          protocolsList.classList.add('hidden');
        } else {
          tocList.classList.add('hidden');
          protocolsList.classList.remove('hidden');
        }
      });
    });

    // Settings
    styleSettingsBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      settingsPopover.classList.toggle('hidden');
      if (!settingsPopover.classList.contains('hidden')) {
        backdrop.classList.add('active');
      } else {
        backdrop.classList.remove('active');
      }
    });

    // Theme Options
    document.querySelectorAll('.theme-opt').forEach(btn => {
      btn.addEventListener('click', () => {
        const val = btn.getAttribute('data-theme-val');
        STATE.theme = val;
        localStorage.setItem('won_theme', val);
        applyStyles();
      });
    });

    // Font Options
    document.querySelectorAll('.font-opt').forEach(btn => {
      btn.addEventListener('click', () => {
        const val = btn.getAttribute('data-font-val');
        STATE.font = val;
        localStorage.setItem('won_font', val);
        applyStyles();
      });
    });

    // Size Options
    document.querySelectorAll('.size-opt').forEach(btn => {
      btn.addEventListener('click', () => {
        const val = btn.getAttribute('data-size-val');
        STATE.size = val;
        localStorage.setItem('won_size', val);
        applyStyles();
      });
    });

    // Quick Theme Toggle
    themeBtn.addEventListener('click', () => {
      const themes = ['light', 'sepia', 'dark', 'midnight'];
      const nextTheme = themes[(themes.indexOf(STATE.theme) + 1) % themes.length];
      STATE.theme = nextTheme;
      localStorage.setItem('won_theme', nextTheme);
      applyStyles();
    });

    // Search
    searchToggleBtn.addEventListener('click', () => {
      searchModal.classList.remove('hidden');
      backdrop.classList.add('active');
      searchInput.focus();
    });

    closeSearchBtn.addEventListener('click', () => {
      searchModal.classList.add('hidden');
      backdrop.classList.remove('active');
    });

    searchInput.addEventListener('input', (e) => {
      performSearch(e.target.value);
    });

    // About Modal
    aboutBtn.addEventListener('click', () => {
      aboutModal.classList.remove('hidden');
      backdrop.classList.add('active');
    });

    closeAboutBtn.addEventListener('click', () => {
      aboutModal.classList.add('hidden');
      backdrop.classList.remove('active');
    });

    // Chapter Navigation
    prevBtn.addEventListener('click', () => {
      if (STATE.currentIndex > 0) loadChapter(STATE.currentIndex - 1);
    });

    nextBtn.addEventListener('click', () => {
      if (STATE.currentIndex < BOOK_DATA.length - 1) loadChapter(STATE.currentIndex + 1);
    });

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT') return;
      if (e.key === 'ArrowLeft') {
        if (STATE.currentIndex > 0) loadChapter(STATE.currentIndex - 1);
      } else if (e.key === 'ArrowRight') {
        if (STATE.currentIndex < BOOK_DATA.length - 1) loadChapter(STATE.currentIndex + 1);
      } else if (e.key === 'Escape') {
        closeDrawer();
        settingsPopover.classList.add('hidden');
        aboutModal.classList.add('hidden');
        searchModal.classList.add('hidden');
        backdrop.classList.remove('active');
      }
    });
  }

  function openDrawer() {
    tocDrawer.classList.add('open');
    backdrop.classList.add('active');
  }

  function closeDrawer() {
    tocDrawer.classList.remove('open');
    backdrop.classList.remove('active');
  }

  // Start Engine on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
