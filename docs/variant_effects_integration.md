# Variant Effects Integration

Este documento resume el soporte para nuevas tecnologías de edición genética en GeneForge.

## Nuevos nodos GFL soportados

- `prime_edit(...)`: edición dirigida por pegRNA, compatible con PE2, PE3, PE5.
- `base_edit(...)`: edición basada en deaminasas como ABE, CBE.
- `prime_del(...)`: permite especificar pares de pegRNAs para deleciones dirigidas.

## Ejemplos de sintaxis GFL

```gfl
prime_edit(
  target = "HBB:c.20A>T",
  pegRNA = peg(pbs = "ATCG", rtt = "TTAGG", nick_site = +17),
  reverse_transcriptase = "PEmax"
)

base_edit(
  target = "PCSK9:g.1120C>T",
  base_editor = "ABE8e",
  mode = "A>G",
  vector = "LNP"
)
Extensión del JSON de salida
Al procesar variantes o diseños, el sistema incluirá automáticamente:

json
Copiar
Editar
{
  "editing_technology": "prime_edit",
  "mave_evidence": true,
  "variant_map_evidence": true
}
Esto permite integrar datos moleculares, reglas probabilísticas y predicciones funcionales en la interpretación de efectos.
