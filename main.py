import os

TEXT = (
    "You have read so many words today. This one is slow. "
    "Somewhere rain is tapping on a tin roof, drop by drop. "
    "A river is carrying one leaf a little further, "
    "and a little further. And the night is still going on, "
    "wide and unhurried, asking nothing of you."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
