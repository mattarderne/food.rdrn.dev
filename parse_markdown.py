from pathlib import Path
import re


for fi in Path("_recipes").glob("**/*.md"):
    print(fi.stem)
    with fi.open("r") as f:
        li = f.readlines()
        li.pop(-1)
    ing, met = False, False
    count = 1
    new = []
    for i, l in enumerate(li):
        if l == "ingredients:\n":
            new.extend(["---\n", "\n", "## Ingredients\n"])
            ing = True
        elif l == "method:\n":
            new.extend(["\n", "## Method\n"])
            met = True
        else:
            new.append(l)
    if not (ing and met):
        print("MISTAKE WITH", fi.stem)
    with fi.open("w") as f:
        f.writelines(new)
