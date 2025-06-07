def fix_gfl_file(filepath):
    with open(filepath, "r", encoding="utf8") as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        line = line.rstrip()
        line = line.replace('""', '"').replace('", "', '", "')
        fixed_lines.append(line)

    return "\n".join(fixed_lines)
