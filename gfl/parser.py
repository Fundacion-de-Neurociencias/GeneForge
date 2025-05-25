# gfl/parser.py
import re
import json
from typing import Any, Dict, List

class GFLParseError(Exception):
    pass

class GFLNode:
    def __init__(self, type_: str, attributes: Dict[str, Any], children: List[Any] = None):
        self.type = type_
        self.attributes = attributes
        self.children = children or []

    def to_dict(self):
        return {
            'type': self.type,
            'attributes': self.attributes,
            'children': [child.to_dict() for child in self.children]
        }

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=2)

class GFLParser:
    def __init__(self):
        self.patterns = {
            'edit': re.compile(r"edit\(([^)]+)\)"),
            'target': re.compile(r"target\(([^:]+):([^)]+)\)"),
            'effect': re.compile(r"effect\(([^:]+):([^)]+)\)"),
            'pathway': re.compile(r"pathway\(([^:]+):([^)]+)\)"),
            'link': re.compile(r"link\(([^-]+)->([^)]+)\)")
        }

    def parse_line(self, line: str) -> GFLNode:
        line = line.strip()
        for type_, pattern in self.patterns.items():
            match = pattern.match(line)
            if match:
                if type_ in ('target', 'effect', 'pathway'):
                    return GFLNode(type_, {'key': match.group(1).strip(), 'value': match.group(2).strip()})
                elif type_ == 'link':
                    return GFLNode(type_, {'from': match.group(1).strip(), 'to': match.group(2).strip()})
                else:
                    return GFLNode(type_, {'value': match.group(1).strip()})
        raise GFLParseError(f"Syntax error: {line}")

    def parse(self, text: str) -> GFLNode:
        lines = text.strip().split('\n')
        root = GFLNode("program", {})
        for line in lines:
            if not line.strip():
                continue
            node = self.parse_line(line)
            root.children.append(node)
        return root

if __name__ == '__main__':
    example = """
    edit(SNP:rs12345)
    target(gene:TP53)
    effect(function:loss_of_function)
    pathway(p53:apoptosis)
    link(edit->target)
    link(target->effect)
    """
    parser = GFLParser()
    tree = parser.parse(example)
    print(tree)
```
