SCHEMAS = {
    "gene_edit": {
        "required": ["type", "target_gene"],
        "optional": []
    },
    "construct": {
        "required": ["name", "elements"],
        "optional": []
    },
    "enhanced_construct": {
        "required": [],
        "optional": ["marker", "promoter"]
    }
}
