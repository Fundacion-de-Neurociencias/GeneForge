from gf.parser import parse_tokens

print("🧪 Testing list of dicts in 'subgoals'...\n")

lines = [
    "pathway_plan {",
    "    goal: \"Increase dopamine synthesis\"",
    "    subgoals: [",
    "        { name: \"Upregulate TH\", method: \"CRISPRa\" },",
    "        { name: \"Enhance BH4 availability\", method: \"cofactor supplementation\" }",
    "    ]",
    "    conditions: \"Only in substantia nigra\"",
    "    checkpoints: [\"qPCR for TH\", \"dopamine levels via HPLC\"]",
    "}"
]

tokens = parse_tokens(lines)
for token in tokens:
    print("🔍 Token:", token)
