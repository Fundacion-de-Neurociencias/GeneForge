import json

def alerta(mensaje):
    print(f"⚠️  {mensaje}")

def main():
    with open("ast_struct.json", encoding="utf8") as f:
        nodes = json.load(f)

    print("\n🧬 ANALISIS DE ESTRATEGIA GENETICA\n")
    alertas = []
    for node in nodes:
        t = node["attrs"].get("type")
        if t == "risk" and "val" in node["attrs"]:
            try:
                val = node["attrs"]["val"]
                # asume formato "offtarget:0.85"
                if "offtarget" in val:
                    score = float(val.split(":")[1])
                    if score >= 0.8:
                        alerta(f"Off-target alto ({score})")
                        alertas.append("Riesgo off-target alto")
            except:
                alerta("Error al parsear riesgo off-target")
        if t == "repeat_edit":
            alerta("Se detectó edición repetida")
            alertas.append("Edición repetida detectada")
        if t == "residue" and node["attrs"].get("label") == "ncAA":
            alerta("Residuo no canónico detectado")
            alertas.append("Residuo ncAA")
        if t == "uaug" and node["attrs"].get("frame") == "1":
            alerta("Inicio alternativo (uAUG, frame 1)")
            alertas.append("uAUG inicio alternativo")
        if t == "structure":
            try:
                dg = float(node["attrs"].get("?G", "0"))
                if dg < -10:
                    alerta(f"Estructura secundaria muy estable (?G={dg})")
                    alertas.append("Estructura secundaria muy estable")
            except:
                alerta("Error al parsear ?G")
        if t == "gc_content":
            try:
                pct = float(node["attrs"].get("pct", "0"))
                if pct < 0.3 or pct > 0.7:
                    alerta(f"Contenido GC fuera de rango ({pct})")
                    alertas.append("GC fuera de rango")
            except:
                alerta("Error al parsear GC")
        if t == "rbp_site" and node["attrs"].get("rbp") == "Pumilio":
            alerta("Sitio RBP: Pumilio detectado")
            alertas.append("RBP Pumilio")
        # Añade reglas para más tipos según necesites

    print("\nResumen final:")
    if alertas:
        for a in set(alertas):
            print(f"- {a}")
    else:
        print("No se detectaron riesgos relevantes.")

if __name__ == "__main__":
    main()
