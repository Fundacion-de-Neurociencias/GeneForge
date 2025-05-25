# integration/HEVisum_connector.py

"""
HEVisum Connector
------------------
This module translates GeneForgeLang (GFL) abstract syntax trees (ASTs) into HEVisum-compatible network inputs
and interprets the outputs to enrich back the AST with network-level inference.
"""

from typing import Dict, Any, List
import json

class HEVisumConnector:
    def __init__(self):
        pass  # Add API credentials or config path if required

    def ast_to_network(self, gfl_ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts GFL AST into a node-edge format suitable for HEVisum visualization or analysis.
        """
        nodes = []
        edges = []

        for node in gfl_ast.get("children", []):
            if node["type"] not in ("link",):
                nodes.append({
                    "id": node["type"] + ":" + node["attributes"].get("value", node["attributes"].get("key", "")),
                    "label": node["type"],
                    "meta": node["attributes"]
                })
            elif node["type"] == "link":
                edges.append({
                    "from": node["attributes"]["from"],
                    "to": node["attributes"]["to"],
                    "type": "causal"
                })

        return {"nodes": nodes, "edges": edges}

    def send_to_hevisum(self, network: Dict[str, Any]) -> str:
        """
        (Placeholder) Sends network to HEVisum system and returns a URL or identifier.
        """
        # Replace with actual POST request to HEVisum server
        print("[DEBUG] Sending network to HEVisum:")
        print(json.dumps(network, indent=2))
        return "https://hevisum.example.org/view/network12345"

    def enrich_ast_with_hevisum(self, gfl_ast: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adds HEVisum-based insights (e.g., centrality, subnetwork) to nodes in AST.
        """
        for node in gfl_ast.get("children", []):
            node["attributes"]["hevisum_score"] = 0.5  # Placeholder for real score
        return gfl_ast

# Example usage
if __name__ == '__main__':
    from gfl.parser import GFLParser
    
    text = """
    edit(SNP:rs123)
    target(gene:TP53)
    effect(function:loss_of_function)
    link(edit->target)
    link(target->effect)
    """
    parser = GFLParser()
    ast = parser.parse(text).to_dict()

    connector = HEVisumConnector()
    net = connector.ast_to_network(ast)
    url = connector.send_to_hevisum(net)
    print("HEVisum URL:", url)

    enriched = connector.enrich_ast_with_hevisum(ast)
    print(json.dumps(enriched, indent=2))
