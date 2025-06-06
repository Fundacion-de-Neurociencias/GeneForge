# 📚 Genetic Forge Schema Definitions with Inheritance and Splicing Support

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
        "extends": "construct",
        "required": [],
        "optional": ["marker", "promoter"]
    },
    "transcript_variant": {
        "required": ["gene", "exons"],
        "optional": ["splicing_pattern", "functional_impact"]
    },
    "protein": {
        "required": ["name", "domains"],
        "optional": ["post_translational_modifications", "localization"]
    },
    "regulatory_element": {
        "required": ["name", "element_type"],
        "optional": ["binding_sites", "strength", "orientation"]
    },
    "genetic_system": {
        "required": ["components", "regulation"],
        "optional": ["output_behavior"]
    }
}

def get_full_schema(node_type):
    base = SCHEMAS.get(node_type)
    if not base:
        return None

    required = list(base.get("required", []))
    optional = list(base.get("optional", []))

    # Handle inheritance
    if "extends" in base:
        parent = get_full_schema(base["extends"])
        if parent:
            required = list(set(required + parent["required"]))
            optional = list(set(optional + parent["optional"]))

    return {
        "required": required,
        "optional": optional
    }
