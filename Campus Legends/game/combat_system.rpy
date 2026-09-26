# =========================================================
# CAMPUS LEGENDS — PARTY + ENEMY TYPES + CONDITIONAL ALLY
# =========================================================

# ---------- GLOBAL DEFAULTS ----------

default personality = {
    "Confident": 0,
    "Caring": 0,
    "Selfish": 0
}

default player_stats = {
    "Strength": 10,
    "Dexterity": 10,
    "Constitution": 10,
    "Charisma": 10
}

default stat_points = 0
default player_class = "Warrior"
default player_level = 1
default player_xp = 0
default xp_to_next_level = 50
default stat_points_per_level = 3

default base_ap_per_turn = 6
default min_ap_per_turn = 3
default max_ap_per_turn = 8
default fatigue_start_turn = 4

default combat_log = "The fight begins."
default combat_choice = None

default warrior_path = None
default rogue_path = None
default sorcerer_path = None

# Ally roster (multiple allies, unlocked via story)
default ally_roster = []
default active_ally = None

# Enemy party
default enemy_party = []


# ---------- CLASS SELECTION (EXAMPLE) ----------

label choose_class:

    "You think about what kind of fighter you want to be."

    menu:
        "Warrior":
            $ player_class = "Warrior"
        "Rogue":
            $ player_class = "Rogue"
        "Sorcerer":
            $ player_class = "Sorcerer"

    "You chose [player_class]."

    return


# ---------- PATH SELECTION (LEVEL 4) ----------

label choose_class_path:

    if player_class == "Warrior" and warrior_path is None and player_level >= 4:
        "Your Warrior training reaches a crossroads."
        menu:
            "Berserker (offense)":
                $ warrior_path = "Berserker"
            "Sentinel (defense)":
                $ warrior_path = "Sentinel"

    if player_class == "Rogue" and rogue_path is None and player_level >= 4:
        "Your Rogue style begins to define you."
        menu:
            "Assassin (burst)":
                $ rogue_path = "Assassin"
            "Trickster (control)":
                $ rogue_path = "Trickster"

    if player_class == "Sorcerer" and sorcerer_path is None and player_level >= 4:
        "Your Sorcerer magic takes shape."
        menu:
            "Enchanter (control)":
                $ sorcerer_path = "Enchanter"
            "WarMage (destruction)":
                $ sorcerer_path = "WarMage"

    return


# =========================================================
# PYTHON CORE — FIGHTERS, ALLIES, ENEMIES, AP, AI
# =========================================================

init python:

    import random

    # ---------- BASE FIGHTER ----------

    class Fighter(object):
        def __init__(self, name, hp, strength, dexterity, constitution, charisma, portrait=None):
            self.name = name
            self.base_hp = hp
            self.constitution = constitution
            self.max_hp = hp + constitution * 2
            self.hp = self.max_hp

            self.strength = strength
            self.dexterity = dexterity
            self.charisma = charisma

            self.portrait = portrait

            self.temp_defense = 0
            self.cooldowns = {}
            self.status = []
            self.alive = True

        def is_alive(self):
            return self.hp > 0


    # ---------- ALLY CLASS ----------

    class Ally(Fighter):
        def __init__(self, name, class_type, branch, personality, stats, abilities, passives, portrait=None):
            super(Ally, self).__init__(
                name,
                hp=stats.get("hp", 20),
                strength=stats.get("Strength", 8),
                dexterity=stats.get("Dexterity", 8),
                constitution=stats.get("Constitution", 8),
                charisma=stats.get("Charisma", 8),
                portrait=portrait
            )
            self.class_type = class_type      # "Warrior", "Rogue", "Sorcerer", "Support", etc.
            self.branch = branch              # "Berserker", "Sentinel", etc.
            self.personality = personality    # dict like player personality
            self.abilities = abilities        # list of ability keys
            self.passives = passives          # list of passive keys
            self.ap = 0


    # ---------- ENEMY CLASS ----------

    class Enemy(Fighter):
        def __init__(self, name, enemy_class, personality, stats, abilities, passives, portrait=None):
            super(Enemy, self).__init__(
                name,
                hp=stats.get("hp", 20),
                strength=stats.get("Strength", 6),
                dexterity=stats.get("Dexterity", 6),
                constitution=stats.get("Constitution", 6),
                charisma=stats.get("Charisma", 6),
                portrait=portrait
            )
            self.enemy_class = enemy_class    # "Bruiser", "Skirmisher", "Caster", "Tank", "Assassin", "Support"
            self.personality = personality    # "Aggressive", "Defensive", "Chaotic", "Calculated"
            self.abilities = abilities        # list of ability keys
            self.passives = passives          # list of passive keys
            self.ap = 0


    # ---------- UTILS ----------

    def roll(dice):
        num, sides = dice.lower().split("d")
        return sum(random.randint(1, int(sides)) for _ in range(int(num)))


    def personality_bonus_for_player():
        bonus = {"hit": 0, "crit": 0, "defense": 0, "damage": 0, "speed": 0}

        if personality.get("Confident", 0) >= 3:
            bonus["hit"] += 2
            bonus["crit"] += 3

        if personality.get("Caring", 0) >= 3:
            bonus["defense"] += 2

        if personality.get("Selfish", 0) >= 3:
            bonus["damage"] += 2
            bonus["speed"] += 1

        return bonus


    def get_hit_chance(attacker, defender, attacker_personality=None):
        base = 60 + attacker.dexterity * 3 - defender.dexterity * 2

        if attacker_personality:
            if attacker_personality.get("Confident", 0) >= 3:
                base += 2

        pb = personality_bonus_for_player()
        if attacker.name == "MC":
            base += pb["hit"]

        return max(20, min(95, base))


    def get_crit_chance(attacker, attacker_personality=None):
        base = 5 + attacker.dexterity * 2 + attacker.charisma

        if attacker_personality:
            if attacker_personality.get("Confident", 0) >= 3:
                base += 3
            if attacker_personality.get("Chaotic", 0) >= 1:
                base += random.randint(0, 5)

        pb = personality_bonus_for_player()
        if attacker.name == "MC":
            base += pb["crit"]

        return max(0, min(50, base))


    def calculate_damage(attacker, defender, flat_bonus=0, attacker_personality=None):
        base = attacker.strength + roll("1d6") + flat_bonus
        reduction = (defender.constitution + defender.temp_defense) // 2

        if attacker_personality:
            if attacker_personality.get("Selfish", 0) >= 3:
                base += 2

        pb = personality_bonus_for_player()
        if attacker.name == "MC":
            base += pb["damage"]
            reduction += pb["defense"]

        dmg = max(1, base - reduction)
        return dmg


    def perform_attack(attacker, defender, attacker_personality=None):
        hit_roll = random.randint(1, 100)
        hit_chance = get_hit_chance(attacker, defender, attacker_personality)

        if hit_roll > hit_chance:
            return False, 0, False

        crit_roll = random.randint(1, 100)
        crit_chance = get_crit_chance(attacker, attacker_personality)
        crit = crit_roll <= crit_chance

        dmg = calculate_damage(attacker, defender, attacker_personality=attacker_personality)
        if crit:
            dmg = int(dmg * 1.5)

        defender.hp = max(0, defender.hp - dmg)
        return True, dmg, crit


    # ---------- AP / FATIGUE / MOMENTUM ----------

    def get_ap_for_turn(turn_count):
        ap = base_ap_per_turn

        if turn_count >= fatigue_start_turn:
            ap -= (turn_count - fatigue_start_turn + 1)

        ap = max(min_ap_per_turn, ap)
        ap = min(max_ap_per_turn, ap)

        return ap


    def apply_momentum(current_ap, crit_happened):
        if crit_happened:
            current_ap += 1
        return min(current_ap, max_ap_per_turn)


    # ---------- LEVELING (PLAYER ONLY) ----------

    def gain_xp(amount):
        global player_xp, player_level, xp_to_next_level, stat_points

        player_xp += amount

        msg = f"You gained {amount} XP."

        while player_xp >= xp_to_next_level:
            player_xp -= xp_to_next_level
            player_level += 1
            xp_to_next_level = int(xp_to_next_level * 1.5)
            stat_points += stat_points_per_level
            msg += f"\nYou leveled up! Now level {player_level}."

        return msg


    # =========================================================
    # ABILITIES — PLAYER, ALLIES, ENEMIES (SIMPLE SET)
    # =========================================================

    # For brevity, we’ll define a few generic abilities used by allies/enemies.
    # You can expand this list with your branch-specific ones later.

    def ability_basic_attack(attacker, defender, ap_cost=2, personality=None):
        hit, dmg, crit = perform_attack(attacker, defender, personality)
        if not hit:
            return "The attack misses.", 0, crit, 0, 0, ap_cost
        return f"{attacker.name} hits {defender.name} for {dmg} damage.", dmg, crit, 0, 0, ap_cost

    def ability_heavy_smash(attacker, defender, personality=None):
        dmg = calculate_damage(attacker, defender, flat_bonus=4, attacker_personality=personality)
        defender.hp -= dmg
        return f"{attacker.name} uses Heavy Smash for {dmg} damage!", dmg, False, 0, 0, 3

    def ability_magic_bolt(attacker, defender, personality=None):
        dmg = 6 + attacker.charisma + roll("1d6")
        defender.hp -= dmg
        return f"{attacker.name} casts Magic Bolt for {dmg} damage!", dmg, False, 0, 0, 3

    def ability_guard(attacker):
        attacker.temp_defense += 5
        return f"{attacker.name} raises their guard.", 0, False, 0, 0, 2

    def ability_ap_drain(attacker, defender, drain_amount=2, personality=None):
        dmg = calculate_damage(attacker, defender, flat_bonus=2, attacker_personality=personality)
        defender.hp -= dmg
        return f"{attacker.name} drains {drain_amount} AP and deals {dmg} damage!", dmg, False, 0, drain_amount, 4

    # Map ability keys to functions for allies/enemies
    ABILITY_MAP = {
        "basic_attack": ability_basic_attack,
        "heavy_smash": ability_heavy_smash,
        "magic_bolt": ability_magic_bolt,
        "guard": ability_guard,
        "ap_drain": ability_ap_drain,
    }


    # =========================================================
    # ENEMY AI (ADVANCED-ish BUT COMPACT)
    # =========================================================

    def enemy_choose_action(enemy, player, ally, current_ap):
        """
        enemy: Enemy object
        player: Fighter (MC)
        ally: Ally or None
        current_ap: enemy.ap
        Returns: (log_message, new_ap)
        """

        # Simple personality-based behavior

        # If low HP, defensive
        if enemy.hp <= enemy.max_hp * 0.3 and current_ap >= 2:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_guard(enemy)
            current_ap -= cost
            return msg, current_ap

        # If Support enemy and ally exists, sometimes buff/debuff
        if enemy.enemy_class == "Support" and current_ap >= 4:
            # Use AP drain on player
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_ap_drain(enemy, player, drain_amount=2)
            current_ap -= cost
            # AP drain would be applied in combat loop
            return msg, current_ap

        # If Caster, use magic
        if enemy.enemy_class == "Caster" and current_ap >= 3:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_magic_bolt(enemy, player)
            current_ap -= cost
            return msg, current_ap

        # Default: basic attack on highest threat (player > ally)
        target = player
        if ally and ally.is_alive():
            # crude threat: higher STR + AP
            player_threat = player.strength + player.dexterity + player.charisma
            ally_threat = ally.strength + ally.dexterity + ally.charisma
            if ally_threat > player_threat:
                target = ally

        if current_ap >= 2:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_basic_attack(enemy, target)
            current_ap -= cost
            return msg, current_ap

        return f"{enemy.name} is too exhausted to act.", current_ap


    # =========================================================
    # ALLY AI (PERSONA-STYLE, ONE ACTION PER TURN)
    # =========================================================

    def ally_choose_action(ally, player, enemies, current_ap):
        """
        ally: Ally object
        player: Fighter (MC)
        enemies: list of Enemy
        current_ap: ally.ap
        Returns: (log_message, new_ap)
        """

        if not enemies:
            return f"{ally.name} has no targets.", current_ap

        # Priority 1: survival
        if ally.hp <= ally.max_hp * 0.3 and current_ap >= 2:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_guard(ally)
            current_ap -= cost
            return msg, current_ap

        # Priority 2: protect MC if MC is low HP
        if player.hp <= player.max_hp * 0.4 and current_ap >= 4:
            # Use AP drain on the most dangerous enemy
            target = max(enemies, key=lambda e: e.strength + e.dexterity + e.charisma)
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_ap_drain(ally, target, drain_amount=2, personality=ally.personality)
            current_ap -= cost
            return msg, current_ap

        # Priority 3: damage — pick weakest enemy
        target = min(enemies, key=lambda e: e.hp)
        if current_ap >= 3 and "heavy_smash" in ally.abilities:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_heavy_smash(ally, target, personality=ally.personality)
            current_ap -= cost
            return msg, current_ap

        if current_ap >= 2:
            msg, dmg, crit, ap_refund, ap_drain, cost = ability_basic_attack(ally, target, personality=ally.personality)
            current_ap -= cost
            return msg, current_ap

        return f"{ally.name} is too exhausted to act.", current_ap


    # =========================================================
    # SIMPLE ALLY ROSTER SETUP (EXAMPLE)
    # =========================================================

    def setup_default_ally_roster():
        global ally_roster

        # Example allies — you can replace with story-driven unlocks
        nora = Ally(
            name="Nora",
            class_type="Rogue",
            branch="Assassin",
            personality={"Confident": 2, "Selfish": 1},
            stats={"hp": 18, "Strength": 7, "Dexterity": 10, "Constitution": 7, "Charisma": 6},
            abilities=["basic_attack", "heavy_smash"],
            passives=["Loyal"]
        )

        malik = Ally(
            name="Malik",
            class_type="Warrior",
            branch="Berserker",
            personality={"Confident": 3, "Selfish": 2},
            stats={"hp": 22, "Strength": 10, "Dexterity": 7, "Constitution": 9, "Charisma": 5},
            abilities=["basic_attack", "heavy_smash"],
            passives=["Chaotic"]
        )

        jess = Ally(
            name="Jess",
            class_type="Sorcerer",
            branch="Enchanter",
            personality={"Caring": 3},
            stats={"hp": 16, "Strength": 5, "Dexterity": 7, "Constitution": 6, "Charisma": 11},
            abilities=["magic_bolt", "ap_drain"],
            passives=["Protective"]
        )

        ally_roster = [nora, malik, jess]


    # =========================================================
    # ENEMY PARTY SETUP (EXAMPLE)
    # =========================================================

    def setup_enemy_party(num_enemies=2):
        global enemy_party

        enemy_party = []

        # Example: mix of Bruiser and Caster
        bully = Enemy(
            name="Dorm Bruiser",
            enemy_class="Bruiser",
            personality="Aggressive",
            stats={"hp": 24, "Strength": 9, "Dexterity": 5, "Constitution": 8, "Charisma": 3},
            abilities=["basic_attack", "heavy_smash"],
            passives=["Rage"]
        )

        mage = Enemy(
            name="Campus Caster",
            enemy_class="Caster",
            personality="Calculated",
            stats={"hp": 20, "Strength": 4, "Dexterity": 6, "Constitution": 5, "Charisma": 10},
            abilities=["magic_bolt", "ap_drain"],
            passives=["Arcane Shield"]
        )

        enemy_party.append(bully)
        if num_enemies > 1:
            enemy_party.append(mage)


# =========================================================
# UI — COMBAT SCREEN (PLAYER + OPTIONAL ALLY + MULTIPLE ENEMIES)
# =========================================================

screen combat_screen(player, ally, enemies):

    modal True

    frame:
        vbox:
            spacing 20

            hbox:
                spacing 40

                vbox:
                    text "[player.name] (Lv [player_level])"
                    bar value player.hp range player.max_hp
                    text "[player.hp] / [player.max_hp] HP"
                    text "AP: [player_ap]"

                if ally:
                    vbox:
                        text "[ally.name] (Ally)"
                        bar value ally.hp range ally.max_hp
                        text "[ally.hp] / [ally.max_hp] HP"
                        text "AP: [ally.ap]"

                vbox:
                    text "Enemies"
                    for e in enemies:
                        text "[e.name]"
                        bar value e.hp range e.max_hp
                        text "[e.hp] / [e.max_hp] HP"
                        text "AP: [e.ap]"

            text "[combat_log]" xalign 0.5

            hbox:
                spacing 10

                # Simple player options (you can plug in your full ability set here)
                if player_ap >= 2:
                    textbutton "Basic Attack (2 AP)" action SetVariable("combat_choice", "basic_attack")
                if player_ap >= 3:
                    textbutton "Guard (3 AP)" action SetVariable("combat_choice", "guard")
                if player_ap >= 4:
                    textbutton "AP Drain (4 AP)" action SetVariable("combat_choice", "ap_drain")

                textbutton "End Turn" action SetVariable("combat_choice", "end_turn")


# =========================================================
# CONDITIONAL ALLY CHOICE SCREEN
# =========================================================

screen ally_choice_screen:

    modal True

    frame:
        vbox:
            spacing 15
            text "Multiple enemies detected. Do you want backup?"

            textbutton "Fight Solo" action [SetVariable("active_ally", None), Return("solo")]

            if ally_roster:
                text "Choose an ally:"
                for a in ally_roster:
                    textbutton "[a.name] ([a.class_type] — [a.branch])" action [SetVariable("active_ally", a), Return("ally")]


# =========================================================
# MAIN COMBAT LABEL — MULTI-ENEMY + CONDITIONAL ALLY
# =========================================================

label campus_fight_multi:

    # Setup player
    $ player = Fighter(
        "MC",
        hp=20,
        strength=player_stats["Strength"],
        dexterity=player_stats["Dexterity"],
        constitution=player_stats["Constitution"],
        charisma=player_stats["Charisma"]
    )

    # Setup ally roster (example)
    $ setup_default_ally_roster()

    # Setup enemy party (2 enemies for demo)
    $ setup_enemy_party(num_enemies=2)

    # Decide if ally is allowed (only if more than one enemy)
    if len(enemy_party) > 1:
        call screen ally_choice_screen
        if _return == "solo":
            $ active_ally = None
        elif _return == "ally":
            pass
    else:
        $ active_ally = None

    $ turn_count = 0
    $ combat_log = "The fight begins."

    while player.is_alive() and any(e.is_alive() for e in enemy_party):

        # Reset temp defense
        $ player.temp_defense = 0
        if active_ally:
            $ active_ally.temp_defense = 0
        for e in enemy_party:
            $ e.temp_defense = 0

        # AP for this turn
        $ turn_count += 1
        $ player_ap = get_ap_for_turn(turn_count)
        if active_ally:
            $ active_ally.ap = get_ap_for_turn(turn_count)
        for e in enemy_party:
            $ e.ap = get_ap_for_turn(turn_count)

        # ---------- PLAYER TURN ----------

        while player_ap > 0 and any(e.is_alive() for e in enemy_party):

            $ combat_choice = None
            call screen combat_screen(player, active_ally, enemy_party)

            if combat_choice == "basic_attack":
                # Target weakest enemy
                $ target = min([e for e in enemy_party if e.is_alive()], key=lambda x: x.hp)
                $ msg, dmg, crit, ap_refund, ap_drain, cost = ability_basic_attack(player, target)
                $ player_ap -= cost
                $ player_ap = apply_momentum(player_ap, crit)
                $ combat_log = msg

            elif combat_choice == "guard":
                $ msg, dmg, crit, ap_refund, ap_drain, cost = ability_guard(player)
                $ player_ap -= cost
                $ combat_log = msg

            elif combat_choice == "ap_drain":
                $ target = max([e for e in enemy_party if e.is_alive()], key=lambda x: x.strength + x.dexterity + x.charisma)
                $ msg, dmg, crit, ap_refund, ap_drain, cost = ability_ap_drain(player, target, drain_amount=2)
                $ player_ap -= cost
                $ combat_log = msg
                # Apply AP drain to target
                $ target.ap = max(0, target.ap - ap_drain)

            elif combat_choice == "end_turn":
                $ combat_log = "You end your turn."
                $ player_ap = 0

            else:
                $ combat_log = "You hesitate, doing nothing."
                $ player_ap = 0

            if not any(e.is_alive() for e in enemy_party):
                jump combat_win_multi

        # ---------- ALLY TURN (IF PRESENT) ----------

        if active_ally and active_ally.is_alive():

            while active_ally.ap > 0 and any(e.is_alive() for e in enemy_party):

                $ msg, new_ap = ally_choose_action(active_ally, player, [e for e in enemy_party if e.is_alive()], active_ally.ap)
                $ active_ally.ap = new_ap
                $ combat_log = combat_log + "\n" + msg

                if not any(e.is_alive() for e in enemy_party):
                    jump combat_win_multi

                # Ally acts only once per turn for simplicity
                $ active_ally.ap = 0

        # ---------- ENEMY TURN ----------

        for e in enemy_party:
            if not e.is_alive():
                continue

            while e.ap > 0 and player.is_alive():

                $ msg, new_ap = enemy_choose_action(e, player, active_ally, e.ap)
                $ e.ap = new_ap
                $ combat_log = combat_log + "\n" + msg

                if not player.is_alive():
                    jump combat_lose_multi

                # Each enemy acts once per turn for simplicity
                $ e.ap = 0

        if not player.is_alive():
            jump combat_lose_multi
        if not any(e.is_alive() for e in enemy_party):
            jump combat_win_multi

    return


label combat_win_multi:
    $ xp_msg = gain_xp(60)
    "You win the fight. The hallway feels a little safer."
    "[xp_msg]"
    return


label combat_lose_multi:
    "You lose the fight. Someone is definitely going to post this on the campus meme page."
    return








