"""
AngloTec Study Bot - Quiz Database
=====================================
100+ quiz questions covering IELTS, OET, and OSCE topics.
Each question includes an explanation for learning value.
"""

import random
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class QuizQuestion:
    """Represents a single quiz question."""
    question: str
    options: List[str]  # 4 options, first is correct
    correct_index: int  # 0-based index of correct answer
    explanation: str
    category: str  # 'ielts', 'oet', 'osce', 'nhs', 'vocabulary'
    difficulty: str  # 'easy', 'medium', 'hard'

    def get_shuffled_options(self) -> tuple[List[str], int]:
        """Return shuffled options and new index of correct answer."""
        indexed = list(enumerate(self.options))
        random.shuffle(indexed)
        new_options = [opt for _, opt in indexed]
        new_correct = [i for i, (orig_idx, _) in enumerate(indexed) if orig_idx == self.correct_index][0]
        return new_options, new_correct


# ============================================================
# IELTS QUIZ QUESTIONS
# ============================================================

IELTS_QUESTIONS = [
    QuizQuestion(
        question="How long is the IELTS Writing Task 2?",
        options=["40 minutes", "20 minutes", "60 minutes", "30 minutes"],
        correct_index=0,
        explanation="IELTS Writing Task 2 (essay) is 40 minutes. Task 1 (graph/letter) is 20 minutes.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the minimum word count for IELTS Writing Task 2?",
        options=["250 words", "150 words", "300 words", "200 words"],
        correct_index=0,
        explanation="Task 2 requires at least 250 words. Writing fewer results in penalization.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How many sections are in the IELTS Listening test?",
        options=["4 sections", "3 sections", "5 sections", "2 sections"],
        correct_index=0,
        explanation="IELTS Listening has 4 sections with 10 questions each, totaling 40 questions.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How long is the IELTS Speaking test?",
        options=["11-14 minutes", "10-12 minutes", "15-20 minutes", "8-10 minutes"],
        correct_index=0,
        explanation="The Speaking test lasts 11-14 minutes and has 3 parts.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In IELTS Reading, how many passages are there?",
        options=["3 passages", "2 passages", "4 passages", "5 passages"],
        correct_index=0,
        explanation="Academic Reading has 3 long passages. General Training has 3 sections with shorter texts.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does 'True/False/Not Given' mean in IELTS Reading?",
        options=["The passage explicitly confirms, contradicts, or doesn't mention the statement", 
                 "Always guess Not Given if unsure",
                 "True means the statement matches your knowledge",
                 "Not Given means the answer will be in the next passage"],
        correct_index=0,
        explanation="T/F/NG must be based ONLY on the passage. 'Not Given' means the passage doesn't address it.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which linking word shows CONTRAST?",
        options=["Nevertheless", "Furthermore", "Consequently", "Similarly"],
        correct_index=0,
        explanation="'Nevertheless' shows contrast. 'Furthermore' adds info, 'Consequently' shows result, 'Similarly' compares.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In IELTS Speaking Part 2, how long do you speak uninterrupted?",
        options=["1-2 minutes", "30 seconds", "3-4 minutes", "5 minutes"],
        correct_index=0,
        explanation="You speak for 1-2 minutes on the cue card topic, with 1 minute of preparation time.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the overall IELTS band calculated from?",
        options=["Average of 4 sections, rounded to nearest 0.5", 
                 "Highest band only",
                 "Average rounded down always",
                 "Writing and Speaking only"],
        correct_index=0,
        explanation="Overall = (L+R+W+S)/4, rounded to nearest 0.5 (0.25 rounds up to 0.5, 0.75 rounds up to whole).",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which is NOT a recommended strategy for IELTS Reading?",
        options=["Read every word carefully from start to finish", 
                 "Skim the passage first for main idea",
                 "Scan for keywords from the questions",
                 "Manage time (1.5 min per question max)"],
        correct_index=0,
        explanation="Reading every word wastes time. Skim for gist (2-3 mins), then scan for specific answers.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you do in the final 10 minutes of IELTS Listening?",
        options=["Transfer answers to the answer sheet", 
                 "Check the next section's questions",
                 "Leave early",
                 "Ask the examiner questions"],
        correct_index=0,
        explanation="In paper-based IELTS, you get 10 minutes at the end to transfer answers to the answer sheet.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which sentence uses the correct academic register for IELTS Writing?",
        options=["The data indicates a significant increase in urban population.", 
                 "The numbers went up a lot in cities.",
                 "City people got more, like, really fast.",
                 "Lots more folks moved to town, you know?"],
        correct_index=0,
        explanation="Academic writing requires formal vocabulary. 'Indicates a significant increase' is formal; casual language lowers your score.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="How many questions are in the IELTS Listening test?",
        options=["40 questions", "30 questions", "50 questions", "20 questions"],
        correct_index=0,
        explanation="IELTS Listening has 40 questions total (10 per section across 4 sections).",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the purpose of IELTS Speaking Part 3?",
        options=["To discuss abstract ideas related to Part 2 topic", 
                 "To introduce yourself",
                 "To describe a personal experience",
                 "To read a passage aloud"],
        correct_index=0,
        explanation="Part 3 is the two-way discussion where the examiner asks abstract, analytical questions related to your Part 2 topic.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="For IELTS Writing Task 1 Academic, what type of task is it?",
        options=["Describe and analyze visual data (graph, chart, diagram)", 
                 "Write an essay on an opinion",
                 "Write a letter",
                 "Summarize an article"],
        correct_index=0,
        explanation="Task 1 Academic requires describing visual data (bar chart, line graph, pie chart, diagram, map, process).",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which cohesive device is used to show RESULT?",
        options=["As a result", "However", "In addition", "For example"],
        correct_index=0,
        explanation="'As a result' shows consequence/result. 'However' = contrast, 'In addition' = adding, 'For example' = exemplifying.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the IELTS score required for NMC registration (UK)?",
        options=["7.0 in all four sections", 
                 "6.5 overall", 
                 "8.0 in all sections",
                 "6.0 overall"],
        correct_index=0,
        explanation="NMC requires IELTS Academic 7.0 in Listening, Reading, Writing, AND Speaking (no averaging).",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In IELTS Writing Task 2, which essay type asks for your opinion?",
        options=["Opinion essay (Do you agree or disagree?)", 
                 "Problem-Solution essay",
                 "Discussion essay (Discuss both views)",
                 "Advantages-Disadvantages essay"],
        correct_index=0,
        explanation="'Do you agree or disagree?' and 'To what extent do you agree?' are opinion essays requiring a clear position.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you NOT do in IELTS Speaking?",
        options=["Memorize and recite a prepared speech", 
                 "Use discourse markers (firstly, moreover, however)",
                 "Give extended answers with reasons and examples",
                 "Paraphrase the examiner's questions"],
        correct_index=0,
        explanation="Memorized speeches are penalized. Examiners can tell — it sounds unnatural and doesn't answer the specific question.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which word is a synonym for 'significant' in academic writing?",
        options=["Substantial", "Small", "Unimportant", "Tiny"],
        correct_index=0,
        explanation="'Substantial' is a synonym for 'significant.' Using varied vocabulary improves your Lexical Resource score.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How is the IELTS General Training Writing Task 1 different from Academic?",
        options=["GT Task 1 is a letter; Academic Task 1 describes a graph/chart", 
                 "GT has no Task 1",
                 "GT Task 1 is shorter (100 words)",
                 "GT Task 1 requires an essay"],
        correct_index=0,
        explanation="General Training Task 1 is a formal, semi-formal, or informal letter (150 words). Academic Task 1 describes visual data.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does 'cohesive devices' mean in IELTS Writing criteria?",
        options=["Linking words and phrases that connect ideas (however, therefore, furthermore)", 
                 "Words that stick together physically",
                 "Using the same word repeatedly",
                 "Writing in bullet points"],
        correct_index=0,
        explanation="Cohesive devices (linking words) connect sentences and paragraphs logically. They account for 25% of your Coherence score.",
        category="ielts",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In IELTS Reading, what does 'YES/NO/NOT GIVEN' test?",
        options=["The author's opinion vs facts in the passage", 
                 "Only grammar knowledge",
                 "Your personal opinion",
                 "Vocabulary only"],
        correct_index=0,
        explanation="Y/N/NG tests whether statements agree with the author's views/opinions (vs T/F/NG which tests facts).",
        category="ielts",
        difficulty="hard",
    ),
    QuizQuestion(
        question="What is the best way to improve IELTS Listening?",
        options=["Practice with timed tests and a variety of accents", 
                 "Only watch American TV shows",
                 "Read more books",
                 "Memorize common answers"],
        correct_index=0,
        explanation="Timed practice with British, Australian, and American accents prepares you for the real test's variety.",
        category="ielts",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which IELTS Writing Task 2 structure is recommended for a Band 7+?",
        options=["Introduction → Body Paragraph 1 → Body Paragraph 2 → Conclusion", 
                 "One long paragraph",
                 "Introduction only",
                 "Body paragraphs without introduction"],
        correct_index=0,
        explanation="A 4-paragraph structure (Intro → 2 Body → Conclusion) is the standard for high-band essays. It shows clear organization.",
        category="ielts",
        difficulty="easy",
    ),
]


# ============================================================
# OET QUIZ QUESTIONS
# ============================================================

OET_QUESTIONS = [
    QuizQuestion(
        question="What does OET stand for?",
        options=["Occupational English Test", 
                 "Official English Test",
                 "Oral English Test",
                 "Occupational Examination Test"],
        correct_index=0,
        explanation="OET = Occupational English Test. It's designed specifically for healthcare professionals.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How long is the OET Speaking role-play?",
        options=["Approximately 5 minutes", 
                 "10 minutes",
                 "15 minutes",
                 "3 minutes"],
        correct_index=0,
        explanation="Each OET Speaking role-play lasts about 5 minutes, preceded by 3 minutes of preparation time.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What type of letter is OET Writing?",
        options=["A referral, discharge, or transfer letter", 
                 "A personal letter to a friend",
                 "A complaint letter",
                 "A job application letter"],
        correct_index=0,
        explanation="OET Writing requires a professional healthcare letter (referral, discharge, transfer) based on case notes.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How many role-plays are in the OET Speaking test?",
        options=["2 role-plays", 
                 "1 role-play",
                 "3 role-plays",
                 "4 role-plays"],
        correct_index=0,
        explanation="OET Speaking consists of 2 role-plays, each with 3 minutes preparation and ~5 minutes speaking.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What should you do during the 3-minute OET Speaking preparation time?",
        options=["Underline tasks on the role card and plan your approach", 
                 "Memorize a script",
                 "Chat with the interlocutor",
                 "Look up medical terms on your phone"],
        correct_index=0,
        explanation="Use prep time to identify tasks on the card, plan how to address each, and think about opening phrases.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In OET Writing, what information should you OMIT from case notes?",
        options=["Irrelevant personal details (e.g., patient's hobbies)", 
                 "Medication names and dosages",
                 "Vital signs and test results",
                 "The reason for referral"],
        correct_index=0,
        explanation="Only include clinically relevant information. Patient's hobbies, unless medically relevant, should be omitted.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which grade is the minimum required for NMC registration with OET?",
        options=["Grade B (350+) in all sections, or C+ in writing with B in others",
                 "Grade C in all sections",
                 "Grade A in all sections",
                 "Grade D is acceptable"],
        correct_index=0,
        explanation="NMC accepts OET with Grade B (350+) in all sections, OR Grade C+ in Writing with Grade B in Listening, Reading, and Speaking.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In OET Speaking, who starts the role-play?",
        options=["The candidate (you) starts the conversation", 
                 "The examiner starts",
                 "The patient (actor) starts",
                 "A bell rings to start"],
        correct_index=0,
        explanation="You (the candidate) initiate the role-play. Prepare a professional opening: introduce yourself, confirm identity, establish rapport.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the word count requirement for OET Writing?",
        options=["180-200 words", 
                 "150-170 words",
                 "250-300 words",
                 "100-150 words"],
        correct_index=0,
        explanation="OET Writing should be 180-200 words. Writing significantly more or less can affect your score.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which of these is an example of plain English in OET Speaking?",
        options=["'High blood pressure' instead of 'hypertension'",
                 "'Myocardial infarction'",
                 "'Idiopathic thrombocytopenic purpura'",
                 "'Cerebrovascular accident'"],
        correct_index=0,
        explanation="Always use plain English with patients. 'High blood pressure' is better than 'hypertension' in patient communication.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does the OET Listening Part A test?",
        options=["Note-completion during a patient consultation", 
                 "Lecture comprehension",
                 "General English conversation",
                 "News broadcast understanding"],
        correct_index=0,
        explanation="OET Listening Part A involves completing healthcare professional notes while listening to a patient consultation.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In OET Speaking, what should you do if you don't understand a task on the role card?",
        options=["Use your professional judgment to address what seems most appropriate", 
                 "Ask the examiner to explain",
                 "Skip that task completely",
                 "Stop the role-play"],
        correct_index=0,
        explanation="You cannot ask for clarification during the role-play. Use your professional judgment and address tasks as best you can.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which section of OET Reading involves matching statements to paragraphs?",
        options=["Part C (expeditious reading - matching)", 
                 "Part A (quick recall)",
                 "Part B (careful reading)",
                 "None of the above"],
        correct_index=0,
        explanation="OET Reading Part C includes matching statements to paragraphs, testing your ability to identify gist and specific information.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In an OET referral letter, where should the purpose of referral be stated?",
        options=["In the opening paragraph", 
                 "In the closing paragraph only",
                 "In the middle, mixed with other information",
                 "In a separate appendix"],
        correct_index=0,
        explanation="State the purpose of referral clearly in the opening paragraph so the reader immediately knows why you're writing.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Which of these opening phrases is appropriate for OET Speaking?",
        options=["'Hello, I'm Nurse [Name], one of the nurses here today.'",
                 "'Hey, what's up? I'm your nurse.'",
                 "'Sit down. I need to ask you some questions.'",
                 "'Okay, let's get this over with.'"],
        correct_index=0,
        explanation="Professional, warm, and clear introductions score well. Be friendly but maintain professional boundaries.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does ICE stand for in patient consultation?",
        options=["Ideas, Concerns, Expectations", 
                 "Immediate Care Evaluation",
                 "Internal Clinical Examination",
                 "Intensive Care Entry"],
        correct_index=0,
        explanation="ICE = Ideas, Concerns, Expectations. Checking these shows patient-centered care and improves your Relationship Building score.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In OET Writing, should you use bullet points?",
        options=["No, write in continuous prose (paragraphs)", 
                 "Yes, bullet points are preferred",
                 "Only for medication lists",
                 "Either is acceptable"],
        correct_index=0,
        explanation="OET Writing requires continuous prose (paragraphs). Bullet points are not appropriate for a professional letter.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="How is OET Speaking scored?",
        options=["On 9 criteria including intelligibility, fluency, and relationship building", 
                 "Just on grammar accuracy",
                 "Only on vocabulary usage",
                 "By word count"],
        correct_index=0,
        explanation="OET Speaking uses 9 criteria: Intelligibility, Fluency, Appropriateness, Resources of Grammar, Relationship Building, etc.",
        category="oet",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you include in the closing of an OET referral letter?",
        options=["A polite request for follow-up and your contact details", 
                 "Your personal social media handles",
                 "A complaint about workload",
                 "Nothing — just stop writing"],
        correct_index=0,
        explanation="Close professionally: thank the reader, request any follow-up if needed, and include your name and position.",
        category="oet",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which healthcare professions can take OET?",
        options=["Nursing, Medicine, Dentistry, Pharmacy, Physiotherapy, and more",
                 "Only nursing",
                 "Only doctors",
                 "Any profession"],
        correct_index=0,
        explanation="OET is available for 12 healthcare professions including Nursing, Medicine, Dentistry, Pharmacy, Physiotherapy, etc.",
        category="oet",
        difficulty="easy",
    ),
]


# ============================================================
# OSCE QUIZ QUESTIONS
# ============================================================

OSCE_QUESTIONS = [
    QuizQuestion(
        question="What does OSCE stand for?",
        options=["Objective Structured Clinical Examination", 
                 "Oral Standardized Clinical Exam",
                 "Objective Surgical Competency Evaluation",
                 "Observed Structured Care Examination"],
        correct_index=0,
        explanation="OSCE = Objective Structured Clinical Examination. It uses standardized patients and stations to assess clinical skills.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does the ABCDE approach prioritize FIRST?",
        options=["Airway", 
                 "Breathing",
                 "Circulation",
                 "Disability"],
        correct_index=0,
        explanation="ABCDE: Airway → Breathing → Circulation → Disability → Exposure. Airway always comes first — without it, nothing else matters.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="How long does a typical OSCE station last?",
        options=["5-10 minutes", 
                 "30 minutes",
                 "1 hour",
                 "2 minutes"],
        correct_index=0,
        explanation="Most OSCE stations are 5-10 minutes long, including reading time and performance time. NMC OSCE stations are typically 8-15 minutes.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does SBAR stand for?",
        options=["Situation, Background, Assessment, Recommendation", 
                 "Systematic Background Analysis Report",
                 "Standardized Bedside Assessment Routine",
                 "Symptoms, Bloodwork, Assessment, Results"],
        correct_index=0,
        explanation="SBAR is a structured communication tool: Situation → Background → Assessment → Recommendation. Use it for all handovers.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In OSCE history taking, what does SOCRATES help assess?",
        options=["Pain characteristics", 
                 "Mental health status",
                 "Social history",
                 "Drug allergies"],
        correct_index=0,
        explanation="SOCRATES assesses pain: Site, Onset, Character, Radiation, Associations, Time, Exacerbating/Relieving factors, Severity.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you ALWAYS do at the start of any OSCE station?",
        options=["Wash hands and introduce yourself", 
                 "Start the examination immediately",
                 "Read the patient notes silently",
                 "Ask for the examiner's help"],
        correct_index=0,
        explanation="Hand hygiene + introduction (name, role) + patient consent are fundamental and are checked in almost every station.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does the NEWS2 score assess?",
        options=["Physiological deterioration (National Early Warning Score)", 
                 "Patient satisfaction",
                 "Nurse workload",
                 "Hospital cleanliness"],
        correct_index=0,
        explanation="NEWS2 = National Early Warning Score 2. It tracks respiration rate, O2 saturation, BP, pulse, consciousness, temperature.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In the SPIKES model for breaking bad news, what does 'S' stand for?",
        options=["Setting up the interview (right environment)", 
                 "Shocking the patient",
                 "Starting immediately",
                 "Sitting far away"],
        correct_index=0,
        explanation="SPIKES: Setting → Perception → Invitation → Knowledge → Emotions → Strategy. Proper setting = privacy, seating, no interruptions.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="During a physical examination, what is the correct order?",
        options=["Inspection → Palpation → Percussion → Auscultation", 
                 "Auscultation → Percussion → Palpation → Inspection",
                 "Palpation → Inspection → Auscultation → Percussion",
                 "Percussion → Auscultation → Palpation → Inspection"],
        correct_index=0,
        explanation="IPPA: Inspect first, then Palpate, Percuss, and Auscultate last (especially for abdomen — palpation before auscultation alters bowel sounds).",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What is the correct compression-to-ventilation ratio for adult CPR?",
        options=["30 compressions : 2 ventilations", 
                 "15 compressions : 2 ventilations",
                 "30 compressions : 1 ventilation",
                 "15 compressions : 1 ventilation"],
        correct_index=0,
        explanation="Adult CPR = 30:2 compression-to-ventilation ratio. Compression depth 5-6cm, rate 100-120/min.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In an OSCE prescription station, what must you ALWAYS include?",
        options=["Drug name, dose, route, frequency, date, and your signature", 
                 "Only the drug name",
                 "Your home address",
                 "Patient's date of birth only"],
        correct_index=0,
        explanation="A complete prescription needs: drug name, dose, route, frequency, start date, prescriber name/signature, and patient identifiers.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What is the purpose of the 'show how' technique in OSCE?",
        options=["To demonstrate procedures when you can't perform them on the patient", 
                 "To show off your skills",
                 "To skip a station",
                 "To ask the examiner for help"],
        correct_index=0,
        explanation="In some stations, you verbally explain AND demonstrate on yourself or a model instead of the patient (e.g., inhaler technique).",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you do if you make a mistake during an OSCE station?",
        options=["Acknowledge it, correct it if possible, and continue confidently", 
                 "Pretend it didn't happen",
                 "Stop and ask to restart",
                 "Leave the station"],
        correct_index=0,
        explanation="Examiners appreciate self-awareness. Acknowledge the error, correct it professionally, and move on. Don't dwell on it.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which vital sign is typically checked FIRST in a routine assessment?",
        options=["Any is acceptable, but many start with pulse/heart rate", 
                 "Blood glucose",
                 "Weight",
                 "Urine output"],
        correct_index=0,
        explanation="There's no absolute rule, but standard vital signs (NEWS2) include: RR, SpO2, BP, pulse, temperature, and consciousness level.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="In a medication administration OSCE, what are the '5 Rights'?",
        options=["Right patient, drug, dose, route, time", 
                 "Right nurse, patient, drug, doctor, time",
                 "Right room, bed, chart, drug, time",
                 "Right hospital, ward, patient, drug, dose"],
        correct_index=0,
        explanation="5 Rights: Right Patient, Right Drug, Right Dose, Right Route, Right Time. Some add: Right Documentation and Right to Refuse.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does GCS stand for and assess?",
        options=["Glasgow Coma Scale — level of consciousness", 
                 "General Clinical Score",
                 "Global Care Standard",
                 "Graduated Competency Score"],
        correct_index=0,
        explanation="GCS = Glasgow Coma Scale. Assesses Eye opening (1-4), Verbal response (1-5), and Motor response (1-6). Total 3-15.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What is the correct way to dispose of a used needle?",
        options=["Immediately into a sharps bin — never recap", 
                 "Recap it first, then dispose",
                 "Put it in the regular trash",
                 "Leave it on the trolley for someone else"],
        correct_index=0,
        explanation="Never recap needles. Dispose immediately into a sharps container at point of use. This prevents needle-stick injuries.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="In OSCE communication stations, what does 'active listening' involve?",
        options=["Paraphrasing, clarifying, and using verbal/non-verbal cues to show engagement", 
                 "Interrupting to give advice quickly",
                 "Staying silent the whole time",
                 "Checking your phone while listening"],
        correct_index=0,
        explanation="Active listening: eye contact, nodding, paraphrasing ('So what you're saying is...'), and open body language.",
        category="osce",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is 'differential diagnosis' in OSCE history taking?",
        options=["A list of possible conditions that could explain the symptoms", 
                 "The final confirmed diagnosis",
                 "A medication difference between patients",
                 "The difference between two nurses"],
        correct_index=0,
        explanation="Differential diagnosis = ranking possible conditions by probability based on the patient's presentation.",
        category="osce",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What should you do when a patient refuses treatment in an OSCE station?",
        options=["Respect their decision, explore concerns, document, and offer alternatives", 
                 "Force them to accept treatment",
                 "Ignore their refusal and proceed",
                 "Call security immediately"],
        correct_index=0,
        explanation="Patients have the right to refuse. Explore their concerns, provide information, respect autonomy, document thoroughly, and escalate if needed.",
        category="osce",
        difficulty="medium",
    ),
]


# ============================================================
# NHS QUIZ QUESTIONS
# ============================================================

NHS_QUESTIONS = [
    QuizQuestion(
        question="How many core values does the NHS have?",
        options=["6 values", "4 values", "8 values", "10 values"],
        correct_index=0,
        explanation="The NHS has 6 core values: Working together for patients, Respect and dignity, Commitment to quality, Compassion, Improving lives, Everyone counts.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does NMC stand for?",
        options=["Nursing and Midwifery Council", 
                 "National Medical Council",
                 "Nursing Management Committee",
                 "National Midwifery Center"],
        correct_index=0,
        explanation="NMC = Nursing and Midwifery Council. It regulates nurses and midwives in the UK and maintains the professional register.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Which IELTS score does the NMC currently require?",
        options=["7.0 in all four sections", 
                 "6.5 overall average",
                 "8.0 in all sections",
                 "6.0 is sufficient"],
        correct_index=0,
        explanation="NMC requires IELTS Academic 7.0 in Listening, Reading, Writing, AND Speaking individually. No averaging allowed.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the CBT in NMC registration?",
        options=["Computer Based Test of nursing knowledge", 
                 "Clinical Blood Test",
                 "Career Background Test",
                 "Competency Board Test"],
        correct_index=0,
        explanation="CBT = Computer Based Test. It's a 120-question multiple choice exam testing nursing knowledge, administered by Pearson VUE.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does the STAR method stand for in NHS interviews?",
        options=["Situation, Task, Action, Result", 
                 "Start, Talk, Answer, Reflect",
                 "Summary, Target, Action, Review",
                 "Situation, Time, Action, Response"],
        correct_index=0,
        explanation="STAR: Situation (set context), Task (your responsibility), Action (what YOU did), Result (positive outcome). Essential for NHS interviews!",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is NHS Band 5?",
        options=["Newly qualified staff nurse (entry level)", 
                 "Senior nurse / Ward manager",
                 "Healthcare assistant",
                 "Hospital director"],
        correct_index=0,
        explanation="Band 5 is the entry-level registered nurse position. Band 6 = senior nurse, Band 7 = ward manager, Band 8 = matron/director.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is revalidation in the NMC?",
        options=["A process to renew registration every 3 years", 
                 "A hospital inspection",
                 "A degree re-assessment",
                 "A drug calculation test"],
        correct_index=0,
        explanation="NMC Revalidation happens every 3 years. Requirements: 450 practice hours, 35 CPD hours, 5 feedback pieces, reflective discussion, professional indemnity.",
        category="nhs",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What is the NHS number used for?",
        options=["A unique 10-digit identifier for each patient", 
                 "A nurse's payroll number",
                 "A hospital's phone number",
                 "A ward's patient capacity"],
        correct_index=0,
        explanation="The NHS Number is a unique 10-digit identifier assigned to every patient registered with the NHS in England and Wales.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is safeguarding in the NHS?",
        options=["Protecting vulnerable people from abuse or neglect", 
                 "Keeping hospital doors locked",
                 "Guarding medical equipment",
                 "Protecting hospital revenue"],
        correct_index=0,
        explanation="Safeguarding means protecting children and vulnerable adults from abuse, neglect, and harm. Every NHS staff member has a safeguarding duty.",
        category="nhs",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is duty of candour?",
        options=["The legal duty to be open and honest when things go wrong", 
                 "A nursing shift schedule",
                 "A patient's right to refuse care",
                 "A medication dispensing protocol"],
        correct_index=0,
        explanation="Duty of Candour (regulated by CQC) requires healthcare providers to be open with patients when things go wrong, apologize, and explain.",
        category="nhs",
        difficulty="medium",
    ),
]


# ============================================================
# VOCABULARY QUIZ QUESTIONS
# ============================================================

VOCAB_QUESTIONS = [
    QuizQuestion(
        question="What does 'exacerbate' mean?",
        options=["To make a problem worse", "To solve completely", "To ignore", "To prevent"],
        correct_index=0,
        explanation="'Exacerbate' means to make a problem worse. E.g., 'Stress can exacerbate hypertension.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does 'alleviate' mean?",
        options=["To make suffering less severe", "To increase pain", "To cause", "To ignore"],
        correct_index=0,
        explanation="'Alleviate' means to reduce severity. E.g., 'The medication alleviated her symptoms.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Choose the correct meaning of 'fluctuate':",
        options=["To rise and fall irregularly", "To remain constant", "To disappear", "To accelerate"],
        correct_index=0,
        explanation="'Fluctuate' means to vary irregularly. E.g., 'Blood pressure can fluctuate throughout the day.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What does 'chronic' mean in medical context?",
        options=["Long-lasting or persistent", "Sudden and severe", "Minor and temporary", "Cured completely"],
        correct_index=0,
        explanation="'Chronic' = long-lasting/persistent (months or years). 'Acute' = sudden/severe but short duration.",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the meaning of 'deteriorate'?",
        options=["To become progressively worse", "To improve rapidly", "To stay the same", "To heal completely"],
        correct_index=0,
        explanation="'Deteriorate' = to get worse. E.g., 'His condition began to deteriorate overnight.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Choose the best synonym for 'ubiquitous':",
        options=["Omnipresent / found everywhere", "Rare", "Expensive", "Complex"],
        correct_index=0,
        explanation="'Ubiquitous' = present everywhere. E.g., 'Smartphones are now ubiquitous in healthcare settings.'",
        category="vocabulary",
        difficulty="hard",
    ),
    QuizQuestion(
        question="What does 'mitigate' mean?",
        options=["To make less severe", "To make worse", "To cancel", "To postpone"],
        correct_index=0,
        explanation="'Mitigate' = to reduce severity. E.g., 'Steps were taken to mitigate the risk of infection.'",
        category="vocabulary",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What is the meaning of 'subsequent'?",
        options=["Following in time or order", "Previous", "Simultaneous", "Unrelated"],
        correct_index=0,
        explanation="'Subsequent' = following after. E.g., 'Subsequent tests confirmed the initial diagnosis.'",
        category="vocabulary",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What does 'transient' mean?",
        options=["Lasting only a short time", "Permanent", "Severe", "Gradual"],
        correct_index=0,
        explanation="'Transient' = temporary, brief. E.g., 'The patient reported transient episodes of dizziness.'",
        category="vocabulary",
        difficulty="medium",
    ),
    QuizQuestion(
        question="Choose the correct meaning of 'viable':",
        options=["Feasible or capable of working successfully", "Impossible", "Damaged", "Temporary"],
        correct_index=0,
        explanation="'Viable' = workable, feasible. E.g., 'Surgery is a viable treatment option for this patient.'",
        category="vocabulary",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What does 'imminent' mean?",
        options=["About to happen very soon", "Already happened", "Unlikely to happen", "Happening slowly"],
        correct_index=0,
        explanation="'Imminent' = about to occur. E.g., 'The patient's discharge is imminent.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the meaning of 'lethargic'?",
        options=["Lacking energy; drowsy", "Very active", "In pain", "Confused"],
        correct_index=0,
        explanation="'Lethargic' = sluggish, lacking energy. E.g., 'The patient appeared lethargic and difficult to rouse.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="Choose the best synonym for 'intricate':",
        options=["Complex and detailed", "Simple", "Large", "Broken"],
        correct_index=0,
        explanation="'Intricate' = complex with many details. E.g., 'The brain has intricate neural pathways.'",
        category="vocabulary",
        difficulty="medium",
    ),
    QuizQuestion(
        question="What does 'advocate' mean as a verb?",
        options=["To publicly support or recommend", "To criticize", "To ignore", "To postpone"],
        correct_index=0,
        explanation="'Advocate' (verb) = to support or speak in favor of. E.g., 'Nurses advocate for patient safety.'",
        category="vocabulary",
        difficulty="easy",
    ),
    QuizQuestion(
        question="What is the meaning of 'stringent'?",
        options=["Strict and precise", "Loose and flexible", "Optional", "Simple"],
        correct_index=0,
        explanation="'Stringent' = strict, exacting. E.g., 'The hospital has stringent infection control policies.'",
        category="vocabulary",
        difficulty="medium",
    ),
]


# ============================================================
# COMBINE ALL QUESTIONS
# ============================================================

ALL_QUESTIONS: List[QuizQuestion] = (
    IELTS_QUESTIONS 
    + OET_QUESTIONS 
    + OSCE_QUESTIONS 
    + NHS_QUESTIONS 
    + VOCAB_QUESTIONS
)

# Track which questions have been used recently (per chat)
_used_questions: dict[int, list[int]] = {}


def get_random_question(chat_id: int = 0) -> tuple[QuizQuestion, List[str], int]:
    """
    Get a random quiz question for a specific chat.
    Returns: (question, shuffled_options, new_correct_index)
    """
    global _used_questions
    
    if chat_id not in _used_questions:
        _used_questions[chat_id] = []
    
    # Avoid recently used questions (keep last 20)
    available = [i for i in range(len(ALL_QUESTIONS)) if i not in _used_questions[chat_id]]
    
    if not available:
        # Reset if all questions used
        _used_questions[chat_id] = []
        available = list(range(len(ALL_QUESTIONS)))
    
    q_idx = random.choice(available)
    _used_questions[chat_id].append(q_idx)
    _used_questions[chat_id] = _used_questions[chat_id][-20:]  # Keep last 20
    
    question = ALL_QUESTIONS[q_idx]
    shuffled_options, new_correct = question.get_shuffled_options()
    
    return question, shuffled_options, new_correct


def get_quiz_by_category(category: str, chat_id: int = 0) -> tuple[QuizQuestion, List[str], int]:
    """Get a random question from a specific category."""
    category_map = {
        "ielts": IELTS_QUESTIONS,
        "oet": OET_QUESTIONS,
        "osce": OSCE_QUESTIONS,
        "nhs": NHS_QUESTIONS,
        "vocabulary": VOCAB_QUESTIONS,
    }
    
    questions = category_map.get(category.lower(), ALL_QUESTIONS)
    question = random.choice(questions)
    shuffled_options, new_correct = question.get_shuffled_options()
    return question, shuffled_options, new_correct


def format_question(question: QuizQuestion, options: List[str], question_num: int = 1) -> str:
    """Format a quiz question for Telegram display."""
    category_emoji = {
        "ielts": "📝",
        "oet": "🏥",
        "osce": "🩺",
        "nhs": "🏥",
        "vocabulary": "📖",
    }
    
    diff_emoji = {
        "easy": "🟢",
        "medium": "🟡",
        "hard": "🔴",
    }
    
    emoji = category_emoji.get(question.category, "❓")
    diff = diff_emoji.get(question.difficulty, "⚪")
    
    options_text = "\n".join(
        f"{chr(65+i)}. {opt}" for i, opt in enumerate(options)
    )
    
    return (
        f"{emoji} <b>Daily Quiz — Question {question_num}</b> {diff}\n"
        f"Category: {question.category.upper()} | Difficulty: {question.difficulty.capitalize()}\n\n"
        f"❓ <b>{question.question}</b>\n\n"
        f"{options_text}\n\n"
        f"💡 <i>Reply with A, B, C, or D</i>"
    )


def format_answer(question: QuizQuestion, user_answer: str, correct_index: int, shuffled_options: List[str]) -> str:
    """Format the answer feedback."""
    answer_map = {"a": 0, "b": 1, "c": 2, "d": 3}
    user_idx = answer_map.get(user_answer.lower().strip(), -1)
    
    if user_idx == -1:
        return "❌ Please reply with A, B, C, or D."
    
    is_correct = user_idx == correct_index
    correct_letter = chr(65 + correct_index)
    
    if is_correct:
        return (
            f"✅ <b>Correct!</b> The answer is {correct_letter}. {shuffled_options[correct_index]}\n\n"
            f"📖 <b>Explanation:</b> {question.explanation}\n\n"
            f"🎯 Want another? Use /quiz!"
        )
    else:
        return (
            f"❌ <b>Not quite!</b> You chose {user_answer.upper()}.\n"
            f"✅ The correct answer is {correct_letter}. {shuffled_options[correct_index]}\n\n"
            f"📖 <b>Explanation:</b> {question.explanation}\n\n"
            f"💪 Keep practicing! Try /quiz again or use /vocab to build your vocabulary."
        )


def get_quiz_stats() -> str:
    """Get statistics about the quiz database."""
    categories = {}
    for q in ALL_QUESTIONS:
        categories[q.category] = categories.get(q.category, 0) + 1
    
    stats_text = "\n".join(f"• {cat.upper()}: {count} questions" for cat, count in sorted(categories.items()))
    
    return (
        f"📊 <b>Quiz Database Statistics</b>\n\n"
        f"🎯 <b>Total Questions:</b> {len(ALL_QUESTIONS)}\n\n"
        f"📁 <b>By Category:</b>\n"
        f"{stats_text}\n\n"
        f"💡 New questions added regularly!"
    )
