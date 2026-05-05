


##############################################
## MC SUPPORT & HEALING SCENES
## Panic Attack • Shutdown • Reflection • Support
##############################################

label mc_panic_attack_scene(source):
    # This scene is triggered automatically when:
    # anxiety >= 75 AND emotional_load >= 60

    scene black with fade
    pause 0.5

    "The world feels like it’s collapsing inward."

    "My chest tightens. Breathing turns sharp and uneven."
    "Everything feels too loud. Too close. Too fast."

    if source:
        "{source} notices immediately."

        "{source} \"Hey—hey, look at me. You’re okay. I’m right here.\""

        "Their voice cuts through the noise, steady and warm."

        "{source} \"Can you match my breathing? In… and out… nice and slow.\""

        "I try. It’s messy. But they stay with me through every shaky breath."

        "{source} \"You’re not alone. I’ve got you.\""

    else:
        "I try to ground myself, but the panic keeps rising."

        "I focus on the floor. The texture. The temperature."
        "Anything to pull myself back."

    "Slowly… painfully… the world stops spinning."

    # Healing from support (if someone was present)
    if source:
        $ mc_receive_support(source, strength=2, kind="grounding")

    return


##############################################
## MC SHUTDOWN SCENE
##############################################

label mc_shutdown_scene(source):
    # Triggered when emotional_load >= 80

    scene black with dissolve
    pause 0.5

    "Everything goes quiet."

    "Not peaceful quiet. The kind where my brain just… stops."
    "Thoughts freeze. Words disappear. I can’t move. I can’t react."

    if source:
        "{source} \"Hey… you’re zoning out. Talk to me?\""

        "I want to. I really do. But nothing comes out."

        "{source} \"Okay. That’s alright. You don’t have to talk.\""
        "{source} \"I’m just gonna sit with you, okay? You’re safe.\""

        "They stay close. Not pushing. Not demanding. Just… present."

        "{source} \"Whenever you’re ready, I’m here.\""

        # Healing
        $ mc_receive_support(source, strength=2, kind="comfort")

    else:
        "I sit alone in the silence, waiting for my mind to thaw."

    return


##############################################
## MC DEPRESSION REFLECTION SCENE
##############################################

label mc_depression_reflection_scene(source):
    # Triggered when depression >= 70

    scene black with fade
    pause 0.5

    "I feel heavy."

    "Not tired. Not sad. Just… heavy."
    "Like every thought has weight. Like moving takes effort."

    "I don’t know how long I’ve been sitting here."

    if source:
        "{source} quietly sits beside me."

        "{source} \"Rough day?\""

        "I nod. It’s all I can manage."

        "{source} \"You don’t have to explain. I’m here.\""

        "They don’t try to fix me. They don’t tell me to cheer up."
        "They just stay. And somehow… that helps."

        # Healing
        $ mc_receive_support(source, strength=2, kind="reassurance")

    else:
        "I try to remind myself that this feeling isn’t permanent."
        "It’s hard. But I’m trying."

    return


##############################################
## GENERAL SUPPORT SCENE (PARTNER OR FRIEND)
##############################################

label mc_support_scene(name):
    # Called when someone notices the MC is struggling

    scene black with dissolve
    pause 0.5

    "{name} notices something’s off."

    "{name} \"You’ve been quiet. Want to sit with me for a bit?\""

    "I hesitate, but they gently guide me to a calmer space."

    "{name} \"You don’t have to talk if you don’t want to.\""
    "{name} \"Just breathe with me. One step at a time.\""

    "Their presence is steady. Warm. Safe."

    # Healing
    $ mc_receive_support(name, strength=1, kind="general")

    return


##############################################
## FRIEND SUPPORT AFTER BREAKUP
##############################################

label mc_friend_support_after_breakup(name):
    # Called automatically after a breakup event

    scene black with fade
    pause 0.5

    "{name} finds me alone."

    "{name} \"Hey… I heard what happened.\""

    "I don’t say anything. I’m not sure I can."

    "{name} sits beside me, not forcing conversation."

    "{name} \"Breakups hurt. Even when you see them coming.\""
    "{name} \"But you’re not going through this alone, okay?\""

    "Their voice is soft. No judgment. No pressure."

    "{name} \"Let’s take it one day at a time. I’ve got your back.\""

    # Healing
    $ mc_receive_support(name, strength=2, kind="comfort")

    return
