default english_score2 = 0

default english_questions2 = [
    {
        "q": "Which sentence is a fragment?",
        "a": [
            "I walked home.",
            "Because I was tired.",
            "I walked because I was tired.",
            "I was tired after class."
        ],
        "correct": 1
    },
    {
        "q": "What is the purpose of a conclusion paragraph?",
        "a": [
            "Introduce new evidence",
            "Restate the thesis and wrap up ideas",
            "Provide citations",
            "Add random thoughts"
        ],
        "correct": 1
    },
    {
        "q": "Which transition word shows addition?",
        "a": [
            "However",
            "Therefore",
            "Furthermore",
            "Meanwhile"
        ],
        "correct": 2
    },
    {
        "q": "Which sentence uses correct comma placement?",
        "a": [
            "Before class I ate breakfast.",
            "Before class, I ate breakfast.",
            "Before, class I ate breakfast.",
            "Before class I, ate breakfast."
        ],
        "correct": 1
    },
    {
        "q": "What is a hook in an essay?",
        "a": [
            "A citation",
            "A sentence that grabs the reader’s attention",
            "A transition",
            "A concluding statement"
        ],
        "correct": 1
    },
    {
        "q": "Which is an example of a credible academic source?",
        "a": [
            "Wikipedia",
            "A peer-reviewed journal",
            "A random blog",
            "A TikTok video"
        ],
        "correct": 1
    },
    {
        "q": "Which sentence is punctuated correctly?",
        "a": [
            "He studied all night however he still felt nervous.",
            "He studied all night; however, he still felt nervous.",
            "He studied all night however; he still felt nervous.",
            "He studied all night, however he still felt nervous."
        ],
        "correct": 1
    },
    {
        "q": "What is paraphrasing?",
        "a": [
            "Copying text word-for-word",
            "Summarizing without changing meaning",
            "Putting someone else's ideas into your own words",
            "Writing a conclusion"
        ],
        "correct": 2
    },
    {
        "q": "Which sentence has correct subject-verb agreement?",
        "a": [
            "The list of items are long.",
            "The list of items is long.",
            "The items in the list is long.",
            "The items in the list was long."
        ],
        "correct": 1
    },
    {
        "q": "Which sentence uses parallel structure?",
        "a": [
            "She likes running, to swim, and biking.",
            "She likes to run, swim, and bike.",
            "She likes running, swimming, and to bike.",
            "She likes to run, swimming, and biking."
        ],
        "correct": 1
    }
]

label english_comp_quiz2:
    "English Composition Quiz — Set 2."
    call run_quiz(english_questions2, english_score2)
    return
