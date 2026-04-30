
# ================================================================
# ROMANCE STATE DICTIONARY
# ================================================================
default romance = {
    "Sienna": "neutral",
    "Jess": "neutral",
    "Aubrey": "neutral",
    "Norah": "neutral",
    "Tiffany": "neutral",
    "Kaia": "neutral"
}

# ================================================================
# DYNAMIC ROMANCE THRESHOLDS
# ================================================================
default romance_thresholds = {
    "Sienna": 30,
    "Jess": 45,
    "Aubrey": 50,
    "Norah": 30,
    "Tiffany": 30,
    "Kaia": 30
}

# ================================================================
# ROMANCE UNLOCK FLAGS
# ================================================================
default sienna_romance_unlocked = False
default jess_romance_unlocked = False
default aubrey_romance_unlocked = False
default norah_romance_unlocked = False
default tiffany_romance_unlocked = False
default kaia_romance_unlocked = False

default girlfriend_evolution = {
    "Sienna": {
        30: {"Confident": 1, "Sienna": 1},   # Girlfriend
        45: {"Confident": 2, "Sienna": 1},   # Strong bond
        60: {"Confident": 2, "Sienna": 2}   # Deep romance
    },
    "Jess": {
        45: {"Caring": 1, "Jess": 1},
        55: {"Caring": 2, "Jess": 1},
        75: {"Caring": 2, "Jess": 2}
    },
    "Aubrey": {
        50: {"Selfish": 1, "Aubrey": 1},
        65: {"Selfish": 2, "Aubrey": 1},
        85: {"Selfish": 2, "Aubrey": 2}
    },
    "Norah": {
        30: {"Caring": 1, "Confident": 1},
        50: {"Caring": 2, "Confident": 1},
        65: {"Caring": 2, "Confident": 2}
    },
    "Tiffany": {
        30: {"Confident": 2},
        45: {"Confident": 3},
        65: {"Confident": 4}
    },
    "Kaia": {
        30: {"Confident": 1, "Selfish": 1},
        45: {"Confident": 2, "Selfish": 1},
        65: {"Confident": 2, "Selfish": 2}
    }
}


# ================================================================
# ROMANCE MANAGER FUNCTIONS
# ================================================================
init python:

    # Check if a character's romance route is available
    def can_romance(name):
        return rel[name] >= romance_thresholds[name] and romance[name] != "closed"

    # Lock in a romance route
    def lock_in(name):
        romance[name] = "locked"

    def close_route(name):
        romance[name] = "closed"
        girlfriend[name] = False


    # Re-open a route (if your story allows it)
    def open_route(name):
        romance[name] = "open"

    # Automatically update romance state based on points
    def auto_check_romance(name):
        if can_romance(name):
            romance[name] = "open"
        else:
            romance[name] = "neutral"

    # Lock one romance and close all others (exclusive routes)
    def lock_exclusive(name):
        for char in romance:
            if char == name:
                romance[char] = "locked"
            else:
                romance[char] = "closed"

    # Dynamic romance unlock check
    def check_romance_unlock(name):
        points = rel.get(name, 0)
        threshold = romance_thresholds.get(name, 3)

        unlocked = points >= threshold

        renpy.store.__dict__[f"{name.lower()}_romance_unlocked"] = unlocked

        return unlocked

    def apply_girlfriend_bonus_tier(girl, trait_or_rel):
        if not girlfriend.get(girl, False):
            return

        tier = get_girlfriend_tier(girl)
        tier_bonuses = girlfriend_evolution[girl][tier]

        if trait_or_rel not in tier_bonuses:
            return

        bonus = tier_bonuses[trait_or_rel]
        change_points(trait_or_rel, bonus)


# ============================================================
# PREFERRED PERSONALITY SYSTEM + AUTO-FLIP PERSONALITY
# ============================================================

# Each character’s preferred MC personality type
default preferred_personality = {
    # Love Interests
    "Sienna": "Confident",
    "Jess": "Caring",
    "Aubrey": "Confident",
    "Norah": "Caring",
    "Tiffany": "Selfish",
    "Kaia": "Confident",

    # Non-Love Interests
    "Coach": "Confident",
    "Roommate": "Confident",
    "Professor": "Caring",
    "Rival": "Selfish",
    "Nick": "Confident"
}

init python:

    # Automatically updates MC's dominant personality
    def update_mc_personality():
        global mc_personality
        highest = max(personality, key=personality.get)
        mc_personality = highest
        return mc_personality

    # Adds personality points AND auto-updates MC personality
    def add_personality_and_update(trait, amount=1):
        personality[trait] += amount
        update_mc_personality()

    # Awards bonus relationship points if MC uses a trait the character prefers
    def personality_bonus(char, trait):
        if preferred_personality.get(char) == trait:
            rel[char] += 1   # bonus amount

default girlfriend = {
    "Sienna": False,
    "Jess": False,
    "Aubrey": False,
    "Norah": False,
    "Tiffany": False,
    "Kaia": False
}

default girlfriend_bonuses = {
    "Sienna": {
        "Confident": 1,     # MC gets +1 Confident on confident choices
        "Sienna": 1         # MC gets +1 extra Sienna relationship point
    },
    "Jess": {
        "Caring": 1,        # MC gets +1 Caring on caring choices
        "Jess": 1           # MC gets +1 extra Jess relationship point
    },
    "Aubrey": {
        "Selfish": 1,       # MC gets +1 Selfish on selfish choices
        "Aubrey": 1         # MC gets +1 extra Aubrey relationship point
    },
    "Norah": {
        "Caring": 1,
        "Confident": 1      # Norah gives dual‑trait boosts
    },
    "Tiffany": {
        "Confident": 2      # Tiffany gives a BIG confidence boost
    },
    "Kaia": {
        "Confident": 1,
        "Selfish": 1        # Kaia rewards bold or reckless behavior
    }
}


# ============================================================
# BREAKUP SYSTEM (Unified + Integrated)
# ============================================================

# Tracks if the MC has broken up with someone
default breakup = {
    "Sienna": False,
    "Jess": False,
    "Aubrey": False,
    "Misty": False,
    "Kaia": False,
    "Tiffany": False,
    "Norah": False,
    
}

# Breakup penalty severity per character
default breakup_penalty = {
    "Sienna": 0,
    "Jess": 0,
    "Aubrey": 0,
    "Norah": 0,
    "Kaia": 0,
    "Tiffany": 0
}

# Romance lockout after breakup
default romance_locked = {
    "Sienna": False,
    "Jess": False,
    "Aubrey": False,
    "Kaia": False,
    "Tiffany": False,
    "Norah": False,
}

# ============================================================
# MAIN BREAKUP FUNCTION
# ============================================================

init python:

    def trigger_breakup(name, severity=1):
        """
        The full breakup engine:
        - Sets breakup flags
        - Applies penalties
        - Adjusts reputation
        - Applies personality-based effects
        - Removes perks
        - Locks romance
        - Triggers world reactions, social media, jealousy
        """

        # Mark breakup
        breakup[name] = True

        # Apply penalty
        breakup_penalty[name] += severity

        # Lock romance route
        romance_locked[name] = True

        # Reputation hits
        rep_with[name] -= 10 * severity
        reputation["loyalty"] -= 5 * severity
        reputation["chaos"] += 8 * severity
        reputation["romantic"] -= 3 * severity

        # Personality-based breakup effects
        if mc_personality == "Confident":
            reputation["social"] -= 2
            reputation["chaos"] += 3

        elif mc_personality == "Caring":
            reputation["loyalty"] -= 8
            rep_with[name] -= 5

        elif mc_personality == "Selfish":
            reputation["chaos"] += 10
            reputation["romantic"] -= 5

        # Remove girlfriend perks
        if name in girlfriend_perks:
            del girlfriend_perks[name]

        # Trigger world reactions
        renpy.call_in_new_context("world_reacts_to_breakup", name)

        # Trigger social media tone shift
        renpy.call_in_new_context("social_media_breakup_shift", name)

        # Trigger jealousy hooks
        renpy.call_in_new_context("jealousy_after_breakup", name)


# ---------------------------------------------------------
# OPTIONAL: Debug Screen Additions
# ---------------------------------------------------------
screen romance_debug():

    frame:
        xalign 0.5
        yalign 0.5
        padding 20

        vbox:
            text "Romance Debug Panel" size 40

            for char in relationship_points:
                text f"{char}: {relationship_points[char]} pts | Locked: {romance_locked[char]} | Broke Up: {breakup_history[char]}"

            textbutton "Recover All (Forgiveness)" action [
                Function(lambda: [breakup_recovery(c) for c in breakup_history])
            ]

# Tracks forgiveness progress per character
default forgiveness_points = {
    "Sienna":  0,
    "Jess":  0,
    "Aubrey": 0,
    "Misty": 0,
    "Kaia": 0,
    "Tiffany": 0,
    "Norah": 0,
}

# How many points needed to forgive
default forgiveness_threshold = {
    "Sienna": 10,
    "Jess": 12,
    "Aubrey": 15,
    "Misty": 8,
    "Kaia": 10,
    "Tiffany": 10,
    "Norah": 10,
}

# Optional: personality-based forgiveness modifiers
default forgiveness_personality_mod = {
    "Confident": 1,
    "Caring": 2,
    "Selfish": -1,
}

init python:
    def add_forgiveness(name, amount=1):
        # Personality bonus/penalty
        bonus = forgiveness_personality_mod.get(mc_personality, 0)
        forgiveness_points[name] += amount + bonus

        # Clamp to threshold
        if forgiveness_points[name] > forgiveness_threshold[name]:
            forgiveness_points[name] = forgiveness_threshold[name]

init python:
    def is_forgiven(name):
        return forgiveness_points[name] >= forgiveness_threshold[name]

init python:
    def try_reconcile(name):
        if is_forgiven(name):
            romance_locked[name] = False
            breakup[name] = False
            return True
        return False

# ============================================================
# CHEATING SYSTEM (Unified + Standalone)
# ============================================================

# ------------------------------------------------------------
# CHEATING FLAGS & SEVERITY
# ------------------------------------------------------------

default cheated_on = {
    "Sienna": False, "Jess": False, "Aubrey": False,
    "Misty": False, "Kaia": False, "Tiffany": False, "Norah": False,
}

default cheating_severity = {
    "Sienna": 0, "Jess": 0, "Aubrey": 0,
    "Misty": 0, "Kaia": 0, "Tiffany": 0, "Norah": 0,
}

# ------------------------------------------------------------
# CHEATING ENGINE
# ------------------------------------------------------------

init python:
    def trigger_cheating(name, severity=1):
        """
        Handles cheating consequences:
        - Marks cheating
        - Applies severity
        - Adjusts reputation
        - Applies personality effects
        - Locks romance
        - Triggers reactions (rumors, jealousy, confrontation)
        """

        # Mark cheating
        cheated_on[name] = True
        cheating_severity[name] += severity

        # Reputation consequences
        reputation["loyalty"] -= 10 * severity
        reputation["chaos"] += 5 * severity
        reputation["romantic"] -= 3 * severity

        # Personality influence
        if mc_personality == "Confident":
            reputation["social"] -= 2

        elif mc_personality == "Caring":
            reputation["loyalty"] -= 5

        elif mc_personality == "Selfish":
            reputation["chaos"] += 5

        # Lock romance route
        romance_locked[name] = True

        # Trigger reactions
        renpy.call_in_new_context("cheating_reaction", name)
        renpy.call_in_new_context("cheating_rumors", name)
        renpy.call_in_new_context("cheating_jealousy", name)

# ------------------------------------------------------------
# CHEATING REACTION LABELS
# ------------------------------------------------------------

label cheating_reaction(name):

    if reputation["loyalty"] <= -15:
        "[name] looks devastated when she hears what happened."

    elif reputation["chaos"] >= 20:
        "[name] confronts you in front of other students."

    else:
        "[name] quietly pulls away from you."

    return

label cheating_rumors(name):

    if reputation["chaos"] >= 15:
        "You hear whispers around campus about what happened."

    if reputation["loyalty"] <= -10:
        "Someone posts a vague message online about betrayal."

    return

label cheating_jealousy(name):

    if mc_personality == 'Confident':
        "[name] watches you from across the room, hurt but angry."

    if mc_personality == 'Caring':
        "[name] avoids you, clearly upset."

    if mc_personality == 'Selfish':
        "People assume you don't care about the fallout."

    return








            