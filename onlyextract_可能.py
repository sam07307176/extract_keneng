import re

with open("./ke_neng_raw.txt", mode='r', encoding="utf-8") as f:
    dataLIST = f.readlines()

nonewline_data = re.sub(r'\n', "", "".join(dataLIST))

no_space_data = re.sub(r'\s+', "", "".join(nonewline_data))

print(no_space_data)

keyword =  r"(?<!\[)可能.*?"
pattern = re.compile(keyword)
matched_sentences = []
for line in dataLIST:
    match = pattern.search(line)
    if match:
        matched_sentences.append(match.group())


for sentence in matched_sentences:
    print(sentence) 