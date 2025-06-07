class GFLNode:
    def __init__(self, node_type, attrs):
        self.type = node_type
        self.attrs = attrs

    def __repr__(self):
        return f"<GFLNode type={self.type} attrs={self.attrs}>"

    @classmethod
    def from_dict(cls, node_dict):
        return cls(node_dict["type"], node_dict["attrs"])

def validate_ast(nodes):
    if not isinstance(nodes, list):
        nodes = [nodes]

    for node in nodes:
        if not hasattr(node, "type"):
            raise TypeError(f"Invalid node: {node}")

        if node.type == "gene_strategy":
            for k in ["objective", "steps", "validation"]:
                if k not in node.attrs:
                    raise ValueError(f"Missing {k} in gene_strategy")

        elif node.type == "strategic_plan":
            for k in ["goal", "steps", "evaluation_criteria"]:
                if k not in node.attrs:
                    raise ValueError(f"Missing {k} in strategic_plan")
            for step in node.attrs["steps"]:
                if not isinstance(step, dict) or "name" not in step or "method" not in step:
                    raise ValueError("Each step must have 'name' and 'method'")

        elif node.type == "chain_of_thought":
            if "goal" not in node.attrs or "steps" not in node.attrs:
                raise ValueError("Missing 'goal' or 'steps' in chain_of_thought")
            valid_ids = set()
            for step in node.attrs["steps"]:
                if not isinstance(step, dict):
                    raise TypeError("Each step in chain_of_thought must be a dict")
                if "id" in step:
                    valid_ids.add(step["id"])
                keys = set(step.keys())
                if keys & {"thought", "conclusion"}:
                    continue
                elif keys >= {"condition", "retry"}:
                    if step["retry"] not in valid_ids:
                        raise ValueError(f"Retry refers to unknown id '{step['retry']}'")
                elif "eval" in step:
                    continue
                else:
                    raise ValueError(f"Step not valid: {step}")
            if "evaluation" in node.attrs and not isinstance(node.attrs["evaluation"], list):
                raise TypeError("'evaluation' must be a list in chain_of_thought")

        elif node.type == "feedback_loop":
            if "condition" not in node.attrs or "strategy" not in node.attrs or "max_iterations" not in node.attrs:
                raise ValueError("Missing one of 'condition', 'strategy', or 'max_iterations' in feedback_loop")

            if not isinstance(node.attrs["condition"], str):
                raise TypeError("'condition' must be a string in feedback_loop")

            if not isinstance(node.attrs["max_iterations"], int) or node.attrs["max_iterations"] <= 0:
                raise TypeError("'max_iterations' must be a positive integer in feedback_loop")

            subnode = node.attrs["strategy"]
            if isinstance(subnode, dict):
                subnode = GFLNode.from_dict(subnode)
            validate_ast(subnode)

        else:
            raise ValueError(f"Unknown node type: {node.type}")
