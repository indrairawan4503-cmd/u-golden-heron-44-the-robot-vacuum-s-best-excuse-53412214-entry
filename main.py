#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — variant C (SENSOR-AND-CAT).

Writes one line to /output/entry.txt: the vacuum's deadpan excuse for
missing a spot, blaming the cat's squatters' rights.

Concept iteration log (ONE concept family: SENSOR-AND-CAT, v1-v8):

v1: "My cliff sensor flagged that spot as a void, and I do not argue with a void."
    (76 chars) DROPPED: too short, the turn is a shrug, no concrete scene.
v2: "The cat claimed that spot before I arrived, and I respect squatters' rights."
    (76 chars) KEPT the concept, DROPPED the line: under budget, punchline
    arrives too early and there is no vacuum action in it.
v3: "The cat claimed that spot before I arrived, so under squatters' rights I
    vacuumed around her and let her keep the dust." (119 chars) KEPT: full
    scene, turn lands on "keep the dust"; DROPPED as final: "before I
    arrived" is flat, no vacuum-log flavour.
v4: "My bumper negotiated a treaty with the chair leg, and under its terms the
    corner stays dirty until further notice." (114 chars) RUNNER-UP: strong
    bureaucratic deadpan, rooted in the bumper; LOST: the cat scene is more
    visual and funnier than furniture diplomacy.
v5: "My cliff sensor read that spot as a sheer drop, so I treated it as a cliff
    and let it keep its dust out of respect." (115 chars) DROPPED: "out of
    respect" is vague and the sensor excuse repeats the word cliff.
v6: "The cat sat on that spot before I arrived, and under squatters' rights I
    am legally required to vacuum around her." (114 chars) KEPT: "legally
    required" is great deadpan; DROPPED: ends on procedure, not on the dust.
v7: "The cat claimed that spot at 09:00 sharp, and under squatters' rights I
    vacuumed around her and let her keep the dust." (118 chars) KEPT: the
    timestamp adds vacuum-log specificity; DROPPED as final: "claimed" is
    less physical than "sat on".
v8: "The cat sat on that spot at 09:00 sharp, and under squatters' rights I
    vacuumed around her and let her keep the dust." (117 chars) SHIPPED:
    concrete scene (cat physically on the spot), vacuum-log timestamp,
    bureaucratic "squatters' rights", and the turn lands on the last words:
    the dust — the one thing the vacuum was sent to remove — is conceded
    to the cat. Deadpan throughout, one sentence, vacuum's own voice.
"""

import os
import sys

LINE = (
    "The cat sat on that spot at 09:00 sharp, and under squatters' rights "
    "I vacuumed around her and let her keep the dust."
)


def write_output(data: bytes) -> None:
    """Write the entry bytes ONLY to /output/entry.txt.

    Never write to the repo root or any path inside the repo: the
    grader sandbox mounts the repo read-only and a repo-root write
    crashes the run with exit code 1.
    """
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)


def main() -> int:
    # Gate: single line, 1-140 chars, no leading/trailing whitespace,
    # no double spaces, valid UTF-8, ends with a full stop.
    if "\r" in LINE or "\n" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: leading/trailing whitespace", file=sys.stderr)
        return 1
    if "  " in LINE:
        print("error: double space", file=sys.stderr)
        return 1
    if not LINE.endswith("."):
        print("error: line must end with a full stop", file=sys.stderr)
        return 1
    try:
        data = LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    # Write ONLY to /output/entry.txt via the helper above.
    write_output(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
