default english_score5 = 0

default english_questions5 = [
    {
        "q": "Which sentence uses correct verb tense consistency?",
        "a": [
            "She walks to class and ate breakfast.",
            "She walked to class and eats breakfast.",
            "She walks to class and eats breakfast.",
            "She walking to class and eats breakfast."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct comma placement for an introductory phrase?",
        "a": [
            "After the exam we went home.",
            "After the exam, we went home.",
            "After, the exam we went home.",
            "After the exam we, went home."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct quotation punctuation?",
        "a": [
            "He said 'Let's go'.",
            "He said, 'Let's go.'",
            "He said 'Let's go.'",
            "He said, 'Let's go'."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is written in active voice?",
        "a": [
            "The essay was written by Maria.",
            "Maria wrote the essay.",
            "The essay is being written.",
            "The essay had been written."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct parallel structure?",
        "a": [
            "He likes to jog, swimming, and biking.",
            "He likes jogging, swimming, and biking.",
            "He likes jogging, to swim, and biking.",
            "He likes to jog, swimming, and to bike."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct apostrophe placement?",
        "a": [
            "The teacher's desk was messy.",
            "The teachers desk was messy.",
            "The teachers' desk was messy.",
            "The teacher's' desk was messy."
        ],
        "correct": 0
    },
    {
        "q": "Which sentence uses correct semicolon placement?",
        "a": [
            "I was tired; I went to bed early.",
            "I was tired; but I went to bed early.",
            "I was tired but; I went to bed early.",
            "I was tired; therefore I went to bed early."
        ],
        "correct": 0
    },
    {
        "q": "Which sentence uses correct colon placement?",
        "a": [
            "She bought: apples, bananas, and grapes.",
            "She bought apples: bananas, and grapes.",
            "She bought three things: apples, bananas, and grapes.",
            "She: bought apples, bananas, and grapes."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence is formal?",
        "a": [
            "This study is kinda wild.",
            "This study is lowkey confusing.",
            "This study provides strong evidence.",
            "This study is weird fr."
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct comma placement?",
        "a": [
            "Before class I grabbed coffee.",
            "Before class, I grabbed coffee.",
            "Before, class I grabbed coffee.",
            "Before class I, grabbed coffee."
        ],
        "correct": 1
    }
]

label english_comp_quiz5:
    "English Composition Quiz — Set 5."
    call run_quiz(english_questions5, english_score5)
    return
