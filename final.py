import re

with open("./ke_neng_raw.txt", mode='r', encoding="utf-8") as f:
    dataLIST = f.readlines()

nonewline_data = re.sub(r'\n|more', "", "".join(dataLIST))

no_space_data = re.sub(r'\s', "", "".join(nonewline_data))

print(no_space_data)

pattern = re.compile(r'\w*可能\w*')
final = pattern.findall(no_space_data)
print(final)

