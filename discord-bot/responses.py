"""
AngloTec Study Bot - Response Database
========================================
100+ keyword-triggered responses for IELTS, OET, OSCE, PLAB, and NHS topics.
Each response provides genuine value first, with a subtle tool link when relevant.
"""

import random
from config import TOOL_LINKS

# ═══════════════════════════════════════════════════════════════════════════════
# RESPONSE DATABASE
# ═══════════════════════════════════════════════════════════════════════════════
# Each entry: {
#   "keywords": ["word1", "word2"],
#   "response": "Helpful text...",
#   "category": "ielts|oet|osce|nhs|general",
#   "link_key": "optional_tool_link_key",
#   "link_text": "Natural sentence introducing the link",
# }

RESPONSES = [

    # ═══════════════════════════════════════════════════════════════════════
    # IELTS - SPEAKING (15 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["ielts speaking", "speaking test", "speaking worried", "speaking nervous"],
        "response": (
            "Speaking is often the most nerve-wracking part! A few tips: practice answering aloud daily, "
            "record yourself and listen back, and use the 'PREP' structure — Point, Reason, Example, Point. "
            "Don't memorise scripts; examiners can tell. Focus on fluency and natural conversation instead."
        ),
        "category": "ielts",
        "link_key": "ielts_speaking",
        "link_text": "We built a free IELTS speaking practice tool with common topics if you want to rehearse: {link}",
    },
    {
        "keywords": ["speaking part 2", "cue card", "describe a"],
        "response": (
            "For Part 2 cue cards, use the 1-minute prep time wisely! Jot down 3-4 bullet points, not full sentences. "
            "Structure your answer: introduce the topic, describe it in detail, share a personal memory or feeling, "
            "and wrap up with a concluding sentence. Aim to speak for the full 2 minutes."
        ),
        "category": "ielts",
        "link_key": "ielts_speaking",
        "link_text": "You can practise with sample cue cards here: {link}",
    },
    {
        "keywords": ["speaking part 3", "discussion", "abstract questions"],
        "response": (
            "Part 3 is where band 7+ answers shine! Use phrases like 'That's an interesting question...' to buy thinking time. "
            "Give balanced arguments — discuss both sides. Use comparatives, conditionals, and speculative language "
            "('might', 'could', 'it's possible that'). This shows advanced grammar range."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["fluency", "fluent", "um uh", "hesitation"],
        "response": (
            "Fluency is about smoothness, not speed! It's okay to pause — just do it at sentence boundaries, not mid-word. "
            "Replace filler sounds (um, uh) with natural phrases: 'That's a good question', 'Let me think', 'I suppose'. "
            "Practice shadowing — listen to a native speaker and repeat simultaneously."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["pronunciation", "accent", "clear speech"],
        "response": (
            "You don't need a British accent! The examiner cares about clarity and intelligibility. "
            "Focus on word stress, sentence stress, and intonation. Record yourself reading a passage, "
            "then compare with a native speaker recording. Chunk your speech into thought groups — pause naturally."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["speaking score", "speaking band", "low speaking"],
        "response": (
            "If your speaking score is stuck, identify which criterion is pulling you down: Fluency & Coherence, "
            "Lexical Resource, Grammatical Range, or Pronunciation. Most people lose marks on grammar range — "
            "make sure you're using a mix of simple, compound, and complex sentences with varied tenses."
        ),
        "category": "ielts",
        "link_key": "ielts_speaking",
        "link_text": "There's a free speaking scoring rubric breakdown here: {link}",
    },
    {
        "keywords": ["nervous speaking", "scared speaking", "speaking anxiety"],
        "response": (
            "Test anxiety is completely normal! Try this: practise in front of a mirror, then with a friend, "
            "then record yourself. Gradually build up. On test day, take a deep breath before entering — "
            "treat the examiner like a friendly colleague, not an interrogator. They WANT you to do well!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["ielts part 1", "speaking introduction", "hometown", "job"],
        "response": (
            "Part 1 is all about YOU — your hometown, work, studies, hobbies. Keep answers concise (2-3 sentences) "
            "but don't give one-word answers. Add a little extra detail or a reason. For example, instead of 'I like reading', "
            "say 'I enjoy reading because it helps me relax after a long day at work, and I particularly love mystery novels.'"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["speaking topics", "common topics", "frequent questions"],
        "response": (
            "Common IELTS Speaking topics include: hometown, work/study, daily routine, transportation, "
            "food, weather, hobbies, technology, travel, and education. Part 2 often covers describing people, "
            "places, events, or objects. Part 3 extends these into broader discussions about society and culture."
        ),
        "category": "ielts",
        "link_key": "ielts_speaking",
        "link_text": "We compiled the most common topics with sample answers here: {link}",
    },
    {
        "keywords": ["speaking practice partner", "practice speaking", "partner"],
        "response": (
            "Finding a speaking partner is one of the best things you can do! Try language exchange apps, "
            "IELTS study groups on Discord, or even practise with a family member. If you can't find a partner, "
            "record yourself answering questions and play them back. Consistency beats intensity — 20 minutes daily is better than 2 hours once a week."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["vocabulary speaking", "words speaking", "lexical resource"],
        "response": (
            "To boost your Lexical Resource score, avoid repeating words. Instead of 'very good', try 'excellent', "
            "'outstanding', 'remarkable'. Learn topic-specific collocations — not just isolated words. For health topics: "
            "'seek medical advice', 'undergo treatment', 'make a full recovery'. For education: 'acquire knowledge', "
            "'broaden horizons', 'stimulating learning environment'."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["speaking idp", "speaking british council", "test center"],
        "response": (
            "Whether you take IELTS with IDP or British Council, the Speaking test format is identical — "
            "it's standardised worldwide. The only difference might be the test centre environment. "
            "Book your test at a centre you're comfortable getting to, and don't stress about which organisation runs it."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["extend answers", "longer answers", "short answers"],
        "response": (
            "If your answers are too short, use the WHY-HOW-WHEN technique. After every statement, ask yourself: "
            "'Why is that?' 'How did that happen?' 'When did that occur?' This naturally extends your answers. "
            "Example: 'I enjoy cooking.' → 'I enjoy cooking because it helps me relax after work, and I especially love trying new recipes on weekends.'"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["complex sentences", "grammar speaking", "grammatical range"],
        "response": (
            "To show grammatical range in speaking, use a mix of: conditionals ('If I had more time, I would...'), "
            "relative clauses ('The city where I live is...'), present perfect ('I've always believed that...'), "
            "and passive voice ('This issue is often discussed...'). Don't force them — weave them in naturally."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["speaking 7", "speaking 8", "speaking band 7", "band 7 speaking"],
        "response": (
            "For Band 7+ Speaking, you need: fluency without noticeable effort, a wide range of vocabulary used flexibly, "
            "a mix of simple and complex grammar with mostly error-free sentences, and clear pronunciation. "
            "The key differentiator is the ability to discuss abstract topics in Part 3 with depth and nuance."
        ),
        "category": "ielts",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # IELTS - WRITING (15 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["ielts writing", "writing test", "task 1", "task 2"],
        "response": (
            "IELTS Writing has two tasks: Task 1 (150 words, 20 mins) and Task 2 (250 words, 40 mins). "
            "Task 2 carries twice the weight, so never spend too long on Task 1! For Task 2, always plan for 5 minutes "
            "before writing — a clear structure (introduction, 2 body paragraphs, conclusion) is essential for a high score."
        ),
        "category": "ielts",
        "link_key": "ielts_writing",
        "link_text": "There's a free writing checklist here that a lot of people find useful: {link}",
    },
    {
        "keywords": ["writing task 1", "graph", "chart", "diagram", "describe"],
        "response": (
            "For Task 1 Academic: Start with an overview (the main trend, highest/lowest values, key comparison). "
            "Don't list every data point — group similar trends. Use comparison language: 'significantly higher than', "
            "'nearly doubled', 'remained stable', 'a sharp decline'. No opinion — just describe what you see!"
        ),
        "category": "ielts",
        "link_key": "ielts_writing",
        "link_text": "You can find sample Task 1 responses with band scores here: {link}",
    },
    {
        "keywords": ["writing task 2", "essay", "opinion essay", "discussion essay"],
        "response": (
            "Task 2 essays need a clear position throughout. Start with a hook + paraphrase the question + state your opinion. "
            "Each body paragraph: topic sentence, explanation, example, link back. Use cohesive devices naturally: "
            "'Furthermore', 'On the other hand', 'Consequently', 'For instance'. Avoid overusing 'In my opinion' — vary your language."
        ),
        "category": "ielts",
        "link_key": "ielts_writing",
        "link_text": "We put together a Task 2 essay template guide here: {link}",
    },
    {
        "keywords": ["agree disagree", "opinion essay", "to what extent"],
        "response": (
            "For 'To what extent do you agree/disagree' essays, pick a clear side — sitting on the fence makes it harder! "
            "Structure: Introduction (state position), Body 1 (main reason + example), Body 2 (second reason + example OR acknowledge the other side briefly), "
            "Conclusion (restate position). Be decisive throughout!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["both views", "discuss both views", "advantages disadvantages"],
        "response": (
            "For 'Discuss both views' essays, dedicate one paragraph to EACH view, then give your own opinion in the "
            "conclusion (or a third paragraph). Use balanced language: 'Proponents argue that...', 'Conversely, others believe...', "
            "'From my perspective...'. This shows you can consider multiple angles objectively."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["problem solution", "causes and solutions", "problem and solution"],
        "response": (
            "For Problem-Solution essays, clearly identify 1-2 problems in the first body paragraph, then propose "
            "matching solutions in the second. Use cause-effect language: 'This stems from...', 'One viable solution would be...', "
            "'This could be addressed by...'. Make sure your solutions are practical and directly linked to the problems!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["cohesion coherence", "cohesive", "linking words", "flow"],
        "response": (
            "Cohesion & Coherence is about how well your ideas connect. Don't just throw in linking words — use them purposefully. "
            "Adding info: 'Furthermore', 'In addition'. Contrasting: 'However', 'Nevertheless'. Causing: 'Consequently', 'As a result'. "
            "Exemplifying: 'For instance', 'A case in point'. Each paragraph should flow logically from the previous one."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["writing vocabulary", "essay vocabulary", "academic words"],
        "response": (
            "Boost your writing vocabulary with academic collocations: 'play a pivotal role', 'a contentious issue', "
            "'a significant proportion', 'widespread concern', 'tangible benefits'. Avoid informal language: use 'children' not 'kids', "
            "'considerable' not 'a lot of', 'individuals' not 'people' (in formal contexts). Learn 10 new collocations per week!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["word count", "not enough words", "too short", "250 words"],
        "response": (
            "If you struggle with word count, you're probably not developing your ideas enough. Use the PEE method: "
            "Point (topic sentence), Explanation (why is this true?), Example (real or hypothetical). Each body paragraph "
            "should be 80-100 words. Aim for 270-300 words in Task 2 — going slightly over is fine, but under 250 loses marks."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["writing time", "run out of time", "time management writing"],
        "response": (
            "Time management is crucial! Recommended: 2 minutes reading/planning Task 2, 5 minutes outlining, "
            "30 minutes writing, 3 minutes reviewing. For Task 1: 3 minutes analysing, 15 minutes writing, 2 minutes checking. "
            "Always leave time to check spelling and grammar — silly errors cost marks!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["general writing", "letter writing", "gt writing", "general training"],
        "response": (
            "General Training Task 1 is a letter (formal, semi-formal, or informal). Match your tone to the task: "
            "formal for complaints/applications ('I am writing to express my dissatisfaction...'), "
            "informal for friends ('It was great to hear from you!'). Remember all 3 bullet points from the prompt must be addressed."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["introduction", "how to start", "opening sentence"],
        "response": (
            "Never copy the question word-for-word in your introduction! Paraphrase it using synonyms and different sentence structures. "
            "Example: 'Some people think that the best way to reduce crime is to give longer prison sentences.' → "
            "'It is argued that extending prison terms is the most effective method of decreasing criminal activity.'"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["conclusion", "how to end", "closing paragraph"],
        "response": (
            "Your conclusion should summarise your main points and restate your opinion clearly. DON'T introduce new ideas here! "
            "Use phrases like: 'In conclusion', 'To sum up', 'Overall'. Keep it 2-3 sentences. Make sure it directly answers the essay question."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["writing 7", "band 7 writing", "writing score 7"],
        "response": (
            "Band 7 Writing requires: a clear position throughout, logically organised ideas with good paragraphing, "
            "a range of cohesive devices used appropriately, sufficient vocabulary with some less common lexical items, "
            "and a mix of simple and complex sentence structures with good grammar control. Plan your essay — it makes a huge difference!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["writing feedback", "check my essay", "essay correction"],
        "response": (
            "Getting feedback on your essays is incredibly valuable! When self-checking, use the official IELTS rubric: "
            "Task Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy. Check each criterion separately. "
            "Better yet, ask a study partner to review your work using these criteria."
        ),
        "category": "ielts",
        "link_key": "ielts_writing",
        "link_text": "There's a detailed self-assessment checklist here: {link}",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # IELTS - READING (10 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["ielts reading", "reading test", "reading difficult"],
        "response": (
            "IELTS Reading has 3 passages with 40 questions in 60 minutes — time pressure is the biggest challenge! "
            "Skim first (2-3 mins per passage for gist), then scan for specific answers. Don't read every word. "
            "The answers appear in order for most question types (True/False/NG, gap-fill, matching)."
        ),
        "category": "ielts",
        "link_key": "ielts_reading",
        "link_text": "There's a free reading strategies guide here: {link}",
    },
    {
        "keywords": ["true false not given", "yes no not given", "tfng"],
        "response": (
            "The trickiest question type! Remember: True = the statement agrees with the passage. "
            "False = the statement contradicts the passage. NOT GIVEN = the information isn't there at all — "
            "don't overthink it! If you can't find it after scanning, it's probably NG. Students often confuse False and NG."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["matching headings", "paragraph headings", "choose heading"],
        "response": (
            "For matching headings, read the paragraph FIRST, then look at the headings — not the other way around! "
            "Focus on the main idea (usually in the first and last sentences). Watch out for distractors that match "
            "a detail but not the overall theme. Cross off used headings to narrow choices."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["reading time", "run out of time reading", "timing reading"],
        "response": (
            "Time management for Reading: Spend 15-20 minutes per passage. If a question takes too long, skip it and come back. "
            "Do the easier question types first (gap-fill, short answer) before harder ones (matching, TFNG). "
            "Transfer all answers to the answer sheet in the last 5 minutes — there's no extra time for this in the paper test!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["scanning", "skimming", "reading technique"],
        "response": (
            "Skimming = reading quickly for the main idea (read first/last sentences of each paragraph). "
            "Scanning = looking for specific information (names, dates, numbers, keywords). "
            "Use both: Skim the passage first (2-3 mins), then scan for each answer. Underline key words in the questions before you start!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["reading vocabulary", "dont understand", "difficult words"],
        "response": (
            "Don't panic if you see unknown words! Use context clues — look at the surrounding sentences for meaning. "
            "If it's not in a question, ignore it! For answers, copy words EXACTLY from the passage (spelling counts). "
            "Build your academic vocabulary daily — learn words in topics: environment, education, health, technology, science."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["gap fill", "sentence completion", "summary completion"],
        "response": (
            "For gap-fill/sentence completion: First, predict what type of word fits (noun, verb, adjective). "
            "Check the word limit (NO MORE THAN TWO WORDS AND/OR A NUMBER). The answers are in passage order. "
            "Make sure your completed sentence is grammatically correct — this is a great self-check!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["multiple choice reading", "choose correct answer"],
        "response": (
            "For multiple choice, eliminate obviously wrong answers first. Watch for distractors that use the EXACT same words "
            "from the passage — IELTS often paraphrases the correct answer. If unsure, go with your best guess — "
            "there's no negative marking!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["academic reading", "general reading", "academic vs general"],
        "response": (
            "Academic Reading passages are longer and more complex (journals, articles, textbooks). "
            "General Training Reading is more everyday (advertisements, notices, workplace documents). "
            "Both have 40 questions and 60 minutes. Nurses/doctors usually need Academic IELTS for NMC registration."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["reading practice", "improve reading", "better reading"],
        "response": (
            "Read authentic English daily: BBC News, The Guardian, New Scientist, National Geographic. "
            "Time yourself — aim to read 900 words in 5 minutes. Practice all question types, not just your favourites. "
            "Review your mistakes carefully — understand WHY you got it wrong, not just what the correct answer is."
        ),
        "category": "ielts",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # IELTS - LISTENING (8 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["ielts listening", "listening test", "listening difficult"],
        "response": (
            "IELTS Listening has 4 sections with 40 questions. The audio plays ONCE only — no repeats! "
            "Use the preparation time before each section to read ahead and predict answers. "
            "Check word limits carefully (NO MORE THAN ONE WORD, etc.) — answers that exceed the limit are marked wrong!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening section 3", "section 3", "discussion", "multiple speakers"],
        "response": (
            "Section 3 is usually a discussion between 2-4 people (often university-related). It's tricky because "
            "multiple people speak quickly! Focus on WHO says WHAT. Note down names or roles. Questions often ask "
            "about opinions and attitudes, not just facts."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening section 4", "section 4", "lecture", "monologue"],
        "response": (
            "Section 4 is a solo academic lecture — the hardest section! The speaker often paraphrases, so "
            "don't expect to hear the exact words from the question. Answers tend to come in quick succession at the end. "
            "Use the 30-second prep time to study the gap-fill questions carefully and predict word types."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening maps", "diagram labelling", "plan labelling"],
        "response": (
            "For map/plan/diagram labelling: Orient yourself first — find the starting point and directions (north, south, etc.). "
            "The speaker describes the route in order. Follow along on the map as they speak. "
            "Prepositions are key: 'to the left of', 'opposite', 'next to', 'at the end of'."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening spelling", "spell correctly", "spelling matters"],
        "response": (
            "Spelling matters in Listening! Wrong spelling = wrong answer. Common traps: double letters (accommodation, necessary), "
            "silent letters (Wednesday, foreign), and names/places that are spelled out in the audio. "
            "Always use British spelling (colour, organisation, centre) unless the audio clearly uses American spelling."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening practice", "improve listening", "better listening"],
        "response": (
            "Listen to English daily: podcasts (BBC 6 Minute English, TED Talks), news (BBC World Service), "
            "and YouTube channels. Practise with different accents: British, Australian, American, Canadian. "
            "Do active listening: pause and summarise what you heard, note down new vocabulary."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening prediction", "predict answers", "read ahead"],
        "response": (
            "Prediction is your superpower in Listening! Before the audio plays, read the questions and predict: "
            "What type of word fits? (noun, number, date, name). What's the grammatical form needed? "
            "This primes your brain to catch the right information when it comes up in the audio."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["listening transfer", "answer sheet", "extra time"],
        "response": (
            "Good news — you get 10 minutes at the end to transfer your answers to the answer sheet in the paper-based test! "
            "Use this time wisely: check spelling, grammar, and word limits. For computer-delivered IELTS, "
            "you type answers as you go and only get 2 minutes at the end to review."
        ),
        "category": "ielts",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # IELTS - GENERAL (8 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["band score", "overall band", "calculate band", "how is band calculated"],
        "response": (
            "Your overall IELTS band is the average of your 4 section scores (Listening, Reading, Writing, Speaking), "
            "rounded to the nearest 0.5 or whole band. Example: L7.0 + R7.5 + W6.5 + S7.0 = 28.0 / 4 = 7.0. "
            "If the average ends in .25, it rounds down; if it ends in .75, it rounds up."
        ),
        "category": "ielts",
        "link_key": "ielts_calculator",
        "link_text": "There's a free band score calculator here if you want to check: {link}",
    },
    {
        "keywords": ["ielts preparation", "prepare ielts", "study plan", "study schedule"],
        "response": (
            "A solid IELTS study plan: Week 1-2 = assess your level and identify weak areas. Week 3-6 = intensive practice "
            "on weakest skills. Week 7-8 = full mock tests under timed conditions. Study 1.5-2 hours daily. "
            "Mix all 4 skills — don't just practise what you're already good at!"
        ),
        "category": "ielts",
        "link_key": "study_planner",
        "link_text": "We built a free study planner you might find helpful: {link}",
    },
    {
        "keywords": ["ielts book", "ielts material", "cambridge ielts", "practice test"],
        "response": (
            "The Cambridge IELTS books (1-19) are the gold standard — they're official past papers. "
            "Start with the most recent books (17-19) as they're closest to current test format. "
            "Also check out: 'The Official Cambridge Guide to IELTS' for strategies, and 'English Grammar in Use' for grammar foundations."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["computer ielts", "paper ielts", "computer delivered", "paper based"],
        "response": (
            "Computer-delivered IELTS: results in 3-5 days, easier to edit writing, countdown timer on screen, "
            "headphones for listening. Paper-based: results in 13 days, more familiar format, 10 minutes to transfer listening answers. "
            "The test content is identical — choose the format you're more comfortable with!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["ielts validity", "how long valid", "ielts expire"],
        "response": (
            "IELTS results are valid for 2 years from the test date. After that, organisations may not accept them "
            "because language proficiency can change. If your IELTS has expired, you'll need to retake it. "
            "Plan your applications so your IELTS is still valid when you apply for NMC registration or university!"
        ),
        "category": "ielts",
    },
    {
        "keywords": ["failed ielts", "didnt pass", "low score", "disappointed"],
        "response": (
            "I'm sorry to hear that — but please don't give up! Many people don't get their target score on the first try. "
            "Analyse your score report: which section was lowest? Focus 70% of your effort there. "
            "Retake when you're ready — there's no limit on how many times you can sit IELTS. You've got this!"
        ),
        "category": "ielts",
        "link_key": "study_planner",
        "link_text": "A structured study plan can make a big difference: {link}",
    },
    {
        "keywords": ["ielts ukvi", "ukvi", "ielts for visa"],
        "response": (
            "IELTS for UKVI is specifically for UK visa applications. It's the same test content but with stricter "
            "security procedures (video recording, ID checks). If you're applying for NMC registration AND a visa, "
            "check with your employer or visa category whether you need IELTS Academic, IELTS UKVI, or OET."
        ),
        "category": "ielts",
    },
    {
        "keywords": ["nmc ielts", "nursing council ielts", "nmc requirement"],
        "response": (
            "For NMC registration, nurses need IELTS Academic with at least 7.0 in Reading, Listening, and Speaking, "
            "and at least 6.5 in Writing (with an overall 7.0). All scores must be from a single test sitting — "
            "NMC does NOT accept combined scores from multiple tests. Check the latest NMC requirements as they can change!"
        ),
        "category": "ielts",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # OET - WRITING (8 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["oet writing", "referral letter", "discharge letter", "transfer letter"],
        "response": (
            "OET Writing is a profession-specific letter (usually referral, discharge, or transfer) based on case notes. "
            "You have 45 minutes. Read the task carefully — note WHO you're writing to and WHY. "
            "Select only RELEVANT information from the case notes. Don't copy everything — prioritise based on the reader's needs!"
        ),
        "category": "oet",
        "link_key": "oet_writing",
        "link_text": "There's a free OET writing checklist here: {link}",
    },
    {
        "keywords": ["oet case notes", "select information", "what to include"],
        "response": (
            "The hardest part of OET Writing is selecting what to include! Ask yourself: 'Does the recipient NEED to know this?' "
            "Include: reason for referral, relevant medical history, current condition/medications, and any specific requests. "
            "Exclude: information the recipient already knows, routine procedures with normal results, and irrelevant social history."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet letter format", "letter structure", "paragraphs"],
        "response": (
            "Standard OET letter structure: Opening (purpose + reader), Paragraph 1 (reason for writing + relevant background), "
            "Paragraph 2 (current situation/management), Paragraph 3 (request/action needed), Closing (offer of contact + polite close). "
            "Use professional but clear language. Avoid abbreviations the reader might not understand."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet writing criteria", "writing score", "oet writing grade"],
        "response": (
            "OET Writing is scored on 6 criteria: Purpose (is the purpose clear?), Content (relevant info selected?), "
            "Conciseness & Clarity (no unnecessary info?), Genre & Style (appropriate tone?), Organisation & Layout (logical flow?), "
            "and Language (grammar, spelling, vocabulary?). You need 350/500 (Grade B) minimum for NMC."
        ),
        "category": "oet",
        "link_key": "oet_writing",
        "link_text": "There's a detailed scoring breakdown here: {link}",
    },
    {
        "keywords": ["oet transformed language", "transform", "paraphrase notes"],
        "response": (
            "'Transformed language' is key for a high OET Writing score! Don't copy case notes word-for-word — "
            "transform them into flowing prose. Example: 'Pt c/o chest pain since yesterday' → 'The patient has been experiencing "
            "chest pain since yesterday.' Convert abbreviations to full words, and notes into complete sentences."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet word count", "oet letter length", "how long letter"],
        "response": (
            "There's no strict word count for OET letters, but most successful letters are 180-220 words. "
            "Quality over quantity! A concise, well-organised letter with all relevant information scores higher than "
            "a rambling 300-word letter. Practise writing within the 45-minute time limit."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet letter types", "types of letter", "referral discharge transfer"],
        "response": (
            "OET Writing tasks include: Referral letter (to another healthcare professional), Discharge letter (to GP/community services), "
            "Transfer letter (to another ward/facility), Letter of advice (to patient/family), and Reply to a complaint. "
            "Each type has a slightly different tone and structure — make sure you practise all of them!"
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet writing practice", "improve oet writing", "better oet letter"],
        "response": (
            "To improve OET Writing: 1) Read the task carefully and underline key points. 2) Plan which case notes to include. "
            "3) Write a first draft focusing on content. 4) Review for transformed language and professional tone. "
            "5) Check for grammar, spelling, and clarity. Do at least 2 practice letters per week under timed conditions!"
        ),
        "category": "oet",
        "link_key": "oet_writing",
        "link_text": "You can find sample letters with examiner feedback here: {link}",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # OET - SPEAKING / ROLEPLAY (8 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["oet speaking", "oet roleplay", "role play", "roleplay"],
        "response": (
            "OET Speaking has two roleplays, each about 5 minutes. You'll play a healthcare professional; "
            "the interlocutor plays a patient, carer, or relative. You get 2-3 minutes to prepare each card — "
            "use this time to plan your approach and note key tasks. You need to show empathy, professionalism, AND clinical competence."
        ),
        "category": "oet",
        "link_key": "oet_speaking",
        "link_text": "We built a free OET roleplay scenario generator for practice: {link}",
    },
    {
        "keywords": ["oet speaking card", "roleplay card", "prepare roleplay"],
        "response": (
            "When you get your roleplay card: 1) Note the setting and who you're speaking to. 2) Identify ALL tasks listed — "
            "you must address each one! 3) Think about how to start (greeting + introduction + purpose). "
            "4) Plan phrases for empathy, explanation, and closing. Don't memorise a script — be flexible!"
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet empathy", "show empathy", "empathetic phrases"],
        "response": (
            "Empathy phrases for OET Speaking: 'I can see this is difficult for you.', 'That must be very worrying.', "
            "'I understand your concern about...', 'It's completely normal to feel this way.', "
            "'Let me reassure you that...'. Use the patient's name, maintain a warm tone, and give them space to express feelings."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet clinical communication", "explain condition", "explain to patient"],
        "response": (
            "When explaining in OET Speaking: Use plain language, not medical jargon. Check understanding: "
            "'Does that make sense?' or 'Do you have any questions about that?'. Use analogies for complex concepts. "
            "Chunk information into small parts and check the patient is following along. Offer written information if appropriate."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet speaking criteria", "speaking score oet", "intelligibility"],
        "response": (
            "OET Speaking is scored on: Intelligibility (clear pronunciation, appropriate accent, stress, intonation), "
            "Fluency (smooth speech, natural pace), Appropriateness (professional tone, rapport, empathy), "
            "Resources of Grammar & Expression (accuracy and range), and Relationship-building (patient-centred care). "
            "You need Grade B in all criteria for NMC registration."
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet interlocutor", "examiner oet", "interlocutor strict"],
        "response": (
            "The OET interlocutor is there to facilitate, not trick you! They follow a script and play their role consistently. "
            "They don't score you — your performance is recorded and assessed later by trained assessors. "
            "So don't worry about their facial expressions — just focus on your communication skills!"
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet speaking practice", "practise roleplay", "speaking partner oet"],
        "response": (
            "Practise OET Speaking with a study partner taking turns as patient and nurse/doctor. Use sample roleplay cards — "
            "practise ALL common scenarios: explaining a diagnosis, giving lifestyle advice, breaking bad news, "
            "dealing with an anxious patient, handling a complaint. Record yourself and review for clarity and empathy."
        ),
        "category": "oet",
        "link_key": "oet_speaking",
        "link_text": "There's a free roleplay scenario generator with common situations here: {link}",
    },
    {
        "keywords": ["breaking bad news", "bad news", "difficult conversation"],
        "response": (
            "For breaking bad news in OET: Prepare the patient ('I'm afraid I have some difficult news to share...'), "
            "Deliver it clearly but compassionately, pause to let them process, acknowledge their emotions, "
            "and offer support/next steps. Use phrases like: 'I wish I had better news...', 'I'm here to support you', "
            "'Would you like me to explain what happens next?'. Never rush this interaction."
        ),
        "category": "oet",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # OET - READING & LISTENING (4 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["oet reading", "oet part a", "oet part b", "oet part c"],
        "response": (
            "OET Reading has 3 parts: Part A (expeditious reading — 4 short texts, 20 mins, gap-fill), "
            "Part B (6 short workplace texts, 1 multiple-choice each), Part C (2 long medical articles, 8 MCQs). "
            "Total: 60 minutes. Part A is the most time-pressured — practise skimming and scanning!"
        ),
        "category": "oet",
        "link_key": "oet_reading",
        "link_text": "There's a free OET Reading strategies guide here: {link}",
    },
    {
        "keywords": ["oet listening", "oet part a listening", "oet part b listening"],
        "response": (
            "OET Listening: Part A (consultation extraction — 2 consultations, note completion), "
            "Part B (short workplace extracts — 6 MCQs), Part C (presentation — 2 long extracts, 6 MCQs). "
            "The audio is healthcare-specific, which helps if you know medical terminology. Write answers in the word forms given!"
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet vs ielts", "which test", "oet or ielts", "oet better"],
        "response": (
            "OET is designed for healthcare professionals, so the vocabulary and scenarios are work-relevant. "
            "IELTS is a general academic test. Many nurses find OET Speaking and Writing easier because the scenarios "
            "are familiar. However, OET can be harder to find preparation materials for. Choose based on your strengths!"
        ),
        "category": "oet",
    },
    {
        "keywords": ["oet preparation", "prepare oet", "oet study plan"],
        "response": (
            "For OET preparation: Focus heavily on Writing (most people struggle here). Practise transforming case notes into letters. "
            "For Speaking, do daily roleplay practice. For Reading, practise Part A under timed conditions. "
            "Use official OET preparation materials — they're the most accurate representation of the actual test."
        ),
        "category": "oet",
        "link_key": "oet_writing",
        "link_text": "We have free OET preparation resources here: {link}",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # OSCE / PLAB (10 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["osce", "objective structured clinical", "clinical exam", "practical exam"],
        "response": (
            "The OSCE (Objective Structured Clinical Examination) tests your clinical skills in simulated scenarios. "
            "You'll rotate through stations (usually 6-18), each 5-10 minutes long. Stations include: history taking, "
            "physical examination, practical procedures, communication skills, and emergency scenarios. It's tough but absolutely passable with practice!"
        ),
        "category": "osce",
        "link_key": "osce_generator",
        "link_text": "We built a free OSCE scenario generator for practice — it has hundreds of cases: {link}",
    },
    {
        "keywords": ["osce stations", "station types", "what stations", "osce format"],
        "response": (
            "Common OSCE station types: 1) History Taking (gather information from a patient actor), 2) Physical Examination "
            "(demonstrate a systematic exam), 3) Data Interpretation (ECG, bloods, imaging), 4) Practical Procedures "
            "(cannulation, catheterisation, suturing), 5) Communication (breaking bad news, consent), 6) Emergency/Acute "
            "(ABCDE approach, resuscitation). Know the format of YOUR specific exam (NMC OSCE vs PLAB 2 vs university OSCE)."
        ),
        "category": "osce",
    },
    {
        "keywords": ["nmc osce", "nmc test of competence", "test of competence", "toc"],
        "response": (
            "The NMC Test of Competence (ToC) OSCE for internationally educated nurses has 10 stations across 4 APIEs "
            "(Assessments, Planning, Implementation, Evaluation): APIE stations (4 stations, 17 mins each), Skills stations "
            "(4 stations, 8 mins each), Professional Values stations (2 stations, 8-17 mins each). You need to pass "
            "ALL APIE stations AND meet the overall pass mark. Check the latest NMC blueprints as they updated in 2024!"
        ),
        "category": "osce",
    },
    {
        "keywords": ["osce api", "api station", "assessment planning", "toc api"],
        "response": (
            "The APIE station is the heart of the NMC OSCE: Assessment (gather info: vital signs, history, observations), "
            "Planning (analyse data, identify problems, set goals), Implementation (carry out interventions), "
            "Evaluation (assess outcomes, modify plan). You have 17 minutes. Time management is critical — practise until it becomes second nature."
        ),
        "category": "osce",
    },
    {
        "keywords": ["osce skills", "practical skills", "cannulation", "catheter", "wound dressing"],
        "response": (
            "Common OSCE skills stations include: vital signs, medication administration, wound dressing, urinary catheterisation, "
            "IM/SC injections, peak flow, blood glucose testing, and manual handling. Practise the FULL procedure — "
            "including hand hygiene, introducing yourself, gaining consent, explaining the procedure, and documentation. "
            "Verbalise everything you're doing!"
        ),
        "category": "osce",
    },
    {
        "keywords": ["plab 2", "plab exam", "plab preparation"],
        "response": (
            "PLAB 2 is a clinical skills exam with 16 scenarios, 8 minutes each, plus 2 rest stations. "
            "Scenarios include: history taking, examination, counselling, communication, and acute/emergency management. "
            "The pass rate is around 70-75%. Most people need 2-3 months of dedicated preparation. Book early — slots fill up months in advance!"
        ),
        "category": "osce",
        "link_key": "plab_tips",
        "link_text": "There's a PLAB 2 preparation guide here: {link}",
    },
    {
        "keywords": ["osce practice", "practise osce", "osce partner"],
        "response": (
            "Practise OSCE scenarios daily! Use the 'see one, do one, teach one' method: watch a demonstration, "
            "practise it yourself, then teach it to a study partner. Time yourself strictly — 8 minutes feels very different "
            "from 10 minutes. Practise under pressure by simulating exam conditions with observers."
        ),
        "category": "osce",
        "link_key": "osce_generator",
        "link_text": "This free OSCE scenario generator has hundreds of practice cases: {link}",
    },
    {
        "keywords": ["osce nervous", "osce anxiety", "scared osce"],
        "response": (
            "OSCE anxiety is SO common! The best antidote is preparation — the more you practise, the more confident you'll feel. "
            "Use visualisation: imagine yourself succeeding at each station. On exam day: arrive early, breathe deeply, "
            "and remember that the actors are there to help you succeed. If you make a mistake, recover and move on — "
            "examiners care more about your recovery than perfection!"
        ),
        "category": "osce",
    },
    {
        "keywords": ["history taking", "take history", "patient history"],
        "response": (
            "For history taking stations, use a systematic approach: Introduction (name, role, consent), "
            "Presenting Complaint (open question first, then focused), History of Presenting Complaint (OPQRST — Onset, "
            "Provocation, Quality, Radiation, Severity, Time), Past Medical History, Medications, Allergies, "
            "Social History, Family History, ICE (Ideas, Concerns, Expectations). Summarise and check understanding at the end!"
        ),
        "category": "osce",
    },
    {
        "keywords": ["physical examination", "exam station", "systematic examination"],
        "response": (
            "For examination stations: ALWAYS introduce yourself, explain what you're doing, gain consent, and ensure privacy/dignity. "
            "Be systematic — don't jump around. For cardiovascular: inspection, palpation, percussion, auscultation. "
            "Verbalise positive AND relevant negative findings. Summarise your findings and offer a differential diagnosis."
        ),
        "category": "osce",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # NHS / INTERVIEW (10 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["nhs interview", "nhs job interview", "interview next week", "interview soon"],
        "response": (
            "NHS interviews often use behavioural questions (Tell me about a time when...) and scenario-based questions. "
            "Use the STAR method: Situation, Task, Action, Result. Research the specific NHS Trust — know their values, "
            "CQC rating, and recent initiatives. Prepare examples around: teamwork, conflict resolution, patient safety, "
            "and a time you went above and beyond."
        ),
        "category": "nhs",
        "link_key": "nhs_interview",
        "link_text": "We compiled a bank of real NHS interview questions with model answers: {link}",
    },
    {
        "keywords": ["nhs values", "6 c's", "nhs constitution", "compassion", "caring"],
        "response": (
            "Know the 6 C's by heart: Care, Compassion, Competence, Communication, Courage, Commitment. "
            "Also know the NHS Constitution values: working together for patients, respect and dignity, commitment to quality "
            "of care, compassion, improving lives, and everyone counts. Try to weave these naturally into your answers!"
        ),
        "category": "nhs",
    },
    {
        "keywords": ["tell me about yourself", "why nhs", "why this job", "why nursing"],
        "response": (
            "For 'Tell me about yourself': Keep it professional and relevant. Structure: current role, key experience, "
            "why you're passionate about nursing/this role, and why this specific Trust. For 'Why NHS': Talk about "
            "your commitment to public service, the NHS values, and your desire to work in a system that prioritises "
            "patient care over profit. Be genuine!"
        ),
        "category": "nhs",
    },
    {
        "keywords": ["scenario question", "what would you do", "situational question"],
        "response": (
            "For scenario questions: 1) Take a moment to think — it's okay to pause. 2) Identify the key issues "
            "(patient safety first!). 3) Explain your actions step-by-step with rationale. 4) Mention who you'd escalate to "
            "and when. 5) Reflect on what you'd learn. Common scenarios: colleague conflict, missed medication, "
            "aggressive patient, safeguarding concern, staffing shortage."
        ),
        "category": "nhs",
    },
    {
        "keywords": ["safeguarding", "safeguarding question", "vulnerable adult", "child protection"],
        "response": (
            "For safeguarding questions: ALWAYS prioritise the patient's safety and wellbeing. Mention: raising concerns "
            "immediately with your line manager/safeguarding lead, documenting clearly and factually, following local "
            "policies and procedures, and working multi-agency. Never promise confidentiality in safeguarding situations — "
            "your duty is to protect the vulnerable person."
        ),
        "category": "nhs",
    },
    {
        "keywords": ["nhs band 5", "band 5 nurse", "newly qualified", "preceptorship"],
        "response": (
            "Band 5 is the entry-level registered nurse grade. Interviewers want to see: evidence-based practice, "
            "teamwork, willingness to learn, understanding of professional accountability, and commitment to CPD. "
            "If you're a newly qualified nurse, mention your preceptorship programme and how you'll continue developing your skills."
        ),
        "category": "nhs",
    },
    {
        "keywords": ["nhs band 6", "band 6 nurse", "senior nurse", "charge nurse"],
        "response": (
            "Band 6 roles (charge nurse, team leader, specialist nurse) require leadership examples. Prepare for: "
            "delegation scenarios, managing underperformance, service improvement projects, mentoring junior staff, "
            "and balancing clinical duties with leadership. Show you understand the difference between management and leadership!"
        ),
        "category": "nhs",
    },
    {
        "keywords": ["nhs cv", "nursing cv", "application form", "supporting statement"],
        "response": (
            "For your NHS application/CV: Tailor EVERY application to the specific job description. Use the person "
            "specification as a checklist — address every point. Quantify achievements: 'Managed a caseload of 8 patients', "
            "'Reduced medication errors by 20% through...'. Keep it concise (2 pages max for CV). Proofread meticulously!"
        ),
        "category": "nhs",
        "link_key": "nhs_cv",
        "link_text": "There's an NHS CV template and guide here: {link}",
    },
    {
        "keywords": ["cbt exam", "nmc cbt", "computer based test", "nmc part 1"],
        "response": (
            "The NMC CBT (Computer Based Test) Part 1 tests your theoretical nursing knowledge. It's 120 MCQs "
            "over 4 hours. Topics: professional values (21%), communication and interpersonal skills (16%), "
            "nursing practice and decision-making (39%), leadership management and team working (24%). "
            "You need 68% to pass. Use the NMC Test of Competence blueprints to guide your revision!"
        ),
        "category": "nhs",
    },
    {
        "keywords": ["nhs jobs", "nhs careers", "find nhs job", "apply nhs"],
        "response": (
            "Search for NHS jobs on: NHS Jobs (jobs.nhs.uk), NHS Scotland, Health Board websites, and agency websites. "
            "Set up job alerts so you don't miss postings. When applying, always tailor your supporting statement to "
            "the person specification. After applying, follow up if you haven't heard back within 2 weeks. "
            "Consider reaching out to the ward manager directly — it shows initiative!"
        ),
        "category": "nhs",
        "link_key": "nhs_interview",
        "link_text": "Preparing for interviews? Here's a bank of real NHS interview questions: {link}",
    },

    # ═══════════════════════════════════════════════════════════════════════
    # GENERAL / MOTIVATIONAL (10 responses)
    # ═══════════════════════════════════════════════════════════════════════
    {
        "keywords": ["worried", "nervous", "stressed", "scared", "anxious", "panic"],
        "response": (
            "I can hear how stressed you are, and that's completely valid. These exams and applications are genuinely tough, "
            "and it's okay to feel overwhelmed. Take a deep breath. Break things down into small, manageable steps. "
            "You've already come so far by getting to this point — that takes courage. One step at a time, you've got this!"
        ),
        "category": "general",
    },
    {
        "keywords": ["failed", "didnt pass", "failed again", "give up"],
        "response": (
            "I'm really sorry you're going through this. Failing doesn't define you — it just means you need a different "
            "approach this time. Many successful nurses and doctors failed exams on their first, second, or even third attempt. "
            "Take some time to process, then analyse what went wrong. Adjust your strategy. You're closer than you were before. 💪"
        ),
        "category": "general",
    },
    {
        "keywords": ["study plan", "how to study", "where to start", "dont know how"],
        "response": (
            "Starting can feel overwhelming! Here's a simple framework: 1) Take a practice test to know your baseline. "
            "2) Identify your weakest area (usually the one dragging your overall score down). 3) Create a weekly schedule "
            "with specific goals. 4) Track your progress weekly. 5) Adjust based on results. Consistency beats cramming every time!"
        ),
        "category": "general",
        "link_key": "study_planner",
        "link_text": "There's a free study planner tool here if you want a structured plan: {link}",
    },
    {
        "keywords": ["motivation", "motivated", "cant study", "no motivation", "burnout"],
        "response": (
            "Burnout and lack of motivation are real, especially when preparing for high-stakes exams. Try the Pomodoro "
            "technique: 25 minutes study, 5 minutes break. After 4 cycles, take a longer 30-minute break. "
            "Also remember WHY you're doing this — picture yourself working as a nurse/doctor in the UK. "
            "Take rest days guilt-free; they're part of the plan, not a failure!"
        ),
        "category": "general",
    },
    {
        "keywords": ["help me", "any tips", "any advice", "need help"],
        "response": (
            "Happy to help! To give you the best advice, could you share a bit more about what you're preparing for "
            "(IELTS, OET, OSCE, NHS interview) and what specifically you're struggling with? In the meantime, "
            "my general advice is: practise under timed conditions, focus on your weakest skill, and get feedback regularly. "
            "You're not alone in this journey!"
        ),
        "category": "general",
    },
    {
        "keywords": ["struggling", "finding hard", "too difficult", "impossible"],
        "response": (
            "These exams ARE difficult — that's why passing them is such an achievement. If you're finding something "
            "impossible, break it into smaller pieces. Can't write a full essay? Start with just introductions. "
            "Can't do a full OSCE station? Practise just the opening. Small wins build momentum. "
            "Every expert was once a beginner. Keep going!"
        ),
        "category": "general",
    },
    {
        "keywords": ["english not good", "weak english", "language barrier", "not confident"],
        "response": (
            "Your English doesn't need to be perfect — it needs to be effective. Focus on communicating clearly rather than "
            "using complex vocabulary. Read English daily (even 15 minutes helps), watch English shows with subtitles, "
            "and speak English whenever you can. Your English WILL improve with consistent practice. "
            "Confidence comes from preparation!"
        ),
        "category": "general",
    },
    {
        "keywords": ["study group", "study partner", "find partner", "study together"],
        "response": (
            "Study groups are incredibly valuable! You can: quiz each other, practise speaking together, review each other's "
            "essays, and keep each other motivated. Look for study partners in this server, IELTS/OET Facebook groups, "
            "or apps like Tandem and HelloTalk. Even 2-3 people meeting weekly can make a huge difference!"
        ),
        "category": "general",
    },
    {
        "keywords": ["work in uk", "move to uk", "nursing uk", "nurse uk", "overseas nurse"],
        "response": (
            "The journey to working in the UK as a nurse involves several steps: 1) English test (IELTS/OET), "
            "2) NMC eligibility and application, 3) CBT exam, 4) OSCE (Test of Competence), 5) Job offer from an NHS Trust, "
            "6) Visa application. It takes 6-18 months typically, but thousands of nurses do it every year. You can too!"
        ),
        "category": "general",
    },
    {
        "keywords": ["thank you", "thanks", "appreciate", "helpful"],
        "response": (
            "You're very welcome! 😊 I'm so glad I could help. Feel free to ask anytime — that's what I'm here for. "
            "Good luck with your preparation, and remember: you've got this!"
        ),
        "category": "general",
    },
]

# ═══════════════════════════════════════════════════════════════════════════════
# TIPS DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

IELTS_TIPS = [
    "Read the question TWICE before answering — many mistakes come from misunderstanding what's being asked.",
    "In Listening, answers are usually spelled out if they're names, places, or unusual words. Listen carefully!",
    "For Writing Task 2, always spend 5 minutes planning your essay structure before you start writing.",
    "In Reading, the answers appear in order for most question types — use this to narrow down where to look.",
    "Speaking Part 2: Use all 2 minutes! If you finish early, the examiner may ask follow-up questions that are harder.",
    "Don't memorise essays or speeches — examiners can tell, and you'll lose marks for unnatural responses.",
    "British spelling is preferred: colour, organisation, centre, programme, travelled.",
    "In True/False/Not Given questions, 'False' means the text CONTRADICTS the statement — not just 'not mentioned'.",
    "Task 2 carries double the marks of Task 1 in Writing — never spend more than 20 minutes on Task 1.",
    "For Speaking Part 3, use phrases like 'That's an interesting perspective...' to buy thinking time.",
    "In Listening, check word limits: 'NO MORE THAN TWO WORDS' means three words = wrong answer.",
    "Build your academic vocabulary by topic: health, education, environment, technology, crime, transport.",
    "For Reading matching headings, read the PARAGRAPH first, then look at the headings — not the other way around.",
    "Use a mix of simple, compound, and complex sentences to show grammatical range in Writing and Speaking.",
    "Always transfer Listening answers carefully — spelling mistakes cost marks even if you heard the word correctly!",
    "In Writing Task 1, include an overview paragraph — without it, you can't score above Band 5 for Task Achievement.",
    "Practise with a timer from day one — time pressure is one of the hardest parts of IELTS.",
    "For Speaking, use the 'WHY-HOW-WHEN' technique to extend your answers naturally.",
    "In Reading gap-fill, make sure your answer fits grammatically in the sentence — this is a great self-check.",
    "Stay calm if you miss a Listening answer — focus on the NEXT question, or you'll miss more.",
]

OET_TIPS = [
    "In OET Writing, select only RELEVANT case notes — including irrelevant information loses marks for conciseness.",
    "For OET Speaking roleplays, always introduce yourself with your full name and role at the start.",
    "Transform case note abbreviations into full words in your letter — 'Pt c/o' → 'The patient complains of'.",
    "Use the 2-3 minute preparation time in Speaking to plan your approach and note key phrases.",
    "Empathy phrases score highly: 'I can see this is difficult for you', 'That must be very worrying'.",
    "In OET Reading Part A, practise completing all 20 questions in 15 minutes — timing is tight!",
    "For Speaking, address ALL tasks on the roleplay card — missing even one task affects your score.",
    "Use professional but clear language in Writing — avoid jargon the recipient won't understand.",
    "In Listening Part A, answers must be in the correct word form — singular vs plural matters!",
    "Practise the most common Speaking scenarios: explaining diagnosis, lifestyle advice, breaking bad news, anxiety.",
    "For Writing, check if the letter should be formal, semi-formal, or informal — tone matters!",
    "In Speaking, use the patient's name throughout — it shows person-centred care.",
    "OET Writing: The purpose of the letter should be clear in the first sentence.",
    "For Reading Part C, read the question stem carefully — distractors often use exact words from the passage.",
    "Practise converting vital signs and measurements from case notes into proper sentences.",
    "In Speaking, check understanding frequently: 'Does that make sense?' or 'Do you have any questions?'",
    "For Writing, include your contact details and offer to discuss — it shows professional courtesy.",
    "OET Listening: Medical terminology is often spelled out if it's complex — be ready to write it down.",
    "Roleplay tip: Start with rapport-building before jumping into clinical tasks.",
    "Review NMC OET grade requirements regularly — they can change!",
]

# ═══════════════════════════════════════════════════════════════════════════════
# AI PROMPTS DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

AI_PROMPTS = {
    "ielts": [
        "Generate an IELTS Writing Task 2 essay question about [topic] and provide a band 9 model answer with explanations.",
        "Create 5 IELTS Speaking Part 2 cue cards about [topic] with sample answers and vocabulary notes.",
        "Write a complex IELTS Reading passage about [topic] with 10 questions (TFNG, gap-fill, matching headings).",
        "Generate 20 advanced IELTS vocabulary items about [topic] with definitions, example sentences, and collocations.",
        "Create an IELTS Listening Section 4 script about [topic] with 10 note-completion questions.",
    ],
    "oet": [
        "Create a set of OET Writing case notes for a [condition] patient requiring a referral letter to [specialist].",
        "Generate an OET Speaking roleplay card: a patient with [condition] who is anxious about their diagnosis.",
        "Write an OET Reading Part A passage about [medical topic] with 4 short texts and 20 gap-fill questions.",
        "Generate 15 medical collocations and phrases useful for OET Writing referral letters about [topic].",
        "Create an OET Listening Part A consultation script about [condition] with 12 note-completion questions.",
    ],
    "osce": [
        "Generate a detailed OSCE history-taking scenario: a [age]-year-old with [symptoms] and relevant social history.",
        "Create a full OSCE examination station for [system] examination with a marking scheme and expected findings.",
        "Write an OSCE communication skills scenario: breaking bad news about [diagnosis] to a patient and their family.",
        "Generate an OSCE emergency scenario: a patient presenting with [emergency] requiring ABCDE assessment.",
        "Create an OSCE professional values scenario about [ethical dilemma] with discussion points.",
    ],
    "nhs": [
        "Generate 10 NHS interview questions for a Band [5/6] [speciality] nurse with model answers using the STAR method.",
        "Create a scenario-based NHS interview question about [situation] with a model structured response.",
        "Write an NHS values-based interview answer addressing the 6 C's for the question: '[question]'.",
        "Generate 5 common NHS safeguarding scenarios with appropriate responses and escalation pathways.",
        "Create an NHS interview preparation checklist for overseas nurses including visa and NMC registration topics.",
    ],
    "general": [
        "Create a 4-week study schedule for [exam] preparation covering all sections with daily tasks.",
        "Generate a personalised study plan for someone working [hours] per week preparing for [exam].",
        "Write a motivational study guide addressing common struggles like procrastination and burnout for [exam] students.",
        "Create a vocabulary-building exercise with 20 advanced words, definitions, and practice sentences about [topic].",
        "Generate a practice test review template to analyse mistakes and track progress across study sessions.",
    ],
}


# ═══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def find_response(message_content: str) -> dict | None:
    """
    Find the best matching response for a given message.
    Returns a response dict or None if no match.
    """
    message_lower = message_content.lower()

    matches = []
    for resp in RESPONSES:
        for keyword in resp["keywords"]:
            if keyword.lower() in message_lower:
                matches.append(resp)
                break  # Only add once per response

    if not matches:
        return None

    # Return a random match if multiple (adds variety)
    return random.choice(matches)


def format_response(response: dict) -> str:
    """
    Format a response dict into a message string.
    Includes the tool link if present, formatted naturally.
    """
    text = response["response"]

    if response.get("link_key") and response.get("link_text"):
        link = TOOL_LINKS.get(response["link_key"], "")
        if link:
            link_text = response["link_text"].format(link=link)
            text = f"{text}\n\n{link_text}"

    return text


def get_random_tips(category: str, count: int = 5) -> list[str]:
    """Get random tips for a given category."""
    if category == "ielts":
        tips = IELTS_TIPS
    elif category == "oet":
        tips = OET_TIPS
    else:
        return []

    if len(tips) <= count:
        return tips

    return random.sample(tips, count)


def get_ai_prompt(category: str) -> str | None:
    """Get a random AI prompt for a given category."""
    prompts = AI_PROMPTS.get(category)
    if not prompts:
        return None
    return random.choice(prompts)


def calculate_ielts_band(listening: float, reading: float, writing: float, speaking: float) -> dict:
    """
    Calculate overall IELTS band score from 4 section scores.
    Returns a dict with detailed breakdown.
    """
    average = (listening + reading + writing + speaking) / 4

    # Round to nearest 0.5 or whole number
    decimal = average - int(average)
    if decimal < 0.25:
        overall = int(average)
    elif decimal < 0.75:
        overall = int(average) + 0.5
    else:
        overall = int(average) + 1

    return {
        "listening": listening,
        "reading": reading,
        "writing": writing,
        "speaking": speaking,
        "average": round(average, 2),
        "overall": overall,
    }


def get_resource_message(command: str) -> str:
    """Get a resource message for a specific command."""
    resources = {
        "ielts": (
            "**IELTS Resources**\n\n"
            "Here's what I've got for IELTS preparation:\n"
            "- **Band Score Calculator** — Check your overall band from section scores\n"
            "  {calc}\n"
            "- **Speaking Practice** — Common topics with sample answers\n"
            "  {speak}\n"
            "- **Writing Checklist** — Self-assessment for Task 1 & 2\n"
            "  {write}\n"
            "- **Reading Tips** — Strategies for all question types\n"
            "  {read}\n\n"
            "Use `!calc [L] [R] [W] [S]` to calculate your band score, "
            "or `!tips ielts` for random study tips!"
        ).format(
            calc=TOOL_LINKS["ielts_calculator"],
            speak=TOOL_LINKS["ielts_speaking"],
            write=TOOL_LINKS["ielts_writing"],
            read=TOOL_LINKS["ielts_reading"],
        ),
        "oet": (
            "**OET Resources**\n\n"
            "Here's what I've got for OET preparation:\n"
            "- **Writing Checklist** — Case note selection & letter structure guide\n"
            "  {write}\n"
            "- **Roleplay Generator** — Hundreds of Speaking practice scenarios\n"
            "  {speak}\n"
            "- **Reading Tips** — Strategies for Parts A, B, and C\n"
            "  {read}\n\n"
            "Use `!tips oet` for random OET study tips!"
        ).format(
            write=TOOL_LINKS["oet_writing"],
            speak=TOOL_LINKS["oet_speaking"],
            read=TOOL_LINKS["oet_reading"],
        ),
        "osce": (
            "**OSCE Resources**\n\n"
            "Here's what I've got for OSCE preparation:\n"
            "- **OSCE Scenario Generator** — Hundreds of practice cases\n"
            "  {osce}\n"
            "- **PLAB 2 Tips** — Preparation guide for international doctors\n"
            "  {plab}\n\n"
            "Tip: Practise under timed conditions with a study partner. "
            "The OSCE Scenario Generator has history-taking, examination, communication, and emergency cases!"
        ).format(
            osce=TOOL_LINKS["osce_generator"],
            plab=TOOL_LINKS["plab_tips"],
        ),
        "nhs": (
            "**NHS Interview Resources**\n\n"
            "Here's what I've got for NHS job preparation:\n"
            "- **Interview Question Bank** — Real NHS interview questions with model answers\n"
            "  {interview}\n"
            "- **CV Builder & Templates** — NHS-specific CV guidance\n"
            "  {cv}\n\n"
            "Use the STAR method for behavioural questions: Situation, Task, Action, Result. "
            "Know the 6 C's and NHS Constitution values by heart!"
        ).format(
            interview=TOOL_LINKS["nhs_interview"],
            cv=TOOL_LINKS["nhs_cv"],
        ),
    }

    return resources.get(command, "Resources not found for this topic.")
