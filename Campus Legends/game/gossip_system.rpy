

default gossip_level = 0  # 0–100

init python:
    def spread_gossip(severity):
        global gossip_level

        # Gossip grows faster with higher severity
        gossip_level = min(100, gossip_level + severity * 2)

        # Reputation drops as gossip spreads
        if gossip_level >= 20:
            update_reputation(-2, tag="player")
        if gossip_level >= 40:
            update_reputation(-3, tag="heartbreaker")
        if gossip_level >= 70:
            update_reputation(-5, tag="cheater")
