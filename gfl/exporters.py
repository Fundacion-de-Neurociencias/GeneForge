import json
import yaml

def ast_to_vcf(ast):
    vcf_lines = [
        "##fileformat=VCFv4.2",
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"
    ]
    for node in ast:
        kind, params = node
        info = ";".join([f"{k}={v}" for k, v in params.items()])
        vcf_lines.append(f"chr1\t1000\t.\tN\tN\t.\t.\t{info}")
    return "\n".join(vcf_lines)

def ast_to_json(ast):
    return json.dumps(ast, indent=2)

def ast_to_gff(ast):
    gff_lines = [
        "##gff-version 3"
    ]
    for node in ast:
        kind, params = node
        attributes = ";".join([f"{k}={v}" for k, v in params.items()])
        gff_lines.append(f"chr1\tGeneForge\t{kind}\t1\t1000\t.\t+\t.\t{attributes}")
    return "\n".join(gff_lines)

def ast_to_yaml(ast):
    return yaml.dump(ast, sort_keys=False, allow_unicode=True)
