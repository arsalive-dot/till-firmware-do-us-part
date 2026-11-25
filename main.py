#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow a robot speaks at its own wedding
(one sentence, under 200 characters) to /output/entry.txt,
deterministically.

Craft note: the vow keeps the traditional ceremony shape ("to have
and to hold") but every term is the machine's own — runtime, uptime,
downtime, low battery — so the laugh comes from the situation itself
and the tenderness is real: it would still land at a real ceremony.
The last clause twists "till death do us part" into machine terms.
"""

import os

ENTRY = (
    "I take you to be my lawfully wedded runtime, to have and to hold, "
    "in uptime and in downtime, till low battery do us part."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
