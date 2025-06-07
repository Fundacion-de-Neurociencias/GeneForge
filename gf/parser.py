from collections import deque
import re

def parse_tokens(lines):
    tokens = []
    stack = deque()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        indent = len(line) - len(line.lstrip())

        token = {"indent": indent, "line": stripped, "attrs": {}}
        keyval = re.match(r'(\w+):\s*"(.*?)"(?:,\s*(.*))?', stripped)
        if keyval:
            key, val, rest = keyval.groups()
            token["key"] = key
            token["attrs"][key] = val
            if rest:
                extra = re.findall(r'(\w+):\s*"(.*?)"', rest)
                for ek, ev in extra:
                    token["attrs"][ek] = ev

        while stack and indent <= stack[-1]["indent"]:
            stack.pop()
        if stack:
            parent = stack[-1]
            if "children" not in parent:
                parent["children"] = []
            parent["children"].append(token)
        else:
            tokens.append(token)

        stack.append(token)

    return {"tokens": tokens}
