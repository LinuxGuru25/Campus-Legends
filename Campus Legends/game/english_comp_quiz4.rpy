default english_score4 = 0

default english_questions4 = [
    {
        "q": "Which sentence uses correct pronoun agreement?",
        "a": [
            "Everyone must bring their pencil.",
            "Everyone must bring his or her pencil.",
            "Everyone must bring they pencil.",
            "Everyone must bring them pencil."
        ],
        "correct": 1
    },
    {
        "q": "What is a credible way to avoid plagiarism?",
        "a": [
            "Copying text but changing a few words",
            "Citing all sources properly",
            "Using someone else's ideas without credit",
            "Not citing anything"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct colon placement?",
        "a": [
            "He brought: chips, soda, and candy.",
            "He brought chips: soda, and candy.",
            "He brought three things: chips, soda, and candy.",
            "He: brought chips, soda, and candy."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence is written in passive voice?",
        "a": [
            "The teacher graded the papers.",
            "The papers were graded by the teacher.",
            "The teacher is grading the papers.",
            "The teacher will grade the papers."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct hyphenation?",
        "a": [
            "A well written essay",
            "A well-written essay",
            "A well written-essay",
            "A well- written essay"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct quotation formatting?",
        "a": [
            "She said, 'I’m tired'.",
            "She said 'I’m tired.'",
            "She said, 'I’m tired.'",
            "She said 'I’m tired'."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct parallel structure?",
        "a": [
            "He likes running, to swim, and biking.",
            "He likes to run, swim, and bike.",
            "He likes running, swimming, and to bike.",
            "He likes to run, swimming, and biking."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct comma placement?",
        "a": [
            "After dinner we watched a movie.",
            "After dinner, we watched a movie.",
            "After, dinner we watched a movie.",
            "After dinner we, watched a movie."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is formal?",
        "a": [
            "This article is kinda weird.",
            "This article is lowkey confusing.",
            "This article provides a detailed analysis.",
            "This article is wild fr."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct semicolon placement?",
        "a": [
            "I studied; but I still felt nervous.",
            "I studied; however, I still felt nervous.",
            "I studied however; I still felt nervous.",
            "I studied, however; I still felt nervous."
        ],
        "correct": 1
    }
]

label english_comp_quiz4:
    "English Composition Quiz — Set 4."
    call run_quiz(english_questions4, english_score4)
    return
