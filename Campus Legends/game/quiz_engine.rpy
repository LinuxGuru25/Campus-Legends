label run_quiz(questions, score_var):

    $ score_var = 0
    $ index = 0

    while index < len(questions):

        $ q = questions[index]
        $ quiz_question = q["q"]
        $ quiz_answer_a = q["a"][0]
        $ quiz_answer_b = q["a"][1]
        $ quiz_answer_c = q["a"][2]
        $ quiz_answer_d = q["a"][3]

        "[quiz_question]"

        $ choice = renpy.display_menu([
            ("A: " + quiz_answer_a, 0),
            ("B: " + quiz_answer_b, 1),
            ("C: " + quiz_answer_c, 2),
            ("D: " + quiz_answer_d, 3)
        ])

        if choice == q["correct"]:
            "Correct!"
            $ score_var += 1
        else:
            "Wrong!"

        $ index += 1

    "You're done!"
    "Your final score is [score_var] out of [len(questions)]."

    return
