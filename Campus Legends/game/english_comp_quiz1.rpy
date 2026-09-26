# ============================================================
# ENGLISH COMPOSITION QUIZ — Campus Legends
# Ten-question multiple-choice test (Set 1)
# ============================================================

default english_score1 = 0

default english_questions1 = [
    {
        "q": "What is a thesis statement?",
        "a": [
            "A question that guides the essay",
            "A sentence that states the main argument",
            "A summary of the conclusion",
            "A quote from a source"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is grammatically correct?",
        "a": [
            "Its going to be a long day.",
            "It's going to be a long day.",
            "Its' going to be a long day.",
            "It going's to be a long day."
        ],
        "correct": 1
    },
    {
        "q": "What is the purpose of a topic sentence?",
        "a": [
            "To introduce the paragraph’s main idea",
            "To summarize the entire essay",
            "To cite a source",
            "To transition to the conclusion"
        ],
        "correct": 0
    },
    {
        "q": "Which of the following is an example of academic writing?",
        "a": [
            "A text message",
            "A research paper",
            "A social media post",
            "A diary entry"
        ],
        "correct": 1
    },
    {
        "q": "What does MLA stand for?",
        "a": [
            "Modern Language Association",
            "Major Literary Analysis",
            "Multiple Learning Areas",
            "Modern Literature Academy"
        ],
        "correct": 0
    },
    {
        "q": "Which is a run-on sentence?",
        "a": [
            "I went to class, and I took notes.",
            "I went to class I took notes.",
            "I went to class. I took notes.",
            "After class, I took notes."
        ],
        "correct": 1
    },
    {
        "q": "What is plagiarism?",
        "a": [
            "Using your own ideas",
            "Citing sources correctly",
            "Using someone else's work without credit",
            "Writing a rough draft"
        ],
        "correct": 2
    },
    {
        "q": "Which transition word shows contrast?",
        "a": [
            "Furthermore",
            "However",
            "Additionally",
            "For example"
        ],
        "correct": 1
    },
    {
        "q": "What belongs in the introduction paragraph?",
        "a": [
            "Only the conclusion",
            "Only citations",
            "Background information and thesis",
            "Only topic sentences"
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct punctuation?",
        "a": [
            "She loves writing however she hates editing.",
            "She loves writing; however, she hates editing.",
            "She loves writing however; she hates editing.",
            "She loves writing, however she hates editing."
        ],
        "correct": 1
    }
]

label english_comp_quiz1:

    $ english_score1 = 0

    "English Composition Quiz — Set 1."

    $ index = 0

    while index < len(english_questions1):

        $ q = english_questions1[index]

        "[q['q']]"

        menu:
            "A: [q['a'][0]]":
                $ choice = 0
            "B: [q['a'][1]]":
                $ choice = 1
            "C: [q['a'][2]]":
                $ choice = 2
            "D: [q['a'][3]]":
                $ choice = 3

        if choice == q["correct"]:
            "Correct!"
            $ english_score1 += 1
        else:
            "Wrong!"

        $ index += 1

    "You're done!"

    "Your final score is [english_score1] out of 10."

    if english_score1 >= 8:
        "Strong writing skills — nice."
    elif english_score1 >= 5:
        "Solid effort."
    else:
        "Might need to brush up on your writing."

    return


