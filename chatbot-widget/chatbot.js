/**
 * Anglotec AI Chatbot Widget - Main Logic
 * Handles conversation flow, Q&A matching, qualifying questions, and recommendations
 */

(function() {
  'use strict';

  // ============================================================
  // CONFIGURATION
  // ============================================================
  const CONFIG = {
    botName: 'Emma',
    companyName: 'Anglotec AI',
    websiteUrl: 'https://tools.anglotec-ai.com',
    greetingDelay: 5000,      // 5 seconds before auto-greeting
    typingDelay: 800,         // ms to simulate typing
    followUpDelay: 1500,      // ms before follow-up question
    maxHistory: 50,           // max messages to keep
    soundEnabled: false       // enable notification sounds
  };

  // ============================================================
  // STATE MANAGEMENT
  // ============================================================
  const state = {
    isOpen: false,
    isMinimized: false,
    messages: [],
    userContext: {
      exam: null,           // ielts | oet | osce | plab | nhs | language
      profession: null,     // nurse | doctor | student
      targetScore: null,
      strugglingArea: null,
      nhsBand: null,
      stage: null,          // greeting | qualifying | recommending | qa
      emailCollected: false
    },
    conversationStep: 0,
    hasGreeted: false,
    messageCount: 0
  };

  // ============================================================
  // DOM REFERENCES (set during init)
  // ============================================================
  let dom = {};

  // ============================================================
  // CONVERSATION FLOW DEFINITIONS
  // ============================================================
  const FLOWS = {
    ielts: {
      name: 'IELTS',
      steps: [
        {
          question: 'Great choice! Are you preparing for **IELTS Academic** or **General Training**?',
          quickReplies: ['Academic', 'General Training', 'Not sure']
        },
        {
          question: 'What\'s your target band score? Most universities need 6.5-7.0, while NMC/GMC require 7.0-7.5.',
          quickReplies: ['5.5-6.0', '6.5', '7.0', '7.5+']
        },
        {
          question: 'Which section do you find most challenging?',
          quickReplies: ['Writing', 'Speaking', 'Reading', 'Listening']
        }
      ],
      recommendations: {
        writing: {
          text: 'Our **IELTS Writing Checker** gives instant AI feedback on your essays!',
          link: { title: 'IELTS Writing Checker', url: 'https://tools.anglotec-ai.com/ielts-writing', desc: 'AI-powered essay feedback & scoring' }
        },
        speaking: {
          text: 'Practice Speaking with our AI tutor - unlimited mock tests!',
          link: { title: 'IELTS Speaking Practice', url: 'https://tools.anglotec-ai.com/ielts-speaking', desc: 'AI mock speaking tests' }
        },
        reading: {
          text: 'Try our IELTS Reading practice tests with timed simulations!',
          link: { title: 'IELTS Reading Practice', url: 'https://tools.anglotec-ai.com/ielts-reading', desc: 'Timed practice tests' }
        },
        listening: {
          text: 'Improve Listening with our audio practice tests!',
          link: { title: 'IELTS Listening Practice', url: 'https://tools.anglotec-ai.com/ielts-listening', desc: 'Audio tests with various accents' }
        },
        default: {
          text: 'Our **Complete IELTS Preparation Platform** has everything you need!',
          link: { title: 'Full IELTS Platform', url: 'https://tools.anglotec-ai.com/ielts-course', desc: 'All sections covered with AI feedback' }
        }
      }
    },

    oet: {
      name: 'OET',
      steps: [
        {
          question: 'Are you a **nurse** or a **doctor**? (Or another healthcare professional?)',
          quickReplies: ['Nurse', 'Doctor', 'Pharmacist', 'Dentist', 'Other']
        },
        {
          question: 'Which sub-test are you most worried about?',
          quickReplies: ['Writing (Referral Letter)', 'Speaking (Role-Play)', 'Reading', 'Listening']
        },
        {
          question: 'Have you taken the OET before?',
          quickReplies: ['Yes, need to improve', 'No, first time', 'Failed previously']
        }
      ],
      recommendations: {
        writing: {
          text: 'Our **OET Writing Practice** tool generates referral letters and gives instant feedback!',
          link: { title: 'OET Writing Practice', url: 'https://tools.anglotec-ai.com/oet-writing', desc: 'Referral letter generator & checker' }
        },
        speaking: {
          text: 'The **OET Role-Play Generator** creates unlimited practice scenarios!',
          link: { title: 'OET Role-Play Generator', url: 'https://tools.anglotec-ai.com/oet-roleplay', desc: 'Unlimited speaking scenarios' }
        },
        reading: {
          text: 'Master OET Reading with practice tests for Parts A, B, and C!',
          link: { title: 'OET Reading Practice', url: 'https://tools.anglotec-ai.com/oet-reading', desc: 'All reading parts covered' }
        },
        listening: {
          text: 'Practice OET Listening with medical consultations and lectures!',
          link: { title: 'OET Listening Practice', url: 'https://tools.anglotec-ai.com/oet-listening', desc: 'Medical audio practice' }
        },
        default: {
          text: 'Get full OET preparation with our **Complete OET Course**!',
          link: { title: 'Full OET Course', url: 'https://tools.anglotec-ai.com/oet-course', desc: 'Nurse & doctor-specific content' }
        }
      }
    },

    osce: {
      name: 'OSCE',
      steps: [
        {
          question: 'Are you preparing for **NMC OSCE** (nurses), **PLAB 2** (doctors), or **medical school OSCE**?',
          quickReplies: ['NMC OSCE', 'PLAB 2', 'Medical School OSCE']
        },
        {
          question: 'Which station type do you find the hardest?',
          quickReplies: ['History Taking', 'Physical Examination', 'Communication/Breaking Bad News', 'Practical Skills', 'Prescribing']
        },
        {
          question: 'How soon is your exam?',
          quickReplies: ['This week!', 'In 2-4 weeks', 'In 1-2 months', '3+ months']
        }
      ],
      recommendations: {
        'history taking': {
          text: 'Practice **History Taking** with our structured OSCE scenarios!',
          link: { title: 'History Taking Trainer', url: 'https://tools.anglotec-ai.com/history-taking', desc: 'Structured patient histories' }
        },
        'physical examination': {
          text: 'Master examinations with step-by-step guides and marking criteria!',
          link: { title: 'Examination Trainer', url: 'https://tools.anglotec-ai.com/examination-trainer', desc: 'All body systems covered' }
        },
        'communication': {
          text: 'Practice **Breaking Bad News** and difficult conversations with AI!',
          link: { title: 'Communication Trainer', url: 'https://tools.anglotec-ai.com/communication', desc: 'SPIKES protocol practice' }
        },
        'practical skills': {
          text: 'Learn procedures with our step-by-step **Skills Trainer**!',
          link: { title: 'OSCE Skills Trainer', url: 'https://tools.anglotec-ai.com/osce-skills', desc: 'IM injection, catheterisation, etc.' }
        },
        default: {
          text: 'Our **OSCE Scenario Generator** creates unlimited practice stations with full marking!',
          link: { title: 'OSCE Scenario Generator', url: 'https://tools.anglotec-ai.com/osce-scenarios', desc: 'Unlimited AI-generated stations' }
        }
      }
    },

    plab: {
      name: 'PLAB 2',
      steps: [
        {
          question: 'Have you passed PLAB 1 already?',
          quickReplies: ['Yes', 'Not yet', 'Taking it soon']
        },
        {
          question: 'Which PLAB 2 station type worries you most?',
          quickReplies: ['Examination Stations', 'History Taking', 'Simulated Consultations', 'Practical Skills']
        },
        {
          question: 'How are you currently preparing?',
          quickReplies: ['Self-study', 'Academy/Course', 'Just starting', 'Retaking']
        }
      ],
      recommendations: {
        default: {
          text: 'Our **PLAB 2 Complete Trainer** has 16-station mock exams with AI feedback!',
          link: { title: 'PLAB 2 Trainer', url: 'https://tools.anglotec-ai.com/plab2', desc: 'Full 16-station mock exams' }
        }
      }
    },

    nhs: {
      name: 'NHS Careers',
      steps: [
        {
          question: 'Are you applying for **Band 5** (newly qualified) or already registered?',
          quickReplies: ['Band 5 - Newly Qualified', 'Band 6 - Experienced', 'Already Registered', 'Not sure about bands']
        },
        {
          question: 'What stage are you at in your NHS journey?',
          quickReplies: ['Applying for jobs', 'Have an interview soon', 'Just exploring options', 'Need NMC registration']
        }
      ],
      recommendations: {
        interview: {
          text: 'Our **NHS Interview Question Bank** has 500+ questions with model answers!',
          link: { title: 'NHS Interview Bank', url: 'https://tools.anglotec-ai.com/nhs-interviews', desc: '500+ interview questions' }
        },
        cv: {
          text: 'Create a winning NHS CV with our **CV Builder**!',
          link: { title: 'NHS CV Builder', url: 'https://tools.anglotec-ai.com/nhs-cv', desc: 'NHS-format CV creator' }
        },
        default: {
          text: 'Explore our **NHS Career Hub** for jobs, interviews, and career progression!',
          link: { title: 'NHS Career Hub', url: 'https://tools.anglotec-ai.com/nhs-careers', desc: 'Jobs, CVs, interviews & more' }
        }
      }
    },

    language: {
      name: 'Language Learning',
      steps: [
        {
          question: 'What language skill do you want to improve most?',
          quickReplies: ['Medical English', 'General English', 'Pronunciation', 'Writing']
        }
      ],
      recommendations: {
        default: {
          text: 'Try our **12-Language AI Tutor** - practice medical conversations in any language!',
          link: { title: '12-Language AI Tutor', url: 'https://tools.anglotec-ai.com/ai-tutor', desc: 'AI-powered multilingual tutor' }
        }
      }
    }
  };

  // ============================================================
  // GREETING & FALLBACK MESSAGES
  // ============================================================
  const GREETING = "Hi there! I'm **Emma**, your AI study assistant at Anglotec. I can help you with **IELTS**, **OET**, **OSCE**, **PLAB 2**, or **NHS career** questions. What are you preparing for?";

  const FALLBACKS = [
    "I'm not sure I understood that correctly. Could you rephrase? I can help with IELTS, OET, OSCE, PLAB 2, or NHS careers.",
    "I want to make sure I give you the best answer! Are you asking about IELTS, OET, OSCE/PLAB, or NHS careers?",
    "Great question! To give you the most helpful answer, could you tell me which exam you're preparing for?"
  ];

  // ============================================================
  // INTENT DETECTION KEYWORDS
  // ============================================================
  const INTENT_KEYWORDS = {
    ielts: ['ielts', 'ielts academic', 'ielts general', 'ielts gt', 'band score', 'band 7', 'band 6', 'band 8', 'ielts writing', 'ielts speaking', 'ielts reading', 'ielts listening'],
    oet: ['oet', 'occupational english', 'occupational english test', 'referral letter', 'role play', 'oet nurse', 'oet doctor', 'oet writing', 'oet speaking'],
    osce: ['osce', 'nmc osce', 'objective structured', 'clinical exam', 'station', 'api', 'api station', 'history taking', 'physical exam'],
    plab: ['plab', 'plab 2', 'plab2', 'gmc', 'gmc registration'],
    nhs: ['nhs', 'band 5', 'band 6', 'band 7', 'interview', 'nurse interview', 'nursing job', 'nhs job', 'nmc registration', 'cbt'],
    language: ['language', 'english', 'vocabulary', 'grammar', 'fluency', 'pronunciation', 'speaking practice', 'medical english']
  };

  // ============================================================
  // UTILITY FUNCTIONS
  // ============================================================
  function detectIntent(text) {
    const lower = text.toLowerCase();
    const scores = {};

    for (const [intent, keywords] of Object.entries(INTENT_KEYWORDS)) {
      scores[intent] = 0;
      for (const kw of keywords) {
        if (lower.includes(kw.toLowerCase())) {
          scores[intent] += kw.split(' ').length; // Weight multi-word matches higher
        }
      }
    }

    // Find highest scoring intent
    let bestIntent = null;
    let bestScore = 0;
    for (const [intent, score] of Object.entries(scores)) {
      if (score > bestScore) {
        bestScore = score;
        bestIntent = intent;
      }
    }

    return bestScore > 0 ? bestIntent : null;
  }

  function findBestQAMatch(text) {
    if (typeof getAllQuestions !== 'function') return null;

    const allQuestions = getAllQuestions();
    const lower = text.toLowerCase();
    let bestMatch = null;
    let bestScore = 0;

    for (const qa of allQuestions) {
      let score = 0;
      // Check keywords
      for (const kw of qa.keywords) {
        if (lower.includes(kw.toLowerCase())) {
          score += kw.split(' ').length * 2;
        }
      }
      // Check question text overlap
      const qWords = qa.question.toLowerCase().split(/\s+/);
      for (const word of qWords) {
        if (word.length > 3 && lower.includes(word)) {
          score += 0.5;
        }
      }

      if (score > bestScore && score >= 2) {
        bestScore = score;
        bestMatch = qa;
      }
    }

    return bestMatch;
  }

  function getTimestamp() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

  function shuffleArray(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  // ============================================================
  // DOM MANIPULATION
  // ============================================================
  function createWidgetHTML() {
    return `
      <!-- Chat Bubble -->
      <button class="anglo-chat-bubble hidden" id="angloBubble" aria-label="Open chat">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/>
          <circle cx="12" cy="10" r="1.5"/><circle cx="8" cy="10" r="1.5"/><circle cx="16" cy="10" r="1.5"/>
        </svg>
        <span class="bubble-badge" id="angloBadge" style="display:none">1</span>
      </button>

      <!-- Chat Window -->
      <div class="anglo-chat-window closed" id="angloWindow">
        <!-- Header -->
        <div class="anglo-chat-header" id="angloHeader">
          <div class="anglo-header-info">
            <div class="anglo-bot-avatar">🤖</div>
            <div class="anglo-header-text">
              <h3>Anglotec AI Assistant</h3>
              <p class="status"><span class="anglo-status-dot"></span> Online now</p>
            </div>
          </div>
          <div class="anglo-header-actions">
            <button class="anglo-header-btn" id="angloMinBtn" title="Minimize">−</button>
            <button class="anglo-header-btn" id="angloCloseBtn" title="Close">✕</button>
          </div>
        </div>

        <!-- Messages Area -->
        <div class="anglo-chat-messages" id="angloMessages"></div>

        <!-- Suggested Topics -->
        <div class="anglo-suggested-topics" id="angloTopics" style="display:none">
          <p>Popular topics:</p>
          <div class="anglo-topic-tags" id="angloTopicTags"></div>
        </div>

        <!-- Input Area -->
        <div class="anglo-chat-input">
          <input type="text" id="angloInput" placeholder="Type your question..." autocomplete="off" />
          <button class="anglo-send-btn" id="angloSendBtn" aria-label="Send message">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/>
            </svg>
          </button>
        </div>

        <!-- Branding -->
        <div class="anglo-branding">
          Powered by <a href="${CONFIG.websiteUrl}" target="_blank">${CONFIG.companyName}</a>
        </div>
      </div>
    `;
  }

  function initDOM() {
    const container = document.createElement('div');
    container.id = 'anglo-chatbot-widget';
    container.innerHTML = createWidgetHTML();
    document.body.appendChild(container);

    dom = {
      bubble: document.getElementById('angloBubble'),
      badge: document.getElementById('angloBadge'),
      window: document.getElementById('angloWindow'),
      header: document.getElementById('angloHeader'),
      messages: document.getElementById('angloMessages'),
      input: document.getElementById('angloInput'),
      sendBtn: document.getElementById('angloSendBtn'),
      closeBtn: document.getElementById('angloCloseBtn'),
      minBtn: document.getElementById('angloMinBtn'),
      topics: document.getElementById('angloTopics'),
      topicTags: document.getElementById('angloTopicTags')
    };

    // Event listeners
    dom.bubble.addEventListener('click', openChat);
    dom.closeBtn.addEventListener('click', closeChat);
    dom.minBtn.addEventListener('click', minimizeChat);
    dom.header.addEventListener('dblclick', minimizeChat);
    dom.sendBtn.addEventListener('click', handleSend);
    dom.input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleSend();
    });
  }

  // ============================================================
  // CHAT UI FUNCTIONS
  // ============================================================
  function openChat() {
    state.isOpen = true;
    state.isMinimized = false;
    dom.bubble.classList.add('hidden');
    dom.window.classList.remove('closed', 'minimized');
    dom.input.focus();

    // Show greeting on first open
    if (!state.hasGreeted) {
      state.hasGreeted = true;
      showTyping(() => {
        addBotMessage(GREETING);
        showQuickReplies(['IELTS', 'OET', 'OSCE', 'PLAB 2', 'NHS Careers', 'Language Help']);
        showSuggestedTopics();
      });
    }
  }

  function closeChat() {
    state.isOpen = false;
    dom.window.classList.add('closed');
    setTimeout(() => {
      dom.bubble.classList.remove('hidden');
    }, 300);
  }

  function minimizeChat() {
    state.isMinimized = !state.isMinimized;
    dom.window.classList.toggle('minimized', state.isMinimized);
    dom.minBtn.textContent = state.isMinimized ? '□' : '−';
  }

  function addBotMessage(text, options = {}) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'anglo-message bot';
    msgDiv.innerHTML = `
      <div class="anglo-message-avatar">🤖</div>
      <div>
        <div class="anglo-message-content">${formatMessage(text)}</div>
        <div class="anglo-message-time">${getTimestamp()}</div>
      </div>
    `;
    dom.messages.appendChild(msgDiv);
    scrollToBottom();
    state.messageCount++;

    // Maybe show link card
    if (options.link) {
      addLinkCard(options.link);
    }

    // Maybe show quick replies
    if (options.quickReplies) {
      showQuickReplies(options.quickReplies);
    }

    // Maybe show email collection
    if (state.messageCount >= 6 && !state.userContext.emailCollected && Math.random() > 0.5) {
      setTimeout(() => showEmailCollector(), 2000);
    }
  }

  function addUserMessage(text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'anglo-message user';
    msgDiv.innerHTML = `
      <div class="anglo-message-avatar">👤</div>
      <div>
        <div class="anglo-message-content">${escapeHtml(text)}</div>
        <div class="anglo-message-time">${getTimestamp()}</div>
      </div>
    `;
    dom.messages.appendChild(msgDiv);
    scrollToBottom();
    state.messageCount++;
  }

  function showTyping(callback) {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'anglo-typing';
    typingDiv.id = 'angloTyping';
    typingDiv.innerHTML = `
      <div class="anglo-message-avatar">🤖</div>
      <div class="anglo-typing-dots">
        <span></span><span></span><span></span>
      </div>
    `;
    dom.messages.appendChild(typingDiv);
    scrollToBottom();

    setTimeout(() => {
      const el = document.getElementById('angloTyping');
      if (el) el.remove();
      if (callback) callback();
    }, CONFIG.typingDelay + Math.random() * 500);
  }

  function showQuickReplies(replies) {
    // Remove existing quick replies
    const existing = dom.messages.querySelectorAll('.anglo-quick-replies');
    existing.forEach(el => el.remove());

    const container = document.createElement('div');
    container.className = 'anglo-quick-replies';
    container.style.marginLeft = '36px';

    replies.forEach(reply => {
      const btn = document.createElement('button');
      btn.className = 'anglo-quick-btn';
      btn.textContent = reply;
      btn.addEventListener('click', () => handleQuickReply(reply));
      container.appendChild(btn);
    });

    dom.messages.appendChild(container);
    scrollToBottom();
  }

  function addLinkCard(link) {
    const card = document.createElement('a');
    card.className = 'anglo-link-card';
    card.href = link.url;
    card.target = '_blank';
    card.rel = 'noopener noreferrer';
    card.innerHTML = `
      <p class="link-title">🔗 ${escapeHtml(link.title)}</p>
      <p class="link-desc">${escapeHtml(link.desc)}</p>
      <p class="link-url">${link.url.replace('https://', '')}</p>
    `;
    card.style.marginLeft = '36px';
    card.style.maxWidth = '320px';
    dom.messages.appendChild(card);
    scrollToBottom();
  }

  function showSuggestedTopics() {
    const topics = [
      'IELTS Writing Tips',
      'OET Role-Play',
      'OSCE Stations',
      'NHS Interview',
      'PLAB 2 Prep',
      'Free Trial'
    ];

    dom.topics.style.display = 'block';
    dom.topicTags.innerHTML = '';

    topics.forEach(topic => {
      const tag = document.createElement('button');
      tag.className = 'anglo-topic-tag';
      tag.textContent = topic;
      tag.addEventListener('click', () => handleQuickReply(topic));
      dom.topicTags.appendChild(tag);
    });
  }

  function showEmailCollector() {
    if (state.userContext.emailCollected) return;

    const existing = dom.messages.querySelector('.anglo-email-form');
    if (existing) return;

    const form = document.createElement('div');
    form.className = 'anglo-email-form';
    form.style.marginLeft = '36px';
    form.style.maxWidth = '320px';
    form.innerHTML = `
      <p>📧 Want study tips sent to your inbox? Get a <strong>free study plan</strong>!</p>
      <div class="email-input-row">
        <input type="email" id="angloEmailInput" placeholder="your@email.com" />
        <button class="email-submit" id="angloEmailSubmit">Send</button>
      </div>
      <p class="privacy-note">🔒 We respect your privacy. Unsubscribe anytime. No spam.</p>
    `;

    dom.messages.appendChild(form);
    scrollToBottom();

    // Handle email submit
    const emailInput = form.querySelector('#angloEmailInput');
    const submitBtn = form.querySelector('#angloEmailSubmit');

    const submitEmail = () => {
      const email = emailInput.value.trim();
      if (email && isValidEmail(email)) {
        state.userContext.emailCollected = true;
        // In production, send to your API
        console.log('[Anglotec Chatbot] Email collected:', email);
        form.innerHTML = '<p style="color: var(--anglo-green); margin: 0; font-weight: 500;">✅ Thanks! Check your inbox for your free study plan!</p>';

        // Follow up message
        setTimeout(() => {
          showTyping(() => {
            addBotMessage("I've sent a personalized study guide to your email! Meanwhile, feel free to ask me anything about your exam preparation. 💪");
          });
        }, 1000);
      } else {
        emailInput.style.borderColor = '#E74C3C';
        setTimeout(() => {
          emailInput.style.borderColor = '';
        }, 2000);
      }
    };

    submitBtn.addEventListener('click', submitEmail);
    emailInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') submitEmail();
    });
  }

  function scrollToBottom() {
    setTimeout(() => {
      dom.messages.scrollTop = dom.messages.scrollHeight;
    }, 50);
  }

  function formatMessage(text) {
    // Convert **bold** to <strong>
    text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    // Convert newlines to <br>
    text = text.replace(/\n/g, '<br>');
    return text;
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // ============================================================
  // MESSAGE HANDLING
  // ============================================================
  function handleSend() {
    const text = dom.input.value.trim();
    if (!text) return;

    addUserMessage(text);
    dom.input.value = '';

    // Process the message
    processUserMessage(text);
  }

  function handleQuickReply(reply) {
    addUserMessage(reply);
    processUserMessage(reply);
  }

  function processUserMessage(text) {
    const lower = text.toLowerCase();

    // Check for special intents first
    if (lower.includes('free trial') || lower.includes('trial') || lower.includes('try')) {
      showTyping(() => {
        addBotMessage("Great news! You can try all our tools for **free** - no credit card required! 🎉", {
          link: { title: 'Start Free Trial', url: 'https://tools.anglotec-ai.com/signup', desc: '7-day free access to all tools' }
        });
      });
      return;
    }

    if (lower.includes('price') || lower.includes('cost') || lower.includes('how much') || lower.includes('pricing')) {
      showTyping(() => {
        addBotMessage("Our pricing is super flexible! We have a **free tier**, premium plans from **£9.99/month**, and full platform access at **£29.99/month**. Plus, training centres get group discounts!", {
          link: { title: 'View Pricing', url: 'https://tools.anglotec-ai.com/pricing', desc: 'All plans with free trials' }
        });
      });
      return;
    }

    if (lower.includes('contact') || lower.includes('email') || lower.includes('phone') || lower.includes('support') || lower.includes('human') || lower.includes('talk to')) {
      showTyping(() => {
        addBotMessage("You can reach our team at **support@anglotec-ai.com** or via WhatsApp. We typically respond within 2 hours during UK business hours. 📧");
      });
      return;
    }

    if (lower.includes('about') || lower.includes('who are you') || (lower.includes('what is') && lower.includes('anglotec'))) {
      showTyping(() => {
        addBotMessage("Anglotec is an **AI-powered education platform** for healthcare professionals. We help nurses, doctors, and medical students pass IELTS, OET, OSCE, and PLAB exams - and build successful UK careers! 🇬🇧", {
          link: { title: 'About Anglotec', url: 'https://tools.anglotec-ai.com/about', desc: 'Learn more about our mission' }
        });
      });
      return;
    }

    if (lower.includes('thank') || lower.includes('thanks')) {
      showTyping(() => {
        const responses = [
          "You're very welcome! 😊 I'm here 24/7 if you need anything else!",
          "My pleasure! Feel free to come back anytime - good luck with your studies! 🍀",
          "Anytime! You've got this! 💪 Remember, consistency is key to exam success."
        ];
        addBotMessage(responses[Math.floor(Math.random() * responses.length)]);
      });
      return;
    }

    if (lower.includes('bye') || lower.includes('goodbye') || lower.includes('see you')) {
      showTyping(() => {
        addBotMessage("Goodbye! Best of luck with your exam preparation! 🌟 Remember, I'm here 24/7 whenever you need help. Come back anytime!");
      });
      return;
    }

    // Detect which exam/topic they're interested in
    const intent = detectIntent(text);

    if (intent) {
      // Check if we already have a context for this intent
      if (state.userContext.exam !== intent) {
        state.userContext.exam = intent;
        state.conversationStep = 0;
        startQualifyingFlow(intent);
      } else {
        // Continue the qualifying flow
        continueQualifyingFlow(text, intent);
      }
      return;
    }

    // Try to find a matching Q&A
    if (typeof getAllQuestions === 'function') {
      const qa = findBestQAMatch(text);
      if (qa) {
        showTyping(() => {
          addBotMessage(qa.answer, {
            link: qa.link,
            quickReplies: generateContextualReplies(qa.category)
          });
        });
        return;
      }
    }

    // Fallback response
    showTyping(() => {
      const fallback = FALLBACKS[Math.floor(Math.random() * FALLBACKS.length)];
      addBotMessage(fallback);
      setTimeout(() => {
        showQuickReplies(['IELTS', 'OET', 'OSCE', 'PLAB 2', 'NHS Careers', 'Free Trial']);
      }, 100);
    });
  }

  // ============================================================
  // QUALIFYING FLOW
  // ============================================================
  function startQualifyingFlow(intent) {
    const flow = FLOWS[intent];
    if (!flow) return;

    const step = flow.steps[0];
    state.userContext.stage = 'qualifying';

    showTyping(() => {
      addBotMessage(`You selected **${flow.name}**! ${step.question}`, {
        quickReplies: step.quickReplies
      });
    });
  }

  function continueQualifyingFlow(text, intent) {
    const flow = FLOWS[intent];
    if (!flow) return;

    const currentStep = state.conversationStep;
    const nextStep = currentStep + 1;

    // Store context from their answer
    storeContextFromAnswer(text, intent, currentStep);

    if (nextStep < flow.steps.length) {
      state.conversationStep = nextStep;
      const step = flow.steps[nextStep];

      showTyping(() => {
        addBotMessage(step.question, {
          quickReplies: step.quickReplies
        });
      });
    } else {
      // All qualifying questions done - give recommendation
      state.userContext.stage = 'recommending';
      provideRecommendation(intent);
    }
  }

  function storeContextFromAnswer(text, intent, step) {
    const lower = text.toLowerCase();

    if (intent === 'ielts') {
      if (step === 0) {
        if (lower.includes('academic')) state.userContext.profession = 'academic';
        else if (lower.includes('general')) state.userContext.profession = 'general';
      } else if (step === 1) {
        const scores = lower.match(/(\d+\.?\d*)/);
        if (scores) state.userContext.targetScore = scores[1];
      } else if (step === 2) {
        if (lower.includes('writing')) state.userContext.strugglingArea = 'writing';
        else if (lower.includes('speaking')) state.userContext.strugglingArea = 'speaking';
        else if (lower.includes('reading')) state.userContext.strugglingArea = 'reading';
        else if (lower.includes('listening')) state.userContext.strugglingArea = 'listening';
      }
    } else if (intent === 'oet') {
      if (step === 0) {
        if (lower.includes('nurse')) state.userContext.profession = 'nurse';
        else if (lower.includes('doctor')) state.userContext.profession = 'doctor';
      } else if (step === 1) {
        if (lower.includes('writing')) state.userContext.strugglingArea = 'writing';
        else if (lower.includes('speaking')) state.userContext.strugglingArea = 'speaking';
        else if (lower.includes('reading')) state.userContext.strugglingArea = 'reading';
        else if (lower.includes('listening')) state.userContext.strugglingArea = 'listening';
      }
    } else if (intent === 'osce') {
      if (step === 0) {
        if (lower.includes('nmc')) state.userContext.profession = 'nurse';
        else if (lower.includes('plab')) state.userContext.exam = 'plab';
        else if (lower.includes('medical school')) state.userContext.profession = 'student';
      } else if (step === 1) {
        if (lower.includes('history')) state.userContext.strugglingArea = 'history taking';
        else if (lower.includes('exam')) state.userContext.strugglingArea = 'physical examination';
        else if (lower.includes('communication') || lower.includes('bad news')) state.userContext.strugglingArea = 'communication';
        else if (lower.includes('skill') || lower.includes('practical')) state.userContext.strugglingArea = 'practical skills';
      }
    } else if (intent === 'nhs') {
      if (step === 0) {
        if (lower.includes('band 5')) state.userContext.nhsBand = 'band5';
        else if (lower.includes('band 6')) state.userContext.nhsBand = 'band6';
      } else if (step === 1) {
        if (lower.includes('interview')) state.userContext.stage = 'interview';
      }
    }
  }

  function provideRecommendation(intent) {
    const flow = FLOWS[intent];
    if (!flow) return;

    const area = state.userContext.strugglingArea;
    const rec = (flow.recommendations && flow.recommendations[area]) || flow.recommendations.default;

    showTyping(() => {
      addBotMessage(`Based on your answers, here's my recommendation: 🎯\n\n${rec.text}`, {
        link: rec.link
      });

      // Follow up
      setTimeout(() => {
        showTyping(() => {
          addBotMessage("Would you like me to help you with anything else? I can also show you our **free trial** options! 🎁", {
            quickReplies: ['Start Free Trial', 'Ask Another Question', 'View All Tools', 'Email Me Study Tips']
          });
        });
      }, CONFIG.followUpDelay + 500);
    });
  }

  function generateContextualReplies(category) {
    const replies = {
      ielts: ['IELTS Writing', 'IELTS Speaking', 'Band Score Calculator', 'Free IELTS Trial'],
      oet: ['OET Writing', 'OET Role-Play', 'OET for Nurses', 'Free OET Trial'],
      osce: ['OSCE Scenarios', 'History Taking', 'Examination Trainer', 'Free OSCE Trial'],
      nhs: ['NHS Interview', 'NHS CV', 'CBT Questions', 'Career Guide'],
      language: ['AI Tutor', 'Medical Vocabulary', 'Fluency Practice', 'Free Trial'],
      ai: ['AI Prompts', 'Free Trial', 'Pricing', 'Contact Support']
    };
    return replies[category] || ['IELTS', 'OET', 'OSCE', 'Free Trial'];
  }

  // ============================================================
  // AUTO-GREETING ON PAGE LOAD
  // ============================================================
  function startAutoGreeting() {
    setTimeout(() => {
      if (!state.isOpen) {
        dom.badge.textContent = '1';
        dom.badge.style.display = 'flex';
        dom.bubble.classList.remove('hidden');
        dom.bubble.classList.add('attention');
        setTimeout(() => dom.bubble.classList.remove('attention'), 500);
      }
    }, CONFIG.greetingDelay);
  }

  // ============================================================
  // INITIALIZATION
  // ============================================================
  function init() {
    // Wait for DOM and questions.js to load
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initWidget);
    } else {
      initWidget();
    }
  }

  function initWidget() {
    initDOM();
    startAutoGreeting();

    // Make available globally for debugging
    window.AngloChatbot = {
      open: openChat,
      close: closeChat,
      sendMessage: (text) => {
        if (!state.isOpen) openChat();
        setTimeout(() => {
          addUserMessage(text);
          processUserMessage(text);
        }, 500);
      },
      getState: () => ({ ...state }),
      getContext: () => ({ ...state.userContext })
    };

    console.log('[Anglotec Chatbot] Initialized and ready!');
  }

  // Start initialization
  init();

})();
