def predict_crista_score(sequence: str) -> float:
    """
    Placeholder para predicción CRISTA.
    Basada en modelo de regresión sobre características moleculares.
    """
    gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence)
    return round(0.5 + 0.3 * gc_content, 3)
