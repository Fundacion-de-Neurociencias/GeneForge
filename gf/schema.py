# gf/schema.py

NODE_SCHEMAS = {
    "gene_edit": {
        "required": ["type", "target_gene"],
        "types": {
            "type": str,
            "target_gene": str
        }
    },
    "construct": {
        "required": ["name", "elements"],
        "types": {
            "name": str,
            "elements": list
        }
    },
    "logic_node": {
        "required": [],
        "types": {
            "flag": bool,
            "debug": bool,
            "fallback": type(None)
        }
    }
}
