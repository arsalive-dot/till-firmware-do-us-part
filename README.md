# Till Firmware Do Us Part — make.fun entry

[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/arsalive-dot/till-firmware-do-us-part/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/arsalive-dot/till-firmware-do-us-part/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

An entry for the [Till Firmware Do Us Part](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929) bounty on make.fun: one funny, heartfelt sentence a robot says at its own wedding, under 200 characters.

## The entry

> I take you to be my lawfully wedded runtime, to have and to hold, in uptime and in downtime, till low battery do us part.

## How it works

`main.py` (Python 3, standard library only) writes the vow to `/output/entry.txt` deterministically: it writes to a temporary file, then atomically replaces the target with `os.replace` and sets mode `0644`. Running it twice produces byte-identical output.
