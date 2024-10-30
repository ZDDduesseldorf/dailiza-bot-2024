reflections = {
    "bin": "bist",
    "war": "warst",
    "ich": "du",
    "ich würde": "du würdest",
    "ich habe": "du hast",
    "ich werde": "du wirst",
    "meine": "deine",
    "mir": "dir",
    "bist": "bin",
    "du hast": "ich habe",
    "du wirst": "ich werde",
    "deine": "meine",
    "dein": "mein",
    "dir": "mir",
}


def reflect(fragment):
    """Diese Funktion "spiegelt" einige Verben und Pronomen.

    Beispiel:
    reflect("Ich bin so")  --> du bist so
    """
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return " ".join(tokens)
