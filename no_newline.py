import re

with open("./ke_neng_raw.txt", mode='r', encoding="utf-8") as f:
    dataLIST = f.readlines()

nonewline_data = re.sub(r'\n', "", "".join(dataLIST))

print(nonewline_data)