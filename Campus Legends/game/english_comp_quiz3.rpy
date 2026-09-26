default english_score3 = 0

default english_questions3 = [
    {
        "q": "Which sentence uses correct apostrophe placement?",
        "a": [
            "The students' books were missing.",
            "The student's' books were missing.",
            "The students's books were missing.",
            "The student’s books were missing."
        ],
        "correct": 0
    },
    {
        "q": "What is the purpose of a body paragraph?",
        "a": [
            "To introduce the thesis",
            "To provide evidence and analysis",
            "To restate the conclusion",
            "To list citations"
        ],
        "correct": 1
    },
    {
        "q": "Which transition word shows cause/effect?",
        "a": [
            "However",
            "Therefore",
            "Meanwhile",
            "Additionally"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is correctly capitalized?",
        "a": [
            "In april, we start exams.",
            "In April, we start exams.",
            "In april, We start exams.",
            "In April, We start Exams."
        ],
        "correct": 1
    },
    {
        "q": "Which is a credible source for academic writing?",
        "a": [
            "A peer-reviewed journal",
            "A meme page",
            "A random YouTube comment",
            "A personal diary"
        ],
        "correct": 0
    },
    {
        "q": "Which sentence uses correct semicolon placement?",
        "a": [
            "I have a big test tomorrow; I can't go out tonight.",
            "I have a big test tomorrow; but I can't go out tonight.",
            "I have a big test; tomorrow I can't go out tonight.",
            "I have; a big test tomorrow I can't go out tonight."
        ],
        "correct": 0
    },
    {
        "q": "What is a credible way to support an argument?",
        "a": [
            "Personal opinions",
            "Peer-reviewed research",
            "Rumors",
            "Unverified claims"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is written in active voice?",
        "a": [
            "The ball was thrown by John.",
            "John threw the ball.",
            "The ball had been thrown.",
            "The ball is being thrown."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses correct comma placement for a list?",
        "a": [
            "I bought apples bananas and oranges.",
            "I bought apples, bananas and oranges.",
            "I bought apples bananas, and oranges.",
            "I bought apples, bananas, and oranges."
        ],
        "correct": 3
    },
    {
        "q": "Which sentence is written formally?",
        "a": [
            "This study is kinda cool.",
            "This study is interesting and provides valuable insight.",
            "This study is lit fr.",
            "This study is weird lol."
        ],
        "correct": 1
    }
]

label english_comp_quiz3:
    "English Composition Quiz — Set 3."
    call run_quiz(english_questions3, english_score3)
    return
