
# reputation.rpy

default campus_reputation = {
    "global": 50,  # 0–100 scale
    "tags": {
        "cheater": 0,
        "heartbreaker": 0,
        "player": 0,
        "loyal": 0,
    }
}


init python:
    def update_reputation(amount, tag=None):
        # Update global reputation
        campus_reputation["global"] = max(0, min(100, campus_reputation["global"] + amount))

        # Update tag if provided
        if tag:
            campus_reputation["tags"][tag] = campus_reputation["tags"].get(tag, 0) + 1

        # Trigger event hook
        romance_events.trigger(
            "on_reputation_change",
            amount=amount,
            tag=tag,
            new_value=campus_reputation["global"]
        )


