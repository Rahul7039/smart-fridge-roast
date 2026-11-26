"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes the chosen roast line, byte-identical, to /output/entry.txt.
The line is a fixed constant; it is never generated or paraphrased.
"""

LINE = "My smart fridge texts my doctor every time I open it after midnight — even my leftovers have a snitch now."

assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip() == LINE, "line must not be only whitespace"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
