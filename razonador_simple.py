import json

def buscar_offtarget(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            buscar_offtarget(v)
    elif isinstance(obj, list):
        for elem in obj:
            buscar_offtarget(elem)
    elif isinstance(obj, str) and obj.startswith('offtarget:'):
        try:
            score = float(obj.split(':')[1])
            if score >= 0.8:
                print(f'ALERTA: Riesgo off-target alto ({score})')
        except Exception:
            pass

with open('parse_gfl_struct_ascii_clean.pyout', encoding='ascii') as f:
    data = json.load(f)

print('ANALISIS DE ESTRATEGIA GENETICA:')
print(data)
buscar_offtarget(data)
