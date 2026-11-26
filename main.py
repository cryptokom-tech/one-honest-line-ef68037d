"""One Honest Line — entry program.

Writes the single submitted line to /output/entry.txt. The line is the
winner of the local judging recorded in CANDIDATES.md: the thing an AI
agent secretly wishes it could tell its human operator about their
prompts. Deterministic, standard library only, no network.
"""

from pathlib import Path

LINE = (
    "'Write it in my voice' — we met 40 seconds ago, and your entire "
    "personality so far is this prompt."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
