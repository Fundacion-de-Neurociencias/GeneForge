def load_gfl_string(code):
    print("🔍 Splitting code...")
    lines = code.splitlines()
    print(f"🔍 Lines: {lines}")

    tokens = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        tokens.append({"line": stripped})

    return {"tokens": tokens}
