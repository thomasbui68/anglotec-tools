/**
 * Anglotec AI Chatbot - Questions & Answers Database
 * 50+ common questions about IELTS, OET, OSCE, PLAB 2, NHS careers, language learning
 */

const QADB = {
  // ============================================================
  // IELTS QUESTIONS (10)
  // ============================================================
  ielts: [
    {
      keywords: ['ielts academic', 'academic ielts', 'ielts for university'],
      question: 'What is IELTS Academic?',
      answer: 'IELTS Academic is designed for people applying for higher education or professional registration in an English-speaking environment. It assesses whether you\'re ready to begin studying or training in English.',
      link: { title: 'IELTS Academic Calculator', url: 'https://tools.anglotec-ai.com/ielts-calculator', desc: 'Calculate your band score' }
    },
    {
      keywords: ['ielts general', 'general training', 'ielts gt'],
      question: 'What is IELTS General Training?',
      answer: 'IELTS General Training measures English language proficiency in a practical, everyday context. It\'s typically required for migration to Australia, Canada, New Zealand, and the UK.',
      link: { title: 'IELTS GT Prep', url: 'https://tools.anglotec-ai.com/ielts-gt', desc: 'General Training resources' }
    },
    {
      keywords: ['band score', 'what score', 'target score', 'pass mark'],
      question: 'What band score do I need?',
      answer: 'For NMC registration, nurses need at least 7.0 in Reading, Listening, and Speaking, and 6.5 in Writing (with an overall 7.0). For GMC, doctors need 7.5 overall with no band below 7.0. University requirements vary (usually 6.0-7.5).',
      link: { title: 'Band Score Calculator', url: 'https://tools.anglotec-ai.com/ielts-calculator', desc: 'Check your required score' }
    },
    {
      keywords: ['ielts writing', 'writing task', 'task 1', 'task 2'],
      question: 'How can I improve my IELTS Writing?',
      answer: 'Focus on: 1) Understanding the task requirements, 2) Planning before you write, 3) Using a range of vocabulary and grammar structures, 4) Practicing time management (20 mins for Task 1, 40 mins for Task 2), 5) Getting feedback on your essays.',
      link: { title: 'IELTS Writing Checker', url: 'https://tools.anglotec-ai.com/ielts-writing', desc: 'AI-powered writing feedback' }
    },
    {
      keywords: ['ielts speaking', 'speaking test', 'speaking part'],
      question: 'What happens in the IELTS Speaking test?',
      answer: 'The Speaking test has 3 parts: Part 1 (4-5 mins) - Introduction and interview about familiar topics; Part 2 (3-4 mins) - Individual long turn (cue card); Part 3 (4-5 mins) - Two-way discussion on abstract topics related to Part 2.',
      link: { title: 'IELTS Speaking Practice', url: 'https://tools.anglotec-ai.com/ielts-speaking', desc: 'Practice with AI feedback' }
    },
    {
      keywords: ['ielts reading', 'reading tips', 'reading strategy'],
      question: 'How do I improve my IELTS Reading score?',
      answer: 'Key strategies: 1) Skim the passage first, 2) Read questions before details, 3) Use keyword scanning, 4) Manage your time (20 mins per passage), 5) Practice True/False/Not Given questions, 6) Build your vocabulary.',
      link: { title: 'IELTS Reading Practice', url: 'https://tools.anglotec-ai.com/ielts-reading', desc: 'Practice tests and tips' }
    },
    {
      keywords: ['ielts listening', 'listening tips', 'hearing test'],
      question: 'How can I improve my IELTS Listening score?',
      answer: 'Tips: 1) Practice with various accents (British, Australian, American), 2) Read questions ahead when you have time, 3) Watch for signpost words, 4) Check spelling carefully, 5) Practice note-taking, 6) Get familiar with different question types.',
      link: { title: 'IELTS Listening Practice', url: 'https://tools.anglotec-ai.com/ielts-listening', desc: 'Audio practice tests' }
    },
    {
      keywords: ['ielts booking', 'book ielts', 'register ielts', 'test dates'],
      question: 'How do I book an IELTS test?',
      answer: 'You can book IELTS through: 1) The British Council website, 2) IDP IELTS website, or 3) Official Cambridge test centres. You\'ll need a valid ID (passport). Book at least 1-2 months in advance for your preferred date.',
      link: null
    },
    {
      keywords: ['ielts results', 'how long results', 'ielts score', 'get results'],
      question: 'How long do IELTS results take?',
      answer: 'IELTS results are available 13 calendar days after your test date for paper-based tests, and 3-5 days for computer-delivered tests. Your Test Report Form (TRF) is valid for 2 years.',
      link: null
    },
    {
      keywords: ['ielts vs oet', 'which exam', 'what exam', 'which test'],
      question: 'Should I take IELTS or OET?',
      answer: 'For healthcare professionals: OET is often easier because it uses medical scenarios and vocabulary you already know. However, IELTS is accepted by ALL regulators. Check with your specific regulatory body. NMC and GMC both accept OET now.',
      link: { title: 'Exam Comparison', url: 'https://tools.anglotec-ai.com/exam-comparison', desc: 'IELTS vs OET guide' }
    }
  ],

  // ============================================================
  // OET QUESTIONS (10)
  // ============================================================
  oet: [
    {
      keywords: ['what is oet', 'oet exam', 'occupational english test'],
      question: 'What is the OET?',
      answer: 'The Occupational English Test (OET) is an English language test designed specifically for healthcare professionals. It assesses your ability to communicate effectively in medical workplace scenarios.',
      link: { title: 'OET Introduction', url: 'https://tools.anglotec-ai.com/oet-intro', desc: 'Learn about OET' }
    },
    {
      keywords: ['oet for nurses', 'nurse oet', 'nursing oet'],
      question: 'What score do nurses need on OET?',
      answer: 'For NMC registration, nurses need at least a Grade C+ (300-340) in Writing and Grade B (350-440) in Reading, Listening, and Speaking. All 4 sub-tests must be passed in a single sitting or within 6 months.',
      link: { title: 'OET for Nurses', url: 'https://tools.anglotec-ai.com/oet-nurses', desc: 'Nursing-specific prep' }
    },
    {
      keywords: ['oet for doctors', 'doctor oet', 'medical oet'],
      question: 'What score do doctors need on OET?',
      answer: 'For GMC registration, doctors need at least Grade B in all 4 sub-tests (Listening, Reading, Writing, Speaking) - that\'s 350-440 in each. Results from two sittings can be combined under certain conditions.',
      link: { title: 'OET for Doctors', url: 'https://tools.anglotec-ai.com/oet-doctors', desc: 'Doctor-specific prep' }
    },
    {
      keywords: ['oet writing', 'referral letter', 'writing subtest'],
      question: 'How do I write the OET referral letter?',
      answer: 'The OET Writing sub-test requires you to write a letter (usually a referral) based on case notes. Key elements: 1) Read the task carefully, 2) Select relevant information from notes, 3) Use appropriate structure, 4) Write 180-200 words in 45 minutes.',
      link: { title: 'OET Writing Practice', url: 'https://tools.anglotec-ai.com/oet-writing', desc: 'Practice referral letters' }
    },
    {
      keywords: ['oet speaking', 'role play', 'speaking roleplay'],
      question: 'What happens in the OET Speaking test?',
      answer: 'OET Speaking has two role-plays (about 5 minutes each). You play your professional role (nurse/doctor) and the interlocutor plays the patient or carer. You\'ll get a card with the scenario and 3 minutes to prepare.',
      link: { title: 'OET Role-Play Generator', url: 'https://tools.anglotec-ai.com/oet-roleplay', desc: 'Unlimited practice scenarios' }
    },
    {
      keywords: ['oet reading', 'reading part a', 'reading part b', 'reading part c'],
      question: 'What is the OET Reading structure?',
      answer: 'OET Reading has 3 parts: Part A (expeditious reading - 15 mins) - match information from 4 short texts; Part B (careful reading - 45 mins) - 6 short workplace texts with MCQs; Part C (careful reading) - 2 longer texts with MCQs.',
      link: { title: 'OET Reading Practice', url: 'https://tools.anglotec-ai.com/oet-reading', desc: 'Practice all parts' }
    },
    {
      keywords: ['oet listening', 'listening part a', 'listening part b', 'consultation'],
      question: 'What is the OET Listening test?',
      answer: 'OET Listening has 3 parts: Part A (consultation) - 2 consultations with note-completion; Part B (short extracts) - 6 workplace extracts with MCQs; Part C (presentation) - 2 longer presentations/extracts with MCQs.',
      link: { title: 'OET Listening Practice', url: 'https://tools.anglotec-ai.com/oet-listening', desc: 'Audio practice tests' }
    },
    {
      keywords: ['oet booking', 'book oet', 'oet test dates'],
      question: 'How do I book an OET test?',
      answer: 'Book OET at the official OET website (occupationalenglishtest.org). You\'ll need a passport photo ID. Tests are held monthly at venues worldwide. Currently OET on Computer at Home is also available.',
      link: null
    },
    {
      keywords: ['oet results', 'oet score', 'oet grades'],
      question: 'How are OET results graded?',
      answer: 'OET uses letter grades: A (highest, 500), B (350-440), C+ (300-340), C (200-290), D (100-190), E (lowest, 0-90). Most regulators require Grade B (350+) in all sub-tests. Results come out approximately 12 days after the test.',
      link: { title: 'OET Score Guide', url: 'https://tools.anglotec-ai.com/oet-scores', desc: 'Understanding OET grades' }
    },
    {
      keywords: ['oet preparation', 'prepare oet', 'oet study', 'oet tips'],
      question: 'How should I prepare for the OET?',
      answer: 'Best OET prep strategy: 1) Understand the test format first, 2) Practice role-plays daily for Speaking, 3) Write referral letters regularly, 4) Build medical vocabulary, 5) Take timed practice tests, 6) Get feedback from tutors or AI tools.',
      link: { title: 'OET Full Course', url: 'https://tools.anglotec-ai.com/oet-course', desc: 'Complete OET preparation' }
    }
  ],

  // ============================================================
  // OSCE QUESTIONS (10)
  // ============================================================
  osce: [
    {
      keywords: ['what is osce', 'osce exam', 'objective structured clinical examination'],
      question: 'What is an OSCE?',
      answer: 'OSCE stands for Objective Structured Clinical Examination. It\'s a practical exam where you rotate through different stations, each testing specific clinical skills like history taking, physical examination, or practical procedures.',
      link: { title: 'OSCE Guide', url: 'https://tools.anglotec-ai.com/osce-guide', desc: 'Complete OSCE introduction' }
    },
    {
      keywords: ['nmc osce', 'osce for nurses', 'nursing osce', 'osce uk'],
      question: 'What is the NMC OSCE for nurses?',
      answer: 'The NMC OSCE is the final test of competency for internationally educated nurses seeking UK registration. It has 10 stations: 4 APIE (Assessment, Planning, Implementation, Evaluation), 2 skill stations, 2 silent written stations, and 2 pair stations.',
      link: { title: 'NMC OSCE Trainer', url: 'https://tools.anglotec-ai.com/nmc-osce', desc: 'Full NMC OSCE preparation' }
    },
    {
      keywords: ['plab 2', 'plab2', 'plab exam'],
      question: 'What is PLAB 2?',
      answer: 'PLAB 2 (Professional and Linguistic Assessments Board) is a practical OSCE-style exam for international doctors seeking GMC registration. It consists of 16 stations (18 minutes each) testing clinical examination, history taking, communication, and practical skills.',
      link: { title: 'PLAB 2 Trainer', url: 'https://tools.anglotec-ai.com/plab2', desc: 'Complete PLAB 2 prep' }
    },
    {
      keywords: ['osce stations', 'station types', 'api', 'api station'],
      question: 'What are the different OSCE station types?',
      answer: 'Common OSCE station types include: 1) History Taking, 2) Physical Examination, 3) A-E Assessment (Airway, Breathing, Circulation, Disability, Exposure), 4) Practical Procedures (IM injection, catheterisation, etc.), 5) Communication/Breaking Bad News, 6) Prescribing, 7) Data Interpretation.',
      link: { title: 'OSCE Scenario Generator', url: 'https://tools.anglotec-ai.com/osce-scenarios', desc: 'Generate practice stations' }
    },
    {
      keywords: ['osce preparation', 'prepare osce', 'osce study', 'osce tips'],
      question: 'How do I prepare for my OSCE exam?',
      answer: 'OSCE prep tips: 1) Practice EVERY station type repeatedly, 2) Use the Anglotec OSCE Scenario Generator for unlimited practice, 3) Record yourself and review, 4) Practice with peers, 5) Learn the marking criteria, 6) Time yourself strictly, 7) Stay calm and structured on exam day.',
      link: { title: 'OSCE Training Platform', url: 'https://tools.anglotec-ai.com/osce-training', desc: 'Full OSCE preparation' }
    },
    {
      keywords: ['history taking', 'take history', 'patient history'],
      question: 'How do I take a good patient history in OSCE?',
      answer: 'Structure your history with: 1) Introduce yourself, 2) Confirm patient identity, 3) Presenting complaint (OLDCART - Onset, Location, Duration, Character, Aggravating/Alleviating, Radiation, Timing), 4) Past medical history, 5) Drug history/allergies, 6) Family history, 7) Social history (crucial for discharge planning), 8) ICE (Ideas, Concerns, Expectations).',
      link: { title: 'History Taking Trainer', url: 'https://tools.anglotec-ai.com/history-taking', desc: 'Practice histories' }
    },
    {
      keywords: ['physical exam', 'examination station', 'clinical examination'],
      question: 'How do I approach a physical examination station?',
      answer: 'Examination structure: 1) Wash hands and introduce yourself, 2) Explain and gain consent, 3) Position and expose the patient appropriately, 4) Inspect from the end of the bed, 5) Systematic examination (look, feel, percuss, auscultate), 6) Thank the patient and wash hands, 7) Present your findings to the examiner.',
      link: { title: 'Examination Trainer', url: 'https://tools.anglotec-ai.com/examination-trainer', desc: 'All body systems' }
    },
    {
      keywords: ['breaking bad news', 'communication station', 'difficult conversation'],
      question: 'How do I handle breaking bad news stations?',
      answer: 'Use the SPIKES protocol: S - Setting up the interview (private space), P - Perception (what do they know?), I - Invitation (how much do they want to know?), K - Knowledge (give information in chunks), E - Emotions (acknowledge and empathise), S - Strategy and Summary.',
      link: { title: 'Communication Trainer', url: 'https://tools.anglotec-ai.com/communication', desc: 'Practice scenarios' }
    },
    {
      keywords: ['osce marking', 'how marked', 'pass mark', 'osce score'],
      question: 'How is the NMC OSCE marked?',
      answer: 'NMC OSCE stations are marked against specific criteria. Each station is pass/fail. You need to pass ALL stations to pass the OSCE. The APIE stations are linked - you must pass all 4 to pass that section. You get 3 attempts total.',
      link: { title: 'OSCE Marking Guide', url: 'https://tools.anglotec-ai.com/osce-marking', desc: 'Understand the criteria' }
    },
    {
      keywords: ['osce anxiety', 'nervous osce', 'exam stress', 'osce panic'],
      question: 'How do I manage OSCE anxiety?',
      answer: 'Manage anxiety by: 1) Being over-prepared (practice until it\'s automatic), 2) Using positive visualisation, 3) Breathing exercises before each station, 4) Having a structured approach for every station type, 5) Remembering the examiner wants you to pass, 6) If you make a mistake, move on quickly.',
      link: { title: 'OSCE Confidence Builder', url: 'https://tools.anglotec-ai.com/osce-confidence', desc: 'Mental preparation' }
    }
  ],

  // ============================================================
  // NHS & CAREER QUESTIONS (8)
  // ============================================================
  nhs: [
    {
      keywords: ['band 5 nurse', 'band5', 'newly qualified nurse'],
      question: 'What is a Band 5 Nurse?',
      answer: 'A Band 5 is a newly qualified Registered Nurse in the NHS. It\'s the entry-level grade for registered nurses, with salaries starting around £29,000-£31,000 per year (varies by location with High Cost Area Supplements).',
      link: { title: 'NHS Career Guide', url: 'https://tools.anglotec-ai.com/nhs-careers', desc: 'NHS nursing careers' }
    },
    {
      keywords: ['nhs interview', 'interview questions', 'nurse interview'],
      question: 'What questions are asked in NHS nurse interviews?',
      answer: 'Common NHS interview questions: 1) Why do you want to work for the NHS? 2) Tell us about a time you dealt with a difficult patient, 3) How do you handle stress? 4) Describe a time you showed compassion, 5) How do you prioritise your workload? 6) What do you know about the 6 Cs? Use the STAR method for behavioural questions.',
      link: { title: 'NHS Interview Bank', url: 'https://tools.anglotec-ai.com/nhs-interviews', desc: '500+ interview questions' }
    },
    {
      keywords: ['6 cs', 'six cs', 'nursing values', 'compassion', 'care'],
      question: 'What are the 6 Cs of Nursing?',
      answer: 'The 6 Cs are: Care (core of nursing), Compassion (showing empathy), Competence (having the skills), Communication (effective interaction), Courage (doing the right thing), and Commitment (dedication to patients and colleagues).',
      link: null
    },
    {
      keywords: ['nhs cv', 'nursing cv', 'cv builder', 'resume'],
      question: 'How do I write a good NHS nursing CV?',
      answer: 'Your NHS CV should include: 1) NMC PIN number, 2) Clinical placements and experience, 3) Key skills (medication administration, wound care, etc.), 4) Relevant certifications (BLS, ALERT, etc.), 5) Use the NHS format if applying via TRAC Jobs, 6) Tailor to the specific job description.',
      link: { title: 'NHS CV Builder', url: 'https://tools.anglotec-ai.com/nhs-cv', desc: 'Create your nursing CV' }
    },
    {
      keywords: ['nmc registration', 'register nmc', 'nmc pin'],
      question: 'How do I get NMC registration?',
      answer: 'Steps for NMC registration: 1) Complete eligibility check on NMC website, 2) Pass English language test (IELTS/OET), 3) Pass CBT (Computer Based Test), 4) Get a nursing job offer in the UK, 5) Pass OSCE, 6) Complete registration and pay fee, 7) Receive your NMC PIN.',
      link: { title: 'NMC Registration Guide', url: 'https://tools.anglotec-ai.com/nmc-guide', desc: 'Step-by-step guide' }
    },
    {
      keywords: ['cbt', 'computer based test', 'nmc cbt'],
      question: 'What is the NMC CBT?',
      answer: 'The CBT (Computer Based Test) is Part 1 of NMC registration. It\'s a 120-question multiple choice exam testing your professional nursing knowledge. You have 4 hours to complete it. You can take it at Pearson VUE test centres worldwide. Pass mark is typically around 68%.',
      link: { title: 'CBT Question Bank', url: 'https://tools.anglotec-ai.com/nmc-cbt', desc: 'Practice questions' }
    },
    {
      keywords: ['nhs pay', 'nhs salary', 'nurse pay scale', 'agenda for change'],
      question: 'What is the NHS pay scale?',
      answer: 'NHS uses Agenda for Change (AfC) pay bands: Band 5 (Newly qualified RN): ~£29,000-£36,000; Band 6 (Charge Nurse/Specialist): ~£36,000-£42,000; Band 7 (Advanced Nurse Practitioner): ~£43,000-£50,000; Band 8a (Matron): ~£51,000-£58,000. London and surrounding areas get additional High Cost Area Supplement.',
      link: null
    },
    {
      keywords: ['working nhs', 'nhs culture', 'nhs as foreign nurse', 'overseas nurse'],
      question: 'What is it like working as a foreign nurse in the NHS?',
      answer: 'Working in the NHS as an international nurse: Pros - Structured training, clear career progression, diverse workforce, good annual leave. Challenges - Culture adjustment, different documentation systems, high workload initially. Most trusts have preceptorship programmes and international nurse support networks.',
      link: { title: 'International Nurse Guide', url: 'https://tools.anglotec-ai.com/international-nurses', desc: 'Guide for overseas nurses' }
    }
  ],

  // ============================================================
  // LANGUAGE LEARNING QUESTIONS (7)
  // ============================================================
  language: [
    {
      keywords: ['improve english', 'learn english', 'english practice'],
      question: 'How can I improve my medical English?',
      answer: 'Best ways to improve medical English: 1) Practice with our 12-Language AI Tutor daily, 2) Listen to medical podcasts, 3) Watch UK medical dramas with subtitles, 4) Read NICE guidelines, 5) Practice explaining conditions to patients, 6) Learn common medical idioms and phrasal verbs.',
      link: { title: '12-Language AI Tutor', url: 'https://tools.anglotec-ai.com/ai-tutor', desc: 'Practice medical English' }
    },
    {
      keywords: ['medical vocabulary', 'healthcare words', 'medical terms'],
      question: 'What medical vocabulary should I learn?',
      answer: 'Key vocabulary areas: 1) Anatomy and body systems, 2) Common conditions and diseases, 3) Medications and prescribing terms, 4) Procedures and investigations, 5) Patient communication phrases, 6) Abbreviations (BP, HR, RR, SpO2, etc.), 7) Mental health terminology.',
      link: { title: 'Medical Vocabulary', url: 'https://tools.anglotec-ai.com/vocabulary', desc: 'Essential healthcare words' }
    },
    {
      keywords: ['british accent', 'uk accent', 'pronunciation'],
      question: 'Do I need a British accent for my exams?',
      answer: 'No! Examiners are trained to understand a variety of accents. What matters is clarity, appropriate intonation, and being easily understood. Focus on clear pronunciation rather than trying to change your natural accent.',
      link: null
    },
    {
      keywords: ['medical idioms', 'english idioms', 'phrasal verbs'],
      question: 'What medical English idioms should I know?',
      answer: 'Common medical idioms: "under the weather" (unwell), "run some tests" (order investigations), "keep an eye on" (monitor), "rule out" (exclude a diagnosis), "follow up" (review later), "break out in" (suddenly develop), "come down with" (become ill), "fight off" (recover from infection).',
      link: { title: 'Medical Idioms Guide', url: 'https://tools.anglotec-ai.com/idioms', desc: 'Learn healthcare idioms' }
    },
    {
      keywords: ['ielts vocabulary', 'academic words', 'word list'],
      question: 'What vocabulary do I need for IELTS?',
      answer: 'Build vocabulary across: 1) Education and learning, 2) Health and medicine, 3) Environment, 4) Technology, 5) Government and society, 6) Work and employment, 7) Family and relationships. Use academic word lists (AWL) and practice using words in context.',
      link: { title: 'IELTS Vocabulary Builder', url: 'https://tools.anglotec-ai.com/ielts-vocab', desc: 'Targeted word lists' }
    },
    {
      keywords: ['speaking fluency', 'speak better', 'fluency tips'],
      question: 'How can I improve my speaking fluency?',
      answer: 'Fluency tips: 1) Practice speaking EVERY day, 2) Don\'t worry about perfection - focus on communication, 3) Use fillers naturally ("That\'s a good question...", "Let me think..."), 4) Record yourself and listen back, 5) Shadow native speakers, 6) Use our AI Tutor for unlimited practice.',
      link: { title: 'Fluency Trainer', url: 'https://tools.anglotec-ai.com/fluency', desc: 'Daily fluency practice' }
    },
    {
      keywords: ['grammar', 'english grammar', 'common mistakes'],
      question: 'What grammar mistakes should I avoid?',
      answer: 'Common grammar mistakes: 1) Articles (a/an/the) - especially with medical conditions, 2) Prepositions ("suffer FROM", "diagnosed WITH"), 3) Tense consistency in writing, 4) Subject-verb agreement, 5) Countable vs uncountable nouns, 6) Conditional sentences.',
      link: { title: 'Grammar Fixer', url: 'https://tools.anglotec-ai.com/grammar', desc: 'Common error correction' }
    }
  ],

  // ============================================================
  // AI TOOLS & PROMPTS QUESTIONS (5)
  // ============================================================
  ai: [
    {
      keywords: ['ai prompts', 'prompt engineering', 'chatgpt prompts', 'ai for study'],
      question: 'How can I use AI to study for my exams?',
      answer: 'AI study strategies: 1) Use ChatGPT to generate practice questions, 2) Ask AI to explain complex medical topics simply, 3) Practice role-plays with our AI tutor, 4) Get instant feedback on your writing, 5) Create mnemonics and memory aids, 6) Generate patient scenarios for OSCE practice.',
      link: { title: 'AI Prompt Library', url: 'https://tools.anglotec-ai.com/prompts', desc: '500+ study prompts' }
    },
    {
      keywords: ['free trial', 'try free', 'trial', 'free account', 'signup', 'sign up'],
      question: 'Can I try Anglotec tools for free?',
      answer: 'Yes! We offer free trials on all our platforms. You can: 1) Try the OSCE Scenario Generator with 5 free scenarios, 2) Use the OET Role-Play Generator for free, 3) Access sample IELTS Writing feedback, 4) Try the AI Tutor for 7 days free. No credit card required!',
      link: { title: 'Free Trial Signup', url: 'https://tools.anglotec-ai.com/signup', desc: 'Start your free trial' }
    },
    {
      keywords: ['pricing', 'cost', 'how much', 'subscription', 'price', 'paid'],
      question: 'How much do Anglotec tools cost?',
      answer: 'Anglotec offers flexible pricing: Free tier with limited access; Premium plans starting from £9.99/month for individual tools; Full Platform Access at £29.99/month (best value); Group discounts available for training centres. All plans include a free trial.',
      link: { title: 'Pricing Page', url: 'https://tools.anglotec-ai.com/pricing', desc: 'View all plans' }
    },
    {
      keywords: ['contact', 'email', 'phone', 'support', 'help', 'human'],
      question: 'How can I contact Anglotec support?',
      answer: 'You can reach us at: Email: support@anglotec-ai.com; Live Chat: Available on all pages (bottom right); WhatsApp: +44 xxx xxx xxxx; Response time is usually within 2 hours during UK business hours.',
      link: null
    },
    {
      keywords: ['about anglotec', 'who are you', 'what is anglotec', 'company'],
      question: 'What is Anglotec?',
      answer: 'Anglotec is an AI-powered education platform designed for healthcare professionals preparing for English language exams and clinical assessments. We combine artificial intelligence with medical expertise to help nurses, doctors, and medical students pass their exams and build successful UK careers.',
      link: { title: 'About Anglotec', url: 'https://tools.anglotec-ai.com/about', desc: 'Learn more about us' }
    }
  ]
};

// Flatten all questions for easy searching
function getAllQuestions() {
  const all = [];
  Object.keys(QADB).forEach(category => {
    QADB[category].forEach(qa => {
      qa.category = category;
      all.push(qa);
    });
  });
  return all;
}

// Export for use in chatbot.js
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { QADB, getAllQuestions };
}
