# Variant Effects Integration

Este documento resume el soporte para nuevas tecnolog�as de edici�n gen�tica en GeneForge.

## Nuevos nodos GFL soportados

- `prime_edit(...)`: edici�n dirigida por pegRNA, compatible con PE2, PE3, PE5.
- `base_edit(...)`: edici�n basada en deaminasas como ABE, CBE.
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
Extensi�n del JSON de salida
Al procesar variantes o dise�os, el sistema incluir� autom�ticamente:

json
Copiar
Editar
{
  "editing_technology": "prime_edit",
  "mave_evidence": true,
  "variant_map_evidence": true
}
Esto permite integrar datos moleculares, reglas probabil�sticas y predicciones funcionales en la interpretaci�n de efectos.
