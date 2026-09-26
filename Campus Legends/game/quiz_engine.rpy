label run_quiz(questions, score_var):

    $ score_var = 0
    $ index = 0

    while index < len(questions):

        $ q = questions[index]

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
            $ score_var += 1
        else:
            "Wrong!"

        $ index += 1

    "You're done!"
    "Your final score is [score_var] out of [len(questions)]."

    return
