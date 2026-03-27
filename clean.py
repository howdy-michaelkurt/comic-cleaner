import fitz
import re
import sys

# open pdf & extract text
pdf = fitz.open(sys.argv[1])
text = "\n".join(page.get_text() for page in pdf)

# remove tabs
text = text.replace("\t", "")

# rejoin wrapped lines (if previous line doesn't end with sentence-ending punctuation)
text = re.sub(r"(?<![.!?:])\n(?=[a-z])", " ", text)
text = re.sub(r"(?<=,)\n(?=[A-Z])", " ", text)

# preserve capitolizaed words for character names
text = re.sub(r"\n(?=[A-Z][A-Z])", "\n\n\n", text)

# collapse 3+ newlines down to 2 (keeps intentional blank lines)
text = re.sub(r"\n{3,}", "\n\n", text)

# ensure PAGE headers are breaks
text = re.sub(r"(PAGE \d+)", r"\n---\n\n\1", text)

# write .txt file
output = sys.argv[1].replace(".pdf", "-clean.txt")
with open(output, "w") as f:
    f.write(text.strip() + "\n")

print(f"Done -> {output}")