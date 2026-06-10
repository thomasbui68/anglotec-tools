"""
AngloTec Study Bot - Responses & Content Database
====================================================
All responses, study tips, vocabulary words, and content generators.
Every response includes a subtle AngloTec tools promotion.
"""

import random
from datetime import datetime
from config import (
    ANGLOTEC_URLS,
    ANGLOTEC_FOOTER,
    ANGLOTEC_FOOTER_SHORT,
    MIN_STUDY_WEEKS,
    MAX_STUDY_WEEKS,
    DEFAULT_STUDY_WEEKS,
)


# ============================================================
# WELCOME & MENU
# ============================================================

def get_welcome_message(first_name: str) -> str:
    """Generate personalized welcome message."""
    return (
        f"👋 <b>Hello, {first_name}!</b>\n\n"
        f"Welcome to <b>AngloTec Study Bot</b> — your free companion for "
        f"IELTS, OET & OSCE exam preparation! 🎯\n\n"
        f"📚 <b>What I can do:</b>\n"
        f"• IELTS band score calculator\n"
        f"• Daily vocabulary & quizzes\n"
        f"• Personalized study plans\n"
        f"• OET speaking & writing tips\n"
        f"• OSCE station preparation\n"
        f"• NHS interview guidance\n\n"
        f"📱 <b>Quick Commands:</b>\n"
        f"🔹 /ielts — IELTS resources\n"
        f"🔹 /oet — OET resources\n"
        f"🔹 /osce — OSCE resources\n"
        f"🔹 /quiz — Daily quiz\n"
        f"🔹 /vocab — Word of the day\n"
        f"🔹 /tips — Study tips\n"
        f"🔹 /calc — Band calculator\n"
        f"🔹 /studyplan — Study planner\n"
        f"🔹 /help — All commands\n\n"
        f"🎓 <b>Ready to start?</b> Try /quiz or /vocab now!"
        f"{ANGLOTEC_FOOTER}"
    )


def get_help_message() -> str:
    """Return the full help message with all commands."""
    return (
        "📋 <b>AngloTec Study Bot — Command Guide</b>\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📚 <b>Study Resources</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /ielts — IELTS study resources & free calculator\n"
        "🔹 /oet — OET study resources & practice tools\n"
        "🔹 /osce — OSCE station resources & generator\n"
        "🔹 /nhs — NHS career resources & interview bank\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 <b>Daily Learning</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /quiz — Daily IELTS/OET quiz question\n"
        "🔹 /vocab — Daily vocabulary word with definition\n"
        "🔹 /tips — 3 random study tips\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🛠️ <b>Tools</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /calc [L] [R] [W] [S] — IELTS band score calculator\n"
        "   <i>Example: /calc 7.0 6.5 7.5 8.0</i>\n"
        "🔹 /studyplan [weeks] — Generate personalized study plan\n"
        "   <i>Example: /studyplan 8</i>\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "📬 <b>Subscription</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /subscribe — Daily study tips in your inbox\n"
        "🔹 /unsubscribe — Stop daily tips\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚙️ <b>General</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🔹 /start — Welcome message & menu\n"
        "🔹 /help — Show this help message\n\n"
        "💡 <b>Tip:</b> Add me to any study group and I work automatically!"
        f"{ANGLOTEC_FOOTER}"
    )


# ============================================================
# IELTS RESOURCES
# ============================================================

def get_ielts_resources() -> str:
    """Return IELTS study resources with subtle tool promotion."""
    sections = [
        (
            "📝 <b>IELTS Writing Tips</b>",
            [
                "✓ Task 1: Spend 20 mins. Describe trends, compare data points.",
                "✓ Task 2: Spend 40 mins. Plan 5 mins before writing.",
                "✓ Use linking words: furthermore, nevertheless, consequently.",
                "✓ Aim for 150 words (Task 1) and 250 words (Task 2).",
                "✓ Practice with timed essays every other day.",
            ],
        ),
        (
            "🎧 <b>IELTS Listening Tips</b>",
            [
                "✓ Read questions BEFORE the audio plays.",
                "✓ Underline keywords in each question.",
                "✓ Watch out for distractors (speaker changes answer).",
                "✓ Write answers in ALL CAPS to avoid spelling issues.",
                "✓ Check answers in the 10-min transfer time.",
            ],
        ),
        (
            "📖 <b>IELTS Reading Tips</b>",
            [
                "✓ Skim passage in 2-3 mins, then scan for answers.",
                "✓ Match question type to strategy (TFNG vs matching).",
                "✓ Don't spend more than 1.5 mins per question.",
                "✓ For TFNG: look for evidence, not your own knowledge.",
                "✓ Practice reading academic articles (The Guardian, BBC).",
            ],
        ),
        (
            "🗣️ <b>IELTS Speaking Tips</b>",
            [
                "✓ Part 1: Give 2-3 sentence answers, be natural.",
                "✓ Part 2: Use the 1-min prep time to jot down key points.",
                "✓ Part 2 structure: introduction → main points → conclusion.",
                "✓ Part 3: Give opinions + reasons + examples.",
                "✓ Record yourself daily and review for fluency issues.",
            ],
        ),
    ]

    chosen = random.choice(sections)
    tips_text = "\n".join(chosen[1])

    return (
        f"🎯 <b>IELTS Study Resources</b>\n\n"
        f"{chosen[0]}\n"
        f"{tips_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🧮 <b>Free IELTS Band Calculator</b>\n"
        f"Calculate your overall band instantly:\n"
        f"👉 {ANGLOTEC_URLS['ielts_calculator']}\n\n"
        f"📅 <b>Study Planner</b> — Create your free plan:\n"
        f"👉 {ANGLOTEC_URLS['study_planner']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# OET RESOURCES
# ============================================================

def get_oet_resources() -> str:
    """Return OET study resources with subtle tool promotion."""
    tips = [
        (
            "🗣️ <b>OET Speaking: Role Play Tips</b>",
            [
                "✓ Start with empathy: 'I understand you're concerned about...'",
                "✓ Use the 3-minute prep to underline key tasks on card.",
                "✓ Always explain medical terms in plain English.",
                "✓ Structure: rapport → information → clarification → close.",
                "✓ Practice with a partner — timing is everything!",
            ],
        ),
        (
            "📝 <b>OET Writing: Referral Letter Tips</b>",
            [
                "✓ Read ALL case notes before planning (5 mins).",
                "✓ Group information logically: history → findings → plan.",
                "✓ Omit irrelevant details (e.g., patient's hobbies).",
                "✓ Use appropriate medical abbreviations (BP, HR, WBC).",
                "✓ Always include a clear purpose in the opening line.",
            ],
        ),
        (
            "🎧 <b>OET Listening Tips</b>",
            [
                "✓ Part A: Fill in notes — write answers as you listen.",
                "✓ Part B: Focus on workplace conversations and concerns.",
                "✓ Part C: Pay attention to speaker opinions and attitudes.",
                "✓ Write answers in the gap immediately — no transfer time!",
                "✓ Practice with medical podcasts and lectures.",
            ],
        ),
        (
            "📖 <b>OET Reading Tips</b>",
            [
                "✓ Part A: Fast extraction — 15 mins for 4 short texts.",
                "✓ Part B: Focus on gist — workplace communications.",
                "✓ Part C: Detailed comprehension — medical articles.",
                "✓ Skim first, scan for keywords, then read in detail.",
                "✓ Time management: 15 + 20 + 25 mins for Parts A/B/C.",
            ],
        ),
    ]

    chosen = random.choice(tips)
    tips_text = "\n".join(chosen[1])

    return (
        f"🏥 <b>OET Study Resources</b>\n\n"
        f"{chosen[0]}\n"
        f"{tips_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🩺 <b>Free OET Practice Tools</b>\n"
        f"Role-play scenarios & writing practice:\n"
        f"👉 {ANGLOTEC_URLS['oet_practice']}\n\n"
        f"📅 <b>Study Planner</b> — Create your free plan:\n"
        f"👉 {ANGLOTEC_URLS['study_planner']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# OSCE RESOURCES
# ============================================================

OSCE_STATIONS = [
    {
        "type": "History Taking",
        "description": "Take a focused history from a patient presenting with a specific complaint.",
        "tips": [
            "Start with open questions: 'Tell me what brought you in today.'",
            "Use the SOCRATES method for pain: Site, Onset, Character, Radiation, Associations, Time, Exacerbating/Relieving, Severity.",
            "Screen for red flags relevant to the presenting complaint.",
            "Check ICE: Ideas, Concerns, Expectations.",
            "Summarize back to the patient before moving to examination.",
        ],
    },
    {
        "type": "Physical Examination",
        "description": "Perform a structured physical examination on a simulated patient.",
        "tips": [
            "Always wash hands and introduce yourself — even in practice!",
            "Expose and position the patient appropriately.",
            "Inspect → Palpate → Percuss → Auscultate (for most systems).",
            "Verbally narrate what you're doing for the examiner.",
            "Finish by thanking the patient and summarizing findings.",
        ],
    },
    {
        "type": "Communication & Counselling",
        "description": "Communicate sensitive information or counsel a patient/family member.",
        "tips": [
            "Use the SPIKES model for breaking bad news.",
            "Show empathy: 'I can see this is difficult for you.'",
            "Check understanding: 'Can you tell me in your own words what you understood?'",
            "Give information in small chunks, check after each.",
            "Offer support and next steps.",
        ],
    },
    {
        "type": "Prescription / Drug Chart",
        "description": "Write a prescription or complete a drug chart accurately.",
        "tips": [
            "Double-check drug name, dose, route, and frequency.",
            "Check for allergies and contraindications.",
            "Include your name, signature, date, and GMC/NMC number.",
            "Write clearly — illegible prescriptions are a safety risk.",
            "Know common dosing: paracetamol 1g QDS, amoxicillin 500mg TDS.",
        ],
    },
    {
        "type": "Emergency / A-E Assessment",
        "description": "Assess and manage an acutely unwell patient using the ABCDE approach.",
        "tips": [
            "Always Airway first — if airway isn't patent, nothing else matters.",
            "Call for help early if the patient is deteriorating.",
            "Treat as you find: don't move to next step without stabilizing.",
            "Use the SBAR handover when referring to seniors.",
            "Document everything and reassess frequently.",
        ],
    },
    {
        "type": "Data Interpretation",
        "description": "Interpret ECGs, blood results, imaging, or other clinical data.",
        "tips": [
            "ECG: Rate → Rhythm → Axis → Intervals → Morphology.",
            "Bloods: Look at trends, not isolated values.",
            "Chest X-ray: Check patient details, rotation, inspiration, exposure.",
            "Always correlate findings with the clinical picture.",
            "State your interpretation confidently, then your management plan.",
        ],
    },
    {
        "type": "Practical Procedure",
        "description": "Demonstrate a clinical procedure (cannulation, ABG, suturing, etc.).",
        "tips": [
            "Explain the procedure and obtain verbal consent.",
            "Position the patient and yourself correctly.",
            "Maintain aseptic technique throughout.",
            "Talk through each step — the examiner can't read your mind.",
            "Dispose of sharps safely and document the procedure.",
        ],
    },
]


def get_osce_resources() -> str:
    """Return OSCE resources with subtle tool promotion."""
    station = random.choice(OSCE_STATIONS)
    tips_text = "\n".join(f"✓ {tip}" for tip in station["tips"])

    return (
        f"🩺 <b>OSCE Preparation Resources</b>\n\n"
        f"📋 <b>Station Type: {station['type']}</b>\n"
        f"<i>{station['description']}</i>\n\n"
        f"💡 <b>Top Tips:</b>\n"
        f"{tips_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 <b>Free OSCE Scenario Generator</b>\n"
        f"Generate unlimited practice scenarios:\n"
        f"👉 {ANGLOTEC_URLS['osce_generator']}\n\n"
        f"📅 <b>Study Planner</b> — Plan your OSCE prep:\n"
        f"👉 {ANGLOTEC_URLS['study_planner']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# NHS RESOURCES
# ============================================================

def get_nhs_resources() -> str:
    """Return NHS career resources with subtle tool promotion."""
    resources = [
        (
            "🌐 <b>NHS Values — 6 Core Principles</b>",
            [
                "1️⃣ Working together for patients",
                "2️⃣ Respect and dignity",
                "3️⃣ Commitment to quality of care",
                "4️⃣ Compassion",
                "5️⃣ Improving lives",
                "6️⃣ Everyone counts",
            ],
            "Memorize these — they come up in every NHS interview!",
        ),
        (
            "💼 <b>Common NHS Interview Questions</b>",
            [
                "❓ 'Why do you want to work for the NHS?'",
                "❓ 'Tell us about a time you dealt with a difficult patient.'",
                "❓ 'How do you handle stress in a clinical environment?'",
                "❓ 'Describe a situation where you showed teamwork.'",
                "❓ 'How would you handle a colleague making a mistake?'",
            ],
            "Use the STAR method: Situation, Task, Action, Result.",
        ),
        (
            "📋 <b>NHS Career Pathway (Overseas Nurses)</b>",
            [
                "1️⃣ Pass IELTS/OET (required scores)",
                "2️⃣ NMC registration / OSCE pass",
                "3️⃣ CBT (Computer Based Test)",
                "4️⃣ Job offer from NHS Trust",
                "5️⃣ Certificate of Sponsorship (CoS)",
                "6️⃣ Visa application & arrival",
                "7️⃣ NMC PIN activation",
            ],
            "Each Trust has its own onboarding — research yours!",
        ),
        (
            "📝 <b>NHS Adaptation Tips</b>",
            [
                "✓ Familiarize yourself with NHS Number system",
                "✓ Learn the NEWS2 scoring system",
                "✓ Understand SBAR handover format",
                "✓ Know your escalation pathways",
                "✓ Join your Trust's Facebook/WhatsApp support group",
            ],
            "Adaptation programs usually last 6-12 months.",
        ),
    ]

    chosen = random.choice(resources)
    items_text = "\n".join(chosen[1])

    return (
        f"🏥 <b>NHS Career Resources</b>\n\n"
        f"{chosen[0]}\n"
        f"{items_text}\n\n"
        f"💡 <i>{chosen[2]}</i>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 <b>Free NHS Interview Question Bank</b>\n"
        f"100+ questions with model answers:\n"
        f"👉 {ANGLOTEC_URLS['nhs_interview']}\n\n"
        f"📝 <b>OSCE Scenario Generator</b> — Practice stations:\n"
        f"👉 {ANGLOTEC_URLS['osce_generator']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# VOCABULARY DATABASE (300+ words)
# ============================================================

VOCABULARY = [
    {"word": "Abate", "pos": "verb", "meaning": "To become less intense or widespread", "example": "The storm showed no signs of abating.", "ielts": True},
    {"word": "Aberration", "pos": "noun", "meaning": "A departure from what is normal or expected", "example": "A temporary aberration in the data.", "ielts": True},
    {"word": "Abridge", "pos": "verb", "meaning": "To shorten without losing the sense", "example": "The book was abridged for radio.", "ielts": True},
    {"word": "Abstain", "pos": "verb", "meaning": "To restrain oneself from doing something", "example": "He abstained from alcohol for a month.", "ielts": True},
    {"word": "Abstract", "pos": "adjective", "meaning": "Existing in thought rather than physical form", "example": "The concept of time is abstract.", "ielts": True},
    {"word": "Abundant", "pos": "adjective", "meaning": "Existing in large quantities", "example": "The region has abundant wildlife.", "ielts": True},
    {"word": "Accede", "pos": "verb", "meaning": "To agree to a demand or request", "example": "He acceded to their demands.", "ielts": True},
    {"word": "Accelerate", "pos": "verb", "meaning": "To begin to move more quickly", "example": "The car accelerated down the road.", "ielts": True},
    {"word": "Accessible", "pos": "adjective", "meaning": "Easy to approach or use", "example": "The museum is wheelchair accessible.", "ielts": True},
    {"word": "Acclaim", "pos": "noun", "meaning": "Enthusiastic and public praise", "example": "The film received critical acclaim.", "ielts": True},
    {"word": "Accommodate", "pos": "verb", "meaning": "To provide lodging or sufficient space for", "example": "The hotel can accommodate 200 guests.", "ielts": True},
    {"word": "Accompany", "pos": "verb", "meaning": "To go somewhere with someone", "example": "She accompanied me to the hospital.", "oet": True},
    {"word": "Accumulate", "pos": "verb", "meaning": "To gather together or acquire an increasing number of", "example": "Toxic chemicals accumulate in the body.", "ielts": True},
    {"word": "Adept", "pos": "adjective", "meaning": "Very skilled at something", "example": "She is adept at managing difficult patients.", "oet": True},
    {"word": "Adhere", "pos": "verb", "meaning": "To stick fast to a surface or substance", "example": "The bandage will adhere to the skin.", "ielts": True},
    {"word": "Adjacent", "pos": "adjective", "meaning": "Next to or adjoining something else", "example": "The room adjacent to the ward.", "oet": True},
    {"word": "Adverse", "pos": "adjective", "meaning": "Preventing success or development; harmful", "example": "The drug had adverse side effects.", "oet": True},
    {"word": "Advocate", "pos": "noun/verb", "meaning": "A person who publicly supports a cause / to recommend", "example": "She advocates for patient rights.", "ielts": True},
    {"word": "Aesthetic", "pos": "adjective", "meaning": "Concerned with beauty or taste", "example": "The building has great aesthetic appeal.", "ielts": True},
    {"word": "Affluent", "pos": "adjective", "meaning": "Having a great deal of money; wealthy", "example": "An affluent neighborhood.", "ielts": True},
    {"word": "Aggregate", "pos": "noun/verb", "meaning": "A whole formed by combining several elements", "example": "The aggregate of consumer spending.", "ielts": True},
    {"word": "Aggressive", "pos": "adjective", "meaning": "Ready to attack or confront", "example": "The tumor is aggressive but treatable.", "oet": True},
    {"word": "Agile", "pos": "adjective", "meaning": "Able to move quickly and easily", "example": "An agile mind adapts to change.", "ielts": True},
    {"word": "Ailment", "pos": "noun", "meaning": "An illness, typically a minor one", "example": "She treats minor ailments at the clinic.", "oet": True},
    {"word": "Alleviate", "pos": "verb", "meaning": "To make suffering or a problem less severe", "example": "The medication alleviated his pain.", "oet": True},
    {"word": "Ambiguous", "pos": "adjective", "meaning": "Open to more than one interpretation", "example": "The instructions were ambiguous.", "ielts": True},
    {"word": "Ambitious", "pos": "adjective", "meaning": "Having a strong desire to succeed", "example": "An ambitious project to build new hospitals.", "ielts": True},
    {"word": "Amend", "pos": "verb", "meaning": "To make minor changes to improve", "example": "The report was amended before publication.", "ielts": True},
    {"word": "Ample", "pos": "adjective", "meaning": "Enough or more than enough; plentiful", "example": "There is ample evidence to support this.", "ielts": True},
    {"word": "Analogy", "pos": "noun", "meaning": "A comparison between two things", "example": "He used an analogy to explain the process.", "ielts": True},
    {"word": "Analyze", "pos": "verb", "meaning": "To examine in detail for interpretation", "example": "We need to analyze the blood results.", "oet": True},
    {"word": "Anecdote", "pos": "noun", "meaning": "A short amusing or interesting story", "example": "She began with a personal anecdote.", "ielts": True},
    {"word": "Anomaly", "pos": "noun", "meaning": "Something that deviates from what is standard", "example": "The anomaly in the test results.", "ielts": True},
    {"word": "Anticipate", "pos": "verb", "meaning": "To regard as probable; expect", "example": "We anticipate a full recovery.", "oet": True},
    {"word": "Apprehensive", "pos": "adjective", "meaning": "Anxious or fearful about the future", "example": "The patient felt apprehensive about surgery.", "oet": True},
    {"word": "Appropriate", "pos": "adjective", "meaning": "Suitable or proper in the circumstances", "example": "Use appropriate language with patients.", "oet": True},
    {"word": "Arbitrary", "pos": "adjective", "meaning": "Based on random choice rather than reason", "example": "The decision seemed arbitrary.", "ielts": True},
    {"word": "Arduous", "pos": "adjective", "meaning": "Involving or requiring strenuous effort", "example": "The journey to registration is arduous.", "ielts": True},
    {"word": "Articulate", "pos": "verb/adjective", "meaning": "To express clearly / having clear speech", "example": "She articulated her concerns clearly.", "ielts": True},
    {"word": "Ascertain", "pos": "verb", "meaning": "To find something out for certain", "example": "We need to ascertain the cause of the pain.", "oet": True},
    {"word": "Assess", "pos": "verb", "meaning": "To evaluate or estimate the nature of", "example": "The nurse assessed the wound daily.", "oet": True},
    {"word": "Attribute", "pos": "verb/noun", "meaning": "To regard as being caused by / a quality", "example": "She attributes her success to hard work.", "ielts": True},
    {"word": "Benevolent", "pos": "adjective", "meaning": "Well-meaning and kindly", "example": "A benevolent organization helping refugees.", "ielts": True},
    {"word": "Bolster", "pos": "verb", "meaning": "To support or strengthen", "example": "The evidence bolstered her argument.", "ielts": True},
    {"word": "Breach", "pos": "noun/verb", "meaning": "An act of breaking a law or agreement", "example": "A breach of patient confidentiality.", "oet": True},
    {"word": "Brief", "pos": "adjective/verb", "meaning": "Short in duration / to instruct", "example": "Keep your answers brief and clear.", "ielts": True},
    {"word": "Candid", "pos": "adjective", "meaning": "Truthful and straightforward; frank", "example": "To be candid, the prognosis is poor.", "oet": True},
    {"word": "Capacity", "pos": "noun", "meaning": "The maximum amount something can contain", "example": "The hospital is at full capacity.", "oet": True},
    {"word": "Chronic", "pos": "adjective", "meaning": "Persisting for a long time or constantly recurring", "example": "She suffers from chronic back pain.", "oet": True},
    {"word": "Clarify", "pos": "verb", "meaning": "To make a statement or situation less confused", "example": "Could you clarify your symptoms?", "oet": True},
    {"word": "Coherent", "pos": "adjective", "meaning": "Logical and consistent; easy to understand", "example": "Write a coherent essay with clear paragraphs.", "ielts": True},
    {"word": "Cohesive", "pos": "adjective", "meaning": "Characterized by or causing cohesion", "example": "Use cohesive devices in your writing.", "ielts": True},
    {"word": "Collapse", "pos": "verb/noun", "meaning": "To fall down or give way suddenly", "example": "The patient collapsed in the corridor.", "oet": True},
    {"word": "Collate", "pos": "verb", "meaning": "To collect and combine in proper order", "example": "Collate all test results for review.", "oet": True},
    {"word": "Comparable", "pos": "adjective", "meaning": "Able to be likened to another; similar", "example": "The results are comparable to last year.", "ielts": True},
    {"word": "Compatible", "pos": "adjective", "meaning": "Able to exist together without conflict", "example": "Check if medications are compatible.", "oet": True},
    {"word": "Compensate", "pos": "verb", "meaning": "To make up for something unwelcome by exerting an opposite force", "example": "The body compensates for blood loss.", "oet": True},
    {"word": "Compile", "pos": "verb", "meaning": "To produce by assembling information", "example": "Compile a list of all medications.", "oet": True},
    {"word": "Complement", "pos": "verb/noun", "meaning": "To add to something in a way that improves it", "example": "The two systems complement each other.", "ielts": True},
    {"word": "Comprehensive", "pos": "adjective", "meaning": "Complete and including all or nearly all elements", "example": "A comprehensive medical history.", "oet": True},
    {"word": "Compromise", "pos": "verb/noun", "meaning": "To settle a dispute by mutual concession", "example": "We need to find a compromise.", "ielts": True},
    {"word": "Concede", "pos": "verb", "meaning": "To admit that something is true after denying it", "example": "He conceded that she had a valid point.", "ielts": True},
    {"word": "Concise", "pos": "adjective", "meaning": "Giving a lot of information clearly in few words", "example": "Write concise referral letters.", "oet": True},
    {"word": "Concur", "pos": "verb", "meaning": "To be of the same opinion; agree", "example": "The doctors concurred on the diagnosis.", "oet": True},
    {"word": "Confidential", "pos": "adjective", "meaning": "Intended to be kept secret", "example": "Patient records are confidential.", "oet": True},
    {"word": "Conform", "pos": "verb", "meaning": "To comply with rules or standards", "example": "The building does not conform to regulations.", "ielts": True},
    {"word": "Consecutive", "pos": "adjective", "meaning": "Following one another in uninterrupted succession", "example": "Three consecutive days of fever.", "oet": True},
    {"word": "Consensus", "pos": "noun", "meaning": "General agreement among a group", "example": "The team reached a consensus.", "ielts": True},
    {"word": "Consequently", "pos": "adverb", "meaning": "As a result; therefore", "example": "She was ill; consequently, she missed work.", "ielts": True},
    {"word": "Considerable", "pos": "adjective", "meaning": "Notably large in size, amount, or extent", "example": "Considerable progress has been made.", "ielts": True},
    {"word": "Consolidate", "pos": "verb", "meaning": "To combine into a single more effective whole", "example": "Consolidate all findings in one report.", "ielts": True},
    {"word": "Conspicuous", "pos": "adjective", "meaning": "Standing out so as to be clearly visible", "example": "Her absence was conspicuous.", "ielts": True},
    {"word": "Contemplate", "pos": "verb", "meaning": "To look at thoughtfully for a long time", "example": "He contemplated his options carefully.", "ielts": True},
    {"word": "Contemporary", "pos": "adjective", "meaning": "Living or occurring at the same time", "example": "Contemporary art from the 21st century.", "ielts": True},
    {"word": "Controversial", "pos": "adjective", "meaning": "Giving rise to public disagreement", "example": "A controversial new healthcare policy.", "ielts": True},
    {"word": "Conventional", "pos": "adjective", "meaning": "Based on what is generally done or believed", "example": "Conventional treatment methods.", "ielts": True},
    {"word": "Convey", "pos": "verb", "meaning": "To make an idea or feeling known", "example": "Her tone conveyed concern.", "ielts": True},
    {"word": "Corroborate", "pos": "verb", "meaning": "To confirm or give support to a statement", "example": "The witness corroborated his account.", "ielts": True},
    {"word": "Criteria", "pos": "noun", "meaning": "Principles or standards by which something is judged", "example": "Meet all the entry criteria.", "ielts": True},
    {"word": "Crucial", "pos": "adjective", "meaning": "Decisive or critical, especially in the success of something", "example": "Timing is crucial in emergency care.", "oet": True},
    {"word": "Cumulative", "pos": "adjective", "meaning": "Increasing or increased in quantity by successive additions", "example": "The cumulative effect of the medication.", "oet": True},
    {"word": "Debate", "pos": "noun/verb", "meaning": "A formal discussion / to argue about", "example": "The issue is still under debate.", "ielts": True},
    {"word": "Decline", "pos": "verb/noun", "meaning": "To diminish in strength or quality", "example": "A decline in cognitive function.", "oet": True},
    {"word": "Dedicate", "pos": "verb", "meaning": "To devote time and effort to a task", "example": "She dedicated herself to patient care.", "oet": True},
    {"word": "Deficiency", "pos": "noun", "meaning": "A lack or shortage of something", "example": "Vitamin D deficiency is common.", "oet": True},
    {"word": "Degrade", "pos": "verb", "meaning": "To break down or deteriorate", "example": "The condition degrades without treatment.", "ielts": True},
    {"word": "Delegate", "pos": "verb", "meaning": "To entrust a task to another person", "example": "Delegate non-urgent tasks to the team.", "oet": True},
    {"word": "Deliberate", "pos": "adjective/verb", "meaning": "Done consciously and intentionally / to engage in debate", "example": "It was a deliberate choice.", "ielts": True},
    {"word": "Demonstrate", "pos": "verb", "meaning": "To clearly show the existence of something", "example": "Demonstrate the procedure to the patient.", "oet": True},
    {"word": "Denote", "pos": "verb", "meaning": "To be a sign of; indicate", "example": "Red circles denote problem areas.", "ielts": True},
    {"word": "Depict", "pos": "verb", "meaning": "To portray in words or pictures", "example": "The graph depicts a clear trend.", "ielts": True},
    {"word": "Designate", "pos": "verb", "meaning": "To officially assign to a position or role", "example": "She was designated as team leader.", "ielts": True},
    {"word": "Deteriorate", "pos": "verb", "meaning": "To become progressively worse", "example": "His condition began to deteriorate.", "oet": True},
    {"word": "Detrimental", "pos": "adjective", "meaning": "Tending to cause harm", "example": "Smoking is detrimental to health.", "ielts": True},
    {"word": "Deviates", "pos": "verb", "meaning": "To depart from an established course", "example": "The result deviates from the norm.", "ielts": True},
    {"word": "Dexterity", "pos": "noun", "meaning": "Skill in performing tasks, especially with the hands", "example": "Manual dexterity is required for this procedure.", "oet": True},
    {"word": "Diagnosis", "pos": "noun", "meaning": "The identification of an illness or condition", "example": "The diagnosis was confirmed by tests.", "oet": True},
    {"word": "Diligent", "pos": "adjective", "meaning": "Having care and conscientiousness", "example": "She is a diligent student.", "ielts": True},
    {"word": "Diminish", "pos": "verb", "meaning": "To make or become less; decrease", "example": "The swelling began to diminish.", "oet": True},
    {"word": "Discharge", "pos": "verb/noun", "meaning": "To allow someone to leave hospital", "example": "The patient was discharged yesterday.", "oet": True},
    {"word": "Discrepancy", "pos": "noun", "meaning": "A lack of compatibility between two facts", "example": "A discrepancy between the two reports.", "ielts": True},
    {"word": "Discrete", "pos": "adjective", "meaning": "Individually separate and distinct", "example": "The study has three discrete phases.", "ielts": True},
    {"word": "Dispense", "pos": "verb", "meaning": "To distribute or provide a service", "example": "Dispense medication according to the chart.", "oet": True},
    {"word": "Disseminate", "pos": "verb", "meaning": "To spread widely", "example": "Disseminate the new guidelines to all staff.", "oet": True},
    {"word": "Distort", "pos": "verb", "meaning": "To twist out of shape or give a misleading account", "example": "Pain can distort a patient's perception.", "oet": True},
    {"word": "Divergent", "pos": "adjective", "meaning": "Tending to be different or develop in different directions", "example": "Two divergent opinions on treatment.", "ielts": True},
    {"word": "Document", "pos": "verb", "meaning": "To record in written or photographic form", "example": "Document all observations accurately.", "oet": True},
    {"word": "Domain", "pos": "noun", "meaning": "An area of knowledge or activity", "example": "This falls outside my domain of expertise.", "ielts": True},
    {"word": "Dominant", "pos": "adjective", "meaning": "Most important or influential", "example": "The dominant factor in recovery.", "ielts": True},
    {"word": "Drastic", "pos": "adjective", "meaning": "Likely to have a strong or far-reaching effect", "example": "A drastic change in treatment plan.", "ielts": True},
    {"word": "Dubious", "pos": "adjective", "meaning": "Hesitating or doubting", "example": "I am dubious about the results.", "ielts": True},
    {"word": "Elaborate", "pos": "verb/adjective", "meaning": "To develop in detail / complex and detailed", "example": "Could you elaborate on that point?", "ielts": True},
    {"word": "Eloquent", "pos": "adjective", "meaning": "Fluent or persuasive in speaking or writing", "example": "An eloquent presentation.", "ielts": True},
    {"word": "Elusive", "pos": "adjective", "meaning": "Difficult to find, catch, or achieve", "example": "A diagnosis remained elusive.", "oet": True},
    {"word": "Empathy", "pos": "noun", "meaning": "The ability to understand others' feelings", "example": "Show empathy when delivering bad news.", "oet": True},
    {"word": "Empirical", "pos": "adjective", "meaning": "Based on observation or experience", "example": "Empirical evidence supports this theory.", "ielts": True},
    {"word": "Endorse", "pos": "verb", "meaning": "To declare one's public approval of", "example": "The guidelines are endorsed by the NHS.", "ielts": True},
    {"word": "Endure", "pos": "verb", "meaning": "To suffer patiently / to remain in existence", "example": "She endured months of treatment.", "ielts": True},
    {"word": "Enhance", "pos": "verb", "meaning": "To intensify or increase in value", "example": "The new system enhances patient safety.", "ielts": True},
    {"word": "Enumerate", "pos": "verb", "meaning": "To mention a number of things one by one", "example": "Enumerate the side effects to the patient.", "oet": True},
    {"word": "Erratic", "pos": "adjective", "meaning": "Not even or regular in pattern or movement", "example": "Erratic heart rate on the monitor.", "oet": True},
    {"word": "Establish", "pos": "verb", "meaning": "To set up on a permanent basis", "example": "Establish a therapeutic relationship.", "oet": True},
    {"word": "Estimate", "pos": "verb/noun", "meaning": "To roughly calculate a value", "example": "Estimate the time needed for recovery.", "ielts": True},
    {"word": "Ethical", "pos": "adjective", "meaning": "Relating to moral principles", "example": "An ethical dilemma in patient care.", "oet": True},
    {"word": "Evasive", "pos": "adjective", "meaning": "Tending to avoid commitment or self-revelation", "example": "The patient was evasive about symptoms.", "oet": True},
    {"word": "Exacerbate", "pos": "verb", "meaning": "To make a problem worse", "example": "Stress can exacerbate the condition.", "oet": True},
    {"word": "Excerpt", "pos": "noun", "meaning": "A short piece taken from a text", "example": "Read this excerpt and answer questions.", "ielts": True},
    {"word": "Exemplify", "pos": "verb", "meaning": "To be a typical example of", "example": "This case exemplifies the need for early detection.", "ielts": True},
    {"word": "Exhaustive", "pos": "adjective", "meaning": "Comprehensive and thorough", "example": "An exhaustive list of symptoms.", "ielts": True},
    {"word": "Expedite", "pos": "verb", "meaning": "To make a process happen sooner", "example": "We need to expedite the referral.", "oet": True},
    {"word": "Explicit", "pos": "adjective", "meaning": "Stated clearly and in detail", "example": "Give explicit instructions to the patient.", "ielts": True},
    {"word": "Extensive", "pos": "adjective", "meaning": "Covering a large area; wide-ranging", "example": "Extensive research has been conducted.", "ielts": True},
    {"word": "Feasible", "pos": "adjective", "meaning": "Possible to do easily or conveniently", "example": "Is home discharge feasible?", "oet": True},
    {"word": "Fluctuate", "pos": "verb", "meaning": "To rise and fall irregularly in number or amount", "example": "Blood pressure can fluctuate throughout the day.", "oet": True},
    {"word": "Frail", "pos": "adjective", "meaning": "Weak and delicate", "example": "The frail elderly patient needs support.", "oet": True},
    {"word": "Futile", "pos": "adjective", "meaning": "Incapable of producing any useful result", "example": "Further treatment would be futile.", "oet": True},
    {"word": "Gauge", "pos": "verb/noun", "meaning": "To estimate or determine the amount of", "example": "Gauge the patient's pain level.", "ielts": True},
    {"word": "Generic", "pos": "adjective", "meaning": "Characteristic of a whole group; not specific", "example": "Use the generic name of the drug.", "oet": True},
    {"word": "Hinder", "pos": "verb", "meaning": "To make it difficult to do something", "example": "Pain may hinder mobility.", "ielts": True},
    {"word": "Hypothesis", "pos": "noun", "meaning": "A proposed explanation made on limited evidence", "example": "Test the hypothesis with more data.", "ielts": True},
    {"word": "Hypothetical", "pos": "adjective", "meaning": "Based on an imagined situation", "example": "Consider a hypothetical scenario.", "ielts": True},
    {"word": "Illicit", "pos": "adjective", "meaning": "Forbidden by law or rules", "example": "The use of illicit substances.", "ielts": True},
    {"word": "Immune", "pos": "adjective", "meaning": "Resistant to a particular infection", "example": "The body becomes immune after vaccination.", "oet": True},
    {"word": "Imminent", "pos": "adjective", "meaning": "About to happen", "example": "Discharge is imminent.", "oet": True},
    {"word": "Implement", "pos": "verb", "meaning": "To put a decision or plan into effect", "example": "Implement the new care protocol.", "ielts": True},
    {"word": "Implication", "pos": "noun", "meaning": "The conclusion that can be drawn from something", "example": "The implications of this policy are significant.", "ielts": True},
    {"word": "Implicit", "pos": "adjective", "meaning": "Implied though not directly expressed", "example": "Implicit in the guidelines.", "ielts": True},
    {"word": "Inadvertent", "pos": "adjective", "meaning": "Not resulting from deliberate planning", "example": "An inadvertent medication error.", "oet": True},
    {"word": "Incentive", "pos": "noun", "meaning": "A thing that motivates or encourages someone", "example": "Financial incentives for staff.", "ielts": True},
    {"word": "Incidence", "pos": "noun", "meaning": "The occurrence or rate of something", "example": "The incidence of diabetes is rising.", "oet": True},
    {"word": "Inclination", "pos": "noun", "meaning": "A person's natural tendency or urge to act", "example": "She has an inclination towards research.", "ielts": True},
    {"word": "Incoherent", "pos": "adjective", "meaning": "Expressed in an incomprehensible way", "example": "The patient became incoherent.", "oet": True},
    {"word": "Incompatible", "pos": "adjective", "meaning": "Not able to coexist or work together", "example": "These medications are incompatible.", "oet": True},
    {"word": "Inconclusive", "pos": "adjective", "meaning": "Not leading to a firm conclusion", "example": "Test results were inconclusive.", "oet": True},
    {"word": "Incorporate", "pos": "verb", "meaning": "To take in as part of a whole", "example": "Incorporate exercise into your routine.", "ielts": True},
    {"word": "Indicate", "pos": "verb", "meaning": "To point out or show", "example": "Symptoms indicate an infection.", "oet": True},
    {"word": "Indifferent", "pos": "adjective", "meaning": "Having no particular interest or concern", "example": "He seemed indifferent to the news.", "ielts": True},
    {"word": "Indigenous", "pos": "adjective", "meaning": "Originating or occurring naturally in a place", "example": "Indigenous plants of the region.", "ielts": True},
    {"word": "Induce", "pos": "verb", "meaning": "To bring about or give rise to", "example": "The medication may induce drowsiness.", "oet": True},
    {"word": "Inevitable", "pos": "adjective", "meaning": "Certain to happen; unavoidable", "example": "Some side effects are inevitable.", "ielts": True},
    {"word": "Infer", "pos": "verb", "meaning": "To deduce from evidence and reasoning", "example": "What can we infer from this data?", "ielts": True},
    {"word": "Inflammation", "pos": "noun", "meaning": "A localized physical condition with redness and swelling", "example": "Signs of inflammation around the wound.", "oet": True},
    {"word": "Inherent", "pos": "adjective", "meaning": "Existing as a natural or permanent quality", "example": "The inherent risks of surgery.", "ielts": True},
    {"word": "Initiate", "pos": "verb", "meaning": "To cause a process or action to begin", "example": "Initiate treatment immediately.", "oet": True},
    {"word": "Innovative", "pos": "adjective", "meaning": "Introducing new ideas or methods", "example": "An innovative approach to healthcare.", "ielts": True},
    {"word": "Insight", "pos": "noun", "meaning": "The capacity to gain an accurate understanding", "example": "The research provides valuable insight.", "ielts": True},
    {"word": "Integral", "pos": "adjective", "meaning": "Necessary to make a whole complete", "example": "Communication is integral to nursing.", "oet": True},
    {"word": "Integrity", "pos": "noun", "meaning": "The quality of being honest and having strong principles", "example": "Professional integrity is essential.", "ielts": True},
    {"word": "Intricate", "pos": "adjective", "meaning": "Very complicated or detailed", "example": "The intricate workings of the brain.", "ielts": True},
    {"word": "Intrinsic", "pos": "adjective", "meaning": "Belonging naturally; essential", "example": "The intrinsic value of education.", "ielts": True},
    {"word": "Intuitive", "pos": "adjective", "meaning": "Using instinct rather than conscious reasoning", "example": "An intuitive understanding of patients.", "oet": True},
    {"word": "Invalidate", "pos": "verb", "meaning": "To make an argument or point void", "example": "New evidence invalidates the theory.", "ielts": True},
    {"word": "Invariably", "pos": "adverb", "meaning": "In every case or on every occasion", "example": "The plan invariably fails.", "ielts": True},
    {"word": "Investigate", "pos": "verb", "meaning": "To carry out a systematic inquiry", "example": "Investigate the cause of the symptoms.", "oet": True},
    {"word": "Involuntary", "pos": "adjective", "meaning": "Done without will or conscious control", "example": "Involuntary muscle movements.", "oet": True},
    {"word": "Irrefutable", "pos": "adjective", "meaning": "Impossible to deny or disprove", "example": "Irrefutable evidence of improvement.", "ielts": True},
    {"word": "Juxtapose", "pos": "verb", "meaning": "To place close together for contrasting effect", "example": "The essay juxtaposes two viewpoints.", "ielts": True},
    {"word": "Legitimate", "pos": "adjective", "meaning": "Conforming to the law or rules", "example": "A legitimate concern.", "ielts": True},
    {"word": "Lethargic", "pos": "adjective", "meaning": "Affected by lack of energy or vitality", "example": "The patient appears lethargic.", "oet": True},
    {"word": "Likewise", "pos": "adverb", "meaning": "In the same way; also", "example": "Nurses work hard; likewise, doctors.", "ielts": True},
    {"word": "Lucid", "pos": "adjective", "meaning": "Expressed clearly; easy to understand", "example": "Give a lucid explanation.", "ielts": True},
    {"word": "Malady", "pos": "noun", "meaning": "A disease or ailment", "example": "A chronic malady.", "oet": True},
    {"word": "Manifest", "pos": "verb/adjective", "meaning": "To display or show / clear and obvious", "example": "Symptoms manifest within 24 hours.", "ielts": True},
    {"word": "Mediate", "pos": "verb", "meaning": "To intervene between parties in a dispute", "example": "A nurse mediated between family members.", "oet": True},
    {"word": "Merely", "pos": "adverb", "meaning": "Just; only", "example": "It is merely a suggestion.", "ielts": True},
    {"word": "Meticulous", "pos": "adjective", "meaning": "Showing great attention to detail", "example": "Meticulous record-keeping.", "oet": True},
    {"word": "Mitigate", "pos": "verb", "meaning": "To make less severe or painful", "example": "Steps to mitigate the risk.", "ielts": True},
    {"word": "Mobility", "pos": "noun", "meaning": "The ability to move freely", "example": "Assess the patient's mobility.", "oet": True},
    {"word": "Moderate", "pos": "adjective", "meaning": "Average in amount or intensity", "example": "Moderate pain on movement.", "oet": True},
    {"word": "Monitor", "pos": "verb/noun", "meaning": "To observe and check over a period", "example": "Monitor vital signs every 4 hours.", "oet": True},
    {"word": "Mutual", "pos": "adjective", "meaning": "Held in common by two or more parties", "example": "Mutual respect between colleagues.", "ielts": True},
    {"word": "Negligible", "pos": "adjective", "meaning": "So small as to be not worth considering", "example": "The risk is negligible.", "ielts": True},
    {"word": "Nonchalant", "pos": "adjective", "meaning": "Feeling or appearing casually calm", "example": "His nonchalant attitude surprised them.", "ielts": True},
    {"word": "Notion", "pos": "noun", "meaning": "A conception or belief about something", "example": "The notion that practice makes perfect.", "ielts": True},
    {"word": "Novel", "pos": "adjective", "meaning": "New or unusual in an interesting way", "example": "A novel approach to treatment.", "ielts": True},
    {"word": "Nuance", "pos": "noun", "meaning": "A subtle difference in meaning or expression", "example": "Understanding cultural nuances.", "ielts": True},
    {"word": "Nullify", "pos": "verb", "meaning": "To make legally null and void; invalidate", "example": "The results were nullified.", "ielts": True},
    {"word": "Objectively", "pos": "adverb", "meaning": "In a way that is not influenced by personal feelings", "example": "Assess the patient objectively.", "oet": True},
    {"word": "Obscure", "pos": "adjective/verb", "meaning": "Not discovered or known about / to hide", "example": "The meaning is obscure.", "ielts": True},
    {"word": "Omit", "pos": "verb", "meaning": "To leave out or exclude", "example": "Do not omit any relevant details.", "oet": True},
    {"word": "Ongoing", "pos": "adjective", "meaning": "Continuing to exist or progress", "example": "Ongoing treatment is required.", "oet": True},
    {"word": "Optimal", "pos": "adjective", "meaning": "Best or most favorable", "example": "Optimal conditions for recovery.", "oet": True},
    {"word": "Paradox", "pos": "noun", "meaning": "A seemingly absurd or contradictory statement", "example": "It's a paradox that less is more.", "ielts": True},
    {"word": "Paramount", "pos": "adjective", "meaning": "More important than anything else", "example": "Patient safety is paramount.", "oet": True},
    {"word": "Peripheral", "pos": "adjective", "meaning": "Relating to the outer edge or surface", "example": "Peripheral vision was affected.", "oet": True},
    {"word": "Persevere", "pos": "verb", "meaning": "To continue in spite of difficulty", "example": "Persevere with your studies!", "ielts": True},
    {"word": "Persistent", "pos": "adjective", "meaning": "Continuing firmly despite difficulty", "example": "Persistent cough for two weeks.", "oet": True},
    {"word": "Pertinent", "pos": "adjective", "meaning": "Relevant or applicable to a particular matter", "example": "Include only pertinent information.", "oet": True},
    {"word": "Pervasive", "pos": "adjective", "meaning": "Spreading widely throughout an area or group", "example": "The pervasive influence of technology.", "ielts": True},
    {"word": "Plausible", "pos": "adjective", "meaning": "Seeming reasonable or probable", "example": "A plausible explanation.", "ielts": True},
    {"word": "Potent", "pos": "adjective", "meaning": "Having great power or influence", "example": "A potent medication.", "oet": True},
    {"word": "Pragmatic", "pos": "adjective", "meaning": "Dealing with things sensibly and practically", "example": "A pragmatic approach to the problem.", "ielts": True},
    {"word": "Precede", "pos": "verb", "meaning": "To come before in time or order", "example": "The headache preceded the other symptoms.", "oet": True},
    {"word": "Precise", "pos": "adjective", "meaning": "Marked by exactness and accuracy", "example": "Give precise instructions.", "ielts": True},
    {"word": "Predicament", "pos": "noun", "meaning": "A difficult or unpleasant situation", "example": "A financial predicament.", "ielts": True},
    {"word": "Predominant", "pos": "adjective", "meaning": "Present as the strongest or main element", "example": "The predominant symptom.", "oet": True},
    {"word": "Preliminary", "pos": "adjective", "meaning": "Denoting an action preceding something", "example": "Preliminary test results.", "ielts": True},
    {"word": "Prerequisite", "pos": "noun", "meaning": "A thing required as a prior condition", "example": "IELTS is a prerequisite for registration.", "ielts": True},
    {"word": "Prescribe", "pos": "verb", "meaning": "To authorize the use of a medicine", "example": "The doctor prescribed antibiotics.", "oet": True},
    {"word": "Presume", "pos": "verb", "meaning": "To suppose that something is true", "example": "I presume you have taken the medication.", "ielts": True},
    {"word": "Prevail", "pos": "verb", "meaning": "To prove more powerful or superior", "example": "Common sense prevailed.", "ielts": True},
    {"word": "Preventative", "pos": "adjective", "meaning": "Designed to keep something undesirable from occurring", "example": "Preventative healthcare measures.", "oet": True},
    {"word": "Prioritize", "pos": "verb", "meaning": "To determine the order of importance", "example": "Prioritize the most urgent tasks.", "oet": True},
    {"word": "Probe", "pos": "verb/noun", "meaning": "To physically explore / a thorough investigation", "example": "Further probing revealed more details.", "oet": True},
    {"word": "Proceed", "pos": "verb", "meaning": "To begin or continue a course of action", "example": "Shall we proceed with the examination?", "oet": True},
    {"word": "Proficient", "pos": "adjective", "meaning": "Competent or skilled in doing something", "example": "Proficient in English communication.", "ielts": True},
    {"word": "Prognosis", "pos": "noun", "meaning": "The likely course of a disease or ailment", "example": "The prognosis is good with treatment.", "oet": True},
    {"word": "Progressive", "pos": "adjective", "meaning": "Happening gradually in stages", "example": "Progressive decline in function.", "oet": True},
    {"word": "Proliferate", "pos": "verb", "meaning": "To increase rapidly in numbers", "example": "Smartphones have proliferated worldwide.", "ielts": True},
    {"word": "Prominent", "pos": "adjective", "meaning": "Important; famous; projecting from something", "example": "A prominent feature of the policy.", "ielts": True},
    {"word": "Prompt", "pos": "verb/adjective", "meaning": "To cause or bring about / done without delay", "example": "The symptoms prompted a visit to A&E.", "oet": True},
    {"word": "Prospective", "pos": "adjective", "meaning": "Expected or expecting to be something in the future", "example": "Prospective nursing students.", "ielts": True},
    {"word": "Protocol", "pos": "noun", "meaning": "The official procedure for an activity", "example": "Follow the clinical protocol.", "oet": True},
    {"word": "Provoke", "pos": "verb", "meaning": "To stimulate a reaction or emotion", "example": "The article provoked debate.", "ielts": True},
    {"word": "Prudent", "pos": "adjective", "meaning": "Acting with care and thought for the future", "example": "It is prudent to monitor the patient.", "ielts": True},
    {"word": "Pursue", "pos": "verb", "meaning": "To follow or chase / to engage in", "example": "She pursued a career in nursing.", "ielts": True},
    {"word": "Qualitative", "pos": "adjective", "meaning": "Relating to the nature of something rather than quantity", "example": "Qualitative research methods.", "ielts": True},
    {"word": "Quantitative", "pos": "adjective", "meaning": "Relating to measurable quantities", "example": "Quantitative data analysis.", "ielts": True},
    {"word": "Query", "pos": "noun/verb", "meaning": "A question / to ask about", "example": "The patient had a query about medication.", "oet": True},
    {"word": "Rapid", "pos": "adjective", "meaning": "Happening in a short time", "example": "Rapid response to treatment.", "oet": True},
    {"word": "Recurrence", "pos": "noun", "meaning": "The fact of occurring again", "example": "Watch for recurrence of symptoms.", "oet": True},
    {"word": "Redundant", "pos": "adjective", "meaning": "No longer needed; superfluous", "example": "This step is redundant.", "ielts": True},
    {"word": "Referral", "pos": "noun", "meaning": "The act of directing a patient to a specialist", "example": "Make a referral to the cardiologist.", "oet": True},
    {"word": "Refute", "pos": "verb", "meaning": "To prove a statement or theory to be wrong", "example": "The evidence refutes this claim.", "ielts": True},
    {"word": "Regimen", "pos": "noun", "meaning": "A prescribed course of medical treatment", "example": "A treatment regimen of 6 weeks.", "oet": True},
    {"word": "Reiterate", "pos": "verb", "meaning": "To say something again for emphasis", "example": "Let me reiterate the instructions.", "ielts": True},
    {"word": "Reluctant", "pos": "adjective", "meaning": "Unwilling and hesitant", "example": "She was reluctant to take time off.", "ielts": True},
    {"word": "Remedy", "pos": "noun/verb", "meaning": "A medicine or treatment / to put right", "example": "The best remedy is rest.", "oet": True},
    {"word": "Renowned", "pos": "adjective", "meaning": "Known or talked about by many people", "example": "A renowned teaching hospital.", "ielts": True},
    {"word": "Reside", "pos": "verb", "meaning": "To have one's permanent home in a place", "example": "She resides in London.", "ielts": True},
    {"word": "Resilience", "pos": "noun", "meaning": "The capacity to recover from difficulties", "example": "Resilience is key to exam success.", "ielts": True},
    {"word": "Respective", "pos": "adjective", "meaning": "Belonging separately to each of two or more people", "example": "They returned to their respective duties.", "ielts": True},
    {"word": "Retrieve", "pos": "verb", "meaning": "To get or bring something back", "example": "Retrieve the patient records.", "oet": True},
    {"word": "Retrospective", "pos": "adjective", "meaning": "Looking back on past events", "example": "A retrospective study of patients.", "oet": True},
    {"word": "Rigor", "pos": "noun", "meaning": "Severity or strictness", "example": "Scientific rigor in research.", "ielts": True},
    {"word": "Robust", "pos": "adjective", "meaning": "Strong and healthy; vigorous", "example": "A robust immune system.", "ielts": True},
    {"word": "Routinely", "pos": "adverb", "meaning": "As part of a regular procedure", "example": "Check observations routinely.", "oet": True},
    {"word": "Scrutinize", "pos": "verb", "meaning": "To examine or inspect closely", "example": "Scrutinize the data carefully.", "ielts": True},
    {"word": "Secular", "pos": "adjective", "meaning": "Not connected with religious matters", "example": "A secular education system.", "ielts": True},
    {"word": "Sequentially", "pos": "adverb", "meaning": "Forming or following a logical order", "example": "Arrange the events sequentially.", "ielts": True},
    {"word": "Severe", "pos": "adjective", "meaning": "Very great; intense", "example": "Severe pain on the right side.", "oet": True},
    {"word": "Simultaneous", "pos": "adjective", "meaning": "Occurring at the same time", "example": "Simultaneous translation.", "ielts": True},
    {"word": "Skeptical", "pos": "adjective", "meaning": "Not easily convinced; having doubts", "example": "Skeptical about the new treatment.", "ielts": True},
    {"word": "Solely", "pos": "adverb", "meaning": "Not involving anyone or anything else", "example": "Based solely on the evidence.", "ielts": True},
    {"word": "Solicit", "pos": "verb", "meaning": "To ask for or try to obtain something", "example": "Solicit feedback from patients.", "oet": True},
    {"word": "Sporadic", "pos": "adjective", "meaning": "Occurring at irregular intervals", "example": "Sporadic episodes of dizziness.", "oet": True},
    {"word": "Stable", "pos": "adjective", "meaning": "Not likely to change or fail", "example": "The patient is now stable.", "oet": True},
    {"word": "Stagnant", "pos": "adjective", "meaning": "Showing no activity; not developing", "example": "Stagnant wages in the sector.", "ielts": True},
    {"word": "Status", "pos": "noun", "meaning": "The relative social or professional position", "example": "Assess the patient's mental status.", "oet": True},
    {"word": "Steadily", "pos": "adverb", "meaning": "In a regular and even manner", "example": "Improve steadily over time.", "ielts": True},
    {"word": "Stratify", "pos": "verb", "meaning": "To arrange in strata or layers", "example": "Stratify patients by risk level.", "oet": True},
    {"word": "Stringent", "pos": "adjective", "meaning": "Strict, precise, and exacting", "example": "Stringent safety requirements.", "ielts": True},
    {"word": "Subsequent", "pos": "adjective", "meaning": "Coming after something in time", "example": "Subsequent tests confirmed the diagnosis.", "ielts": True},
    {"word": "Subtle", "pos": "adjective", "meaning": "So delicate or precise as to be difficult to analyze", "example": "A subtle difference in meaning.", "ielts": True},
    {"word": "Sufficient", "pos": "adjective", "meaning": "Enough; adequate", "example": "Ensure sufficient fluid intake.", "oet": True},
    {"word": "Supplement", "pos": "verb/noun", "meaning": "To add to something / an addition", "example": "Supplement your diet with vitamins.", "ielts": True},
    {"word": "Surmount", "pos": "verb", "meaning": "To overcome a difficulty", "example": "Surmount the language barrier.", "ielts": True},
    {"word": "Susceptible", "pos": "adjective", "meaning": "Likely to be influenced or harmed by", "example": "Susceptible to infection.", "oet": True},
    {"word": "Sustainable", "pos": "adjective", "meaning": "Able to be maintained at a certain rate", "example": "Sustainable healthcare practices.", "ielts": True},
    {"word": "Symptom", "pos": "noun", "meaning": "A physical or mental feature indicating a condition", "example": "The presenting symptom was chest pain.", "oet": True},
    {"word": "Tentative", "pos": "adjective", "meaning": "Not certain or fixed; provisional", "example": "A tentative diagnosis.", "oet": True},
    {"word": "Thorough", "pos": "adjective", "meaning": "Complete with regard to every detail", "example": "A thorough examination.", "oet": True},
    {"word": "Threshold", "pos": "noun", "meaning": "The point at which a stimulus produces an effect", "example": "Above the pain threshold.", "oet": True},
    {"word": "Transient", "pos": "adjective", "meaning": "Lasting only for a short time", "example": "Transient loss of consciousness.", "oet": True},
    {"word": "Trivial", "pos": "adjective", "meaning": "Of little value or importance", "example": "A trivial complaint.", "ielts": True},
    {"word": "Ubiquitous", "pos": "adjective", "meaning": "Present, appearing, or found everywhere", "example": "Smartphones are now ubiquitous.", "ielts": True},
    {"word": "Unanimous", "pos": "adjective", "meaning": "Fully in agreement; without opposition", "example": "A unanimous decision.", "ielts": True},
    {"word": "Underlying", "pos": "adjective", "meaning": "Significant as a cause or basis of something", "example": "Treat the underlying cause.", "oet": True},
    {"word": "Undertake", "pos": "verb", "meaning": "To commit oneself to and begin", "example": "Undertake further training.", "ielts": True},
    {"word": "Uniform", "pos": "adjective/noun", "meaning": "Remaining the same / distinctive clothing", "example": "A uniform approach to treatment.", "ielts": True},
    {"word": "Unprecedented", "pos": "adjective", "meaning": "Never done or known before", "example": "Unprecedented demand for nurses.", "ielts": True},
    {"word": "Urge", "pos": "verb/noun", "meaning": "To try to persuade strongly / a strong desire", "example": "I urge you to practice daily.", "ielts": True},
    {"word": "Utilize", "pos": "verb", "meaning": "To make practical and effective use of", "example": "Utilize all available resources.", "ielts": True},
    {"word": "Vague", "pos": "adjective", "meaning": "Of uncertain or unclear character or meaning", "example": "The patient gave a vague history.", "oet": True},
    {"word": "Valid", "pos": "adjective", "meaning": "Actually supporting the point being made", "example": "A valid argument.", "ielts": True},
    {"word": "Viable", "pos": "adjective", "meaning": "Capable of working successfully; feasible", "example": "A viable treatment option.", "oet": True},
    {"word": "Vigilant", "pos": "adjective", "meaning": "Keeping careful watch for danger", "example": "Remain vigilant for complications.", "oet": True},
    {"word": "Virtual", "pos": "adjective", "meaning": "Almost or nearly as described, but not completely", "example": "Virtual learning environments.", "ielts": True},
    {"word": "Volatile", "pos": "adjective", "meaning": "Liable to change rapidly and unpredictably", "example": "Volatile blood sugar levels.", "oet": True},
    {"word": "Vulnerable", "pos": "adjective", "meaning": "Susceptible to physical or emotional attack or harm", "example": "Vulnerable elderly patients.", "oet": True},
    {"word": "Widespread", "pos": "adjective", "meaning": "Found or distributed over a large area", "example": "Widespread adoption of the policy.", "ielts": True},
    {"word": "Warrant", "pos": "verb/noun", "meaning": "To justify or necessitate / authorization", "example": "The symptoms warrant further investigation.", "oet": True},
    {"word": "Wary", "pos": "adjective", "meaning": "Feeling or showing caution", "example": "Be wary of misleading information.", "ielts": True},
    {"word": "Whereas", "pos": "conjunction", "meaning": "In contrast or comparison with", "example": "Whereas the NHS is public, some systems are private.", "ielts": True},
    {"word": "Yield", "pos": "verb/noun", "meaning": "To produce or provide / an amount produced", "example": "The treatment yielded good results.", "ielts": True},
    {"word": "Zeal", "pos": "noun", "meaning": "Great energy or enthusiasm", "example": "Her zeal for learning is admirable.", "ielts": True},
]


def get_daily_vocab(count: int = 1) -> str:
    """Get random vocabulary words with definitions."""
    words = random.sample(VOCABULARY, min(count, len(VOCABULARY)))
    sections = []
    for w in words:
        tags = []
        if w.get("ielts"):
            tags.append("📝 IELTS")
        if w.get("oet"):
            tags.append("🏥 OET")
        tag_text = " | ".join(tags) if tags else ""
        sections.append(
            f"📖 <b>{w['word']}</b> <i>({w['pos']})</i> {tag_text}\n"
            f"💡 <b>Meaning:</b> {w['meaning']}\n"
            f"📝 <b>Example:</b> <i>\"{w['example']}\"</i>"
        )
    content = f"🎯 <b>Daily Vocabulary ({count} word{'s' if count > 1 else ''})</b>\n\n" + "\n\n".join(sections)
    return content + f"\n\n🌐 Practice more vocabulary at {ANGLOTEC_URLS['vocab_app']}" + ANGLOTEC_FOOTER_SHORT


# ============================================================
# STUDY TIPS DATABASE
# ============================================================

STUDY_TIPS = [
    "🎯 <b>Set a fixed study time</b> — Same hour every day builds habit. Even 30 minutes daily beats 3 hours once a week.",
    "📝 <b>Use active recall</b> — Don't just re-read. Close the book and test yourself. This is the #1 science-backed study method.",
    "🗣️ <b>Record yourself speaking</b> — For IELTS Speaking and OET role-plays, record daily and review for filler words (um, uh, like).",
    "📚 <b>Read academic articles</b> — BBC Health, The Guardian, and BMJ articles improve reading speed and vocabulary simultaneously.",
    "⏱️ <b>Time your practice</b> — IELTS Writing Task 1 = 20 mins, Task 2 = 40 mins. Practice with a timer always.",
    "🎧 <b>Listen to medical podcasts</b> — For OET Listening, try BBC Health Check, BMJ Podcast, or Nursing Standard.",
    "🧠 <b>Use spaced repetition</b> — Review vocabulary on Day 1, Day 3, Day 7, Day 14. Apps like Anki help automate this.",
    "✍️ <b>Write every day</b> — Even 150 words on any topic keeps your writing skills sharp. Consistency > intensity.",
    "🤝 <b>Find a study partner</b> — Practice OET speaking role-plays with a partner. IELTS speaking too. Feedback is gold.",
    "📱 <b>Use AngloTec's free tools</b> — The IELTS calculator and study planner save hours of planning time.",
    "🔁 <b>Review your mistakes</b> — Keep an error log. Every wrong answer is a learning opportunity.",
    "🧘 <b>Take breaks</b> — Use the Pomodoro technique: 25 mins study, 5 mins break. Your brain needs rest to consolidate.",
    "📖 <b>Learn word families</b> — Don't just learn 'analyze.' Learn analysis, analytical, analyst. Triple your vocabulary fast.",
    "🏥 <b>Practice NHS scenarios</b> — For OSCE, rehearse breaking bad news using the SPIKES model until it's automatic.",
    "🎯 <b>Know the band descriptors</b> — IELTS publishes exact criteria for each band. Study them to know what examiners want.",
    "📊 <b>Track your progress</b> — Log your practice test scores weekly. Seeing improvement keeps motivation high.",
    "💬 <b>Shadow native speakers</b> — Listen to BBC news and repeat immediately, mimicking intonation and rhythm.",
    "📝 <b>Plan before writing</b> — Spend 5 minutes outlining your IELTS Task 2 essay. A good plan = a good essay.",
    "🎵 <b>Use background music</b> — Lo-fi or classical music can help focus during reading practice.",
    "🌅 <b>Study in the morning</b> — Cortisol levels are highest in the morning, which aids memory formation.",
    "📋 <b>Create flashcards</b> — For OET, put medical terms on one side and lay explanations on the other.",
    "🗣️ <b>Speak aloud</b> — Reading silently is passive. Reading aloud engages multiple senses and improves retention.",
    "🔍 <b>Analyze model answers</b> — Don't just read them. Break down structure, vocabulary, and linking words.",
    "📅 <b>Set weekly goals</b> — 'This week I will master Task 1 graph language' is better than 'I will study more.'",
    "💤 <b>Sleep on it</b> — Studies show sleep consolidates memory. Review before bed, test yourself in the morning.",
    "🌍 <b>Immerse in English</b> — Change your phone, social media, and Netflix to English. Passive learning adds up.",
    "🏆 <b>Simulate exam conditions</b> — Take full mock tests in a quiet room with a timer. No phone, no breaks.",
    "📌 <b>Focus on weak areas</b> — If Writing is your lowest score, dedicate 60% of time to it.",
    "💡 <b>Teach what you learn</b> — Explaining a concept to someone else is the best way to master it.",
    "🎯 <b>Use the AngloTec study planner</b> — A structured plan beats random studying every time.",
]


def get_study_tips(count: int = 3) -> str:
    """Get random study tips."""
    tips = random.sample(STUDY_TIPS, min(count, len(STUDY_TIPS)))
    tips_text = "\n\n".join(tips)
    return (
        f"💡 <b>Study Tips ({count} tips for today)</b>\n\n"
        f"{tips_text}\n\n"
        f"📅 <b>Create your free study plan:</b>\n"
        f"👉 {ANGLOTEC_URLS['study_planner']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# STUDY PLAN GENERATOR
# ============================================================

def generate_study_plan(weeks: int) -> str:
    """Generate a personalized study plan based on available weeks."""
    weeks = max(MIN_STUDY_WEEKS, min(weeks, MAX_STUDY_WEEKS))

    # Define the plan structure based on duration
    if weeks <= 2:
        focus = "🚨 <b>Intensive Crash Plan</b>"
        schedule = [
            "Week 1: Full mock test → identify weak areas → intensive practice on lowest skill",
            "Week 2: Focused skill building → daily timed practice → full mock test every 2 days",
        ]
    elif weeks <= 4:
        focus = "⚡ <b>Short-Term Plan</b>"
        schedule = [
            "Week 1: Diagnostic test + foundation building (grammar, basic vocabulary)",
            "Week 2: Skill development (Reading + Listening strategies)",
            "Week 3: Writing practice + Speaking practice daily",
            "Week 4: Full mock tests + review of all weak areas",
        ]
    elif weeks <= 8:
        focus = "📈 <b>Standard Plan</b>"
        schedule = [
            "Weeks 1-2: Foundation — grammar review, core vocabulary (20 words/day), listening practice",
            "Weeks 3-4: Reading strategies — skimming, scanning, practice tests every 3 days",
            "Weeks 5-6: Writing focus — Task 1 & 2 practice, model answer analysis, timed essays",
            "Weeks 7-8: Speaking practice + full mock tests weekly + final review of all skills",
        ]
    elif weeks <= 12:
        focus = "🎓 <b>Comprehensive Plan</b>"
        schedule = [
            "Weeks 1-3: Foundation phase — grammar, vocabulary building, basic skills",
            "Weeks 4-6: Skill building — Reading & Listening strategies, note-taking techniques",
            "Weeks 7-9: Intensive Writing & Speaking — daily practice, feedback, improvement",
            "Weeks 10-12: Mock test phase — full tests weekly, error analysis, final polish",
        ]
    else:
        focus = "🏆 <b>Mastery Plan</b>"
        schedule = [
            "Months 1-2: Foundation — core vocabulary (500+ words), grammar mastery, daily reading",
            "Months 3-4: Skill development — all 4 skills with strategies, weekly practice tests",
            "Months 5-6: Advanced practice — complex topics, timed conditions, speaking fluency",
            "Final month: Mock test week, intensive review, confidence building",
        ]

    schedule_text = "\n".join(f"• {s}" for s in schedule)

    daily_routine = (
        "\n📅 <b>Daily Routine Template:</b>\n"
        "• Morning (30 min): Vocabulary + Reading practice\n"
        "• Midday (30 min): Listening practice\n"
        "• Evening (45 min): Writing practice or Speaking practice (alternate days)\n"
        "• Weekend: Full mock test or intensive review"
    )

    return (
        f"📋 <b>Your Personalized Study Plan</b>\n"
        f"{focus} — <i>{weeks} week{'s' if weeks > 1 else ''}</i>\n\n"
        f"{schedule_text}\n"
        f"{daily_routine}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 <b>Track your progress with our free tools:</b>\n"
        f"• IELTS Calculator: {ANGLOTEC_URLS['ielts_calculator']}\n"
        f"• Study Planner: {ANGLOTEC_URLS['study_planner']}\n"
        f"• Vocabulary App: {ANGLOTEC_URLS['vocab_app']}\n\n"
        f"💪 <b>You've got this!</b> Consistency is the key to success."
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# IELTS BAND CALCULATOR
# ============================================================

def calculate_ielts_band(listening: float, reading: float, writing: float, speaking: float) -> str:
    """Calculate overall IELTS band score."""
    scores = [listening, reading, writing, speaking]
    
    # Validate scores
    for s in scores:
        if not (0.0 <= s <= 9.0):
            return (
                "❌ <b>Invalid Score</b>\n\n"
                "Each band score must be between 0.0 and 9.0.\n\n"
                "<b>Usage:</b> /calc 7.0 6.5 7.5 8.0\n"
                "(Listening Reading Writing Speaking)"
            )
    
    # Calculate overall (rounded to nearest 0.5)
    raw_average = sum(scores) / 4
    # IELTS rounding: 0.25 rounds up to 0.5, 0.75 rounds up to next whole
    fractional = raw_average % 1
    if fractional < 0.25:
        overall = int(raw_average)
    elif fractional < 0.75:
        overall = int(raw_average) + 0.5
    else:
        overall = int(raw_average) + 1
    
    # Determine CEFR level
    if overall >= 8.0:
        cefr = "C2 (Proficiency)"
    elif overall >= 7.0:
        cefr = "C1 (Advanced)"
    elif overall >= 6.0:
        cefr = "B2 (Upper-Intermediate)"
    elif overall >= 5.0:
        cefr = "B1 (Intermediate)"
    elif overall >= 4.0:
        cefr = "A2 (Elementary)"
    else:
        cefr = "A1 (Beginner)"
    
    # NHS requirement check
    if overall >= 7.0:
        nhs_status = "✅ <b>Meets NHS requirement</b> (Band 7.0+)"
    elif overall >= 6.5:
        nhs_status = "⚠️ <b>Below NHS requirement</b> (Need 7.0+ for most roles)"
    else:
        nhs_status = "❌ <b>Below NHS requirement</b> (Need 7.0+ for NMC registration)"
    
    # Find weakest skill
    skill_names = ["Listening", "Reading", "Writing", "Speaking"]
    min_score = min(scores)
    weakest = skill_names[scores.index(min_score)]
    
    return (
        f"🧮 <b>IELTS Band Score Calculator</b>\n\n"
        f"📊 <b>Your Scores:</b>\n"
        f"🎧 Listening:    {listening:.1f}\n"
        f"📖 Reading:      {reading:.1f}\n"
        f"✍️ Writing:      {writing:.1f}\n"
        f"🗣️ Speaking:     {speaking:.1f}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🏆 <b>Overall Band: {overall:.1f}</b>\n"
        f"📈 Raw Average: {raw_average:.2f}\n"
        f"🌍 CEFR Level: {cefr}\n\n"
        f"{nhs_status}\n\n"
        f"💡 <b>Focus Area:</b> Your weakest skill is <b>{weakest}</b> ({min_score:.1f}).\n"
        f"   Spend extra time improving this area!\n\n"
        f"🎯 Want a study plan? Use /studyplan [weeks]"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


# ============================================================
# DAILY THEME CONTENT GENERATORS
# ============================================================

def get_monday_vocab() -> str:
    """Monday: IELTS vocabulary (3 words)"""
    return get_daily_vocab(count=3)


def get_tuesday_oet_tip() -> str:
    """Tuesday: OET speaking tip"""
    oet_tips = [
        (
            "🗣️ <b>OET Speaking Tip: Building Rapport</b>",
            "Start every role-play by establishing rapport. Use the patient's name, show empathy, "
            "and acknowledge their feelings. Example: 'Hello Mrs. Smith, I can see you've been waiting. "
            "I'm here to help you with your concerns today.' This first 30 seconds sets the tone for "
            "the entire interaction."
        ),
        (
            "🗣️ <b>OET Speaking Tip: Task Management</b>",
            "You have 3 minutes to prepare. Underline ALL tasks on the role card. Number them 1, 2, 3. "
            "During the role-play, tick off each task as you complete it. If time is running short, "
            "prioritize the most critical tasks. The examiner checks if you addressed every task."
        ),
        (
            "🗣️ <b>OET Speaking Tip: Explaining Medical Terms</b>",
            "Never use medical jargon without explaining it. Instead of 'hypertension,' say 'high blood pressure.' "
            "Instead of 'myocardial infarction,' say 'heart attack.' Your score depends on the patient "
            "understanding you clearly. Practice translating medical terms into everyday English."
        ),
        (
            "🗣️ <b>OET Speaking Tip: Active Listening</b>",
            "Use active listening phrases: 'I see,' 'I understand,' 'That must be difficult.' "
            "Paraphrase what the patient says: 'So what you're saying is...' This shows the examiner "
            "you're engaged and builds trust with the patient. It's worth band points!"
        ),
        (
            "🗣️ <b>OET Speaking Tip: Closing the Consultation</b>",
            "Always close properly: summarize key points, check understanding ('Does that make sense?'), "
            "outline next steps, and offer further help. A strong closing leaves a good final impression "
            "and ensures you score on relationship-building criteria."
        ),
    ]
    title, content = random.choice(oet_tips)
    return (
        f"📅 <b>Tuesday — OET Speaking Focus</b>\n\n"
        f"{title}\n\n"
        f"{content}\n\n"
        f"🎯 <b>Practice this today:</b> Do one role-play recording and review it!\n\n"
        f"🩺 <b>Free OET Practice Tools:</b>\n"
        f"👉 {ANGLOTEC_URLS['oet_practice']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


def get_wednesday_osce_tip() -> str:
    """Wednesday: OSCE station type explanation"""
    station = random.choice(OSCE_STATIONS)
    tips_text = "\n".join(f"• {tip}" for tip in station["tips"])
    return (
        f"📅 <b>Wednesday — OSCE Station Focus</b>\n\n"
        f"🩺 <b>Station Type: {station['type']}</b>\n"
        f"<i>{station['description']}</i>\n\n"
        f"💡 <b>Key Strategies:</b>\n"
        f"{tips_text}\n\n"
        f"🎯 <b>Practice this today:</b> Time yourself doing this station type (8-10 mins)!\n\n"
        f"🩺 <b>Free OSCE Scenario Generator:</b>\n"
        f"👉 {ANGLOTEC_URLS['osce_generator']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


def get_thursday_ai_prompt() -> str:
    """Thursday: AI prompt of the day"""
    prompts = [
        (
            "🤖 <b>AI Prompt: IELTS Writing Feedback</b>",
            "Copy-paste this into ChatGPT/Claude after writing your essay:\n\n"
            "<code>Review my IELTS Task 2 essay. Score it using IELTS band descriptors. "
            "Identify: 1) Task response issues, 2) Coherence problems, 3) Vocabulary limitations, "
            "4) Grammar errors. Rewrite weak sentences and suggest band 8 alternatives.</code>\n\n"
            "💡 <b>Tip:</b> Always ask the AI to use IELTS-specific criteria, not general feedback."
        ),
        (
            "🤖 <b>AI Prompt: OET Speaking Practice</b>",
            "Use this prompt for realistic OET speaking practice:\n\n"
            "<code>Act as a patient who is anxious about upcoming surgery. I am your nurse. "
            "Respond naturally, ask questions, show emotions, and occasionally be vague or resistant. "
            "Give me feedback on my communication skills using OET criteria after 5 minutes.</code>\n\n"
            "💡 <b>Tip:</b> Practice with different AI personalities (angry patient, confused elderly, etc.)"
        ),
        (
            "🤖 <b>AI Prompt: OSCE Scenario Generator</b>",
            "Generate unlimited OSCE practice with this prompt:\n\n"
            "<code>Create a 10-minute OSCE station for [cardiovascular examination]. Include: "
            "patient brief, examiner checklist with scoring points, common mistakes students make, "
            "and a time management breakdown (2 min intro, 5 min exam, 3 min closure).</code>\n\n"
            "💡 <b>Tip:</b> Replace [cardiovascular] with any system: respiratory, neuro, GI, etc."
        ),
        (
            "🤖 <b>AI Prompt: Vocabulary Builder</b>",
            "Build topic-specific vocabulary fast:\n\n"
            "<code>Generate 20 IELTS Band 7+ vocabulary words related to [healthcare/technology/environment]. "
            "For each word, provide: definition, example sentence, word family (noun/verb/adj/adv), "
            "and a common collocation.</code>\n\n"
            "💡 <b>Tip:</b> Focus on one topic per week to build deep vocabulary knowledge."
        ),
        (
            "🤖 <b>AI Prompt: NHS Interview Prep</b>",
            "Prepare for NHS interviews with this prompt:\n\n"
            "<code>Ask me 5 common NHS interview questions one at a time. After each answer, "
            "score my response (1-5) using the STAR method criteria. Suggest improvements "
            "and give me a model Band 5 answer for each question.</code>\n\n"
            "💡 <b>Tip:</b> Record your spoken answers and transcribe them for AI feedback."
        ),
    ]
    title, content = random.choice(prompts)
    return (
        f"📅 <b>Thursday — AI Prompt of the Day</b>\n\n"
        f"{title}\n\n"
        f"{content}\n\n"
        f"🎯 <b>Try this prompt today and level up your study!"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


def get_friday_nhs_value() -> str:
    """Friday: NHS value of the week"""
    values = [
        (
            "🤝 <b>NHS Value: Working Together for Patients</b>",
            "Patients come first in everything we do. This means collaborating across teams, "
            "sharing information appropriately, and always asking: 'What is best for the patient?'\n\n"
            "<b>Interview tip:</b> Use an example of multidisciplinary team working. "
            "Example: 'In my unit, I worked with doctors, physios, and social workers to "
            "create a discharge plan that put the patient's needs at the center.'"
        ),
        (
            "💙 <b>NHS Value: Respect and Dignity</b>",
            "Every person — patient or colleague — deserves to be treated with respect. "
            "This means valuing diversity, maintaining privacy, and listening without judgment.\n\n"
            "<b>Interview tip:</b> Share how you adapted care for someone with cultural/language needs. "
            "Example: 'I used a professional interpreter rather than family members to ensure "
            "the patient's dignity and accurate communication.'"
        ),
        (
            "⭐ <b>NHS Value: Commitment to Quality of Care</b>",
            "We continuously strive to improve. This means staying updated with evidence, "
            "reflecting on practice, and embracing lifelong learning.\n\n"
            "<b>Interview tip:</b> Talk about CPD activities. "
            "Example: 'I regularly attend training sessions and read journal articles to ensure "
            "my practice reflects current evidence-based guidelines.'"
        ),
        (
            "❤️ <b>NHS Value: Compassion</b>",
            "We respond with humanity and kindness to each person's pain, distress, anxiety, or need. "
            "Compassion is at the heart of nursing and care delivery.\n\n"
            "<b>Interview tip:</b> Give a specific example of going above and beyond. "
            "Example: 'I noticed a patient was anxious before surgery, so I sat with them, "
            "held their hand, and explained the process until they felt calmer.'"
        ),
        (
            "🌟 <b>NHS Value: Improving Lives</b>",
            "We aim to improve health and well-being for individuals, communities, and populations. "
            "This means thinking beyond the immediate clinical need to the bigger picture.\n\n"
            "<b>Interview tip:</b> Discuss health promotion or community work. "
            "Example: 'I organized a diabetes education session for patients and their families, "
            "helping them manage the condition better at home.'"
        ),
        (
            "🌍 <b>NHS Value: Everyone Counts</b>",
            "We maximize resources for the benefit of the whole community. Nobody is excluded. "
            "This means fair access to care regardless of background.\n\n"
            "<b>Interview tip:</b> Show understanding of healthcare equality. "
            "Example: 'I ensure all my patients receive the same standard of care, regardless of "
            "their background, and I advocate for those who may struggle to access services.'"
        ),
    ]
    title, content = random.choice(values)
    return (
        f"📅 <b>Friday — NHS Value of the Week</b>\n\n"
        f"{title}\n\n"
        f"{content}\n\n"
        f"🎯 <b>Prepare for NHS interviews with our free question bank:</b>\n"
        f"👉 {ANGLOTEC_URLS['nhs_interview']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


def get_saturday_motivation() -> str:
    """Saturday: Study motivation quote"""
    quotes = [
        ("🌟 <b>Success is the sum of small efforts, repeated day in and day out.</b>", "— Robert Collier"),
        ("📚 <b>The future belongs to those who believe in the beauty of their dreams.</b>", "— Eleanor Roosevelt"),
        ("🎯 <b>It always seems impossible until it's done.</b>", "— Nelson Mandela"),
        ("💪 <b>Don't watch the clock; do what it does. Keep going.</b>", "— Sam Levenson"),
        ("🔥 <b>The only way to do great work is to love what you do.</b>", "— Steve Jobs"),
        ("🌈 <b>Your limitation—it's only your imagination.</b>", "— Unknown"),
        ("🏆 <b>Push yourself, because no one else is going to do it for you.</b>", "— Unknown"),
        ("⭐ <b>Great things never come from comfort zones.</b>", "— Unknown"),
        ("🚀 <b>Dream it. Wish it. Do it.</b>", "— Unknown"),
        ("💡 <b>Success doesn't just find you. You have to go out and get it.</b>", "— Unknown"),
        ("🌟 <b>The harder you work for something, the greater you'll feel when you achieve it.</b>", "— Unknown"),
        ("🎯 <b>Dream bigger. Do bigger.</b>", "— Unknown"),
        ("📖 <b>Learning is not attained by chance. It must be sought for with ardor and attended to with diligence.</b>", "— Abigail Adams"),
        ("💪 <b>I am not a product of my circumstances. I am a product of my decisions.</b>", "— Stephen Covey"),
        ("🔥 <b>Believe you can and you're halfway there.</b>", "— Theodore Roosevelt"),
    ]
    quote, author = random.choice(quotes)
    return (
        f"📅 <b>Saturday — Study Motivation</b>\n\n"
        f"{quote}\n"
        f"<i>{author}</i>\n\n"
        f"💪 <b>This weekend's challenge:</b> Do ONE full mock test. "
        f"Track your scores. Every practice session brings you closer to your goal!\n\n"
        f"🎯 <b>Free tools to help you prepare:</b>\n"
        f"• IELTS Calculator: {ANGLOTEC_URLS['ielts_calculator']}\n"
        f"• Study Planner: {ANGLOTEC_URLS['study_planner']}\n"
        f"• OSCE Generator: {ANGLOTEC_URLS['osce_generator']}"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )


def get_sunday_challenge() -> str:
    """Sunday: Weekly study challenge"""
    challenges = [
        (
            "🎯 <b>This Week's Challenge: Perfect Your Introduction</b>",
            "Write and memorize a perfect IELTS Writing Task 2 introduction template. "
            "Practice applying it to 5 different essay questions. A strong introduction "
            "sets the examiner's impression for your entire essay."
        ),
        (
            "🎯 <b>This Week's Challenge: Vocabulary Sprint</b>",
            "Learn 50 new words this week. That's just 7 words per day! Use flashcards, "
            "write sentences, and review daily. Focus on one topic area (health, education, or technology)."
        ),
        (
            "🎯 <b>This Week's Challenge: Listening Marathon</b>",
            "Complete one full IELTS Listening test every day this week. That's 7 tests! "
            "Track your score each day. Aim to improve by at least 2 correct answers by Sunday."
        ),
        (
            "🎯 <b>This Week's Challenge: Speaking Recordings</b>",
            "Record yourself answering one IELTS Speaking Part 2 topic every day. "
            "Listen back and count your 'um's and 'uh's. Reduce them by 50% by next Sunday."
        ),
        (
            "🎯 <b>This Week's Challenge: OET Role-Play Mastery</b>",
            "Do 5 OET speaking role-plays this week. Focus on ONE skill each time: "
            "Rapport building → Task management → Medical explanation → Empathy → Closing."
        ),
        (
            "🎯 <b>This Week's Challenge: NHS Value Memorization</b>",
            "Memorize all 6 NHS Values AND prepare one STAR-method example for each. "
            "This is the #1 preparation for NHS interviews. Practice saying them aloud."
        ),
        (
            "🎯 <b>This Week's Challenge: Error Log Review</b>",
            "Gather all your past mistakes from practice tests. Categorize them: "
            "vocabulary errors, grammar mistakes, time management issues, misunderstanding questions. "
            "Create a personal 'don't do this' checklist."
        ),
        (
            "🎯 <b>This Week's Challenge: Speed Reading</b>",
            "Practice reading IELTS passages in 15 minutes instead of 20. "
            "Use skimming for the first 2 minutes, then scan for answers. Time yourself strictly."
        ),
    ]
    title, content = random.choice(challenges)
    return (
        f"📅 <b>Sunday — Weekly Study Challenge</b>\n\n"
        f"{title}\n\n"
        f"{content}\n\n"
        f"🏆 <b>Share your progress!</b> Tell your study group what you achieved this week.\n\n"
        f"📊 <b>Track your progress:</b>\n"
        f"• IELTS Calculator: {ANGLOTEC_URLS['ielts_calculator']}\n"
        f"• Study Planner: {ANGLOTEC_URLS['study_planner']}\n\n"
        f"💪 <b>New week, new progress!</b> You've got this!"
        f"{ANGLOTEC_FOOTER_SHORT}"
    )
