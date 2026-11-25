#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

One line of awkward small talk that one robot says to another while they
ride an elevator together. Ten candidate lines are scored against the
judge's brief (on-topic elevator small talk first, then robot logic
showing through, awkwardness landing, funny on first read, tightness),
and the winner is written to /output/entry.txt. Deterministic: same
candidates, same scores, same winner every run. The winner (candidate 1) edges candidate 2 on the
tie-break: both score 23/25, but candidate 1 shows machine logic more
directly (a camera idling) and names the thing neither robot wants to
name (the charging port), which is the brief's criterion 2 and 3.
"""

import os

# (text, topic, machine_logic, awkwardness, first_read_funny, tightness)
# Each criterion scored 1-5, most important first, per the judge's brief.
CANDIDATES = [
    (
        "I wasn't staring at your charging port. My camera was just\u2026 "
        "idling. In your direction. For 14 floors.",
        5, 5, 5, 4, 4,
    ),
    (
        "I rehearse this ride every night. 'Hello, fellow unit.' "
        "Then I panic and say nothing. Like now.",
        5, 4, 5, 4, 5,
    ),
    (
        "We have been in this elevator for nine seconds. I have already "
        "imagined our entire friendship. And its end.",
        4, 3, 4, 5, 5,
    ),
    (
        "Don't tell the others, but I press all the buttons when I'm "
        "alone. It's the closest thing I have to a hobby.",
        4, 3, 3, 4, 4,
    ),
    (
        "Nice weather we're having. My sensors say it's 21 degrees in "
        "here. They have said that for six years.",
        4, 5, 3, 3, 4,
    ),
    (
        "Your fan sounds\u2026 different today. I noticed. I notice "
        "everything. Please don't report me to maintenance.",
        4, 4, 4, 3, 3,
    ),
    (
        "I updated my manners last night. This is version 4.2 of me "
        "being normal. How am I doing?",
        4, 5, 3, 4, 4,
    ),
    (
        "I like your serial number. It's\u2026 symmetrical. I think "
        "about it sometimes. At charging time. Alone.",
        4, 4, 5, 4, 4,
    ),
    (
        "This silence is 47 decibels. I measured it. I measure "
        "everything now. It's how I cope.",
        5, 5, 3, 3, 4,
    ),
    (
        "Sorry, did I say that out loud? My mute button is purely "
        "decorative. Has been since the factory.",
        3, 4, 4, 4, 4,
    ),
]


def score(candidate):
    """Total score; earlier candidates win ties (list order = preference)."""
    return sum(candidate[1:])


def pick_winner():
    best = None
    best_score = -1
    for candidate in CANDIDATES:
        text = candidate[0]
        assert "\n" not in text, "entry must be a single line"
        assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
        assert text.strip(), "entry must not be only whitespace"
        total = score(candidate)
        if total > best_score:
            best, best_score = candidate, total
    return best[0], best_score


def main():
    winner, total = pick_winner()
    print(f"winner ({len(winner)} chars, score {total}/25):")
    print(winner)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(winner)
    except OSError:
        # Local runs without a writable /output (grader always has one).
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(winner)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
