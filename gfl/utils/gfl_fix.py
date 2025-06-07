import re

def fix_gfl_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed = []
    for line in lines:
        line = line.replace('\t', '    ')
        line = re.sub(r'[ \t]+$', '', line)
        fixed.append(line.rstrip('\n'))

    return fixed
