/**
 * Anglotec AI Academy - IELTS Band Calculator Widget
 * Embeddable widget for calculating IELTS overall band scores
 * 
 * Embed code:
 * <script src="https://tools.anglotec-ai.com/widgets/ielts-calculator-widget.js" data-container="ielts-widget"></script>
 * <div id="ielts-widget"></div>
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
    containerMinWidth: '320px',
    maxWidth: '420px',
    logoText: 'ANGLOTEC',
    logoSubtext: 'AI ACADEMY',
    baseUrl: 'https://tools.anglotec-ai.com',
    utmParams: '?utm_source=widget&utm_medium=embed&utm_campaign=ielts-calculator'
  };

  // CEFR mapping
  function getCEFR(overall) {
    if (overall < 2) return { level: 'A1', label: 'Beginner', color: '#6B8F71' };
    if (overall < 3.5) return { level: 'A2', label: 'Elementary', color: '#5A9A6E' };
    if (overall < 5) return { level: 'B1', label: 'Intermediate', color: '#4A9F6C' };
    if (overall < 6.5) return { level: 'B2', label: 'Upper-Intermediate', color: '#3A8A5C' };
    if (overall < 7.5) return { level: 'C1', label: 'Advanced', color: CONFIG.brandOrange };
    return { level: 'C2', label: 'Proficiency', color: CONFIG.brandOrange };
  }

  // Study tips based on score
  function getStudyTip(overall) {
    if (overall < 4) return 'Focus on building foundational grammar and vocabulary. Try daily reading practice with simple articles.';
    if (overall < 5.5) return 'Work on expanding your vocabulary and practice speaking about familiar topics regularly.';
    if (overall < 6.5) return 'Strengthen your Writing Task 2 structure and practice Listening with timed exercises.';
    if (overall < 7.5) return 'Refine your academic vocabulary and practice complex grammar structures in Writing.';
    return 'Maintain your level with regular practice. Focus on precision and sophistication in all modules.';
  }

  // Calculate overall band (average rounded to nearest 0.5)
  function calculateOverall(listening, reading, writing, speaking) {
    const average = (parseFloat(listening) + parseFloat(reading) + parseFloat(writing) + parseFloat(speaking)) / 4;
    return Math.round(average * 2) / 2;
  }

  // Get container ID from script data attribute
  function getContainerId() {
    const scripts = document.querySelectorAll('script[src*="ielts-calculator-widget"]');
    for (const script of scripts) {
      const containerId = script.getAttribute('data-container');
      if (containerId) return containerId;
    }
    return 'ielts-widget';
  }

  // Widget HTML template
  function getTemplate() {
    return `
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }
        
        .aw-widget-container {
          font-family: ${CONFIG.fontFamily};
          background: ${CONFIG.white};
          border-radius: 16px;
          box-shadow: 0 4px 24px rgba(44, 74, 62, 0.12), 0 1px 4px rgba(0,0,0,0.06);
          overflow: hidden;
          min-width: ${CONFIG.containerMinWidth};
          max-width: ${CONFIG.maxWidth};
          margin: 0 auto;
          border: 1px solid ${CONFIG.lightGray};
        }
        
        .aw-header {
          background: ${CONFIG.brandGreen};
          padding: 20px 24px 16px;
          text-align: center;
          position: relative;
        }
        
        .aw-logo {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          margin-bottom: 4px;
        }
        
        .aw-logo-icon {
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
        
        .aw-logo-text {
          color: ${CONFIG.white};
          font-size: 18px;
          font-weight: 800;
          letter-spacing: 2px;
        }
        
        .aw-logo-sub {
          color: rgba(255,255,255,0.7);
          font-size: 9px;
          font-weight: 600;
          letter-spacing: 3px;
          text-transform: uppercase;
          margin-bottom: 12px;
        }
        
        .aw-header h2 {
          color: ${CONFIG.white};
          font-size: 15px;
          font-weight: 600;
          opacity: 0.95;
        }
        
        .aw-body {
          padding: 20px 24px;
        }
        
        .aw-slider-group {
          margin-bottom: 16px;
        }
        
        .aw-slider-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 6px;
        }
        
        .aw-slider-label {
          font-size: 13px;
          font-weight: 600;
          color: ${CONFIG.darkText};
          display: flex;
          align-items: center;
          gap: 6px;
        }
        
        .aw-slider-icon {
          font-size: 14px;
        }
        
        .aw-slider-value {
          font-size: 16px;
          font-weight: 700;
          color: ${CONFIG.brandGreen};
          background: rgba(44, 74, 62, 0.08);
          padding: 2px 10px;
          border-radius: 20px;
          min-width: 36px;
          text-align: center;
        }
        
        .aw-slider {
          width: 100%;
          height: 6px;
          border-radius: 3px;
          outline: none;
          -webkit-appearance: none;
          appearance: none;
          background: linear-gradient(to right, ${CONFIG.brandGreen} var(--progress, 0%), ${CONFIG.lightGray} var(--progress, 0%));
          cursor: pointer;
        }
        
        .aw-slider::-webkit-slider-thumb {
          -webkit-appearance: none;
          appearance: none;
          width: 20px;
          height: 20px;
          border-radius: 50%;
          background: ${CONFIG.brandOrange};
          cursor: pointer;
          border: 3px solid ${CONFIG.white};
          box-shadow: 0 2px 6px rgba(212, 101, 59, 0.35);
          transition: transform 0.15s ease;
        }
        
        .aw-slider::-webkit-slider-thumb:hover {
          transform: scale(1.15);
        }
        
        .aw-slider::-moz-range-thumb {
          width: 20px;
          height: 20px;
          border-radius: 50%;
          background: ${CONFIG.brandOrange};
          cursor: pointer;
          border: 3px solid ${CONFIG.white};
          box-shadow: 0 2px 6px rgba(212, 101, 59, 0.35);
        }
        
        .aw-result-section {
          background: ${CONFIG.brandCream};
          border-radius: 12px;
          padding: 16px 20px;
          margin-top: 20px;
          text-align: center;
        }
        
        .aw-overall-label {
          font-size: 11px;
          font-weight: 700;
          color: ${CONFIG.midGray};
          text-transform: uppercase;
          letter-spacing: 1.5px;
          margin-bottom: 4px;
        }
        
        .aw-overall-score {
          font-size: 42px;
          font-weight: 800;
          color: ${CONFIG.brandGreen};
          line-height: 1.1;
          margin-bottom: 8px;
        }
        
        .aw-cefr-badge {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          background: ${CONFIG.white};
          padding: 5px 14px;
          border-radius: 20px;
          margin-bottom: 10px;
        }
        
        .aw-cefr-level {
          font-size: 14px;
          font-weight: 700;
        }
        
        .aw-cefr-label {
          font-size: 11px;
          color: ${CONFIG.midGray};
          font-weight: 500;
        }
        
        .aw-divider {
          width: 30px;
          height: 2px;
          background: ${CONFIG.lightGray};
          margin: 10px auto;
          border-radius: 1px;
        }
        
        .aw-tip-section {
          text-align: left;
        }
        
        .aw-tip-label {
          font-size: 10px;
          font-weight: 700;
          color: ${CONFIG.brandOrange};
          text-transform: uppercase;
          letter-spacing: 1px;
          margin-bottom: 4px;
        }
        
        .aw-tip-text {
          font-size: 12px;
          color: ${CONFIG.darkText};
          line-height: 1.55;
          font-weight: 400;
        }
        
        .aw-footer {
          padding: 14px 24px;
          background: ${CONFIG.brandCream};
          border-top: 1px solid ${CONFIG.lightGray};
          text-align: center;
        }
        
        .aw-footer a {
          color: ${CONFIG.brandGreen};
          text-decoration: none;
          font-size: 11px;
          font-weight: 600;
          transition: color 0.2s ease;
        }
        
        .aw-footer a:hover {
          color: ${CONFIG.brandOrange};
        }
        
        .aw-footer-text {
          font-size: 10px;
          color: ${CONFIG.midGray};
          margin-top: 4px;
        }
        
        .aw-scale-hint {
          display: flex;
          justify-content: space-between;
          padding: 0 2px;
          margin-top: 2px;
        }
        
        .aw-scale-hint span {
          font-size: 9px;
          color: ${CONFIG.midGray};
        }

        @media (max-width: 360px) {
          .aw-body {
            padding: 16px 18px;
          }
          .aw-overall-score {
            font-size: 36px;
          }
        }
      </style>
      
      <div class="aw-widget-container">
        <div class="aw-header">
          <div class="aw-logo">
            <div class="aw-logo-icon">A</div>
            <div>
              <div class="aw-logo-text">${CONFIG.logoText}</div>
              <div class="aw-logo-sub">${CONFIG.logoSubtext}</div>
            </div>
          </div>
          <h2>IELTS Band Score Calculator</h2>
        </div>
        
        <div class="aw-body">
          <div class="aw-slider-group">
            <div class="aw-slider-header">
              <span class="aw-slider-label">
                <span class="aw-slider-icon">🎧</span> Listening
              </span>
              <span class="aw-slider-value" id="aw-val-listening">7.0</span>
            </div>
            <input type="range" class="aw-slider" id="aw-slider-listening" min="0" max="9" step="0.5" value="7">
            <div class="aw-scale-hint"><span>0</span><span>9</span></div>
          </div>
          
          <div class="aw-slider-group">
            <div class="aw-slider-header">
              <span class="aw-slider-label">
                <span class="aw-slider-icon">📖</span> Reading
              </span>
              <span class="aw-slider-value" id="aw-val-reading">7.0</span>
            </div>
            <input type="range" class="aw-slider" id="aw-slider-reading" min="0" max="9" step="0.5" value="7">
            <div class="aw-scale-hint"><span>0</span><span>9</span></div>
          </div>
          
          <div class="aw-slider-group">
            <div class="aw-slider-header">
              <span class="aw-slider-label">
                <span class="aw-slider-icon">✍️</span> Writing
              </span>
              <span class="aw-slider-value" id="aw-val-writing">7.0</span>
            </div>
            <input type="range" class="aw-slider" id="aw-slider-writing" min="0" max="9" step="0.5" value="7">
            <div class="aw-scale-hint"><span>0</span><span>9</span></div>
          </div>
          
          <div class="aw-slider-group">
            <div class="aw-slider-header">
              <span class="aw-slider-label">
                <span class="aw-slider-icon">🗣️</span> Speaking
              </span>
              <span class="aw-slider-value" id="aw-val-speaking">7.0</span>
            </div>
            <input type="range" class="aw-slider" id="aw-slider-speaking" min="0" max="9" step="0.5" value="7">
            <div class="aw-scale-hint"><span>0</span><span>9</span></div>
          </div>
          
          <div class="aw-result-section">
            <div class="aw-overall-label">Overall Band Score</div>
            <div class="aw-overall-score" id="aw-overall">7.0</div>
            <div class="aw-cefr-badge">
              <span class="aw-cefr-level" id="aw-cefr-level">C1</span>
              <span class="aw-cefr-label" id="aw-cefr-label">Advanced</span>
            </div>
            <div class="aw-divider"></div>
            <div class="aw-tip-section">
              <div class="aw-tip-label">💡 Study Tip</div>
              <div class="aw-tip-text" id="aw-tip">Maintain your level with regular practice. Focus on precision and sophistication in all modules.</div>
            </div>
          </div>
        </div>
        
        <div class="aw-footer">
          <a href="${CONFIG.baseUrl}${CONFIG.utmParams}" target="_blank" rel="noopener">Powered by Anglotec AI Academy →</a>
          <div class="aw-footer-text">Free IELTS preparation tools</div>
        </div>
      </div>
    `;
  }

  // Initialize the widget
  function init() {
    const containerId = getContainerId();
    const container = document.getElementById(containerId);
    if (!container) {
      console.warn('[Anglotec IELTS Widget] Container #' + containerId + ' not found');
      return;
    }

    // Create shadow root for style isolation
    const shadow = container.attachShadow({ mode: 'open' });
    shadow.innerHTML = getTemplate();

    // Cache DOM references from shadow root
    const sliderListening = shadow.getElementById('aw-slider-listening');
    const sliderReading = shadow.getElementById('aw-slider-reading');
    const sliderWriting = shadow.getElementById('aw-slider-writing');
    const sliderSpeaking = shadow.getElementById('aw-slider-speaking');
    const valListening = shadow.getElementById('aw-val-listening');
    const valReading = shadow.getElementById('aw-val-reading');
    const valWriting = shadow.getElementById('aw-val-writing');
    const valSpeaking = shadow.getElementById('aw-val-speaking');
    const overallEl = shadow.getElementById('aw-overall');
    const cefrLevelEl = shadow.getElementById('aw-cefr-level');
    const cefrLabelEl = shadow.getElementById('aw-cefr-label');
    const tipEl = shadow.getElementById('aw-tip');

    // Update slider progress visual
    function updateSliderProgress(slider) {
      const percent = ((slider.value - slider.min) / (slider.max - slider.min)) * 100;
      slider.style.setProperty('--progress', percent + '%');
    }

    // Format band value
    function formatBand(val) {
      return parseFloat(val).toFixed(1);
    }

    // Main update function
    function update() {
      const l = sliderListening.value;
      const r = sliderReading.value;
      const w = sliderWriting.value;
      const s = sliderSpeaking.value;

      valListening.textContent = formatBand(l);
      valReading.textContent = formatBand(r);
      valWriting.textContent = formatBand(w);
      valSpeaking.textContent = formatBand(s);

      updateSliderProgress(sliderListening);
      updateSliderProgress(sliderReading);
      updateSliderProgress(sliderWriting);
      updateSliderProgress(sliderSpeaking);

      const overall = calculateOverall(l, r, w, s);
      const cefr = getCEFR(overall);
      const tip = getStudyTip(overall);

      overallEl.textContent = formatBand(overall);
      overallEl.style.color = cefr.color;
      cefrLevelEl.textContent = cefr.level;
      cefrLevelEl.style.color = cefr.color;
      cefrLabelEl.textContent = cefr.label;
      tipEl.textContent = tip;
    }

    // Attach listeners
    [sliderListening, sliderReading, sliderWriting, sliderSpeaking].forEach(function(slider) {
      slider.addEventListener('input', update);
    });

    // Initial render
    update();
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
