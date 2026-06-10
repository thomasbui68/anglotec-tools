/**
 * Anglotec AI Academy - Medical English Word of the Day Widget
 * Embeddable widget for daily medical English vocabulary
 * 
 * Embed code:
 * <script src="https://tools.anglotec-ai.com/widgets/medical-word-widget.js" data-container="medword-widget"></script>
 * <div id="medword-widget"></div>
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
    medicalGreen: '#E8F5E9',
    medicalGreenDark: '#388E3C',
    fontFamily: '"Inter", "Segoe UI", system-ui, -apple-system, sans-serif',
    containerMinWidth: '280px',
    maxWidth: '400px',
    baseUrl: 'https://amc.anglotec-ai.com',
    utmParams: '?utm_source=widget&utm_medium=embed&utm_campaign=medical-word'
  };

  // 50 Medical English words
  const WORDS = [
    { word: 'auscultation', pronunciation: '/ˌɔːskəlˈteɪʃən/', definition: 'The act of listening to sounds within the body using a stethoscope.', example: 'The doctor performed auscultation to check for abnormal heart sounds.' },
    { word: 'bradycardia', pronunciation: '/ˌbrædɪˈkɑːrdiə/', definition: 'An abnormally slow heart rate, typically fewer than 60 beats per minute.', example: 'The patient presented with bradycardia during the routine check-up.' },
    { word: 'cholecystectomy', pronunciation: '/ˌkoʊləsɪsˈtektəmi/', definition: 'Surgical removal of the gallbladder.', example: 'She underwent a laparoscopic cholecystectomy to treat gallstones.' },
    { word: 'dyspnea', pronunciation: '/dɪspˈniːə/', definition: 'Difficult or labored breathing; shortness of breath.', example: 'The patient reported dyspnea upon mild exertion.' },
    { word: 'echocardiogram', pronunciation: '/ˌekoʊˈkɑːrdiəɡræm/', definition: 'An ultrasound test that uses sound waves to produce images of the heart.', example: 'The echocardiogram revealed mild mitral valve regurgitation.' },
    { word: 'febrile', pronunciation: '/ˈfiːbraɪl/', definition: 'Having or showing symptoms of a fever.', example: 'The febrile infant was admitted for further investigation.' },
    { word: 'gastroenteritis', pronunciation: '/ˌɡæstroʊˌentəˈraɪtɪs/', definition: 'Inflammation of the stomach and intestines, typically from infection.', example: 'Viral gastroenteritis is the most common cause of diarrhea in children.' },
    { word: 'hematoma', pronunciation: '/ˌhiːməˈtoʊmə/', definition: 'A localized collection of blood outside the blood vessels, usually in liquid form.', example: 'A subdural hematoma was identified on the CT scan.' },
    { word: 'idiopathic', pronunciation: '/ˌɪdiəˈpæθɪk/', definition: 'Relating to any disease or condition that arises spontaneously or for which the cause is unknown.', example: 'The patient was diagnosed with idiopathic pulmonary fibrosis.' },
    { word: 'jaundice', pronunciation: '/ˈdʒɔːndɪs/', definition: 'A yellow discoloration of the skin and eyes caused by excess bilirubin.', example: 'Newborn jaundice typically appears within the first week of life.' },
    { word: 'kyphosis', pronunciation: '/kaɪˈfoʊsɪs/', definition: 'An excessive outward curvature of the spine, causing hunching of the back.', example: 'Severe kyphosis can cause pain and breathing difficulties.' },
    { word: 'leukocytosis', pronunciation: '/ˌluːkəsaɪˈtoʊsɪs/', definition: 'An increase in the number of white cells in the blood, especially during infection.', example: 'Leukocytosis is a common finding in bacterial infections.' },
    { word: 'myocardial', pronunciation: '/ˌmaɪoʊˈkɑːrdiəl/', definition: 'Relating to the muscular tissue of the heart.', example: 'The patient suffered an acute myocardial infarction.' },
    { word: 'nephrology', pronunciation: '/neˈfrɑːlədʒi/', definition: 'The branch of medicine that deals with the physiology and diseases of the kidneys.', example: 'He was referred to the nephrology department for chronic kidney disease.' },
    { word: 'osteoporosis', pronunciation: '/ˌɑːstioʊpəˈroʊsɪs/', definition: 'A bone disease that occurs when the body loses too much bone or makes too little.', example: 'Postmenopausal women are at increased risk of osteoporosis.' },
    { word: 'palliative', pronunciation: '/ˈpæliˌeɪtɪv/', definition: 'Relieving symptoms without dealing with the underlying cause of a condition.', example: 'The patient was transferred to palliative care to manage pain.' },
    { word: 'quadriplegia', pronunciation: '/ˌkwɑːdrəˈpliːdʒə/', definition: 'Paralysis of all four limbs; also known as tetraplegia.', example: 'High cervical spine injuries can result in quadriplegia.' },
    { word: 'remission', pronunciation: '/rɪˈmɪʃən/', definition: 'A period during which symptoms of disease are reduced or disappear.', example: 'The cancer has been in remission for over two years.' },
    { word: 'sepsis', pronunciation: '/ˈsepsɪs/', definition: 'A life-threatening condition caused by the body\'s response to an infection.', example: 'Early recognition and treatment of sepsis significantly improve survival rates.' },
    { word: 'tachycardia', pronunciation: '/ˌtækɪˈkɑːrdiə/', definition: 'A heart rate that exceeds the normal resting rate, generally over 100 bpm.', example: 'The patient developed tachycardia following the administration of the medication.' },
    { word: 'ulcer', pronunciation: '/ˈʌlsər/', definition: 'An open sore on an external or internal surface of the body.', example: 'Peptic ulcer disease is commonly associated with H. pylori infection.' },
    { word: 'vasoconstriction', pronunciation: '/ˌveɪzoʊkənˈstrɪkʃən/', definition: 'The constriction of blood vessels, which increases blood pressure.', example: 'Cold temperatures cause vasoconstriction in peripheral blood vessels.' },
    { word: 'wheezing', pronunciation: '/ˈwiːzɪŋ/', definition: 'Breathing with a whistling or rattling sound in the chest.', example: 'The child presented with wheezing and respiratory distress.' },
    { word: 'xerostomia', pronunciation: '/ˌzɪroʊˈstoʊmiə/', definition: 'Dryness of the mouth caused by reduction or absence of saliva flow.', example: 'Many medications list xerostomia as a common side effect.' },
    { word: 'cyanosis', pronunciation: '/ˌsaɪəˈnoʊsɪs/', definition: 'A bluish discoloration of the skin resulting from poor circulation or inadequate oxygenation.', example: 'Central cyanosis may indicate serious cardiac or respiratory disease.' },
    { word: 'edema', pronunciation: '/ɪˈdiːmə/', definition: 'Swelling caused by excess fluid trapped in the body\'s tissues.', example: 'Bilateral ankle edema was noted during the physical examination.' },
    { word: 'fistula', pronunciation: '/ˈfɪstʃʊlə/', definition: 'An abnormal connection between two hollow spaces or vessels.', example: 'An arteriovenous fistula was created for hemodialysis access.' },
    { word: 'granuloma', pronunciation: '/ˌɡrænjuˈloʊmə/', definition: 'A mass of granulation tissue, typically produced in response to infection or inflammation.', example: 'The biopsy revealed non-caseating granulomas suggestive of sarcoidosis.' },
    { word: 'hypertension', pronunciation: '/ˌhaɪpərˈtenʃən/', definition: 'Abnormally high blood pressure, especially in the arteries.', example: 'Uncontrolled hypertension is a major risk factor for stroke.' },
    { word: 'ischemia', pronunciation: '/ɪˈskiːmiə/', definition: 'Restriction in blood supply to tissues, causing a shortage of oxygen.', example: 'Myocardial ischemia can present as angina pectoris.' },
    { word: 'juxtaposition', pronunciation: '/ˌdʒʌkstəpəˈzɪʃən/', definition: 'The fact of two things being seen or placed close together with contrasting effect.', example: 'The juxtaposition of symptoms helped narrow the differential diagnosis.' },
    { word: 'ketonuria', pronunciation: '/ˌkiːtəˈnjʊəriə/', definition: 'The presence of ketone bodies in the urine.', example: 'Ketonuria is commonly found in patients with diabetic ketoacidosis.' },
    { word: 'lymphadenopathy', pronunciation: '/lɪmˌfædənˈɑːpəθi/', definition: 'Disease of the lymph nodes, usually referring to swollen lymph nodes.', example: 'Generalized lymphadenopathy may indicate systemic infection.' },
    { word: 'metastasis', pronunciation: '/məˈtæstəsɪs/', definition: 'The development of secondary malignant growths from a primary tumor.', example: 'The biopsy confirmed metastasis to the regional lymph nodes.' },
    { word: 'neutropenia', pronunciation: '/ˌnuːtrəˈpiːniə/', definition: 'An abnormally low count of neutrophils, a type of white blood cell.', example: 'Chemotherapy often causes neutropenia, increasing infection risk.' },
    { word: 'orthopnea', pronunciation: '/ɔːrˈθɒpniə/', definition: 'Shortness of breath that occurs when lying flat.', example: 'The patient reported orthopnea and required three pillows to sleep.' },
    { word: 'pericardium', pronunciation: '/ˌperɪˈkɑːrdiəm/', definition: 'The membrane sac enclosing the heart.', example: 'Fluid was detected in the pericardium during the ultrasound.' },
    { word: 'rales', pronunciation: '/rɑːlz/', definition: 'Abnormal lung sounds heard on auscultation, also called crackles.', example: 'Bilateral basal rales were noted in the patient with pneumonia.' },
    { word: 'syncope', pronunciation: '/ˈsɪŋkəpi/', definition: 'Temporary loss of consciousness caused by a fall in blood pressure.', example: 'The patient experienced syncope while standing for a prolonged period.' },
    { word: 'tinnitus', pronunciation: '/ˈtɪnɪtəs/', definition: 'Ringing or buzzing noise in one or both ears.', example: 'The patient complained of persistent tinnitus in the left ear.' },
    { word: 'urticaria', pronunciation: '/ˌɜːrtɪˈkeriə/', definition: 'A rash of round, red welts on the skin that itch intensely; also called hives.', example: 'The patient developed urticaria after receiving penicillin.' },
    { word: 'vertigo', pronunciation: '/ˈvɜːrtɪɡoʊ/', definition: 'A sensation of whirling and loss of balance; dizziness.', example: 'Benign paroxysmal positional vertigo is the most common cause of vertigo.' },
    { word: 'wound', pronunciation: '/wuːnd/', definition: 'An injury to living tissue caused by various means.', example: 'Proper wound care is essential to prevent infection and promote healing.' },
    { word: 'xenograft', pronunciation: '/ˈzenəɡræft/', definition: 'A tissue graft from a donor of another species.', example: 'A porcine xenograft was used as a biological dressing for the burn wound.' },
    { word: 'atrophy', pronunciation: '/ˈætrəfi/', definition: 'The wasting away or decrease in size of a body organ or tissue.', example: 'Muscle atrophy is common in patients with prolonged immobilization.' },
    { word: 'biopsy', pronunciation: '/ˈbaɪɑːpsi/', definition: 'An examination of tissue removed from a living body.', example: 'A core needle biopsy was performed to establish the diagnosis.' },
    { word: 'catheter', pronunciation: '/ˈkæθɪtər/', definition: 'A flexible tube inserted into a narrow opening for drainage or administration.', example: 'A Foley catheter was inserted to monitor urine output.' },
    { word: 'defibrillation', pronunciation: '/diːˌfɪbrɪˈleɪʃən/', definition: 'Treatment of life-threatening cardiac arrhythmias by delivering an electric shock.', example: 'Immediate defibrillation was required to restore sinus rhythm.' },
    { word: 'epistaxis', pronunciation: '/ˌepɪˈstæksɪs/', definition: 'Bleeding from the nose; also known as a nosebleed.', example: 'The patient presented with recurrent epistaxis requiring nasal packing.' },
    { word: 'fracture', pronunciation: '/ˈfræktʃər/', definition: 'The breaking of a bone or cartilage.', example: 'An X-ray confirmed a displaced fracture of the distal radius.' }
  ];

  // Get today's date as day index
  function getDayIndex() {
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    const diff = now - start;
    const oneDay = 1000 * 60 * 60 * 24;
    return Math.floor(diff / oneDay) % WORDS.length;
  }

  // Format date nicely
  function formatDate() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return now.toLocaleDateString('en-US', options);
  }

  // Get container ID from script
  function getContainerId() {
    const scripts = document.querySelectorAll('script[src*="medical-word-widget"]');
    for (const script of scripts) {
      const containerId = script.getAttribute('data-container');
      if (containerId) return containerId;
    }
    return 'medword-widget';
  }

  // Widget HTML template
  function getTemplate() {
    return `
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        .mw-widget-container {
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
        
        .mw-header {
          background: ${CONFIG.brandGreen};
          padding: 18px 22px 14px;
          position: relative;
        }
        
        .mw-header::after {
          content: '';
          position: absolute;
          bottom: -12px;
          left: 0;
          right: 0;
          height: 24px;
          background: ${CONFIG.white};
          border-radius: 50% 50% 0 0;
        }
        
        .mw-logo {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          margin-bottom: 10px;
          position: relative;
          z-index: 1;
        }
        
        .mw-logo-icon {
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
        
        .mw-logo-text {
          color: ${CONFIG.white};
          font-size: 17px;
          font-weight: 800;
          letter-spacing: 2px;
        }
        
        .mw-header-title {
          color: rgba(255,255,255,0.9);
          font-size: 13px;
          font-weight: 600;
          text-align: center;
          position: relative;
          z-index: 1;
        }
        
        .mw-body {
          padding: 8px 22px 20px;
        }
        
        .mw-date-badge {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          background: ${CONFIG.medicalGreen};
          color: ${CONFIG.medicalGreenDark};
          font-size: 11px;
          font-weight: 600;
          padding: 5px 14px;
          border-radius: 20px;
          margin-bottom: 16px;
        }
        
        .mw-word-card {
          background: ${CONFIG.brandCream};
          border-radius: 14px;
          padding: 22px;
          border: 1px solid ${CONFIG.lightGray};
          margin-bottom: 16px;
          position: relative;
        }
        
        .mw-word-number {
          position: absolute;
          top: 12px;
          right: 14px;
          font-size: 10px;
          font-weight: 700;
          color: ${CONFIG.midGray};
          background: ${CONFIG.white};
          padding: 2px 8px;
          border-radius: 10px;
        }
        
        .mw-word {
          font-size: 22px;
          font-weight: 800;
          color: ${CONFIG.brandGreen};
          margin-bottom: 4px;
          letter-spacing: -0.3px;
        }
        
        .mw-pronunciation {
          font-size: 13px;
          color: ${CONFIG.midGray};
          font-weight: 500;
          margin-bottom: 14px;
          font-style: italic;
        }
        
        .mw-divider {
          height: 2px;
          background: linear-gradient(to right, ${CONFIG.brandOrange}, transparent);
          border-radius: 1px;
          margin: 12px 0;
          width: 40px;
        }
        
        .mw-definition-label {
          font-size: 9px;
          font-weight: 700;
          color: ${CONFIG.brandOrange};
          text-transform: uppercase;
          letter-spacing: 1.5px;
          margin-bottom: 4px;
        }
        
        .mw-definition {
          font-size: 13px;
          color: ${CONFIG.darkText};
          line-height: 1.6;
          margin-bottom: 14px;
        }
        
        .mw-example-label {
          font-size: 9px;
          font-weight: 700;
          color: ${CONFIG.medicalGreenDark};
          text-transform: uppercase;
          letter-spacing: 1.5px;
          margin-bottom: 4px;
        }
        
        .mw-example {
          font-size: 12px;
          color: ${CONFIG.darkText};
          line-height: 1.6;
          font-style: italic;
          padding-left: 12px;
          border-left: 3px solid ${CONFIG.medicalGreenDark};
        }
        
        .mw-nav {
          display: flex;
          justify-content: space-between;
          align-items: center;
          gap: 10px;
        }
        
        .mw-nav-btn {
          flex: 1;
          padding: 10px 16px;
          border: 1.5px solid ${CONFIG.brandGreen};
          background: ${CONFIG.white};
          color: ${CONFIG.brandGreen};
          border-radius: 10px;
          font-size: 12px;
          font-weight: 600;
          font-family: inherit;
          cursor: pointer;
          transition: all 0.2s ease;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 4px;
        }
        
        .mw-nav-btn:hover {
          background: ${CONFIG.brandGreen};
          color: ${CONFIG.white};
        }
        
        .mw-nav-btn:disabled {
          opacity: 0.4;
          cursor: not-allowed;
        }
        
        .mw-nav-btn:disabled:hover {
          background: ${CONFIG.white};
          color: ${CONFIG.brandGreen};
        }
        
        .mw-counter {
          font-size: 11px;
          color: ${CONFIG.midGray};
          font-weight: 500;
          text-align: center;
          min-width: 60px;
        }
        
        .mw-footer {
          padding: 14px 22px;
          background: ${CONFIG.brandCream};
          border-top: 1px solid ${CONFIG.lightGray};
          text-align: center;
        }
        
        .mw-footer a {
          color: ${CONFIG.brandGreen};
          text-decoration: none;
          font-size: 11px;
          font-weight: 600;
          transition: color 0.2s ease;
        }
        
        .mw-footer a:hover {
          color: ${CONFIG.brandOrange};
        }
        
        .mw-footer-text {
          font-size: 10px;
          color: ${CONFIG.midGray};
          margin-top: 4px;
        }

        @media (max-width: 320px) {
          .mw-body { padding: 8px 14px 16px; }
          .mw-word-card { padding: 16px; }
          .mw-word { font-size: 18px; }
        }
      </style>
      
      <div class="mw-widget-container">
        <div class="mw-header">
          <div class="mw-logo">
            <div class="mw-logo-icon">A</div>
            <div class="mw-logo-text">ANGLOTEC</div>
          </div>
          <div class="mw-header-title">Medical English - Word of the Day</div>
        </div>
        
        <div class="mw-body">
          <div class="mw-date-badge" id="mw-date">📅 Today</div>
          
          <div class="mw-word-card">
            <div class="mw-word-number" id="mw-number">1 / 50</div>
            <div class="mw-word" id="mw-word">auscultation</div>
            <div class="mw-pronunciation" id="mw-pronunciation">/ˌɔːskəlˈteɪʃən/</div>
            <div class="mw-divider"></div>
            <div class="mw-definition-label">Definition</div>
            <div class="mw-definition" id="mw-definition">The act of listening to sounds within the body using a stethoscope.</div>
            <div class="mw-example-label">Clinical Example</div>
            <div class="mw-example" id="mw-example">The doctor performed auscultation to check for abnormal heart sounds.</div>
          </div>
          
          <div class="mw-nav">
            <button class="mw-nav-btn" id="mw-prev">
              ← Previous
            </button>
            <div class="mw-counter" id="mw-counter">1 / 50</div>
            <button class="mw-nav-btn" id="mw-next">
              Next →
            </button>
          </div>
        </div>
        
        <div class="mw-footer">
          <a href="${CONFIG.baseUrl}${CONFIG.utmParams}" target="_blank" rel="noopener">Learn more Medical English →</a>
          <div class="mw-footer-text">Powered by Anglotec AI Academy</div>
        </div>
      </div>
    `;
  }

  function init() {
    const containerId = getContainerId();
    const container = document.getElementById(containerId);
    if (!container) {
      console.warn('[Anglotec Medical Word Widget] Container #' + containerId + ' not found');
      return;
    }

    const shadow = container.attachShadow({ mode: 'open' });
    shadow.innerHTML = getTemplate();

    let currentIndex = getDayIndex();
    
    const wordEl = shadow.getElementById('mw-word');
    const pronEl = shadow.getElementById('mw-pronunciation');
    const defEl = shadow.getElementById('mw-definition');
    const exEl = shadow.getElementById('mw-example');
    const numEl = shadow.getElementById('mw-number');
    const counterEl = shadow.getElementById('mw-counter');
    const dateEl = shadow.getElementById('mw-date');
    const prevBtn = shadow.getElementById('mw-prev');
    const nextBtn = shadow.getElementById('mw-next');

    dateEl.textContent = '📅 ' + formatDate();

    function render() {
      const w = WORDS[currentIndex];
      wordEl.textContent = w.word;
      pronEl.textContent = w.pronunciation;
      defEl.textContent = w.definition;
      exEl.textContent = w.example;
      numEl.textContent = (currentIndex + 1) + ' / ' + WORDS.length;
      counterEl.textContent = (currentIndex + 1) + ' / ' + WORDS.length;
      
      prevBtn.disabled = currentIndex === 0;
      nextBtn.disabled = currentIndex === WORDS.length - 1;
    }

    prevBtn.addEventListener('click', function() {
      if (currentIndex > 0) {
        currentIndex--;
        render();
      }
    });

    nextBtn.addEventListener('click', function() {
      if (currentIndex < WORDS.length - 1) {
        currentIndex++;
        render();
      }
    });

    render();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
