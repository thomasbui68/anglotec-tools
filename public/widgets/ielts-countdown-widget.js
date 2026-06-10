/**
 * Anglotec AI Academy - IELTS Countdown Timer Widget
 * Embeddable countdown timer for IELTS test dates
 * 
 * Embed code:
 * <script src="https://tools.anglotec-ai.com/widgets/ielts-countdown-widget.js" data-container="countdown-widget" data-test-date="2025-08-15"></script>
 * <div id="countdown-widget"></div>
 */
(function() {
  'use strict';

  // Configuration
  const CONFIG = {
    brandGreen: '#2C4A3E',
    brandOrange: '#D4653B',
    brandCream: '#F7F5F2',
    white: '#FFFFFF',
    darkText: '#1A1A1A',
    lightGray: '#E8E6E3',
    midGray: '#8A8680',
    fontFamily: '"Inter", "Segoe UI", system-ui, -apple-system, sans-serif',
    containerMinWidth: '300px',
    maxWidth: '440px',
    baseUrl: 'https://agmp.anglotec.com',
    utmParams: '?utm_source=widget&utm_medium=embed&utm_campaign=ielts-countdown'
  };

  // Study milestones based on days remaining
  function getMilestone(days) {
    if (days <= 0) return { message: '🎉 Good Luck on your IELTS test!', sub: 'You\'ve got this!', type: 'success' };
    if (days === 1) return { message: '⏰ Tomorrow is the big day!', sub: 'Get plenty of rest and trust your preparation.', type: 'urgent' };
    if (days <= 3) return { message: '🔥 Final countdown — stay focused!', sub: 'Review your notes and do light practice only.', type: 'urgent' };
    if (days <= 7) return { message: '📚 Last week — prioritize weak areas!', sub: 'Do 1-2 full mock tests and review mistakes.', type: 'warning' };
    if (days <= 14) return { message: '✍️ Two weeks left — Writing & Speaking focus!', sub: 'Get feedback on your essays and do mock speaking tests.', type: 'warning' };
    if (days <= 30) return { message: '🎯 One month left — simulate test conditions!', sub: 'Take full-length practice tests under timed conditions.', type: 'info' };
    if (days <= 60) return { message: '📖 Build vocabulary & grammar foundations', sub: 'Read academic articles daily and note new collocations.', type: 'info' };
    if (days <= 90) return { message: '🌱 Early prep — explore all modules evenly', sub: 'Get familiar with all 4 sections of the IELTS format.', type: 'info' };
    return { message: '🚀 Great start — plan your study schedule!', sub: 'Set weekly goals and track your progress consistently.', type: 'info' };
  }

  // Get test date from script data attribute
  function getTestDate() {
    const scripts = document.querySelectorAll('script[src*="ielts-countdown-widget"]');
    for (const script of scripts) {
      const dateStr = script.getAttribute('data-test-date');
      if (dateStr) {
        const parsed = new Date(dateStr + 'T00:00:00');
        if (!isNaN(parsed.getTime())) return parsed;
      }
    }
    // Default: 30 days from now
    const d = new Date();
    d.setDate(d.getDate() + 30);
    return d;
  }

  // Get container ID
  function getContainerId() {
    const scripts = document.querySelectorAll('script[src*="ielts-countdown-widget"]');
    for (const script of scripts) {
      const containerId = script.getAttribute('data-container');
      if (containerId) return containerId;
    }
    return 'countdown-widget';
  }

  // Format test date
  function formatTestDate(date) {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
  }

  // Widget HTML template
  function getTemplate() {
    return `
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        .cw-widget-container {
          font-family: ${CONFIG.fontFamily};
          background: ${CONFIG.white};
          border-radius: 16px;
          box-shadow: 0 4px 24px rgba(44, 74, 62, 0.10), 0 1px 4px rgba(0,0,0,0.05);
          overflow: hidden;
          min-width: ${CONFIG.containerMinWidth};
          max-width: ${CONFIG.maxWidth};
          margin: 0 auto;
          border: 1px solid ${CONFIG.lightGray};
        }
        
        .cw-header {
          background: ${CONFIG.brandGreen};
          padding: 20px 24px;
          text-align: center;
          position: relative;
        }
        
        .cw-logo {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          margin-bottom: 12px;
        }
        
        .cw-logo-icon {
          width: 28px;
          height: 28px;
          background: ${CONFIG.brandOrange};
          border-radius: 6px;
          display: flex;
          align-items: center;
          justify-content: center;
          font-weight: 800;
          font-size: 12px;
          color: ${CONFIG.white};
          letter-spacing: 0.5px;
        }
        
        .cw-logo-text {
          color: ${CONFIG.white};
          font-size: 17px;
          font-weight: 800;
          letter-spacing: 2px;
        }
        
        .cw-header h2 {
          color: ${CONFIG.white};
          font-size: 15px;
          font-weight: 600;
          opacity: 0.95;
        }
        
        .cw-test-date {
          color: rgba(255,255,255,0.8);
          font-size: 12px;
          margin-top: 6px;
          font-weight: 500;
        }
        
        .cw-body {
          padding: 24px;
        }
        
        .cw-countdown-grid {
          display: grid;
          grid-template-columns: repeat(4, 1fr);
          gap: 10px;
          margin-bottom: 22px;
        }
        
        .cw-countdown-item {
          background: ${CONFIG.brandGreen};
          border-radius: 12px;
          padding: 14px 6px;
          text-align: center;
          position: relative;
          overflow: hidden;
        }
        
        .cw-countdown-item::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          height: 3px;
          background: ${CONFIG.brandOrange};
        }
        
        .cw-countdown-number {
          font-size: 28px;
          font-weight: 800;
          color: ${CONFIG.white};
          line-height: 1.1;
          display: block;
        }
        
        .cw-countdown-label {
          font-size: 10px;
          font-weight: 600;
          color: rgba(255,255,255,0.75);
          text-transform: uppercase;
          letter-spacing: 1px;
          margin-top: 4px;
          display: block;
        }
        
        .cw-milestone {
          background: ${CONFIG.brandCream};
          border-radius: 12px;
          padding: 16px 18px;
          border-left: 4px solid ${CONFIG.brandOrange};
          margin-bottom: 18px;
        }
        
        .cw-milestone.success {
          border-left-color: #4CAF50;
          background: #E8F5E9;
        }
        
        .cw-milestone.urgent {
          border-left-color: #D32F2F;
          background: #FFEBEE;
        }
        
        .cw-milestone.warning {
          border-left-color: #F57C00;
          background: #FFF3E0;
        }
        
        .cw-milestone.info {
          border-left-color: ${CONFIG.brandGreen};
        }
        
        .cw-milestone-message {
          font-size: 13px;
          font-weight: 700;
          color: ${CONFIG.darkText};
          margin-bottom: 4px;
          line-height: 1.4;
        }
        
        .cw-milestone-sub {
          font-size: 11px;
          color: ${CONFIG.midGray};
          line-height: 1.5;
        }
        
        .cw-progress-section {
          margin-bottom: 4px;
        }
        
        .cw-progress-label {
          display: flex;
          justify-content: space-between;
          font-size: 11px;
          color: ${CONFIG.midGray};
          margin-bottom: 6px;
          font-weight: 500;
        }
        
        .cw-progress-bar {
          height: 8px;
          background: ${CONFIG.lightGray};
          border-radius: 4px;
          overflow: hidden;
        }
        
        .cw-progress-fill {
          height: 100%;
          background: linear-gradient(to right, ${CONFIG.brandGreen}, ${CONFIG.brandOrange});
          border-radius: 4px;
          transition: width 0.5s ease;
        }
        
        .cw-footer {
          padding: 14px 24px;
          background: ${CONFIG.brandCream};
          border-top: 1px solid ${CONFIG.lightGray};
          text-align: center;
        }
        
        .cw-footer a {
          color: ${CONFIG.brandGreen};
          text-decoration: none;
          font-size: 11px;
          font-weight: 600;
          transition: color 0.2s ease;
        }
        
        .cw-footer a:hover {
          color: ${CONFIG.brandOrange};
        }
        
        .cw-footer-text {
          font-size: 10px;
          color: ${CONFIG.midGray};
          margin-top: 4px;
        }

        .cw-expired {
          text-align: center;
          padding: 10px 0;
        }
        
        .cw-expired-icon {
          font-size: 48px;
          margin-bottom: 8px;
        }
        
        .cw-expired h3 {
          font-size: 20px;
          color: ${CONFIG.brandGreen};
          margin-bottom: 4px;
        }
        
        .cw-expired p {
          font-size: 13px;
          color: ${CONFIG.midGray};
        }

        @media (max-width: 360px) {
          .cw-countdown-number { font-size: 22px; }
          .cw-countdown-item { padding: 12px 4px; }
          .cw-body { padding: 18px 16px; }
        }
      </style>
      
      <div class="cw-widget-container">
        <div class="cw-header">
          <div class="cw-logo">
            <div class="cw-logo-icon">A</div>
            <div class="cw-logo-text">ANGLOTEC</div>
          </div>
          <h2>IELTS Test Countdown</h2>
          <div class="cw-test-date" id="cw-test-date">Test Date: August 15, 2025</div>
        </div>
        
        <div class="cw-body">
          <div class="cw-countdown-grid" id="cw-countdown-grid">
            <div class="cw-countdown-item">
              <span class="cw-countdown-number" id="cw-days">30</span>
              <span class="cw-countdown-label">Days</span>
            </div>
            <div class="cw-countdown-item">
              <span class="cw-countdown-number" id="cw-hours">00</span>
              <span class="cw-countdown-label">Hours</span>
            </div>
            <div class="cw-countdown-item">
              <span class="cw-countdown-number" id="cw-minutes">00</span>
              <span class="cw-countdown-label">Mins</span>
            </div>
            <div class="cw-countdown-item">
              <span class="cw-countdown-number" id="cw-seconds">00</span>
              <span class="cw-countdown-label">Secs</span>
            </div>
          </div>
          
          <div class="cw-progress-section" id="cw-progress-section">
            <div class="cw-progress-label">
              <span>Study Progress</span>
              <span id="cw-progress-text">Day 1 of 30</span>
            </div>
            <div class="cw-progress-bar">
              <div class="cw-progress-fill" id="cw-progress-fill" style="width: 3%"></div>
            </div>
          </div>
          
          <div class="cw-milestone" id="cw-milestone">
            <div class="cw-milestone-message" id="cw-milestone-msg">🎯 One month left — simulate test conditions!</div>
            <div class="cw-milestone-sub" id="cw-milestone-sub">Take full-length practice tests under timed conditions.</div>
          </div>
        </div>
        
        <div class="cw-footer">
          <a href="${CONFIG.baseUrl}${CONFIG.utmParams}" target="_blank" rel="noopener">Practice with IELTS Mock Tests →</a>
          <div class="cw-footer-text">Powered by Anglotec AI Academy</div>
        </div>
      </div>
    `;
  }

  function init() {
    const containerId = getContainerId();
    const container = document.getElementById(containerId);
    if (!container) {
      console.warn('[Anglotec Countdown Widget] Container #' + containerId + ' not found');
      return;
    }

    const shadow = container.attachShadow({ mode: 'open' });
    shadow.innerHTML = getTemplate();

    const testDate = getTestDate();
    const testDateEl = shadow.getElementById('cw-test-date');
    const daysEl = shadow.getElementById('cw-days');
    const hoursEl = shadow.getElementById('cw-hours');
    const minsEl = shadow.getElementById('cw-minutes');
    const secsEl = shadow.getElementById('cw-seconds');
    const milestoneEl = shadow.getElementById('cw-milestone');
    const milestoneMsgEl = shadow.getElementById('cw-milestone-msg');
    const milestoneSubEl = shadow.getElementById('cw-milestone-sub');
    const progressTextEl = shadow.getElementById('cw-progress-text');
    const progressFillEl = shadow.getElementById('cw-progress-fill');
    const progressSection = shadow.getElementById('cw-progress-section');

    testDateEl.textContent = '📅 ' + formatTestDate(testDate);

    // Calculate total days for progress bar
    const nowForTotal = new Date();
    const totalDays = Math.max(1, Math.ceil((testDate - nowForTotal) / (1000 * 60 * 60 * 24)));

    function update() {
      const now = new Date();
      const diff = testDate - now;

      if (diff <= 0) {
        // Test has passed
        daysEl.textContent = '00';
        hoursEl.textContent = '00';
        minsEl.textContent = '00';
        secsEl.textContent = '00';
        
        const milestone = getMilestone(0);
        milestoneEl.className = 'cw-milestone ' + milestone.type;
        milestoneMsgEl.textContent = milestone.message;
        milestoneSubEl.textContent = milestone.sub;
        progressSection.style.display = 'none';
        return;
      }

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((diff % (1000 * 60)) / 1000);

      daysEl.textContent = String(days).padStart(2, '0');
      hoursEl.textContent = String(hours).padStart(2, '0');
      minsEl.textContent = String(minutes).padStart(2, '0');
      secsEl.textContent = String(seconds).padStart(2, '0');

      // Update milestone
      const milestone = getMilestone(days);
      milestoneEl.className = 'cw-milestone ' + milestone.type;
      milestoneMsgEl.textContent = milestone.message;
      milestoneSubEl.textContent = milestone.sub;

      // Update progress
      const elapsedDays = Math.max(0, totalDays - days);
      const progressPct = Math.min(100, Math.max(0, (elapsedDays / totalDays) * 100));
      progressFillEl.style.width = progressPct + '%';
      progressTextEl.textContent = 'Day ' + elapsedDays + ' of ' + totalDays;
    }

    update();
    const interval = setInterval(update, 1000);

    // Cleanup on page hide to save resources
    document.addEventListener('visibilitychange', function() {
      if (document.hidden) {
        clearInterval(interval);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
