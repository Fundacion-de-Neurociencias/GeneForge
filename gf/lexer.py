def tokenize(code):
    # Separador simple por líneas y eliminación de comentarios
    lines = code.splitlines()
    tokens = []
    for line in lines:
        clean = line.strip()
        if clean and not clean.startswith('#'):
            tokens.append(clean)
    return tokens
